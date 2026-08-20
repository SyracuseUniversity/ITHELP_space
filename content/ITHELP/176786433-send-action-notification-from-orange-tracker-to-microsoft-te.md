---
title: "Send Action Notification from Orange Tracker to Microsoft Teams"
confluence_id: "176786433"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/176786433/Send+Action+Notification+from+Orange+Tracker+to+Microsoft+Teams"
version: 8
last_modified: "2024-11-14T18:22:43.231Z"
status: "current"
parent_id: "159941388"
---

Orange Tracker can be integrated into Microsoft Teams so that any time an action occurs within Orange Tracker (i.e. Issue Created, Issue Updated), a message can be sent to a Microsoft Teams channel. This is done through configurations in both environments through automations, workflows, and webhooks. This will generate an Adaptive Card in an MS Teams Channel similar to the following screenshot:

![](https://answers.atlassian.syr.edu/wiki/download/attachments/176786433/Screenshot%202024-07-12%20at%201.02.07%E2%80%AFPM.png?api=v2)

## Microsoft Teams Setup

1. Decide which MS Teams Channel should receive updates sent by Orange Tracker
2. On the desired MS Teams Channel, under the **Channel Options** (…), select **Workflows**
3. Select the **Post to a channel when a webhook request is received** option
4. Name the workflow
5. Select Add workflow
6. Copy the URL presented on the following dialogue

## Orange Tracker Setup

Must have Project Administrator role.

1. Navigate to **Project Settings**
2. Select **Automation**
3. Select **Create New Rule**
4. Select the desired trigger to send the notification (i.e. Issue Created, Issue Updated)
5. Add another **THEN: Add an action** component
6. Search for and select **Send web request**
7. In the *Web request URL* field, enter the URL copied from MS Teams
8. Ensure the *HTTP method* is set to **POST**
9. Set the *Web request body* to **Custom data** and use the following code block:

   ```
   {
      "type":"message",
      "attachments":[
         {
            "contentType":"application/vnd.microsoft.card.adaptive",
            "contentUrl":null,
            "content":{
               "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
               "type":"AdaptiveCard",
               "version":"1.3",
               "body":[
                  {
               "type": "TextBlock",
               "size": "Medium",
               "weight": "Bolder",
               "text": "[Issue Created] {{issue.key}}: {{issue.summary}}"
           },
           {
               "type": "ColumnSet",
               "columns": [
                   {
                       "type": "Column",
                       "width": "auto",
                       "items": [
                           {
                               "type": "Image",
                               "url": "{{reporter.avatarUrls.48x48}}",
                               "size": "Small"
                           }
                       ]
                   },
                   {
                       "type": "Column",
                       "items": [
                           {
                               "type": "TextBlock",
                               "weight": "Bolder",
                               "text": "{{issue.reporter.displayName}}",
                               "wrap": true
                           },
                           {
                               "type": "TextBlock",
                               "spacing": "None",
                               "text": "Created {{issue.created.mediumDateTime}}",
                               "isSubtle": true,
                               "wrap": true
                           }
                       ],
                       "width": "stretch"
                   }
               ]
           },
           {
               "type": "ColumnSet",
               "columns": [
                   {
                       "type": "Column",
                       "width": 1,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "Issue Type",
                               "wrap": true,
                               "weight": "Bolder"
                           }
                       ]
                   },
                   {
                       "type": "Column",
                       "width": 3,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "{{issue.issueType.name}}",
                               "wrap": true
                           }
                       ]
                   }
               ]
           },
           {
               "type": "ColumnSet",
               "columns": [
                   {
                       "type": "Column",
                       "width": 1,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "Customer Request Type",
                               "wrap": true,
                               "weight": "Bolder"
                           }
                       ]
                   },
                   {
                       "type": "Column",
                       "width": 3,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "{{issue.Request Type.requestType.name}}",
                               "wrap": true
                           }
                       ]
                   }
               ]
           },
           {
               "type": "ColumnSet",
               "columns": [
                   {
                       "type": "Column",
                       "width": 1,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "Issue Priority",
                               "wrap": true,
                               "weight": "Bolder"
                           }
                       ]
                   },
                   {
                       "type": "Column",
                       "width": 3,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "{{issue.priority.name}}",
                               "wrap": true
                           }
                       ]
                   }
               ]
           },
           {
               "type": "ColumnSet",
               "columns": [
                   {
                       "type": "Column",
                       "width": 1,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "Issue Description",
                               "wrap": true,
                               "weight": "Bolder"
                           }
                       ]
                   },
                   {
                       "type": "Column",
                       "width": 3,
                       "items": [
                           {
                               "type": "TextBlock",
                               "text": "{{issue.description}}",
                               "wrap": true
                           }
                       ]
                   }
               ]
           }
               ],
               "actions": [
                  {
                     "type": "Action.OpenUrl",
                     "title": "View Issue",
                     "url": "{{issue.url}}"
                 }
               ],
            }
         }
      ]
   }
   ```
10. In the Headers, set `Content-Type` to `application/json`
11. Select **Turn on rule** (top-right), then name your new automation
12. Select **Turn On Rule** to save
