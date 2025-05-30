---

title: HTML `<ol>` Tag: Ordered List Element

date: 2025-05-29

---


# HTML `<ol>` Tag: Ordered List Element

The `<ol>` tag in HTML creates ordered lists with sequence-aware numbering, supporting customization through attributes and nested structures. This guide explores its basic usage, attribute options, and browser compatibility, emphasizing its role in creating structured, accessible web content.


## Basic Usage and Structure

The `<ol>` tag creates an ordered list of items, typically displayed with numbers or letters. This element represents a sequence of items where the order holds significance. Each list item is defined using the `<li>` tag, and multiple `<li>` elements can be nested within an `<ol>` element to create hierarchical lists.

The `<ol>` tag supports several attributes for customization:

- The type attribute determines the marker style and can be set to "1" (default) for numbers, "A" for uppercase letters, "a" for lowercase letters, "I" for uppercase Roman numerals, or "i" for lowercase Roman numerals.

- The start attribute allows setting the initial number in the sequence, always as an Arabic numeral, even when using letter or Roman numeral styles. For example, to begin numbering from "d" or "iv", use start="4".

- The reversed attribute can be used to display the list in descending order, though it requires no value when applied.

By default, browsers display ordered lists with decimal numbering, though they can be styled using CSS to change this behavior. The element supports all modern browsers including Internet Explorer, Firefox, Chrome, Edge, Safari, and Opera.


## Numbering Options and Attributes

The `<ol>` tag defines an ordered list of items, where each item is represented by the `<li>` tag. To customize the numbering style, the type attribute can be set to several options:

- "1" (default) for decimal numbers

- "A" for uppercase letters

- "a" for lowercase letters

- "I" for uppercase Roman numerals

- "i" for lowercase Roman numerals

For example:

```

<ol type="A">

  <li>Coffee</li>

  <li>Tea</li>

  <li>Milk</li>

</ol>

```

To control the starting value of the sequence, use the start attribute, which accepts integer values. This attribute always uses Arabic numerals, even when the type attribute is set to letters or Roman numerals. For instance, to begin counting from "d" or "iv", set start="4":

```

<ol start="4">

  <li>Coffee</li>

  <li>Tea</li>

  <li>Milk</li>

</ol>

```

The element supports nested lists, allowing for hierarchical organizational structures. Both ordered and unordered lists can be nested within each other to create complex document layouts.


## CSS Styling and Default Properties

The default display properties for the ordered list element include:

- display: block

- list-style-type: decimal

- margin-top: 1em

- margin-bottom: 1em

- margin-left: 0

- margin-right: 0

- padding-left: 40px

According to the HTML specification, the element's default presentation behavior is standardized across browsers, although developers may customize these properties using CSS styling. The block-level display and margin/padding values help to clearly separate ordered lists from surrounding content while providing consistent spacing.

For developers seeking to modify the default styling, the padding-left property provides the primary mechanism for adjusting the indentation of list items. This value is set to 40px in the default style, allowing authors to extend or reduce the indentation based on their design requirements.

The ordered list element's default properties consistently across all modern browsers, including Internet Explorer, Firefox, Chrome, Edge, Safari, and Opera, ensuring consistent appearance while leaving room for customization through CSS styling.


## Browser Compatibility and Attributes

The `<ol>` element supports the following attributes to customize its behavior:

- The reversed attribute specifies that the list order should be reversed (9,8,7...). This attribute requires no value when applied.

- The start attribute specifies the ordinal value of the first list item, allowing for custom numbering sequences. This attribute always uses Arabic numerals, even when the type attribute is set to letters or Roman numerals. For example, to begin the list from "d" or "iv", use start="4".

- The type attribute determines the marker type used in the list, with options including "1" for decimal numbers, "a" for lowercase letters, "A" for uppercase letters, "i" for lowercase Roman numerals, and "I" for uppercase Roman numerals. For instance:

```html

<ol type="A">

  <li>Coffee</li>

  <li>Tea</li>

  <li>Milk</li>

</ol>

```

The `<ol>` element also supports global attributes and event attributes, providing flexibility for additional customization and interactive functionality. Modern browsers fully support the `<ol>` element across all platforms, including Internet Explorer, Firefox, Chrome, Edge, Safari, and Opera.


## Nested Lists and Accessibility

The `<ol>` element supports nested structures, allowing the creation of hierarchical lists through the embedding of `<ol>` or `<ul>` elements within `<li>` elements. This feature enables the representation of complex data structures in web documents while maintaining semantic clarity through appropriate use of ordered and unordered list elements.

Both the `<ol>` and `<li>` elements carry implicit ARIA roles. The `<ol>` element has an implicit ARIA role of 'list', while `<li>` elements carry the 'listitem' role. These roles facilitate accessibility by providing clear semantic information to screen readers and assistive technologies. The `<ol>` element also supports various ARIA states and properties, including 'aria-labelledby' and 'aria-describedby', which can be used to associate the list with other elements in the document and provide additional context for screen reader users.

The element's browser compatibility reflects its widespread support across modern web browsers, including Internet Explorer, Firefox, Chrome, Edge, Safari, and Opera. This consistent support enables developers to confidently implement nested lists while maintaining cross-browser compatibility. The element's robust attribute set, including support for reversed, start, and type, further enhances its utility for creating complex and accessible list structures.

## References

- [HTML Relnoopener](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relnoopener.md)
- [HTML Nobr The non Breaking Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nobr%20The%20non%20Breaking%20Text%20Element.md)
- [HTML The Mark Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Mark%20Text%20Element.md)
- [HTML Autofocus](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Autofocus.md)
- [HTML dd The Description Details Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20dd%20The%20Description%20Details%20Element.md)