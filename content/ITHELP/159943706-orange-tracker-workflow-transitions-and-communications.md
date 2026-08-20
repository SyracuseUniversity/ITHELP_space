---
title: "Orange Tracker Workflow Transitions and Communications"
confluence_id: "159943706"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications"
version: 18
last_modified: "2023-09-18T12:46:16.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "orange-tracker"
  - "ot"
  - "jira"
  - "workflow"
  - "jsm"
  - "comments"
  - "agent"
---

This document outlines the automation between communications with the Customer and the statuses in the project workflow. This document is to help guide project Agents and Administrators on understanding when automated events will fire. Some ticket actions do not fire an workflow transition event. This is by design to allow projects use a global standard and have the flexibility to change workflow status or not.

When an Agent communicates to the Reporter, they can use two methods:

1. Reply to Customer
2. Request Feedback

The two methods are very similar, but the Request Feedback method will utilize workflow statuses and the Reply to Customer does not.

To learn more about just communicating to customers, please see [Orange Tracker Comments and Talking to Customers](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159949480/Orange+Tracker+Comments+and+Talking+to+Customers)

## Reply to Customer

Using the Reply to Customer method will allow Agents to send a message to the Reporter but not change the workflow status. This is for projects who do not need to keep track of the workflow within tickets.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159943706/Comments.png?api=v2)

## Request Feedback

This option is a manual transition where the Agent will select the "Request Feedback" workflow button.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159943706/Screenshot%202023-08-14%20at%202.27.34%20PM.png?api=v2)

This will bring up a Comment screen where the Agent will write their message in the "Respond to Customer" tab.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159943706/Screenshot%202023-08-14%20at%202.39.25%20PM.png?api=v2)

Once the Agent selects the "Request Feedback" button, the workflow status will change to "Waiting for Feedback" and the comment will be sent to the Customer.

## Transition from "Waiting for Feedback" to "Open"

This transition happens when the Customer responds to a ticket in the "Waiting for Feedback" status. OT Administrators have a global automation rule that handles this action for all projects: [Orange Tracker Automation](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation)

## Transition a Resolved/Closed Ticket to "Reopened"

This transition happens when the Reporter responds to a ticket in the "Resolved" or "Closed" status. OT Administrators have a global automation rule that handles this action for all projects: [Orange Tracker Automation](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation)

## Audience

---

AGENTS

## On This Page

---

- [Reply to Customer](#OrangeTrackerWorkflowTransitionsandCommunications-ReplytoCustomer)
- [Request Feedback](#OrangeTrackerWorkflowTransitionsandCommunications-RequestFeedback)
- [Transition from "Waiting for Feedback" to "Open"](#OrangeTrackerWorkflowTransitionsandCommunications-Transitionfrom"WaitingforFeedback"to"Open")
- [Transition a Resolved/Closed Ticket to "Reopened"](#OrangeTrackerWorkflowTransitionsandCommunications-TransitionaResolved/ClosedTicketto"Reopened")
- [Audience](#OrangeTrackerWorkflowTransitionsandCommunications-Audience)

## Related Content

---

- Page:[Orange Tracker Personal Settings](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970956/Orange+Tracker+Personal+Settings)
- Page:[Orange Tracker Workflow Transitions and Communications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications)
- Page:[Orange Tracker Canned Responses](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952101/Orange+Tracker+Canned+Responses)
- Page:[Orange Tracker Assets and Asset Management](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952177/Orange+Tracker+Assets+and+Asset+Management)
- Page:[Orange Tracker Knowledge Base](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949258/Orange+Tracker+Knowledge+Base)
- Page:[Orange Tracker Internal Notifications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952210/Orange+Tracker+Internal+Notifications)
- Page:[Orange Tracker Comments and Talking to Customers](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949480/Orange+Tracker+Comments+and+Talking+to+Customers)
- Page:[Orange Tracker Customer Notifications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951630/Orange+Tracker+Customer+Notifications)
