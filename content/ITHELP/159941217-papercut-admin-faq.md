---
title: "PaperCut Admin FAQ"
confluence_id: "159941217"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941217/PaperCut+Admin+FAQ"
version: 18
last_modified: "2021-06-23T18:48:42.000Z"
status: "current"
parent_id: "159941207"
labels:
  - "s17"
---

The following page will provide answers to common questions organizational unit administrators may have regarding managing servers and devices, as well as the PaperCut administrative interface. 

- [PaperCut Admin FAQ](#PaperCutAdminFAQ-PaperCutAdminFAQ)
  - [What is PaperCut?](#PaperCutAdminFAQ-WhatisPaperCut?)
  - [Where do I install PaperCut?](#PaperCutAdminFAQ-WheredoIinstallPaperCut?)
  - [How do I add a new printer?](#PaperCutAdminFAQ-HowdoIaddanewprinter?)
  - [I set up a new printer and jobs go through to the print server but never print. Why is this?](#PaperCutAdminFAQ-Isetupanewprinterandjobsgothroughtotheprintserverbutneverprint.Whyisthis?)
  - [Where is the admin interface?](#PaperCutAdminFAQ-Whereistheadmininterface?)
  - [How do I get admin interface access?](#PaperCutAdminFAQ-HowdoIgetadmininterfaceaccess?)
  - [How do I provide admin role(s) access to OU staff?](#PaperCutAdminFAQ-HowdoIprovideadminrole(s)accesstoOUstaff?)
  - [Can staff have more than one admin role?](#PaperCutAdminFAQ-Canstaffhavemorethanoneadminrole?)
  - [How do I enable printing for a faculty member that is an adjunct or alumni?](#PaperCutAdminFAQ-HowdoIenableprintingforafacultymemberthatisanadjunctoralumni?)
  - [How can I add additional specialty printing items to the Purchase Items interface in Web Cashier?](#PaperCutAdminFAQ-HowcanIaddadditionalspecialtyprintingitemstothePurchaseItemsinterfaceinWebCashier?)
  - [Who can provide refunds?](#PaperCutAdminFAQ-Whocanproviderefunds?)
  - [How can my OU enable email to print?](#PaperCutAdminFAQ-HowcanmyOUenableemailtoprint?)
  - [How is reporting accomplished?](#PaperCutAdminFAQ-Howisreportingaccomplished?)
- [Getting Help](#PaperCutAdminFAQ-GettingHelp)

# PaperCut Admin FAQ

### What is PaperCut?

A [web-based interface](http://printing.syr.edu/admin) allows administrators to install, manage, and update their department's printing environment.

### Where do I install PaperCut?

Papercut is installed by adding a [new](https://su-jsm.atlassian.net/wiki/x/_oKICQ) or [existing](https://su-jsm.atlassian.net/wiki/x/coKICQ) print server to the PaperCut server group. If converting an existing server, be sure to [remove PMP](https://su-jsm.atlassian.net/wiki/x/yIKICQ) and confirm that [printers have PaperCut ports](https://su-jsm.atlassian.net/wiki/x/8IKICQ)

### How do I add a new printer?

New printers need to first be [installed](https://su-jsm.atlassian.net/wiki/x/d4KICQ) and [configured](https://su-jsm.atlassian.net/wiki/x/8IKICQ) on the print server. They can then be further [configured in the PaperCut admin interface](https://su-jsm.atlassian.net/wiki/x/wIKICQ)

### I set up a new printer and jobs go through to the print server but never print. Why is this?

In the PaperCut admin interface, go to the Filters & Restrictions tab and make sure Group Restriction is active and then enabled for your groups on the list. This is covered on the [Printers - Managing Printer Settings page](https://su-jsm.atlassian.net/wiki/x/wIKICQ)

### Where is the admin interface?

The PaperCut admin interface is located at [printing.syr.edu/admin](https://printing.syr.edu/admin)

### How do I get admin interface access?

Access is based on user enrollment in admin groups on a department level. OU administrators should gain the role of <OU> - PaperCut Admin. Administrative access should be granted within one hour.

### How do I provide admin role(s) access to OU staff?

As with OU admin access, this is based on user enrollment in admin groups on a department level. New employees should be added to the group of the administrative role desired (ex: <OU> - PaperCut Web Cashier; <OU> - PaperCut Refund Jobs). Once added to a role group, the staff will have [administrative access based on the role](https://su-jsm.atlassian.net/wiki/x/V4KICQ) within one hour.

### Can staff have more than one admin role?

Yes. Simply add the staff to the groups reflecting the role(s) you'd like their access to encompass. The staff will have [administrative access based on the role](https://su-jsm.atlassian.net/wiki/x/V4KICQ) within one hour.

### **How do I enable printing for a faculty member that is an adjunct or alumni?**

Note that only active student, staff or faculty account will have account present in PaperCut. The status of a faculty member should first be addressed by the organizational unit if they are not currently in active status. Please contact the PMTT at [pmtt@syr.edu](mailto:pmtt@syr.edu) in the event you require manual intervention regarding an adjunct or alumni PaperCut account.

Once the user is active in PaperCut they may still not a member of the built-in group [OU]-Faculty-Active. Add them to [OU]-RSC-Papercut-Faculty to enable printing. This step will process in an overnight update.

### How can I add additional specialty printing items to the Purchase Items interface in Web Cashier?

The item types listed in the Purchase Items interface will be limited by organizational unit. They are currently limited to five per organizational unit. OU admins can request additional specialty printing items by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu)

### Who can provide refunds?

Admins in the Refund Jobs role can provide refunds for printers within their OU. Full-time staff in the ITS Service Center can provide refunds to public printers.

### How can my OU enable email to print?

Email to print is off by default. To request email to print, send an email to [pmtt@syr.edu](mailto:pmtt@syr.edu)

### How is reporting accomplished?

Users in the OU admin role should use [filtering and printing of logs](https://su-jsm.atlassian.net/wiki/x/aoKICQ) for reporting.

# Getting Help

If you have general questions or are having technical difficulties with SU's printing management system, contact the print management technical team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu)

You are also welcome to review [PaperCut's FAQ documentation](http://www.papercut.com/faq/).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941217/PaperCut+Admin+FAQ#PaperCutAdminFAQ-topofpage)
