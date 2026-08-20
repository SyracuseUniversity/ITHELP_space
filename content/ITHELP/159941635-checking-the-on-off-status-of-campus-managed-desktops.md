---
title: "Checking the On/Off Status of Campus Managed Desktops"
confluence_id: "159941635"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941635/Checking+the+On+Off+Status+of+Campus+Managed+Desktops"
version: 18
last_modified: "2020-06-03T18:36:05.000Z"
status: "current"
parent_id: "159942121"
labels:
  - "remote"
  - "status"
  - "on"
  - "power"
  - "turned"
  - "powered"
---

The following page provides faculty and staff with instructions to determine if a campus managed desktop is on or off, a key requirement in making the machine reachable for a remote connection. This IS NOT used to ping remote lab or virtual desktops.

Remote Access Required

Users must have or acquire remote access to a campus managed desktop prior to remote connection.To request access remotely to your on-campus desktop, configure your work desktop, or to report an issue related to connecting to your work computer, please contact your [academic](https://its.syr.edu/contact_its/school-and-college-support-contact-information/) or [administrative](https://its.syr.edu/contact_its/departmental-support-contact-information/) support personnel.

Users will need to know the remote computer name or IP address.  This information was likely provided by your distributed or department support personnel and should look like the following examples.

Computer Name → uc-joldrxa-15.ad.syr.edu

Computer IP address → 128.230.xxx.xxx

Additional information about remote access, including VPN configuration and remote desktop solutions, is available on the [Remote Access home page](https://su-jsm.atlassian.net/wiki/x/6YWICQ).

---

**Instructions by Operating System**

This would be the operating system you are using to ping the remote desktop, not the campus desktop itself.

**- [Windows](#CheckingtheOn/OffStatusofCampusManagedDesktops-Windows)
- [macOS](#CheckingtheOn/OffStatusofCampusManagedDesktops-macOS)**

---

## Windows

1. Highlight "Start" in the Windows menu bar and then type "command" into the "Type here to search" field and then double click "Command Prompt" listed under Programs.
2. Type "ping [x]" (without quotation marks) into Command Prompt.   Replace "[x]" with the IP address or host name of the target computer.
3. Press "Enter" to ping the remote computer.

Positive and negative response examples are below. Positive responses will look similar to the following with a different Reply from and values:  "Reply from 127.0.0.1: bytes=32 time<1ms TTL=128".  Negative response will return "Request timed out.". Example images are below.

### Positive Response Example

Note that the computer should respond to a remote request.

![Sample Ping results window](https://answers.atlassian.syr.edu/wiki/download/attachments/159941635/good%20ping.png?api=v2)

### *Negative Response Example*

*Note that the computer is not available to respond to a remote request.*

![Sample Ping results window](https://answers.atlassian.syr.edu/wiki/download/attachments/159941635/bad%20ping.png?api=v2)

---

## macOS

1. In the Finder type "Terminal" and then double click the Terminal app in the left column.
2. Type ping -c <*number of times to ping*> <*IP address*>. The IP address is *xxx.xxx.xxx.xxx*, where *xxx* is a number between 0 and 255. For example, to ping 192.168.1.1 five times, you would type ping -c 5 192.168.1.1.

**Note:** If you do not enter the number of times that you want to ping the IP address, your system will continuously ping the address until you manually stop it. To stop pinging the IP address, press Control + C.

If the ping is successful, you should receive replies from the address that you are trying to ping.  If the ping is unsuccessful, you need to diagnose your network setup further.

### Positive Response Example

Note that the computer should respond to a remote request.

*![Sample Ping results window](https://answers.atlassian.syr.edu/wiki/download/attachments/159941635/OSX%20Ping%20Success.png?api=v2)*

### Negative Response Example

*Note that the computer is not available to respond to a remote request.*

*![Sample Ping results window](https://answers.atlassian.syr.edu/wiki/download/attachments/159941635/OSX%20Ping%20Fail%20edited.png?api=v2)*

*![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=toplink&locale=en_US&version=2)*
