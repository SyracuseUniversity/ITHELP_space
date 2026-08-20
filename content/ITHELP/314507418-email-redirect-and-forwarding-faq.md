---
title: "Email Redirect and Forwarding FAQ"
confluence_id: "314507418"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/314507418/Email+Redirect+and+Forwarding+FAQ"
version: 17
last_modified: "2025-03-24T21:10:21.644Z"
status: "current"
parent_id: "159941384"
---

As part of Syracuse University's ongoing efforts to maintain and secure email services, SUMail account owners are no longer allowed to automatically forward or redirect emails to third-party accounts. Note that the SU Policy pages have not yet been updated to reflect this change.

# Why is this changing?

New email protocols, such as [DMARC](https://dmarc.org/), [SPF](https://www.proofpoint.com/us/threat-reference/spf), and [DKIM](https://www.mimecast.com/content/dkim/), have been adopted by service providers to ensure the validity of incoming messages. For example, the original “To:” address is compared to the destination mailbox. If the addresses do not match – which is the case for redirected messages – the message will be rejected as spam. The message won’t be delivered and likely deleted.

# When did the ban on automated redirects become effective?

The policy became effective in March 2025. Configurations and rules in individuals' accounts that automatically forwarded or redirected emails to a 3rd party email system were deleted or disabled on March 26, 2025. Affected users were notified in advance by email in November 2024 and again in February 2025.

# Who is affected?

All individual account holders: students, faculty, staff, sponsored associates (guests) and other affiliates that qualify for SUMail.

# What is not affected?

The following scenarios are not impacted by this change:

- Rules in SUMail accounts that forward or redirect email to another SUMail account are still supported.
- Generic accounts, (e.g., department and sysadmin accounts) are not affected.
- Listservs will continue to work for subscribers. However, a user cannot forward to a listserv because it is considered an external forwarding.

# What do I need to do?

Inspect forwarding or redirect rules you may have in place and change how you manage messages accordingly. You are encouraged to remove your own Rules and Forwarding configurations so you are aware of them and can change how you manage SUMail messages.

If you do nothing, Forwarding configurations will be deleted, and Rules that forward or redirect to a 3rd party email system will cease to function starting March 26, 2025.

# Can I still forward messages one at a time?

Yes, you can still forward individual emails to other accounts manually.
