---
title: "Installing PaperCut on a New Print Server"
confluence_id: "159941370"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941370/Installing+PaperCut+on+a+New+Print+Server"
version: 19
last_modified: "2021-07-07T18:21:32.000Z"
status: "current"
parent_id: "159941357"
labels:
  - "s17"
---

The following page will guide an administrator through preparing a new server as a print server and installing PaperCut.

University Device Guidelines

Before installing any printer on campus, be aware of [Syracuse University's imaging device guidelines](https://answers.syr.edu/display/infosec011/SU+Information+Technology+Security+Standards+and+Procedures?preview=/54362577/54887652/ImagingDeviceGuidelines-G0101.pdf).

- [Installing PaperCut on a New Print Server](#InstallingPaperCutonaNewPrintServer-InstallingPaperCutonaNewPrintServer)
  - [1 - Create a Windows Server](#InstallingPaperCutonaNewPrintServer-1-CreateaWindowsServer)
  - [2 - Install a Print Server](#InstallingPaperCutonaNewPrintServer-2-InstallaPrintServer)
  - [3 - Add Print Server to the PaperCut Server Group](#InstallingPaperCutonaNewPrintServer-3-AddPrintServertothePaperCutServerGroup)
  - [4 - Install and Configure Printers for PaperCut](#InstallingPaperCutonaNewPrintServer-4-InstallandConfigurePrintersforPaperCut)
  - [5 - Confirm Printers in Admin Interface](#InstallingPaperCutonaNewPrintServer-5-ConfirmPrintersinAdminInterface)
- [Getting Help](#InstallingPaperCutonaNewPrintServer-GettingHelp)

# Installing PaperCut on a New Print Server

Follow the steps below to prepare a new print server and install PaperCut.

Existing Print Server?

If you are looking to convert an existing print server to PaperCut, please follow the [Installing PaperCut on an Existing Print Server guide](https://su-jsm.atlassian.net/wiki/x/coKICQ).

#### 1 - Create a Windows Server

Create a new Windows Server 2012 R2 server as per your department guidelines.

#### 2 - Install a Print Server

Follow the [Install a Print Server on Windows Server 2012 R2 guide](https://su-jsm.atlassian.net/wiki/x/dIKICQ) to condition your newly created server as a print server.

#### 3 - Add Print Server to the PaperCut Server Group

Once the print server is ready, add the server to the following groups:

- OU-Computers
- OU-Software-RU-SpecOpsDeploy
- OU-Software-RU-Papercut Print Server

 After adding the server to each group, restart the print server and proceed to the next step.

#### 4 - Install and Configure Printers for PaperCut

A PaperCut port will need to be created for each printer. The standard TCP/IP ports will need to be changed to the newly created PaperCut TCP/IP port. Use the settings found in the [Configuring a PaperCut Printer guide](https://su-jsm.atlassian.net/wiki/x/8IKICQ) to ensure that each printer is ready for use in PaperCut.

#### 5 - Confirm Printers in Admin Interface

Log into the [PaperCut admin interface](http://printing.syr.edu/admin) and navigate to the Printers tab.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941370/printertab.PNG?api=v2)

The Printer List tab should be the default sub-tab. 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941370/printerlist.PNG?api=v2)

The Printer List should be populated with any printers that have been properly added to your print server.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941370/printerlists.PNG?api=v2)

Printer Not Showing Up?

If a printer is not showing up, revisit the [Configuring a PaperCut Printer guide](https://su-jsm.atlassian.net/wiki/x/8IKICQ) to ensure that it has been properly configured for PaperCut.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941370/Installing+PaperCut+on+a+New+Print+Server#InstallingPaperCutonaNewPrintServer-topofpage)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941370/Installing+PaperCut+on+a+New+Print+Server#InstallingPaperCutonaNewPrintServer-topofp)
