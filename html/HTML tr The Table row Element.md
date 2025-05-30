---

title: HTML Tr: The Table Row Element

date: 2025-05-29

---


# HTML Tr: The Table Row Element

The `<tr>` element, or table row, is a fundamental building block of HTML tables, organizing data into manageable rows that can span multiple columns through advanced attributes. This comprehensive guide explores the technical structure of `<tr>`, its compliant usage within table sections, and the modern CSS approaches that have replaced many of its traditional styling capabilities.


## Defining Table Rows

The `<tr>` element is a fundamental building block for HTML tables, used to define individual rows of data. Each `<tr>` element must contain one or more `<td>` (table data) or `<th>` (table header) elements, though it can include both header and data cells within the same row.

A `<tr>` element must be a direct child of either `<thead>`, `<tbody>`, or `<tfoot>` elements, following the structure defined in HTML specifications. The `<tr>` element serves as the parent for `<td>` and `<th>` elements, with a typical default display property of "table-row."

The table structure consists of `<colgroup>` elements followed by an optional `<thead>` section, which can contain zero or more `<tr>` elements. Below the `<thead>`, table rows may be represented by one or more `<tbody>` elements or additional `<tr>` elements. An optional `<tfoot>` section follows these elements, containing its own `<tr>` rows.

While the `<tr>` element supports global attributes and has an implicit ARIA role of "row," it has largely transitioned from using alignment and background color attributes toward CSS for styling purposes. Modern web development practices recommend employing CSS properties like text-align, background-color, and vertical-align instead of the deprecated align, bgcolor, char, charoff, and valign attributes.


## Element Structure and Compliance

The `<tr>` element is a crucial component of HTML table structures, serving as the foundation for organizing rows of data. Each `<tr>` element must contain either `<td>` (table data) or `<th>` (table header) elements, though it can nest both types within the same row.

The `<tr>` element follows strict parent-child relationships, residing directly within `<thead>`, `<tbody>`, or `<tfoot>` elements. This nesting structure enables semantic organization of table content, with `<thead>` for header rows, `<tbody>` for body rows, and `<tfoot>` for footer rows.

The element's structure supports multiple `<td>` or `<th>` cells, each representing a cell in the row. These cells can span multiple columns using the colspan attribute or multiple rows with the rowspan attribute, though these deprecated attributes are recommended for CSS replacement. Modern best practices prioritize CSS for layout and styling.

Each `<tr>` element can include standard HTML attributes, such as id, class, lang, dir, and title, as well as event handlers like onclick, ondblclick, and onmouseover. However, certain attributes have been deprecated in favor of CSS, including align, bgcolor, char, charoff, and valign. Supported properties now include text-align, background-color, and vertical-align, offering greater control over cell content presentation.


## RowSpan and ColSpan

The `<tr>` element's child cells can use rowspan and colspan attributes for complex row spanning and column spanning. These attributes allow cells to extend across multiple rows and columns, though they have been deprecated in favor of modern CSS techniques for similar functionality.

The rowspan attribute specifies the number of rows the cell should span, defaulting to 1 if not specified (or using zero to span from the current row to the last row of the current table section). This attribute enables cells to vertically span multiple rows, while the colspan attribute serves a similar purpose horizontally, allowing cells to span multiple columns. The attribute value of zero for either property spans to the last column or row of the respective section (thead, tbody, tfoot).

For example, consider this table structure:

|   | ID | Name | Age |

|---|---|---|---|

| **Header** | 101 | Alice | 30 |

| | 102 | Bob | 25 |

| | 103 | Charlie | 35 |

The *Header* row uses `<th>` elements to define column headers. To merge the ID and Name columns into a single header, this structure would change to:

|   | ID/Name | Age |

|---|---|---|

| **Header** | ID/Name | Age |

| | 101 | Alice | 30 |

| | 102 | Bob | 25 |

| | 103 | Charlie | 35 |

In this revised structure, the *Header* row utilizes colspan to combine the ID and Name columns into a single header cell.

Similarly, the rowspan attribute allows cells to span multiple rows. For instance, in the same table, to display a summary row above the actual data:

|   | ID/Name | Age | Summary |

|---|---|---|---|

| **Summary** | Average Age: 
30.0 | | |

| **Header** | ID/Name | Age | Summary |

| | 101 | Alice | 30 |

| | 102 | Bob | 25 |

| | 103 | Charlie | 35 |

Here, the Summary row uses rowspan to create vertical space between the header and data rows.

While historically these attributes controlled alignment and background color through attributes like align and bgcolor, modern web development recommends using CSS properties such as text-align, background-color, and vertical-align for layout and styling, maintaining semantic and accessible table structures.


## CSS Support and Deprecated Attributes

The `<tr>` element supports several global attributes, including id, class, lang, dir, and title, as well as event handlers like onclick and onmouseover. However, multiple attributes have been deprecated in favor of modern CSS properties:

The align attribute controls horizontal cell alignment, accepting values like left, right, center, and justify. In cases where char alignment is specified, the charoff attribute determines the character offset from the alignment character. These attributes are now replaced by the text-align property in CSS.

The bgcolor attribute sets the background color of each row cell, accepting HTML color values such as 6-digit hexadecimal RGB codes or color keywords (prefixed with #). While CSS `<color>` values are supported, developers are directed to use the background-color property instead.

The char attribute determines content alignment to a specific character, typically period (.) for numerical or monetary values. When align is not set to char, this attribute has no effect. The charoff attribute further specifies character offset from the alignment character, functionality now managed by CSS.

Additional deprecated attributes include accesskey, colspan, headers, rowspan, and usemap. The element's implicit ARIA role remains "row," facilitating accessible table structures while modern CSS properties like text-align, background-color, and vertical-align provide enhanced layout and styling capabilities.


## Row-Based Table Structuring

The HTML table row structure prioritizes rows over columns for vertical alignment, with user agents determining default cell alignment based on directionality. The default cell alignment depends on the user agent, with exceptions for directionality inheritance.

The table structure divides into three main sections: table head (thead), table foot (tfoot), and table body (tbody). Each section contains row groups defined by the tr element, with the tfoot element appearing before tbody within a table definition to allow user agents to render the foot before receiving all data rows.

For visual rendering, the HTML specification recommends a 1-pixel border for table, header, and data cells, with merged adjacent cell borders through CSS's border-collapse: collapse property. Cell padding adds visual separation within cells.

User agents determine default attributes based on directionality, substituting "left" with appropriate values. TD and TH elements inherit attributes from the first cell in a span, and non-visual user agents use these elements' attributes for intuitive rendering. The headers attribute lists header cells for pertinent data cells, with each header cell named using the id attribute.

The TABLE element's cellspacing attribute specifies space between table edges, columns/rows, and cells, while cellpadding controls cell content margins at 20% of available vertical space for top/bottom and 20% of available horizontal space for left/right. These attributes may conflict with fixed-width table widths, with user agents prioritizing cellspacing and cellpadding over width.

The HTMLTableRowElement interface provides access to row properties and methods, supported by several CSS properties for background color, border, text alignment, and vertical alignment of cell content. Pseudo-classes :nth-of-type, :first-of-type, and :last-of-type enable selecting specific row cells.

