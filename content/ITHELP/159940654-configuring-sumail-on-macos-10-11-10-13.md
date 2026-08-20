---
title: "Configuring SUMail on macOS 10.11 - 10.13"
confluence_id: "159940654"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159940654/Configuring+SUMail+on+macOS+10.11+-+10.13"
version: 11
last_modified: "2021-01-22T18:27:30.000Z"
status: "current"
parent_id: "159941405"
labels:
  - "sumail"
  - "mail"
  - "apple"
  - "yosemite"
  - "openreview2014"
  - "revwmay12"
  - "acreview2014"
  - "mavericks"
---

Not the Latest Version

Please note that these instructions are for users of macOS 10.11 - 10.13, which is not the latest version of macOS.

Instructions for the latest macOS version can be found on the [Configuring SUMail on macOS (Apple Mail) page](https://su-jsm.atlassian.net/wiki/x/HYOICQ).

Preparing Exchange for SUMail

If you received an email indicating you need to configure your Exchange account in preparation for migration to SUMail, we recommend simply removing your account from the device and reconfiguring the account using the steps below. Configuring your email account with your full email address will properly prepare you for your account's migration. On macOS specifically, you may be required to perform this task AFTER your account is migrated. More migration details are available on the [Exchange Email Migration to SUMail page](https://su-jsm.atlassian.net/wiki/x/yYaICQ).

- [Apple Mail after Microsoft's MFA (Two-Factor Authentication or 2FA)](#ConfiguringSUMailonmacOS10.11-10.13-AppleMailafterMicrosoft'sMFA(Two-FactorAuthenticationor2FA))
- [Getting to Mail Setup](#ConfiguringSUMailonmacOS10.11-10.13-GettingtoMailSetup)
- [Setting up Mail](#ConfiguringSUMailonmacOS10.11-10.13-SettingupMail)

# Apple Mail after Microsoft's MFA (Two-Factor Authentication or 2FA)

As of March 2019, Syracuse University Mail (SUMail) requires Microsoft MFA (also known as two-factor authentication or 2FA). All versions of MacOS before 10.14 Mojave do not support what is referred to as "modern authentication". When trying to access older versions of Mail, you may continually asked to log in without success. You may see the following screen asking for internal and external URLs as well as a statement that Apple Mail cannot verify the account name or password:

![Apple Mail inbox add account screen error](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/Screen%20Shot%202019-03-05%20at%204.03.51%20PM.png?api=v2)

In order to continue to use Apple's Mail app, you will need to update MacOS to the latest version, 10.14 Mojave, which is freely available in the Mac App store. You must also remove and then re-add your SUMail account in order to Apple's Mail app to recognize the MFA/2FA. Follow the instructions listed under the "Related Articles" section for more information.

Additional work arounds include installing Microsoft office using your provided Office365 subscription, and use Outlook. You could also use Outlook's web based email on your preferred browser

---

# Getting to Mail Setup

1. Start Apple Mail (is located in the dock by default).

   First Account in Mail?

   If you do not have an account already in mail you can skip down to Setting up Mail
2. Go to Apple Mail's Preferences. Click the Accounts tab at the top.
   ![mail preferences menu](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/2p.png?api=v2)
3. To add a new account click the small + button under Accounts.
   ![click the plus button for adding an account](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/Add%20accounts.png?api=v2)

# Setting up Mail

1. It will prompt you to choose a mail account to add. Select Exchange and hit continue.

   ![select the exchange type of account](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/SUMail%20-%20AMail%201.png?api=v2)
2. Enter your full email address (netid@syr.edu) and associated account password and click Sign In.

   ![enter your su account credential in the email and password locations](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/SUMail%20-%20AMail%202.png?api=v2)
3. Upon entering a correct email address and the correct server, this should be your next screen.

   ![verify account configuration](https://answers.atlassian.syr.edu/wiki/download/attachments/159940654/SUMail%20-%20AMail%203.png?api=v2)
4. Choose the things that you would like mail to sync with then click done.  SUMail will load into Apple Mail.
