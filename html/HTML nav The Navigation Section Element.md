---

title: The HTML `<nav>` Element: Navigation Section

date: 2025-05-29

---


# The HTML `<nav>` Element: Navigation Section

The HTML `<nav>` element serves as a crucial component in website and document navigation, representing sections that link to other pages or parts within the current page. According to the HTML specification, this semantic element encapsulates major navigation blocks, providing structure and clarity to the information architecture of web applications and documents.

The `<nav>` element offers several advantages, including improved accessibility through ARIA attributes and enhanced document organization through nested sections. By wrapping navigation links in appropriate list elements like `<ul>` or `<ol>`, developers can create semantic structures that are both human-readable and assistive technology-friendly.

Key aspects of `<nav>` usage include its placement flexibility, support for multiple navigation sections, and its role in defining navigation landmarks. Best practices recommend using two distinct `<nav>` elements - one for primary navigation in the header and another for secondary navigation in the footer - while ensuring proper labeling for accessibility.

This introduction sets the stage for an exploration of the `<nav>` element's capabilities, from its basic functionality to its role in creating accessible and well-structured navigation systems.


## What is the `<nav>` Element?

According to the HTML specification, the nav element represents a section of a page that links to other pages or parts within the page, specifically major navigation blocks (HTML Standard, Navigation Section element). This semantic element is used to create navigation sections, which are collections of navigation links that help users navigate through a document or website (HTML Standard).

The nav element can contain other navigation elements such as anchor (a) elements for links, unordered list (ul) elements for menus, and ordered list (ol) elements for numbered lists (HTML Standard, Navigation Section element). While both forms are valid, using a list element provides better semantic clarity and accessibility (HTML Standard, Navigation Section element).

The HTML5 specification states that the nav element is intended for sections consisting of major navigation blocks. Not all groups of links on a page need to be in a nav element; it is primarily for navigation sections that consist of multiple links (HTML Standard, Navigation Section element). Common examples of navigation sections include primary and secondary navigation bars, tables of contents, and breadcrumb menus (MDN Web Docs, The nav element).

The nav element can be placed anywhere within a document, not just in the header (MDN Web Docs, The nav element). It can contain multiple navigation sections within the header and can be used for various purposes, such as presenting navigation information in a sidebar, navigation bar, or dropdown menu with appropriate CSS styling (MDN Web Docs, The nav element).


## How to Use the `<nav>` Element

The `<nav>` element should contain one or more list elements (like `<ul>` or `<ol>`) to represent the navigation links, as this provides better semantic clarity and accessibility (MDN Web Docs, The nav element).

While the `<nav>` element itself can contain various types of content, including prose links, it is recommended to use list elements whenever possible for clarity (MDN Web Docs, The nav element). The element can be presented in different layouts, such as a sidebar, navigation bar, or dropdown menu, with appropriate CSS styling (MDN Web Docs, The nav element).


### Major Navigation Blocks

The `<nav>` element is specifically intended for major navigation blocks, which consist of multiple links that help users navigate through the website or document (MDN Web Docs, The nav element). Not all groups of links on a page need to be contained within a `<nav>` element, but major navigation sections should use this semantic structure (MDN Web Docs, The nav element).


### Common Navigation Elements

In practice, navigation sections are typically found in the header, though they can also appear in other parts of the document, such as footers or sidebars (Semantic HTML, The `<nav>` Element). Common examples include menus, tables of contents, and breadcrumb sequences (HTML Standard, Navigation Section element).


### Document Structure

The `<nav>` element can contain multiple sections within the header, allowing for complex navigation structures (MDN Web Docs, The nav element). This element acts as a sectioning content element, defining the scope of `<header>` and `<footer>` elements nested within it (MDN Web Docs, The nav element). While the `<footer>` element is often used for lists of links that don't require nested `<nav>` elements, multiple `<nav>` elements can be present in a document (HTML Standard, Navigation Section element).


## Attributes and Accessibility

The `<nav>` element supports global attributes and can use ARIA (Accessible Rich Internet Applications) attributes to enhance accessibility. The most commonly used ARIA attributes include aria-labelledby to reference a nearby heading and aria-label for situations where no existing label text exists.

While the `<nav>` element primarily contains list elements like `<ul>` and `<ol>` for navigation links, it has the flexibility to include other content types as well. This semantic structure allows the element to represent a major block of navigation links, even when the content includes prose descriptions of links rather than simple HTML anchor tags.


### ARIA Attribute Usage

The `<nav>` element incorporates accessibility features through ARIA attributes:

- The `aria-labelledby` attribute points to another element containing the label text, typically using the element's ID (HTML Standard)

- The `aria-label` attribute contains the label text itself when no existing element has the proper label (MDN Web Docs)


### Content Types

The `<nav>` element can accommodate multiple content types while maintaining semantic clarity:

- Lists of navigation items using either `<ul>` or `<ol>`

- Prose descriptions of links for enhanced accessibility and content clarity

- Nested navigation structures using multiple `<nav>` elements (MDN Web Docs)


### Document Placement

The `<nav>` element can be placed anywhere within a document, supporting various layout options through CSS styling:

- Main navigation sections in the header

- Secondary navigation sections in footers or sidebars

- Table of contents sections (HTML Standard)


### Common Patterns

Developers frequently implement multiple `<nav>` elements per document, with common patterns including:

- Site-wide navigation in the header

- Intra-page navigation in footers or sidebars

- Specific navigation blocks for content sections (MDN Web Docs)


## Common Usage Examples

The `<nav>` element is commonly found in website headers as a primary navigation bar, providing a clear visual structure for site navigation. While the opening document mentions that navigation sections can appear in any part of the document, including footers or sidebars, header navigation remains the most prevalent use case (HTML Standard, Navigation Section element).

When used in headers, `<nav>` elements typically contain multiple navigation sections, allowing for complex navigation structures (HTML Standard). These sections can be nested within each other using multiple `<nav>` elements when necessary, though this is not common practice (MDN Web Docs, The nav element).

In addition to primary navigation bars, `<nav>` elements are frequently employed for table of contents sections and breadcrumb menus. The opening document specifically mentions that the table of contents on their website uses the `<nav>` element, demonstrating its versatility in organizing content navigations (Semantic HTML, The `<nav>` Element).

The element's flexibility allows it to contain various types of content, including prose links. While list elements like `<ul>` and `<ol>` are recommended for clarity and accessibility (MDN Web Docs), `<nav>` can accommodate prose descriptions of links to enhance content clarity and user understanding (HTML Standard).

Common patterns for `<nav>` implementation include site-wide navigation in headers and intra-page navigation in footers or sidebars (Semaphore). The element's ability to define navigation landmarks through ARIA attributes makes it particularly valuable for enhancing accessibility, especially when combined with appropriate CSS styling for different layout options (MDN Web Docs).


## Best Practices


### Structure Guidelines

The `<nav>` element can contain multiple sections within the header and footers, as demonstrated in the HTML Standard specification (Semantics, structure, and logic of HTML). However, Best Practice recommends using two distinct `<nav>` elements: one in the header for primary navigation and one in the footer for secondary navigation (Semantic HTML, The `<nav>` Element).


### Accessibility Considerations

When multiple `<nav>` elements are present, they must be labeled correctly to assist screen reader users (HTML Standard). The most effective approach is to use the `aria-labelledby` attribute, which points to a nearby heading element containing the label text. Alternatively, the `aria-label` attribute can be used when no existing element contains the label text (MDN Web Docs).


### Nesting Guidelines

While the `<nav>` element allows for nesting, this practice is uncommon and generally unnecessary (MDN Web Docs). The HTML Standard indicates that `<nav>` elements should represent whole sections of navigation links, not individual links (4.4.3 The nav element). Each `<nav>` element should clearly represent a distinct navigation landmark (HTML Standard).

## References

- [HTML The HTML Select Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20HTML%20Select%20Element.md)
- [HTML Nobr The non Breaking Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nobr%20The%20non%20Breaking%20Text%20Element.md)
- [HTML Author Fast Loading HTML Pages](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Author%20Fast%20Loading%20HTML%20Pages.md)
- [HTML Param The Object Parameter Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Param%20The%20Object%20Parameter%20Element.md)
- [HTML The Embed Text Track Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Embed%20Text%20Track%20Element.md)