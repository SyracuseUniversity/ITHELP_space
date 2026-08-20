---
title: "How to move your data to a new Mac using Migration Assistant"
confluence_id: "159940886"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159940886/How+to+move+your+data+to+a+new+Mac+using+Migration+Assistant"
version: 13
last_modified: "2020-03-04T15:28:09.000Z"
status: "current"
parent_id: "159941670"
labels:
  - "mac"
  - "migration"
  - "macos"
  - "osx"
  - "transfer"
  - "data"
  - "assistant"
  - "macbook"
---

Use Migration Assistant to copy all of your documents, apps, user accounts, and settings to a new Mac from another computer.

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-toc&locale=en_US&version=2)

# Summary

Migration Assistant copies all of your files to your new Mac so that you don't have to [copy your files manually](https://support.apple.com/kb/HT202910).

- If your files are currently on a Windows PC, follow the [PC migration steps](https://support.apple.com/kb/HT204087) instead.

# Check software, settings, and power

- [Install all available Apple software updates](https://support.apple.com/kb/HT201541) on both Mac computers. Install any updates for your third-party apps as well.
- Make sure that your old Mac has a computer name: Choose Apple () menu > System Preferences, then click Sharing and check the Computer Name field.
- Connect both computers to AC power.

# Connect the computers to each other

- If both computers are using macOS Sierra or later, just make sure that they're near each other and have Wi-Fi turned on, however, we suggest connecting the computers with a hardline connect to improve the speed of the data transfer.
- Or connect them [using target disk mode and the appropriate cable or adapter](https://support.apple.com/kb/HT201462). Then start up your old computer in target disk mode.
- Or connect your new Mac to a [Time Machine backup](https://support.apple.com/kb/HT201250) of your old Mac.

# Use Migration Assistant

On your new Mac:

1. Open Migration Assistant, which is in the Utilities folder of your Applications folder. Click Continue.
2. When asked how you want to transfer your information, select the option to transfer from a Mac, Time Machine backup, or startup disk. Click Continue.

![Migration Assistant Window](https://answers.atlassian.syr.edu/wiki/download/attachments/159940886/macos-high-sierra-migration-assistant.jpg?api=v2)

On your **old** Mac:
*If you started your old Mac in target disk mode or are migrating from a Time Machine backup, skip these four steps.*

1. Open Migration Assistant.
2. Click Continue.
3. When asked how you want to transfer your information, select the option to transfer to another Mac.
4. Click Continue.

On your **new** Mac:

1. When asked to select a Mac, Time Machine backup, or other startup disk, click the appropriate icon.
2. Click Continue. You might see a security code.

![Transfer Information to this Mac screen](https://answers.atlassian.syr.edu/wiki/download/attachments/159940886/image.png?api=v2)

On your **old** Mac:
*If you started your old Mac in target disk mode or are migrating from a Time Machine backup, skip these two steps.*

1. If you see a security code, make sure that it's the same code as on your new Mac.
2. Click Continue.

On your **new** Mac:

1. You should see a list of backups organized by date and time. Choose the backup that you want to use.
2. Click Continue.

![Transfer Information to this Mac screen](https://answers.atlassian.syr.edu/wiki/download/attachments/159940886/image.png?api=v2)

Continuing on your **new** Mac:

1. Select the information to transfer.
2. Click Continue to start the transfer. If you have a lot of content, the transfer might take several hours to finish.

![Transfer Information to this Mac screen](https://answers.atlassian.syr.edu/wiki/download/attachments/159940886/image.png?api=v2)

> In the example above, John Appleseed is a macOS user account. If you transfer an account that has the same name as an account on your new Mac, you're asked to rename the old account or replace the one on your new Mac. If you rename, the old account appears as a separate user on your new Mac, with a separate home folder and login. If you replace, the old account overwrites the account on your new Mac, including everything in its home folder.

After Migration Assistant is done, log in to the migrated account on your new Mac to see its files.

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-deck&locale=en_US&version=2)
