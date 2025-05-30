---

title: The blockquote element: HTML Quotation and Citation

date: 2025-05-29

---


# The blockquote element: HTML Quotation and Citation

When it comes to properly formatting quotations in HTML, developers have a range of elements at their disposal. While short inline quotations can use the convenient q element, extended quotes require a different approach. In this article, we'll explore the blockquote element, a powerful tool for incorporating longer quotations while maintaining semantic structure. We'll examine its proper usage, from basic implementation to advanced styling options, ensuring your quoted content is both accurate and visually appealing.


## Definition and Purpose

The blockquote element clearly indicates that the enclosed text is an extended quotation from another source, as demonstrated in the example where it's used to quote directly from the World Wildlife Fund's website. This usage distinguishes it from inline quotations, which should be marked with the q tag, as shown in the comparison between blockquote and q elements in the HTML Quotation and Citation Elements document.

The element's structure follows the specifications for flow content and sectioning root, with support for global attributes and event handling. As noted in the HTML elements reference, it's a mandatory block-level element that requires both a start and end tag, following the syntax `<blockquote>`...`</blockquote>`. This structure allows for the inclusion of multiple HTML elements within the quote, such as headers, footers, and paragraphs, to maintain proper content structure.

Default browser rendering treats blockquote elements with indentation, as described in the HTML Blockquote Tag Explained document. Browser compatibility spans major platforms including Chrome, Edge, Firefox, Safari, and Opera, ensuring wide accessibility. While default styling provides basic separation through margins, developers can customize appearance extensively using CSS properties like border-left, padding-left, and margin-left, as illustrated in the styling examples provided.


## HTML Structure and Attributes

The blockquote element is a block-level flow content element that requires both a start and end tag, following the syntax `<blockquote>`...`</blockquote>`. It's capable of incorporating multiple HTML elements including headers, footers, and paragraphs to maintain structured content, as demonstrated in examples from the HTML elements reference and the `<blockquote>`: The Block Quotation element documentation.

According to the HTML5 specification, the element supports global attributes and event handling, providing flexibility in how it's used within a document. When used correctly, blockquote elements enhance semantic structure by clearly indicating quoted content, as shown in the example from the World Wildlife Fund's website.

The element's official attribute is the cite attribute, which provides a URL for the source of the quotation. This URL can be referenced through the cite IDL attribute, as specified in the HTML5 element reference. For shorter quotes that should remain inline rather than in a separate block, the q element should be used instead, as illustrated in the HTML Quotation and Citation Elements documentation.

Commonly, browsers render blockquote elements with indentation for visual separation, following the default display properties described in the HTML Blockquote Tag Explained document. However, developers have extensive customization capabilities through CSS properties such as border-left, padding-left, and margin-left, demonstrated in the styling examples provided. This allows for precise control over the visual presentation of quoted content while maintaining semantic structure.


## CSS Styling Options

By default, browsers render blockquote elements with indentation to visually separate them from the surrounding content. This visual distinction helps maintain content structure while indicating that the enclosed text is from an external source, as explained in the blockquote reference documentation.

For detailed customization, developers can use various CSS properties. The default browser rendering already applies margin properties, but developers can further control indentation with margin-left and margin-right properties. Alternative styling options include setting quotes to italics or using background colors, although these styles should be applied sparingly to maintain accessibility, as noted in the blockquote styling guidance.

The element's styling capabilities support both text and container layouts. For instance, developers can add a left border using border-left, create padding through padding-left, or control margins with margin-left and margin-right properties. When properly used, these CSS options enhance the presentation without overwhelming the content, as demonstrated in the blockquote styling examples.

The blockquote element's styling flexibility makes it suitable for various contexts, from simple indentation to complex quotation boxes. The key is to prioritize semantic clarity over purely visual effects, ensuring that the content remains accessible and meaningful to all users. As the American Psychological Association's guidelines emphasize, proper blockquote formatting supports effective communication while maintaining academic and professional standards.


## Best Practices and Accessibility

Use the blockquote element for quotations over 40 words to maintain proper semantic structure, as explained in the HTML Tutorials documentation. When incorporating source information, place the citation within the blockquote element rather than after the closing tag, in accordance with best practices outlined in the `<blockquote>`: The Block Quotation element documentation.


### Content Separation and Attribution

To enhance accessibility and readability, separate quotation content from attribution information, placing the citation outside the blockquote structure when appropriate, as noted in the HTML Tutorials summary. This approach maintains clear visual separation of quoted material from its source while ensuring proper semantic tagging.


### Styling Considerations

When applying visual styles, prioritize semantic clarity over decorative effects. Avoid using quotation marks or background colors that could hinder readability for users with visual disabilities, as advised in the blockquote styling guidance. Instead, focus on maintaining consistent text formatting across quoted and non-quoted content within the same document, ensuring that quoted material remains distinguishable through consistent indentation or other structural means while remaining readily accessible to all readers.


## Technical Specifications and Browser Support

The blockquote element represents an extended quotation from another source and is part of the HTML5 specification for flow content and sectioning root. It must contain flow content and can nest other HTML elements such as headers, footers, and paragraphs to maintain proper content structure.


### Technical Specifications

The element's syntax requires both start and end tags: `<blockquote>...</blockquote>`. It supports global attributes and event handling, with the cite attribute providing a URL for the source of the quotation. The HTMLQuoteElement interface manages the element's functionality and attributes. Common attributes include:

- cite: Specifies the URL of the source, reflected through the cite IDL attribute

- Global attributes: Supports standard HTML attributes like class, id, and style

- Event attributes: Allows adding event handlers through the onclick, onmouseover, etc. properties


### Default Rendering

The browser's default rendering for blockquote elements includes indentation, margin properties, and display block for separation from surrounding text. Customization options for indentation and margins include:

- display: block

- margin-top: 1em

- margin-bottom: 1em

- margin-left: 40px

- margin-right: 40px


### Browser Support

The blockquote element is natively supported across major browsers including Chrome, Edge, Firefox, Safari, and Opera, ensuring consistent functionality across platforms.

## References

- [HTML The Output Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Output%20Element.md)
- [HTML Translate](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Translate.md)
- [HTML Draggable](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Draggable.md)
- [HTML The Button Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Button%20Element.md)
- [HTML Data](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Data.md)