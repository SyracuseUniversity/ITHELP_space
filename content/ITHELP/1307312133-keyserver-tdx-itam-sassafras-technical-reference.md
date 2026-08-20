---
title: "KeyServer (TDX ITAM / Sassafras) — Technical Reference"
confluence_id: "1307312133"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/1307312133/KeyServer+TDX+ITAM+Sassafras+Technical+Reference"
version: 3
last_modified: "2026-08-18T10:17:49.855Z"
status: "current"
parent_id: "159940616"
---

- [Overview](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-Overview)
- [Current Environment](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-CurrentEnvironment)
- [Architecture at a Glance](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-ArchitectureataGlance)
- [Administration](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-Administration)
  - [Division Management](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-DivisionManagement)
  - [Sections and the SU Division](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-SectionsandtheSUDivision)
  - [Anchoring Computers](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-AnchoringComputers)
  - [Admin Program Version Requirement](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-AdminProgramVersionRequirement)
- [Common Use Cases / When to Reference This Page](#KeyServer(TDXITAM/Sassafras)—TechnicalReference-CommonUseCases/WhentoReferenceThisPage)

## Overview

KeyServer, developed by Sassafras Software, is the license management and software metering platform used by SU ITS to track and control concurrent-use software licenses across campus. It is an observer of license use to give better control of budget.

At SU, KeyServer monitors usage across a range of concurrently-licensed software (e.g. MATLAB, SPSS, Mathematica/MathLM, and other toolboxes). Rather than acting primarily as a strict gatekeeper, its core value is visibility: giving ITS and departments the usage data needed to make informed decisions about license counts, renewals, and budget. It also supports hardware/asset **lifecycle tracking** for computers and devices across campus.

## Current Environment

| Component | Detail |
| --- | --- |
| Version | KeyServer 8.1 |
| Host OS | Windows Server 2022 |
| Authentication | Local KeyServer accounts (SAML/SSO via Entra ID planned, not yet in place) |
| Management | ITAM Web UI (division management); KeyConfigure (section management, admin console) |
| ITAM Integration | TDX (TeamDynamix) ITAM |

## Architecture at a Glance

- **KeyServer engine** — the core service that observes and logs license checkouts/checkins per product, building the usage picture that drives budget and renewal decisions.
- **Client redirection** — licensed applications on endpoints are pointed at the KeyServer host (via config files, environment variables, or license manager settings specific to each application).
- **Divisions** — KeyServer organizes clients/computers into “divisions,” which map roughly to departments. This is where a lot of day-to-day admin work happens (adding/moving computers between divisions to keep usage tracking organized by department for budget purposes).
- **SAML/SSO (Entra ID)** — planned to replace local KeyServer accounts for admin console authentication; not yet implemented.
- **TDX ITAM** — KeyServer data feeds into TDX for asset/license lifecycle tracking, supporting the broader ITAM migration effort.

**Login Types: Dedicated, Leased, Dormant, Excluded**

- **Dedicated** — A permanent seat that does not expire and is not automatically reassigned, even during periods of inactivity. Computers usually land here because a Node Policy is assigned to them or an admin manually moves them here. Moving a Dedicated computer to another Login Type revokes any Node Policies assigned to it, though usage history remains available in the Usage Log and Reports.
- **Leased** — The default category for newly discovered computers. Leased seats have an expiration time that renews each time the computer checks in or uses managed software. If the lease expires without renewal, the computer automatically moves to Dormant. A computer that unexpectedly reappears in Leased after being Dormant can signal that something came back online that was not expected to be in service.
- **Dormant** — Does not consume a license seat and does not appear in Audit reports, but historical usage remains available in Usage reports. If a Dormant computer reconnects, reports usage, or uses managed software, it automatically switches back to Leased or Dedicated. Computers should typically be moved to Dormant when retired from service.
- **Excluded** — Not really a login type; excluded computers cannot receive services, and KeyServer records no new data for them. Like Dormant computers, they do not count against the license/client limit and do not appear in Audit reports, but existing historical usage may still appear in Usage reports. Exclusion fully retires a record while preserving its history.

## Administration

### Division Management

Section admins move computers between divisions using the **ITAM Web UI** (<https://keyserver.syr.edu>). Divisions can be added, renamed, deleted, and computers reassigned between them directly in the web interface — no need to use KeyConfigure for routine division management.

**Note:** Sections (the higher-level container that governs which divisions an admin has rights to) can only be managed in **KeyConfigure**, not the Web UI. Section admins won’t need this for day-to-day division moves, but it’s worth knowing if a new section needs to be created or section-level permissions need to change.

**Scoping note:** Section admins can only move computers *within their own section*. A computer can only be reassigned to a different division that belongs to the same section the admin manages — cross-section moves are not permitted. This keeps usage tracking aligned with departmental/section boundaries and prevents accidental cross-section reassignment.

### Sections and the SU Division

Every OU has a corresponding Section in KeyServer. There is also a division called SU that sits outside of any Section — every admin has access to it, regardless of which section(s) they normally manage. Admins should move computers they recognize as belonging to them from the SU division into their own section as soon as they're identified — leaving them in SU longer than necessary means they stay exposed to being moved or affected by any admin.

**Caution:** Admins should never move a computer into the SU division unless they are positive the object has been placed in their section incorrectly. Because the SU division is accessible to all admins, be very careful when moving computers out of a section and into SU. A computer moved out of its proper section loses the scoped protections that section provides, and any admin can then move or affect it. Only make this move when you're confident it corrects a misplaced object — not as a routine or exploratory action.

### Anchoring Computers

To prevent a computer from being moved out of its assigned division/section by Rules or AD/OU mapping without an admin explicitly doing so, use the **Anchor in Division** feature:

1. In the ITAM Web UI (<https://keyserver.syr.edu>), go to the Computers list.
2. Select the computer(s) you want to protect.
3. Open the **More** menu (⁞ ▾) in the top ribbon, **or** right-click the computer directly.
4. Choose **Anchor in Division**.

Anchoring forces the computer to stay in its currently assigned division — it will not be automatically moved by Rules or AD mapping. It will only move if an admin manually reassigns it. This is worth using for computers that should stay put regardless of naming-rule changes or AD/OU shifts.

### Admin Program Version Requirement

The KeyServer Admin program used to connect to the server **must match the server’s version** (currently 8.1.0.6). KeyConfigure will not work if its version does not match the server.

**Best option — download directly from the SU server:** These links are served by the KeyServer host itself, so they always match whatever version the server is actually running (no version drift, even between minor updates):

- Windows x64: [ksp-admin-x64-latest.exe](https://keyserver.syr.edu/kami/ksp-admin-x64-latest.exe)
- Windows arm64: [ksp-admin-arm64-latest.exe](https://keyserver.syr.edu/kami/ksp-admin-arm64-latest.exe)
- Mac: [ksp-admin-latest.pkg](https://keyserver.syr.edu/kami/ksp-admin-latest.pkg)

**Alternative — Sassafras/TDX download page:** [Current ITAM Downloads](https://solutions.teamdynamix.com/TDClient/1965/Portal/KB/Article/169236/Current-ITAM-Downloads) — separate tabs for **Windows**, **Macintosh**, and **Linux**; grab **Admin (KeyConfigure)** under the appropriate OS tab, not the Client (KeyAccess) or Server (KeyServer) packages also listed there.

**Known issue with the Sassafras/TDX page:** It only offers the current minor version — it does not host older minor version installers. If the server is ever running a minor version behind the latest available download there, there’s no way to grab a matching older client from that page. The SU-hosted links above avoid this problem entirely since they’re pulled straight from the server, so use those as the primary source.

## Common Use Cases / When to Reference This Page

- Pulling usage data to inform budget decisions on license counts and renewals
- New computers need to be added to a division so their usage is tracked accurately by department for budget purposes
- A department wants to know actual usage/demand for a concurrently-licensed product before a purchasing decision
- Troubleshooting login issues on the KeyServer admin console
- Choosing the appropriate Login Type: use **Dormant** for hardware that is temporarily out of service or retired but might return, such as seasonal lab machines or loaners between checkouts. Use **Excluded** for computers that are permanently decommissioned or should never interact with KeyServer again. Leave everything else as **Leased**, the default, unless a Node Policy requires **Dedicated**.
