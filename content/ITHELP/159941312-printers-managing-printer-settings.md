---
title: "Printers - Managing Printer Settings"
confluence_id: "159941312"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941312/Printers+-+Managing+Printer+Settings"
version: 16
last_modified: "2024-01-12T12:48:01.000Z"
status: "current"
parent_id: "159941251"
labels:
  - "s17"
---

The following page details how to manage a printer within your group using the administrative interface.

Manage Printers Carefully

The current administrative interface prevents the PMTT from limiting printer settings access for individual users. Avoid changing printer settings for printers outside of the intended print group.

Printers Must First Be Installed

Note that you are unable to initially install a new printer within the administrative interface. If you have a new printer you'd like added to your group, please refer to the [Installing New Printers page](https://su-jsm.atlassian.net/wiki/x/d4KICQ).

- [Managing Printer Settings](#Printers-ManagingPrinterSettings-ManagingPrinterSettings)
  - [Managing Individual Printers](#Printers-ManagingPrinterSettings-ManagingIndividualPrinters)
    - [Configurations](#Printers-ManagingPrinterSettings-Configurations)
    - [Hold/Release Queue Settings](#Printers-ManagingPrinterSettings-Hold/ReleaseQueueSettings)
    - [Printer/Device Groups](#Printers-ManagingPrinterSettings-Printer/DeviceGroups)
    - [Filters & Restrictions (optional)](#Printers-ManagingPrinterSettings-Filters&Restrictions(optional))
    - [Job Log](#Printers-ManagingPrinterSettings-JobLog)
    - [Print/Export Job Log](#Printers-ManagingPrinterSettings-Print/ExportJobLog)
  - [Copy Settings Between Printers](#Printers-ManagingPrinterSettings-CopySettingsBetweenPrinters)
  - [Reviewing Printer Statistics](#Printers-ManagingPrinterSettings-ReviewingPrinterStatistics)

# Managing Printer Settings

Users in the Admin role can manage the settings of printers within their departmental environment. To do so, navigate to the Printers Tab. The Printer List sub-tab will be displayed by default.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/printersloc.PNG?api=v2)

Once there, the steps below will be available.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941312/Printers+-+Managing+Printer+Settings#Printers-ManagingPrinterSettings-topofpa)

## Managing Individual Printers

To manage an individual printer, locate the Printer List subtab as shown in the image above. By default, only printers in your printer group will be visible. Click on the name of the printer you'd like to manage to be taken to the Print Details page.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/printerlist.PNG?api=v2)

Follow the steps below to navigate through the various Printer Detail tab sub-tabs. Be sure to click Apply to save all setting changes.

Manage the Settings Below Only

While other printer settings may appear changeable, it is recommended that only the settings below be changed.

Advanced Scripting Not Supported

Note that while the scripting sub-tab may be available, advanced scripting is not supported by the print management technical team.

#### Configurations

The configurations section will give an overview of printer information and allow administrators to change the location of the printer, link to the charging scheme, enable and disable the printer, and determine the queue type.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/config.PNG?api=v2)

If the default cost per page and charging scheme needs to be changed, click standard or the Charging sub-tab above to reveal more advance payment options for this printer.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/charge.PNG?api=v2)

#### Hold/Release Queue Settings

OU admins can also determine if a printer will have a hold/release queue enabled. To do so, simply check the enable box in the Hold/Release Queue Settings in the Summary tab.

Requires Additional Filtering

When Hold/Release is enabled on a printer, it shows up in the mobile interface. If you enable this option, you also need to filter the access so it’s not available to everyone seeking to print using the mobile interface.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/h-r.PNG?api=v2)

#### Printer/Device Groups

The next setting needing attention is the Printer/Device Groups. Admins should restrict their printers to only allow indicated groups to print.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/printgroups.PNG?api=v2)

Clicking on the drop down will reveal an alphabetical list of groups that can be added to print at this location.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/dropdown.PNG?api=v2)

#### Filters & Restrictions (optional)

An important setting within the Filters & Restrictions tab is the Group Restriction. If you don’t set this, print jobs will appear to go through to the server but will not print.

Enable this setting and then browse the unsorted list for your groups and enable.

The three base groups of interest for your OU are usually:

- SU-[OU]-RSC-Papercut-Staff
- SU-[OU]-RSC-Papercut-Faculty
- SU-[OU]-RSC-Papercut-Students

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/groups.PNG?api=v2)

#### Job Log

The job log sub-tab will reveal the jobs that occurred on the selected printer. Included statistics will be the date of the print job, user who printer, pages printed, cost of the print job, name and format of the document, print job details, and the status.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/joblog2.PNG?api=v2)

Clicking edit at the top will reveal advanced filtering options. Be sure to click Apply Filter in the lower right to apply the selected filter options.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/filterlist2.PNG?api=v2)

The status column will be of particular interest. Here you can see if each job was successfully printed, cancelled, or if a refund has been provided.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/status2.PNG?api=v2)

#### Print/Export Job Log

You can easily print or export the default or filtered job log for this printer with the options at the bottom of the screen.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/exportprint.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941312/Printers+-+Managing+Printer+Settings#Printers-ManagingPrinterSettings-topofpa)

## Copy Settings Between Printers

Copying & Notifications

While your admin role may not restrict access to use the **Copying settings from printer to printer** or **Notifications options** areas no administrator is permitted to make changes or alter the settings found in these locations. If you would like more information on either copying printer settings or notification settings contact the print management technical team at [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941312/Printers+-+Managing+Printer+Settings#Printers-ManagingPrinterSettings-topof)

## Reviewing Printer Statistics

Another feature of the Printers tab allows users to view statistics related to the printers in their print group. To do so, click on View statistics in the Actions menu.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/printeractions2.PNG?api=v2)

The Charts page will reveal filtering options for time frame via a drop down menu. Once the time frame and printers are selected.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941312/stats.PNG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941312/Printers+-+Managing+Printer+Settings#Printers-ManagingPrinterSettings-topofpage)
