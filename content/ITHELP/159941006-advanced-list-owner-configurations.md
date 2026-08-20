---
title: "Advanced List Owner Configurations"
confluence_id: "159941006"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941006/Advanced+List+Owner+Configurations"
version: 9
last_modified: "2025-03-15T12:44:44.674Z"
status: "current"
parent_id: "159940971"
labels:
  - "listserv"
  - "owner"
  - "password"
  - "for_listserv_owners"
---

This document describes how to change list configuration information such as list ownership, editors, subscription options and more.

- [Accessing the Listserv Configuration Information](#AdvancedListOwnerConfigurations-AccessingtheListservConfigurationInformation)
- [Editing the List Configuration](#AdvancedListOwnerConfigurations-EditingtheListConfiguration)
- [Change Configuration](#AdvancedListOwnerConfigurations-ChangeConfiguration)
- [Updating HDR and MSTP Settings (Messages Unreadable)](#AdvancedListOwnerConfigurations-UpdatingHDRandMSTPSettings(MessagesUnreadable))
- [Getting Help](#AdvancedListOwnerConfigurations-GettingHelp)

---

## Accessing the Listserv Configuration Information

1. Go to the web page of [Listserv](http://listserv.syr.edu).
2. Click on the "List Management Interface" Link.
3. Login if necessary (if you have already used the Listserv web page, Listserv can be configured to automatically log you in).
4. Choose "List Management>List Dashboard: from the menu
5. Click on [Configure](#) underneath the list you will be editing.
6. Click on the Save button when you're done.

---

## Editing the List Configuration

Following is a sample list configuration with some common parameters- this is an incomplete list, and some may not apply to your list. If you need more information, please go [here](http://listserv.syr.edu).

\*Test List Description
\* Review= Owner Subscription= Open,Confirm Send= Private
\* Reply-to= Sender,Respect
\* Validate= Yes,Confirm
\* Confidential= Yes
\* Attachments= No
\* Default-options= Repro
\* Digest= No
\* Service= \*
\* Owner= jeandoe@syr.edu (Jean Q. Doe, 315-999-9999)

- General information Keywords and Parameters are generally of the form:
  Keyword= Parameter, e.g. [answers31:Send=Private]
  - We recommend you put new keywords on a line by themselves. Although you may put multiple keywords, especially Owner, Editor, and Moderator lines can get cluttered if you do.
  - Keywords may be in any order, but we recommend putting Owner information at the end.
  - Listserv will usually not allow you to save incorrectly formatted information, and will catch most errors. You may not always get the result you expected, but you probably won't disable your list.
  - After typing your changes, click on the Save button. Reload will discard your changes (back to the last Update)

---

## Change Configuration

The owner line is as follows:

- Owner= username@mydomain (optional description text, such as name and phone number)
  Example: Owner= jeandoe@syr.edu (Jean Q. Doe, 315-000-0000)
  - to remove an owner, delete the entire line
  - to add an owner, add a line of the above format.
  - owner lines may go anywhere, but by convention they are usually the last items
  - you may put multiple owners on a single line, but we recommend one owner per line
  - If you do not want an owner to receive notices and error messages, use the following format:
    Owner= Quiet:, jeandoe@syr.edu
    Be sure to include the : (colon) and the , (comma)
    THE QUIET KEYWORD MEANS ALL SUBSEQUENTLY LISTED OWNERS ARE QUIET, i.e., you only need to specify Quiet once. In the following example, sbrown & jchin are quiet:
    Owner= rblumen@syr.edu
    Owner= Quiet:, sbrown@syr.edu
    Owner= jchin@syr.edu
  - WE HIGHLY RECOMMEND HAVING AT LEAST 2 OWNERS. Lists must have at least one viable owner or risk being removed. For example, with lists owned by students, it's common for email addresses to become inactive at graduation. A second or third owner will probably stay viable when others become inactive.
  - At least one of the owner addresses must be @...syr.edu or @esf.edu.

- the list description is usually the top configuration line. You may change this but we suggest you keep it shorter than 60 characters.

- List Creation Date: please do not edit.
- Review=: Who can find out list membership. We highly recommend this be only set to
  - Review= Owner
  - It is very common for spammers to subscribe to a list, get all of the subscriber's emails, leave the list, and spam everyone, so do not use Review=Private.
- Subscription= process:
  - Subscription= Open, Confirm Anyone can subscribe, but Listserv will verify it's a valid email address. This is what we recommend.
  - Subscription= By\_Owner Only the owner can subscribe people. Given most folk's occasional fumble-fingers, this usually results in a few incorrect subscriptions. Especially for a new list, you may wish to consider starting with Open, Confirm, and then switching to By\_Owner after most people are subscribed.

- Send=: Who can send to the list:
  - Send= Private only list members. The From: line in their email must match their subscription.
  - Send= Public anyone. Use with caution.
  - Send= Editor, Hold require confirmation by a moderator
- Reply-To=: controls the Reply-To field in mail outgoing from Listserv. When a list subscriber receives a posting and wants to respond, this field tries to control where the response will be sent. This field guarantees nothing, but relies on the subscriber's email program and subscriber's behavior to have any effect.
  The following uses this example: jeandoe@syr.edu sends to a list Clocks, and a subscriber (recipient) responds.
  - Reply-to= Sender, Respect Sets the Reply-To field to point to the original sender. In our example, the response would go to jeandoe@syr.edu.
  - Reply-to= List, Respect In our example, the reply would go to the Clocks list.
- Validate=. This controls whether and how Listserv validates commands. Change this at your own peril, unless you want to allow spammers to modify your list without your knowledge.
  - Validate=Yes,Confirm or Validate= Yes (these are acceptable values)
- Confidential=. This should almost always be Confidential=Yes. Confidential controls if the list is advertised in Listserv's global directory, and "yes" means don't advertise it. While you may think you want it advertised, the people most likely to find it here are spammers. Other advertising mechanisms are much more effective.
- Attachments: to enable or disable attachments, change (or add) the line
  - Attachments=Yes or Attachments= No
    You can also allow particular attachment types- see the listserv documentation or contact ITS for further information.

- Default-options\*\* This controls any subscription options for new subscribers. Most new lists are setup with Default-Options= Repro, which means people receive a copy of their own postings.
- Digest=: enable the option to receive one aggregate of all posting for a day, instead of all the individual postings. Note that this only enables the option- individual subscribers must select it.
  - Digest= Yes, Same, Daily
  - Digest= No
- Service=. Service Local limits subscribers to the Syracuse University community.
  - Service= \*Subscribers may be from anywhere
- Editor: (option not shown in example above) controls who can send to a list configured as Send=Editor,Hold. It's formatted like owner information, and there may be multiple editors.
  - Editor= jeandoe@syr.edu (optional information)
- Moderator: (option not shown in example above) for Send=Editor,Hold lists, controls who may approve messages. Message submitted by anyone not an editor must be approved by a moderator. If no moderator is specified, it will default to the editors. The moderator is formatted like owner information.
  - Moderator= jeandoe@syr.edu (optional information)
    Messages are sent to the moderators in round robin fashion for approval- no moderator sees all of the messages. It's designed to distribute the load on busy lists so one person doesn't do all of the work.
  - Moderator= All, jeandoe@syr.edu (optional information)
    This is a special form, and the parameter "All" is on the first moderator. This causes every message to be sent to all moderators.

---

## Updating HDR and MSTP Settings (Messages Unreadable)

Some lists that have been used for a few years may still have a setting called ***shorthdr*** or ***shortbmstp***. Newer lists have a default setting called ***fullhdr***. ***Shorthdr*** or ***shortbmstp*** cause messages to display an abbreviated e-mail header and masks most of the detail that documents the path a message takes to go from the sender to the recipient. While this is usually a good thing, the settings are increasingly causing the problem described above. Here's why:

Briefly, when abbreviated headers are sent through Listserv, information that identifies the message format is also suppressed. If the message is written in plain text, this is not a problem, since that is the default format. However, if the message is specially formatted with such elements as Web-based e-mail packages or other e-mail agents, or includes formatted attachments, Listserv cannot identify the format and attempts to display the message in plain text. This results in a non-readable message.

To fix the problem, modify your list configuration. Here are the steps:

- Log onto the listserv list management page.
- Select the list: Choose "List Management>List Dashboard: from the menu
- Click on Configure underneath the list you will be editing.
- Examine the configuration that appears in the text box. If you see a line like this:*Default-options= shortbmstp*
  or
  *Default-options= shorthdr* 
  change the line to read: 
  *Default-options= fullhdr*
- Click the "Save" button below the text box.

**Note:** This change in the configuration will affect all new subscriptions to the list. It will not affect existing subscriptions. You must also reset all existing subscriptions. To do that, send an email to [listserv@listserv.syr.edu](mailto:listserv@listserv.syr.edu) from your owner e-mail address. In the body of the message, type:

*quiet set* ***<listname>*** *fullhdr for \**

Listserv will send you an e-mail with directions to confirm the change. Once you respond to the confirmation, Listserv will reset all subscriptions to ***fullhdr***.

---

## Getting Help

Subscribers and list members should contact their list owner(s) for assistance by emailing <listname-request@[listserv.syr.edu](http://listserv.syr.edu)>. For example, if the listserv is [clocks@listserv.syr.edu](mailto:clocks@listserv.syr.edu), send email to <clocks-request@[listserv.syr.edu](http://listserv.syr.edu)>.

Additional Listserv instructions, including how-to instructions and videos, can be found on the [Learn Listserv page](http://www.lsoft.com/resources/learnlistserv.asp).

For support of the information above, contact the [ITS Help Desk](http://its.syr.edu/supportsvc) by calling at 315-443-2677, by emailing [help@syr.edu](mailto:help@syr.edu). Further information regarding hours and location can be found on the [ITS Service Center](https://its.syr.edu/its_service_center/) page.

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=toplink&locale=en_US&version=2)
