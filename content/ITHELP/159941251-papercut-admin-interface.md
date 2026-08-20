---
title: "PaperCut Admin Interface"
confluence_id: "159941251"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface"
version: 69
last_modified: "2017-06-05T13:35:54.000Z"
status: "current"
parent_id: "159941207"
labels:
  - "printing"
  - "instructions"
  - "s17"
  - "admin"
  - "interface"
  - "papercut"
---

The following page will help familiarize users with administrative access to the tabs and functions of PaperCut's administrative interface. Following the instructions or click the links within a tab section for details regarding key functions within each admin interface tab.

Managing Administrative Roles

Note that administrative access is not managed within the PaperCut admin interface. Access is based on user enrollment in admin groups on a department level. New employees should be added to the group of the administrative role desired. If you feel you should have access to a particular role, please contact your [organizational unit administrator](http://its.syr.edu/contactus.html). 

- [Administrative Tabs](#PaperCutAdminInterface-AdministrativeTabs)

  - [Tab Access Restrictions](#PaperCutAdminInterface-TabAccessRestrictions)- [Dashboard](#PaperCutAdminInterface-Dashboard)
  - [Users](#PaperCutAdminInterface-Users)
    - [Users Actions](#PaperCutAdminInterface-UsersActions)
    - [Users - Finding and Filtering User Lists](#PaperCutAdminInterface-Users-FindingandFilteringUserLists)
    - [Users - Service Center Refunds](#PaperCutAdminInterface-Users-ServiceCenterRefunds)
  - [Printers](#PaperCutAdminInterface-Printers)
    - [Printers Actions](#PaperCutAdminInterface-PrintersActions)
    - [Printers - Managing Printer Settings](#PaperCutAdminInterface-Printers-ManagingPrinterSettings)
    - [Printers - Managing Hold/Release Queues](#PaperCutAdminInterface-Printers-ManagingHold/ReleaseQueues)
    - [Printers - Refunding Failed Print Jobs](#PaperCutAdminInterface-Printers-RefundingFailedPrintJobs)
  - [Logs](#PaperCutAdminInterface-Logs)
    - [Logs - Filtering Logs and Printing Reports](#PaperCutAdminInterface-Logs-FilteringLogsandPrintingReports)
  - [Web Cashier Interface](#PaperCutAdminInterface-WebCashierInterfacewebcashier)
    - [Web Cashier - Applying Funds](#PaperCutAdminInterface-WebCashier-ApplyingFunds)
    - [Web Cashier - Processing Purchases](#PaperCutAdminInterface-WebCashier-ProcessingPurchases)
- [Getting Help](#PaperCutAdminInterface-GettingHelp)

# Administrative Tabs

By default, each user will see every tab regardless of role. Access to each tab will be based on user's administrative role as indicated in the grid below. Please see the [Web Cashier](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-webcashier) section below for details regarding logging into the web cashier interface.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/tabs.PNG?api=v2)

|  | Dashboard | Users | Printers | Logs | Web Cashier |
| --- | --- | --- | --- | --- | --- |
| Refund Jobs |  |  | X |  |  |
| Hold Release |  |  | X |  |  |
| Web Cashier |  |  |  |  | X |
| (OU) Admin | X | X | X | X |  |
| SVC Admin | X | X |  | X |  |

### Tab Access Restrictions

Users who attempt to click on tabs and features that are not granted by their administrative role as indicated the grid above will receive an error message similar to the one below and be returned to the initial login screen. 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/denied.PNG?api=v2)

Other Tabs

Note that while the Groups, Accounts, Devices, Reports, and Options are visible in the administrative interface, no administrative role will grant access to these spaces.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

## Dashboard

Administrative accounts that see the dashboard will see a default breakdown of the SU print environment. This dashboard represents that entire environment, not just your individual department(s).

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/dashboard.PNG?api=v2)

Default applets on the dashboard include:

- System Status - The status of the entire PaperCut environment.
- Pages Printed - Graphical representation of the total pages printed in the last 30 days by day.
- Environmental Impact - PaperCut's calculation of the current print usage as it relates to environmental impact.
- Printer Status - Each printer's status and toner indication, if low.
- News - Information provided from PaperCut regarding their product and services.
- Real-time Activity - All administrative interface activity by user and action.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/dashboardcontent.PNG?api=v2)

Not Customizable

Unfortunately, there is currently no options to configure the dashboard beyond the default applets displayed.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

## Users

The Users tab is restricted to administrators in the Admin and SVC Admin roles.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/userlist.PNG?api=v2)

#### Users Actions

Administrators can only use "Export/Print" and "User printing- summary (last 30 days)" in the Actions window. Export/Print will allow an administrator to print the currently shown results or export to Excel, PDF, or web link. The 30-day summary will allow the same options and include usage of the filtered results for the past 30 days.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/actionsedit.png?api=v2)

Bulk User Actions

In some cases, your department may be required to make bulk user actions, such as bulk changes to user account balances. If you require a bulk user action, contact the Print Management Technical Team by emailing [pmtt@syr.edu.](mailto:pmtt@syr.edu.)

#### [Users - Finding and Filtering User Lists](https://su-jsm.atlassian.net/wiki/x/N4KICQ)

#### [Users - Service Center Refunds](https://su-jsm.atlassian.net/wiki/x/3oKICQ)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

## Printers

Access to the Printers tab is restricted to administrators in the Refund Jobs, Hold Release, and Admin roles.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/printers.PNG?api=v2)

#### Printers Actions

Administrators can use the actions found in the Printers tab. Each of the available Printers tabs and actions will be restricted based on role. Permitted tasks include reset the print statistics of their location's printers, viewing the jobs pending release queue and providing refunds for failed print jobs. **DO NOT CHANGE COPY OR NOTIFICATION SETTINGS**. 

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/printeractionsedit.png?api=v2)

Copying & Notifications

While your admin role may not restrict access to use the **Copying settings from printer to printer** or **Notifications options** areas no administrator is permitted to make changes or alter the settings found in these locations. If you would like more information on either copying printer settings or notification settings contact the print management technical team at [pmtt@syr.edu](mailto:pmtt@syr.edu).

#### [Printers - Managing Printer Settings](https://su-jsm.atlassian.net/wiki/x/wIKICQ)

#### [Printers - Managing Hold/Release Queues](https://su-jsm.atlassian.net/wiki/x/9YKICQ)

#### [Printers - Refunding Failed Print Jobs](https://su-jsm.atlassian.net/wiki/x/bIKICQ)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

## Logs

Administrators with access to the Logs tab will be able to produce reports regarding the printers in their location(s). The log will allow an administrator to see each print job including page counts, costs, documents printed, detailed print attributes (duplex, grayscale, etc.), if the print was successful or canceled, and if the cost refunded.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/joblog.PNG?api=v2)

#### [Logs - Filtering Logs and Printing Reports](https://su-jsm.atlassian.net/wiki/x/aoKICQ)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

## Web Cashier Interface

The web cashier is restricted to administrators in the Web Cashier role. The interface is accessed at [printing.syr.edu/webcashier](https://printing.syr.edu/webcashier). Note that administrators in the web cashier role will not be able to log into the administrative interface.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941251/webcashier.PNG?api=v2)

#### [Web Cashier - Applying Funds](https://su-jsm.atlassian.net/wiki/x/44KICQ)

#### [Web Cashier - Processing Purchases](https://su-jsm.atlassian.net/wiki/x/1oKICQ)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu.](mailto:pmtt@syr.edu.)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941251/PaperCut+Admin+Interface#PaperCutAdminInterface-ToC)
