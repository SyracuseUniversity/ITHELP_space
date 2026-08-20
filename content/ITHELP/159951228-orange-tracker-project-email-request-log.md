---
title: "Orange Tracker Project Email Request Log"
confluence_id: "159951228"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951228/Orange+Tracker+Project+Email+Request+Log"
version: 13
last_modified: "2023-09-01T15:43:06.000Z"
status: "current"
parent_id: "159941388"
labels:
  - "email"
  - "admin"
  - "orange-tracker"
  - "ot"
  - "jira"
  - "jsm"
---

## Overview

---

This document outlines viewing the email requests for your Orange Tracker project. Project Managers and Administrators have the ability to view the project email requests. It is recommended to review the Email Requests log, for a Project, to view incoming email activity. If a message is REJECTED, it will not create a ticket.

As of 7/24/2023 3pm, we have DISABLED one of the two DMARC settings for the system. But we still find DMARC errors within mail due to third party mail systems, like Gmail.

As of 8/8/2023 1pm, we DISABLED the second DMARC setting, focusing more on the application.

## Viewing the Project Email Log

---

If you are a Project Manager, please use the left navigation bar and click on the **Project Settings** button near the bottom

Next, find the **Email Requests** button on the left navigation bar and click it

On this screen you'll find the email address used for the project, <***projectkey>***@su-jsm.atlassian.net

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159951228/image2023-7-25_9-25-51.png?api=v2)

Next, click on the **View Logs** link to view the log

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159951228/image2023-7-25_9-30-36.png?api=v2)

Most logs will not have any errors and will show **New Requests** and **New Comments**. At times you may see errors

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159951228/image2023-7-25_9-32-8.png?api=v2)

## Email Log Errors

---

We have found errors and here are some common reasons for the messages:

### Rejected

- Failed a DMARC validation check
  - This typically happens when forms send a message as the reporter. This is a potential mail spoof.
- Auto-reply mail
  - This was a customer permissions issue and we have edited all projects to allow all users
  - This also could be the Forward method. Ensure you are forwarding messages correctly: <https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940689>
- Signup is not currently available
  - This was a customer permissions issue and we have edited all projects to allow all users
- Automated delivery status message
  - This typically  is an auto 'out of office' message

Atlassian has a more detailed page about the log and a list of processing errors: <https://support.atlassian.com/jira-service-management-cloud/docs/about-email-logs-in-jira-service-management/>

## On This Page

---

- [Overview](#OrangeTrackerProjectEmailRequestLog-Overview)
- [Viewing the Project Email Log](#OrangeTrackerProjectEmailRequestLog-ViewingtheProjectEmailLog)
- [Email Log Errors](#OrangeTrackerProjectEmailRequestLog-EmailLogErrors)

## Related Content

---

- Page:[Orange Tracker Project Email Request Log](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951228/Orange+Tracker+Project+Email+Request+Log)
- Page:[Orange Tracker Cloud - Issue Sharing & Collaboration](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159946604/Orange+Tracker+Cloud+-+Issue+Sharing+Collaboration)
- Page:[Orange Tracker Currently Tracked Projects & Issues](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942717/Orange+Tracker+Currently+Tracked+Projects+Issues)
- Page:[Orange Tracker New Project Request](https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159947266/Orange+Tracker+New+Project+Request)
