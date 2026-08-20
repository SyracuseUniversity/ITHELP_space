---
title: "Mac Device Tunnel"
confluence_id: "159942330"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942330/Mac+Device+Tunnel"
version: 27
last_modified: "2025-10-16T13:10:18.866Z"
status: "current"
parent_id: "159942121"
labels:
  - "vpn"
  - "macos"
  - "openvpn"
---

The article below outlines installation and set up instructions for accessing network resources remotely from University owned and Jamf managed macOS computers.

---

**Computers not managed by the University**

If you have a computer that is not University owned and managed (Jamf), please see our [Remote Access](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942121/Remote+Access) page for alternative secure connection methods.

---

### Install OpenVPN Connect

OpenVPN Connect is an add-on program to allow VPN support on University owned and Jamf managed macOS computers.

1. Launch **Self Service** and log in as needed
2. Under the section "SU Management" find "Mac Device Tunnel" and choose to install

   If you do not see "Mac Device Tunnel" listed in Self Service, please reach out to your [academic](https://its.syr.edu/contact_its/school-and-college-support-contact-information/) or [administrative](https://its.syr.edu/contact_its/departmental-support-contact-information/) support personnel.
3. When the installer has finished, an OpenVPN icon will be added to your menu bar (located at the top of the screen):

   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942330/Screen%20Shot%202021-12-16%20at%201.57.16%20PM.png?api=v2)
4. Click on the OpenVPN icon and choose "Connect":

   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942330/Screen%20Shot%202021-12-16%20at%201.57.33%20PM.png?api=v2)
5. The icon changes appearance when it is connected:

   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942330/Screen%20Shot%202021-12-16%20at%202.11.33%20PM.png?api=v2)

---

### Expected Behavior:

- Manually connecting to VPN should only be required after installation the first time.
- VPN should reconnect after a restart or log out and log in.
- Connectivity should be similar to your on campus connectivity, whereas, you should be able to connect to on campus services without interruption.
- As always, your internet speed at your current location will depend on the quality of the connection.

OpenVPN will **not** connect while on you are connected to a wired campus network.

---

### Getting Help:

For support of the information above, staff and faculty should first contact their [academic](https://its.syr.edu/contact_its/school-and-college-support-contact-information/) or [administrative](https://its.syr.edu/contact_its/departmental-support-contact-information/) support personnel.
