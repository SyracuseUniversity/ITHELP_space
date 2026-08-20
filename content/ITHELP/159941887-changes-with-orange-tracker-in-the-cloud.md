---
title: "Changes with Orange Tracker in the Cloud"
confluence_id: "159941887"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941887/Changes+with+Orange+Tracker+in+the+Cloud"
version: 16
last_modified: "2023-11-22T14:36:52.000Z"
status: "current"
parent_id: "159941388"
---

The Orange Tracker team is migrating the Orange Tracker (OT) system to the cloud. With this move, we will be migrating into a newer application that is more suited for our needs here on campus. This new application will be similar to the previous version, but there will be a few minor changes when migrating to this new application.

The OT cloud system will be based on Atlassian's Jira Service Management (JSM). This application will combine the core Jira features of our original application, and add many features based on service requests, incident management, change management, and asset management.

This page will help document the changes and show the new features. The OT team will also offer training for teams who wish to learn more about the changes in order to help prepare for this migration.

- [What is Changing](#ChangeswithOrangeTrackerintheCloud-WhatisChanging)
  - [New Layout](#ChangeswithOrangeTrackerintheCloud-NewLayout)
  - [Customer Access](#ChangeswithOrangeTrackerintheCloud-CustomerAccess)
  - [Restricted Comments](#ChangeswithOrangeTrackerintheCloud-RestrictedComments)
  - [Issue Types](#ChangeswithOrangeTrackerintheCloud-IssueTypes)
  - [REST API Access](#ChangeswithOrangeTrackerintheCloud-RESTAPIAccess)
- [What is Leaving](#ChangeswithOrangeTrackerintheCloud-WhatisLeaving)

### What is Changing

There will be a few minor changes when migrating to this new application.

#### New Layout

Since we are staying within the Atlassian ecosystem, the overall core functions and features will remain. The layout does change to account for everything:

**Current Orange Tracker**

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941887/6529_Jira.png?api=v2)

**New Orange Tracker**

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941887/6529_JSM.png?api=v2)

You can see we still have all the major fields within each issue. Summary, Description, Assignee, Reporter, Components, date fields, status, Links, Comments, and more will all remain. We will gain a section for SLA's if your project would like to use this feature.

#### Customer Access

Customer accounts will have limited access to the system. They will no longer have access to the main application and will use one of the following methods to submit tickets:

- Email the project address
- Use the new customer portal

Customers can still receive email notifications about the issue and respond to that email just like they currently do. In addition, they can use the portal to track their existing tickets and communicate with the support team. This gives the customer options on how to work with the support team.

The customer portal will be an evolving implementation to provide a consistent and enhanced user experience for customers (and Service Desk Agents).

#### Restricted Comments

Restricted Comments are easier. With our existing system you would have to select the "Add Comment" button and then select to restrict it. Now, with the new system, you'll select the restriction first with the "Add internal note" or the "Reply to customer" buttons.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941887/Screenshot%202023-05-08%20at%2011.35.09%20AM.png?api=v2)

Internal notes have a light yellow shading and display "internal note" near the top of each comment.

Additional details on Internal Notifications is available at [Orange Tracker Internal Notifications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159952210/Orange+Tracker+Internal+Notifications).

#### Issue Types

There will be some changes with issues types. Service Request will still be used and that will cover 90% of the projects. For the other issue types, the following table will show the translation to the new issue types:

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941887/IssueTypes.png?api=v2)

#### REST API Access

Some teams utilize Atlassian's REST API to help automate certain function within their project. The REST API will still be available when moving to the cloud, but the URL and access will change. Basic Authentication will still be allowed, but you'll have to generate an API token. For more information please see the following pages:

- Basic Authentication: <https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/>
- API tokens: <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>

We will be working on providing a standard and more secure process in the future. Please reach out to the team if you have any questions.

### What is Leaving

With migrating to Jira Service Management, some features will not be available:

- JSM does not utilize Kanban or Agile Boards or the agile reporting  templates
- JSM does not utilize the software development tooling like release management and versioning
- JSM does not utilize Epic, Story, or Bug Issue Types (see above mapping for how these will be display after the migration)
