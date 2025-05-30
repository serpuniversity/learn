---

title: HTML `<thead>`: The Table Head Element

date: 2025-05-29

---


# HTML `<thead>`: The Table Head Element

The `<thead>` element plays a crucial role in HTML tables by providing semantic structure for headers. Unlike its unnamed predecessor, `<thead>` specifically designates table headers through a structured approach that enhances accessibility and styling. This article explores `<thead>`'s capabilities, from basic implementation to advanced features like rowgroup headers and multi-row headers, while highlighting its importance in creating well-organized and accessible table structures.


## Overview

The `<thead>` element is designed specifically for table headers and must contain one or more `<tr>` elements (table rows). These rows typically house `<th>` (table header) elements, which provide semantic structure for the table's columns.


### Element Attributes

The `<thead>` element supports several attributes, though many are deprecated:

- **align**: Specifies horizontal alignment of cell content, though it's generally recommended to use CSS for this purpose.

- **char**: Defines the alignment character for the cell content.

- **charoff**: A deprecated attribute that originally intended to specify character offset from the alignment character; it serves no function in modern usage.

- **valign**: Specifies vertical alignment of cell content, with possible values including baseline, bottom, middle, and top. This attribute is similarly deprecated in favor of CSS's vertical-align property.


### Content Structure

The `<thead>` element should appear after any `<caption>` or `<colgroup>` elements and before `<tbody>`, `<tfoot>`, or `<tr>` elements. While it's possible to place `<thead>` content directly between `<table>` tags, explicitly enclosing it in `<thead>` tags enhances semantic clarity and accessibility.


### Browser Support

All modern browsers fully support the `<thead>` element, allowing developers to create well-structured tables that can be effectively interpreted by both humans and machines. The element's basic functionality requires no additional libraries or plugins. Its implementation is consistent across multiple browser versions, making it a reliable choice for web development projects.


## Structure and Usage

The `<thead>` element is positioned after any `<caption>` or `<colgroup>` elements and before `<tbody>`, `<tfoot>`, or `<tr>` elements, establishing clear semantic structure for the table. A basic table structure incorporating `<thead>` might look like this:

```html

<table>

  <caption>Basic Table Example</caption>

  <colgroup>

    <col />

    <col />

  </colgroup>

  <thead>

    <tr><th>Column 1</th><th>Column 2</th></tr>

  </thead>

  <tbody>

    <tr><td>Data 1</td><td>Data 2</td></tr>

    <tr><td>Data 3</td><td>Data 4</td></tr>

  </tbody>

</table>

```

This structure allows for multiple rows within the `<thead>` element, as demonstrated in this enhanced table structure:

```html

<table>

  <caption>Table with Multiple Header Rows</caption>

  <colgroup>

    <col />

    <col />

    <col />

  </colgroup>

  <thead>

    <tr><th>Column 1</th><th>Column 2</th><th>Column 3</th></tr>

    <tr><th scope="rowgroup">First Name</th><th scope="rowgroup">Last Name</th><th>Additional Info</th></tr>

  </thead>

  <tbody>

    <tr><td>John</td><td>Doe</td><td>John Doe</td></tr>

    <tr><td>Jane</td><td>Roe</td><td>Jane Roe</td></tr>

  </tbody>

</table>

```

The `<thead>` element's display property defaults to table-header-group, enabling consistent styling across different browsers. While the align, char, charoff, and valign attributes are supported, they're deprecated and should be replaced with CSS for proper styling.


## Supported Content

The `<thead>` element requires at least one `<tr>` element to function. It can contain multiple `<tr>` elements, allowing for complex header structures. Each `<tr>` element within `<thead>` should contain at least one `<th>` element, which defines header information for the table's columns.


### Attributes and Support

The `<thead>` element supports various attributes, though many are deprecated. The following attributes are supported:

- **align**: Specifies horizontal alignment of cell content. This attribute should be used with caution, as it is generally recommended to use CSS for positioning.

- **char**: Sets the alignment of content inside `<thead>` to a specific character. This attribute can help orient content within cells when using character-based alignment.

- **charoff**: A deprecated attribute that originally intended to specify character offset from the alignment character. It serves no function in modern usage.

- **valign**: Specifies vertical alignment of cell content. Possible values include baseline, bottom, middle, and top. Similar to align, this attribute is deprecated and should be replaced with CSS's vertical-align property.


### Advanced Features

The `<thead>` element can use the headers and scope attributes to help assistive technologies process header information. Specifically:

- **headers**: This attribute allows authors to associate header cells with specific data cells. It accepts a comma-separated list of header cell identifiers.

- **scope**: Defines the scope of a header cell. Possible values include "row" (default for TH elements), "col", "rowgroup", and "colgroup". This attribute helps user agents understand the relationship between header cells and data cells.


### Browser Support

The `<thead>` element is fully supported by all modern browsers and can be effectively utilized in various table structures. While the element's basic functionality requires no additional libraries or plugins, developers may choose to use CSS for improved styling and layout control.


##  Styling and Layout

The `<thead>` element's default display property is table-header-group, providing consistent styling across different browsers. It is typically rendered with vertical-align: middle, border-color: inherit, and a display property of table-header-group.

According to the HTML5 specification, the `<thead>` element may have a start tag and its end tag may be omitted if immediately followed by a tbody or tfoot element. Its permitted parent element is table, and it contains zero or more tr elements.

When styling `<thead>` elements, developers can use CSS to modify their appearance and layout. The provided examples demonstrate how to achieve specific alignments, such as vertical-align: bottom for a tr element with height: 100px. For comprehensive styling, developers can use rulesets like:

table, th, td {

  border: 1px solid black;

  border-collapse: collapse;

}

table {

  margin-left: auto;

  margin-right: auto;

}

th, td {

  padding: 10px;

}

The specification allows for at most one `<thead>` and one `<tfoot>` element per table. For additional headers, developers can use `<th scope=rowgroup>` within regular `<tr>` elements, as specified in the HTML standard. This approach enables flexibility in table structure while maintaining semantic clarity.


## Browser Support

The `<thead>` element's broad compatibility across browsers enables developers to implement consistent table structures in modern web development projects. As outlined in the HTML5 specification, the element requires both opening and closing tags and can serve as a child of any flow content container.

Modern browsers fully implement the element's core functionality without requiring additional libraries or plugins. The `<thead>` tag's behavior aligns with the broader table structure rules: it can appear after `<caption>` and `<colgroup>` elements but before `<tbody>`, `<tfoot>`, or individual `<tr>` elements.

The typical use case involves placing `<thead>` content between `<table>` tags, though its most effective use stems from being explicitly defined. This approach enhances semantic clarity for both human readers and assistive technologies.

The latest browser versions maintain consistent behavior with the element's default display property of table-header-group. Some developers may still employ deprecated attributes like align, char, charoff, and valign; however, the W3C recommends these be replaced with appropriate CSS properties for alignment and styling.

