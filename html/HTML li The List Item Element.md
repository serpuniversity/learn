---

title: HTML `<li>`: The List Item Element

date: 2025-05-29

---


# HTML `<li>`: The List Item Element

Lists are fundamental building blocks of web content, providing a structured way to present items of related information. Whether you're creating a navigation menu, a step-by-step guide, or a simple collection of links, understanding how to use HTML's `<li>` element is crucial. This article explores the `<li>` tag in detail, from its basic usage and styling options to more advanced techniques for creating interactive and accessible list-based interfaces. You'll learn how to customize bullet styles, style list items using CSS, and even create horizontal navigation menus. By the end, you'll be able to create dynamic, accessible lists that enhance both the functionality and visual appeal of your web pages.


## HTML `<li>` basics

The `<li>` tag defines a single item in a list, commonly used within unordered list (`<ul>`) and ordered list (`<ol>`) elements. Within unordered lists and `<menu>` elements, list items typically display as bullet points, while ordered lists display numbered elements by default. The `<li>` tag supports the value attribute for ordered lists, allowing developers to specify the starting number of the list sequence.

To customize list item display, developers have several options. The `<li>` tag supports the type attribute, allowing selection between circle (unfilled), disc (filled), and square bullet styles. For more extensive customization, developers can leverage CSS properties. The `<li>` tag accepts both Global Attributes and Event Attributes, expanding its functionality beyond basic list item definition.


## Displaying List Items

The display of list items follows specific default styles based on their containing element. By default, unordered list items display as circles, while ordered list items display as numbers or letters. These default markers can be customized using CSS properties. The most commonly used property is `list-style-type`, which accepts several values including "disc" for circles, "circle" for unfilled circles, and "square" for filled squares. The property can also be set to "none" to remove default markers entirely.

For more advanced styling, the `::before` pseudo-element offers precise control over bullet appearance and positioning. This technique involves removing the default list style with `list-style: none;`, creating space for the custom bullet using `padding-left`, and applying the custom bullet character through `content: "";`. Additional styling can be added using `border-radius`, background color, and other CSS properties to create the desired effect. This method maintains compatibility across modern browsers, including Internet Explorer 8 and later versions.

The `list-style-position` property further extends customization options by controlling where the marker appears relative to the list item content. With the default "outside" position, markers display to the left of the content. Setting `list-style-position` to "inside" aligns markers with the first line of content, allowing the content to wrap below. For horizontal navigation menus, developers can use either `display: inline-block` or `float: left` on `li` elements. The inline-block method requires careful margin and padding adjustments to maintain proper spacing between items, while the float method may necessitate additional clearance to restore normal page flow.


## Attributes and Customization

The `<li>` tag supports several attributes that modify the style of the list item bullet. The most commonly used attribute is `type`, which can take three values: "circle" (unfilled circle), "disc" (filled circle), and "square" (filled square). For example:

```html

<ol>

  <li type="circle">First item</li>

  <li type="disc">Second item</li>

  <li type="square">Third item</li>

</ol>

```

The value attribute is used to specify the starting number of the list item in ordered lists. This attribute only works for ordered lists (ol) tag. For example:

```html

<ol>

  <li value="4">Buy groceries</li>

  <li>Complete homework</li>

  <li>Walk the dog</li>

</ol>

```

The tag also supports Global Attributes and Event Attributes, though specific examples are not provided in the documentation. The li tag must have a start tag and can omit its end tag if immediately followed by another li element or if there is no more content in the parent element. This allows for concise list definition while maintaining proper HTML structure.


## Accessibility and Semantics

The `<li>` element must be contained within an `<ul>` (unordered list) or `<ol>` (ordered list) parent element. This structure ensures accessibility and semantic clarity for screen reader users, as it explicitly indicates the presence of a list and its type. Screen readers announce the number of items in a list and maintain proper reading order, which is crucial for accessibility compliance.

The `<li>` element supports multiple list style property values, including list-style-type and list-style-position. These properties allow fine-grained control over the appearance and behavior of list items. For example, developers can use list-style-type to select between circle (unfilled), disc (filled), and square bullet styles.

To implement horizontally oriented lists, developers have two primary methods. The first method uses display: inline-block on `<li>` elements, creating a single line with space between each item while removing the list item marker. The second method employs float: left on `<li>` elements, aligning all items in a row without space between them. The float method requires additional clearing to restore normal page flow.

The `<li>` element serves as a fundamental building block for displaying structured content, supporting both simple and complex list structures. Understanding its role in HTML semantics and accessibility ensures that web developers create clear, usable, and compliant list presentations for all users.


## Interactive List Items

List items can be made interactive through JavaScript or by structuring the HTML to link internal elements correctly. This functionality requires careful consideration of the default click behavior of both the `<li>` element and its contained `<a>` tag.

A common challenge is ensuring that clicking on the entire `<li>` element activates the link within it. The default behavior of browsers can make parts of the `<li>` element non-clickable, particularly where the `<a>` tag has padding or background settings that extend beyond the visible text area.

To achieve full-clickability, developers can adjust the padding and display properties of both the `<li>` and `<a>` elements. For example, setting the `<li>` padding to zero and the `<a>` display property to block allows the entire `<li>` element to function as a clickable link. Proper implementation requires testing across different browsers, as some versions may require additional adjustments for optimal performance.

For static solutions, developers can use JavaScript to handle the click event directly on the `<li>` element. This approach involves adding an onclick attribute to the `<li>` element that changes the location or performs another desired action. The element can also be styled to indicate a clickable state, such as changing the cursor to a pointer when hovered over.

More complex implementations might consider using a single `<a>` element that contains multiple `<li>` elements. This structure requires additional CSS to maintain proper styling while allowing the nested `<li>` elements to function as clickable items. The parent `<a>` element should inherit the href attribute to ensure correct link functionality.

While these approaches effectively make list items interactive, it's important to note that HTML validation tools may raise concerns about the structural integrity of the document. The W3C recommendation explicitly states that child elements of `<ul>` and `<ol>` should be `<li>` elements, which may conflict with interactive designs that wrap links around multiple items. Understanding these limitations helps developers create accessible, interactive lists while maintaining semantic correctness.

## References

- [HTML Translate](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Translate.md)
- [HTML Comments](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Comments.md)
- [HTML The Generic Search Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Generic%20Search%20Element.md)
- [HTML Attribute min](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20min.md)
- [HTML Samp The Sample Output Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Samp%20The%20Sample%20Output%20Element.md)