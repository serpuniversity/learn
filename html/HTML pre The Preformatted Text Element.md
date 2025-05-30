---

title: `<pre>`: The Preformatted Text element

date: 2025-05-29

---


# `<pre>`: The Preformatted Text element

The pre element defines preformatted text that preserves spaces, line breaks, and formatting characters, displaying content in a fixed-width font. This article explores the syntax, usage, and styling options for the pre element, including its attributes, content considerations, and accessibility requirements. Additionally, it examines how preformatted text differs from regular text, handles various content types, and provides advanced styling techniques while addressing common pitfalls.


## Syntax and Basic Usage

The pre element defines preformatted text that preserves spaces, line breaks, and formatting characters. This text displays in a fixed-width font and can be customized with CSS. The basic syntax requires both opening and closing tags:

`<pre>` Contents... `</pre>`

The element's default styling includes a block-level display, monospaced font, and preserved white space. However, several attributes and features impact its behavior and appearance:

Attribute Usage:

- cols: Specifies the number of characters per logical line (though this has no visual effect, use CSS width instead)

- wrap: Controls text wrapping behavior (ignored in modern browsers, use CSS white-space instead)

- width: Sets the preferred count of characters per line (also has no visual effect, CSS width is recommended)

Content Considerations:

Leading newline characters immediately following the opening tag are stripped. The element parses text content as HTML, requiring special handling for characters like <, which must be escaped using character references. Commonly contained elements include code, samp, and kbd for representing computer code, output, and keyboard inputs respectively.

For accessibility, alternate descriptions are required for images or diagrams created using preformatted text, especially important for users with low vision conditions. The default CSS settings include display: block, font-family: monospace, white-space: pre, and margin: 1em 0. These properties ensure consistent rendering across modern browsers while allowing developers to customize the element's appearance.


## Text Output and Formatting

The pre element specifically preserves all whitespace, including leading spaces and line breaks, which is crucial for maintaining the intended layout of formatted text. This behavior is distinct from regular paragraph elements, which collapse multiple spaces into single spaces and ignore most whitespace characters.

Since preformatted text is displayed in a fixed-width font, it's particularly useful for showing code snippets or ASCII art where exact positioning of characters matters. The element handles tab characters consistently, rendering them as a fixed number of spaces (typically eight), which helps maintain alignment across different viewing environments.

The default rendering of preformatted text includes keeping all original whitespace intact, displaying each line based on natural boundaries (such as newline characters), and maintaining consistent spacing between characters. This combination of features makes pre the ideal choice for showing source code, configuration files, or any text where visual layout is as important as the content itself.


## Accessibility and Content Handling

The preformatted text element requires careful handling, especially when dealing with computer code and ASCII art content. Leading newlines immediately following the opening tag are stripped, which can affect how your text displays, particularly when creating diagrams or precise layouts. To maintain proper rendering, always test your content after modifying the structure near the tag's opening point.

For accessibility, provide clear descriptions of images or diagrams represented through preformatted text, particularly for users with visual disabilities. This guidance applies to both ASCII art representations and any visual content you choose to display using these elements. The default CSS styling includes some basic properties, but additional customization might be necessary to meet specific accessibility requirements.

Modern alternatives like `<textarea>` offer enhanced functionality while maintaining similar formatting capabilities, making them worth considering for complex or user-editable content. When using preformatted text for code samples, ensure each code block includes proper language syntax highlighting or wraps correctly using appropriate CSS properties.


## Advanced Usage and Styling

In addition to basic text, `<pre>` elements can contain `<code>`, `<samp>`, and `<kbd>` tags to represent computer code, sample output, and keyboard inputs respectively, providing a robust framework for structured preformatted content. When representing computer code, the `<code>` element should be nested within a `<pre>` block to maintain proper formatting and structure according to language conventions. For example:

```html

<pre>

<code>function Panel(element, canClose, closeHandler) { this.element = element; this.canClose = canClose; this.closeHandler = function () { if (closeHandler) closeHandler() }; }</code>

</pre>

```

The `<samp>` element can be used to represent computer output, while `<kbd>` is ideal for indicating keyboard inputs or user actions. This semantic approach enhances both the accessibility and maintainability of your code samples.

Modern CSS allows extensive customization of `<pre>` elements, including precise control over display properties. The element's default block-level display can be overridden with custom styles, and the monospaced font can be replaced with any desired fixed-width typeface. Essential CSS properties for `<pre>` elements include:

- display: block (or another block-level value)

- font-family: monospace (or any fixed-width font family)

- white-space: pre (or pre-wrap for more flexible line-wrapping)

- margin (for spacing)

- border and padding (for visual boundaries)

Accessibility requires careful consideration, particularly when displaying images or diagrams through preformatted text. Always provide clear and concise alternative descriptions, especially for users with visual disabilities. The default browser styling includes display: block, font-family: monospace, white-space: pre, and margin: 1em 0, which can be extended with additional CSS properties as needed.


## Common Pitfalls and Best Practices

The `<pre>` element's functionality can be extended using the `<code>`, `<samp>`, and `<kbd>` tags for specialized content representation. For computer code, the `<code>` element should be nested within a `<pre>` block to maintain proper formatting and structure according to language conventions. For example:

```html

<pre>

<code>function Panel(element, canClose, closeHandler) { this.element = element; this.canClose = canClose; this.closeHandler = function () { if (closeHandler) closeHandler() }; }</code>

</pre>

```

When displaying sample output or computer-generated text, the `<samp>` element serves as an effective alternative, while `<kbd>` is ideal for representing keyboard inputs or user actions. This semantic approach enhances both the accessibility and maintainability of code samples.

Modern CSS provides extensive customization options for `<pre>` elements, including precise control over display properties. Essential CSS properties for `<pre>` elements include:

- display: block (or another block-level value)

- font-family: monospace (or any fixed-width font family)

- white-space: pre (or pre-wrap for more flexible line-wrapping)

- margin (for spacing)

- border and padding (for visual boundaries)

To properly display images or diagrams through preformatted text, provide clear and concise alternative descriptions, especially for users with visual disabilities. The default browser styling includes display: block, font-family: monospace, white-space: pre, and margin: 1em 0, which can be extended with additional CSS properties as needed.

Following best practices, ensure that `<pre>` elements contain valid HTML syntax, particularly when using characters like <, which must be escaped using character references. Leading newline characters immediately following the opening `<pre>` tag result in the first newline being stripped, which can affect diagram display. Always test content modifications near the tag's opening point to maintain proper rendering.

## References

- [HTML Reference](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Reference.md)
- [HTML Using HTML Form Validation And The Constraint Validation API](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20HTML%20Form%20Validation%20And%20The%20Constraint%20Validation%20API.md)
- [HTML th The Table Header Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20th%20The%20Table%20Header%20Element.md)
- [HTML u The Unarticulated Annotation Underline Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20u%20The%20Unarticulated%20Annotation%20Underline%20Element.md)
- [HTML Relme](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relme.md)