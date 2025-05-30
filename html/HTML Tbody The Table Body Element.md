---

title: Understanding the HTML `<tbody>` Element

date: 2025-05-29

---


# Understanding the HTML `<tbody>` Element

The `<tbody>` element plays a crucial role in HTML table structure, organizing the main body of data while providing semantic benefits for screen readers and search engines. This article explores the element's functionality, proper usage, and best practices for creating well-structured tables that maintain consistent header and footer content across different viewing contexts.


## What is the `<tbody>` Element?

The `<tbody>` element encloses a set of table rows (TR elements) that represent the main body of the table's data. It follows the `<caption>`, `<colgroup>`, and `<thead>` elements within the table structure. When table rows are direct children of the `<table>` element without nested grouping elements, the browser automatically creates a `<tbody>` element to encapsulate them.

The `<tbody>` element supports various attributes including id, class, lang, dir, title, and style. It can also use event attributes to handle interactions. This element helps browsers correctly interpret table structure and provides semantic information for assistive technologies, including screen readers and search engines.

The `<tbody>` element can contain one or more `<tr>` elements, but must have at least one row. It is required when the table contains multiple table bodies, heads, or feet. When present, each `<tbody>` contains a row group. The element supports deprecated attributes like valign, which specifies the vertical alignment of cells, and char, which specifies the alignment character. The possible values for valign are baseline, bottom, middle, and top.

The `<tbody>` element plays a crucial role in table layout and rendering, particularly in complex table structures where multiple data sections need to be grouped. It allows for independent scrolling of table body sections while maintaining consistent header and footer content. In print contexts, `<thead>` and `<tfoot>` typically contain information that remains consistent across pages, while `<tbody>` content varies per page. The element's structure supports CSS selectors like table > tr, enabling precise styling and layout management.


## How to Use the `<tbody>` Element

The `<tbody>` element must follow `<caption>`, `<colgroup>`, and `<thead>` elements within a table structure. It must contain at least one `<tr>` element and can include multiple rows of data. The element is required when a table contains multiple table bodies, heads, or feet. Each `<tbody>` section contains its own header information typically presented as a single-row `<tr>` with a `<th>` element.

The element's structure enables the creation of distinct data groups within a table, as demonstrated in the example provided by MDN Web Docs. In this example, programming paradigms (object-oriented and procedural) are grouped within separate `<tbody>` sections, each containing its own header row. This structure allows for independent scrolling of table body sections while maintaining consistent header and footer content.

The `<tbody>` element supports various attributes including id, class, lang, dir, title, and style. It can also use event attributes to handle interactions. While these attributes provide semantic information for browsers, assistive technologies, and print functionality, MDN Web Docs notes that several attributes have been deprecated.

The HTML specification allows for multiple `<tbody>` elements within a single table to create row groupings. This functionality enables complex table structures while maintaining browser compatibility and proper document interpretation. The element's placement and usage follow strict guidelines to ensure correct table structure and behavior across different HTML specifications and browser implementations.


## Best Practices and Considerations

Each major should be grouped within its own `<tbody>` block, with the first row serving as the head of the block and displaying the major title within a `<th>` element. This structured grouping enables the creation of distinct data sections within a table, as shown in the example provided by MDN Web Docs.

The `<tbody>` element supports multiple attributes including id, class, lang, dir, title, and style, along with event attributes for interaction handling. However, the HTML specification requires that a table contain only one `<thead>` element, while multiple `<tbody>` elements can be used to create row groupings. There should be no nesting of `<tbody>` elements, as this can lead to unpredictable behavior and incorrect interpretation by browsers.

When implementing multiple `<tbody>` elements, ensure each group contains a distinct section of the table's body. This structured approach enables proper rendering and interpretation by browsers, particularly in scenarios requiring independent scrolling of table body sections while maintaining consistent header and footer content.


## Attributes and Styling

The `<tbody>` element supports a variety of attributes for styling and semantic markup, including id, class, lang, dir, title, and style. It also enables event handling through attributes like onclick, ondblclick, onmousedown, onmouseup, onmouseover, onmousemove, onmouseout, onkeypress, onkeydown, and onkeyup.

Style sheet properties for the `<tbody>` element include background color through bgcolor, though this attribute is deprecated in favor of inline style information. Vertical alignment of cells within the element can be controlled using the valign attribute, with possible values baseline, bottom, middle, and top. The char attribute specifies an alignment character, though this attribute is also deprecated.

The element supports multiple rowspans and colspan values for `<td>` and `<th>` elements. The rowspan attribute specifies the number of rows spanned by a cell, with a default of 1 and a special value of 0 indicating it spans all rows in the table section. Similarly, the colspan attribute specifies the number of columns spanned by a cell, with a default of 1 and a special value of 0 indicating it spans all columns in the column group.

The `<tbody>` element provides semantic value for both screen and print rendering, particularly in complex table structures. For multipage tables, `<thead>` and `<tfoot>` typically contain information that remains consistent across pages, while `<tbody>` content varies per page. In screen contexts, user agents may allow scrolling of `<thead>`, `<tbody>`, `<tfoot>`, and `<caption>` blocks separately from the parent `<table>`.

The element supports CSS styling for various table sections, including `<table>`, `<thead>`, `<th>`, and `<td>` elements with border specifications of 1.5px solid #A569BD. This styling allows for precise control over table appearance while maintaining semantic structure.


## Common Pitfalls and Troubleshooting

Incorrect placement of the `<tbody>` element outside the `<table>` structure can lead to rendering issues, as browsers require it to be a direct child of the `<table>` element. The element should follow any `<caption>`, `<colgroup>`, and `<thead>` elements, and be placed before any `<tfoot>` element.

The `<tbody>` element can appear multiple times within a `<table>` structure to divide table data into distinct sections. This functionality enables the creation of separate row groups, as demonstrated in examples where programming paradigms (object-oriented and procedural) are grouped within distinct `<tbody>` sections.

Nesting `<tbody>` elements is not recommended and can cause unpredictable behavior, as the HTML specification explicitly states that a table can contain only one `<thead>`, one `<tfoot>`, and one `<tbody>` element. This restriction applies to both previous and current HTML specifications, as noted in the official documentation.

When implementing multiple `<tbody>` elements, it's important to avoid placing them after `<tfoot>` elements, as this violates the HTML structure requirements. The correct placement ensures proper rendering and interpretation by browsers, particularly in scenarios where independent scrolling of table body sections is required while maintaining consistent header and footer content.

## References

- [HTML The Footer Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Footer%20Element.md)
- [HTML br The Line Break Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20br%20The%20Line%20Break%20Element.md)
- [HTML Class](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Class.md)
- [HTML h1 h6 The HTML Section Heading Elements](https://github.com/serpuniversity/learn/blob/main/html/HTML%20h1%20h6%20The%20HTML%20Section%20Heading%20Elements.md)
- [HTML s The Strikethrough Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20s%20The%20Strikethrough%20Element.md)