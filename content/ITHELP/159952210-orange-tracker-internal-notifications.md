---
title: "Orange Tracker Internal Notifications"
confluence_id: "159952210"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952210/Orange+Tracker+Internal+Notifications"
version: 10
last_modified: "2023-10-05T13:02:17.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
  - "comments"
  - "agent"
---

Orange Tracker (OT) projects have two sections dealing with notifications. Notifications are messages sent from the system when certain events happen. For example, the Agents are notified when a new ticket is created and an email is sent to each person, notifying them of the event. The email address will be <projectkey>@su-jsm.atlassian.net.

The OT system now divides the notifications into two sections:

- **Internal Jira Notifications** are the standard Jira notifications we are used to
- **Customer Notifications** are only sent to the Customer/Reporter and any Request Participants listed in the ticket

Customers and Request Participants will not receive any Internal Notifications. Many migrated Jira Notification Schemes show the Reporter being notified on certain events. The Reporter will not be notified by this as it is an Internal Notification. Internal Notifications are only for Agents and Project Administrators of the project.

For information on **Customer Notifications**, please see the following page: [Orange Tracker Customer Notifications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159951630/Orange+Tracker+Customer+Notifications)

## Internal Jira Notifications

Internal Jira Notifications are designed only for the project team. Some Internal Notification Schemes have Reporter listed and these will not trigger a message to the Reporter. The system forces reporters and participants to use the Customer Notifications.

Only OT System Administrators have access to create new notification schemes, edit existing ones, or move your project to a different scheme. Please work with the OT System Administrators for requests.

## Standard Notification Schemes

We have created a few standard notification schemes that should work for the majority of the projects within the system.

**SU Standard - Level 1 Reporter : Level 1 Watchers : Consultants on Create Issue**

This scheme is a bare minimum set of notifications. This scheme limits notifications to the Watcher role.

- Watchers receive an email on Issue Creation, Issue Resolved, Issue Updated, Issue Commented, Issue Reopened, Feedback Request, Work Scheduled, and On Hold.
- Watchers do not receive an email on Issue Closed. This gives the project Consultants the flexibility to close the ticket without notifying the Reporter. The Consultant should Resolve the ticket and interact with the Reporter. Then, once all work is completed, Close the ticket and only the Assignee shall be notified.
- Consultants can choose to interact with the Reporter by adding an unrestricted comment at the bottom, or use the Request Feedback button near the top. There are triggers for workflow when using the Request Feedback button and places the ticket in "Waiting for Feedback" status until the Reporter responds. Using the comments at the bottom bypasses these triggers, but the consultants can still set the ticket in this status if needed.
- Consultants receive an email when an issue has been assigned. This notifies the team that the issue is being addressed.

**SU Standard - Level 2 Reporter : Level 2 Watchers : Consultants on Create Issue**

This scheme takes the bare minimum set of notifications that go to the Watchers from the Level 1 scheme and adds more notifications to the roles.

- Watchers receive an email on Issue Creation, Issue Updated, Issue Assigned, Issue Resolved, Issue Commented, Issue Comment Edited, Issues Comment Deleted, Issue Reopened, Issue Moved, Feedback Request, Work Scheduled, and On Hold.
- Watchers do not receive an email on Issue Closed. This gives the project Consultants the flexibility to close the ticket without notifying the Reporter. The Consultant should Resolve the ticket and interact with the Reporter. Then, once all work is completed, Close the ticket and only the Assignee shall be notified.
- Consultants can choose to interact with the Reporter by adding an unrestricted comment at the bottom, or use the Request Feedback button near the top. There are triggers for workflow when using the Request Feedback button and places the ticket in "Waiting for Feedback" status until the Reporter responds. Using the comments at the bottom bypasses these triggers, but the consultants can still set the ticket in this status if needed.
- Consultants receive an email when an issue has been assigned. This notifies the team that the issue is being addressed.

**SU Standard - Level 1 Reporter : Level 2 Watchers : Consultants on Create Issue**

This scheme takes the bare minimum set of notifications that go to the Watchers receive Level 2 notifications. This allows the Watchers to be treated like the Assignee and receive the same amount of notifications.

- Watchers receive an email on Issue Creation, Issue Updated, Issue Assigned, Issue Resolved, Issue Commented, Issue Comment Edited, Issues Comment Deleted, Issue Reopened, Issue Moved, Feedback Request, Work Scheduled, and On Hold.
- Watchers do not receive an email on Issue Closed. This gives the project Consultants the flexibility to close the ticket without notifying the Reporter. The Consultant should Resolve the ticket and interact with the Reporter. Then, once all work is completed, Close the ticket and only the Assignee shall be notified.
- Consultants can choose to interact with the Reporter by adding an unrestricted comment at the bottom, or use the Request Feedback button near the top. There are triggers for workflow when using the Request Feedback button and places the ticket in "Waiting for Feedback" status until the Reporter responds. Using the comments at the bottom bypasses these triggers, but the consultants can still set the ticket in this status if needed.
- Consultants receive an email when an issue has been assigned. This notifies the team that the issue is being addressed.

**Standard Scheme with Reporter Notifications Reduced plus Notifications to Consultants on Create Issue**

This scheme has been an existing standard that many projects use. This scheme treats the Reporter and Watchers differently where the Watchers receive the same notifications as the Assignee.

- Reporter receives an email on **Issue Resolved** and **Feedback Request** only.
- Consultants are notify that an new issue/ticket has been created.
- Watchers receive the same notifications as the Assignee, which is about all notifications.
- Adding a comment at the bottom of the issue ticket will **not** send a email to the Reporter.
- Consultants communicate through the **Feedback Request** button if they need to ask a question to the Reporter.

**Standard Scheme with Reporter Notifications Reduced plus Notifications to Project Managers on Create Issue**

This scheme has been an existing standard as well, and the major difference is Project Managers receive an email that as issue/ticket has been created, not the Consultants role. This scheme still treats the Reporter and Watchers differently where the Watchers receive the same notifications as the Assignee.

- Reporter receives an email on **Issue Creation, Issue Resolved, Issue Reopened, and Feedback Request** only.
- Project Managers are notify that an new issue/ticket has been created. This allows the project managers to assign the issue to the consultant that best suits the issue.
- Watchers receive the same notifications as the Assignee, which is about all notifications.
- Adding a comment at the bottom of the issue ticket will **not** send a email to the Reporter.
- Consultants communicate through the **Feedback Request** button if they need to ask a question to the Reporter.

## Details of Notification Schemes

### Standard Notification Scheme

|  |  |  |  |
| --- | --- | --- | --- |
| Standard Notification Scheme | | Roles that get notified | |
| Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ |
| Issue Updated | ✓ | ✓ |
| Issue Assigned | ✓ | ✓ |
| Issue Resolved | ✓ | ✓ |
| Issue Closed | ✓ | ✓ |
| Issue Commented | ✓ | ✓ |
| Issue Comment Edited | ✓ | ✓ |
| Issue Comment Deleted | ✓ | ✓ |
| Issue Reopened | ✓ | ✓ |
| Issue Deleted | ✓ | ✓ |
| Issue Moved | ✓ | ✓ |
| Work Logged On Issue | ✓ | ✓ |
| Work Started On Issue | ✓ | ✓ |
| Work Stopped On Issue | ✓ | ✓ |
| Issue Worklog Updated | ✓ | ✓ |
| Issue Worklog Deleted | ✓ | ✓ |
| Generic Event | ✓ | ✓ |
| Notify |  |  |
| Soft Close |  |  |
| Issue Marked As Spam | ✓ | ✓ |
| Feedback Request | ✓ | ✓ |
| CM Status Reminder |  |  |
| Feedback Received | ✓ | ✓ |
| Work Scheduled |  |  |
| On Hold |  |  |

### Standard Scheme plus Notification to All Consultants on All Events

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Notification Scheme  plus Notification to Consultants  on All Events | | Roles that get notified | | |
| Project Role  (Consultants) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated | ✓ | ✓ | ✓ |
| Issue Assigned | ✓ | ✓ | ✓ |
| Issue Resolved | ✓ | ✓ | ✓ |
| Issue Closed | ✓ | ✓ | ✓ |
| Issue Commented | ✓ | ✓ | ✓ |
| Issue Comment Edited | ✓ | ✓ | ✓ |
| Issue Comment Deleted | ✓ | ✓ | ✓ |
| Issue Reopened | ✓ | ✓ | ✓ |
| Issue Deleted | ✓ | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue | ✓ | ✓ | ✓ |
| Work Started On Issue | ✓ | ✓ | ✓ |
| Work Stopped On Issue | ✓ | ✓ | ✓ |
| Issue Worklog Updated | ✓ | ✓ | ✓ |
| Issue Worklog Deleted | ✓ | ✓ | ✓ |
| Generic Event | ✓ | ✓ | ✓ |
| Notify |  |  |  |
| Soft Close |  |  |  |
| Issue Marked As Spam | ✓ | ✓ | ✓ |
| Feedback Request | ✓ | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received | ✓ | ✓ | ✓ |
| Work Scheduled |  |  |  |
| On Hold |  |  |  |

### Standard Scheme with Reporter Notifications Reduced

|  |  |  |  |
| --- | --- | --- | --- |
| Standard Scheme with Reporter  Notifications Reduced | | Roles that get notified | |
| Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ |
| Issue Updated | ✓ | ✓ |
| Issue Assigned | ✓ | ✓ |
| Issue Resolved | ✓ | ✓ |
| Issue Closed | ✓ | ✓ |
| Issue Commented | ✓ | ✓ |
| Issue Comment Edited | ✓ | ✓ |
| Issue Comment Deleted | ✓ | ✓ |
| Issue Reopened | ✓ | ✓ |
| Issue Deleted | ✓ | ✓ |
| Issue Moved | ✓ | ✓ |
| Work Logged On Issue | ✓ | ✓ |
| Work Started On Issue | ✓ | ✓ |
| Work Stopped On Issue | ✓ | ✓ |
| Issue Worklog Updated | ✓ | ✓ |
| Issue Worklog Deleted | ✓ | ✓ |
| Generic Event | ✓ | ✓ |
| Notify | ✓ | ✓ |
| Soft Close |  |  |
| Issue Marked As Spam | ✓ | ✓ |
| Feedback Request | ✓ | ✓ |
| CM Status Reminder |  |  |
| Feedback Received | ✓ | ✓ |
| Work Scheduled | ✓ | ✓ |
| On Hold | ✓ | ✓ |

### Standard Scheme plus Notification to Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Scheme plus Notifications  to Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated |  | ✓ | ✓ |
| Issue Assigned |  | ✓ | ✓ |
| Issue Resolved |  | ✓ | ✓ |
| Issue Closed |  | ✓ | ✓ |
| Issue Commented |  | ✓ | ✓ |
| Issue Comment Edited |  | ✓ | ✓ |
| Issue Comment Deleted |  | ✓ | ✓ |
| Issue Reopened |  | ✓ | ✓ |
| Issue Deleted |  | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue |  | ✓ | ✓ |
| Work Started On Issue |  | ✓ | ✓ |
| Work Stopped On Issue |  | ✓ | ✓ |
| Issue Worklog Updated |  | ✓ | ✓ |
| Issue Worklog Deleted |  | ✓ | ✓ |
| Generic Event |  | ✓ | ✓ |
| Notify |  |  |  |
| Soft Close |  |  |  |
| Issue Marked As Spam |  | ✓ | ✓ |
| Feedback Request |  | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received |  | ✓ | ✓ |
| Work Scheduled |  |  |  |
| On Hold |  |  |  |

### Standard Scheme with Reporter Notifications Reduced plus Notification to Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Scheme with Reporter  Notifications Reduced plus Notification  to Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated |  | ✓ | ✓ |
| Issue Assigned |  | ✓ | ✓ |
| Issue Resolved |  | ✓ | ✓ |
| Issue Closed |  | ✓ | ✓ |
| Issue Commented |  | ✓ | ✓ |
| Issue Comment Edited |  | ✓ | ✓ |
| Issue Comment Deleted |  | ✓ | ✓ |
| Issue Reopened |  | ✓ | ✓ |
| Issue Deleted |  | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue |  | ✓ | ✓ |
| Work Started On Issue |  | ✓ | ✓ |
| Work Stopped On Issue |  | ✓ | ✓ |
| Issue Worklog Updated |  | ✓ | ✓ |
| Issue Worklog Deleted |  | ✓ | ✓ |
| Generic Event |  | ✓ | ✓ |
| Notify |  |  |  |
| Soft Close |  |  |  |
| Issue Marked As Spam |  | ✓ | ✓ |
| Feedback Request |  | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received |  | ✓ | ✓ |
| Work Scheduled |  | ✓ | ✓ |
| On Hold |  | ✓ | ✓ |

### Standard Scheme plus Notification to Project Managers on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Scheme plus  Notifications to Project Managers  on Create Issue | | Roles that get notified | | |
| Project Role  (Project Managers) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated |  | ✓ | ✓ |
| Issue Assigned |  | ✓ | ✓ |
| Issue Resolved |  | ✓ | ✓ |
| Issue Closed |  | ✓ | ✓ |
| Issue Commented |  | ✓ | ✓ |
| Issue Comment Edited |  | ✓ | ✓ |
| Issue Comment Deleted |  | ✓ | ✓ |
| Issue Reopened |  | ✓ | ✓ |
| Issue Deleted |  | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue |  | ✓ | ✓ |
| Work Started On Issue |  | ✓ | ✓ |
| Work Stopped On Issue |  | ✓ | ✓ |
| Issue Worklog Updated |  | ✓ | ✓ |
| Issue Worklog Deleted |  | ✓ | ✓ |
| Generic Event |  | ✓ | ✓ |
| Notify |  |  |  |
| Soft Close |  |  |  |
| Issue Marked As Spam |  | ✓ | ✓ |
| Feedback Request |  | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received |  | ✓ | ✓ |
| Work Scheduled |  |  |  |
| On Hold |  |  |  |

### Standard Scheme with Reporter Notifications Reduced plus Notification to Project Managers on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Scheme with Reporter  Notifications Reduced plus  Notification to Project Managers  on Create Issue | | Roles that get notified | | |
| Project Role  (Project Managers) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated |  | ✓ | ✓ |
| Issue Assigned |  | ✓ | ✓ |
| Issue Resolved |  | ✓ | ✓ |
| Issue Closed |  | ✓ | ✓ |
| Issue Commented | ✓ | ✓ | ✓ |
| Issue Comment Edited |  | ✓ | ✓ |
| Issue Comment Deleted |  | ✓ | ✓ |
| Issue Reopened |  | ✓ | ✓ |
| Issue Deleted |  | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue |  | ✓ | ✓ |
| Work Started On Issue |  | ✓ | ✓ |
| Work Stopped On Issue |  | ✓ | ✓ |
| Issue Worklog Updated |  | ✓ | ✓ |
| Issue Worklog Deleted |  | ✓ | ✓ |
| Generic Event |  | ✓ | ✓ |
| Notify |  | ✓ | ✓ |
| Soft Close |  |  |  |
| Issue Marked As Spam |  | ✓ | ✓ |
| Feedback Request |  | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received |  | ✓ | ✓ |
| Work Scheduled |  | ✓ | ✓ |
| On Hold |  | ✓ | ✓ |

### Standard Scheme with Reporter Feedback and Resolve plus Notification to Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Standard Scheme with Reporter  Notifications Reduced plus Notification  to Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current Assignee | All Watchers |
| Events | Issue Created | ✓ | ✓ | ✓ |
| Issue Updated |  | ✓ | ✓ |
| Issue Assigned |  | ✓ | ✓ |
| Issue Resolved |  | ✓ | ✓ |
| Issue Closed |  | ✓ | ✓ |
| Issue Commented |  | ✓ | ✓ |
| Issue Comment Edited |  | ✓ | ✓ |
| Issue Comment Deleted |  | ✓ | ✓ |
| Issue Reopened |  | ✓ | ✓ |
| Issue Deleted |  | ✓ | ✓ |
| Issue Moved | ✓ | ✓ | ✓ |
| Work Logged On Issue |  | ✓ | ✓ |
| Work Started On Issue |  | ✓ | ✓ |
| Work Stopped On Issue |  | ✓ | ✓ |
| Issue Worklog Updated |  | ✓ | ✓ |
| Issue Worklog Deleted |  | ✓ | ✓ |
| Generic Event |  | ✓ | ✓ |
| Notify |  |  |  |
| Soft Close |  |  |  |
| Issue Marked As Spam |  | ✓ | ✓ |
| Feedback Request |  | ✓ | ✓ |
| CM Status Reminder |  |  |  |
| Feedback Received |  | ✓ | ✓ |
| Work Scheduled |  | ✓ | ✓ |
| On Hold |  | ✓ | ✓ |

### SU Standard - Level 1 Reporter : Level 1 Watchers : Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SU Standard - Level 1 Reporter : Level 1 Watchers : Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current  Assignee | All  Watchers |
|  | **Issue Created**  An issue has entered into the system | ✓ | ✓ | ✓ |
| Issue Updated  An issue has had its details changed. This includes the deletion of an issue comment. |  | ✓ | ✓ |
| Issue Assigned  An issue has been assigned to a new user. | ✓ | ✓ |  |
| **Issue Resolved** An issue has been resolved (usually after being worked on and fixed). |  | ✓ | ✓ |
| Issue Closed  An issue has been closed. (Note that an issue may be closed without being resolved). |  | ✓ |  |
| **Issue Commented**  An issue has had a comment added to it. |  | ✓ | ✓ |
| Issue Comment Edited  An issue's comment has been modified. |  | ✓ |  |
| Issue Comment Deleted  An issue has been deleted. |  | ✓ |  |
| **Issue Reopened**  An issue has been re-opened. |  | ✓ | ✓ |
| Issue Deleted  An issue has been deleted. |  | ✓ |  |
| Issue Moved  An issue has been moved into or out of this project. | ✓ | ✓ |  |
| Work Logged On Issue  An issue has had hours logged against it (i.e. a worklog has been added). |  |  |  |
| Work Started On Issue  The Assignee has started working on an issue. |  |  |  |
| Work Stopped On Issue  The Assignee has stopped working on an issue. |  |  |  |
| Issue Worklog Updated  An entry in an issue's worklog has been modified. |  |  |  |
| Issue Worklog Deleted  An entry in an issue's worklog has been deleted. |  |  |  |
| Generic Event  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| Notify  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Soft Close  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Issue Marked As Spam  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| **Feedback Request**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| CM Status Reminder  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Feedback Received  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **Work Scheduled**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **On Hold**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |

### SU Standard - Level 2 Reporter : Level 2 Watchers : Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SU Standard - Level 2 Reporter : Level 2 Watchers : Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current  Assignee | All  Watchers |
|  | **Issue Created**  An issue has entered into the system | ✓ | ✓ | ✓ |
| **Issue Updated**  An issue has had its details changed. This includes the deletion of an issue comment. |  | ✓ | ✓ |
| **Issue Assigned**  An issue has been assigned to a new user. | ✓ | ✓ | ✓ |
| **Issue Resolved** An issue has been resolved (usually after being worked on and fixed). |  | ✓ | ✓ |
| Issue Closed  An issue has been closed. (Note that an issue may be closed without being resolved). |  | ✓ |  |
| **Issue Commented**  An issue has had a comment added to it. |  | ✓ | ✓ |
| **Issue Comment Edited**  An issue's comment has been modified. |  | ✓ | ✓ |
| **Issue Comment Deleted**  An issue has been deleted. |  | ✓ | ✓ |
| **Issue Reopened**  An issue has been re-opened. |  | ✓ | ✓ |
| Issue Deleted  An issue has been deleted. |  | ✓ |  |
| **Issue Moved**  An issue has been moved into or out of this project. | ✓ | ✓ | ✓ |
| Work Logged On Issue  An issue has had hours logged against it (i.e. a worklog has been added). |  |  |  |
| Work Started On Issue  The Assignee has started working on an issue. |  |  |  |
| Work Stopped On Issue  The Assignee has stopped working on an issue. |  |  |  |
| Issue Worklog Updated  An entry in an issue's worklog has been modified. |  |  |  |
| Issue Worklog Deleted  An entry in an issue's worklog has been deleted. |  |  |  |
| Generic Event  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| Notify  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Soft Close  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Issue Marked As Spam  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| **Feedback Request**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| CM Status Reminder  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Feedback Received  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **Work Scheduled**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **On Hold**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |

### SU Standard - Level 1 Reporter : Level 2 Watchers : Consultants on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SU Standard - Level 1 Reporter : Level 2 Watchers : Consultants on Create Issue | | Roles that get notified | | |
| Project Role  (Consultants) | Current  Assignee | All  Watchers |
|  | **Issue Created**  An issue has entered into the system | ✓ | ✓ | ✓ |
| **Issue Updated**  An issue has had its details changed. This includes the deletion of an issue comment. |  | ✓ | ✓ |
| **Issue Assigned**  An issue has been assigned to a new user. | ✓ | ✓ | ✓ |
| **Issue Resolved** An issue has been resolved (usually after being worked on and fixed). |  | ✓ | ✓ |
| Issue Closed  An issue has been closed. (Note that an issue may be closed without being resolved). |  | ✓ |  |
| **Issue Commented**  An issue has had a comment added to it. |  | ✓ | ✓ |
| **Issue Comment Edited**  An issue's comment has been modified. |  | ✓ | ✓ |
| **Issue Comment Deleted**  An issue has been deleted. |  | ✓ | ✓ |
| **Issue Reopened**  An issue has been re-opened. |  | ✓ | ✓ |
| Issue Deleted  An issue has been deleted. |  | ✓ |  |
| **Issue Moved**  An issue has been moved into or out of this project. | ✓ | ✓ | ✓ |
| Work Logged On Issue  An issue has had hours logged against it (i.e. a worklog has been added). |  |  |  |
| Work Started On Issue  The Assignee has started working on an issue. |  |  |  |
| Work Stopped On Issue  The Assignee has stopped working on an issue. |  |  |  |
| Issue Worklog Updated  An entry in an issue's worklog has been modified. |  |  |  |
| Issue Worklog Deleted  An entry in an issue's worklog has been deleted. |  |  |  |
| Generic Event  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| Notify  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Soft Close  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Issue Marked As Spam  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| **Feedback Request**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| CM Status Reminder  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Feedback Received  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **Work Scheduled**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **On Hold**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |

### SU Standard - Level 1 Reporter : Level 1 Watchers : PM on Create Issue

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SU Standard - Level 1 Reporter : Level 1 Watchers : Project Managers on Create Issue | | Roles that get notified | | |
| Project Role  (Project Manager) | Current  Assignee | All  Watchers |
|  | **Issue Created**  An issue has entered into the system | ✓ | ✓ | ✓ |
| Issue Updated  An issue has had its details changed. This includes the deletion of an issue comment. |  | ✓ | ✓ |
| Issue Assigned  An issue has been assigned to a new user. | ✓ | ✓ |  |
| **Issue Resolved** An issue has been resolved (usually after being worked on and fixed). |  | ✓ | ✓ |
| Issue Closed  An issue has been closed. (Note that an issue may be closed without being resolved). |  | ✓ |  |
| **Issue Commented**  An issue has had a comment added to it. |  | ✓ | ✓ |
| Issue Comment Edited  An issue's comment has been modified. |  | ✓ |  |
| Issue Comment Deleted  An issue has been deleted. |  | ✓ |  |
| **Issue Reopened**  An issue has been re-opened. |  | ✓ | ✓ |
| Issue Deleted  An issue has been deleted. |  | ✓ |  |
| Issue Moved  An issue has been moved into or out of this project. | ✓ | ✓ |  |
| Work Logged On Issue  An issue has had hours logged against it (i.e. a worklog has been added). |  |  |  |
| Work Started On Issue  The Assignee has started working on an issue. |  |  |  |
| Work Stopped On Issue  The Assignee has stopped working on an issue. |  |  |  |
| Issue Worklog Updated  An entry in an issue's worklog has been modified. |  |  |  |
| Issue Worklog Deleted  An entry in an issue's worklog has been deleted. |  |  |  |
| Generic Event  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| Notify  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Soft Close  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Issue Marked As Spam  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ |  |
| **Feedback Request**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| CM Status Reminder  The exact nature of this event depends on the workflow transition(s) from it was fired. |  |  |  |
| Feedback Received  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **Work Scheduled**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |
| **On Hold**  The exact nature of this event depends on the workflow transition(s) from it was fired. |  | ✓ | ✓ |

## Audience

---

AGENTS ADMIN

## On This Page

---

- [Internal Jira Notifications](#OrangeTrackerInternalNotifications-InternalJiraNotifications)
- [Standard Notification Schemes](#OrangeTrackerInternalNotifications-StandardNotificationSchemes)
- [Details of Notification Schemes](#OrangeTrackerInternalNotifications-DetailsofNotificationSchemes)
  - [Standard Notification Scheme](#OrangeTrackerInternalNotifications-StandardNotificationScheme)
  - [Standard Scheme plus Notification to All Consultants on All Events](#OrangeTrackerInternalNotifications-StandardSchemeplusNotificationtoAllConsultantsonAllEvents)
  - [Standard Scheme with Reporter Notifications Reduced](#OrangeTrackerInternalNotifications-StandardSchemewithReporterNotificationsReduced)
  - [Standard Scheme plus Notification to Consultants on Create Issue](#OrangeTrackerInternalNotifications-StandardSchemeplusNotificationtoConsultantsonCreateIssue)
  - [Standard Scheme with Reporter Notifications Reduced plus Notification to Consultants on Create Issue](#OrangeTrackerInternalNotifications-StandardSchemewithReporterNotificationsReducedplusNotificationtoConsultantsonCreateIssue)
  - [Standard Scheme plus Notification to Project Managers on Create Issue](#OrangeTrackerInternalNotifications-StandardSchemeplusNotificationtoProjectManagersonCreateIssue)
  - [Standard Scheme with Reporter Notifications Reduced plus Notification to Project Managers on Create Issue](#OrangeTrackerInternalNotifications-StandardSchemewithReporterNotificationsReducedplusNotificationtoProjectManagersonCreateIssue)
  - [Standard Scheme with Reporter Feedback and Resolve plus Notification to Consultants on Create Issue](#OrangeTrackerInternalNotifications-StandardSchemewithReporterFeedbackandResolveplusNotificationtoConsultantsonCreateIssue)
  - [SU Standard - Level 1 Reporter : Level 1 Watchers : Consultants on Create Issue](#OrangeTrackerInternalNotifications-SUStandard-Level1Reporter:Level1Watchers:ConsultantsonCreateIssue)
  - [SU Standard - Level 2 Reporter : Level 2 Watchers : Consultants on Create Issue](#OrangeTrackerInternalNotifications-SUStandard-Level2Reporter:Level2Watchers:ConsultantsonCreateIssue)
  - [SU Standard - Level 1 Reporter : Level 2 Watchers : Consultants on Create Issue](#OrangeTrackerInternalNotifications-SUStandard-Level1Reporter:Level2Watchers:ConsultantsonCreateIssue)
  - [SU Standard - Level 1 Reporter : Level 1 Watchers : PM on Create Issue](#OrangeTrackerInternalNotifications-SUStandard-Level1Reporter:Level1Watchers:PMonCreateIssue)
- [Audience](#OrangeTrackerInternalNotifications-Audience)

## Related Pages

---

- Page:[Login for all Atlassian Cloud Products](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943058/Login+for+all+Atlassian+Cloud+Products)
- Page:[Orange Tracker Personal Settings](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970956/Orange+Tracker+Personal+Settings)
- Page:[Orange Tracker Workflow Transitions and Communications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications)
- Page:[Orange Tracker Training Resources](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941521/Orange+Tracker+Training+Resources)
- Page:[Orange Tracker Canned Responses](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952101/Orange+Tracker+Canned+Responses)
- Page:[Orange Tracker Customer Satisfaction Surveys](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159944128/Orange+Tracker+Customer+Satisfaction+Surveys)
- Page:[Orange Tracker Assets and Asset Management](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952177/Orange+Tracker+Assets+and+Asset+Management)
- Page:[Orange Tracker Knowledge Base](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949258/Orange+Tracker+Knowledge+Base)
- Page:[Orange Tracker Internal Notifications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952210/Orange+Tracker+Internal+Notifications)
- Page:[Orange Tracker Comments and Talking to Customers](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949480/Orange+Tracker+Comments+and+Talking+to+Customers)
- Page:[Orange Tracker Customer Notifications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951630/Orange+Tracker+Customer+Notifications)
- Page:[Adding Customers to a Project in Orange Tracker](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943060/Adding+Customers+to+a+Project+in+Orange+Tracker)
