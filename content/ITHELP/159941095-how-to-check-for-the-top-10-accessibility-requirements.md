---
title: "How to Check for the Top 10 Accessibility Requirements"
confluence_id: "159941095"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941095/How+to+Check+for+the+Top+10+Accessibility+Requirements"
version: 17
last_modified: "2020-01-31T15:28:59.000Z"
status: "current"
parent_id: "159940839"
labels:
  - "wave"
---

# Skip to Content Link

1. Analyze the accessibility of your web page by entering the URL for your web page in the [WAVE Web Accessibility Tool](http://wave.webaim.org//).
2. On the left side of your screen, click the Styles selector so the slider moves to the left .

   ![WAVE tool Styles off and on toggle slider](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/image2020-1-30_14-52-48.png?api=v2)
3. On the right side of your screen, the display of your web page will change to one without styles (formatted like an outline). Check to see if there is a hyperlink that says “Skip to Content” or "Skip to main content."  It should be the first or second item listed at the top of the page.
4. If the hyperlink is there, open your web page in another tab. Is the Skip to Content link visible?
5. If not, using the Tab key, see if the Skip to Content link becomes visible as you Tab through the top of the page.  If so, select it by pressing Enter and make sure that it works as intended and moves the visual focus to the main content area of the page.

# Alternative Text (Alt text)

1. Using the [WAVE Web Accessibility Tool](http://wave.webaim.org//), enter the URL for your web page.
2. When the results of the evaluation are displayed, on the left side of the screen, select the flag tab underneath the clipboard tab.

   ![WAVE Flags Location](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/Example-WAVEtoolbar.jpg?api=v2)
3. Look at the errors denoted in red indicating errors in alternative text or missing alternative text.

   ![WAVE Errors](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/Example-WAVEalt-text-error.jpg?api=v2)
4. Click on the red error boxes to see which images are missing alt text.

# Tab Focus

1. Using the instructions from Navigation (above), Tab through your webpage.
2. Is there is a visual indicator, i.e. a box outline, an underline, or font color change, to indicate where you are on the webpage?

   ![Tab Focus Example](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/example-tabfocus.jpg?api=v2)

# Navigation

1. While your webpage is open in your browser, click on the address bar at the top of your browser.
2. Put your mouse under your desk or somewhere that you cannot reach it.
3. Press the Tab key. Continue pressing Tab to see if you can continually access all of the content on the webpage.
4. Be sure that items in drop down menus are either usable from the keyboard (using the Tab or arrow keys) or that all of the information that is in those drop down menus is available and usable from the keyboard only on the destination page for the menu item.
5. Pay attention to the Tab order. Does it jump from one side of the page to another? Or does it go in a logical, orderly fashion? (For example, down the left hand column, down the center, and down the right hand column.)

# Descriptive Hyperlinks

1. Look at the hyperlinks on your webpage.
2. Check to see if any of them say things like “Read more”, “Continue” or "Click here."
3. Do any hyperlinks that have the same text lead to different places? For example, two hyperlinks that are “Read More”, but lead to different destinations?
4. Check for hyperlinks that simply show the URL rather than displaying a description of the destination page. For example, use [Syracuse University Libraries](http://library.syr.edu/) rather than <http://library.syr.edu>.

# Contrast

1. Using the [WAVE Web Accessibility Tool,](http://www.wave.webaim.org/) select the contrast button.
   ![WAVE Contrast Accessibility Evaluate](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/contrast%20arrow.jpg?api=v2)
2. You will see the contrast errors found on your webpage. Click on each error to see where it appears on your webpage.
   ![Contrast Errors](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/contrast%20ex.jpg?api=v2)

# Form Labels

1. Using the [WAVE Web Accessibility Tool,](http://www.wave.webaim.org/) scroll down through the errors to see "Missing form label" is listed. (Note: If you do not see this error, your site has all of its form elements labeled correctly or there are no form elements on the page.)

   ![Missing Form Labels Error](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/form%20label%20error.jpg?api=v2)

# Headings

1. Using the [WAVE Web Accessibility Tool,](http://www.wave.webaim.org/) click on the icon on the left that looks like a little piece of paper.
   ![Heading Errors](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/heading%20checker.jpg?api=v2)
2. All of the headings on your page will be listed. Do you have headings?
3. Does the heading text for each heading make sense when read on its own?

# Captioning

1. On the video tool bar, click on the button that says “CC.” (If there is no CC button that means there is no closed captioning.)
   ![arrow pointing to CC button in video player.](https://answers.atlassian.syr.edu/wiki/download/attachments/159941095/ExampleCCButton.jpg?api=v2)
2. If the video has captions, turn off the volume on the video. Play the video. Can you can fully understand the message from the captions?
3. If not, turn up the volume and watch the video again.  Are there a lot of errors in the captions?

# External Documents

Adobe Acrobat Pro, Microsoft Word and Microsoft PowerPoint have accessibility checkers built-in.  Use these tools to check the accessibility of all documents you link from your webpages. For more information about how to use the accessibility checkers, refer to the relevant resources in [Creating Accessible Content](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159940780/Create+More+Accessible+Content)
