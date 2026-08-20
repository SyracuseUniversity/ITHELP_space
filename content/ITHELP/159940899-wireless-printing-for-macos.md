---
title: "Wireless Printing for macOS"
confluence_id: "159940899"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159940899/Wireless+Printing+for+macOS"
version: 30
last_modified: "2023-08-18T19:36:34.000Z"
status: "current"
parent_id: "159941246"
labels:
  - "mac"
  - "wireless"
  - "printing"
  - "osx"
  - "s17"
  - "printers"
---

This page is for manual wireless printing from macOS Sierra (10.12) and newer.

Mobility Print Preferred

It is recommended that you first attempt Mobility Print prior to the steps below as it requires far fewer steps to print. Instructions can be found here: <https://www.papercut.com/support/resources/manuals/mobility-print/mobility-print-devices/topics/en/client-setup-ios.html>

- [Step 1 - Launch System Preferences](#WirelessPrintingformacOS-Step1-LaunchSystemPreferences)
- [Step 2 - Select Printers & Scanners.](#WirelessPrintingformacOS-Step2-SelectPrinters&Scanners.)
- [Step 3 - Add The Printer](#WirelessPrintingformacOS-Step3-AddThePrinter)
- [Step 4 - Add the desired printer](#WirelessPrintingformacOS-Step4-Addthedesiredprinter)
- [Can't Add a printer?](#WirelessPrintingformacOS-Can'tAddaprinter?)

## Step 1 - Launch System Preferences

Go to the **Apple** menu and click **System Preferences**

![arrow indicating where system preferences is in the apple menu](https://answers.atlassian.syr.edu/wiki/download/attachments/159940899/Screen%20Shot%202020-02-26%20at%208.36.51%20AM.png?api=v2)

## Step 2 - Select **Printers & Scanners**.

Printers & Scanners is located toward the bottom of the System Preferences window. Your window may look different as the window in the example is macOS 10.15 Catalina.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159940899/Screen%20Shot%202020-02-26%20at%208.38.34%20AM.png?api=v2)

## Step 3 - Add The Printer

Under the printers list click on the **+** icon to add a new printer.

![click the plus symbol to add a new device](https://answers.atlassian.syr.edu/wiki/download/attachments/159940899/Screen%20Shot%202016-06-14%20at%2012.04.20%20PM.png?api=v2)

## Step 4 - Add the desired printer

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159940899/Screen%20Shot%202020-02-26%20at%208.42.38%20AM.png?api=v2)

**How to Print**

1. Open the file you wish to print
2. Go to the **File** menu and choose **Print**. From the printer dropdown, select the printer that you want to use. (NOTE: Snow Leopard users who did not already add the "Duplex Printing Unit" will need to take an additional, one-time, step in order to print double-sided. Go to System Preferences, Print & Fax, select the double-sided printer, then select "Options & Supplies", select the "Driver" tab and check the "Duplex Printing Unit" option. Then click "OK".) Then, click the **Print** button in the file you wish to print.
3. You will be asked to log in as a "registered user". Type your SU NetID in **ad\NetID** format -- for example, **ad\jdoe.** Your password is your SU NetID password. Be sure to use your SU Login, not your Mac username **Without the ad\ your authentication will fail**.
4. Once you are sure that you have used the **ad\login** format, check the box to save your credentials in the keychain. Click **OK**.
5. Once you are ready, click **Print**.

Didn't Print?

If your document fails to print, you may need to open the print queue (from Print &Fax menu located in System Preferences), double-click on the document name in the queue and enter your credentials as directed in Step 3. If the window never pops up, you may have set up a keychain access for that. In order to remove it, search for Keychain Access and remove the password associated with wireless printing.

## Can't Add a printer?

Make sure the device has a connection to a network (wired or wireless). Is the username and password correct? You can confirm this on the [NetID self serve page](http://netid.syr.edu).

Are you using the ad\netid format when attempting to print? Revisit your configuration, make sure that everything is correct with the print server and the printer name.
