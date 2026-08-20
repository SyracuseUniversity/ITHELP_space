---
title: "Internet Explorer mode in Microsoft Edge"
confluence_id: "159942752"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942752/Internet+Explorer+mode+in+Microsoft+Edge"
version: 2
last_modified: "2024-03-25T14:23:17.000Z"
status: "current"
parent_id: "159941373"
---

## What is IE mode?

Internet Explorer mode on Microsoft Edge uses the integrated Chromium engine for modern sites, and it uses the Trident MSHTML engine from Internet Explorer 11 (IE11) for legacy sites. So if you have a page that has yet to be upgraded to format or function with a newer browser such as Edge, Chrome, Firefox, etc, this will be a way that you can use the pages necessary while Microsoft continues to phase out Internet Explorer.

When a site loads in IE mode, the IE logo indicator displays on the left side of navigation bar. You can click the IE logo indicator to display additional information, as shown:

![IE logo indicator](https://learn.microsoft.com/en-us/deployedge/media/ie-mode/ie-logo-indicator1.png)

### IE mode supports the following Internet Explorer functionality

- All document modes and enterprise modes
- ActiveX controls (such as Java or Silverlight). **Note**: Silverlight reaches [end of support](https://support.microsoft.com/windows/silverlight-end-of-support-0a3be3c7-bead-e203-2dfd-74f0a64f1788) on October 12, 2021.
- Browser Helper Objects
- Internet Explorer settings and group policies that affect security zone settings and Protected Mode
- F12 developer tools for IE, when launched with [IEChooser](https://learn.microsoft.com/en-us/deployedge/edge-ie-mode-faq#how-can-i-debug-my-legacy-application-while-using-ie-mode-on-microsoft-edge-)
- Microsoft Edge extensions (Extensions that interact with the IE page content directly are not supported.)

### IE mode doesn't support the following Internet Explorer functionality

- Internet Explorer toolbars
- Internet Explorer settings and group policies that control the navigation menu.
- IE11 or Microsoft Edge F12 developer tools

## How to enable IE Mode?

- Open Microsoft Edge on Windows 10.

- Click the Settings and More (ellipsis) button on the top-right corner.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942752/Untitled.png?api=v2)

- Select the Settings option.

- Click on Default browser.

- Under the “Internet Explorer compatibility” section, turn on the “Allow sites to be reloaded in Internet Explorer mode” toggle switch.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942752/Screenshot%202022-12-14%20124322.png?api=v2)

- Click the Restart button.

Congratulations, you have now enabled IE mode for Microsoft Edge!
