---
title: "Troubleshooting Steps for Non-Delivery of Email"
confluence_id: "451215663"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/451215663/Troubleshooting+Steps+for+Non-Delivery+of+Email"
version: 2
last_modified: "2025-08-20T18:14:00.244Z"
status: "current"
parent_id: "159940971"
labels:
  - "troubleshoot"
  - "listserv"
  - "troubleshooting"
---

### 1. **Confirm the Email Address**

- Verify that the subscriber’s email address is spelled correctly in the subscription request.
- Check for common errors (extra spaces, missing periods, wrong domain, etc.).

### 2. **Check Subscription Status**

- Confirm if the subscriber is **already subscribed** to the list.

  - For Dynamic/Smart lists use the command line in list manager and type the following: **REVIEW listname (RCPT NOH MSG ALL TOPICS BY NAME**
- Look for pending confirmation requests (if double opt-in is enabled).
- Verify if the address is on a **suppression list** (e.g., previously unsubscribed, bounced, or blacklisted).

  - Log in to the LISTSERV web interface with your **list owner credentials**.
  - Navigate to your list management dashboard.
  - Look for the **“Subscriber Management”** section.
  - Search for the email address in question.

    - If the address does not appear as an active subscriber but has a status message like *“Bad Address”*, *“Bounced”*, *“Deleted”*, or *“Hold”*, it may have been automatically placed on the **auto-delete/suppression list**. Please reach out to your listserv administrator for additional support.

### 3. **Review Delivery Logs**

- Determine whether the message was:

  - Delivered successfully
  - Deferred or delayed

    - Log in to the LISTSERV web interface with your **list owner credentials**.
    - Navigate to your list management.
    - Select List Activity Reports

### 4. **Check Moderation and List Settings**

- Ensure the subscriber’s request or the message to them was not:

  - Held for moderation
  - Blocked by list policies (e.g., restricted senders)
  - Sent to a digest (delaying immediate delivery)

### 5. **Inspect Bounce or Error Messages**

- Look for bounce notifications tied to the subscriber’s address, these will be emailed directly to the list owner
- Identify common reasons:

  - Mailbox full
  - Invalid domain or recipient not found
  - Rejected by the recipient’s mail server (SPAM or policy filters)

### 6. **Check Email Filters and Spam Folder**

- Ask the subscriber to:

  - Review their spam/junk folder.
  - Add the list’s sending address to their **contacts/whitelist**.
  - Check whether their organization blocks bulk or automated messages.

### 7. **Test with Alternate Addresses**

- Try sending a test message to the subscriber from outside the listserv system.
- If that fails, the issue is likely with the subscriber’s mail provider.
- If successful, the problem is specific to the list system.

### 8. **Escalate if Necessary**

- If list activity show delivery attempts but the subscriber still cannot receive:

  - Contact the listserv administrator for deeper log analysis.
  - Provide timestamps, the subscriber’s email address, and any bounce/error codes for further investigation.
  - Listserv administrator can be reach by submitting a request to either option below:

    - [Report an Issue](https://support.atlassian.syr.edu/servicedesk/customer/portal/22/group/366/create/866)
    - [Email](mailto:cdiapps@su-jsm.atlassian.net)

---

✅ **Tip for List Managers**: Always document what steps were taken so recurring issues with the same subscriber can be tracked and resolved more quickly.
