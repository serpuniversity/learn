---

title: HTML Strikethrough: Master the Art of Crossed-Out Text in Web Development

date: 2025-05-29

---


# HTML Strikethrough: Master the Art of Crossed-Out Text in Web Development

Web developers often need to indicate changes, obsolescence, or revisions in their content. HTML provides several tags for creating strikethrough effects, including `<s>`, `<del>`, and `<strike>`. While these tags produce similar visual results, their semantic meanings differ significantly. The `<s>` tag indicates content that is no longer relevant or accurate, the `<del>` tag shows document edits and deletions, and the `<strike>` tag is a simpler alternative that produces the same effect as `<s>`. Modern best practices recommend using semantic tags over inline styling, offering both visual consistency and improved accessibility. This comprehensive guide will help web developers choose the right tag and implement effective strikethrough effects using HTML and CSS.


## HTML & CSS Fundamentals

The HTML strikethrough functionality has evolved significantly since its introduction in HTML 4. The `<s>` tag is specifically designed to mark content that is no longer relevant or accurate, providing better semantic meaning than its predecessor, the `<strike>` tag. The `<del>` tag, on the other hand, is specifically intended to indicate document edits and deletions, though it produces similar visual results to the other tags.

From a practical standpoint, developers can create strikethrough effects using several methods. The basic HTML tags (`<s>`, `<del>`, `<strike>`) produce similar visual results but differ in their semantic meaning. For example, the code `<p>GeeksforGeeks is a <s>Math</s> Computer Science Portal.</p>` produces the same visual effect as `~~Math~~` but carries more semantic weight than the equivalent `<strike>` version.

Modern web development best practices recommend using semantic tags over inline styling whenever possible. CSS provides robust alternatives through the `text-decoration` property, which can be applied directly to text elements or combined with existing styles. The CSS example `.sale-price { text-decoration: line-through; }` demonstrates how to style prices that are no longer valid without using inline markup.

For more advanced customization, developers can use CSS pseudo-elements and additional properties. The recommended approach for cross-browser compatibility is to use the `:after` selector with absolute positioning, as demonstrated in this code snippet:

```css

s, strike {

  text-decoration: none;

  position: relative;

  display: inline-block;

}

s:after, strike:after {

  content: "";

  position: absolute;

  bottom: 0;

  left: 0;

  border-top: 2px solid red;

  height: 45%; /* adjust as necessary */

  width: 100%;

  transform: rotateZ(-4deg);

}

```

This method provides the flexibility needed for specialized design requirements while maintaining compatibility across modern browsers.


## Semantics and Accessibility

The `<s>` and `<del>` tags offer distinct advantages in web development. The `<s>` tag is ideal for marking content that is no longer relevant or accurate, making it particularly effective for showing outdated information or replaced text. For instance, during a sale event, it can clearly indicate that the regular price is no longer valid, as demonstrated in this usage example:

```html

<p>Grab the latest Smartphone X!</p>

<p><s>Regular Price: $999</s></p>

<p>Special Sale: Only <strong>$799</strong>!</p>

```

The `<del>` tag, while producing similar visual effects, is specifically designed for indicating document edits and deletions. This semantic distinction helps screen readers and assistive technologies correctly interpret the content's meaning. For example, when showcasing a product's revised return policy, the tag would be used as follows:

```html

<p>Our previous return policy:</p>

<p>The item must be returned within 14 days of delivery.</p>

<p>Current policy:</p>

<p>The item must be returned within 30 days of delivery.</p>

<p>The previous policy, now <del>defunct</del>, did not allow returns after 14 days.</p>

```


### Screen Reader Compatibility

When using strikethrough elements, developers must consider how assistive technologies interpret the content. Screen readers typically announce `<del>` content as "deleted," which helps users understand the text's revision history. However, both `<s>` and `<del>` elements lack specific ARIA roles, making it crucial for surrounding content to clarify their meaning.


### Testing and Implementation

To ensure optimal functionality across different browsers and screen readers, developers should test their implementation thoroughly. The recommended approach is to use the `<s>` tag for general reductions or emphasis while reserving `<del>` for document edits. For visual customization, CSS provides robust options through the text-decoration property, allowing precise control over line thickness, color, and position. Pseudo-element techniques enable advanced styling while maintaining compatibility with various browsers and assistive technologies.


## Customization and Advanced Styling

The basic strikethrough effect can be extended using several CSS techniques while maintaining compatibility across browsers and screen readers.


### Multi-Line Effects

For multiline strikes, developers can use the :after selector with absolute positioning and CSS transforms, as demonstrated in the following code snippet:

```css

s, strike {

  text-decoration: none;

  position: relative;

  display: inline-block;

}

s:after, strike:after {

  content: "";

  position: absolute;

  bottom: 0;

  left: 0;

  border-top: 2px solid red;

  height: 45%; /* adjust as necessary */

  width: 100%;

  transform: rotateZ(-4deg);

}

```

This method is effective for most cases but has limitations for large blocks of text. The gradient approach using background properties provides better multiline support, though it requires careful adjustment of background-size and color-stops based on line-height.


### Color Options

To change the color of the strikethrough line, developers can use the text-decoration-color property. However, browser support varies - as of 2024, it is fully supported in all major browsers except Microsoft browsers.

For cross-browser compatibility, developers can use multiple text-decoration properties with specific styling:

```css

.yourClass {

  text-decoration: line-through;

  text-decoration-color: red;

}

```

Alternatively, they can wrap the text in span elements with specific styles:

```html

<span style="color:red;text-decoration:line-through">

  <span style="color:black">black with red strikethrough</span>

</span>

```


### Advanced Customization

For more complex designs, developers can use pseudo-elements and additional properties. The recommended approach is to create a .lineThrough class with CSS:

```css

.lineThrough {

  position: relative;

}

.lineThrough:after {

  content: " ";

  display: block;

  width: 60px;

  height: 1px;

  background: red;

  position: absolute;

  top: 49%;

  left: 50%;

  margin-left: -30px;

}

```

To create a transparent strikethrough effect, developers can use background properties as demonstrated in the Stack Overflow example:

```css

span {

  text-decoration: none;

  background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0) 50%, rgba(255,255,255,1) 50%, rgba(255,255,255,1) 100%);

  background-size: 100% 2px;

  background-position: 0 100%;

}

```

These techniques enable precise control over strikethrough effects while maintaining compatibility across modern browsers and assistive technologies.


## Browser Compatibility and Backwards Support

Browser support for strikethrough functionality has evolved significantly since its introduction in HTML 4. While the basic `<s>` and `<del>` tags maintain good compatibility across modern browsers, developers must consider implementation techniques to ensure support for older versions like Internet Explorer 8.


### Basic Tag Support

The `<s>` and `<del>` tags maintain consistent support across major browsers. According to comprehensive testing across multiple versions of Chrome, Firefox, Safari, Edge, and Internet Explorer, both tags function correctly in modern browsers. However, Internet Explorer 8 and earlier versions do not support these semantic tags, requiring alternative approaches for compatibility.


### Legacy Browser Workarounds

For supporting older browsers, developers can use CSS techniques that provide fallbacks for semantic tags. The recommended approach is to use the :after pseudo-element with absolute positioning and CSS transforms, as demonstrated in this widely-tested code snippet:

```css

s, strike {

  text-decoration: none;

  position: relative;

  display: inline-block;

}

s:after, strike:after {

  content: "";

  position: absolute;

  bottom: 0;

  left: 0;

  border-top: 2px solid red;

  height: 45%; /* adjust as necessary */

  width: 100%;

  transform: rotateZ(-4deg);

}

```

This method has been confirmed to work effectively in Internet Explorer 8 and all subsequent versions, providing a reliable fallback for older browser support.


### Advanced Customization

For developers requiring additional styling capabilities or multi-line effects, the gradient approach using background properties provides robust support across modern browsers. As of 2024, this technique works without issues in all major browsers, including older versions of Internet Explorer.


### Testing and Validation

To ensure compatibility across multiple browsers and versions, developers should perform thorough testing using tools like BrowserStack or testing frameworks that support multiple environments. This approach helps identify potential issues early in the development process, ensuring consistent rendering across all target platforms.


## Best Practices and Common Mistakes

HTML strikethrough provides multiple methods for indicating changes, obsolescence, and revisions in web content. While the `<strike>` tag remains supported for compatibility, developers should prioritize the `<s>` and `<del>` tags for semantic clarity and accessibility.

The `<s>` tag is most appropriate for marking content that is no longer relevant or accurate, such as this example from the source material: "Support for Internet Explorer 11 continues. Support has officially ended."

The `<del>` tag is specifically designed for document edits and deletions, as demonstrated in the following legal content excerpt: "The event is on Thursday Friday evening."

In practice, combining strikethrough with other semantic elements can enhance both functionality and clarity. For instance, the source material recommends using strikethrough in conjunction with `<strong>`, `<em>`, or `<a>` tags to maintain emphasis while crossing out content: "The VIP plan is no longer offered."

To ensure consistent rendering across browsers, developers should implement cross-browser compatible solutions using CSS. The text-decoration property offers robust styling options, as shown in this pricing example: "This product is discontinued" with the CSS rule .discontinued { text-decoration: line-through; }

For more advanced customization, the `<s>` tag's :after pseudo-element provides flexibility in line style and color. As noted in the source material, this technique enables precise control while maintaining compatibility across modern browsers.

