---

title: HTML `<strike>` Tag: A Comprehensive Guide

date: 2025-05-29

---


# HTML `<strike>` Tag: A Comprehensive Guide

The HTML `<strike>` tag has long provided a simple way to create strikethrough text, but its days as a recommended solution may be numbered. While still supported by modern browsers, this tag has fallen out of favor with the web development community due to its lack of semantic meaning and potential compatibility issues in the future. In this comprehensive guide, we'll explore the `<strike>` tag's basic functionality, its historical usage, and why developers are encouraged to move on to more modern alternatives. You'll learn about the tag's syntax, browser support, and common use cases, as well as best practices for replacing it with the more semantically appropriate `<s>` and `<del>` tags.


## Introduction to HTML `<strike>`

The HTML `<strike>` tag creates a strikethrough effect in text by drawing a horizontal line through the content. This tag has been deprecated since HTML 4 and is no longer supported in HTML5, where developers should use alternative methods for achieving strikethrough effects.

The syntax for the `<strike>` tag is straightforward: it wraps around text that should appear with a strikethrough. For example:

```html

<p>Its an Edutech Company handles all Technical <strike>Non-Technical</strike> Subjects</p>

```

This will render as: Its an Edutech Company handles all Technical ~~Non-Technical~~ Subjects

The `<strike>` tag has basic support across multiple modern browsers including Chrome, Android, Firefox, Safari, and Opera. However, its use is discouraged due to its lack of semantic meaning and potential for improved accessibility through modern alternatives.

While the `<strike>` tag remains functional in most current browsers, it's important to note that it may not be supported in future web standards. Developers are encouraged to use the `<del>` tag for strike-through effects when indicating deleted text, or the `<s>` tag when marking content as obsolete. Both of these alternatives provide better semantic meaning and maintain compatibility with modern web development practices.


## Syntax and Basic Usage

The `<strike>` tag's primary function is to draw a horizontal line through text, creating a strikethrough effect. This is achieved by wrapping the text within the opening `<strike>` and closing `</strike>` tags.

Basic usage involves wrapping text with these tags to apply the strikethrough style. For example:

```html

<p>Its an Edutech Company handles all Technical <strike>Non-Technical</strike> Subjects</p>

```

This will render as: Its an Edutech Company handles all Technical ~~Non-Technical~~ Subjects

The tag's basic syntax is straightforward:

```html

<strike>Text with strikethrough effect</strike>

```

Each occurrence of `<strike>` must be properly closed with `</strike>`. For multi-line text, each line should be wrapped in its own `<strike>` tags.

As noted in the documentation, browsers maintain basic support for `<strike>`, including Chrome, Android, Firefox, Safari, and Opera. However, developers should not rely on its continued functionality, as it has been deprecated since HTML 4 and removed from HTML5 standards. The `<strike>` tag is now considered obsolete and is recommended for replacement with `<del>` for deleted content or `<s>` for general strikethrough effects.


## Browser Support and Compatibility

The `<strike>` tag maintains basic support in modern browsers including Chrome, Android, Firefox, Safari, and Opera. This compatibility ensures that existing websites using `<strike>` will continue to display strikethrough text correctly.

Developers should note that while `<strike>` remains functional, it has been deprecated since HTML 4 and removed from HTML5 standards. Instead, developers should use the `<del>` tag for deleted text or the `<s>` tag for general strikethrough effects. Both alternatives provide better semantic meaning and maintain compatibility with modern web development practices.

The `<strike>` tag's basic functionality allows it to be used interchangeably with `<s>` in most cases. However, its specific use case as a tag for deleted content makes `<del>` a more appropriate choice in many scenarios. The `<strike>` tag's continued support demonstrates its basic utility, though developers are strongly encouraged to transition to the more semantic alternatives for new projects.


## Common Usage Scenarios

The `<strike>` tag's primary historical use case involved text that has been deleted or is no longer relevant. This aligns with its current recommended use as a wrapper for deleted content, though modern alternatives provide clearer semantic meaning.

Common scenarios for `<strike>` include:

- Crossed-out text in early JavaScript and web interface design

- Displaying sold-out items in e-commerce applications

- Removing outdated content from web pages

- Indicating price changes through struck-through text

While `<strike>` remains functional for basic strikethrough effects, its specific use case as a deleted content marker makes `<del>` a more appropriate choice. The `<s>` tag serves as a general alternative, offering semantic parity with `<strike>` while maintaining better compatibility with modern web standards.


## Best Practices and Alternatives

The `<strike>` tag remains functional for basic strikethrough effects, but developers are strongly encouraged to transition to the more semantic alternatives for new projects. The primary usage case for `<strike>` involves text that has been deleted or is no longer relevant, though modern alternatives provide clearer semantic meaning.

For content requiring deleted status, the `<del>` tag is the recommended choice. This HTML5 element specifically indicates content that has been removed or revised, offering better semantic meaning. For general strikethrough effects without specific deleted context, the `<s>` tag serves as an appropriate alternative. Both `<s>` and `<del>` provide similar visual results through strikethrough functionality while maintaining better compatibility with modern web standards.

When using `<del>` to indicate deleted text, browsers typically render it with a strikethrough effect by default. However, developers have additional styling options using CSS, including changing the color and appearance of the strikethrough text. This flexibility allows for precise control over the visual representation of deleted content while maintaining semantic accuracy.

For developers working with legacy code that uses `<strike>`, the transition to `<del>` or `<s>` involves replacing `<strike>` tags with their respective modern alternatives. This process requires careful consideration of content context to maintain semantic accuracy. In cases where both `<del>` and `<s>` are valid options, developers should choose based on specific usage scenarios: `<del>` for content removal or revision history, and `<s>` for general strikethrough effects without deleted context.

## References

- [HTML The Document Title Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Title%20Element.md)
- [HTML Marquee The Marquee Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Marquee%20The%20Marquee%20Element.md)
- [HTML Using Date And Time Formats In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20Date%20And%20Time%20Formats%20In%20HTML.md)
- [HTML hr The Thematic Break Horizontal Rule Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20hr%20The%20Thematic%20Break%20Horizontal%20Rule%20Element.md)
- [HTML Nonce](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nonce.md)