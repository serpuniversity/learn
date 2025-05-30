---

title: HTML `<ul>`: The Unordered List Element

date: 2025-05-29

---


# HTML `<ul>`: The Unordered List Element

The HTML `<ul>` element plays a crucial role in web development by providing a semantic way to represent unordered lists—typically displayed with bullet points. Unlike ordered lists, unordered lists focus on grouping items without implying any specific sequence. This fundamental structure consists of a `<ul>` container and `<li>` items, offering flexibility through nested lists and customizable styling options. Understanding how to properly implement and style `<ul>` elements can significantly enhance both the functionality and accessibility of web applications.


## Definition and Purpose

The HTML `<ul>` element represents an unordered list, typically displayed with bullet points, while serving a distinct semantic purpose in web development. When the sequence of items in a list doesn't affect its meaning, an unordered list is appropriate, as its primary function is to group items without implying any specific order.

This fundamental structure consists of the `<ul>` tag as a container, with each item represented by an `<li>` tag as its child element. The relationship between these tags is crucial: while `<li>` is the only direct child of `<ul>`, it can contain other elements that support flow content, allowing for complex structures like nested lists.

The element's default styling, defined in CSS properties, presents each list item with a bullet point. These default styles can be customized through various CSS attributes and values. For example, the `list-style-type` property allows developers to specify whether bullets should appear as circles, squares, or other shapes, while the `list-style-position` property controls whether bullets are placed inside or outside the text flow using values "inside" and "outside."

According to the specifications, the `<ul>` element supports nesting up to three levels, with each level maintaining distinct visual hierarchy through indentation. While it can alternate between unordered and ordered lists without restriction, this practice is recommended only when appropriate to the content structure.


## Markup and Syntax

The `<ul>` element requires the `<li>` element as its direct child, with the `<li>` element serving as the container for each individual list item. This fundamental structure allows for the creation of simple or nested unordered lists, with each `<li>` tag representing a single item in the list.

To create a basic unordered list, developers use the `<ul>` tag as the outer container, with each list item enclosed in `<li>` tags. For example:

```html

<ul>

  <li>Item 1</li>

  <li>Item 2</li>

  <li>Item 3</li>

</ul>

```

This generates a list of three items, each represented by a bullet point. The `<ul>` element supports nesting, allowing developers to create hierarchical structures by placing an `<ul>` tag within an `<li>` tag. However, this structure should only be used when the nested list maintains its own semantic meaning, as in the following example:

```html

<ul>

  <li>HTML

    <ul>

      <li>JavaScript</li>

      <li>React</li>

      <li>Vue</li>

    </ul>

  </li>

  <li>CSS</li>

</ul>

```

While the `<ul>` element supports multiple levels of nesting, the documentation recommends limiting this to three levels to maintain clarity and avoid excessive visual indentation.

The `<ul>` element defaults to displaying list items with bullet points, but developers have control over the appearance through CSS properties. The `list-style-type` property allows changing the bullet style to circles, squares, or removing them entirely, while the `list-style-position` property determines whether the bullet appears before or after the text using values "inside" or "outside."


## Styling and Customization

The `<ul>` element's default styling presents each list item with a bullet point, but developers have extensive control over this appearance through CSS properties. While the most straightforward approach is to set the `list-style-type` property to "none," several options and nuances exist for different use cases.

Developers can remove bullet points using multiple methods:

1. Inline CSS solution: Applying `ul {list-style-type: none;}` to the parent element removes bullet points for both the ul and its li elements, making longer lines more readable when they spill over to additional screen lines.

2. Combined CSS approach: Setting both the ul and li elements to remove list-style-type using `ul, li {list-style-type: none;}`

3. Individual li styling: Targeting only the li elements with `li {list-style-type: none;}`

4. CSS class method: Using a class to apply the style selectively, such as `<style> ul.no-bullets li { list-style-type: none; } </style> <ul class="no-bullets"> <li>Item 1</li> <li>Item 2</li> </ul>`

For cases where the default style doesn't respond to list-style-type changes, developers should check for custom list styles in the theme. If !important doesn't resolve the issue, there may be conflicting styles requiring attention.

When removing list styles, it's important to address all related properties for proper layout:

- Setting margin properties to zero: `margin: 0; margin-block-start: 0; margin-block-end: 0; margin-inline-start: 0; margin-inline-end: 0`

- Removing padding from the ul tag: `padding-left: 0`

After removing bullet points, developers often need to address resulting layout issues:

- Using `li {display: block;}` to maintain vertical stacking

- Applying padding and margin adjustments as needed

Additional styling options include customizing bullet types:

- Circles: Using `ul {list-style-type: circle;}` for circular markers

- Squares: Using `ul {list-style-type: square;}` for square markers

For creative applications, developers can use the `::before` pseudo-element to add custom content, such as emojis. This requires removing default padding and margin from the ul tag and specifying content using the `content` property with `:nth-child()` selectors for targeted styling.


## Nesting and Structure

The `<ul>` element allows for hierarchical structures through nested lists, where one list can be placed within another list item. This creates a visual hierarchy through indentation, with each level maintaining semantic meaning.

To create a nested unordered list, developers place the `<ul>` tag inside an `<li>` tag, with the nested list starting and ending with `<ul>` tags. For example:

```html

<ul>

  <li>HTML

    <ul>

      <li>JavaScript</li>

      <li>React</li>

      <li>Vue</li>

    </ul>

  </li>

  <li>CSS</li>

</ul>

```

The documentation recommends using nested lists only when they maintain semantic meaning, avoiding unnecessary complexity that can affect readability. Each nested level maintains its own visual hierarchy through indentation, with up to three levels supported for clarity.

When nesting lists, developers should consider the impact on default styling. The text notes that the `<ul>` element inherently displays bullet points, so additional CSS is often required to remove them. The recommended approach is to set `list-style-type: none;` for both the ul and li elements, while also addressing related properties like margin and padding to maintain proper layout.


### Best Practices

- Limit nested lists to three levels to maintain visual clarity

- Ensure semantic meaning when nesting lists

- Use CSS to remove bullet points and adjust related properties

- Consider accessibility and screen reader support when customizing list styles


## Browser Support and Accessibility

The `<ul>` element enjoys broad compatibility across modern web browsers, with documented support in Chrome, Edge, Safari, Firefox, and Opera. Internet Explorer also fully supports this element, though older versions may display minor differences in rendering. For developers concerned with backward compatibility, testing on Internet Explorer 6-9 is advised to ensure proper display and functionality.

Unlike some complex HTML elements, the `<ul>` doesn't carry specific accessibility concerns beyond general best practices. It inherently takes on an "list" ARIA role, inheriting this from its default behavior as a container for unordered items. While other ARIA roles and global attributes are technically allowed, the documentation recommends against explicitly setting these, particularly the deprecated "directory" role.

For developers implementing accessibility features, the `<ul>` element works well with standard ARIA attributes like role="list" when custom list styles are applied. This helps screen readers and assistive technologies correctly interpret the list structure, ensuring users can navigate and understand the content regardless of visual display.

## References

- [HTML pre The Preformatted Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20pre%20The%20Preformatted%20Text%20Element.md)
- [HTML Draggable](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Draggable.md)
- [HTML Tbody The Table Body Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Tbody%20The%20Table%20Body%20Element.md)
- [HTML The Strong Importance Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Strong%20Importance%20Element.md)
- [HTML The Figure With Optional Caption Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Figure%20With%20Optional%20Caption%20Element.md)