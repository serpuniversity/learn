---

title: HTML `<td>` Element: Table Data Cells

date: 2025-05-29

---


# HTML `<td>` Element: Table Data Cells

The `<td>` element is a fundamental building block of HTML tables, representing standard data cells that contain tabular information. This article explores the basic usage and structure of `<td>` elements, showcasing how they form the backbone of any table structure through nested rows and columns. We'll examine advanced techniques like row and column spanning, which enable more complex table layouts. The article also delves into the default display properties of `<td>` elements and how they interact with other table elements. Through practical examples, we'll demonstrate how to effectively utilize `<td>` attributes for better accessibility and structure.


## Basic Usage and Structure

The `<td>` element represents a standard data cell in an HTML table, contrasting with header cells defined by the `<th>` element. It is used to contain tabular data within the structure of `<table>` elements.


### Basic Structure

A table consists of table cells nested within rows and columns. Each table cell is defined using the `<td>` and `</td>` tags, where "td" stands for table data. The content for a table cell appears between these tags.


### Row Spanning and Column Spanning

The `<td>` element supports two attributes for spanning multiple cells:

- `colspan` specifies the number of columns the cell should span (default is 1, 0 spans all columns)

- `rowspan` specifies the number of rows the cell should span (default is 1, 0 spans all rows)


### Header Information and Relationships

While `<td>` elements contain the actual data, tables can include header information for better accessibility and structure. This is typically done using `<th>` elements, which can appear anywhere within `<tbody>` for header information, not just in `<thead>`. To programmatically associate table cells with their corresponding header cells, developers should use the combination of the `id` attribute and the `headers` attribute.


### Default Display Properties

By default, `<td>` elements display as table cells with left-alignment. These elements will have a display property of `table-cell`, vertical-align set to inherit, and will inherit background and border properties from their parent elements. Cell content is left-aligned unless explicitly styled otherwise.


### Example Structure

A basic table structure might look like this:

```html

<table>

  <tr>

    <th>Header</th>

    <th>Header 2</th>

  </tr>

  <tr>

    <td>Data</td>

    <td>Data 2</td>

  </tr>

  <tr>

    <td>RowSpanningData</td>

    <td></td>

  </tr>

</table>

```

In this example, the first row contains header information defined with `<th>` elements, while the subsequent rows define data cells using `<td>`. The third row demonstrates a `<td>` element spanning multiple rows using the `rowspan` attribute.


## Cell Spanning Attributes

The colspan attribute allows a cell to span multiple columns, while the rowspan attribute enables a cell to span multiple rows. These attributes can be applied to both `<td>` and `<th>` elements, though their primary functionality is demonstrated through `<td>` examples.

When the colspan attribute is set to 2, a cell occupies the space of two adjacent columns, as shown in the following structure:

```html

<th colspan="2">Name</th>

<th>Class</th>

```

This creates a combined cell spanning two columns in the header row.

Similarly, the rowspan attribute allows a cell to span multiple rows. For example, when set to 2 in a `<td>` element, it causes the row below to have one less cell:

```html

<td rowspan="2">Mahima</td>

<td rowspan="2">Gupta</td>

<td>11</td>

<td rowspan="2">MVM School</td>

```

This structure creates merged cells spanning two rows.

The HTML Table Colspan attribute allows merging or combining adjacent table cells horizontally, creating a single, wider cell that spans across multiple columns. The example demonstrates this functionality through the following HTML structure:

```html

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>HTML Table with Colspan</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>HTML Table</title>

    <style>

        h1, h3 { text-align: center; color: green; }

        table { width: 100%; border: 1px solid #100808; border-collapse: collapse; }

        th, td { padding: 10px; border: 2px solid black; }

    </style>

</head>

<body>

    <h1>GeeksforGeeks</h1>

    <h3>Table with Colspan </h3>

    <table>

        <thead>

            <tr>

                <th colspan="2">Name</th>

                <th>Class</th>

            </tr>

        </thead>

        <tbody>

            <tr>

                <td>Mahima</td>

                <td>Gupta</td>

                <td>1</td>

            </tr>

            <tr>

                <td>Sri</td>

                <td>Krishn</td>

                <td>3</td>

            </tr>

            <tr>

                <td>Shivika</td>

                <td>Goyal</td>

                <td>5</td>

            </tr>

        </tbody>

    </table>

</body>

</html>

```

The output shows the merged cells spanning multiple columns:

![tc](https://media.geeksforgeeks.org/wp-content/uploads/20240116113917/tc.png)

The HTML Table with Rowspan determines how many rows a specific cell in a table should cover. When a cell spans multiple rows, it occupies the space of those rows within the table. The rowspan attribute is applied within a `<td>` or `<th>` element. The example demonstrates this functionality through the following HTML structure:

```html

<!DOCTYPE html>

<html>

<head>

    <title>HTML rowspan</title>

    <style>

        body { display: flex; flex-direction: column; justify-content: center; align-items: center; }

        h1 { color: green; }

        table { width: 70%; }

        table, th, td { border: 1px solid black; border-collapse: collapse; padding: 6px; }

    </style>

</head>

<body>

    <h1>GeeksforGeeks</h1>

    <h2>HTML Table Rowspan</h2>

    <table>

        <tr>

            <th>Name</th>

            <th>Class</th>

            <th rowspan="3">MVM School</th>

        </tr>

        <tr>

            <td>Radha</td>

            <td>10</td>

        </tr>

        <tr>

            <td>Ankur</td>

            <td>11</td>

        </tr>

    </table>

</body>

</html>

```

The output shows the merged cells spanning multiple rows:

![tablerowspan](https://media.geeksforgeeks.org/wp-content/uploads/20240116120029/tablerowspan.png)

The Table with Rowspan and Colspan Together helps in creating more complex and structured tables by utilizing both attributes to merge cells both horizontally and vertically.


## Styling and Display Properties

The `<td>` element defines table data cells, with default properties set by most browsers. The HTML TD element has specific alignment preferences: rows take precedence over columns, meaning horizontal alignment is determined by columns while vertical alignment prioritizes rows. Default text alignment generally follows the user agent's settings, with left-to-right texts offsetting from the left margin and right-to-left texts from the right margin.

The element supports several CSS properties for customization, including:

- vertical-align, which accepts baseline, sub, super, text-top, text-bottom, middle, top, bottom, %, and length values

- white-space, with normal, pre, nowrap, pre-wrap, and pre-line options

- border-collapse, supporting collapse and separate modes

- border-spacing, defining the distance between cells

- width, for setting cell dimensions

- border, specifying cell borders

Some notable behaviors include:

- In collapsed border environments (default), cells share a single border width

- Cell backgrounds appear due to stacking order, not specific td styling

- Text direction offsets align with current directionality, though user agents may not support this attribute

- Width properties override table-level styles in conflicts, with columns determining allocation

Additional behavior to note includes:

- Horizontal alignment characters are determined by columns over rows

- Vertical alignment characters prioritize rows over columns

- Default alignment varies by user agent, requiring substitution when needed

- Multiple alignment characters within content may produce undefined behavior


## Header and Data Relationships

To programmatically associate table cells with their corresponding header cells, developers should use the combination of the `id` attribute and the `headers` attribute. Each row header cell associated with a data cell is given a unique identifier with the `id` attribute, while the data cell uses these `id` values in a space-separated list for the `headers` attribute.

In practice, this implementation improves accessibility by providing clear relationships between header and data cells. For example, consider the following table structure:

```html

<table>

  <tr>

    <th id="a" scope="row">A</th>

    <td>Alfa</td>

    <td>AL fah</td>

    <td headers="a b c" rowspan="3">ABC</td>

  </tr>

  <tr>

    <th id="b" scope="row">B</th>

    <td>Bravo</td>

    <td>BRAH voh</td>

  </tr>

  <tr>

    <th id="c" scope="row">C</th>

    <td>Charlie</td>

    <td>CHAR lee</td>

  </tr>

  <tr>

    <th scope="row">D</th>

    <td>Delta</td>

    <td colspan="2">DELL tah</td>

  </tr>

  <tr>

    <th scope="row">E</th>

    <td>Echo</td>

    <td colspan="2">ECK oh</td>

  </tr>

</table>

```

This implementation maintains the same visual presentation while establishing explicit relationships between header and data cells. The `id` attribute uniquely identifies each row header cell (A, B, C, D, E), while the `headers` attribute in the data cells specifies which header cells relate to them (ABC cell spans three rows, referencing all header cells).


## Browser Support and Standards

The `<td>` element has demonstrated consistent browser support across all major browsers since its introduction into HTML standards. This universal compatibility ensures that developers' table structures remain accessible and functional across different platforms and environments.

Browser implementation aligns with the specification that `<td>` elements fall under the global attributes category, which includes standard attributes and event attributes. While the documents do not explicitly list these attributes, their omission suggests they follow the established pattern for HTML elements.

For developers implementing table structures, understanding these underlying browser capabilities ensures reliable cross-browser functionality. The consistent support across browsers allows for standardized development practices without the need for browser-specific workarounds.

