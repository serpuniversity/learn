---

title: HTML `<ins>` Element: The Inserted Text Markup

date: 2025-05-29

---


# HTML `<ins>` Element: The Inserted Text Markup

The `<ins>` element in HTML serves a crucial role in marking up text that has been added to a document, providing both semantic meaning and flexibility in content representation. From its basic functionality of denoting inserted text to its more sophisticated attributes for explaining changes and recording timestamps, this element plays a significant part in maintaining the integrity and evolution of web content. Whether you're building a simple webpage or managing complex document updates, understanding how to use `<ins>` effectively can enhance both your development process and the accessibility of your content.


## Introduction to the `<ins>` Element

The `<ins>` element in HTML is used to indicate text that has been added to a document, serving as a semantic marker for changes or updates. This element, also known as the Inserted Text element, requires both a start (opening) and end (closing) tag to properly define the inserted content.

Basic Usage and Syntax

The fundamental syntax for the `<ins>` element is:

```html

<ins>Insert inserted text here</ins>

```

The element can be placed within any element that accepts phrasing content and has no specific parent restrictions. For example:

```html

<p>HTML stands for <ins>Hypertext Markup Language</ins>.</p>

```

While the element primarily generates underlined text by default, as per the current browser CSS settings, developers have the flexibility to customize this visual representation through CSS styling. More specifically, the element applies a text-decoration property of "underline" by default, which can be modified to suit design requirements.

Additional Features and Attributes

The `<ins>` element supports several attributes to provide further context for the inserted content:

- `cite`: This attribute allows specifying the URL of a document or message that explains why the text was inserted.

- `datetime`: This attribute provides the date and time of the insertion, formatted as YYYY-MM-DDThh:mm:ssTZD. This helps maintain the document's chronological accuracy and provenance.

For instance, the following example demonstrates using both the `cite` and `datetime` attributes:

```html

<p>HTML <ins datetime="2018-11-21T15:55:03Z" cite="https://example.com/revision-history">5 is the latest version of HTML</ins></p>

```

The `<ins>` element plays an important role in semantic web development, particularly in accessibility and content management. Semantically, it allows clearly marking up changes in a document, distinguishing it from other elements like `<strong>` (strong text) or `<em>` (emphasized text). This distinction helps screen readers and other assistive technologies provide accurate information about the document's evolution and content status.

In terms of rendering, while most browsers display inserted text with an underline by default, developers have complete control over how this content is presented through CSS styling properties. The element's semantic value resides in its ability to clarify changes in document content while allowing full customization of its visual representation.


## Basic Usage and Syntax

The `<ins>` element must always be used in pairs - a start tag and an end tag - with the content placed between them. This structure applies to all HTML elements unless specified otherwise in the documentation:

```html

<ins>Opening text content</ins>

```

Both the start and end tags are required; omitting either will result in parsing errors. The element can contain any phrasing content, including other HTML elements, but cannot include both block and inline content within the same `<ins>` block:

```html

<p>This paragraph contains <ins>some inline content</ins> and <ins>multiple <strong>sub-elements</strong></ins></p>

```

To demonstrate proper usage:

```html

<!doctype html>

<html>

<head>

  <title>Example of <ins> Tag</title>

</head>

<body>

  <p>HTML stands for Hypertext Markup Language.</p>

  <p>HTML is the basic building block of any webpage. It is used with CSS and Javascript to create interactive web pages.</p>

  <p><ins>HTML5 is the latest version of HTML</ins></p>

</body>

</html>

```

This example correctly uses `<ins>` to highlight the latest version of HTML within a paragraph of related content.


## Attributes and Customization

The ins element supports several attributes to provide additional context for the inserted text. The cite attribute requires a valid URL that explains why the text was added, while the datetime attribute provides the date and time of the insertion in a format defined by RFC 3339. These attributes help maintain the document's chronological accuracy and provenance.

The datetime attribute must contain a valid date-time value, formatted as YYYY-MM-DDThh:mm:ssTZD. This format requires specific character casing (uppercase T and Z) and strict date format requirements (year component must be four or more digits representing a number greater than 0). The element can also include optional global attributes and event attributes, which are documented in the HTML specification.

When displaying ins elements, user agents may follow citation links for private use and determine modification timestamps based on time zone offset information. The screen reader announcements associated with ins elements can be customized using CSS, including techniques to enable or disable content announcements as needed.


## Rendering and Browser Support

The `<ins>` element is displayed with default styling that includes text-decoration: underline, though this can be customized through CSS. As a inline element, it has no specific parent restrictions and can contain any phrasing content, including other HTML elements, except block content within the same `<ins>` block.

All modern browsers fully support the `<ins>` element, with consistent implementation across popular engines including Firefox 1.5+, Safari 2+, Chrome 1+, Opera 9+, Edge 79+, Edge (Legacy) 12+, and Internet Explorer 9+. These implementations adhere to the HTML specification, providing reliable support for both the element's basic functionality and its attributes (cite and datetime).

The element's rendering behavior remains consistent across supported browsers, with all major engine implementations supporting the required pair of start and end tags. Developers can confidently rely on this element's presence in web development projects targeting contemporary browser environments.


## Accessibility and Semantics

The `<ins>` element's support for ARIA roles helps integrate with assistive technologies, though its basic implicit role of "insertion" is sufficient for many use cases. Authors can explicitly set the element's role using ARIA attributes when more specific semantics are needed.

The element supports several standard HTML attributes, including class, id, and slot, which can enhance its accessibility through CSS styling and improved document structure. Authors should use these attributes to enhance semantic meaning and maintain a clear document hierarchy.

For customized built-in elements requiring specific accessibility handling, authors must implement additional techniques such as:

- Using tabindex for focusability

- Setting ARIA role to "button" for accessibility technologies

- Providing aria-label for accessible names

- Managing aria-disabled states for logical disablement

- Implementing keyboard event handling

- Updating visual styling to reflect logical state changes

This implementation approach ensures that customized elements remain accessible across different user agents and assistive technologies, maintaining the semantic integrity of the inserted content.

