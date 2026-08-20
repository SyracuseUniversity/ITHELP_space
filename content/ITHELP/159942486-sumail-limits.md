---
title: "SUMail Limits"
confluence_id: "159942486"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942486/SUMail+Limits"
version: 8
last_modified: "2021-09-14T15:06:29.000Z"
status: "current"
parent_id: "159941384"
labels:
  - "email"
  - "exchange"
  - "adtt"
---

There are various service limits for SUMail that are designed to protect the email service as a whole and detect anomalies such as compromised accounts. The following list breaks out limits that would most likely affect all email users, and for a complete list of service limits check the following link: 
[Exchange Online limits - Service Descriptions | Microsoft Docs](https://docs.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits?redirectedfrom=MSDN)

All active Students, Staff, and Faculty are on an E3 license plan. Alumni are E1, and inactive users aren't licensed. Shared/Resource mailboxes also do not receive a license since they are not directly logged into.

| Type | Limit | Notes |
| --- | --- | --- |
| Message rate limiting | 30 email submissions per minute, per mailbox | There are no overrides for this.  No sent messages are lost or denied, they will sit in users outbox until the next minute and send as many as possible. |
| Recipient rate limiting | 10000 recipients every 24 hours, per mailbox | Specifies the total number of email addresses which can be mailed to in a 24 hour period, whether unique or not. |
| Receive rate limit | 3,600 messages per hour, per mailbox |  |
| User mailbox storage | 100gb (active staff/faculty/student mailboxes) | - warning: 98gb - prohibit send: 99gb - prohibit send/receive: 100gb |
| Shared/resource mailbox storage | 50gb |  |
| Alumni mailbox storage | 50gb |  |
| Archive mailbox storage | Unlimited | Available only for E3 licensed mailboxes |
| Messages per mailbox folder | 1 million |  |
| Folders per mailbox | 10,000 |  |
| Message size limit | 50mb | This includes attachments, but does not account for mime encoding or client limits. |
| Junk mail folder retention | 30 days |  |
| Deleted Items retention | 90 days |  |
| Inbox Forwarding Rule limit | 10 Forwardee limit | The maximum number of recipients that can be configured for an inbox or transport rule with a redirecting action. |
