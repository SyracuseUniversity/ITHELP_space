---
title: "Project Email Address as Request Participant and Mail Loops"
confluence_id: "159951455"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159951455/Project+Email+Address+as+Request+Participant+and+Mail+Loops"
version: 30
last_modified: "2023-08-04T14:26:51.000Z"
status: "current"
parent_id: "159941887"
---

## Recent Action

---

The AAP team has removed access to the following project email addresses:

- aascsys@syr.edu
- accesibl@ot.syr.edu
- acshelp@ot.syr.edu
- acsserv@ot.syr.edu
- adtt@ot.syr.edu
- aeaweb@ot.syr.edu
- arch@ot.syr.edu
- as@ot.syr.edu
- asweb@ot.syr.edu
- auxhelp@ot.syr.edu
- bb@ot.syr.edu
- bsrrep@ot.syr.edu
- catering@ot.syr.edu
- citrus@ot.syr.edu
- cisunix@ot.syr.edu
- consult@cas.syr.edu
- dlp@ot.syr.edu
- ecscit@syr.edu
- esehelp@ot.syr.edu
- falk@ot.syr.edu
- falkweb@ot.syr.edu
- firstyear@syr.edu
- help@ot.syr.edu
- housing@ot.syr.edu
- hrssc@ot.syr.edu
- idmhelp@syr.edu, idmhelp@ot.syr.edu
- infosec@ot.syr.edu
- imodules@ot.syr.edu
- itscm@ot.syr.edu
- lawfacil@ot.syr.edu
- lawhelp@ot.syr.edu
- lcscit@ot.syr.edu
- lits@ot.syr.edu
- maxcomms@syr.edu, maxcomms@ot.syr.edu
- maxictsys@ot.syr.edu
- ndd@ot.syr.edu
- ols@ot.syr.edu
- sehelp@ot.syr.edu
- siihelp@syr.edu, siihelp@ot.syr.edu
- soe@syr.edu
- uchelp@ot.syr.edu
- vett@ot.syr.edu
- vpa@ot.syr.edu
- wiring@ot.syr.edu

## Background Information

---

Project teams have noticed several rejected messages within their project mail log. The tickets have the project email address listed in the Request Participants field. These participants are notified when comments are made. Since the email address is the project email address, this email would create a mail loop and the system rejects this message. This is good as it prevents a problem, but we don't want to project email address listed in this field. This also creates additional "noise" in project email logs.

The following screenshot depicts the error shown in Project email logs. The initial request creation resulted in a ticket being created but at the same time the Request Participant was added with the email forward. A reply was sent to a forwarded address, then came back into the project email queue. These will be Rejected, Sent from within the project, and caught by the Jira mail loop filter.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159951455/Screenshot%202023-08-01%20at%2016.10.08.png?api=v2)

Atlassian adds the original mail address as a CC to any email that is forwarded to the system. We forward most mail to the cloud. For example, aascsys@syr.edu is forwarded to aascsys@su-jsm.atlassian.net. Atlassian will auto-add the original email address to the email as a CC. And we allow all CC addresses to be a Request Participant for that ticket.

Atlassian has a public reference page: <https://confluence.atlassian.com/jirakb/email-requests-rejected-due-to-jira-mail-loop-filter-1189798024.html>

## Current Status

---

The AAP team will be removing access for those project email addresses to the JSM cloud site. This will only stop that address from being added as a Request Participant and stop the rejected message. Communications to the Reporter, Assignee, and all other individuals will function as normal.

## Action Needed

---

If you notice your project email address in the Request Participant field, feel free to remove it from any existing ticket. And please contact us at [aascsys@syr.edu](mailto:aascsys@syr.edu) and we will work with you to remove access to that account in order to correct this for future tickets.

Email requests submitted to an @ot.syr.edu vanity address after the fix has been applied **will still route into Jira and create tickets** and retain that functionality.
