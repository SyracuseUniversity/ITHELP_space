---
title: "Multifactor Authentication (MFA)"
confluence_id: "159941112"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941112/Multifactor+Authentication+MFA"
version: 144
last_modified: "2026-10-09T15:57:57.506Z"
status: "current"
parent_id: "159940932"
labels:
  - "office365"
  - "mfa"
  - "twofactor"
  - "2fa"
  - "two-factor"
  - "multi-factor"
  - "mobileapp"
  - "multifactor"
---

## What is multifactor authentication?

Multifactor authentication (MFA) adds a second step when you sign in. After you enter your NetID and password, you verify your identity using something you have with you, like your phone or a security key. This prevents someone else from using your account even if they know your password.

MFA is required for all Syracuse University accounts.

## Sign-in methods

Syracuse University supports several ways to verify your identity. You need at least one set up on your account.

| Method | How it works | What you need |
| --- | --- | --- |
| **Microsoft Authenticator** (recommended) | A notification pops up on your device. You match a number and tap to approve. | Phone or tablet (iPhone, Android, or iPad) |
| **Passkey** (recommended) | Your device verifies you with Face ID, a fingerprint, your screen lock, or a PIN. Nothing to type. | Most modern phones, tablets, and computers, or a password manager that supports passkeys |
| **Security key** | You plug in or tap a small hardware key when prompted. | A FIDO2-compatible security key (such as a YubiKey) |
| **Authenticator app codes** | You enter a six-digit code from an authenticator app, such as Microsoft Authenticator, Authy, or Google Authenticator. | Phone or tablet with an authenticator app |

## Set up Microsoft Authenticator

Setup is easiest when you have both a computer and your phone in front of you. You will scan a QR code from your computer screen with your phone.

1. Download Microsoft Authenticator from the [App Store (iPhone/iPad)](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) or [Google Play (Android)](https://play.google.com/store/apps/details?id=com.azure.authenticator)
2. On your computer, go to [mfa.syr.edu](https://mfa.syr.edu) and sign in
3. Select **Add sign-in method**, then choose **Authenticator app**

   ![Add a sign-in method dialog listing six options Passkey in Microsoft Authenticator, Passkey, Microsoft Authenticator (highlighted), Hardware token, Alternate phone, and Office phone, with a link to learn more about each method](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/Screenshot%202026-09-30%20142454.png?api=v2)
4. Follow the on-screen steps. When asked to add an account in the app, choose **Work or School**

   ![Sign-in screen titled 'Set up your account in app,' showing a phone illustration and instructions to allow notifications, add an account, and select Work or school.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/2.png?api=v2)
5. Scan the QR code shown on your computer screen with the Authenticator app

   ![Sign-in screen titled 'Scan the QR code' showing a QR code to scan with the Microsoft Authenticator app to connect it to the user's account.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/3.png?api=v2)
6. Approve the test notification sent to your device. Once verified, you are all set.

   ![Sign-in screen confirming 'Authenticator Added' with the Microsoft Authenticator icon and a message that it is now the default sign-in method.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/4.png?api=v2)

Microsoft Authenticator also works on tablets, including iPads and Android tablets.

---

### How signing in works after setup

After you set up Authenticator, here is what happens when you sign in:

1. Enter your NetID and password as usual
2. A two-digit number appears on your sign-in screen

   !['Approve sign in request' screen displaying the number to enter in the Authenticator app.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/Screenshot%202026-09-30%20145353.png?api=v2)
3. Open the notification from Authenticator on your phone or tablet
4. Type the matching number into the app and tap **Approve**

   ![Authenticator app prompt asking, 'Are you trying to sign in' with the number entered.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941112/Image.jpg?api=v2)

This number matching step confirms the sign-in request actually came from you.

---

## Set up a passkey

A passkey lets you verify your identity with Face ID, a fingerprint, your screen lock, or a security key. There is no code to type.

You can save a passkey in a few places:

- **In a password manager,** such as Apple Passwords (iCloud Keychain) or Google Password Manager. The passkey syncs across your devices that use the same account.
- **On one device,** such as your laptop with Windows Hello. The passkey stays on that device.
- **In Microsoft Authenticator** on your phone or tablet.
- **On a security key,** such as a YubiKey.

To set one up:

1. Go to [mfa.syr.edu](https://mfa.syr.edu) and sign in
2. Select **Add sign-in method**
3. Choose the passkey option
4. Follow the prompts. Your device will ask where you want to save the passkey.

Passkeys aren't available for parent and guest accounts. If you have one of these accounts, use Microsoft Authenticator instead.

For more help, see [MFA Setup using iOS Keychain/Passwords app](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/360743269/MFA+Setup+using+iOS+Keychain+Passwords+app) or Microsoft's guide: [Register a passkey](https://support.microsoft.com/en-us/accounts-billing/security/create-save-passkey)

---

## Got a new phone?

If you replaced your phone and Authenticator is no longer working, see [New Phone and the Authenticator App Isn't Working?](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/299630762/New+Phone+and+the+Authenticator+App+Isn+t+Working) for steps to restore access.

To avoid this in the future, register a second sign-in method as a backup, like a passkey in your password manager or on your laptop. That way you can still sign in and set up Authenticator again on your new phone without calling the help desk.

---

## Traveling

Set up your sign-in method before you leave. Microsoft Authenticator can generate verification codes even without an internet or cell connection, so it works abroad.

[Syracuse Abroad](https://suabroad.syr.edu/) students should make sure their sign-in methods are working before departure.

If you have a situation that prevents you from using any of the methods listed on this page while traveling, contact the [ITS Service Center](https://its.syr.edu/its_service_center/) before your trip.

---

## Manage your sign-in methods

Add, change, or remove your verification methods at any time at [mfa.syr.edu](https://mfa.syr.edu).

To choose which method you're asked for first, see <https://answers.atlassian.syr.edu/wiki/spaces/CIS/pages/1462796327>.

---

## Getting help

- **ITS Service Center:** 315-443-2677 | [help@syr.edu](mailto:help@syr.edu) | [Location and hours](https://its.syr.edu/its_service_center/)
- **Faculty and staff:** Contact your [academic](https://its.syr.edu/contact_its/school-and-college-support-contact-information/) or [administrative](https://its.syr.edu/contact_its/departmental-support-contact-information/) support team for hands-on help
