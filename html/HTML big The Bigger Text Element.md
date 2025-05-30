---

title: HTML `<big>`: The Bigger Text Element

date: 2025-05-29

---


# HTML `<big>`: The Bigger Text Element

The `<big>` element once provided a straightforward way to increase text size in HTML, raising the font level by one step and capping at a maximum size. While its functionality was simple, the element's limitations and the web's evolution toward standards-based development have made it obsolete. Understanding how `<big>` worked – increasing text size by one level with a maximum cap – provides valuable context for modern web developers who need to adjust text sizing while following best practices.


## Overview of the `<big>` Element

The big element in HTML was specifically designed to increase the font size of text by one level compared to the surrounding text. This increase typically followed a medium font size to a large font size. However, it's important to note that the big element has been deprecated in HTML5 and should no longer be used for this purpose.

The element worked by rendering enclosed text at a font size one level larger than the surrounding text. While it provided a simple way to increase text size, it had several limitations. Notably, it had a maximum font size cap that prevented excessive text enlargement, which could be problematic for accessibility and readability.

Modern web development practices now recommend using CSS for text sizing instead of relying on HTML elements like big. This shift aligns with the web standards movement to separate content structure from presentation styling.


## Historical Usage

The big element increased text size by one level compared to surrounding text, with a maximum font size. This size increase typically followed a medium font size to a large font size, effectively making the text one level larger than its context.

From a technical perspective, the element rendered enclosed text at a font size one level larger than the surrounding text. For example, this meant that text enclosed in `<big>` tags would appear in a larger font size than the text around it, typically following a medium size to large size progression. This behavior could be described as a one-level increase in font size, with a practical limit on the maximum permitted size to prevent excessive text enlargement.

The element's functionality was straightforward but had significant limitations. It could only increase text size by one level, meaning that subsequent `<big>` elements would not produce progressively larger text beyond the initial size increase. This approach prevented the kind of cascading size changes that modern CSS allows, instead implementing a fixed-size increase that could be described as a medium to large font transition.


## Modern Alternatives

The modern web development landscape offers robust alternatives to the deprecated `<big>` element, with CSS providing the most flexible and standards-compliant methods for controlling text size. CSS's font-size property allows developers to set text size precisely and consistently across documents, while maintaining separation between content structure and presentation styling.


### CSS Syntax Options

There are several CSS syntax options for setting text size, each with its own advantages:

- **Inline CSS:** Directly applies styles within an HTML tag using the style attribute. For example:

  ```html

  <h1 style="font-size:4em;">Hello World!</h1>

  <p style="font-size:14px;">Any text whose font we want to change</p>

  ```

- **Internal/External CSS:** Uses selectors to apply styles to HTML elements. For example:

  ```html

  <p>Any text whose font we want to change</p>

  <style> p { font-size: 14px; } </style>

  ```

- **Class-based CSS:** Uses classes to apply styles to multiple elements. For example:

  ```html

  <p class="my-paragraph">Any text whose font we want to change</p>

  <style> .my-paragraph { font-size: 14px; } </style>

  ```


### Text Size Calculation

Modern approaches to text sizing rely on mathematical formulas for precise control. For example, to set the `<h1>` element to 2.5 times the base size (45px), developers can use the following formula: (target / base) * 100%. This results in the `<h1>` element being 250% of the base size.

For secondary headings, the formula translates to:

- h2: 36px (200% of base)

- h3: 32px (177.78% of base)

- h4: 26px (162.5% of base)

- h5: 22px (122% of base)

- h6: 18px (100% of base)


### Browser Compatibility

All modern browsers support CSS's font-size property across various syntax options. While the `<big>` element is still functional in most browsers, relying on CSS ensures compatibility with future standards and maintains cleaner, more maintainable code. The browser compatibility for key CSS text metrics properties is as follows:

- fontBoundingBoxAscent & fontBoundingBoxDescent: Supported in Firefox 116+, Safari 11.1+, Chrome 87+

- actualBoundingBoxAscent & actualBoundingBoxDescent: Supported in Firefox 74+, Safari 11.1+, Chrome 77+

- emHeightAscent & emHeightDescent: Supported in Firefox 74+, Safari 11.1+, Chrome 77+


## Element Behavior

The `<big>` element increased font size by one level, with a maximum permitted size. According to the HTML standard, it rendered enclosed text at a font size one level larger than the surrounding text (medium becomes large), with a maximum permitted font size cap that prevented excessive text enlargement.

The element's functionality relied on a one-level increase in font size, meaning that subsequent `<big>` elements would not produce progressively larger text beyond the initial size increase. This approach limited the creation of cascading size changes, in contrast to modern CSS, which enables precise control over text size progression.

Implementation of the element followed a mathematical formula based on the base font size. For example, to achieve a two-level size increase from the base font, developers applied a 200% size multiplier. This calculation continued for further levels, resulting in specific size outputs for each heading level: h2 at 36px (200% of base), h3 at 32px (177.78% of base), h4 at 26px (162.5% of base), h5 at 22px (122% of base), and h6 at 18px (100% of base).

The element's maximum font size served multiple purposes. While providing a practical limit to text enlargement, it also prevented style inconsistencies across different browser implementations. This cap ensured that text size remained within a controlled range, maintaining readability and accessibility standards.

Browser implementation of the `<big>` element generally followed these size progression rules, with the actual maximum size varying slightly based on font families and system settings. For example, the browser might default to 36px (1.5 times 24px) as the maximum size, but this could increase to 48px or 60px with different font stacks or system configurations.


## Browser Support

The `<big>` element remains functional across most major browsers, offering compatibility with older codebases and document structures. However, its use is explicitly discouraged in current web development practices. The element retains its fundamental functionality of rendering enclosed text one font size larger than the surrounding content, aligning with its historical behavior of medium to large font size progression.

Browser support for the `<big>` element spans multiple versions, with compatibility extending back to Internet Explorer 2 and Netscape 1. Modern browsers maintain support through version 6, aligning with the deprecation timeline set by HTML5 standards. The element's continued functionality across these versions demonstrates its historical integration into web development practices, even as its use has become deprecated.

The `<big>` element's behavior consistently applies a one-level increase in font size, with implementation following a mathematical progression based on the base font size. For example, applying four consecutive `<big>` tags produces the same visual effect as the `<font size="7">` tag, demonstrating the element's consistency in font size calculation across implementations. This mathematical progression continues for larger size increases, with subsequent levels maintaining a precise relationship to the base font size.

In practical implementation, the element caps its maximum font size according to browser and system settings, typically ranging between 36px and 60px based on font family and configuration. This maximum size serves to maintain readability and consistency across different rendering environments, preventing the style inconsistencies that might arise from unrestricted font size adjustments.

While the element remains supported, its use continues to be discouraged in favor of modern CSS approaches. The HTML5 specification explicitly removes the `<big>` element from the official standard, recommending CSS for text styling needs. This change aligns with the wider trend toward separation of content structure from presentation styling in current web development practices.

## References

- [HTML em The Emphasis Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20em%20The%20Emphasis%20Element.md)
- [HTML Reldns Prefetch](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Reldns%20Prefetch.md)
- [HTML Itemtype](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Itemtype.md)
- [HTML rp The Ruby Fallback Parenthesis Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20rp%20The%20Ruby%20Fallback%20Parenthesis%20Element.md)
- [HTML add A Hitmap On top Of An Image](https://github.com/serpuniversity/learn/blob/main/html/HTML%20add%20A%20Hitmap%20On%20top%20Of%20An%20Image.md)