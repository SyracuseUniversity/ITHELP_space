---
title: "Troubleshooting USB/Internal Camera and Audio In Zoom/Collaborate/Teams"
confluence_id: "159941844"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941844/Troubleshooting+USB+Internal+Camera+and+Audio+In+Zoom+Collaborate+Teams"
version: 5
last_modified: "2023-08-22T18:22:09.000Z"
status: "current"
parent_id: "159941641"
---

The following troubleshooting steps below can help to fix a non-working webcam, microphones or speakers/headphones. The steps are more general and not specific to any brand of webcam. Linked below are pages that deal with specific operating systems or hardware type.

---

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-toc&locale=en_US&version=2)

---

## General Solutions

1. **Plug/Unplug**(This section doesn't apply to integrated peripherals, e.g. a webcam built into the display.)
   1. Unplug the webcam from the computer, then plug it back into the computer. You may also want to try plugging the device into a different USB port than it was plugged into previously.
   2. If unplugging and re-plugging does not work, unplug the device again. Restart the computer with the device unplugged. After the computer has restarted and loaded back into the operating system, plug the device into a USB port.
   3. If the unplug and re-plug process did not work, continue to the next section.
2. **Restart App and Devices**
   1. Restart the app trying to access the  camera or mic, e.g. Zoom or Collaborate Ultra
   2. Restart the computer if you did not already do so in section 1
3. **Miscellaneous Troubleshooting**
   1. Clear cache and cookies if the camera is being accessed by a web browser (this is much more common in Collaborate than Zoom, since Zoom isn't usually run in a browser.) If you have accidentally hit "deny" when the app asked them for device permission this should solve the problem.
   2. Other apps may have control of the device. (Zoom, Collaborate, Skype, etc...) For example close all other apps that could be using the camera, exit and try again.
   3. Reboot the computer

---

## macOS Additional Solutions

1. Verify audio input/output by going to System Preferences > Sound > input/output. You will be able to verify that the correct device(s) are recognized and set as the default.
2. Run software updates, device drivers in macOS are packaged with  system updates so this will often resolve issue.
3. If necessary, download the driver or device software *directly from the manufacturer's website.*Downloads from third party sites can often be bundled with malware and represent a security risk.

## Apple Troubleshooting Pages

[If your built-in camera isn't working on your Mac](https://support.apple.com/en-us/HT211130)

[Control access to your microphone on Mac](https://support.apple.com/guide/mac-help/control-access-to-your-microphone-on-mac-mchla1b1e1fe/mac)

[About the audio ports on a Mac](https://support.apple.com/guide/mac-help/about-audio-ports-cpmh0052/10.15/mac/10.15)

[If you can't hear sound from your speakers](https://support.apple.com/guide/mac-help/if-you-cant-hear-sound-from-your-speakers-mchlp1439/mac)

---

## Windows 10 Additional Solutions

1. **Uninstall and reinstall  (**Follow the steps below to uninstall and reinstall the device on your computer if **Miscellaneous Troubleshooting**does not resolve)

1. 1. Uninstall any device related software on the computer.
   2. Open the Device Manager.
   3. Expand the Universal Serial Bus controllers section and look for the device in the device list. It should include the brand or model number of the webcam in the name of the device.
   4. Select the device in the list, then right-click on the device and select Uninstall device.
   5. Unplug the device from the computer.
   6. Restart the computer.
   7. After the operating system has loaded, plug the device into the computer again. The operating system should recognize the device and reinstall the drivers for it.
   8. Reinstall any additional software that came with the device.

For more information here is a link to Microsoft's page on [How to Update/Un-install/Re-install drivers](https://support.microsoft.com/en-us/help/4028443/windows-10-update-drivers).

2. **Known Lenovo issue**

1. 1. If camera displays, but shows the picture below  the computer has preinstalled software called Lenovo Vantage.  Open Lenovo Vantage and use settings to turn off this camera privacy feature:    The following link has more information.  <https://support.lenovo.com/us/en/solutions/ht500417>

![Lenovo Camera Image](https://answers.atlassian.syr.edu/wiki/download/attachments/159941844/Lenovo%20Camera.jpg?api=v2)

3.  **Windows Application Permissions**

MIcrosoft Windows controls how an application accesses hardware devices such as USB cameras, microphones and speakers.   In Windows 10, you can use the Privacy page to choose which apps can use a particular feature.   
***Select Start  > Settings  > Privacy***.   Select the app (for example, Calendar) and choose which app permissions are on or off.   

Here is a link to a Microsoft article about [Application Privacy settings](https://support.microsoft.com/en-us/help/10557/windows-10-app-permissions).

4.**Try an alternate computer**

If an alternate computer is available to test the device.

---

## Microsoft Troubleshooting Pages

[Camera doesn't work in Windows 10](https://support.microsoft.com/en-us/help/13753/windows-10-camera-does-not-work)

[Fix microphone problems in Windows 10](https://support.microsoft.com/en-sg/help/4034886/accessories-headset-troubleshooting-microphone-issues)

---

## Getting Help

For additional support on the information above, contact the  [ITS Help Desk](http://its.syr.edu/supportsvc)  by calling at 315.443.2677 or by emailing  [help@syr.edu](mailto:help@syr.edu).

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=toplink&locale=en_US&version=2)
