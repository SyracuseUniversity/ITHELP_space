---
title: "Configuring a PaperCut Printer"
confluence_id: "159941360"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer"
version: 20
last_modified: "2018-06-18T20:07:36.000Z"
status: "current"
parent_id: "159941357"
labels:
  - "s17"
---

Use the following steps to configure a newly installed PaperCut printer.

 

University Device Guidelines

Before installing any printer on campus, be aware of [Syracuse University's imaging device guidelines](https://answers.syr.edu/display/infosec011/SU+Information+Technology+Security+Standards+and+Procedures?preview=/54362577/54887652/ImagingDeviceGuidelines-G0101.pdf).

- [Configuring a PaperCut Printer](#ConfiguringaPaperCutPrinter-ConfiguringaPaperCutPrinter)
  - [1 - Enable Listing in Directory](#ConfiguringaPaperCutPrinter-1-EnableListinginDirectory)
  - [2 - Verify Printer Ports](#ConfiguringaPaperCutPrinter-2-VerifyPrinterPorts)
  - [3 - Manage Advanced Settings](#ConfiguringaPaperCutPrinter-3-ManageAdvancedSettings)
  - [4 - Leave Security at Default](#ConfiguringaPaperCutPrinter-4-LeaveSecurityatDefault)
  - [5 - Review and Finalize](#ConfiguringaPaperCutPrinter-5-ReviewandFinalize)
  - [6 - Manage Printer Specific Protocols (Disable WS Discovery)](#ConfiguringaPaperCutPrinter-6-ManagePrinterSpecificProtocols(DisableWSDiscovery))
    - [HP LJ 400 M451DW](#ConfiguringaPaperCutPrinter-HPLJ400M451DW)
    - [HP M401DNE](#ConfiguringaPaperCutPrinter-HPM401DNE)
    - [Xerox 7556 WC](#ConfiguringaPaperCutPrinter-Xerox7556WC)
    - [Xerox 7970](#ConfiguringaPaperCutPrinter-Xerox7970)
- [Getting Help](#ConfiguringaPaperCutPrinter-GettingHelp)

# Configuring a PaperCut Printer

Follow the steps below to configure a new or existing PaperCut printer. If you have a new printer, please first install it using our [Installing a PaperCut Printer guide](https://su-jsm.atlassian.net/wiki/x/d4KICQ).

Not Accessible in PaperCut

While you can edit the settings and restrictions of a printer in the PaperCut admin interface once you've installed it, the initial configuration process occurs on the print server. If you'd like more information about managing printers once installed and configured, visit the [Printers - Managing Printer Settings page](https://su-jsm.atlassian.net/wiki/x/wIKICQ).

### 1 - Enable Listing in Directory

In the Print Management Interface, Print Management MMC, right-click on the desired printer and select "**Properties**". Select the Sharing tab and check off "**List in** **directory**". Click "**Apply**". 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/Step8.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

### 2 - Verify Printer Ports

Next, click on the Ports tab. In most cases, we recommend selecting the Standard TCP/IP port. This port type will permit some types of printer status notifications back to the client that are blocked when using the PaperCut TCP/IP port type (such as with Xerox 7556/7970 copiers).

Xerox Copier Notifications

Client notifications are blocked when using the Papercut TCP/IP port type. Notifications are supported using the Standard TCP/IP port type; however, if you have IP filtering enabled on the copier to scope direct access only to your print and management servers (which is good practice), then these client notifications will be blocked, and clients will see a [‘Status not Available: Printer Status is not available at this time’ message](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/statusnotavail.png?version=1&modificationDate=1479835588000&cacheVersion=1&api=v2) every time they print. To suppress this message, turn off Job Notification in the Xerox print properties on the print server (Properties > Administration tab > Job Notification: Disabled).

Community Name Must Match When Using Standard TCP/IP

When enabling SNMP status in the port configuration, the Community Name must match the SNMP setting in the printer’s internal network interface (such as changing to SUSNMP), otherwise the print server may report the printer is ‘offline’ and fail to send jobs through.

The PaperCut port type is needed only if you plan to use [PaperCut’s hardware check feature](http://www.papercut.com/products/ng/manual/applicationserver/topics/printer-hwcheck.html) (‘validate page counts after printing’), which is not enabled by default and is found under the Advanced Configuration section on the Summary tab for each printer in PaperCut.

Only Standard Ports Available?

If you do not see PaperCut ports, please revisit the installation process of PaperCut. Only print servers with PaperCut properly installed will allow PaperCut ports to be selected.

No Bi-Directional Support

The print management technical team recommends bi-directional support be disabled (if it is not already unchecked by default). This setting can cause functionality related issues, particularly with HP printers.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/Step9.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

### 3 - Manage Advanced Settings

Navigate to the Advanced tab. Uncheck "**Enable advanced printing features**". It is also recommended that "**Start printing after the last page is spooled**" be selected. The remaining settings should be configured as appropriate for your environment, but should look similar to the image below. Click "**Apply**" if any changes were made.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/Step10.PNG?api=v2)

Clicking on "**Printing Defaults...**" will reveal the ability to make further changes to the printer's configurations. Again, click "**Apply**" if any changes were made.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/Step12.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

### 4 - Leave Security at Default

The print management technical team recommends that you do not change printer security settings at this location. The default should look similar to the image below. It is recommended that security settings are changed in the [PaperCut Administrative interface](https://su-jsm.atlassian.net/wiki/x/wIKICQ). 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/Step11.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

### 5 - Review and Finalize

Review the changes that have been made. Ensure that the Apply button is greyed out indicating no new changes have occurred. Click "**OK**" to finalize the printer's configurations. Your printer is now ready to be used in the [PaperCut admin interface](https://printing.syr.edu/admin).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

### 6 - Manage Printer Specific Protocols (Disable WS Discovery)

Now that your printer has been installed and configured for use you'll want to ensure the correct protocols are in place. In general, you will want to ensure WS Discovery is disabled. This step is different by model. Below are paths and screenshots for some of the more readily used models on campus. 

Finding WS Discovery Enabled Devices

Though not required, using the host name in DDI for the hostname on the device will provide you with location information in the event WS Discovery is enabled.

#### HP LJ 400 M451DW

For the HP LJ 400 M 451DW the settings are located in Networking→Security→Advanced

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/hpprinter.jpg?api=v2)

#### HP M401DNE

For the HP M401DNE the settings are located in Networking→Configuration→Advanced  

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/hp401dne.png?api=v2)

#### Xerox 7556 WC

For Xerox 7556 WC the settings are located in Properties→Connectivity→Protocols

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/xerox7556.png?api=v2)

#### Xerox 7970

For the Xerox 7970 the settings are located in Properties→Services→Printing→Printing Web Services

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941360/xerox7970.jpg?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941360/Configuring+a+PaperCut+Printer#ConfiguringaPaperCutPrinter-topofpage)
