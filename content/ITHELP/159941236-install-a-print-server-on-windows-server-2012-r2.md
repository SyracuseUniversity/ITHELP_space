---
title: "Install a Print Server on Windows Server 2012 R2"
confluence_id: "159941236"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2"
version: 9
last_modified: "2016-07-06T16:24:21.000Z"
status: "current"
parent_id: "159941370"
labels:
  - "s17"
---

he following page will aid in preparing a newly created server to be used as a print server.

- [Installing a Print Server on Windows Server 2012 R2](#InstallaPrintServeronWindowsServer2012R2-InstallingaPrintServeronWindowsServer2012R2)
  - [1 - Locate Add Roles and Features](#InstallaPrintServeronWindowsServer2012R2-1-LocateAddRolesandFeatures)
  - [2 - Review Preparation Information](#InstallaPrintServeronWindowsServer2012R2-2-ReviewPreparationInformation)
  - [3 - Select Installation Type](#InstallaPrintServeronWindowsServer2012R2-3-SelectInstallationType)
  - [4 - Select the Server](#InstallaPrintServeronWindowsServer2012R2-4-SelecttheServer)
  - [5 - Specify Server Roles](#InstallaPrintServeronWindowsServer2012R2-5-SpecifyServerRoles)
  - [6 - Continue Past Features](#InstallaPrintServeronWindowsServer2012R2-6-ContinuePastFeatures)
  - [7 - Review Print Document Services](#InstallaPrintServeronWindowsServer2012R2-7-ReviewPrintDocumentServices)
  - [8 - Set Role Services](#InstallaPrintServeronWindowsServer2012R2-8-SetRoleServices)
  - [9 - Confirm Settings and Install](#InstallaPrintServeronWindowsServer2012R2-9-ConfirmSettingsandInstall)
  - [10 - Confirm Installation](#InstallaPrintServeronWindowsServer2012R2-10-ConfirmInstallation)
  - [11 - Update Print Spooler Location](#InstallaPrintServeronWindowsServer2012R2-11-UpdatePrintSpoolerLocation)
- [Getting Help](#InstallaPrintServeronWindowsServer2012R2-GettingHelp)

# Installing a Print Server on Windows Server 2012 R2

### 1 - Locate Add Roles and Features

First, log in to your Windows server 2012 R2 as an Administrator. When you log in, the Server Manager will be opened automatically. If it does not, you must open it manually.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/1.jpg?api=v2)

In the Server Manager click on the "**Manage**" button and select the "**Add Roles and Features**" to add the new feature.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/2.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 2 - Review Preparation Information

A new window opened. Review the instructions and click "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/3.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 3 - Select Installation Type

Now it will ask for the "Installation Type" from which you must select “**Role-based or feature-based installation**” and then click on "Next".

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/4.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 4 - Select the Server

On the next screen, choose ”**Select a server from the server pool**”. Select the desired print server and click “**Next**” to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/5.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 5 - Specify Server Roles

The next steps will reveal a list of available roles for this server. Select "**Print and Document Services**".

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/6.jpg?api=v2)

After selecting Print and Document Services a new window will be open. Click "**Add Features**" to grant the required permission.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/7.jpg?api=v2)

The components and features are now ready to install. Just click **"Next**" to proceed.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 6 - Continue Past Features

Leave the Features page at the default. You do not need to install any features in order for print and document services. Click “**Next**” to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/8.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 7 - Review Print Document Services

The Print Document Services page will have you review some notable information. After reviewing the content, click "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/9.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 8 - Set Role Services

Select the "**Role Services**" page. Once there you must select the first option, "**Print Server**". Once selected, click "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/10.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 9 - Confirm Settings and Install

A confirmation page will now open. Choose to provide the server with permission to restart if required or click on "**Install**" without giving permission to restart.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/11.jpg?api=v2)

The installation will now begin.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/12.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 10 - Confirm Installation

If you did not choose the restart if necessary restart the server. In the Server Manager, confirm the installation was successfully completed. This confirmation can be located by clicking on the flag in the upper right-hand corner.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/13.jpg?api=v2)

The server should now be properly set up as a print server.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

### 11 - Update Print Spooler Location

The print spooler location should be amended from its default location C:\Windows\system32\spool\PRINTERS, to a location separate from the system's drive such as D:\spool\PRINTERS. An advantage would be the system drive cannot get full by user actions (ex. consider malicious user/software creating many large spool files => systemdrive full=denial of service attack!).

Recommended for Heavy Use

While updating the print spooler location is not required, the print management technical team recommends doing so for higher volume print locations.

To do so, launch Print Management and highlight the print server. Right-click and select "Properties".

Once there, navigate to the Advanced tab.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/advancedtab.png?api=v2)

Amend the Spool folder location to a location that is not on the system drive such as D:\spool\PRINTERS. Select "**Apply**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/advancedprinter.png?api=v2)

A warning will be shown to verify changes to the spool folder are intended. Select "**Yes**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/spoolchange.png?api=v2)

Before applying the newly changed print spooler settings, a services restart is required. To do so, open the Server Manager Print Services.

Right click on the print spooler under Services and click "**Restart Services**".

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941236/servicesrestart.png?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941236/Install+a+Print+Server+on+Windows+Server+2012+R2#InstallaPrintServeronWindowsServer2012R2-topofpage)
