---
title: "Installing a PaperCut Printer"
confluence_id: "159941239"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer"
version: 32
last_modified: "2018-06-18T19:45:33.000Z"
status: "current"
parent_id: "159941357"
labels:
  - "s17"
---

Use the following steps to install a newly acquired printer to your department's printer group.

University Device Guidelines

Before installing any printer on campus, be aware of [Syracuse University's imaging device guidelines](https://answers.syr.edu/display/infosec011/SU+Information+Technology+Security+Standards+and+Procedures?preview=/54362577/54887652/ImagingDeviceGuidelines-G0101.pdf).

- [Installing New Printers](#InstallingaPaperCutPrinter-InstallingNewPrinters)
  - [1 - Select Add Printer](#InstallingaPaperCutPrinter-1-SelectAddPrinter)
  - [2 - Create a New Port](#InstallingaPaperCutPrinter-2-CreateaNewPort)
  - [3 - Identify Printer Driver](#InstallingaPaperCutPrinter-3-IdentifyPrinterDriver)
  - [4 - Name the Printer](#InstallingaPaperCutPrinter-4-NamethePrinter)
  - [5 - Review Printer Settings](#InstallingaPaperCutPrinter-5-ReviewPrinterSettings)
  - [6 - Finalize Printer Installation](#InstallingaPaperCutPrinter-6-FinalizePrinterInstallation)
- [Getting Help](#InstallingaPaperCutPrinter-GettingHelp)

# Installing New Printers

The steps below assume that the administrator has properly installed PaperCut on a new or existing print server. If PaperCut is not installed, please refer to the PaperCut installation guides for [new](https://su-jsm.atlassian.net/wiki/x/_oKICQ) or [existing](https://su-jsm.atlassian.net/wiki/x/coKICQ) print servers.

Can't Install Within PaperCut

While you can edit the settings and restrictions of a printer in the PaperCut admin interface once you've installed it, the initial installation process occurs on the print server. If you'd like more information about managing printers once installed, visit the [Printers - Managing Printer Settings page](https://su-jsm.atlassian.net/wiki/x/wIKICQ).

### 1 - Select Add Printer

In the Print Management Interface, Print Management MMC, right click on "**Printers**" and select "**Add Printer...**".

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step1.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

### 2 - Create a New Port

Specify the creation of a new port. In the drop down menu, select "**PaperCut TCP/IP Port**".

PaperCut Port Not Working?

There is a handful of devices that may have difficulties interacting with the PaperCut TCP/IP Port. As a best practice, always attempt to use the PaperCut port first, but use the Standard TCP/IP port if necessary.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step2.PNG?api=v2)

Port Not Available?

If the PaperCut TCP/IP port is not available ensure PaperCut is installed on the print server. If this is the case, refer to the PaperCut installation guides for [new](https://su-jsm.atlassian.net/wiki/x/_oKICQ) or [existing](https://su-jsm.atlassian.net/wiki/x/coKICQ) print servers.

Use IP or DNS components as you normally do (by department). Once populated, click "**Add Port**" and then "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step3.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

### 3 - Identify Printer Driver

Use a new or existing driver. The driver will be dictated by the printer itself. Once selected, click "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step4.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

### 4 - Name the Printer

The next step requires naming of the printer. Be sure to always check "**Share this printer**". The Share Name should mirror the Printer Name. Comments are not required, but encouraged to help with future configurations. Click " **Next** " to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step5.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

### 5 - Review Printer Settings

Review the settings that you have made to the new printer. Go back if necessary. If the settings are correct, click "**Next**" to proceed.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step6.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

### 6 - Finalize Printer Installation

If the printer was successfully installed the page below will be shown. Click "**Finish**" to conclude the process. You are welcome to print a test page, but it is not required. There is also an option to add another printer if more printers require installation.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941239/Step7.PNG?api=v2)

The printer is now installed and ready for configuration. Follow the [Configuring a PaperCut printer page](https://su-jsm.atlassian.net/wiki/x/8IKICQ) for details on configuring the newly installed printer's settings.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941239/Installing+a+PaperCut+Printer#InstallingaPaperCutPrinter-topofpage)
