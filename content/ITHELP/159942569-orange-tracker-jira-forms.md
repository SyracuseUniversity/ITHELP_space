---
title: "Orange Tracker Jira Forms"
confluence_id: "159942569"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942569/Orange+Tracker+Jira+Forms"
version: 9
last_modified: "2023-09-25T12:44:52.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "form"
  - "create"
  - "forms"
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
  - "agent"
---

## Overview

Jira Forms help create tickets within OT projects with guided questions from the project team to help gather the correct information in order to solve the issue. You can add forms to Customer Request Types to gather more structured information when customers raise requests, or to create issues.

If additional questions or information is needed within a ticket, Jira Forms can help get that information and save it within the ticket. Projects can create unique questions and data points. These fields are not the typical custom fields Jira Administrators have to create in order for projects to use. They are sudo-custom fields and cannot be searched through using Jira's JQL.

Jira Forms can be useful for several items:

- Provide a more robust customer feedback survey solution.
  - Choose the option to “add to an issue” this will allow for agents and admins to be able to quickly include the form before closing/resolving an issue.
- Request Forms
  - Create a form that would have direct customer access in the Portal.
  - Once form is completed (customized) it will generate to the project queue of who owns the form.
  - Examples: Orange Help project can include a request form for Listserv requests, Blackboard project can include a request form for merge course requests
- Any form you would like a customer to complete can be created in Jira Forms using an existing template or customized template.
  - By setting the form settings to “recommend in issue” an “add form” option appears for Jira agent. The agent will have the opportunity to select a form associated with the project and add it directly to an issue for customer completion.

## Create a Jira Form

Project Managers have access to create and edit Jira Forms. After selecting your project, on the left panel of the screen you will need to select Project Settings and the navigate to Forms.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942569/Capture5420232.PNG?api=v2)

The Forms screen will display and show any existing Forms for the project

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942569/Capture5420233.PNG?api=v2)

To start a new form you will select the Create Form button

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942569/Capture5420234.PNG?api=v2)

The next screen will display the new form. You'll also see three tabs: Build, Preview, and Settings

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942569/Capture5420235.PNG?api=v2)

Under the Build tab, this is where you will begin your form creation. There are two options when creating a new form:

1. ***Creating a form using a pre-existing template:*** You can browse the many built in templates that Jira forms has built in and customize it to your project needs. You will have the ability to delete, re-label or add to a built in template.
2. ***Creating your own template:*** You have the ability to add many field types and add sections to the form as well starting from a blank form. This is done by adding Field Types and Sections.
   1. **Field Types:** Text Fields, Choice Fields,  Date Fields, Numeric Fields,  User Fields and Other Fields. When selecting one of these options a window pane will appear on the right side of the screen so you can change things such as the label name, description, required response option, minimum maximum characters, etc...
   2. **Other Fields:** Include Asset Objects which is linked to a "Jira Field" ex. Assignee, Reporter, Components, etc....

When you complete your new form, use the "Save Changes" button to save your work. You can then select the "Preview" tab as this will allow for you to view what the customer will see when filling out the form.

Next, you will need to select the "Settings" tab.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942569/Capture5420237.PNG?api=v2)

### **Request Form**

When you add a form to the request form for a request type, it’ll appear for customers to fill out when they raise a request of that request type in the portal. <https://su-jsm.atlassian.net/servicedesk/customer/portals>

In the portal, when a customer is raising a request:

- The form can be used on its own for raising requests, or used alongside existing Jira fields.
- The form will appear underneath any Jira fields that were added when configuring the request type.
- Form fields will look much like regular Jira fields – customers won’t notice that the form is a separate object to the usual request form that they’re used to filling out. However, after the request is raised, the form will be separated, and customers will be able to see it under **Forms** on their request.
- If you want to use the form on its own, but automatically fill Jira fields with form field information, you can link form fields to Jira fields.

TIP: Do not duplicate fields. Your "Request Type" will already have built in fields, so a form option will be adding to the pre-existing fields.

### **Create New Issue**

You can choose to use the form to create new issues in OT using a URL. This URL can be shared externally so that forms can be filled out by any licensed, logged-in Jira users and create issues. This option in settings is for Project Agents/Consultants. **This option is not available in the portal and it is not customer facing.**

## Audience

---

ADMIN

## On This Page

---

- [Overview](#OrangeTrackerJiraForms-Overview)
- [Create a Jira Form](#OrangeTrackerJiraForms-CreateaJiraForm)
  - [Request Form](#OrangeTrackerJiraForms-RequestForm)
  - [Create New Issue](#OrangeTrackerJiraForms-CreateNewIssue)
- [Audience](#OrangeTrackerJiraForms-Audience)

## Related Content

---

- Page:[Login for all Atlassian Cloud Products](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943058/Login+for+all+Atlassian+Cloud+Products)
- Page:[Orange Tracker for Agents](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949749/Orange+Tracker+for+Agents)
- Page:[Orange Tracker Personal Settings](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970956/Orange+Tracker+Personal+Settings)
- Page:[Orange Tracker Workflow Transitions and Communications](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943706/Orange+Tracker+Workflow+Transitions+and+Communications)
- Page:[Orange Tracker Issue User Roles](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159970567/Orange+Tracker+Issue+User+Roles)
