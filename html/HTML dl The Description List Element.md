---

title: HTML dl Tag: The Description List Element

date: 2025-05-29

---


# HTML dl Tag: The Description List Element

The HTML `<dl>` element provides a robust mechanism for displaying metadata through key-value pairs, offering developers a semantic solution for complex term-description structures. This article explores the `<dl>` element's capabilities, from its basic syntax to advanced styling techniques, ensuring developers understand how to implement and optimize this versatile HTML feature for modern web development.


## Description and Purpose

The HTML `<dl>` element represents a description list, which displays metadata as a list of key-value pairs. It consists of one or more `<dt>` (term) elements followed by one or more `<dd>` (description) elements, though `<div>`, `<script>`, and `<template>` elements can also be included. The structure must contain only `<dt>`, `<dd>`, `<div>`, `<script>`, or `<template>` elements, with terms followed by descriptions.


### Content Order and Grouping

Each term in a description list is defined between `<dt>` elements, while the corresponding description follows in one or more `<dd>` elements. Multiple descriptions can be grouped under a single term by placing them after the `<dt>`. For example:

```html

<dl>

  <dt>Firefox</dt>

  <dd>A free, open source, cross-platform, graphical web browser developed by the Mozilla Corporation and hundreds of volunteers.</dd>

  <dt>Mozilla Firefox</dt>

  <dd>Same as above</dd>

  <dt>Fx</dt>

  <dd>Same as above</dd>

</dl>

```


### Styling and Accessibility

The default CSS styling provides basic spacing between items, with display: block, margin-top: 1em, margin-bottom: 1em, margin-left: 0, and margin-right: 
0. To create a key-value separator in CSS, you can use: dt::after { content: ": "; }. For accessibility, while screen readers do not specifically identify `<dl>` content as a list, the structure should be written in a way that clearly communicates relationships between terms and descriptions.


## Syntax and Basic Usage

The `<dl>` element consists of `<dt>` (term) elements and `<dd>` (description) elements, as demonstrated in the examples provided. These elements can be combined in various ways: a single term with multiple descriptions, multiple terms with a single description, or multiple terms and descriptions mixed together. For instance, Mozilla's Firefox browser can be represented as a single term with multiple descriptions about its development and technical specifications.

The `<dl>` element can contain multiple structures, including:

- Single term and description: `<dl>``<dt>`Term`</dt>``<dd>`Description`</dd>``</dl>`

- Single term with multiple descriptions: `<dl>``<dt>`Term`</dt>``<dd>`Description 1`</dd>``<dd>`Description 2`</dd>``</dl>`

- Multiple terms with multiple descriptions: `<dl>``<dt>`Term 1`</dt>``<dd>`Description 1`</dd>``<dt>`Term 2`</dt>``<dd>`Description 2`</dd>``</dl>`

The element supports multiple content types, including flow elements, `<div>` elements, `<script>` elements, and `<template>` elements. To demonstrate, consider this example of a simple definition list wrapped in a `<div>` element: `<div>``<dl>``<dt>`Term`</dt>``<dd>`Description`</dd>``</dl>``</div>`. This structure allows for grouping related terms and descriptions while maintaining the proper `<dl>` element hierarchy.

HTML5 standards specify that the element must contain only `<dt>`, `<dd>`, `<div>`, `<script>`, or `<template>` elements. Developers can use these elements to create flexible, semantic structures for displaying key-value pairs, such as metadata or glossary information. The `<dl>` element's browser support spans all major platforms, including Chrome, Edge, Firefox, Safari, and Opera, making it a reliable choice for cross-browser compatibility.


## Content Structure and Validation

The `<dl>` element requires both start and end tags and contains either direct term-description groups (with one or more `<dt>` elements followed by one or more `<dd>` elements) or `<div>` elements that contain these elements. The structure must only include `<dt>`, `<dd>`, `<div>`, `<script>`, or `<template>` elements, with terms followed by descriptions.


### Content Constraints and Best Practices

The `<dl>` element must contain either zero or more groups consisting of one or more `<dt>` elements followed by one or more `<dd>` elements, or one or more `<div>` elements containing these elements. The compact attribute, while supported, is considered obsolete and should be replaced with CSS for layout control.


### Valid Content Examples

To demonstrate proper structure, consider the following valid examples:


#### Single term and description

```html

<dl>

  <dt>Firefox</dt>

  <dd>A free, open source, cross-platform, graphical web browser developed by the Mozilla Corporation and hundreds of volunteers.</dd>

</dl>

```


#### Single term with multiple descriptions

```html

<dl>

  <dt>CSS</dt>

  <dd>Cascading Style Sheets, a language used for describing the presentation of a document written in HTML</dd>

  <dd>When combined with HTML, it enables web developers to create the visual layout of web pages</dd>

</dl>

```


### Structural Best Practices

Developers should ensure that each `<dt>` element is directly followed by one or more `<dd>` elements, with no content other than `<dt>`, `<dd>`, `<div>`, `<script>`, or `<template>` elements allowed within the `<dl>` scope. This strict structure maintains semantic clarity and accessibility, making the relationship between terms and descriptions easily understandable for both humans and screen readers.


##  Styling and Accessibility

The default CSS styling for `<dl>` elements provides basic spacing with margin-top and margin-bottom set to 1em, while margin-left and margin-right are both 0. This allows for clean separation between list items while maintaining a minimal appearance. However, developers have significant flexibility in customizing the layout through CSS, including control over padding and margin values.

To clarify the relationship between terms and descriptions, developers can implement a key-value separator using CSS. For example: dt::after { content: ": "; } This approach ensures that screen readers and other assistive technologies can properly interpret the structure of description lists. When implementing custom styles, developers should maintain the semantic relationship between `<dt>` and `<dd>` elements to preserve accessibility.

Mozilla's developer documentation includes an example demonstrating proper styling techniques. This example resets all margins and padding using dl { margin: 0; padding: 0; } while applying specific padding to `<dt>` elements: dt { padding: 10px; font-weight: bold; } These techniques provide a clear visual distinction between terms and descriptions while maintaining semantic clarity for screen readers. Proper styling and accessibility practices ensure that description lists remain effective and usable across various devices and user contexts.


## Browser Support and Implementation

The `<dl>` element has full browser support across desktop and mobile platforms, including Chrome, Edge, Firefox, Internet Explorer, Opera, Safari, and their respective mobile versions. The element's implementation and requirements are detailed in the HTML specifications and MDN Web Docs.


### Browser Support

All major web browsers fully support the `<dl>` element, making it a reliable choice for cross-browser compatibility. The element works consistently across platforms, from desktop computers to mobile devices, ensuring that description lists display correctly regardless of the user's environment.


### Implementation Requirements

The `<dl>` element requires both start and end tags and contains either direct term-description groups or `<div>` elements that contain these groups. It supports flow content, including `<div>`, `<script>`, and `<template>` elements, while maintaining strict structure requirements.


### Semantic and Accessibility Considerations

For accessibility, while screen readers do not specifically identify `<dl>` content as a list, the structure should communicate relationships between terms and descriptions clearly. The element's implementation must adhere to HTML standards, ensuring compatibility with assistive technologies and proper semantic meaning.


### Styling and Customization

Developers can customize `<dl>` elements using standard CSS properties such as margin, padding, and display. Common techniques include resetting margins, applying specific padding to `<dt>` elements, and implementing key-value separators with CSS content properties. Proper styling maintains semantic clarity while improving visual presentation.

