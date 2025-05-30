---

title: HTML `<samp>`: The Sample Output element

date: 2025-05-29

---


# HTML `<samp>`: The Sample Output element

When working with web development and programming documentation, it's crucial to properly display code outputs and terminal interactions. HTML offers several elements to achieve this, but the `<samp>` tag stands out for its specific use case and default styling. In this guide, we'll explore the `<samp>` tag's basic usage, styling options, and accessibility considerations to help you effectively display sample output in your web pages.


## Basic Usage and Structure

The `<samp>` tag is used to display sample output from computer programs, providing default monospaced font rendering. Content within the tag is displayed in the browser's default monospaced font, such as Courier or Lucida Console. The element encapsulates inline text that represents sample or quoted output from a computer system or program, and works in conjunction with the `<pre>` element to maintain formatting, including spaces and line breaks.

The `<samp>` tag requires both start and end tags and can contain any phrasing content. Browser compatibility across Chrome, Edge, Safari, Firefox, Opera, and Internet Explorer is supported, with specific nuances and older version support details available in the "Useful Resources" section. The element inherits global attributes and has a default `role` attribute value of "generic," though the use of specific roles is generally discouraged.


### Basic Usage

The `<samp>` tag can be styled using CSS to change its appearance while browser defaults can be overridden to achieve specific design requirements. For example, a command line tool's website could style `<samp>` specifically, while the basic structure of an HTML page includes a `<samp>` tag with sample text inside it:

```html

<p>Here is an example of using the <samp> tag:</p>

<samp>Sample Text</samp>

```


### Styling and Customization

CSS properties can be used to style the `<samp>` tag, such as in the following example:

```css

samp {

  background-color: #f1f1f1;

  padding: 1em;

  border-radius: 5px;

}

```


### Accessibility Considerations

The `<samp>` tag plays a role in semantic markup by indicating sample output, though it should be used appropriately to maintain accessibility and proper document structure. It accepts no specific attributes beyond global attributes and can be used in elements that accept phrasing content. The element's DOM interface is HTMLElement and is part of the HTML specification, with no specific naming restrictions for ARIA roles.


##  Styling and Customization

The `<samp>` element provides subtle colorization and emboldens keyboard input within sample text, though these stylistic enhancements are applied by the browser's default rendering. Browser preferences may take precedence over CSS when styling `<samp>` elements, and authors should be aware that while the element can be styled using CSS, the browser's default monospaced font (such as Courier or Lucida Console) is typically used.

The `<samp>` element works in conjunction with the `<pre>` element to maintain formatting, including spaces and line breaks. Content within `<samp>` tags is displayed inline by default, but authors can use CSS to modify its presentation. For example, a background color, padding, and border radius can be applied to the `<samp>` element as demonstrated in the first code example:

```css

samp {

  background-color: #f1f1f1;

  padding: 1em;

  border-radius: 5px;

}

```

In conjunction with the `<kbd>` element, `<samp>` can be used to highlight user inputs or commands. The `<samp>` element can contain any phrasing content and works in any element that accepts phrasing content. Its default display properties are defined as follows: samp { font-family: monospace; }

While the element can be styled with CSS, browser default styles, such as the monospaced font, may take precedence. Authors should use global ARIA attributes and roles appropriately when styling `<samp>` elements to maintain accessibility and proper document structure.


## Accessibility Considerations

The `<samp>` tag is specifically designed for displaying sample output from computer programs and applications, with its content typically rendered in the browser's default monospaced font. This default rendering helps maintain consistency in the display of code outputs, system responses, and terminal/console interactions (MDN Web Docs, n.d.).

The tag's basic structure requires both start and end tags, encapsulating any phrasing content between them. While authors can use CSS to style the `<samp>` element, browser preferences may take precedence over explicit styling (HTML `<samp>` Tag, n.d.). To maintain accessibility and proper document structure, the element should be used appropriately for its intended semantic purpose.

When combined with other elements, `<samp>` can create more complex displays of code and user interactions. For example, it can be paired with `<kbd>` elements to represent both sample output and user input (HTML `<samp>` Tag, n.d.). This combination allows developers to clearly distinguish between system outputs and user commands within a single code snippet.

The `<samp>` element's default display properties are defined as monospace font, though authors can override this with CSS to achieve specific design requirements (HTML `<samp>` Tag, n.d.). By providing semantic meaning for sample output, the element helps maintain proper document structure while allowing for flexible styling options through CSS.


## Common Use Cases

Developers frequently use the `<samp>` tag to display code outputs, system responses, and terminal/console interactions within web pages. This usage is particularly common in documentation, code examples, and interactive tutorials where the output of specific commands or processes needs to be demonstrated to readers or users.

For instance, a developer might use `<samp>` to show the result of executing a command in a terminal, as illustrated in the following example from the HTML `<samp>` Tag documentation:

```html

<samp> $ git status

On branch master

nothing to commit, working directory clean

</samp>

```

This combination of `<samp>` and `<pre>` elements maintains proper formatting while clearly distinguishing between system output and user input through the use of `<kbd>` for commands. The `<samp>` tag can also be styled using CSS to enhance presentation, as shown in this example from the Creating a Sample Output lab:

```html

<samp>

  <code>

    print("Hello World");

  </code>

</samp>

```

With its monospaced font default, `<samp>` ensures consistent display of code outputs across different browsers and devices, making it particularly useful for web-based development environments and documentation sites.

The element's broad compatibility across modern browsers and its ability to work within any element that accepts phrasing content make it a versatile choice for developers seeking to display program output in their web pages. This common usage helps maintain proper document structure while providing developers with flexible styling options through CSS.

## References

- [HTML The Marquee Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Marquee%20Element.md)
- [HTML u The Unarticulated Annotation Underline Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20u%20The%20Unarticulated%20Annotation%20Underline%20Element.md)
- [HTML Tbody The Table Body Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Tbody%20The%20Table%20Body%20Element.md)
- [HTML Relpreload](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relpreload.md)
- [HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML.md)