---
title: "MFA Setup using iOS Keychain/Passwords app"
confluence_id: "360743269"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/360743269/MFA+Setup+using+iOS+Keychain+Passwords+app"
version: 1
last_modified: "2025-05-02T13:52:51.503Z"
status: "current"
parent_id: "159941112"
---

Apple Keychain (available in Safari on iOS 15+ and macOS 10.15+)

If you had an MFA reset it should prompt you to set up a new method on login otherwise you can go to [mfa.syr.edu](https://mfa.syr.edu) and use the “add sign-in method” option on that page.

![add method.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/add%20method.PNG?api=v2)

It should then present you with the type of method you would like to add. Choose Microsoft Authenticator even though that is not the authentication app we will be using.

![choose authenticator.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/choose%20authenticator.PNG?api=v2)

It will then instruct you to install the app. On this dialog there is an option for “I want to use a different authenticator app” that you will need to click.

![start_by_getting_the_app.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/start_by_getting_the_app.PNG?api=v2)

It will then give an option to set up your account. You would proceed by clicking the “Next” button.

![copy_and_paste.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/copy_and_paste.PNG?api=v2)

It should now present you with a dialog that displays the secret key needed to set up the verification code. If you touch the icon bellow the secret key it will copy it to the clipboard.

![password_app.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/password_app.PNG?api=v2)

If you have a login saved already in your keychain or passwords app for the Microsoft login you would need to go into either the app or the Passwords portion in Settings and search for the correct Microsoft login.

![edit login.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/edit%20login.PNG?api=v2)

You would need to choose to edit the saved password with the “Edit” button in the top right.

![set_up_code.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/set_up_code.PNG?api=v2)

When editing the saved login choose the “Set Up Code” option.

![paste key.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/paste%20key.PNG?api=v2)

In the dialog that pops up paste in the secret key that had been copied and confirm with “Use Setup Key” After that is done you can save the edit you made to the login.

![enter code.PNG](https://answers.atlassian.syr.edu/wiki/download/attachments/360743269/enter%20code.PNG?api=v2)

If you go back to the browser and if you choose next it should ask for the verification code. You should be able to autofill the code as you would with a saved password. Once you hit next is should show up in the list of methods for authentication. If you use iCloud for passwords it will also sync across your Apple devices. If you have the Microsoft Authenticator app setup it will default to that method when logging in and you would need to choose the “cannot use the Microsoft Authenticator” option and then it will give you an option to use a verification code instead.
