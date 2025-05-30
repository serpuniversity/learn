---

title: HTML Main element

date: 2025-05-29

---


# HTML Main element

The HTML main element serves as a crucial container for webpage content, distinguishing itself from navigation, sidebars, and repeated sections through its semantic and technical specifications. As the primary content area of a document, it requires proper implementation to provide meaningful structure for both automated tools and human readers. This article explores the main element's technical requirements, browser support, and essential guidelines for creating accessible, SEO-friendly web content that follows HTML standards.


## Main Content Container

The main element serves as the primary container for webpage content, distinguishing itself from navigation, sidebars, and repeated sections. According to HTML standards, it must contain unique content specific to the page or application and typically should not include navigation links, copyright notes, sidebars, forms, or branding assets.


### Technical Specifications

The main element follows specific technical guidelines:

- It requires both the starting and ending tags

- It can only appear as a hierarchically correct main element within flow content

- Its DOM interface is HTMLElement

- It has the ARIA role of main

- Its content type is flow content and palpable content


### Browser Support

The main element receives varying levels of support across browsers:

- Chrome: 
26.0

- Firefox: 
12.0

- Edge: 
21.0

- Internet Explorer: 
7.0

- Safari: 
16.0


## Semantic Importance

The main element holds fundamental importance in HTML document structure for several key reasons:


### Defining Core Content

The main element explicitly marks the primary content area of a document, distinguishing it from other elements like navigation, sidebars, and repeated sections. This semantic distinction helps both automated tools and human readers understand the document's structure and focus.


### Accessibility

From an accessibility standpoint, the main element behaves as a main landmark role, which assistive technologies can use to identify and navigate to large sections of content. This feature is particularly valuable for users who rely on screen readers or other assistive technologies.


### SEO Optimization

Search engines benefit from the main element's clear semantic meaning. Modern search algorithms use HTML structure, including the main element, to better understand and index web page content, potentially improving site visibility and ranking.


### Implementation Guidelines

To implement the main element correctly, developers should ensure it contains unique content specific to the page or application, following these guidelines:

- Use only one visible main element per document

- Avoid including navigation links, copyright notes, sidebars, forms, or branding assets within the main element

- The element should not contain more than one instance without the hidden attribute

- Support skip navigation through proper id attribute usage (e.g., `<main id="main-content">`)

By adhering to these principles, developers can create more accessible, semantically rich web content that leverages the powerful features of the HTML main element.


## Technical Specifications

The main element's technical specifications are detailed in the HTML specification, where it is defined as having both starting and ending tags and requiring a properly structured hierarchy within flow content. Its DOM interface aligns with standard HTML elements as an instance of HTMLElement, and it carries the ARIA role of "main," enhancing its accessibility functionality.

The element's content type is categorized as flow content, which means it can contain a wide range of other HTML elements, except for certain prohibited elements like `<address>`, `<article>`, `<aside>`, `<blockquote>`, `<details>`, `<dialog>`, `<figure>`, `<footer>`, `<form>`, `<h1>` to `<h6>`, `<header>`, `<main>`, `<menu>`, `<nav>`, `<ol>`, `<p>`, `<section>`, `<table>`, `<ul>`. This restriction prevents nested landmark elements and ensures clear content structure.

Custom data attributes can be added using the standard `data-` prefix, allowing authors to attach additional information without affecting the element's core functionality. The main element also supports global attributes and event attributes, maintaining compatibility with standard HTML features while providing specific functionality for landmark identification and skip navigation.


## Accessibility Features

The `<main>` element's accessibility features include support for skip navigation functionality and its role as a main landmark, which benefits assistive technology users. By providing an `id` attribute, developers can enable skip navigation links, allowing users to bypass repeated content sections. This functionality particularly benefits users who rely on screen readers or other assistive technologies.

When implementing skip navigation, developers should structure their code as follows:

```html

<body>

  <a href="#main-content">Skip to main content</a>

  <!-- navigation and header content -->

  <main id="main-content"> <!-- main page content --> </main>

</body>

```

Browser support for these features is widely available across modern browsers, including Chrome 26.0, Firefox 12.0, Edge 21.0, Internet Explorer 7.0, and Safari 16.0, ensuring broad compatibility for developers looking to enhance their website's usability and accessibility.


## Best Practices

The main element serves as the primary content container for a webpage, distinguishing itself from navigation links, copyright notes, sidebars, forms, or branding assets. Implementations should ensure that a document contains only one visible main element, with content that is unique to the document and not repeated across multiple pages.


### Content and Structure

Content within the main element should expand upon the central topic of the document or application, representing the dominant content of the `<body>`. Browser support begins with Chrome 26.0, Firefox 12.0, Edge 21.0, Internet Explorer 7.0, and Safari 16.0. The element supports global attributes applicable to all HTML elements, but does not define any specific attributes.


### Behavioral Guidelines

The main element must not contain more than one instance without the hidden attribute, and should not be a descendant of `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` elements. The content model requires at least one `<li>` element for `<ul>` structures, with the element itself requiring at least one unique child element to maintain proper semantic structure.


### Technical Considerations

The element supports a wide range of content, including but not limited to `<li>`, script-supporting elements, and other flow content. However, certain elements like `<address>`, `<article>`, `<aside>`, `<blockquote>`, `<details>`, `<dialog>`, `<figure>`, `<footer>`, `<form>`, `<h1>` to `<h6>`, `<header>`, `<main>`, `<menu>`, `<nav>`, `<ol>`, `<p>`, `<section>`, and `<table>` are explicitly prohibited to prevent nested landmark elements and maintain clear content structure.


### Integration with Accessibility

The main element functions as a primary landmark, allowing assistive technologies to identify and navigate significant document sections. Authors can enable skip navigation through proper id attribute usage, allowing users to bypass repeated content sections such as navigation menus or copyright notices. This functionality is particularly beneficial for users who rely on screen readers or other assistive technologies.

