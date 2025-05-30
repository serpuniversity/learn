---

title: HTML `<del>`: The Deleted Text Element

date: 2025-05-29

---


# HTML `<del>`: The Deleted Text Element

The HTML `<del>` tag serves a specific purpose in web development by visually indicating deleted text through a standard strikethrough effect. This semantic element not only transforms the appearance of marked content but also enhances document organization, particularly in scenarios where revisions or track changes are essential. From its basic functionality to its extended capabilities with attributes like cite and datetime, the `<del>` tag demonstrates the balance between simple implementation and rich semantic meaning in modern web design.


## Introduction to the `<del>` Tag

The HTML `<del>` tag marks text that has been deleted from a document, applying a strikethrough effect by default. This element visually distinguishes deleted content, making it particularly useful for displaying document revisions or track changes. For example, in the provided code snippet:

```html

<p><del datetime="2011-01-05T08:15:30+05:30" cite="https://www.w3resource.com/html/HTML-tutorials.php">We are not using HTML 4.01 Transitional DOCTYPE.</del></p>

```

This marks specific text within a paragraph, with the deletion timestamp and reference link displayed inline.

The `<del>` tag supports two key attributes for additional context:

- `cite`: Specifies a URL explaining the reason for deletion

- `datetime`: Indicates when the deletion occurred, using ISO 8601 date-time format

These attributes help maintain document integrity by providing clear explanations for changes. The element's basic syntax requires both a start and end tag, allowing it to contain multiple inline or block-level elements as needed.


## Rendering and Default Styles

When the `<del>` tag is used, browsers typically render the deleted text with a horizontal line through it. This styling applies the CSS property "text-decoration: line-through" by default, though user stylesheets can override this appearance. For example:

```html

<p style="text-decoration:line-through;">The content to be deleted</p>

```

This inline CSS produces the same strikethrough effect as the `<del>` tag.

The element visually represents deleted text in red with a gray background color:

```html

<style>

  del { color: red; text-decoration: line-through; background-color: #fbb; color: #555; }

</style>

```

This styling results in the deleted text appearing as ~~deleted~~ with a reddish background and darker gray text color.

In addition to the default styling, authors can customize the appearance using standard CSS properties. For instance:

```html

<style>

  del { text-decoration: line-through; color: red; }

</style>

<p>This is <del>deleted</del> text.</p>

```

The element's default rendering allows it to contain either inline elements or block-level elements. When used as an inline element, no block-level elements should be nested within it. However, it can reside within both inline and block-level elements without limitation.


## Attributes and Additional Information

The cite attribute requires a URL explaining the reason for deletion, which should be a well-formed URI. For example:

```html

<del cite="https://www.w3resource.com/html/HTML-tutorials.php">We are not using HTML 4.01 Transitional DOCTYPE.</del>

```

The datetime attribute demands a valid ISO 8601 date-time format with specific case requirements. Here are examples of properly formatted values:

```html

<del datetime="1990-12-31T23:59:60Z">Sample deleted text</del>

<del datetime="1996-12-19T16:39:57-08:00">More deleted text</del>

```

The attribute value must include the literal letters 'T' and 'Z' in uppercase, and the date-fullyear production must present four or more digits representing a number greater than 0.

The `<del>` element supports both phrasing content and flow content, allowing it to be nested within various HTML structures. However, when used as an inline element, it should not contain block-level elements. For example, while this is valid:

```html

<p>Removed content: <del>old information</del></p>

```

This would be invalid:

```html

<p><del>old <strong>information</strong></del></p>

```

To enhance accessibility, authors should provide additional context through the cite and datetime attributes. The cite attribute can link to a document explaining the deletion, while the datetime attribute specifies when the change occurred. This metadata helps users understand the history and purpose of the deleted text.

Additionally, the element's default style includes a red foreground color with a gray background. To maintain readability, particularly for users with visual impairments, the contrast ratio between the text and background should meet accessibility standards.


## Usage Examples

The `<del>` tag can be used in various contexts to indicate deleted text within an HTML document. Here are some examples demonstrating its usage:


### Basic Usage

The `<del>` tag can be used to mark deleted text within a paragraph:

```html

<p>DLF stands for <del>Delhi Land and Finance.</del></p>

<p>Delhi Land and Finance is one of the largest commercial real estate developers in India.</p>

```

When rendered, the first paragraph will display "DLF stands for ~~Delhi Land and Finance~~" with the deleted text strikethrough.


### Combined with CSS

CSS can be used alongside the `<del>` tag to customize its appearance:

```html

<style>

  del { color: red; text-decoration: line-through; background-color: lightred; }

</style>

<p>The <del>quick</del> brown fox jumps over the lazy dog.</p>

```

This will produce red, strikethrough text with a light red background.


### Attribute Usage

Both the cite and datetime attributes can be used to provide context about the deleted text:

```html

<p> The project deadline has been changed from <del datetime="2024-01-03T12:00:00Z">January 15, 2024</del> to January 30, 2024. </p>

<p> The following feature was removed: <del datetime="2024-01-05T12:00:00Z" cite="https://www.tutorialspoint.com/index.htm">User authentication via email</del>. </p>

```

These examples demonstrate proper usage of the datetime attribute with a timestamp and the cite attribute with a reference link.


### Block-Level Element Usage

The `<del>` tag can also be used as a block-level element within a document:

```html

<!DOCTYPE html>

<html>

<head>

<style>

  del { color: red; text-decoration: line-through; }

</style>

</head>

<body>

<h2>Deleted Content</h2>

<del>These changes will take effect immediately.</del>

<p>Additional paragraph explaining the change.</p>

</body>

</html>

```

This structure maintains proper document flow while indicating deleted content.


### Nested Usage

The `<del>` tag can be nested within other elements to indicate progressive deletion:

```html

<p>The <del>quick <strong>brown</strong> fox jumps over the lazy dog</del>.</p>

```

This example demonstrates nested elements within the `<del>` tag while maintaining proper structure.


## Best Practices

The `<del>` tag is specifically designed for indicating deleted text within HTML documents, providing both visual styling and semantic meaning. While browsers render deleted text with a strikethrough by default, authors can also achieve this effect through inline CSS styling, demonstrating the element's versatility.


### Semantic Usage and Browser Support

The `<del>` tag is particularly useful for tracking changes or revisions in documents. As noted in the WebReference documentation, it helps highlight altered content, making it valuable for version control scenarios. Modern browsers provide robust support for this element, though specific attribute requirements must be followed for proper functionality.


### Best Practices for Accessibility

To ensure deleted text remains accessible to all users, including those with visual impairments, authors should maintain sufficient color contrast between the text and background. While the default red color provides good visibility, developers can customize this through CSS while ensuring adequate contrast ratios.


### Inclusive Design Considerations

For users who rely on screen readers or other assistive technologies, providing additional context through the cite and datetime attributes significantly enhances the element's utility. The cite attribute should link to a detailed explanation of why text was deleted, while the datetime attribute should clearly specify the deletion time using ISO 8601 format. These metadata elements help maintain document integrity and provide valuable context for all users.

