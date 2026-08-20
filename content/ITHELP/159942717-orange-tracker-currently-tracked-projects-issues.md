---
title: "Orange Tracker Currently Tracked Projects & Issues"
confluence_id: "159942717"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942717/Orange+Tracker+Currently+Tracked+Projects+Issues"
version: 40
last_modified: "2023-11-22T20:08:01.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "admin"
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
  - "agent"
---

## Overview

---

Listed below are the currently tracked projects and issues relating to the Orange Tracker (OT) Jira Service Management (JSM) Cloud migration.

### Status Descriptions

OPEN Project/Issue has been identified and recorded, but has **not yet been reviewed**.

IN PROGRESS Project/Issue has been identified, recorded, and reviewed, and is **actively being worked on**.

RESOLVED Project/Issue has been **completed or resolved**.

SELF MITIGATION Project/Issue has been **resolved** but may require additional self mitigation actions by responsible unit.

BACKLOG Project/Issue has been identified, recorded, and reviewed, but will be reviewed again at a later date.

### Priority Levels

3 Lowest Priority (Normal)

2 Medium Priority

1 Highest Priority

## OT Cloud Currently Tracked Projects & Issues

---

| Summary | Status | Priority | Resolution Date | Details |
| --- | --- | --- | --- | --- |
| Form Mail Spoofing | SELF MITIGATION | 3 | 26 Jul 2023 | Forms sending an email with the From: field populated by the users provided (free-form text field or auto-authenticated) email address are not generating tickets IF they are not a [syr.edu](http://syr.edu) domain user. (stopped at Project by DMARC).  Forms must use the default form sender address; Do not use an address populated by the users as the From:.  This applies to both external and internal  "@syr.edu" Domain addresses.  Additionally all forms should use the [su-jsm.atlassian.net](http://su-jsm.atlassian.net) Email address of your project for the destination.  Project Managers and associated Form Owners will need to identify and correct the forms in use. |
| External Email Not Generating New Tickets (DMARC) | SELF MITIGATION | 3 | 25 Jul 2023 | The email was delivered to the Cloud but Rejected on Auto-reply mail by the SD auto reply filter. This was traced back to accounts with a true mailbox and using Rules to forward/redirect email.  These will have to alter the forward/redirect rule. The current rule should be replaced with an 'outside' forwarding rule within your account. Documentation on how to do that is in Answers: <https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940689> |
| Email Button / JETI Sending Mail Issues | IN PROGRESS | 1 | 09 Jan 2024 | 11/22/23 - eric mumpton - The Jira Email This Issue (aka JETI or Email Issue) function continues to encounter problems delivering email notifications to some addresses. Efforts to correct or work around this inconsistant behavior are not making progress to allow us to continue providing this third-party plugin to Jira Service Managment.   JETI will be discontinued in Orange Tracker as of January 9, 2024. This is expected to provide adequate time for current users to modify their processes for using out-of-the-box functionality in place of JETI.  We are instructing people to use the new built-in features in JSM instead of the JETI features. JETI was a workaround for the older Jira system to send mail to other people who need to stay informed on the ticket. JSM has this feature built-in, with the Request Participants field, Watchers (internal teams) and Notifications (Jira and Customer Notifications). We have some pages discussing this: [Orange Tracker Comments and Talking to Customers](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159949480/Orange+Tracker+Comments+and+Talking+to+Customers); [Orange Tracker Cloud - Issue Sharing & Collaboration](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159946604/Orange+Tracker+Cloud+-+Issue+Sharing+Collaboration).  Using the Email button to send email to customers (and cc'es) failing with external customer email address (i.e. "@gmail.com"). Failure is related to untrusted JETI mail headers.  No DMARC implemented.  ~~Work is in progress to send through [syr.edu](http://syr.edu) SMTP servers.  Temporary solution while we work on replacing JETI with built-in Jira Service Management functionality.~~ |
| Workflow Status Auto-Transition - Waiting for Feedback | RESOLVED | 3 | 15 Aug 2023 | Reporter comments or replies to Request Feedback are not transitioning the ticket out of the Waiting for Feedback state. We are developing an Answers page: [Orange Tracker Workflow Transitions and Communications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications) |
| Workflow Status Auto-Transition - Reopen Closed Ticket | RESOLVED | 3 | 17 Aug 2023 | Reporter comments on a Resolved/Closed tickets, transition to Reopened. Documentation is on our Answers page: [Orange Tracker Workflow Transitions and Communications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications) |
| App Requests | RESOLVED | 3 |  | We are still enabling new features that are built into the system and not accepting new Add-on Application Requests at this time. Add-ons are enabled for the whole system and will still need a process that includes Accessibility and Security approvals. |
| API Documentation | RESOLVED | 3 | 28 Jul 2023 | Document the new process for making API calls to the cloud. |
| Service Accounts for API Access | OPEN | 3 |  | Develop a process to utilize service accounts for the teams using API calls. |
| Component Auto-Added to each Ticket | SELF MITIGATION | 3 | 28 Jul 2023 | Some projects were requiring the Component field to be entered when the ticket was created. The migration selected one the project components as a default value. We have created a document to help change or remove the default component: [Component Field Automatically Added to Ticket](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159951626/Component+Field+Automatically+Added+to+Ticket) |
| Non-SD Agents Unable to Create Tickets | RESOLVED | 2 | 26 Jul 2023 | Orange Tracker Administrators adjusted the Customer Permissions → Service Project Access setting and allowed anyone to create tickets via email or the portal.  The email was delivered to Cloud but Failed on a permissions to access project error from the Jira Service Management Mail Handler.  This was an issue with existing internal users (non-SD Agents). They were not in the correct group for permissions to create tickets in OT. |
| Former User Cleanup | OPEN | 3 |  | We have some migrated users who are labeled as "Former Users". The team will identify them and update the user with their proper name and information. |
| Clone Plus Issues | RESOLVED | 3 | 11 Aug 2023 | Cloning a ticket to another project would fail and display a "Reporter is Required" error, and the Reporter field is not on the screen. This is a permissions issue and the JSM Administrators are working on correcting this. |
| Customer Sharing - Request Participant Issues | RESOLVED | 3 | 28 Jul 2023 | Orange Tracker Administrators adjusted the Customer Permissions → Customer Sharing setting which allowed customers to add users into the Request Participant field the users who were CC'ed in the email. |
| Customer Notifications | RESOLVED | 3 | 03 Aug 2023 | Document and recommend customer notification settings for projects. Documentation on notifications is in Answers: [Orange Tracker Customer Notifications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159951630/Orange+Tracker+Customer+Notifications) |
| Mail Sent From atlassian.net Not Trusted | OPEN | 3 |  | Causes concerns. "feedback from a faculty member who isn’t a frequent user of OT.   The non SYR email address has him thinking it was not someone at SU responding."  "But, I mean, it's not an SYR email.  So, our central IT expects us to trust random external emails?  That's not a reassuring sign! "  Resolution  Provide added Communication / Education.  Options for customer notification (customization/branding).  Project to research, plan, implement (with CIS Mail/DMARC). DMARC mitigation to send mail from OT as a [syr.edu](http://syr.edu) domain sender. |
| Email - [JIRA] Subscription: ${searchRequest.getName()} | RESOLVED | 3 | 21 Aug 2023 | Filter Subscription sends a blank email with no link to the filter |
| Clone Plus - Cloned Issue(s) Comment Creator Issue | RESOLVED | 3 |  | When cloning an issue using Clone Plus and **including comments** in the cloned issue, ALL comments on the cloned issue come over under the user who performed the clone and not the user(s) who originally created the comment(s). |
