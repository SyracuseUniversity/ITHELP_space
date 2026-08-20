---
title: "Accessibility Q&A"
confluence_id: "159942006"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942006/Accessibility+Q+A"
version: 19
last_modified: "2022-04-04T14:23:14.000Z"
status: "current"
parent_id: "159966137"
---

## Accessibility Q&A

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=html&locale=en_US&version=2)

Have a questions about accessibility? Send it to [accessibleIT@syr.edu.](mailto:accessibleIT@syr.edu.) Here are some of the questions that are frequently asked about accessibility.

## Documents and Presentations

There are two common issues that could be causing the PDF accessibility errors. First, when you export your accessible Word document to PDF you must do it using Word (Win) because Word (Mac) cannot export an accessible PDF. Exporting from Word (Mac) will result in a PDF that has no tag tree and therefore no structure. Another common issue is using 'Print to PDF' instead of 'Export to PDF' or 'Save as PDF'. Using the 'Print to PDF' option will also result in a PDF with no tag tree and no structure, which results in a document which is completely inaccessible to screen reader users.

Headers and Footers are often used in longer documents to include content information and navigational aids such as the document title, current chapter or section of a book, page numbers, and even journal citation information. When you are creating long documents, adding this type of information to the header and footer helps meet accessibility guidelines by providing logical structure.

That being said, header and footer information can pose a variety of issues for screen reader users. Header and footer content can interrupt the logical reading flow of the document. For this reason authoring tools such as Microsoft Word and Adobe InDesign when exported to PDF will place header and footer information in page artifact tags in other words they will be hidden from screen reader users

But for scanned articles and book chapters the footer may contain important information such as the original page numbering of a journal article that doesn't match the page number of the scanned PDF. This information is important and should be available for the screen reader user.

Usually I recommend that you tag the first occurrence of a running header or footer in the reading order and mark subsequent occurrences as page artifacts that won't be read aloud by the screen reader.

Next, if page numbers on the footer don't match the page numbers of the PDF re-number the PDF pages to match the original. This can be done in the page thumbnails panel.Go to page thumbnails and choose page labels there you can customize the page numbering of the PDF pages.

The 'appropriate nesting failed' error pertains to the use of headings in the document. Headings should be used to communicate the structure of the document and can be used to create an outline of the content. They should begin with H1 as the top level heading, and move to H2 for subheadings, H3 for further subheadings and so on.

The 'appropriate nesting failed' error occurs most often when the document either has no headings at all or begins with something other than an H1. Open the tags panel and review your tags to make sure that there is an H1 as the first heading and that other headings are assigned in a logical manner.

When creating hyperlinks it is important that the text communicates the purpose of the link. Displaying a long URL is usually not sufficient to meet this criterion, so the preferred method is to hyperlink the title of the resource/site being linked. Presumably, if you are providing a hyperlink, the intention is that the user will be able to click/tap the link rather than write it down. In some cases you can show a web address if is reasonably short and contains understandable text. For example: [zoom.syr.edu](http://zoom.syr.edu), [bookstore.syr.edu](https://bookstore.syr.edu), etc. Note that SU branding/editorial guidelines call for hiding the https:// portion of the URL for stylistic purposes.

You are correct that all slides in your PowerPoint presentation must have a title. Slide titles are added as headings in an exported PDF and they are also used as main headings in the Outline View of the presentation. If you don't want the slide title to appear on the slide you can go to the Arrange tool on the toolbar, open the Selection Pane, and toggle the visibility of the slide title off.

When you use a template to create a PowerPoint presentations there are usually empty content containers for slide titles, bulleted lists, images. etc. If you only add content using these containers your content will be read by a screen reader in the order intended. If you add any other content to the slide such as text boxes or images that is outside of the default containers you will get a warning to check the slide reading order. You can do this by going to Arrange > Selection Pane. This shows you the content layers on the slide and you can reorder them as needed. Note: this pane is a list of stacked layers so the title would be on the bottom followed by the main content box, followed by the footer, etc.

Trying to merge two PowerPoint presentations, or even copy slides from one presentation to another, can cause a number of accessibility issues including slides without titles, empty content boxes, and reading order issues. This is most often related to merging/copying slides that have two different master slides and themes. In order to minimize the errors be sure to use the Insert > Reuse Slides functionality. Be sure to uncheck the 'Use Source Formatting' checkbox so that the slides will be imported into the new presentation's theme. Never try to copy/paste slides from one presentation to another.

## Web

This actually relates to WCAG 1.3.1: Info and Relationships, specifically the need for semantic markup as opposed to strictly visual markup. There is absolutely nothing wrong with using bold and italics on the web, you just have to be sure not to mark them up using the older <b> and <i> elements. These tags are strictly visual and don't carry any semantic meaning. The preferred method is to use <em> and <strong> instead. These elements are semantic elements and will represent the text both visually as bolder or italicized text AND semantically as carrying more importance or stress. It should be noted that at this point in time screen readers do not pass this kind of emphasis on to the user, however using semantic markup is considered valid HTML.

There is nothing in the WCAG 2.1 guidelines that prohibits the use of an accessible PDF on the web. That being said, even accessible PDF documents can present problems for users with disabilities, users of assistive technology, and users of mobile devices. For this reason we strongly encourage you to consider whether the information being shared wouldn't be better presented as a web page or in the body of an email rather than as a PDF.

Using the target attribute to open a link in a new tab or window is allowed but should be used only when necessary. For example, a help link in a form will open a new tab or window so as not to interrupt the process of filling out the form. If you are going to use the target attribute to open a new tab or window you should advise the user in advance to avoid confusion.

Embedded third-party content should always be tested for keyboard accessibility, color contrast, and screen reader accessibility. The three most popular types of embedded content are Google interactive maps, Twitter feeds, and YouTube videos. Each of these use iframes to embed content and are pretty good in terms of keyboard and screen reader accessibility. There are some color contrast issues with Google maps and some YouTube controls that have been reported to Google. Note that the generated embed code for the iframe usually does not include a title attribute so always be sure to go into the code and add title="whatever the title of the thing is" to the <iframe>.

This question is addressed in WCAG 1.4.5: Images of Text (Level AA) which states that if the technologies being used (in our case WordPress, Answers, etc.) can achieve the visual presentation, text is used to convey information rather than images of text. Exceptions to this are things like logos where the graphical representation is considered essential, or text that occurs as part of a chart, graph, or screenshot.

Graphical text poses problems not just for screen reader users but also for users who rely on screen magnification or users who need to enlarge the font size or modify the color contrast on their device. Graphic text can't be modified using these settings and for this reason should not be used.

According to WCAG Success Criterion 1.4.1: Use of Color, you must use some means other than color alone to distinguish text links from other textual content on the page. Usually this is an underline, but it would also be acceptable to use another form of text decoration such as a visible outline shading, etc. The goal is to ensure that the links are communicated to users who cannot perceive color. Keep in mind that this does not have to be applied to text links that are inside of navigation menus or drop-down fields.

We know that meaningful images on the web require descriptive alternative text for screen reader users, and decorative images should be given null alternative text (alt=""). But what about images that are also links? If you have a linked image that is immediately adjacent to a text-based link, and they both go to the same URL, you should wrap the image and the text link inside of the same link tag and give the image null alternative text. This makes it a single tab stop for keyboard users and prevents redundant links for screen reader users. If on the other hand you have an image that is being used as a link without any adjacent text, use the alternative text attribute to describe the link destination rather than the image. In other words, for linked images the link purpose is considered more important than the visual description.

## Forms

You can create accessible document-based forms in Word or as a fillable PDF, however keep in mind that with a Word form you are limited to only a couple of form input types: specifically text boxes and checkboxes. Other form input types such as drop-down boxes and radio buttons are not currently accessible in Word. Using a fillable PDF form gives you more input-type options. That being said, I would encourage you to consider whether your form should be document-based at all. You may want to consider a forms authoring tool like Frevvo or Qualtrics for accessible online forms.

Once you have used the Prepare Form tool to create all of your form fields, given them labels using the tooltip field, and verified the tab order in the fields list panel there is one more thing you need to do to make the form accessible. Each form field has to be in it's own top-level <form> tag in the PDF. This is done in the tag tree, not in the Prepare Form tool. If you haven't done this you will probably get a 'Tagged form fields failed' error. Instructions for tagging your form fields are available from WebAIM on the [Add Tags to Form Fields](https://webaim.org/techniques/acrobat/forms#tags) section of their accessible forms page.

## Captions

Kaltura creates machine-generated captions for videos that are uploaded or saved automatically from a Zoom cloud recording. While Kaltura does boast a high accuracy rate, machine-generated captions will always require editing. Usually names, places, school/college names, etc. will need to be edited, capitalization and punctuation should be reviewed, etc. Luckily Kaltura has a caption editor built in for making these kinds of edits.

## Procurement

Yes. The ICT Accessibility Policy applies to all information and communication technology purchases regardless of the intended audience. The policy does allow for an exclusion in the case of single instance, specialized software or hardware purchased for individual use. Examples would include hardware purchased for individual use, specialized research software, etc. Note that this provision does not apply if the software is required as part of a job function as this would impact others who may be called upon to perform those duties.

The required forms depend on the type of approval being sought. You will find all of the forms and required documentation for Policy Exclusion, Compliant Software, and Non-Compliant Software requests along with the accompanying testing tools on the [Procurement of Accessible ICT Products and Services](https://answers.atlassian.syr.edu/wiki/spaces/itsservapp011/pages/159387372/Procurement+of+Accessible+ICT)  page under the Forms and Required Documentation section.
