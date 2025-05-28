---

title: CSS List: Styling and Display Options

date: 2025-05-26

---


# CSS List: Styling and Display Options

CSS lists provide a powerful way to organize content on web pages, offering both semantic structure and flexible styling options. This article explores the fundamentals of CSS lists, from basic unordered and ordered lists to more advanced features like nested structures, custom styling, and specialized numbering options. You'll learn how to control every aspect of list presentation, from marker types and positioning to image-based markers and custom counting sequences. The examples and demonstrations throughout the article show you how to apply these techniques in real-world scenarios, whether you're building navigation menus, creating step-by-step instructions, or organizing complex content hierarchies.


## List Types and Nesting

HTML provides three primary list types: unordered lists (`ul`), ordered lists (`ol`), and description lists (`dl`). Unordered lists use the `<ul>` element, with individuals items created using `<li>`. Ordered lists employ the `<ol>` element structure, while description lists utilize `<dl>`.

Lists can be nested to create complex structures. For instance, an unordered list might contain another unordered list as one of its items. The default marker for both `<ul>` and `<ol>` elements can be customized using CSS properties like `list-style-type`, `list-style-position`, and `list-style-image`.


### Nested List Structure

When nesting lists, the marker style changes based on the depth of nesting. For example, an unordered list nested within an ordered list will adopt a hollow circle marker rather than the solid disc used in the parent list. Each list item maintains semantic structure, with `<ul>` and `<ol>` elements containing only `<li>` elements as direct children.


### List Item Marker Customization

The `list-style-type` property offers several styling options, including:

- `disc`: filled circle (default for unordered lists)

- `circle`: hollow circle

- `square`: filled square

- `decimal`: numbers starting from 1 (default for ordered lists)

- `lower-alpha`: lowercase ASCII letters

- `lower-roman`: lowercase Roman numerals

- `upper-alpha`: uppercase ASCII letters

- `upper-roman`: uppercase Roman numerals

Additional customization includes `none` for no bullet markers, and `list-style-image` for using background images as markers. The `list-style-position` property controls marker placement, with values `inside` and `outside`. For unordered lists, the default is outside; for ordered lists, the default is inside.


### Advanced List Styling

CSS provides extensive control through the `list-style` shorthand property, combining `list-style-type`, `list-style-position`, and `list-style-image`. When an image-based marker fails to load, the `none` value ensures fallback to default bullet styles. Lists can also be styled with background properties, offering more precise control over marker appearance.


## List Item Marker Styling

CSS allows for detailed customization of list item markers through several key properties. The `list-style-type` property offers a wide range of options, from simple shapes like circles and squares to specialized styles including Roman numerals and ASCII letters. Beyond basic shapes, the property supports more complex options such as decimal-leading-zero and upper-roman, providing flexibility for various design requirements.

The `list-style-image` property introduces the ability to use background images as list markers, expanding the styling possibilities beyond traditional bullet points. This property requires careful consideration of image selection, particularly for unordered lists, where smaller, plain graphics typically yield the best results.

The placement of list markers is controlled through the `list-style-position` property, which offers two primary options: outside and inside. When set to outside, markers appear to the left of content, with text wrapping around them. In contrast, the inside position aligns markers with the first line of text, creating a more integrated visual appearance. These positioning options can significantly impact the overall layout and readability of complex list structures.

The `list-style` property combines `list-style-type`, `list-style-position`, and `list-style-image` into a single declaration, streamlining the styling process. This shorthand property accepts any combination of its constituent values, providing a powerful tool for precise list customization. By combining multiple properties in a single declaration, developers can achieve consistent and efficient list styling across their web applications.


## List Display and Floating

Lists can be displayed in various layouts through CSS properties. The default vertical display can be modified using `display` and `float` properties to create horizontal lists or arrange items in custom layouts.

To display list items in a single line, developers can use either `display: inline` or `display: inline-block` for list items (`<li>`). This creates a horizontal display with a single space between each list item. For more control over the layout, `float: left` can be applied to `<li>` elements, aligning them side by side without additional space between items.

The marker display can be customized using these properties while maintaining semantic structure. When changing the `display` property to `inline` or `inline-block`, list item markers are removed, allowing for cleaner horizontal alignment. The `inline-block` display type allows adding vertical margins and spacing, while `inline` does not.

Lists are commonly used in navigation menus, where `<li>` elements are typically displayed as `inline-block`. This creates a clean, horizontal menu with proper spacing between items. The example CSS provided demonstrates this application, setting font styles and ensuring proper spacing for a navigation menu.

For image-based markers, CSS allows using background images through the `list-style-image` property. The image selection requires consideration of size and complexity; smaller, plain graphics typically work best for unordered lists where markers need to integrate seamlessly with text.


## Reversed Lists and Counting

The `start` attribute in ordered lists allows setting a custom starting point different from the default of 1. For example, an ordered list using the start attribute will begin counting from the specified value. When combined with the `reversed` attribute, this allows creating countdown lists.

The `reversed` attribute reverses the order of an ordered list, making it useful for countdowns or specific numbering sequences. When used, the list items display in descending order. This attribute must be explicitly applied to the <ol> element:

```html

<ol start="4" reversed>

  <li>Final step</li>

  <li>Second to last step</li>

  <li>Third step</li>

</ol>

```

This results in a list counting down from 4 to 1. The `start` attribute can be combined with `reversed` for more complex numbering sequences, though care must be taken with the `value` attribute to ensure correct sequential numbering.

For individual items that need custom numbering, the `value` attribute allows setting specific numerical values. This affects subsequent item numbering, making it particularly useful for multi-part instructions or procedures:

```html

<ol>

  <li>Start here</li>

  <li value="9">This item skips 7 and 8</li>

  <li>Continuing normal sequence</li>

  <li>Another step in sequence</li>

</ol>

```

This creates a list that counts 1, 2, 9, 4, demonstrating how the `value` attribute can be used to control specific numbering patterns.


## Nesting and Layout


### Nested List Structure

Nested lists allow for complex document structures, with each level of nesting modifying marker styles. The parent unordered list (`<ul>`) containing a nested unordered list (`<ul>`) displays hollow circles for its markers, while the nested list uses solid circles. This structure maintains semantic integrity, with `<ul>` and `<ol>` elements consistently containing only `<li>` children.


### Custom List Styles

The provided exercise outlines detailed steps for custom list styling:

Square bullet points for unordered lists: `ul { list-style-type: square; }`

1.5 times font-size line-height for both list items: `li { line-height: 
1.5 * font-size; }`

Lower alphabetical bullets for ordered lists: `ol { list-style-type: lower-alpha; }`


### Background Image Integration

Custom bullet points can be achieved using background images, though careful consideration of image selection is crucial:

- Image should be smaller than text height

- Recommended for unordered lists

- CSS example: `ul { list-style-image: url(star.svg); background-position: 0 0; background-size: 
1.6rem 1.6rem; background-repeat: no-repeat; }`


### List Counting and Starting Values

Starting points can be customized using the `start` attribute:

HTML example: `<ol start="4">`

Result: List begins at 4 and continues sequentially

Reversed lists display in descending order using the `reversed` attribute:

HTML example: `<ol start="4" reversed>`

Result: List counts down from 4


### Custom Numbering

Ordered lists support custom numbering through the `value` attribute:

HTML example: `<li value="9">`

Result: This item appears as 9, skipping 7 and 8

