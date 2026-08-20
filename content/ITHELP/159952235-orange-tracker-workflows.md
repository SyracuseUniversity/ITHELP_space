---
title: "Orange Tracker Workflows"
confluence_id: "159952235"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952235/Orange+Tracker+Workflows"
version: 7
last_modified: "2023-09-18T17:17:18.000Z"
status: "current"
parent_id: "159941388"
---

The workflow is a set of statuses and transitions that are used in an ticket's lifecycle. A status represents the state of a ticket at a specific point in your workflow. A ticket can be in only one status at a given point in time. A transition is a link between two statuses that enables a ticket to move from one status to another. In order for a ticket to move between two statuses, a transition must exist. A ticket starts with an open status and moves through a series of one or more steps until it is closed. Each project can decide which workflow is assigned.

The ITS AASC AAP team has designed workflows based on user needs and feedback. These workflows should fit most projects as they have enough steps to properly report on, as well as the inter-connectivity to move from Open to Closed if the process requires. These workflows are designed to be general to fit the majority of projects. If there is a need to design a custom workflow, or have any questions about workflow, please contact the AAP team at [aascsys@syr.edu](mailto:aascsys@syr.edu)

The standard workflows that have been created are based on the previous local instance of Orange Tracker. The AAP team will be reviewing the standard workflow and the new workflows within the cloud system and making changes to fit the need of the projects and the system.

Orange Tracker has a few basic workflow schemes:

# Standard Workflow v4.0

In Progress. Currently being developed in 2023. This workflow is similar to workflow v3.0. This workflow incorporates the built-in features from Orange Tracker in the cloud.

**List of Improvements:**

- Remove the workflow button **Consultant Comment**. Teams will use the built-in feature **Add Internal Note**.
- Adjust the permissions for the **Request Feedback**, **Start Progress**, **Stop Progress**, **Reschedule**, and **Put on Hold** transitions. These can now be done by all project agents and not just the Assignee.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/Screenshot%202023-09-18%20at%2012.23.03%20PM.png?api=v2)

# Standard Workflow v3.0

Developed in 2019. This workflow is similar to the current standard workflow most projects are running, with added features and improvements based on user feedback.

**List of Improvements:**

- Workflow button **Consultant Comment** creates a comment that is automatically restricted the Consultants.
  - This button opens up a Comment box that is auto-restricted to Consultants and helps the team create restricted comments within the ticket.
- Ability to use the **Request for Feedback** workflow button at different steps of the workflow.
  - Another request from users was the ability to ask another question to the Reporter. Currently, in the Standard Workflow v2.0, if a Consultant uses the **Request for Feedback** button and they want to ask another question, they have to use the **Start Progress** and **Stop Progress** buttons in order to see and use the **Request for Feedback** button again.
  - Adjustments were made that allow the **Request for Feedback** button to be available at multiple stages within the workflow.
- The **Resolve** status has been removed to simplify the workflow and eliminate having multiple closed statuses. The workflow still has the existing **Resolve Issue** and **Close Issue** workflow buttons and they will work very similar to the previous workflow buttons.
  - The **Resolve Issue** button will still fire the Resolve event, but transition to the Closed Status.
  - The **Close Issue** button will fire the Close event, and will transition to the Closed Status.
  - These events interact with the notification scheme and typically email will be sent to the Reporter on **Resolve** and **Close** is reserved as a 'Soft Close' and email is not sent out to the Reporter.
- **Resolve** and **Close** screens will contain the same fields. Both screens have the ability to assign the ticket, link tickets, and add components before completely the ticket.
  - In previous workflows, the Resolve and Close screens had different fields and they should be fairly similar to each other. The Resolve screen had Resolution, Linked Issues, Assignee, and the Feedback Survey. The Close screen had Resolution, Assignee, and Components. The problem is when users Close a ticket they cannot link another ticket, or if users Resolves an ticket, they cannot set the component.
  - The Feedback Survey still remains under only the Resolve screen, but all other fields have been added to both screens.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/Workflow3.png?api=v2)

# Standard Workflow v2.0

Created in 2015. This workflow is the most used workflow we offer. This workflow is preferred as it is an upgrade version of v1.2.

![A screenshot of the standard workflow 2.0 is shown](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/image2019-4-18_11-9-20.png?api=v2)

This workflow is based from the v1.2 workflow and adds two more transitions:

- Schedule Work (status:  Scheduled – you should set a due date when you schedule the work)
- Put On Hold (status:  On Hold)

![Workflow button with two added options in Standard Workflow 2.0 scheme](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/Workflow%20with%202%20added%20options.PNG?api=v2)

Created tickets have a default status of Open.  The workflow options available are:  "Start Progress," "Request Feedback," and under the drop-down menu for the "Workflow" button:  "Resolve Issue," "Close Issue," "Mark as Spam."

![Workflow buttons on main screen](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/workflow%20buttons.PNG?api=v2)

When a ticket is in the "Scheduled" status, a button to "Reschedule" will appear.  You can use this to change the due date of the ticket (the status will remain "Scheduled").

If a ticket has a status of "Waiting for feedback" and the Reporter replies to the email that was generated by the "Request Feedback" process, the status of the ticket will automatically change to "Open" and the email from the reporter will be added as a comment to this ticket.

# Standard Workflow v1.2

April 2013. This is the easiest workflow with 6 statuses:

![A screenshot of the standard workflow 1.2 is shown](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/image2019-4-18_11-6-35.png?api=v2)

Created tickets have a default status of Open.  The workflow options available are:  "Start Progress," "Request Feedback," and under the drop-down menu for the "Workflow" button:  "Resolve Issue," "Close Issue," "Mark as Spam."

![Workflow buttons on main screen](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/workflow%20buttons.PNG?api=v2)

![Workflow button showing options](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/More%20workflow%20buttons.PNG?api=v2)

Selecting workflow options changes the status of the ticket.  You can then use the status to track how work on the ticket is progressing (including in searches, filters, and dashboards).  Tickets in different statuses may have different workflow buttons available.   For example, if you select "Start Progress",  the ticket will have a status of "In Progress," and a new button will appear that lets you "Stop Progress."

![In Progress Status showing that Stop Progress button is now available](https://answers.atlassian.syr.edu/wiki/download/attachments/159952235/In%20Progress.PNG?api=v2)

If you close a ticket, the status will be closed, and a new button that lets you "Reopen" the ticket appears (all other workflow options are no longer available unless you reopen the ticket).

| Button | Resulting Status |
| --- | --- |
| Start Progress | In Progress |
| Stop Progress | Open |
| Request Feedback | Waiting for Feedback |
| Resolve | Resolved |
| Close | Closed |
| Reopen | Reopened |
| Mark as Spam | Closed (with a resolution type of spam) |

If a ticket has a status of "Waiting for feedback" and the Reporter replies to the email that was generated by the "Request Feedback" process, the status of the ticket will automatically change to "Open" and the email from the reporter will be added as a comment to this ticket.

## Audience

---

AGENTS ADMIN

## On This Page

---

- [Standard Workflow v4.0](#OrangeTrackerWorkflows-StandardWorkflowv4.0)
- [Standard Workflow v3.0](#OrangeTrackerWorkflows-StandardWorkflowv3.0)
- [Standard Workflow v2.0](#OrangeTrackerWorkflows-StandardWorkflowv2.0)
- [Standard Workflow v1.2](#OrangeTrackerWorkflows-StandardWorkflowv1.2)

## Related Pages

---

- Page:[Orange Tracker Project Email Request Log](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951228/Orange+Tracker+Project+Email+Request+Log)
- Page:[Login for all Atlassian Cloud Products](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943058/Login+for+all+Atlassian+Cloud+Products)
- Page:[Orange Tracker for Agents](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949749/Orange+Tracker+for+Agents)
- Page:[Orange Tracker Personal Settings](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970956/Orange+Tracker+Personal+Settings)
- Page:[Orange Tracker Workflow Transitions and Communications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications)
- Page:[Orange Tracker Issue User Roles](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970567/Orange+Tracker+Issue+User+Roles)
- Page:[Orange Tracker Training Resources](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941521/Orange+Tracker+Training+Resources)
- Page:[Orange Tracker Service Level Agreements](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159948952/Orange+Tracker+Service+Level+Agreements)
- Page:[Orange Tracker Canned Responses](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952101/Orange+Tracker+Canned+Responses)
- Page:[Orange Tracker Customer Satisfaction Surveys](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159944128/Orange+Tracker+Customer+Satisfaction+Surveys)
- Page:[Orange Tracker Jira Forms](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942569/Orange+Tracker+Jira+Forms)
- Page:[Orange Tracker Assets and Asset Management](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952177/Orange+Tracker+Assets+and+Asset+Management)
