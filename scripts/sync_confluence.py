#!/usr/bin/env python3
"""
sync_confluence.py

Export one or more Confluence Cloud spaces to Markdown files for downstream
ingestion (IBL GitHub tool, static-site crawl, RAG index, etc.).

Design notes
------------
* Incremental by default. Each generated file carries the Confluence page
  version number in its YAML frontmatter, so a re-run only fetches bodies for
  pages whose version actually changed. No external state file is needed --
  the committed Markdown *is* the state.
* Deterministic output paths (OUTPUT_DIR/<SPACE>/<page-id>-<slug>.md) so that
  `git diff` between runs is readable and reviewable.
* Orphan cleanup: any file under a managed space directory that was neither
  written nor retained on this run is deleted. That covers page deletions,
  page moves out of scope, and title changes (which shift the slug).

Environment variables
---------------------
CONFLUENCE_BASE    https://<site>.atlassian.net      (required)
CONFLUENCE_CLOUD_ID  cloud ID -- REQUIRED for scoped API tokens, omit for
                     classic unscoped tokens. See notes on API_ROOT below.
CONFLUENCE_EMAIL   account email for the API token   (required)
CONFLUENCE_TOKEN   Atlassian API token               (required)
SPACE_KEYS         comma-separated space keys        (required)
OUTPUT_DIR         output root                       (default: content)
PAGE_STATUS        current | archived                (default: current)
FETCH_LABELS       true | false                      (default: true)
REQUEST_DELAY      seconds between requests          (default: 0.15)
FORCE_FULL         true | false (ignore version cache, default: false)
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import time
import unicodedata
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from requests.auth import HTTPBasicAuth

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("confluence-sync")


def _env(name: str, default: str | None = None, required: bool = False) -> str:
    value = os.environ.get(name, default)
    if required and not value:
        log.error("Missing required environment variable: %s", name)
        sys.exit(1)
    return value or ""


def _env_bool(name: str, default: bool) -> bool:
    return _env(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


BASE = _env("CONFLUENCE_BASE", required=True).rstrip("/")
CLOUD_ID = _env("CONFLUENCE_CLOUD_ID", "").strip()
EMAIL = _env("CONFLUENCE_EMAIL", required=True)
TOKEN = _env("CONFLUENCE_TOKEN", required=True)
SPACE_KEYS = [k.strip() for k in _env("SPACE_KEYS", required=True).split(",") if k.strip()]
OUTPUT_DIR = Path(_env("OUTPUT_DIR", "content"))
PAGE_STATUS = _env("PAGE_STATUS", "current")
FETCH_LABELS = _env_bool("FETCH_LABELS", True)
REQUEST_DELAY = float(_env("REQUEST_DELAY", "0.15"))
FORCE_FULL = _env_bool("FORCE_FULL", False)

# Two different roots, deliberately kept separate:
#
#   API_ROOT -- where requests go. Scoped API tokens MUST use the
#               api.atlassian.com gateway and will 401 against the site URL.
#               Classic (unscoped) tokens use the site URL directly.
#   BASE     -- the human-facing site URL. Always used for source_url in
#               frontmatter and for absolutizing image/link hrefs, because
#               those are for browsers, not for the API.
#
# Set CONFLUENCE_CLOUD_ID to switch to gateway mode. Find it at:
#   https://<site>.atlassian.net/_edge/tenant_info
API_ROOT = f"https://api.atlassian.com/ex/confluence/{CLOUD_ID}" if CLOUD_ID else BASE
API = f"{API_ROOT}/wiki/api/v2"

MAX_RETRIES = 5
MAX_SLUG_LEN = 60


# --------------------------------------------------------------------------
# HTTP layer
# --------------------------------------------------------------------------

def make_session() -> requests.Session:
    session = requests.Session()
    session.auth = HTTPBasicAuth(EMAIL, TOKEN)
    session.headers.update({
        "Accept": "application/json",
        "User-Agent": "su-confluence-sync/1.0 (+Syracuse University ITS)",
    })
    return session


def api_get(session: requests.Session, url: str, params: dict | None = None) -> dict | None:
    """GET with 429/5xx backoff. Returns None on 404."""
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, params=params, timeout=60)
        except requests.RequestException as exc:
            wait = 2 ** attempt
            log.warning("Request error (%s); retrying in %ss", exc, wait)
            time.sleep(wait)
            continue

        if resp.status_code == 429:
            wait = float(resp.headers.get("Retry-After", 2 ** attempt))
            log.warning("Rate limited; sleeping %.1fs", wait)
            time.sleep(wait)
            continue

        if resp.status_code >= 500:
            wait = 2 ** attempt
            log.warning("Server error %s; retrying in %ss", resp.status_code, wait)
            time.sleep(wait)
            continue

        if resp.status_code == 404:
            return None

        if resp.status_code in (401, 403):
            log.error(
                "Auth/permission failure (%s) on %s. Check the API token and that "
                "the service account has read access to this space.",
                resp.status_code, url,
            )
            resp.raise_for_status()

        resp.raise_for_status()
        if REQUEST_DELAY:
            time.sleep(REQUEST_DELAY)
        return resp.json()

    raise RuntimeError(f"Exhausted retries for {url}")


def paginate(session: requests.Session, url: str, params: dict | None = None):
    """Yield results across v2 cursor pagination."""
    payload = api_get(session, url, params)
    while payload:
        yield from payload.get("results", [])
        nxt = (payload.get("_links") or {}).get("next")
        if not nxt:
            break
        # `next` is a root-relative path beginning with /wiki. Concatenate onto
        # API_ROOT -- do NOT use urljoin here: an absolute path would replace
        # the /ex/confluence/{cloudId} prefix and silently break gateway mode.
        payload = api_get(session, nxt if nxt.startswith("http") else API_ROOT + nxt)


# --------------------------------------------------------------------------
# Confluence API helpers
# --------------------------------------------------------------------------

def resolve_spaces(session: requests.Session, keys: list[str]) -> list[dict]:
    found = {}
    for space in paginate(session, f"{API}/spaces", {"keys": ",".join(keys), "limit": 100}):
        found[space["key"]] = space
    for key in keys:
        if key not in found:
            log.warning("Space %r not found or not visible to this account -- skipping", key)
    return [found[k] for k in keys if k in found]


def list_pages(session: requests.Session, space_id: str):
    """Page metadata only (no bodies) -- cheap enumeration."""
    yield from paginate(
        session,
        f"{API}/spaces/{space_id}/pages",
        {"status": PAGE_STATUS, "limit": 250, "sort": "id"},
    )


def get_page_body(session: requests.Session, page_id: str) -> str:
    """export_view renders macros (TOC, excerpt, include) into real HTML."""
    payload = api_get(session, f"{API}/pages/{page_id}", {"body-format": "export_view"})
    if not payload:
        return ""
    return ((payload.get("body") or {}).get("export_view") or {}).get("value", "") or ""


def get_labels(session: requests.Session, page_id: str) -> list[str]:
    if not FETCH_LABELS:
        return []
    try:
        return [lbl["name"] for lbl in paginate(session, f"{API}/pages/{page_id}/labels", {"limit": 100})]
    except Exception as exc:  # labels are nice-to-have, never fatal
        log.debug("Label fetch failed for %s: %s", page_id, exc)
        return []


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------

def absolutize(soup: BeautifulSoup) -> None:
    """Rewrite Confluence-relative hrefs/srcs to absolute URLs."""
    for tag, attr in (("a", "href"), ("img", "src")):
        for el in soup.find_all(tag):
            val = el.get(attr)
            if val and val.startswith("/"):
                el[attr] = BASE + val


def clean_html(raw: str) -> str:
    soup = BeautifulSoup(raw, "html.parser")

    for el in soup(["script", "style"]):
        el.decompose()

    # Confluence chrome that carries no content value
    for cls in ("expand-control", "conf-macro-render-error", "aui-message"):
        for el in soup.select(f".{cls}"):
            el.decompose()

    # Any residual ac:/ri: storage-format elements: keep text, drop the wrapper
    for el in soup.find_all(lambda t: t.name and (":" in t.name)):
        el.unwrap()

    absolutize(soup)
    return str(soup)


def html_to_markdown(raw: str) -> str:
    if not raw.strip():
        return ""
    md = markdownify(
        clean_html(raw),
        heading_style="ATX",
        bullets="-",
        strip=["span", "div"],
    )
    md = re.sub(r"\n{3,}", "\n\n", md)          # collapse blank-line runs
    md = re.sub(r"[ \t]+\n", "\n", md)          # trailing whitespace
    return md.strip() + "\n"


# --------------------------------------------------------------------------
# File layout
# --------------------------------------------------------------------------

def slugify(title: str) -> str:
    norm = unicodedata.normalize("NFKD", title or "").encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", norm).strip("-").lower()
    return (slug[:MAX_SLUG_LEN].rstrip("-")) or "untitled"


def page_path(space_key: str, page: dict) -> Path:
    return OUTPUT_DIR / space_key / f"{page['id']}-{slugify(page.get('title', ''))}.md"


def yaml_scalar(value) -> str:
    """JSON strings are valid YAML double-quoted scalars -- avoids a PyYAML dep."""
    return json.dumps(value, ensure_ascii=False)


def build_frontmatter(page: dict, space: dict, labels: list[str]) -> str:
    version = page.get("version") or {}
    webui = (page.get("_links") or {}).get("webui", "")
    url = f"{BASE}/wiki{webui}" if webui else ""

    lines = [
        "---",
        f"title: {yaml_scalar(page.get('title', ''))}",
        f"confluence_id: {yaml_scalar(str(page['id']))}",
        f"space_key: {yaml_scalar(space['key'])}",
        f"space_name: {yaml_scalar(space.get('name', ''))}",
        f"source_url: {yaml_scalar(url)}",
        f"version: {version.get('number', 0)}",
        f"last_modified: {yaml_scalar(version.get('createdAt', ''))}",
        f"status: {yaml_scalar(page.get('status', ''))}",
    ]
    if page.get("parentId"):
        lines.append(f"parent_id: {yaml_scalar(str(page['parentId']))}")
    if labels:
        lines.append("labels:")
        lines.extend(f"  - {yaml_scalar(lbl)}" for lbl in labels)
    lines.append("---\n")
    return "\n".join(lines)


FM_VERSION_RE = re.compile(r"^version:\s*(\d+)\s*$", re.MULTILINE)


def existing_version(path: Path) -> int | None:
    """Read the cached version number from a previously generated file."""
    try:
        with path.open("r", encoding="utf-8") as fh:
            head = fh.read(2048)
    except OSError:
        return None
    if not head.startswith("---"):
        return None
    match = FM_VERSION_RE.search(head)
    return int(match.group(1)) if match else None


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def sync_space(session: requests.Session, space: dict) -> set[Path]:
    key = space["key"]
    log.info("Syncing space %s (%s)", key, space.get("name", ""))

    kept: set[Path] = set()
    created = updated = skipped = 0

    for page in list_pages(session, space["id"]):
        target = page_path(key, page)
        remote_version = (page.get("version") or {}).get("number", 0)
        local_version = None if FORCE_FULL else existing_version(target)

        if local_version is not None and local_version == remote_version:
            kept.add(target)
            skipped += 1
            continue

        body_html = get_page_body(session, page["id"])
        labels = get_labels(session, page["id"])

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            build_frontmatter(page, space, labels) + "\n" + html_to_markdown(body_html),
            encoding="utf-8",
        )
        kept.add(target)
        if local_version is None:
            created += 1
        else:
            updated += 1

    log.info("  %s: %d new, %d updated, %d unchanged", key, created, updated, skipped)
    return kept


def prune_orphans(space_keys: list[str], kept: set[Path]) -> int:
    removed = 0
    for key in space_keys:
        space_dir = OUTPUT_DIR / key
        if not space_dir.is_dir():
            continue
        for path in space_dir.rglob("*.md"):
            if path not in kept:
                log.info("  removing orphan %s", path)
                path.unlink()
                removed += 1
        # tidy up any directories left empty
        for d in sorted(space_dir.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    return removed


def main() -> int:
    if CLOUD_ID:
        log.info("Gateway mode (scoped token): %s", API_ROOT)
    else:
        log.info(
            "Site mode (classic token): %s -- if this 401s, your token is scoped; "
            "set CONFLUENCE_CLOUD_ID.", API_ROOT
        )

    session = make_session()

    spaces = resolve_spaces(session, SPACE_KEYS)
    if not spaces:
        log.error("No accessible spaces resolved from SPACE_KEYS -- nothing to do.")
        return 1

    kept: set[Path] = set()
    for space in spaces:
        kept |= sync_space(session, space)

    removed = prune_orphans([s["key"] for s in spaces], kept)

    log.info("Done. %d pages on disk, %d orphans removed.", len(kept), removed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
