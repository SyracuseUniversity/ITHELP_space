---
title: "Migrating Google Drive to OneDrive"
confluence_id: "159941540"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941540/Migrating+Google+Drive+to+OneDrive"
version: 7
last_modified: "2024-01-05T17:21:20.000Z"
status: "current"
parent_id: "159940652"
---

### Option 1. Copy your Google Drive files to OneDrive manually

This option involves downloading the files to your hard drive and uploading them to OneDrive.

Here's how you can do it:

1. Download the files from Google Drive to your computer. You can do that either by selecting them and clicking the "Download" button or by using Google Takeout.

   If you decide to use Google Takeout, please note that it will **not**download files and folders that are **shared with you.**To save the documents that other people have shared with you, select and download them manually from the "Shared with me" section of your Drive.

   ![Menu for downloading 'Shared with me' items in Google Drive manually](https://www.vaultme.com/assets/images/articles/transfer-drive-onedrive/download-shared-with-me%E2%80%93items-from-google-drive.jpg)

   How to download "Shared with me" items manually

2.  Upload the files to your OneDrive.

![Step 2 of manual migration to OneDrive. The menu for the upload from the hard drive](https://www.vaultme.com/assets/images/articles/transfer-drive-onedrive/manual-upload-to-onedrive.png)

             How to upload files to OneDrive

The obvious drawback of this method is that you have to handle your owned and shared files separately.

Important things that you should also take into account before you begin:

- Depending on the size of your Google Drive account, the download and upload process may take up to several days or even weeks.
- You will need to have enough storage space on your hard drive for a copy of your Google Drive account.
- Your computer will have to stay powered on during the whole download and upload process. Any interruptions to the internet connection and power supply can cause the process to fail.
- When you download multiple files (either manually or using Google Takeout), Google puts them in archives. To recreate the structure of your Google Drive in OneDrive, you will have to unzip the archives on your computer and re-organize the files before you upload them to OneDrive.
- If you have a large account (over 10 GB) and decide to use Google Takeout, your archive will be split into several parts by default. Some of them may fail to generate properly and the archive will have to be requested again.

---

### Option 2. Export your Google Drive files to OneDrive directly using Google Takeout

Please note that this option is ONLY available when exporting to a personal OneDrive account. Unfortunately our @syr.edu accounts are not compatible with this method.

Using this option, you will be able to put **a zipped archive**of your Google Drive into OneDrive automatically.

Here’s how you export Google Drive files to OneDrive:

1. Go to Google Takeout.
2. Select "Drive" and click "Next step".
3. In the "Delivery method" drop-down menu select "Add to OneDrive".
4. Select the frequency ("Export once") and the export file type and size. Then click "Create export".

![Step 3 of Google Takeout export to OneDrive. The menu for selecting OneDrive](https://www.vaultme.com/assets/images/articles/transfer-drive-onedrive/google-takeout-export-to-onedrive.png)

           How to export Google Drive to OneDrive

Please consider the following when choosing this method:

- Google Takeout **will not transfer the files and folders that are shared with you**. To copy shared documents, select and download them manually from the "Shared with me" folder of your Drive. Then upload them to OneDrive.
- The migration process may take up to several days depending on the size of your export. Larger accounts (10+ GB) will be split into several archives by default.
- Google Takeout will export one or several archives instead of individual files and folders. To use your documents in OneDrive, you will first need to download, unzip and re-organize them.

---

### Option 3. Third-Party Application

There are a variety of third-party applications that a user can choose to complete the migration task, a few which have been outlined below. Please keep in mind none of these options are supported by Syracuse University or the Information Technology staff.

1. [SysTools G Drive to OneDrive migration Tool](https://www.systoolsgroup.com/google-drive/onedrive/) (recommended by Microsoft)
2. [VaultME](https://app.vaultme.com/#/setup/introduction)
3. [Shoviv Cloud Drive Migrator](https://www.shoviv.com/cloud-drive-migrator.html)
