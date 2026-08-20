---
title: "Uninstalling Print Manager Plus"
confluence_id: "159941320"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941320/Uninstalling+Print+Manager+Plus"
version: 10
last_modified: "2016-07-06T16:24:41.000Z"
status: "current"
parent_id: "159941234"
labels:
  - "s17"
---

Following the steps below to remove Print Manager Plus from a departmental print server.

- [Uninstalling Print Manager Plus](#UninstallingPrintManagerPlus-UninstallingPrintManagerPlus)
  - [1 - Open Programs and Features](#UninstallingPrintManagerPlus-1-OpenProgramsandFeatures)
  - [2 - Uninstall Print Manager Plus](#UninstallingPrintManagerPlus-2-UninstallPrintManagerPlus)
  - [3 - Confirm the Uninstall](#UninstallingPrintManagerPlus-3-ConfirmtheUninstall)
  - [4 - Finalize and Restart](#UninstallingPrintManagerPlus-4-FinalizeandRestart)
  - [5 - Remove Admins](#UninstallingPrintManagerPlus-5-RemoveAdmins)
- [Getting Help](#UninstallingPrintManagerPlus-GettingHelp)

# Uninstalling Print Manager Plus

Follow the steps below to remove Print Manager Plus from an existing departmental print server.

Required for PaperCut

Uninstalling Print Manager Plus via the steps below are required to install PaperCut.

### 1 - Open Programs and Features

Navigate to the programs and features window within your print server.

### 2 - Uninstall Print Manager Plus

Select Print Manager Plus (PMP) and click uninstall.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerProgramsandFeatures%20PMP.jpg?api=v2)

Ensure that all features are completely removed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerProgramsandFeatures%20PMPConfirmUninstall.jpg?api=v2)

### 3 - Confirm the Uninstall

Be sure to also remove Print Manager Plus - Client is also removed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerProgramsandFeatures%20PMPandClient.jpg?api=v2)

Client Uninstall Only If Necessary

Some organizational units may have server that do not contain the server. If so, you do not need to confirm the client has been removed to proceed.

Again, ensure that all features are completely removed.

 ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerProgramsandFeatures%20PMPConfirmUninstall.jpg?api=v2)

### 4 - Finalize and Restart

Once the PMP has been removed, click Finish and restart your print server.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerProgramsandFeatures%20PMPUninstallFinish.jpg?api=v2)

### 5 - Remove Admins

Open the Administrators Properties window. Select AD\root-pmp and click  Remove.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941320/PMPServerLocalAdminGroup%20root-pmp.jpg?api=v2)

 [Return of Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941320/Uninstalling+Print+Manager+Plus#UninstallingPrintManagerPlus-topofpage)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941320/Uninstalling+Print+Manager+Plus#UninstallingPrintManagerPlus-topofpage)
