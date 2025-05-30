---

title: HTML Cheat Sheet

date: 2025-05-29

---


# HTML Cheat Sheet

HTML forms the bedrock of web development, powering everything from simple text documents to complex interactive applications. Its importance cannot be overstated – every website you visit relies on HTML to deliver its content. Yet, despite its fundamental role, many developers and designers struggle to master its intricacies. This cheat sheet distills the essential concepts and elements of HTML, equipping you with the knowledge to build robust, semantically meaningful web pages. Whether you're just beginning your coding journey or looking to refine your expertise, this guide covers everything from basic structure to advanced features, helping you craft web content that's both functional and accessible.


## Definitions

The `<html>` element serves as the root (top-level element) of an HTML document and contains all other elements, making it the foundation of web page structure. According to MDN Web Docs, all HTML documents follow a standard format that includes this element, which signals to web browsers that the content is written in HTML5, the most current version of the language.

The document's structure begins with the DOCTYPE declaration, which informs the browser about the document type and version being used. For HTML5 documents, the required syntax is <!DOCTYPE html>, though the actual document type declaration can be omitted due to browser compatibility.

Within the HTML structure, the `<head>` section contains essential metadata about the webpage, including the document's title, character encoding, and links to external CSS and JavaScript files. The `<head>` can also include elements for defining the page's relationship to external sources, specifying custom font styles, and embedding time stamps using the `<time>` element.

The `<body>` section contains all content visible to users, providing the container for the entire webpage's elements. It includes fundamental tags for creating paragraphs, lists, and preformatted text, as well as specialized elements for handling multimedia content like images, audio, and video.

Text content can be formatted using various HTML elements, each serving specific purposes. The `<strong>` and `<em>` elements emphasize text through strong importance and text styling, respectively, while the `<sub>` and `<sup>` elements create subscript and superscript text. The `<abbr>` element represents abbreviations or acronyms, while the `<mark>` element highlights text for reference purposes.

Lists can be created using `<ul>` for unordered lists and `<ol>` for ordered lists, while detailed information can be presented using `<dl>`, `<dt>`, and `<dd>` for description lists. These elements allow developers to create structured content that is both visually organized and semantically meaningful.

The HTML structure also supports multimedia content through several key tags. The `<img>` element links images to web pages, while `<audio>` and `<video>` elements embed media players for sound and video files. The `<embed>` and `<object>` elements further extend this capability by allowing developers to include multimedia content and objects such as Portable Document Format (PDF) files directly in web pages.


## Document Structure

The structure of an HTML document follows a specific format that includes several key components. The document begins with a document type declaration that informs the browser about the document type and version being used. For modern HTML documents, the required syntax is <!DOCTYPE html>, though the actual document type declaration can be omitted due to browser compatibility.

The HTML document is structured around three primary elements: the `<html>`, `<head>`, and `<body>` tags. The `<html>` element serves as the root (top-level element) of the document and contains all other elements, making it the foundation of web page structure. This element also includes a lang attribute that specifies the document's language, which can improve accessibility and localization.

Within the `<html>` element, the `<head>` section contains essential metadata about the webpage, including the document's title, character encoding, and links to external CSS and JavaScript files. This section is crucial for providing the browser with important information about how to render the page. Specifically, the `<head>` section requires the charset declaration and title element, with additional components including viewport settings, base URL, stylesheet links, and icon definitions.

The visible content of the webpage is contained within the `<body>` section of the document. This section includes fundamental tags for creating paragraphs, lists, and preformatted text, as well as specialized elements for handling multimedia content like images, audio, and video. The `<body>` section also supports various text formatting elements, including `<strong>` for strong importance, `<em>` for text styling, and `<sub>` and `<sup>` for subscript and superscript text. The `<abbr>` element represents abbreviations or acronyms, while the `<mark>` element highlights text for reference purposes.

HTML documents support the creation of structured content through several key elements. Headings can be defined using the `<h1>` to `<h6>` tags, with the `<h1>` tag typically reserved for the page's main title while subsequent tags denote subheadings in descending order of importance. The `<div>` element serves as a generic container for page sections or blocks, while the `<span>` element functions as an inline container for styling elements. Paragraphs are created using the `<p>` element, which forms the foundational structure for visible content.

Multimedia content can be embedded in HTML documents using several key tags. The `<img>` element links images to web pages, while `<audio>` and `<video>` elements enable the embedding of media players for sound and video files. The `<embed>` and `<object>` elements further extend this capability by allowing developers to include multimedia content and objects such as Portable Document Format (PDF) files directly in web pages. These elements enable the creation of rich, interactive web experiences while maintaining the fundamental structure and organization of the HTML document.


## Common Elements


### Common HTML Elements and Their Usage

Developers frequently utilize a wide array of HTML elements to structure and present content. This section introduces key elements, their attributes, and demonstrations of their usage.


#### Text Formatting

HTML offers several elements for emphasizing and styling text. The `<em>` element provides emphasis, rendering text in italics, while `<strong>` indicates strong importance, displaying text in bold. For example:

`<em>`Italicized text`</em>` vs. `<strong>`Bold text`</strong>`

The `<sub>` and `<sup>` elements create subscript and superscript text, respectively. The `<abbr>` element represents abbreviations or acronyms, while `<mark>` highlights text for reference purposes.


#### List Tags

Lists are essential for organizing information in a structured format. The `<ul>` tag creates an unordered list, while `<ol>` defines an ordered list. Each item in these lists is represented by the `<li>` tag.

For example, an unordered list might look like this:

`<ul>`

  `<li>`Item 1`</li>`

  `<li>`Item 2`</li>`

  `<li>`Item 3`</li>`

`</ul>`

Description lists use the `<dl>` tag to group terms with descriptions. Each term is defined by `<dt>`, while the description follows with `<dd>`. Here's an example:

`<dl>`

  `<dt>`Term 1`</dt>`

  `<dd>`Description 1`</dd>`

  `<dt>`Term 2`</dt>`

  `<dd>`Description 2`</dd>`

`</dl>`


#### Table Tags

Tables enable the presentation of tabular data. The `<table>` element defines the overall structure, while `<caption>` provides a caption for the table. The `<thead>` section groups header rows, while `<tbody>` contains table body content.

Here's an example of basic table structure:

`<table>`

  `<caption>`Sample Table`</caption>`

  `<thead>`

    `<tr>`

      `<th>`Column 1`</th>`

      `<th>`Column 2`</th>`

    `</tr>`

  `</thead>`

  `<tbody>`

    `<tr>`

      `<td>`Row 1, Column 1`</td>`

      `<td>`Row 1, Column 2`</td>`

    `</tr>`

    `<tr>`

      `<td>`Row 2, Column 1`</td>`

      `<td>`Row 2, Column 2`</td>`

    `</tr>`

  `</tbody>`

`</table>`


#### Additional Elements

The `<figure>` element denotes self-contained content, often with a caption provided by `<figcaption>`. The `<hr>` element represents a thematic break between paragraph-level elements.

For example:

`<figure>`

  `<img src="example.jpg" alt="Example Image">`

  `<figcaption>`Figure Caption`</figcaption>`

`</figure>`

HTML also includes several useful elements for specific purposes. The `<address>` element denotes contact information, as seen in this example:

`<address>`

  Written by `<a href="mailto:example@example.com">`Author Name`</a>`. Find us at: example.com

`</address>`

The `<article>` element denotes a self-contained composition, while the `<aside>` element represents content tangentially related to the main document. These elements help in creating more semantic and accessible web content.


## Advanced Features

The HTML Document Object Model (DOM) represents the structure of a web page as a tree of nodes, with elements as the primary building blocks. The DOM API provides JavaScript methods for interacting with these elements, enabling dynamic web page manipulation. This API allows developers to read and modify the content, structure, and style of web pages using script.

Element creation and manipulation are fundamental operations in web development. The DOM API includes methods for creating new elements, setting their attributes, and appending them to the document. For example, the `document.createElement()` method creates a new HTML element, while `element.setAttribute()` sets its attributes and `element.appendChild()` adds child elements.

Manipulating the DOM allows developers to create responsive and interactive web pages. For instance, the `element.classList` property manages CSS classes, while `element.innerHTML` sets the element's content. The DOM also supports event handling through methods like `element.addEventListener()`, enabling developers to react to user interactions and dynamic changes.

Web development frameworks and libraries often build upon the DOM API to provide higher-level abstractions. Understanding the underlying DOM operations enables developers to effectively use these tools while maintaining control over web page structure and behavior.

## References

- [HTML Using HTML Comments](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20HTML%20Comments.md)
- [HTML Font](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Font.md)
- [HTML The Document Body Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Body%20Element.md)
- [HTML Using Microformats In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20Microformats%20In%20HTML.md)
- [HTML Standard Metadata Names](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Standard%20Metadata%20Names.md)