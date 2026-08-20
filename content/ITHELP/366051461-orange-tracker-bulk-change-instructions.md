---
title: "Orange Tracker Bulk Change Instructions"
confluence_id: "366051461"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/366051461/Orange+Tracker+Bulk+Change+Instructions"
version: 3
last_modified: "2025-05-01T02:34:34.723Z"
status: "current"
parent_id: "159941388"
labels:
  - "admin"
---

Use the following steps to perform a bulk update (e.g., move issues between projects and modify customer request types). Please note: OT allows bulk changes for up to **1,000 issues at a time**.

---

#### **Step 1: Filter the Relevant Issues**

1. Navigate to **Filters**
2. Use JQL or the basic search to locate the tickets you want to update. A sample JQL query might look like:

```
project = [ProjectKey] AND "Customer Request Type" = [RequestType]
```

3. Add any additional filters as needed (e.g., status, assignee, component).
4. Once your search results are accurate, click the **“...” menu (More)** in the top-right corner and select **Bulk change work items**.

---

#### **Step 2: Select Issues**

1. On the **Choose Issues** screen:

   - Check the box next to each issue you want to update.
   - To select all on the page (up to 1,000 issues), use the checkbox at the top-left of the issue list.
2. Scroll to the bottom of the page and click **Next**.

---

#### **Step 3: Choose Bulk Action**

1. From the list of available bulk operations, select **Move Issues**.
2. Click **Next**.

---

#### **Step 4: Set Destination Project and Fields**

1. **Choose the destination project** from the dropdown.
2. Click **Next**.

On the next screens:

- Match or set values for required fields in the destination project (e.g., **Components**, **Issue Type**, **Priority**, etc.).
- For the **Customer Request Type** field:

  - Select the appropriate request type that matches your initial filter (e.g., “Email”).
  - If the matching request type does not exist in the target project, you may need to create it or consult with a Jira admin.

Click **Next** after completing each field-mapping screen.

---

#### **Step 5: Review and Confirm**

1. Review the changes summary to ensure all field mappings and issue selections are correct.
2. Click **Confirm** to execute the bulk move.

---

### ⚠️ Important Notes

- You must have **Bulk Change** and **Move Issues** permissions for both the source and destination projects.
- Always **test with a small batch** before making large-scale changes.
