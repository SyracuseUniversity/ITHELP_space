---
title: "Email Commands for List Owners"
confluence_id: "1467285516"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/1467285516/Email+Commands+for+List+Owners"
version: 3
last_modified: "2026-10-13T18:10:13.493Z"
status: "current"
parent_id: "159940971"
---

This reference summarizes email commands that LISTSERV 17.5 list owners can use to manage subscriptions, retrieve list information, and administer list settings. Replace `<listname>` with the list name and send commands to listserv@listserv.syr.edu, unless a command specifies another recipient.

## (blue star) Before sending a command

1. Send the message to listserv@listserv.syr.edu, not to the mailing list address.
2. Put the command in the message body. Unless otherwise specified, the subject line is ignored.
3. Send one command per line and remove automatic signatures or disclaimers that could be interpreted as additional commands.
4. Use the email address associated with your LISTSERV account when a command requires authentication or confirmation.
5. Remove your signature from the message body.

## (blue star) Common list-owner commands

| Command | Purpose | Example |
| --- | --- | --- |
| `INFO <listname>` | Requests information about a list, including its public description and available list details. | `INFO faculty-news` |
| `REVIEW <listname>` | Requests the list's subscriber roster when list policy and permissions allow it. | `REVIEW faculty-news` |
| `QUERY <listname>` | Returns subscription settings for the requesting address on a specific list. | `QUERY faculty-news` |
| `QUERY *` | Requests a list of the LISTSERV lists to which the sender is subscribed. | `QUERY *` |
| `LIST` | Requests a catalog of local lists that are visible to the requester. | `LIST` |
| `LIST /<text>` | Searches local list names and titles for a matching text string. | `LIST /research` |
| `LIST GLOBAL /<text>` | Searches the global LISTSERV catalog for lists matching a text string. | `LIST GLOBAL /libraries` |

## (blue star) Subscription and subscriber commands

These commands are useful for testing list behavior or assisting subscribers. Some operations may require confirmation, owner approval, or authorization based on the list configuration.

| Command | Purpose | Example |
| --- | --- | --- |
| `SUBSCRIBE <listname> <Your name>` | Subscribes the sender to a list. | `SUBSCRIBE faculty-news Jordan Lee` |
| `UNSUBSCRIBE <listname>` | Removes the sender from a list. | `UNSUBSCRIBE faculty-news` |
| `CHANGE <listname> <newaddress>` | Changes the sender's subscribed address when the sender can access both the old and new accounts. The new address must typically confirm the change. | `CHANGE faculty-news newaddress@example.edu` |
| `SET <listname> NOMAIL` | Suspends mail delivery while retaining the subscription. | `SET faculty-news NOMAIL` |
| `SET <listname> MAIL` | Restores normal mail delivery. | `SET faculty-news MAIL` |
| `SET <listname> DIGEST` | Enables digest delivery when supported by the list. | `SET faculty-news DIGEST` |
| `SET <listname> REPRO` | Requests copies of the sender's own postings. | `SET faculty-news REPRO` |
| `SET <listname> NOREPRO` | Stops copies of the sender's own postings. | `SET faculty-news NOREPRO` |

Commands may be rejected when they are sent from an address that is not subscribed, when the list configuration restricts the operation, or when confirmation is required. Keep the complete LISTSERV response when requesting support.

## (blue star) Troubleshooting and support

1. Confirm that the command was sent to listserv@listserv.syr.edu, not `<listname>@listserv.syr.edu`.
2. Check the command spelling, list name, and sender address.
3. Remove signatures, quoted replies, and extra text from the message body.
4. Review the LISTSERV response for confirmation links, authorization errors, or delivery restrictions.
5. For subscriber or list-specific issues, contact the list owner at `<listname>-request@listserv.syr.edu`.
6. For additional assistance, contact the ITS Help Desk at 315.443.2677 or [Listserv at Syracuse University](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940753/Listserv+at+Syracuse+University).

## Related resources

- [Listserv at Syracuse University](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940753/Listserv+at+Syracuse+University)
- [Listserv Owners How-To's](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940971/Listserv+Owners+How-To+s)
- [Listserv Subscriber How-To's](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941631/Listserv+Subscriber+How-To+s)
