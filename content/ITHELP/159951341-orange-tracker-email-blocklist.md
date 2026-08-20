---
title: "Orange Tracker Email Blocklist"
confluence_id: "159951341"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951341/Orange+Tracker+Email+Blocklist"
version: 5
last_modified: "2023-09-26T15:18:36.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "email"
  - "ot"
  - "jira"
  - "jsm"
  - "blocklist"
---

## Overview

---

The blocklist prevents users and domains from submitting requests by email to Orange Tracker. This is **project-centric** and can be updated by the respective Project Admins.

Atlassian Doc: <https://support.atlassian.com/jira-service-management-cloud/docs/manage-your-blocklist/>

Mark As Spam Does Not Add To Blocklist

Prior to the Cloud migration, the Mark As Spam resolution initiated a backend process to add addresses to the site-wide blocklist. After going to Cloud, this transition no longer adds accounts to the blocklist, allowing these accounts to still submit requests through email. The manual identification and addition of these spam accounts to the blocklist is the only way to prevent these accounts from submitting email (see below).

## Adding Blocklist Entry

---

1. From your service project, go to **Project settings →** **Email requests**
2. Select **More** → **Manage blocklist**
3. Select **+ Add email address or domain**
4. Enter the domain name (do not include @), or the specific email address you want to block
5. Select **Save**

Currently, blocklists only support exact domain matching. For example, adding the domain 'example.com' will match 'anyuser@example.com' but not 'anyuser@example.com**.au**' or 'anyuser@**mail**.example.com'.

The blocklist does not currently support wildcards or pattern matching.

## Audience

---

PROJECT ADMIN

## On This Page

---

- [Overview](#OrangeTrackerEmailBlocklist-Overview)
- [Adding Blocklist Entry](#OrangeTrackerEmailBlocklist-AddingBlocklistEntry)

## Related Content

---

- Page:[Orange Tracker Customer Portal](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159945235/Orange+Tracker+Customer+Portal)
- Page:[Orange Tracker Automation](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation)
- Page:[Orange Tracker](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941388/Orange+Tracker)
- Page:[Orange Tracker Add a New Agent](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159948827/Orange+Tracker+Add+a+New+Agent)
- Page:[Atlassian Public Name](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159944600/Atlassian+Public+Name)
