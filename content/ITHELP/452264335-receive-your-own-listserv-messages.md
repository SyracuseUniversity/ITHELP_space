---
title: "Receive Your Own LISTSERV Messages"
confluence_id: "452264335"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/452264335/Receive+Your+Own+LISTSERV+Messages"
version: 2
last_modified: "2025-08-22T15:55:57.706Z"
status: "current"
parent_id: "159940971"
labels:
  - "email"
  - "listserv"
  - "subscribers"
---

By default, LISTSERV is set so that when you post a message to the list, you will *not* receive a copy of your own email. This is intended to reduce duplicate messages in your inbox.

If you would like to begin receiving copies of your own posts, you can enable the **REPRO** option for your subscription:

**How to Enable REPRO**

1. Send an email to:

   ```
   listserv@listserv.syr.edu
   ```

   (Remove your automatic signature)
2. Leave the subject line blank.
3. In the body of the message, type:

   ```
   SET listname REPRO
   ```

   *(replace “listname” with the actual list name, such as IST-STUDENTS).*
4. Send the email. LISTSERV will reply with a confirmation.

**How to Disable Again**
If you decide you no longer want copies of your own posts, simply send:

```
SET listname NOREPRO
```

This setting only applies to your subscription—it does not affect how others receive messages.
