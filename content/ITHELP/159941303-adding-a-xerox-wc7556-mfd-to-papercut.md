---
title: "Adding a Xerox WC7556 (MFD) to PaperCut"
confluence_id: "159941303"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut"
version: 13
last_modified: "2018-04-16T13:44:20.000Z"
status: "current"
parent_id: "159941357"
---

The following page provides steps to adding a Xerox WC7556 to the currently existing PaperCut environment. 

- [First Steps and Recommendations](#AddingaXeroxWC7556(MFD)toPaperCut-FirstStepsandRecommendations)
  - [Request the Device License](#AddingaXeroxWC7556(MFD)toPaperCut-RequesttheDeviceLicense)
  - [Security Configuration](#AddingaXeroxWC7556(MFD)toPaperCut-SecurityConfiguration)
  - [Machine Configuration](#AddingaXeroxWC7556(MFD)toPaperCut-MachineConfiguration)
  - [PaperCut Admins](#AddingaXeroxWC7556(MFD)toPaperCut-PaperCutAdmins)
  - [Organizational Unit Required Information](#AddingaXeroxWC7556(MFD)toPaperCut-OrganizationalUnitRequiredInformation)
- [Configuring the Copier](#AddingaXeroxWC7556(MFD)toPaperCut-ConfiguringtheCopier)
- [Getting Help](#AddingaXeroxWC7556(MFD)toPaperCut-GettingHelp)

## First Steps and Recommendations

### Request the Device License

Please contact the PMTT to request the license for your device. To do so, send a detailed email to [pmtt@syr.edu](mailto:pmtt@syr.edu.) indicating the exact make and model of the device. Please also include contact information if additional information is required.

Request License Early If Possible

Note that MFD licenses are limited and contacting the PMTT is recommended during the consideration of the product. Last minute license requests may not be available and may result in delays to product use.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

### Security Configuration

Follow the Imaging Device Guideline (G0101) for securing the device located at: <https://answers.syr.edu/display/infosec011/SU+Information+Technology+Security+Standards+and+Procedures?preview=/54362577/54887652/ImagingDeviceGuidelines-G0101.pdf>

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

### Machine Configuration

Machine Software Version:  061.121.226.31400 (Newer than web download. Received from Usherwood and can post online.).

1. Open a Web Browser window and enter the WorkCentre’s URL, using the format <http://xxx.xxx.xxx.xxx>.
2. Select the ‘index’ link on the top right of the page then select ‘Upgrades’ (Will be prompted for admin login).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Index.JPG?api=v2)
3. Select enable and apply.
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Enable%20Upgrades.JPG?api=v2)
4. Go to Manual Upgrades
5. Select the Browse button and locate the WorkCentre\_7500-system-sw#xxxxxx#.DLM File.
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Manual%20Upgrade.JPG?api=v2)
6. Select the “Install Software option. A pop-up will be shown saying ‘File has been submitted’, click OK. The machine will soon go into upgrade mode.

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

### **PaperCut Admins**

The PaperCut Admins will need to perform a couple steps to get your device ready. PaperCut Admins follow the instructions found [here](https://su-jsm.atlassian.net/wiki/x/mIKICQ). Contact the Print Management Technical Team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu). Include that you are setting up a new MFD device and confirm that you have configured the device using the security guidelines. 

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

### Organizational Unit Required Information

The orangization requires the following to properly add the device:

1. Device name:  OU-Your name for the device-copier
2. Location or Department information
3. IP address of the device
4. Device’s administrator username
5. Device’s administrator password

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

## Configuring the Copier

1. Change Admin Password (Properties -> Security -> Admin Password).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Admin%20Password.JPG?api=v2)
2. We’ve seen the built in device administrator account password change and revert to 1111. We created a second local device administrator account for web access. Use the steps below to create another local administrator account if you wish. The known step that reverts the password is enabling FIPS 140-2 encryption on the device.
3. Add additional local device PaperCut administrator account (Ex. lib-papercut-devices admin) to use at the physical device (Properties -> Security -> Authentication -> User Permissions -> Authenticated Users -> Machine System Roles -> System Administrator -> Edit -> Add New User.

   Account Info Provided by PMTT

   The local account information for this step will be provided by the PMTT member assisting you with this process.

   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/User%20Permissions.JPG?api=v2)

   1. Put in User Name, Friendly Name, and Password.
      ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Add%20New%20User.JPG?api=v2)
   2. Give the account: Accounting Administrator and System Administrator Permissions.
4. Enable Secure HTTPS (Properties -> Connectivity -> Protocols -> HTTP -> Secure HTTPS) This will restart the web service.  
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/HTTPS.JPG?api=v2)
5. Change Certificate Key Length to 2048 (Properties -> Security -> Certificates -> Certificate Key Length).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Certificate%20Key%20Length.JPG?api=v2)
6. Create a New Default Xerox Device Certificate with a far expiration date. (Properties -> Security -> Certificates -> Security Certificates -> Create New Xerox Certificate).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Create%20New%20Cert.JPG?api=v2)
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Cert%20Fields.JPG?api=v2)
7. Set SNMP v1/v2c Properties the following: (Properties -> Connectivity -> Protocols -> SNMP).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/SNMP-1.JPG?api=v2)
   1. GET Community Name: public (susnmp once we make PaperCut change).
   2. SET Community Name: To your own private name.
      ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/SNMP-2.JPG?api=v2)
8. Turn off Services you will not need on device (Properties -> Services -> Service Registration) – also removes from interface.
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Services.JPG?api=v2)
9. Turn on Accounting Method and set to Network Accounting (Properties -> Accounting -> Setup -> Current Accounting Method -> Network Accounting).
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Accounting-1.JPG?api=v2)
   ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Accounting-2.JPG?api=v2)
10. Set Authentication Method on the machine’s touch interface to Xerox Secure Access Unified ID System (Properties -> Security -> Authentication -> Setup -> Authentication method on the machine’s touch interface (Touch UI) -> Edit -> Xerox Secure Access Unified ID System).
    ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Authentication%20method-1.JPG?api=v2)
    ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Authentication%20method-2.JPG?api=v2)
    1. Configure Xerox Secure Access Setup with the following: (Click on the edit button below for Xerox Secure Access Setup -> Manually Override Settings or Manually Configure).
       ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Authentication%20method-3.JPG?api=v2)
       1. Device Log In Methods = Xerox Secure Access Device + alternate on-screen authentication method.
       2. Accounting Information = Automatically apply Accounting Codes from the server.
          ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Manual%20Override.JPG?api=v2)
    2. Setup Tools and Feature Access through the Custom Access option: Each copier could be different.
       1. Services Pathway needs to be unlocked to change individual services settings.
       2. Change the individual services to locked or unlocked depending your needs.
          ![](https://answers.atlassian.syr.edu/wiki/download/attachments/159941303/Tools%20and%20Features.JPG?api=v2)

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)

## Getting Help

 If you have general questions or are having technical difficulties with SU's printing management system, contact the Print Management Technical Team by emailing [pmtt@syr.edu](mailto:pmtt@syr.edu).

[Return to Top](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941303/Adding+a+Xerox+WC7556+MFD+to+PaperCut#AddingaXeroxWC7556(MFD)toPaperCut-top)
