---
title: "Setup a Smartcard / YubiKey"
confluence_id: "155453564"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/155453564/Setup+a+Smartcard+YubiKey"
version: 94
last_modified: "2026-04-17T16:47:48.117Z"
status: "current"
parent_id: "159942121"
labels:
  - "security"
  - "adtt"
  - "smartcard"
---

### Prerequisites

---

#### **Smartcard Setup**

- If a YubiKey is being reused, ensure it has been factory reset and that the default PIN is set to `123456`.

**C- Account Request**

- The DSP (Department Support Personnel) for the department or unit must initiate the process by creating a ticket in the [One IT Systems & Services (SYSSVCS) OT project](https://support.atlassian.syr.edu/servicedesk/customer/portal/1222) with the c- account request.
- The email should include any necessary [SUPER permissions](https://answers.atlassian.syr.edu/wiki/x/FQRECQ) and the appropriate DAG number(s).

**Setup Appointment**

- Once the c- account is created, permissions are added, and the smartcard is provided to the end user, they should schedule a [Smartcard Setup appointment](https://outlook.office365.com/book/SmartcardSetup@bookings.syr.edu/) to have the required certificates installed on the YubiKey.

### Table of Contents

---

- [Steps for a New Smartcard Setup](#SetupaSmartcard/YubiKey-StepsforaNewSmartcardSetup)
- [Video Tutorial](#SetupaSmartcard/YubiKey-VideoTutorial)
- [YubiKey's for Non-ITS Staff, faculty, and/or vendors](#SetupaSmartcard/YubiKey-YubiKey'sforNon-ITSStaff,faculty,and/orvendors)
- [Setup and Reset Requests for Non-ITS users](#SetupaSmartcard/YubiKey-SetupandResetRequestsforNon-ITSusers)
- [Changing the PIN on the Smartcard](#SetupaSmartcard/YubiKey-ChangingthePINontheSmartcard)
- [Steps for Smartcard Renewal](#SetupaSmartcard/YubiKey-StepsforSmartcardRenewal)
- [Troubleshooting](#SetupaSmartcard/YubiKey-Troubleshooting)

It is important to keep your YubiKey or Smartcard secure and prevent unauthorized access. Do not share your PIN or allow anyone else to use your YubiKey or Smartcard. If you suspect that your YubiKey or Smartcard has been lost, stolen, or compromised in any way, contact IT support immediately.

Be aware that YubiKeys have a limit of **10 attempts** for entering a PIN before they automatically lock. If your YubiKey locks, it will need to be reset, reach out to your IT support personnel for assistance.

Once reset, [**Schedule a Smartcard Setup**](https://outlook.office365.com/owa/calendar/SmartcardSetup@bookings.syr.edu/bookings/) **appointment**.

---

## Steps for a New Smartcard Setup

---

**Using an AD-managed Windows computer:**

1. **Connect to the server:**

   - Use Remote Desktop Connection (RDP) to connect to `smartcard.syr.edu`.
2. **Log in:**

   - When prompted for logon, select "More choices" and choose "Use a different account."
   - Enter the username: `c-netid` (e.g., `c-testuser` or `AD\c-testuser`) and the password provided in the email from Smart Card Manager.
3. **Launch the Smartcard Setup:**

   - On the server's desktop, find the "Setup Smartcard" icon in the upper left and double-click it. A PowerShell window will launch, and the program will begin.
   - If not already inserted, ensure the YubiKey is plugged into a USB port on the computer.
4. **Monitor the process:**

   - The process is now underway and may take a few moments. If you're concerned that the process hasn't started, you can confirm it's running if the white cursor is blinking on a new line in the console.
5. **Enter the PIN:**

   - When prompted, enter the default PIN `123456`.
   - Shortly after, you'll be prompted to reenter the same PIN to add the root certificate, enhancing the versatility of your YubiKey.
6. **Exit the program:**

   - When the program states "press Enter to exit," you can sign out of the RDP session by following these steps:

     - Go to the Start Menu, click on the silhouette of a person located just above the Start Menu, and select the "Sign Out" option.
7. **Final steps:**

   - After completing the process, direct login to any server using only the username and password, as done in step 2, will no longer be possible. Instead, you will be required to utilize the Smartcard and its associated PIN.
   - You will need to establish a PIN that consists of exactly eight characters. This can be accomplished by accessing the Security Options Window on a Windows machine via "Ctrl + Alt + Delete."
   - Remove and reinsert the YubiKey in the USB port before trying to use it.
8. **Reboot if needed:**

   - If you just renewed your smartcard, you might need to reboot your system before the Kerberos protocol can utilize the smartcard subsystem.

## Video Tutorial

---

![](https://answers.atlassian.syr.edu/wiki/download/attachments/155453564/SetupYubikeyTutorial.mp4?api=v2)

Please note that the terms "Smartcard" and "YubiKey" are used interchangeably.

---

## YubiKey's for Non-ITS Staff, faculty, and/or vendors

---

- **Order or Receive the YubiKey:**

  - The IT unit responsible for managing the YubiKey should [order the device](https://answers.atlassian.syr.edu/wiki/spaces/CIS/pages/155452743/How+to+Acquire+a+Smartcard) or receive it directly from the user if they are providing their own.
- **Set Up the YubiKey:**

  - The IT unit can complete the YubiKey setup on behalf of the user by contacting `ADTT@syr.edu`.
- **Deliver the YubiKey:**

  - Once the setup is complete, the YubiKey can be given or mailed to the user, along with instructions on how to set the PIN.

## Setup and Reset Requests for Non-ITS users

---

### **If the Request is to Set Up a New Card:**

1. **Obtain the Physical Card:**

   - The DSP (Department Support Personnel) should have the physical card with them.
2. **Schedule a Setup Appointment:**

   - Use the following link to reserve a time with an ADTT team member: [Smartcard Setup on Bookings](https://outlook.office365.com/book/SmartcardSetup@bookings.syr.edu/)
3. **(Optional) Group Membership Configuration:**

   - After the account is created and the card is set up, the DSP can add the `c-` account to the necessary groups for the user.
4. **Deliver the Card to the User:**

   - Ensure that the card is delivered directly to the intended user. Please verify that the actual user receives the card and explain how to change the PIN using this guide: [Managing Your YubiKey/Smartcard PIN with Yubico Authenticator App](https://answers.atlassian.syr.edu/wiki/spaces/CIS/pages/155452700/Managing+Your+YubiKey+Smartcard+PIN+with+Yubico+Authenticator+App#Changing-Your-YubiKey-PIN)

---

### **If the Request is to Reset a Smartcard:**

1. **Collect the Card:**

   - The DSP should collect the card from the user.
2. **Reset the Card:**

   - Reset the card to university defaults using this guide: [Reset YubiKey / Smartcard To University Defaults](https://answers.atlassian.syr.edu/wiki/spaces/CIS/pages/155452700/Managing+Your+YubiKey+Smartcard+PIN+with+Yubico+Authenticator+App)
3. **Schedule a Reset Appointment**

   - Reserve a time with ADTT for assistance with resetting the card: [Smartcard Setup](https://outlook.office365.com/owa/calendar/SmartcardSetup@bookings.syr.edu/bookings/)
4. **Reset Process Assistance**

   - ADTT will assist in resetting the card following the steps outlined above.

---

---

## Changing the PIN on the Smartcard

---

If the YubiKey is still using the default PIN of `123456`, it must be changed before the end user can access Syracuse University resources.

**Recommended Method: Use Yubico Authenticator**

1. **Download the app**: Open the Microsoft Store and search for "Yubico Authenticator" (published by Yubico AB)
2. **Connect your YubiKey**: Insert the YubiKey into a USB port
3. **Launch the app**: The app should automatically detect your YubiKey
4. **Change the PIN**: Look for PIN management or settings options within the app to change from the default `123456` to your preferred 8-character PIN

**Alternative Method**: Windows 10 users can also change the PIN using the Security Options window (Ctrl + Alt + Delete), though the Yubico Authenticator app provides a more user-friendly experience.

**Important**: Your new PIN must be exactly 8 characters long and will be required each time you use the YubiKey to access Syracuse University resources.

---

---

## Steps for Smartcard Renewal

---

10 days prior to certificate expiration, an email will be sent to the mailbox of the C- account that requires renewal. After receiving the email, follow the steps below to renew your smartcard without ADTT assistance.

**Using an AD-managed Windows computer:**

1. **Connect to the Server**

   - Use Remote Desktop Connection (RDP) to connect to `smartcard.syr.edu`.
2. **Log On**

   - When prompted, use your current YubiKey and PIN to log onto the server.
3. **Launch the Smartcard Setup**

   - On the server's desktop, locate the "Setup Smartcard" icon in the upper left and double-click it. A PowerShell window will launch, and the program will begin.
   - If not already inserted, plug the YubiKey into a USB port on the computer.
4. **Monitor the Process**

   - The process is now underway and may take a few moments.
5. **Enter the PIN**

   - When prompted, enter your current PIN.
   - Shortly after, you will be prompted to reenter the same PIN to add the root certificate, enhancing the versatility of your YubiKey.
6. **Exit the Program**

   - When the program states "press Enter to exit," sign out of the RDP session by following these steps:

     - Go to the Start Menu, click on the silhouette of a person located just above the Start Menu, and select the "Sign Out" option.
7. **Post-Process**

   - After completing the process, direct login to any server using only the username and password, as done in step 2, will no longer be possible. Instead, you will be required to utilize the Smartcard and its associated PIN.
   - **If you are renewing your YubiKey, the PIN will remain unchanged.**
8. **Final Steps**

   - Remove and reinsert the YubiKey into the USB port before attempting to use it.
   - If you have just renewed your smartcard, you might need to reboot your system before the Kerberos protocol can utilize the smartcard subsystem.

---

---

## Troubleshooting

---

#### **General**

1. **YubiKey Insertion**

   - Ensure the YubiKey is properly inserted into the USB port. For USB-A style YubiKeys, it can be inserted in either orientation. When inserted correctly, the "y" on the card will flash green.
2. **YubiKey Touch Button**

   - The gold medallion on the YubiKey functions as a touch button. Pressing or touching it generates a One-Time Password (OTP) and simulates the Enter key press. Although this feature is not currently utilized, it may be used in the future.
3. **Access Denied Warning**

   - If you encounter an "Access Denied" warning while attempting to log into the server during step two, it is likely that your account has `SmartcardLogonRequired` set to `true`. In such cases, please contact your IT team for assistance.
4. **Delayed PIN Prompt**

   - If you are waiting for a PIN prompt for more than 20 seconds and it does not appear, click on the PowerShell window and press Enter twice. If the issue persists, please reach out to ITS for further support.

#### **Windows Specific**

1. **Smart Cards Setting**

   - Check the Smart Cards setting for a Yubico Minidriver under Device Manager on your computer. If the driver is not present and the computer is DOMAIN JOINED, restart the computer and check again. If the driver is still missing, contact ITS for assistance.
   - If the driver is not present and the computer is NOT DOMAIN JOINED, download the driver manually from Yubico's website: [Download Yubico Smart Card Drivers](https://www.yubico.com/products/services-software/download/smart-card-drivers-tools/). Go to <http://yubico.com> > Support > Downloads, find the CAB download for the Yubico mini-driver, extract it to a folder, right-click the `.inf` file, and select "Install." After the driver is installed, the computer may require a restart.
2. **Certificate Validation Error**

   - If you receive the error message "*The client has failed to validate the domain controller certificate for \_\_\_\_\_\_\_. The following error was returned from the certificate validation process: A certificate chain could not be built to a trusted root authority.*" on a non-DOMAIN JOINED computer, it may mean the computer does not trust the root certificate from AD. Contact [adtt@syr.edu](mailto:adtt@syr.edu) for assistance with trusting the certificate.

#### **macOS Specific**

1. **Network Level Authentication (NLA) Issues**

   - **Issue:** Apple computers may face issues using the smartcard after setup due to Network Level Authentication (NLA). When attempting to connect to RDP, macOS may require a username and password before allowing the smartcard to be utilized, which can prevent the smartcard from functioning properly.
   - **Workaround:** If you encounter this issue, one option is to use a Windows computer or virtual machine (VM) to connect via RDP. Once connected, you can use the Smartcard or YubiKey by selecting it from the "More Choices" option.
2. **RDP Version and Smartcard Recognition**

   - **Ensure Compatibility:** Make sure your Apple computer is running macOS and Microsoft Remote Desktop app Version 10 or later, as newer versions offer better support for smartcards.
   - **Smartcard Not Detected:**

     - If your smartcard is not being recognized during RDP connection setup, first ensure that the smartcard is being recognized by macOS itself. You can use the `pcsctest` tool available in the Terminal.app to verify smartcard detection.
     - If macOS recognizes the smartcard but the Microsoft Remote Desktop app does not, check the "Devices & Audio" or "Redirection" settings in the app to ensure that smartcard redirection is enabled. Reconnect to the session and try again.
3. **First-Time Configuration Issues**

   - **Smartcard Not Appearing:** If the Smartcard does not appear as an option when configuring it for the first time using the remote client application (assuming it is version 10+), it may indicate that the connection does not support Smartcards.

     - **Fix:** Exit the connection, right-click on it in the Microsoft Remote Desktop client application, select "Edit," navigate to the Devices tab, and ensure that "Smart Card" is checked. Reconnect to the session and try again.
     - **Driver Consideration:** Unlike Windows, macOS typically does not require additional drivers for most smartcards, including YubiKeys. However, keeping your system and Microsoft Remote Desktop app up-to-date is crucial for ensuring proper functionality.

If issues persist, consider reaching out to ITS for further support or explore additional troubleshooting based on your specific environment’s configurations.
