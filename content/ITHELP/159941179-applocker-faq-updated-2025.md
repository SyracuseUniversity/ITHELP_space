---
title: "Applocker FAQ (Updated 2025)"
confluence_id: "159941179"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941179/Applocker+FAQ+Updated+2025"
version: 7
last_modified: "2025-11-20T14:03:14.639Z"
status: "current"
parent_id: "159941608"
labels:
  - "security"
  - "applocker"
---

**Q: Why am I seeing this AppLocker message?**

A: The app you're trying to open is running from a location that AppLocker does not trust on SU-managed Windows computers.

**Q: How do I get my application to run?**

A: : Move the application (or its entire folder) into a folder named Apps-SU. Once the app is inside Apps-SU, it should run normally.

**Valid locations for an "Apps-SU" folder:**

- On your Desktop
- In your Documents
- At the root of your Syracuse University OneDrive
- At the root of a thumb drive
- At C:/Apps-SU

**Q: I’m working with Twinmotion exports; what should I do?**

A: Twinmotion exports a folder called Presentation\_[ProjectName]. To run the included files without being blocked, move the entire exported Presentation folder into your Apps-SU folder.

**Q: What if I’m still blocked or need more help?**

A: Contact your department’s IT support group for assistance: <https://its.syr.edu/contact_its/departmental-support-contact-information/> or <https://its.syr.edu/contact_its/school-and-college-support-contact-information/>.

**Q: What if I installed software using an EDA account?**

A: When installing software as an EDA user, choose C:\Program Files if prompted. This ensures the software runs correctly for standard users.
