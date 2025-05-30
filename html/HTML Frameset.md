---

title: Understanding the HTML `<frameset>` Tag

date: 2025-05-29

---


# Understanding the HTML `<frameset>` Tag

When the World Wide Web first emerged in the early 1990s, the `<frameset>` tag revolutionized web design by enabling simultaneous display of multiple independent web content sections within a single browser window. This innovative approach to webpage structure allowed developers to create sophisticated, multi-pane layouts that predated modern responsive design frameworks.

At its core, the frameset solution provided an elegant way to divide the browser window into distinct, independently scrolling regions. Each region could load and display a separate HTML document, creating complex layouts featuring navigation bars, headers, footers, and main content areas. This capability represented a significant departure from the single-document structure of traditional HTML pages.

While the `<frameset>` tag has long since been deprecated in favor of more modern layout techniques, understanding its conceptual foundations remains valuable for web developers and designers. Its influence can be seen in contemporary approaches to responsive design, where similar principles of independent content regions and dynamic layout division continue to shape web development practices.


## Introduction to HTML Frameset

The original purpose of frameset was to enable simultaneous display of multiple, independent web content sections within a single browser window. This allowed for sophisticated webpage designs featuring elements like navigation bars, headers, footers, and main content areas. Each frame within the frameset could contain a distinct HTML document, enabling developers to structure complex web pages in new ways.

A basic frameset divides the browser window into rows or columns using the `rows` and `cols` attributes. For example, to create a layout with two frames taking up 50% of the height each, one would use `rows="50%,50%"`. Similarly, horizontal division into three equal-width columns would employ `cols="33%,33%,33%"`.

At the most fundamental level, a frameset contains frame elements through which it loads and displays individual HTML documents. The frameset itself replaces the traditional `<body>` tag in framing documents, while each frame uses the `<frame>` tag to define its contents and behavior. Essential attributes of the frame elements include `src` to specify the loaded document, `name` for frame identification, and `frameborder` to control border visibility between frames.

The frameset structure supports multiple levels of nesting, allowing for complex layouts with both horizontal and vertical divisions. This nesting capability enables developers to create sophisticated multi-column, multi-row designs, though modern alternatives generally offer more flexible and responsive solutions.


## Basic Syntax and Structure

The `<frameset>` tag contains frame elements that divide the screen into multiple smaller sections, each displaying an independent HTML document. This fundamental structure replaced the `<body>` tag in frameset documents, with each frame defined by the `<frame>` tag.

The frameset element supports both horizontal and vertical divisions through the `rows` and `cols` attributes. For example, to create two frames each occupying 50% of the browser window, one would use `rows="50%,50%"` for vertical division or `cols="50%,50%"` for horizontal division.

Each frame within the frameset uses the `src` attribute to specify the URL of the document it should display, while the `name` attribute provides identification for future reference. Additional frame attributes include `frameborder` to control border visibility, `marginwidth` and `marginheight` to set spacing between the frame border and content, and `scrolling` to control the display of scrollbars.


### Example Usage

A basic frameset structure might look like this:

```html

<!DOCTYPE html>

<html>

<head>

<title>HTML Frames</title>

</head>

<frameset rows="10%,80%,10%">

  <frame name="top" src="/html/top_frame.htm" />

  <frame name="main" src="/html/main_frame.htm" />

  <frame name="bottom" src="/html/bottom_frame.htm" />

</frameset>

<noframes>

  <body>

    Your browser does not support frames.

  </body>

</noframes>

</html>

```

This example creates a frameset with three vertical sections, each displaying a different HTML document. The `<noframes>` element provides alternative content for browsers that do not support frames.


## Common Attributes

The rows and cols attributes enable precise control over frame layout. For instance, setting `cols="33%,33%,33%"` divides the window into three equally-sized columns. The rows attribute functions similarly for vertical divisions, while combining both can create complex layouts.

The frameborder attribute controls border display between frames, with values of 1 (default) drawing a separator or 0 eliminating it. The marginwidth and marginheight attributes specify space between frame contents and their respective margins, though their default values vary between user agents.

The scrolling attribute manages scroll bar behavior, offering options for "auto" (default, displaying scrollbars when necessary), "yes" (always displaying scrollbars), and "no" (disabling scrollbars completely). Each frame can be uniquely identified using the name attribute for targeted content placement.

The id attribute assigns a document-wide identifier, while the class attribute provides a document-wide identifier similar to the class attribute. The title attribute specifies the frame's title, and the style attribute allows inline style information.

The FRAME element supports additional properties not directly related to framesets, including longdesc for linking to long descriptions, bordercolor for setting frame border color (using named colors or #RRGGBB format), and hidefocus for controlling focus visibility (true or false).

The FRAMESET element can include attributes like border (setting frame border width, default 4 pixels), bordercolor (setting frame border color), framespacing (measuring space between frames), and lang (setting language code). These attributes help control the visual appearance and behavior of framesets and frames.


## Historical Usage and Modern Replacements

Framesets were widely used in web development for creating navigation bars, headers, footers, and more, serving as the foundation for advanced web development frameworks before being deprecated long before HTML 5's release in 2014. Current browser versions no longer support framesets, which have been replaced by modern alternatives.

One of the primary usability issues with framesets was their inability to adapt to responsive designs, as each frame represented a separate HTML file, making complex project maintenance difficult. The poor user interface featured multiple scroll bars for each frame in a single webpage, and frame buttons functioned independently, including back button functionality. These limitations significantly affected accessibility, particularly for screen readers and assistive technologies.

The frameset's main advantage was providing access to multiple devices in one place without requiring physical hardware, offering broader testing coverage and reduced costs. However, modern web development has addressed these limitations through alternative technologies like CSS Flexbox, Grid, and iframes. The frameset tag still defines layout using rows and columns through the 'rows' and 'cols' attributes, but these have been superseded by more flexible and scalable solutions.

Examples of modern alternatives include React for single-page applications and the widespread adoption of iframes for embedding content from other sources while maintaining a clean main page structure. The latest version of HTML 5, released in 2014, officially deprecated the frameset and frame tags due to these significant usability and accessibility issues. Developers are encouraged to migrate to these more effective and maintainable solutions for creating responsive, accessible web content.


## Implementation Examples

A simple horizontal frameset divides the screen into two sections, each displaying an individual HTML document. For instance, the following code creates a frameset where the top frame displays a navigation menu and the bottom frame displays the main content:

```html

<!DOCTYPE html>

<html>

<head>

<title>Horizontal Frame Layout</title>

</head>

<frameset rows="40%,60%">

  <frame src="/html/navigation.htm" />

  <frame src="/html/content.htm" />

</frameset>

<noframes>

  <body>

    Your browser does not support frames.

  </body>

</noframes>

</html>

```

This basic structure can be extended to create more complex layouts through nested framesets. For example, the following code demonstrates a three-column layout where the left column contains navigation, the right column displays content, and the center column acts as a container for additional frames:

```html

<!DOCTYPE html>

<html>

<head>

<title>Three-Column Frame Layout</title>

</head>

<frameset cols="25%,50%,25%">

  <frame src="/html/left_menu.htm" />

  <frameset rows="20%,80%">

    <frame src="/html/sidebar.htm" />

    <frame src="/html/main_content.htm" />

  </frameset>

  <frame src="/html/right_column.htm" />

</frameset>

<noframes>

  <body>

    Your browser does not support frames.

  </body>

</noframes>

</html>

```

Modern web development encourages the use of alternative layout techniques like CSS Flexbox and Grid for creating responsive and maintainable designs. While framesets remain useful for understanding traditional web layout concepts, developers are advised to explore these modern alternatives for building contemporary web applications.

