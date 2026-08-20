---
title: "Accessibility Guide for Qualtrics Survey Creators"
confluence_id: "159942482"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942482/Accessibility+Guide+for+Qualtrics+Survey+Creators"
version: 9
last_modified: "2022-02-18T20:12:18.000Z"
status: "current"
parent_id: "159941401"
---

## General Guidelines

[Accessibility Checklist for Forms](https://answers.atlassian.syr.edu/wiki/download/attachments/159941401/Form%20Accessibility%20Checklist.docx?version=2&modificationDate=1638541750000&cacheVersion=1&api=v2) (.docx)

## Qualtrics Specific Tips

### Qualtrics Accessibility Checker

1. The Check Survey Accessibility Tool is not a reliable indicator of the overall accessibility of your survey.
2. Always review your survey against the [Accessibility Checklist for Forms](https://answers.atlassian.syr.edu/wiki/download/attachments/159941401/Form%20Accessibility%20Checklist.docx?version=2&modificationDate=1638541750000&cacheVersion=1&api=v2) (.docx) and conduct your own tests. The best way to reveal accessibility issues is by completing the survey with only your keyboard and by completing the survey while using a screen reader. See the following pages for tips on testing with your keyboard and with three popular screen readers:
   1. [Keyboard Navigation for Web Accessibility Testing.docx](#)
   2. [JAWS Basics for Web Accessibility Testers](https://su-jsm.atlassian.net/wiki/display/itsservapp011/JAWS+Basics+for+Web+Accessibility+Testers)
   3. [NVDA Basics for Web Accessibility Testers](https://su-jsm.atlassian.net/wiki/display/itsservapp011/NVDA+Basics+for+Web+Accessibility+Testers)
   4. [VoiceOver Basics for Web Accessibility Testers](https://su-jsm.atlassian.net/wiki/display/itsservapp011/VoiceOver+Basics+for+Web+Accessibility+Testers)

### Themes

1. Currently the Syracuse Simple/Classic theme is the theme with the fewest accessibility issues. Flat and Modern themes should be avoided.
2. Themes are currently undergoing revisions, so watch for updates.
3. School/College themes have not been evaluated.

### Title

1. Add a survey title in **Survey Options  > Display Name** so that the survey title appears in the browser tab.

### Buttons and Graphical Content

1. Add alternative text to the Syracuse University logo by inserting the following string to the source code of the **Look & Feel > General > Footer:**<script>document.querySelector ('#Logo > img').alt = "Syracuse University"</script>
2. Add alternative text to all images using **Graphics Library > Edit Image > Description.**
3. Navigation buttons must include text that describes the function of the button (Begin Form, Previous, Next, Submit, etc.). Add text to buttons using **Edit Block > Format > Next/Previous Button Text**

### Question Numbering

1. The progress bar in Qualtrics is not accessible, so you must select **Survey Options > Enable Question Numbers** for surveys of more than one page. If using randomization this will likely pose a question numbering issue. Survey developers might consider consulting the [Qualtrics XM Community](https://community.qualtrics.com/XMcommunity/) for possible custom Javascript solutions that are outside the scope of this guide.
2. It is also considered best practice to indicate the number of questions in the survey introduction (if possible).
3. Turn off question numbering for the Text/Graphic question type which does not require user interaction by inserting the Javascript string: **jQuery("#"+this.questionId+" .ExportTag").hide();**into the addOnReady section of the **Edit Question JavaScript box.**
4. If questions are added or skipped using logic you must alert the user. For example, "Answering yes to this question will reveal two additional follow-up questions." or "If answering no skip to question 14."

### Survey Content

1. Be sure to add the survey title as a Header 1 to the first page of the survey using the Text/Graphic question type.
2. Indicate in the survey instructions how many questions (approximate is fine if logic is used) and how long it should take the user to complete.
3. Textual content over one sentence in length must be left-aligned (not fully justified) and have adequate line and paragraph spacing.
4. Instructions must not rely on shape, size, or visual location (Ex. Answer the questions below or Click the orange button for example).
5. Any links that are included in the survey must be plain text links (Ex. [Syracuse University](https://syracuse.edu) instead of <https://syracuse.edu>)
6. If color is used in any textual content it must adhere to minimum contrast guidelines (no less than 4.5:1 for standard text, no less than 3:1 for large text/headings)
7. When a screen reader user navigates your survey the textual content between questions is often skipped. Therfore, any instructional text that precedes the survey or that is inserted between questions using the Text/Graphic question type must include the appropriate heading (Heading 2, Heading 3, etc.) for navigation purposes. Use the **Rich Content Editor** to format the text.

### Required Fields and Field Validation

1. Qualtrics error handling is not sufficient to meet WCAG Level A and AA compliance, making it difficult or impossible for users of assistive technology to locate and correct errors. Therefore, the use of required questions and field validation should be avoided if possible or kept to an absolute minimum.
2. **Required fields** must include the word (Required) in the text of the question, usually at the end. It can be in red if desired.
3. For any field that uses **Field Validation** (phone number formats, email formats, date formats, etc.), the expected format must be included as part of the question. Ex. Start Date (MM-DD-YYYY)

## Accessible Question Types

### The following question types are WCAG compliant (**Simple/Classic Theme** only)

- Constant Sum (text entry format only)
- Drill Down
- Multiple Choice (Single Answer Radio Button and Multiple Answer Checkbox)
- Net Promoter (keep the number of values low due to issues with mobile viewport scaling)
- Text Input

### The following question types should be avoided:

- Captcha Verification (Mobile version forces user to full Captcha rather than checkbox)
- Constant Sum (Bars and Sliders)
- File Upload
- Graphic slider
- Heat Map
- Highlight
- Hot Spot
- Matrix: Likert
- Matrix: Bipolar
- Matrix: Maxdiff
- Multiple Choice: Multi-Select Drop-Down Box
- Rank Order
- Side-by-Side (Likert/Scaled Response option)
- Signature
