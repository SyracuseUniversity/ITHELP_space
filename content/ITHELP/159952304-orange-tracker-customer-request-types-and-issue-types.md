---
title: "Orange Tracker Customer Request Types and Issue Types"
confluence_id: "159952304"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159952304/Orange+Tracker+Customer+Request+Types+and+Issue+Types"
version: 14
last_modified: "2023-11-15T18:53:53.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
  - "agent"
---

This document outlines Customer Request Types and Issue Types for tickets in the Orange Tracker system. While Customer Request Types and Issue Types are project based, the Orange Tracker Administrators manage what issue types are available for projects. Customer Request Types are maintained by the project.

Customer Request Types are the types of requests that can be raised in your service project, such as ‘Get IT help’ or ‘Request a new account’. They direct your customers to the right place to submit their requests.

Customer Request Types are also needed in order for customers to view their issues within the portal. If an issue does not have a Customer Request Type then it will not show in the portal for the customer.

## The Difference Between Customer Request Types and Issue Types

All Customer Request Types in JSM are connected to a single Issue Type. **Customer** **Request Types** manage the specific settings of an issue (such as naming, portal customization, and work categories) while **issue types** manage the basic settings of an issue (such as workflows and fields).

Within a Service Desk Project, **one Issue Type** can be used/connected with **many different Customer Request Types.** For example, the *Purchase* Issue Type could be used for both the *Request new hardware* AND *Request new software* Request Types. And **each Customer****Request Type** can only be connected to **one Issue Type**. For example, the *Request new software* request type could use the *Purchase* issue type OR another issue type, but not both.

## Customer Request Types

Customer Request Types (CRT) are new and helps categorize the types of requests for a project. CRTs work within the portal to help guide customers to getting the right help on a problem. These request types will ask certain questions and create a ticket with the project.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159952304/RequestTypes.png?api=v2)

This is a critical field and a value needs to be entered in order for customer to receive notifications and be visible for the customer in the portal.

Project teams must ensure the CRT field has a value before they start communicating with the Customer. Orange Tracker administrators have developed an Automation rule that can be used: [Orange Tracker Automation](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation)

CRTs are specifically linked to Issue Types. A single CRT needs to be assigned to an Issue Type, but multiple CRTs can be assigned to the same Issue Type.

## Issue Types

Issue Types are different types of work. For the Orange Tracker system, this is a general field and most projects are limited to just the Service Request issue type.

If a project has multiple Issue Types, it is recommended to create a CRT for each Issue Type.

## Sub-Tasks

Sub-Tasks are a form of Issue Type, but a Customer Request Type cannot be used for Sub-Tasks. This means Customers will not receive email notifications and will not see the ticket in the portal. Sub-Tasks are designed to be used only for internal work teams and do not require customer notification.

## Audience

---

AGENTS

## On This Page

---

- [The Difference Between Customer Request Types and Issue Types](#OrangeTrackerCustomerRequestTypesandIssueTypes-TheDifferenceBetweenCustomerRequestTypesandIssueTypes)
- [Customer Request Types](#OrangeTrackerCustomerRequestTypesandIssueTypes-CustomerRequestTypes)
- [Issue Types](#OrangeTrackerCustomerRequestTypesandIssueTypes-IssueTypes)
- [Sub-Tasks](#OrangeTrackerCustomerRequestTypesandIssueTypes-Sub-Tasks)
- [Audience](#OrangeTrackerCustomerRequestTypesandIssueTypes-Audience)

## Related Pages

---

- Page:[Login for all Atlassian Cloud Products](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943058/Login+for+all+Atlassian+Cloud+Products)
- Page:[Orange Tracker Training Resources](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941521/Orange+Tracker+Training+Resources)
- Page:[Orange Tracker Customer Satisfaction Surveys](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159944128/Orange+Tracker+Customer+Satisfaction+Surveys)
- Page:[Adding Customers to a Project in Orange Tracker](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159943060/Adding+Customers+to+a+Project+in+Orange+Tracker)
- Page:[Orange Tracker Customer Portal](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159945235/Orange+Tracker+Customer+Portal)
