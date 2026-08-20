---
title: "Orange Tracker Automation"
confluence_id: "159949212"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation"
version: 32
last_modified: "2025-11-12T19:35:26.868Z"
status: "current"
parent_id: "159941388"
labels:
  - "automated"
  - "featured"
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
---

This document will help project Agents and Administrators understand the Automation feature within Orange Tracker (OT) and the current Automation rules set for the system.Automation rules are made up of three parts:

- **Triggers** that kick off the rule
- **Conditions** that refine the rule
- **Actions** that perform tasks

There are three scopes of Automation:

- Single Project runs for one specific project
- Multi-Project runs for several projects
- Global will runs for all projects

While Global Automation is a great option, the process of how each project operates is slightly different. That impacts the use of Global Automation and the better option is to allow projects to 'Opt-In' certain Multi-Project rules or create and maintain their own rules. This gives the greatest flexibility for all projects.

Atlassian has a great pages about Automation:

Basics of Automation: <https://support.atlassian.com/cloud-automation/docs/automation-basics/>

Detailed and Advanced Automation: <https://support.atlassian.com/cloud-automation/docs/jira-cloud-automation/>

## Project Automation

Project Administrators can add, edit, and remove project automation rules.

To review automation, select the Project Settings → Automation

This screen will show you all the rules, including the Multi-Project rules.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159949212/Screenshot%202023-08-17%20at%208.23.48%20AM.png?api=v2)

You can use the filters to show certain rules.

## Multi-Project Automation

OT Administrators will focus on creating a few multi-project rules that will allow certain projects to use standard rules. These rules can only be adjusted by the OT Administrators. Using multi-project rules allows projects to "Opt-Out" of the rule if that rule does not meet their needs.

Multi-project and Global rules we execution limits. Based on our current license, we have a limit of 1.2M executions per month. OT Administrators will monitor this usage and plan accordingly. They may seem like a large number, but the global rules fire often.

### Current Multi-Project Automation Rules

This is a list of current Multi-Project Automation Rules set by the OT Administrators

| **Rule Name** | **Description** |
| --- | --- |
| Customer Comments -> Transition to Open | When a customer responds to a ticket in "Waiting for Feedback" status, transition to "Open" |
| Reporter Reopens Closed Tickets | When the Reporter comments on a Resolved/Closed request, set the Status to "Reopened" |

### Opt-Out

All new and existing projects are automatically added into the Multi-Project Automation Rules. A project can request to Opt-Out and the OT Administrators will remove the project/s from one or all rules. This will allow projects to construct their own custom rule to better suit their needs.

If a project wants to opt-out of a standard rule, a project administrator will contact the OT administrators at [cdiapps@syr.edu](mailto:cdiapps@syr.edu) to have the project removed from the standard rule.

## Global Automation

OT Administrators can add, edit, and remove Global Automation rules. With the number of projects in OT and the way projects operate, global automation rules are not the ideal process for automating tasks.

Multi-project and Global rules we execution limits. Based on our current license, we have a limit of 1.2M executions per month. OT Administrators will monitor this usage and plan accordingly. They may seem like a large number, but the global rules fire often.

## Automation Recipes

We have a few automation recipes that you could use for your project or edit to fit your needs. Project Administrators can create project automation, edit existing ones, and maintain these project rules. Each rule has an Audit Log to track all actions and help the team understand when the rule fires.

### Customer Comments -> Transition to Open

When a customer responds to a ticket in "Waiting for Feedback" status, transition to "Open"

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159949212/Screenshot%202023-09-06%20at%208.58.37%20AM.png?api=v2)

### Reporter Reopens Closed Tickets

When the Reporter comments on a Resolved/Closed request, set the Status to "Reopened"

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159949212/Screenshot%202023-09-05%20at%203.56.25%20PM.png?api=v2)

### Auto-Add Request Type

When a new issue is created, or moved without a Request Type, add the Email Request Type.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159949212/Screenshot%202023-09-06%20at%209.05.13%20AM.png?api=v2)

### Unassign Moved Tickets

Unassign any Tickets Moved into the Project where the current assign is not part of the project team.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159949212/Screenshot%202023-09-06%20at%209.08.22%20AM.png?api=v2)

## On This Page

---

- [Project Automation](#OrangeTrackerAutomation-ProjectAutomation)
- [Multi-Project Automation](#OrangeTrackerAutomation-Multi-ProjectAutomation)
  - [Current Multi-Project Automation Rules](#OrangeTrackerAutomation-CurrentMulti-ProjectAutomationRules)
  - [Opt-Out](#OrangeTrackerAutomation-Opt-Out)
- [Global Automation](#OrangeTrackerAutomation-GlobalAutomation)
- [Automation Recipes](#OrangeTrackerAutomation-AutomationRecipes)
  - [Customer Comments -> Transition to Open](#OrangeTrackerAutomation-CustomerComments->TransitiontoOpen)
  - [Reporter Reopens Closed Tickets](#OrangeTrackerAutomation-ReporterReopensClosedTickets)
  - [Auto-Add Request Type](#OrangeTrackerAutomation-Auto-AddRequestType)
  - [Unassign Moved Tickets](#OrangeTrackerAutomation-UnassignMovedTickets)

## Related Content

---

- Page:[Orange Tracker Project Email Request Log](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951228/Orange+Tracker+Project+Email+Request+Log)
- Page:[Orange Tracker Cloud - Issue Sharing & Collaboration](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159946604/Orange+Tracker+Cloud+-+Issue+Sharing+Collaboration)
- Page:[Orange Tracker Currently Tracked Projects & Issues](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942717/Orange+Tracker+Currently+Tracked+Projects+Issues)
- Page:[Orange Tracker New Project Request](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159947266/Orange+Tracker+New+Project+Request)
- Page:[Orange Tracker Automation](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159949212/Orange+Tracker+Automation)
