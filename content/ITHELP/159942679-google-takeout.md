---
title: "Google Takeout"
confluence_id: "159942679"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942679/Google+Takeout"
version: 18
last_modified: "2026-08-07T13:24:10.076Z"
status: "current"
parent_id: "159940652"
labels:
  - "migration"
  - "drive"
  - "gmail"
  - "transfer"
  - "google-workspace"
  - "google"
  - "photos"
  - "takeout"
  - "google-takeout"
---

**Table of Contents**

- [Overview](#GoogleTakeout-Overview)
- [Full Data Export](#GoogleTakeout-FullDataExport)
  - [Shared Drives](#GoogleTakeout-SharedDrives)
  - [Larger Export Files](#GoogleTakeout-LargerExportFiles)
- [Migrating Drive and Gmail Data to Personal Google Account](#GoogleTakeout-MigratingDriveandGmailDatatoPersonalGoogleAccount)
- [Migrating Photos Data to Personal Google Account](#GoogleTakeout-MigratingPhotosDatatoPersonalGoogleAccount)
  - [Step 1: Export Archive](#GoogleTakeout-Step1:ExportArchive)
  - [Step 2: Import](#GoogleTakeout-Step2:Import)

## Overview

---

The recommended option for migrating your data over to another Google Workspace account would be through Google's migration tool, Google Takeout. This process is recommended by Google. The tool is provided by Google and due to its intricacies is not supported by Syracuse University ITS.

## Full Data Export

---

### Shared Drives

Files in a Shared Drive **will not be included** in the export. To include files in a Shared Drive, place all desired files from a Shared Drive into My Drive.

1. Log into the account you want to transfer data **from**
2. Go to <https://takeout.google.com>
3. In *Step 1 Select Data to Export*, select all checkboxes
4. Select **Next Step**
5. In *Step 2 Choose Filetype, Frequency, and Destination*, set the *Delivery Method* to **Send Download Link via Email**
6. Set *Frequency* to **Export Once**
7. Leave *Filetype* and *File Size* as the default (.zip; 2 GB)

   ### Larger Export Files

   By default, the export may create multiple 2 GB .zip archive files depending on how much data exists in your account. If you are familiar with .tgz files, you may select that option to create archives that are larger in size but fewer in quantity.
8. Select **Export**
9. Download the export on the following page

## Migrating Drive and Gmail Data to Personal Google Account

---

Verify you are able to log into your g.syr.edu account before proceeding.

1. Log into the account you want to transfer data **from**
2. Go to <https://takeout.google.com/transfer>
3. In the destination account, enter the account the data is going **to**
4. Select **Send Code**. An email will be sent to the account receiving data.
5. In a new browser window, log into Gmail for the account **receiving** the data. In the email, select the **Get Confirmation Code** button.
6. Using the code provided, switch back to the Google Takeout Transfer page and enter the code in the *Step 2 Verify Destination Account* section.
7. In *Step 3 Select Content to Copy and Transfer,* verify that the from and to accounts are correct and that both Google Drive and Gmail are toggled on.
8. Start the transfer. It may take some time for all files to come over. The Google Drive data will come over under a new folder in the top-level Drive with the account and timestamp as the folder name.

   1. Ex. `netid@syr.edu 2022-07-22 13:45`

## Migrating Photos Data to Personal Google Account

---

### Step 1: Export Archive

1. Log into the account you want to transfer data **from**
2. Go to <https://takeout.google.com>
3. In *Step 1 Select Data to Export*, unselect all checkboxes and only select **Photos**
4. Select **Next Step**
5. In *Step 2 Choose Filetype, Frequency, and Destination*, set the *Delivery Method* to **Send Download Link via Email**
6. Set *Frequency* to **Export Once**
7. Leave *Filetype* and *File Size* as the default (.zip; 2 GB)
8. Select **Export**
9. Download the export on the following page

### Step 2: Import

1. Log into the Google account you want to import the Photos into
2. Go to <https://photos.google.com>
3. On your computer, locate and extract the .zip archive from the previous step

   1. .zip file should begin with "takeout"
4. In the extracted folder, go to **takeout[...]** > **Takeout**
5. Drag and drop the Google Photos folder from your computer (in the Takeout folder) to your browser with Google Photos open 

   ![Google photos folder with an arrow pointing it to photos.google.com](https://answers.atlassian.syr.edu/wiki/download/attachments/159942679/Screen%20Shot%202022-07-20%20at%202.26.32%20PM.png?api=v2)
