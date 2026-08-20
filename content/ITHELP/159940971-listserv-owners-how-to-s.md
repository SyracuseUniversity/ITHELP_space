---
title: "Listserv Owners How-To's"
confluence_id: "159940971"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159940971/Listserv+Owners+How-To+s"
version: 56
last_modified: "2025-11-06T16:58:08.377Z"
status: "current"
parent_id: "159940753"
---

Below you will find instructions to common Listserv list owner tasks. Owners looking to make changes to the way their list mail is delivered should reference the commands available on the [Listserv Subscribers How-To's page](https://su-jsm.atlassian.net/wiki/x/-4OICQ). Users may also find step-by-step instructions under 'Tips for Owners' on the [Listserv manuals page](http://www.lsoft.com/resources/manuals.asp).

**Need a password?** If you are logging in for the first time or have forgotten your Listserv password simply follow the instructions on the [Listserv password page](https://listserv.syr.edu/scripts/wa.exe?GETPW1).

**Need to create or delete a list?** Please use the forms and information found on the [Creating and Deleting Lists page](https://su-jsm.atlassian.net/wiki/x/GoKICQ).

- [Listserv List Management Interface](#ListservOwnersHow-To's-ListservListManagementInterface)
- [Listserv Security](#ListservOwnersHow-To's-ListservSecurity)
- [General List Management](#ListservOwnersHow-To's-GeneralListManagement)
  - [Add an Owner to Your List](#ListservOwnersHow-To's-AddanOwnertoYourList)
  - [Managing Messages to List Owners](#ListservOwnersHow-To's-ManagingMessagestoListOwners)
  - [Managing List Content & Out of Office Messages](#ListservOwnersHow-To's-ManagingListContent&OutofOfficeMessages)
  - [Enabling List Digests](#ListservOwnersHow-To's-EnablingListDigests)
  - [Archiving Lists](#ListservOwnersHow-To's-ArchivingLists)
- [Managing Subscribers](#ListservOwnersHow-To's-ManagingSubscribers)
  - [Reviewing Current Subscribers](#ListservOwnersHow-To's-ReviewingCurrentSubscribers)
  - [Adding Subscribers in Bulk](#ListservOwnersHow-To's-AddingSubscribersinBulk)
  - [Deleting Subscribers](#ListservOwnersHow-To's-DeletingSubscribers)
  - [Requesting a Smart Listserv for subscriber management](#ListservOwnersHow-To's-RequestingaSmartListservforsubscribermanagement)
- [Getting Help](#ListservOwnersHow-To's-GettingHelp)

---

## Listserv List Management Interface

Log into the Listserv List Management Interface:

[Listserv Management Page](https://listserv.syr.edu/scripts/wa.exe?LOGON)

This link is for Listserv owners looking to manage or moderate their lists.

Additional Listserv tutorials, including using the list management interface, can be found on the [Listserv manuals page](http://www.lsoft.com/resources/manuals.asp).

![Listserv_Login_Page.png](https://answers.atlassian.syr.edu/wiki/download/attachments/159940971/Listserv_Login_Page.png?api=v2)

---

## Listserv Security

Listserv controls access with an email address/password combination that it manages. Listserv does not know about your Syracuse University NetID or any other account, and Listserv passwords are exclusively linked to an email address. Further, passwords are **not** linked to a list or to you personally.

While we commonly say that a person (yourself!) owns a list, lists are actually owned by an email address(es). Therefore, when your email address changes, you will likely lose the ability to manage your list (you may still be able to login using your old email address and password, but if Listserv asks for email confirmation of a command- which it does for the most sensitive operations- you will be unable to complete the confirmation).

Bottom line, your email address and associated Listserv password are the key to managing your list, and should be guarded like any other personal account. YOU CANNOT GIVE YOUR PASSWORD TO ANOTHER PERSON in order to transfer list ownership. Note that this is also true for subscribers and their ability to manage their subscriptions.

---

## General List Management

The majority of management tasks are easily located within the list management interface. Below are some additional list owner tasks. Technical users can also reference both the [Advanced List Owner Configurations page](https://su-jsm.atlassian.net/wiki/x/joGICQ) as well as the the [L-Soft Listserv Manual](http://www.lsoft.com/resources/manuals.asp).

### Add an Owner to Your List

1. Log into the list management interface.
2. Select the "List Dashboard" option on the "List Management" drop-down menu. This will show the lists you own, click on the name of the list you want to modify.
3. Choose "List Configuration" from the List Management drop-down menu.
4. Select "Edit Manually"
5. Carefully make any changes (like adding an additional "owner=" line specifying the additional owner), and click the Update button.

### Managing Messages to List Owners

Owners may want to receive more or fewer list management and error messages, or where the errors are sent. The following parameters are available in this list management interface:

- Quiet - Owners do not receive normal list messages. Note that there must be at least one non-quiet owner.
- Errors-to - Designate owners to receive error messages.
- Auto-Delete - Control BOTH the automatic removal of invalid addresses, and the messages you receive about undeliverable postings (bounces). This can be very useful on a busy list with several postings per day, but useless on infrequently used lists.

### Managing List Content & Out of Office Messages

Content filtering is most commonly used to restrict "Out of Office" (Vacation) messages, although other types of messages can be filtered as well. Consequently, Listserv has a default site wide filter which includes the most common "Out of Office" messages. List owners can customize this filter by adding other filters (it's not limited to "Out of Office" messages), or you may wish to allow "Out of Office" messages.

Technical users should reference the [Listserv manual](http://www.lsoft.com/resources/manuals.asp) for configuration. Alternatively, users may contact the [ITS Help Desk](http://its.syr.edu/supportsvc) by calling at 315-443-2677, by emailing [help@syr.edu](mailto:help@syr.edu), or by visiting us at the ITS Service Center. Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.

### Enabling List Digests

Listserv list owners may request that digests be enabled for their list. Digests can only be enabled by the Listserv Administration. List owners should direct request to enable digest to the [ITS Help Desk](http://its.syr.edu/supportsvc) by calling at 315-443-2677, by emailing [help@syr.edu](mailto:help@syr.edu), or by visiting us at the ITS Service Center. Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.

Once enabled,  list owners can have digest be automatically enabled for all NEW suscribers. This can be done by adding the following line to the list configuration: Default-Options=Digest.

List owners can use the following email command to set digenst for an individual subscriber: set <listname> digest for <useremail>

### Archiving Lists

By default, this archive feature is not enabled and this feature must be requested by the list owner. To archive a list, contact the [ITS Help Desk](http://its.syr.edu/supportsvc) by calling at 315-443-2677, by emailing [help@syr.edu](mailto:help@syr.edu), or by visiting us at the ITS Service Center. Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.

Once archived, the archived messages can be viewed in the list management interface. You must be at least a subscriber to the list in order to access the list's archive, if the archives are designated as private.  To access private archives:

1. Login to the Listserv Web Interface.
2. Click on the "Subscriber's Corner" link on the toolbar.  The lists you have subscribed to will be displayed on the page.
3. Click the list name whose archive you want to view.  Navigate the archive screen in a manner as described in step 3 of the previous section.

---

## Managing Subscribers

Listserv has subscriber management option through the list management interface. After choosing the list in "List Dashboard", Choose "List Management>Subscriber Management". Below you will find additional options.

### Reviewing Current Subscribers

- Option 1: In subscriber management, go to the bottom of the page and choose either of the links following the text "Review List Members:"
- Option 2: After you have selected a list in the list management interface, choose menu item "List Management >List Reports>Subscriber Reports." You can change any subscriber information here.

Note that most lists are configured so that list members CANNOT review the list. This avoids "drive by" harvesting where someone subscribes to a list, gets the list membership, leaves the list, and then spams the list.

### Adding Subscribers in Bulk

Listserv has a bulk subscriber load interface accessible through the list management interface (Located in List Management>Subscriber Reports>Bulk Operations), however, Listserv can load a plain text file\* from your computer with the following format, with a space between the address and the optional name:

myaddr@syr.edu Firstname lastname
myaddr2@syr.edu Firstname2 lastname2

While the name is not required. If you don't have a name, you can omit it or substitute a single asterisk (\*) for the name.

There are several load options: please read them carefully as some add to the existing subscriber list and some replace the subscriber list.

\*Please note when selecting your file name, select Text (Tab delimited) (\*.txt) as your file type and click Save. This will produce a file that LISTSERV's bulk upload feature can accept.

### Deleting Subscribers

While Listserv has options to manage subscribers in the subscriber management interface, additional commands are available. The "quiet" form of the commands is often recommended. Quiet means that the user being deleted will not get notification. This command is often used to delete obsolete addresses, or to delete all members of a class list. Therefore notification is either unnecessary, or in the case of obsolete addresses, could not be delivered.

Send an email message to [listserv@listserv.syr.edu](mailto:listserv@listserv.syr.edu) containing one or more of the following commands:

1. delete listname userid@node Example: delete sasusers [abzmith@mailbox.syr.edu](mailto:abzmith@mailbox.syr.edu).
2. quiet delete listname userid@node Example: quiet delete sasusers [abzmith@mailbox.syr.edu](mailto:abzmith@mailbox.syr.edu).
3. For multiple deletions, or for the deletion of the entire subscribers' list, the command should be (the "quiet" form is highly recommended): quiet delete listname \* or delete listname \*

### Requesting a Smart Listserv for subscriber management

A Smart Listserv is a type of mailing list that automatically updates its membership based on certain criteria or conditions in a query that runs against SU's data warehouse (DW). Unlike a static mailing list where members must be added or removed manually.

To request a listserv be changed to a DW query, click the link below and enter the required information. The DW team will work with you to fine-tune the query to dynamically capture the correct members. Once finalized, they will send the finished query to the administrators to be used for your listserv.

[**Smart Listserv Request**](https://support.atlassian.syr.edu/servicedesk/customer/portal/89/group/89/create/1383)

---

## Getting Help

Subscribers and list members should contact their list owner(s) for assistance by emailing <listname-request@listserv.syr.edu>. For example, if the listserv is clocks@listserv.syr.edu, send email to <clocks-request@listserv.syr.edu>.

Additional Listserv instructions, including how-to instructions and videos, can be found on the [Listserv manuals page](http://www.lsoft.com/resources/manuals.asp).

For support of the information above, contact the [ITS Help Desk](http://its.syr.edu/supportsvc) by calling at 315-443-2677, by emailing [help@syr.edu](mailto:help@syr.edu), or by visiting us at the ITS Service Center. Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.

[Top](https://su-jsm.atlassian.net/wiki/display/scpay101/Listserv+Errors+and+Troubleshooting#com-atlassian-confluence)
