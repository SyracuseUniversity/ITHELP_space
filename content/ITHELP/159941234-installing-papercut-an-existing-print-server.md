---
title: "Installing PaperCut an Existing Print Server"
confluence_id: "159941234"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941234/Installing+PaperCut+an+Existing+Print+Server"
version: 15
last_modified: "2018-04-16T13:45:11.000Z"
status: "current"
parent_id: "159941357"
labels:
  - "s17"
---

The following page is intended to guide organization unit administrators through adapting an existing print server to PaperCut.

University Device Guidelines

Before installing any printer on campus, be aware of [Syracuse University's imaging device guidelines](https://answers.syr.edu/display/infosec011/SU+Information+Technology+Security+Standards+and+Procedures?preview=/54362577/54887652/ImagingDeviceGuidelines-G0101.pdf).

- [Installing PaperCut an Existing Print Server](#InstallingPaperCutanExistingPrintServer-InstallingPaperCutanExistingPrintServer)
  - [1 - Uninstall Print Manager Plus](#InstallingPaperCutanExistingPrintServer-1-UninstallPrintManagerPlus)
  - [2 - Add Print Server to the PaperCut Server Group](#InstallingPaperCutanExistingPrintServer-2-AddPrintServertothePaperCutServerGroup)
  - [3 - Re-Configure Printers for PaperCut](#InstallingPaperCutanExistingPrintServer-3-Re-ConfigurePrintersforPaperCut)
  - [4 - Confirm Printers in Admin Interface](#InstallingPaperCutanExistingPrintServer-4-ConfirmPrintersinAdminInterface)
- [Getting Help](#InstallingPaperCutanExistingPrintServer-GettingHelp)

# Installing PaperCut an Existing Print Server

Follow the steps below to convert an existing print server to PaperCut.

New Print Server?

If you are creating a new print server, please follow the [Installing PaperCut on a New Print Server guide](https://su-jsm.atlassian.net/wiki/x/_oKICQ).

#### 1 - Uninstall Print Manager Plus

To install PaperCut, Print Manager Plus must first be removed. Follow our [Uninstall Print Manager Plus guide](https://su-jsm.atlassian.net/wiki/x/yIKICQ) to prepare your existing print server.

After removing PMP, restart the print server and proceed to the next step.

#### 2 - Add Print Server to the PaperCut Server Group

Once the print server is ready, add it to the designated PaperCut server group. After adding it to the server group, restart the print server and proceed to the next step.

#### 3 - Re-Configure Printers for PaperCut

A new PaperCut port will need to be created for each printer. The old TCP/IP ports will need to be abandoned. Use the settings found in the [Configuring a PaperCut Printer guide](https://su-jsm.atlassian.net/wiki/x/8IKICQ) to ensure that each printer is ready for use in PaperCut.

#### 4 - Confirm Printers in Admin Interface

Log into the [PaperCut admin interface](http://printing.syr.edu/admin) and navigate to the Printers tab.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941234/printertab.PNG?api=v2)

The Printer List tab should be the default sub-tab. 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941234/printerlist.PNG?api=v2)

The Printer List should be populated with any printers that have been properly added to your print server.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941234/printerlists.PNG?api=v2) 

Printer Not Showing Up?

If a printer is not showing up, revisit the [Configuring a PaperCut Printer guide](https://su-jsm.atlassian.net/wiki/x/8IKICQ) to ensure that it has been properly configured for PaperCut.

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941234/Installing+PaperCut+an+Existing+Print+Server#InstallingPaperCutanExistingPrintServer-topofp)
