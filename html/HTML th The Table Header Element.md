---

title: `<th>`: The Table Header Element

date: 2025-05-29

---


# `<th>`: The Table Header Element

The `<th>` element plays a crucial role in HTML table structures by defining header cells that provide essential context for tabular data. This article explores the technical specifications of `<th>` elements, including their allowed content, required attributes, and basic structure. We'll examine how this element supports accessibility through attributes like abbr, colspan, headers, and rowspan while maintaining proper document hierarchy. The discussion will also cover best practices for styling `<th>` elements using CSS, ensuring both visual appeal and clear semantic meaning in table structures.


## Element Structure and Content

The `<th>` element must contain flow content but cannot include header, footer, sectioning content, or heading content descendants. It supports several attributes to enhance functionality and accessibility, including abbr, colspan, headers, rowspan, and scope.


### Attributes and Their Usage

The abbr attribute provides an abbreviated version of the header content, which is particularly useful for screen readers. The colspan attribute allows a single `<th>` to span multiple columns, while the headers attribute links a `<th>` to one or more `<td>` elements, helping assistive technologies understand cell relationships.

The rowspan attribute enables a single `<th>` to span multiple rows, and the scope attribute clarifies whether the header applies to a column, row, row group, or column group. These attributes help screen readers and other assistive technologies interpret the table structure accurately.


### Basic Structure Requirements

The `<th>` element must be placed within a `<tr>` element and can only be immediately followed by `<th>` or `<td>` elements. If no more content follows within the parent element, both start and end tags are mandatory. This structure helps maintain the logical flow of table content and ensures proper rendering across different devices and screen sizes.


### Default Display Properties

By default, browsers render text within `<th>` elements with bold font weight and centered alignment. These default styles help draw attention to the header cells and improve visual hierarchy within the table. While these default properties enhance readability, developers should consider overriding them with CSS to maintain accessibility standards and visual consistency across various devices and screen sizes.


## Element Usage and Placement

The `<th>` element should be placed within a `<tr>` element and can only be immediately followed by `<th>` or `<td>` elements. If no more content follows within the parent element, both start and end tags are mandatory. This structure helps maintain the logical flow of table content and ensures proper rendering across different devices and screen sizes.

The `<th>` element is a crucial component of tabular data, serving to define header cells in a table structure. These cells typically contain titles for each column or row and help users understand the organization of the table data. The `<th>` element should be used within a `<tr>` (table row) element to create headers, while `<td>` (table data) elements contain the actual cell content.

The `<th>` element supports several attributes to enhance functionality and accessibility, including scope, colspan, headers, and rowspan. The scope attribute indicates the relationship between header cells and data cells, with possible values of col (column), row (row), colgroup (group of columns), and rowgroup (group of rows). The colspan attribute allows a single `<th>` to span multiple columns, while the headers attribute links a `<th>` to one or more `<td>` elements for better assistive technology support. The rowspan attribute enables a single `<th>` to span multiple rows, providing flexibility in table cell placement.

For example, consider the following HTML structure:

```html

<table>

  <tr>

    <th scope="col">Name</th>

    <th scope="col" colspan="2">Location</th>

  </tr>

  <tr>

    <td>John Doe</td>

    <td>New York</td>

    <td>USA</td>

  </tr>

</table>

```

In this structure, the first column header spans two columns using the colspan attribute, while the second column header maintains its default single-column span. The scope attribute on the first header cell clearly indicates its relationship to the data cells in the same column, improving accessibility for screen readers and other assistive technologies.


## Accessibility and ARIA Roles

Web developers must balance aesthetic considerations with accessibility needs when working with table headers. Using color alone to distinguish header cells from data cells may not suffice for users with color blindness, and setting small font sizes for stylistic reasons can make text difficult to read for users with low vision.

To address these tradeoffs, developers should adhere to web accessibility standards like the Web Content Accessibility Guidelines (WCAG). These guidelines recommend sufficient contrast between text and background colors, using legible font sizes, and providing alternative ways to convey information. When restructuring tables for smaller screens, designers must ensure that headers and data cells remain legible and accessible.

Accessibility requirements dictate that screen readers rely on `<th>` elements to announce column and row headers and use the `scope` attribute to specify header relationships. For complex tables, the `id` and `headers` attributes enable direct linking between data cells and header cells. The typical default display properties for `<th>` elements include bold font weight and centered alignment, which can be customized with CSS while maintaining accessibility standards.


## Default Styling and Browser Compatibility

While the specific browser compatibility details are not provided in the documentation, the structure and content requirements for the `<th>` element remain consistent across browsers. The element must contain flow content without header, footer, sectioning content, or heading content descendants, with start and end tags required unless immediately followed by `<th>` or `<td>` elements or no more data in the parent element.

The element's placement within table structures follows these rules:

- It must be placed within a `<tr>` element

- May only be immediately followed by `<th>` or `<td>` elements

- Both start and end tags are mandatory unless no more content follows within the parent element

The `<th>` element's default display properties, typically applied by browsers, consist of:

- display: table-cell

- vertical-align: inherit

- font-weight: bold

- text-align: center

These default styles help draw attention to the header cells and improve visual hierarchy within the table. Modern browsers consistently render text within `<th>` elements in bold and centered alignment, while data cells remain regular in font weight and left-aligned.

For developers implementing `<th>` elements, adherence to these basic structure requirements and default styling expectations ensures consistent table rendering across contemporary browsers and devices. The element's primary function remains defining header cells in table structures, where its bold font weight and centered alignment enhance readability and visual organization for both sighted and screen reader users.


## CSS Properties and Customization

The basic `<th>` element structure requires content that meets flow content requirements while excluding certain non-flow content types. To style these header cells effectively, developers have access to several CSS properties that influence both presentation and accessibility.


### Basic Styling

The most common default styling for `<th>` elements includes bold font weight and centered alignment, achieved through the browser's built-in display properties. These properties help distinguish header cells visually and aid screen readers in interpreting the table structure. For example:

```css

th {

  display: table-cell;

  vertical-align: inherit;

  font-weight: bold;

  text-align: center;

}

```


### Background and Border Styling

Developers can enhance the visual hierarchy of tables by customizing background colors and borders. For instance, the following CSS sets a distinctive background color and border style for header cells:

```css

th {

  background-color: #4CAF50; /* Green background */

  color: white; /* White text */

  font-size: 1em; /* Relative font size for accessibility */

  border-bottom: 2px solid #8B8B8B; /* Gray border */

}

```


### Column and Row Styling

For complex tables with multiple header levels, targeted styling allows differentiation between columns and rows. The MDN documentation demonstrates this approach through specific classes and IDs:

```css


#join-confirmed th {

  background-color: #2E8B57; /* Dark green for "Joined" column */

}


#join-confirmed th.cancel {

  background-color: #FFA07A; /* Light orange for "Canceled" column */

}


#join-details th {

  background-color: #E1E5F4; /* Light blue for "Date" column */

}

```


### Text Alignment

Text alignment options allow precise control over how header content is displayed. Common values include `left`, `right`, and `center`, with relative unit font sizes recommended for better accessibility:

```css

td.left-align {

  text-align: left;

}

td.right-align {

  text-align: right;

}

td.center-align {

  text-align: center;

}

```


### Border Control

The border attribute, though deprecated, offers basic control over table boundaries through CSS properties:

```css

table {

  border-collapse: collapse; /* Ensure borders are continuous */

}

th, td {

  border: 1px solid #CCCCCC; /* Gray border */

  padding: 
0.5em; /* Sufficient padding for readability */

}

```


### Advanced Visual Formatting

CSS2 introduced extensive properties for table visual formatting, allowing detailed customization of frame and rules attributes:

```css

table { border-collapse: separate; }

th { border: 1px solid #AAAAAA; }

th.thead-first { border-left: none; /* Customize cell borders */ }

th.thead-first, td.thead-first { border-top: none; }

th.thead-last, td.thead-last { border-bottom: none; }

th.thead-last { border-right: none; }

```

By understanding and applying these CSS properties, developers can create visually appealing and accessible table headers that enhance both user experience and document accessibility.

