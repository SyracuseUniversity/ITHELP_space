---
title: "Check OS Installation Dates"
confluence_id: "159940745"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159940745/Check+OS+Installation+Dates"
version: 30
last_modified: "2022-12-14T18:13:07.000Z"
status: "current"
parent_id: "159942502"
labels:
  - "windows"
  - "macos"
  - "openreview2014"
  - "revwnov12"
  - "quarantine"
---

How to check OS install dates for quarantined statuses.

---

- [Check OS Installation Dates on Windows](#CheckOSInstallationDates-CheckOSInstallationDatesonWindows)
- [Check OS Installation Dates on macOS (Yosemite and El Capitan)](#CheckOSInstallationDates-CheckOSInstallationDatesonmacOS(YosemiteandElCapitan))
- [Check OS Installation Dates on macOS (Catalina and Above)](#CheckOSInstallationDates-CheckOSInstallationDatesonmacOS(CatalinaandAbove))

---

## Check OS Installation Dates on Windows

1. *Hold* *down* the **Windows Key** and *Press* **R** on your keyboard.
2. *Type* in **cmd** and *Press***CTRL + SHIFT + ENTER.**
3. *Type* in **systeminfo** and *Press***ENTER.**

![Command prompt window showing the original install date](https://answers.atlassian.syr.edu/wiki/download/attachments/159940745/original_install_date.png?api=v2)

---

## Check OS Installation Dates on macOS (Yosemite and El Capitan)

1. Open the console window in the Utilities folder, as outlined above.
2. Navigate to /var/log, then click on install.log
3. Scroll all the way to the top of the list, until you see a series of text that says "OSInstaller" 

   ![Console Window 2](https://answers.atlassian.syr.edu/wiki/download/attachments/159940745/Screen%20Shot%202015-11-12%20at%209.16.26%20AM.png?api=v2)
4. The date next to the text is the install date.

---

## Check OS Installation Dates on macOS (Catalina and Above)

1. Open the console application found in Applications > Utilities > Console
2. In the sidebar select "Log Reports"
3. In the top half of the window select "install.log"
4. The lower half of the log window scroll up to the earliest possible date to see the install date.

   Note

   The earliest date will either be when the computer was first set after being purchased or from the last clean install. If a computer is upgraded there will be an install log on the date of the install recording the upgrade.

![Screenshot of Console Log](https://answers.atlassian.syr.edu/wiki/download/attachments/159940745/Screen%20Shot%202019-10-28%20at%209.49.16%20AM.png?api=v2)

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=toplink&locale=en_US&version=2)
