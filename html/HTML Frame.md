---

title: HTML Frames and Iframes

date: 2025-05-29

---


# HTML Frames and Iframes

HTML frames once offered a practical way to display multiple web pages within a single window. However, their complexities and limitations have led modern web standards to recommend alternatives. This article explores framesets and iframes, examining their history, functionality, and why frames are no longer recommended for new web development projects.


## Frameset Basics

A frameset in HTML divides a browser window into multiple sections, each capable of displaying a separate HTML document. This structure is defined using the `<frameset>` element, which acts as a container for `<frame>` elements—each of which represents a distinct window within the overall layout.

To create a frameset, you first need to prepare separate HTML files to display in each frame. For example, you might create three files named frame1.html, frame2.html, and frame3.html. These files can contain any valid HTML content.

The basic syntax for a frameset defines either rows or columns using the cols and rows attributes, respectively. Here's an example of a frameset with three columns, each taking up 33% of the available space:

```html

<!DOCTYPE html>

<html>

<head>

<title>Frameset Example with Columns</title>

</head>

<body>

<frameset cols="33%, 33%, 33%">

<frame src="frame1.html">

<frame src="frame2.html">

<frame src="frame3.html">

</frameset>

</body>

</html>

```

Alternatively, you can use rows to create vertically stacked frames. Here's an example with three rows of different heights:

```html

<!DOCTYPE html>

<html>

<head>

<title>Frameset Example with Rows</title>

</head>

<body>

<frameset rows="50%, 25%, 25%">

<frame src="frame1.html">

<frame src="frame2.html">

<frame src="frame3.html">

</frameset>

</body>

</html>

```

Each frame can be customized with various attributes. For instance, you can control the border appearance with the frameborder attribute (1 for visible border, 0 for no border) and adjust the margin spacing between frame content using marginwidth and marginheight attributes. Here's an example with a frame that has no resize functionality and specific margin settings:

```html

<frame src="frame2.html" noresize frameborder="0" marginwidth="10" marginheight="15">

```

The `<frameset>` element should replace the `<body>` element in frameset documents, while the `<frame>` elements define the content for each frame. It's important to note that while modern browsers still support frames for backward compatibility, they are considered obsolete and should be avoided in new web development projects. Instead, developers are encouraged to use the `<iframe>` element for embedding independent HTML documents.


## Frame Elements

The FRAME element serves as the building block for frameset documents, allowing authors to define the content and appearance of individual frames. Each frame requires a separate HTML file and can be customized using attributes like src, name, and frameborder.

The SRC attribute specifies the initial document content for the frame, while the NAME attribute assigns a unique identifier that enables targeted loading of content. For example, setting target="mid_col" loads content into a middle frame, while target="_blank" or target="_top" reloads the entire page.

The FRAMEBORDER attribute controls border visibility, with a default value of 1 (showing all borders) that can be overridden by `<frameset>` attributes. For better control over frame appearance, developers can set MARGINWIDTH and MARGINHEIGHT to define space between frame contents and borders, measured in pixels.

The SCROLLING attribute determines scroll behavior, with options auto (default, providing scrolling devices when necessary), yes (always showing scrollbars), or no (disabling scrollbars). The FRAME element also accepts style sheet definitions for presentation, though these are less widely supported than `<frameset>` attributes.

To demonstrate FRAME usage, consider a nested frameset structure where the outer frame set divides available space into three equal columns. The inner frame set then divides the second area into two rows of unequal height. To enable data sharing among frames, authors include an OBJECT element in the HEAD of the frameset document with an ID attribute. Any document containing frame content can reference this identifier to access shared resources.

While frames offer basic functionality for embedding and organizing content, their implementation requires careful consideration of browser compatibility and user experience. The W3C explicitly advises against using frames in web development, recommending modern alternatives like content management systems (WordPress, Joomla!, Drupal) for website management. The IFRAME element provides similar functionality with enhanced features and better support for responsive design principles.


## Frameset Attributes

The `<frameset>` element plays a crucial role in organizing browser window space into multiple sections, with each section capable of displaying distinct HTML documents. This layout is achieved through the cols and rows attributes, which define the number and size of horizontal and vertical spaces, respectively. While these attributes still function, their use is deprecated in modern HTML development.


### Multi-Length Lists

The `<frameset>` element uses MultiLengths for specifying row and column sizes. These lists can contain pixel measurements, percentage values, or relative lengths. For instance, a simple two-column layout can be defined as follows:

```html

<frameset cols="200px, *">

```

This creates two columns, with the first fixed at 200 pixels and the second expanding to fill remaining space. Percentages allow for flexible sizing that scales with the window size:

```html

<frameset rows="50%, 50%">

```

This divides the window into two equal parts, each taking up 50% of the available height. The element's default behavior is to span 100% of the available space when dimensions are not specified.


### Additional Attributes

Beyond layout specifications, the `<frameset>` element supports several useful attributes:

- **Id and Class**: Document-wide identifiers for styling and scripting purposes

- **Title**: Element title for accessibility and metadata

- **Style**: Inline style information for presentation

- **Onload and Onunload**: Intrinsic events for script execution

- **Nested Frame Support**: Capable of handling nested frame sets to any depth


### Data Sharing and Scripting

Framesets facilitate data sharing through the OBJECT element, which can be included in the HEAD of the frameset document with a unique ID. This allows any frame document to reference the shared data. For example, the frameset might contain:

```html

<object id="sharedData" data="shared_data.html"></object>

```

And frames accessing this data would include:

```html

<frame src="frame_1.html" target="sharedData">

```

This structure enables coordinated content loading and data access across multiple frames.


### Implementation Considerations

When implementing framesets, developers should consider several key points:

- **Browser Support**: While most modern browsers still support frames, they are considered legacy technology in HTML5 and may be phased out in future versions

- **Responsive Design**: For better compatibility and accessibility, developers are encouraged to transition from frames to responsive iframe implementations

- **Performance**: Frames can impact page load times and resource management, making them less ideal for complex web applications

- **Accessibility**: Properly structured framesets improve usability for screen readers and assistive technologies, though they still present challenges for smaller devices and varying display environments


## Iframe Alternatives

As recommended by the W3C, modern web development should avoid using frames in favor of more flexible alternatives. While all current browsers support frames for historical compatibility, they are explicitly considered obsolete in HTML5 and may be removed in future versions.


### iframe Basics

The `<iframe>` element offers a direct alternative for embedding independent HTML documents within web pages. It provides essential attributes for controlling display and behavior, including width, height, and scrolling preferences. Unlike frames, iframes can be easily styled with CSS and resized using standard layout techniques.


### Embedding Content

To use an iframe, you simply specify the source URL using the src attribute and define visual dimensions with width and height properties. For example:

```html

<iframe src="https://example.com" width="600" height="400"></iframe>

```

This approach allows for precise control over embedded content while maintaining compatibility with modern web standards.


### Modern Implementation

By using iframes instead of frames, developers can implement responsive design principles more effectively. Rather than attempting to replicate frame functionality with deprecated attributes, modern development focuses on using iframes within responsive layouts. This approach provides better performance and accessibility while addressing the limitations of frames.

The move to iframes represents a broader shift in web development practices, with modern frameworks and content management systems (CMS) providing robust alternatives to frame-based layouts. As browser support continues to phase out legacy technologies, adopting these modern approaches ensures compatibility and adaptability in evolving web standards.


## Responsive Frame Design

Responsive frame design requires a different approach in modern web development. While frames can provide some responsiveness, they are not well-suited for creating truly responsive websites. The basic recommendation from web standards bodies is to use rows rather than columns and to use percentages for column widths instead of pixels.

The transition from frames to modern approaches typically involves evaluating existing frame-based layouts and converting them to use `<iframe>` elements with responsive CSS. While CSS can often duplicate frame layouts, iframes provide more flexibility and better performance.

A key consideration is that frames have limited support on smaller devices and can exhibit inconsistent behavior across different computers with varying screen resolutions. Additionally, their handling of the browser back button can be problematic.

For developers transitioning away from frames, the W3C recommends evaluating why frames were used originally. In most cases, CSS provides sufficient functionality to replace frames. If external content embedding is necessary, `<iframe>` elements offer a modern and more flexible alternative.

The modern approach to responsive design with iframes typically involves using CSS to style and size the frames. This includes setting dimensions with height and width properties, removing borders with CSS, and using percentage-based sizing for better responsiveness. The iframe tag itself uses standard attributes like src, width, and height to define the frame's content and appearance.

