---

title: HTML `<tfoot>`: The Table Foot Element

date: 2025-05-29

---


# HTML `<tfoot>`: The Table Foot Element

The `<tfoot>` tag in HTML defines the footer section of a table, providing a structured way to display summary information or footnotes alongside `<thead>` (table header) and `<tbody>` (table body) elements. This introduction will explore the tag's basic structure, common use cases, browser compatibility, content styling options, and advanced usage considerations to help developers effectively implement and optimize table footers in their web applications.


## Basic Structure and Usage

The `<tfoot>` tag defines the footer section of an HTML table, working in conjunction with `<thead>` and `<tbody>` tags to structure table content. This element must contain one or more `<tr>` tags and appears after any `<caption>`, `<colgroup>`, `<thead>`, and `<tbody>` elements within a table.

Common use cases for `<tfoot>` include displaying summary information or footnotes, such as total values or explanatory notes. For example, in a financial report table, the `<tfoot>` might contain the net profit figure or additional text explaining the data presented. The `<tfoot>` tag supports several attributes for basic styling, though these are deprecated in HTML5 and should be replaced with CSS for proper text alignment and vertical positioning.

To demonstrate correct implementation, consider a simple table showing student grades:

`<table>`

`<thead>`

`<tr>`

`<th>`Student`</th>`

`<th>`Subject`</th>`

`<th>`Grade`</th>`

`</tr>`

`</thead>`

`<tbody>`

`<tr>`

`<td>`John Doe`</td>`

`<td>`Math`</td>`

`<td>`90`</td>`

`</tr>`

`<tr>`

`<td>`Jane Smith`</td>`

`<td>`Science`</td>`

`<td>`85`</td>`

`</tr>`

`<tr>`

`<td>`David Johnson`</td>`

`<td>`History`</td>`

`<td>`92`</td>`

`</tr>`

`</tbody>`

`<tfoot>`

`<tr>`

`<td colspan="2">`Average Grade:`</td>`

`<td>`89`</td>`

`</tr>`

`</tfoot>`

`</table>`

In this example, the `<tfoot>` tag contains a single row with a colspan attribute spanning the first two columns to display the "Average Grade:" text. The actual average grade value is shown in the third column. This structure allows for clear visual separation between the table body data and the summary information, enhancing both visual appeal and readability of the table.


## Browser Compatibility

The `<tfoot>` element is supported across modern browsers including Chrome, Edge, Firefox, Safari, and Opera. It functions as a child of the `<table>` element, appearing after `<caption>`, `<colgroup>`, `<thead>`, and `<tbody>` sections. Each `<tfoot>` element must contain one or more `<tr>` tags and can include attributes for text alignment (align), vertical positioning (valign), character alignment (char), and character offset (charoff). However, these deprecated attributes should be replaced with CSS for proper styling.

The element's structure enables advanced table features like independent scrolling of the table body, header, and footer. When printing tables that span multiple pages, `<tfoot>` facilitates the consistent display of headers and footers at the top and bottom of each page. Common use cases include displaying summary information, such as total values or explanatory notes, making it particularly useful for financial reports or data summaries.


## Content and Styling

The `<tfoot>` element supports several styling attributes, though these are deprecated in HTML5 and should be replaced with CSS for proper text alignment and vertical positioning. The available attributes include:

- align: Sets the alignment of text content (left, center, right, justify, char)

- valign: Sets the vertical alignment of text content

- char: Aligns content in a header cell to a specific character

- charoff: Sets the number of characters aligned with the character specified by the char attribute

For example, the following CSS styles demonstrate typical `<tfoot>` formatting:

```css

tfoot {

    border-top: 3px dotted rgb(160 160 160);

    background-color: #2c5e77;

    color: #fff;

    text-align: right; /* for table header cells */

    font-weight: bold; /* for table data cells */

    border-bottom: 2px solid rgb(160 160 160);

    background-color: #2c5e77;

    color: #fff;

    border-collapse: collapse;

    border: 2px solid rgb(140 140 140);

    font-family: sans-serif;

    font-size: 
0.8rem;

    letter-spacing: 1px;

}

tfoot td:last-child {

    text-align: center;

}

```

The `<tfoot>` element must contain one or more `<tr>` tags and appears after the `<caption>`, `<colgroup>`, `<thead>`, and `<tbody>` elements in a table. While the start tag is mandatory, the end tag may be omitted if no further content follows in the parent `<table>` element. This structure enables advanced table features like independent scrolling of the table body, header, and footer, particularly useful for large tables spanning multiple pages. The footer content will consistently appear at the bottom of each page during printing.


## Table Model and Semantics

According to the HTML specification, the `<tfoot>` element represents the table footer, containing rows that typically display summary information or footnotes. It plays a crucial role in the table model by allowing user agents to render the footer before receiving all the data rows, which enables more efficient rendering and better performance for large tables.

The element must appear after any `<caption>`, `<colgroup>`, `<thead>`, and `<tbody>` elements within a TABLE definition. This placement requirement ensures proper rendering of table sections, particularly for complex tables where header and footer information needs to be distinguished from the main body of data. The specification allows the `<tfoot>` end tag to be omitted if no additional content follows in the parent TABLE element, providing flexibility in table structure definition.

In terms of positioning, the `<tfoot>` element's `<tr>` elements are distinguished from table body cells through specific CSS styling properties. These properties include a border-top of 3px dotted rgb(160 160 160), background color of #2c5e77, and text color of #fff. The specification notes that this structure enables both semantic and presentational benefits, improving table accessibility and print formatting capabilities.


## Advanced Usage and Best Practices

To ensure the footer appears only at the end of the table on the last page, developers can use CSS display properties or client-side scripting. The `<tfoot>` tag should always contain `<tr>` elements and appear after the table's header and body sections.


### CSS Display Properties

Setting `tfoot { display: table-row-group }` removes the repeated behavior that causes the footer to display at the end of each page. However, this places the `<tfoot>` at the start of the table, before normal rows, according to HTML 4 syntax. The browser's default `display: table-footer-group` property causes the footer to appear after any other rows and may be repeated at the end of each page if the browser wants to do that.


### Client-Side Scripting

A more flexible approach uses JavaScript to manipulate the `<tfoot>` element's position. This requires the table element to have an `id` attribute, such as `id=tbl`. The process involves finding the `<tfoot>` element, setting its display property to `table-row-group`, removing it from the table, and appending it back. This method ensures the footer appears only at the end of the table on the last printed page.


### Historical Context

In HTML4, the `<tfoot>` element's placement had different requirements. It could not be placed after `<tbody>` and `<tr>` elements, though the specification has since evolved to allow this for better table rendering and printing capabilities. The element's structure enables advanced table features like independent scrolling of the table body, header, and footer, particularly useful for large tables spanning multiple pages.

## References

- [HTML Itemtype](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Itemtype.md)
- [HTML li The List Item Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20li%20The%20List%20Item%20Element.md)
- [HTML The Textarea Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Textarea%20Element.md)
- [HTML The Footer Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Footer%20Element.md)
- [HTML Attribute rel](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20rel.md)