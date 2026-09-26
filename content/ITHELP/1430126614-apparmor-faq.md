---
title: "AppArmor FAQ"
confluence_id: "1430126614"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/1430126614/AppArmor+FAQ"
version: 1
last_modified: "2026-09-23T18:08:04.217Z"
status: "current"
parent_id: "159941299"
---

## What is AppArmor?

AppArmor is a desktop emergency alert application, part of the Rave (Motorola Solutions) suite. It gives campus a fast, reliable way to push critical alerts directly to desktops, complementing our existing notification channels.

## Why are we rolling this out?

It adds another layer to campus emergency communications, so critical alerts reach people directly on their screens, not just through email or text.

## Who is behind this rollout?

ITS and the Department of Public Safety are leading the rollout, working closely with ACS and CIS throughout the process.

## Where has it been tested?

On lab and presentation role devices, across both Windows and Mac.

## Which devices will get AppArmor?

Any lab or presentation role Windows device, as well as shared Macs.

## How can I confirm the agent is installed and running before a test?

Look for the AppArmor icon, a green triangle in the system tray on Windows, or the menu bar tray on Mac, and confirm the machine is logged in. Alerts only display on machines that are logged in when the alert is issued.

## What happens when an alert fires while someone is logged in?

The alert displays full-screen with sound and visuals, and the user must manually dismiss it or the admin-set timeout is reached.

## What happens if the machine is logged out or asleep when an alert fires?

Nothing displays. This is expected, vendor-confirmed behavior, not a bug.

## Can a missed alert reach a user after the fact?

Yes, but only if "Queue Notifications for Disconnected Devices" is enabled in the admin console and the alert is still active when the user logs back in.

## When is the campus-wide rollout happening?

We're on track to move into broader distribution soon.

## What do I need to do to prepare?

Nothing yet. More details on department and support staff responsibilities will follow as we get closer to full deployment.

## Where can I learn more or ask questions?

Join the October 1st SUIT Forum meeting, where we'll cover AppArmor in more detail.
