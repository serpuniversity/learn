---

title: HTML `<small>`: the side comment element

date: 2025-05-29

---


# HTML `<small>`: the side comment element

The `<small>` element in HTML offers a straightforward way to denote side comments, disclaimers, and small print. While its default behavior of reducing text size by 30% provides a quick solution for inline notifications, developers face choices about when to use `<small>` versus CSS for text reduction. This article explores the element's capabilities, from basic usage to its role in semantic HTML, helping authors make informed decisions about when to leverage this built-in formatting tool.


## Definition and Basic Usage

The `<small>` element signifies side-comments and small print in a document, often including disclaimers, legal text, and copyrights. By default, browsers render content within this element in a smaller font size than the surrounding text. The `<small>` tag can contain phrasing content and must have both start and end tags, though it cannot contain block-level elements or certain interactive content.

The element's default font size reduction is defined by CSS, with the `<small>` tag applying a font size of 0.7em. However, authors have the flexibility to adjust these settings through CSS, allowing for more precise control over the element's appearance. While the `<small>` element remains fully compatible with modern browsers, the HTML specification encourages developers to exercise judgment when deciding whether to use this tag for semantic purposes or to rely on CSS for styling.

The element's classification as phrasing content means it can be placed within any element that accepts this type of content. The `<small>` tag is particularly useful for legal notices, copyright information, and fine print, as demonstrated by its usage in footer elements to display copyright statements. This semantic approach to small print provides better accessibility than generic styling, though developers are encouraged to supplement visually distinguished content with appropriate ARIA attributes when additional context is necessary.


## Rendering and Default Styles

By default, the `<small>` tag renders text at 0.7em (70% of the parent element's font size). This consistent scaling enables developers to create hierarchies of text sizes without manual calculations. The tag's inline display property means it respects surrounding text flow while maintaining its reduced size.

The element's consistent behavior across browsers ensures reliable rendering of small print without requiring complex fallbacks or multiple classes. This uniformity allows designers to trust that their content will appear as intended across different viewing environments and devices.


### Key Considerations for Implementation

When using `<small>` for text reduction, authors should consider the potential accessibility implications. While the element serves its semantic purpose well for copyright and disclaimer text, longer passages or complex legal documents may require more structured approaches. Using `<small>` for entire paragraphs can result in inconsistent reading experiences, particularly for users relying on screen readers.

The element's compatibility with both global and event attributes provides flexibility for interactive applications. Developers can apply conditional styling based on user interactions without altering the underlying semantic structure. This dual functionality demonstrates HTML's ongoing adaptability while maintaining a clear separation between presentation and meaning.


## Content Constraints and Nesting

The `<small>` element requires both a start and end tag, with no support for namespace declarations even in foreign elements. It accepts global attributes and event attributes, offering flexibility beyond basic semantic use cases. While the element supports CSS for text sizing, its default behavior defines a font size of 0.7em, equivalent to "smaller" styling.

As a phrasing content element, `<small>` can appear anywhere phrasing content is accepted, including within paragraph contents and footer elements. This classification enables consistent rendering across different parent elements while maintaining semantic clarity. The element's simple structure makes it widely compatible across major browsers, including Chrome, Edge, Safari, Firefox, Opera, and Internet Explorer.

The `<small>` tag's flexibility extends to event attributes, allowing for interactive applications that conditionally apply styles based on user interactions. While the element's default styling works well for short text runs, its use cases include copyright information, disclaimers, and legal text. For more complex content structures, developers are encouraged to supplement `<small>` with additional semantic elements or CSS classes for greater accessibility and maintainability.


## Accessibility and Semantics

The `<small>` element functions as phrasing content and must be placed within elements that accept phrasing content or flow content. This includes standard paragraph elements and footer sections, where it can effectively serve as secondary content formatting.

The element carries no implicit ARIA role and defaults to the generic role, making it suitable for side comments and fine print without requiring additional accessibility roles. For improved clarity, developers may use ARIA attributes like `aria-describedby` to provide more context for de-emphasized content, particularly when assistive technologies may miss the semantic significance of the `<small>` styling.

While the element remains valid in HTML5, the specification encourages authors to use their best judgment when determining whether `<small>` is appropriate for its intended purpose or if CSS styling would be more suitable. The `<small>` tag's simple structure and consistent browser support make it a reliable choice for formatting secondary content, though its use should align with broader web accessibility principles and presentation needs.


## Best Practices and Considerations

Authors are encouraged to exercise judgment when deciding whether to use `<small>` or CSS for formatting purposes. While the element remains a valid HTML5 choice, its use should align with broader web accessibility principles and presentation needs. The small element's classification as phrasing content means it can appear anywhere that accepts phrasing content or flow content, including standard paragraph elements and footer sections.

For authors concerned about separation between structure and presentation, the small element's compatibility with both global and event attributes offers flexibility for interactive applications. The element's simple structure and consistent browser support make it a reliable choice for formatting secondary content. However, when using the small element for extended content or entire sections, developers are encouraged to supplement its use with additional semantic elements or CSS classes for greater accessibility and maintainability.

## References

- [HTML Attribute Step](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Step.md)
- [HTML Using Microdata In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20Microdata%20In%20HTML.md)
- [HTML tr The Table row Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20tr%20The%20Table%20row%20Element.md)
- [HTML Using HTML Form Validation And The Constraint Validation API](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20HTML%20Form%20Validation%20And%20The%20Constraint%20Validation%20API.md)
- [HTML The Generic Section Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Generic%20Section%20Element.md)