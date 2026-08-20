---
title: "Setting Up MFA on macOS"
confluence_id: "353797131"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/353797131/Setting+Up+MFA+on+macOS"
version: 1
last_modified: "2025-04-11T01:34:21.870Z"
status: "current"
parent_id: "159941112"
---

## Apple Keychain/Passwords *(available in Safari on iOS 15+ and macOS 10.15+)*

If the user has already had their MFA reset it should prompt you to set up a new method on login otherwise you can go to [mfa.syr.edu](http://mfa.syr.edu) and use the “add sign-in method” option on that page.

![add signin method.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/add%20signin%20method.jpg?api=v2)

It will then present you with the type of method they would like to add. You should choose Microsoft Authenticator even though that is not the authentication app we will be using.

![choose sign in method.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/choose%20sign%20in%20method.jpg?api=v2)

It will then instruct you to install the app. On this dialog there is an option for “I want to use a different authenticator app” that you will need to click.

![authenticator app.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/authenticator%20app.jpg?api=v2)

It will then give you an option to set up their account. Click the next button.

![scan code.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/scan%20code.jpg?api=v2)

On the next dialog it will show you a QR code. If you right click on the QR code it will give you an option to “set up verification code”

![unlock passwords.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/unlock%20passwords.jpg?api=v2)

It will then prompt the user to unlock your Safari passwords.

![choose saved login.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/choose%20saved%20login.jpg?api=v2)

It will then ask you which saved password in keychain to use. You can search for your saved SU login, which may be a listed under a microsoft online domain. If you do not have one setup already for SU you will need to create a saved password using the “+” button next to the search field.

![verification code.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/verification%20code.jpg?api=v2)

It should then show the verification code generated for that domain. If you click on the code it should copy to your keyboard.

![enter code.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/enter%20code.jpg?api=v2)

You can then go back to the MFA prompt and if you hit “next” it will allow you to paste the code into that dialog. Hit next and it should then show you the new method in your list of authentication methods.

![method added.jpg](https://answers.atlassian.syr.edu/wiki/download/attachments/353797131/method%20added.jpg?api=v2)

You can now autofill your verification code in the same way Safari allows you to fill in your username and passwords. This will also sync across your Apple devices via iCloud.

While the initial setup requires the use of Safai macOS has an iCloud password extension available for most major browsers that will allow you to autofill the verification code using your Touch ID.
