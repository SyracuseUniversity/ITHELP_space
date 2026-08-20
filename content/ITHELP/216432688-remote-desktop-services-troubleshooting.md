---
title: "Remote Desktop Services - Troubleshooting"
confluence_id: "216432688"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/216432688/Remote+Desktop+Services+-+Troubleshooting"
version: 7
last_modified: "2025-09-22T13:47:05.952Z"
status: "current"
parent_id: "159941534"
labels:
  - "remote"
  - "rds"
  - "remotedesktopservices"
---

## Overview

---

From time to time, users may experience connection problems with RDS. On this page, you’ll find solutions to commonly reported issues.

## On This Page

---

- [When RDS is Showing a Black Screen](#RemoteDesktopServices-Troubleshooting-WhenRDSisShowingaBlackScreen)
- [Missing Icons, Connection Errors, or Certificate/SSL Warnings](#RemoteDesktopServices-Troubleshooting-MissingIcons,ConnectionErrors,orCertificate/SSLWarnings)
- [Server Authentication Cerificate Error](#RemoteDesktopServices-Troubleshooting-ServerAuthenticationCerificateError)
- [Getting Help](#RemoteDesktopServices-Troubleshooting-GettingHelp)

---

### When RDS is Showing a Black Screen

###### **Issue:**

##### Black Screen

###### Solution:

##### **Sign Out & Sign Back In**

After signing in, you may encounter a black screen that persists for a period of time that looks like this:

![RDS black screen](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/image2024-9-6_15-59-2.png?api=v2)

If that happens, follow the steps below:

**Step 1:** Use a keyboard shortcut to access the menu.

On Windows: **Ctrl + Alt + End**

On MacOS: **fn + Control + Option + Backspace**

![The RDS menu that appears after using the keyboard shortcut.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/image2024-9-6_16-1-57.png?api=v2)

**Step 2:** Select the “Sign out” option from this menu. Once you are logged out, try signing into RDS again.

---

### Missing Icons, Connection Errors, or Certificate/SSL Warnings

###### **Issue:**

##### Missing Icons, Connection Errors, or Certificate/SSL Warnings

###### Solution:

##### **Clearing the Site’s Cache and Cookies**

If you notice issues such as missing icons, connection errors, or certificate/SSL warnings, a quick solution is to clear the browser cache specific to rds.syr.edu. This means you won't be erasing all your saved website data, just the data associated with the RDS site.

To remove only the cookies/cache from [rds.syr.edu](http://rds.syr.edu) on Google Chrome or Microsoft Edge, follow the steps below:

**Step 1:** Select the “View site information” icon from your browser’s address bar:

![Red arrow pointing to the site information icon in the browser's address bar, showing the tooltip 'View Site Information' - the first step in clearing the cache specific to the RDS site.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no1.png?api=v2)

**Step 2:** Click on the "Cookies and site data" tab > “Manage on-device site data” to open a new pop-up window:

![Red arrow pointing to the 'Cookies and site data' option in the site information menu.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no2.png?api=v2)![Red arrow pointing to the 'Manage on-device site data' option that appears after selecting 'Cookies and site data'  from the previous menu.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20NO3.png?api=v2)

**Step 3:** Delete the websites listed under the section titled: “Data from the site you’re visiting”.

To do so, click on the trash icons for all items listed under this section (shown below). Once they have been removed, select “Done” at the bottom of the window to finish clearing the cookies/cache that are specific to the RDS site:

![The trash icons under the 'Data from the site you're visiting' section in the 'on-device site data' menu.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDSreplacementno4.png?api=v2)

---

### Server Authentication Cerificate Error

##### Issue:

##### Server Authentication Certificate Error

##### Solution:

##### Clear the SSL Cache for your Operating System/Browsers

Encountering an unexpected server authentication certificate warning? This typically means there's a discrepancy between the server's certificate and the one your system expects. Clearing the SSL cache can help. To do so, please follow the device and browser-specific instructions below:

**Windows Computers using Google Chrome or Microsoft Edge**:

*Start Menu > Internet Options > Control panel > Clear SSL State > OK*

- Search for and open **Internet Options** from the Windows Start Menu:

![An arrow points to the Windows Start Menu, where a search has been made for 'Internet Options'. ](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no4.png?api=v2)

- In the dialogue box that appears, select the **Content** tab.

- Click **Clear SSL State** button followed by “OK” to complete the action:

!['Clear SSL state' button under the content tab of the Internet Options control panel.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no6.png?api=v2)

**MacOS Computers using Google Chrome:**

*Chrome > Kebab Menu > Delete Browsing Data > Time Range = All time > Delete Data*

- In Google Chrome, and open the kebab menu ( **⋮** ) found at the upper right corner of the browser window. Here, you’ll find the **Delete browsing data** option:

![The 'Delete browsing data' option from the Google Chrome menu.](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no8.png?api=v2)

- In the new window that appears, ensure the **Time range** drop-down menu is set to***All time***. Select “Delete data” to complete the action:

![Setting the time range menu to 'All time' in the Delete browsing data window. ](https://answers.atlassian.syr.edu/wiki/download/attachments/216432688/RDS%20no9.png?api=v2)

---

### Getting Help

---

We're here to ensure you have a smooth experience with RDS. If you need assistance:

- **Students**: Feel free to reach out to the [ITS Help Desk](https://its.syr.edu/its_service_center/) directly. Call us at 315-443-2677, email at [help@syr.edu](mailto:help@syr.edu), or drop by in person at the ITS Service Center. Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.
- **Faculty and Staff**: For the most efficient support, it's recommended to start with your respective [academic](https://its.syr.edu/contact_its/school-and-college-support-contact-information/) or [administrative](https://its.syr.edu/contact_its/departmental-support-contact-information/) support teams. They're equipped with tools and knowledge tailored to your needs.
