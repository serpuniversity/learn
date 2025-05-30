---

title: The HTML `<mark>` Element

date: 2025-05-29

---


# The HTML `<mark>` Element

In the era of digital communication, effectively conveying emphasis and highlighting crucial information has become more important than ever. The HTML `<mark>` element emerges as a powerful tool for marking text that needs special attention - whether that's search results, important keywords, or quoted material. This comprehensive guide explores the `<mark>` element's basic usage, advanced styling options, and accessibility considerations, helping developers create more informative and accessible web content. From highlighting key concepts to marking up citations, we'll examine how this simple yet versatile tag can enhance your web authoring toolkit.


## Basic Usage and Structure

The `<mark>` element highlights text for reference or notation purposes, typically rendered with a yellow background. For example, in a complete paragraph, the words "highlighted text" will appear with a yellow background color in most browsers (WebReference, HTML5: Edition for Web Authors).

The element requires both opening and closing tags and supports global attributes like lang, id, accesskey, and draggable, as well as event attributes such as onclick and onload (mark Tag in HTML). However, it does not have any attributes specific to the `<mark>` tag itself (The HTML `<mark>` Element).

By default, browsers render the marked text with a yellow background color and black text color (HTML5: Edition for Web Authors). This color scheme provides sufficient contrast for readability, meeting WCAG 4.5:1 color contrast ratio guidelines (WebReference).

The `<mark>` element can be customized using CSS to change the background and text colors. Inline CSS allows for specific styling, while CSS classes enable consistent formatting across the document (How to Highlight Text in HTML: A Comprehensive Guide).

To implement the `<mark>` tag, the HTML document must include the <!DOCTYPE html> declaration for proper rendering (HTML `<mark>` Tag). Common usage includes highlighting important text, such as keywords, quotes, or relevant information within a paragraph (WebReference).

When used in conjunction with JavaScript or CSS, the `<mark>` element provides additional functionality for highlighting important content in web pages (WebReference).


## Rendering and Styling

The element supports both global attributes and event attributes, as demonstrated in advanced usage examples (HTML `<mark>` Tag). Common attributes include lang, id, accesskey, and draggable, with additional support for onclick, onload, and other event attributes (mark Tag in HTML).

For detailed styling, the element's background color defaults to yellow with black text, but developers can customize these properties using CSS (How to Highlight Text in HTML: A Comprehensive Guide). For example, inline CSS allows specific styling like this:

```html

<p>This is a <mark style="background-color: green;">highlighted text</mark> in a complete paragraph.</p>

```

Alternatively, CSS classes enable consistent formatting across documents:

```html

/* In your CSS file */

.highlight {

  background-color: green;

}

<!DOCTYPE html>

<html>

<head>

  <link rel="stylesheet" type="text/css" href="styles.css">

</head>

<body>

  <p>This is a <mark class="highlight">highlighted text</mark> in a complete paragraph.</p>

</body>

</html>

```


### Browser Support

The element's basic functionality - text highlighting with yellow background - has been supported since HTML 6.0 of Internet Explorer, 9.0 of Firefox, 4.0 of Safari, 5.0 of Chrome, and 11.1 of Opera (HTML mark Tag). As of July 2015, the feature was implemented across browsers, with consistent support across desktop platforms including Chrome, Firefox, Safari, Edge, Internet Explorer, and Opera (The Mark Text element - HTML: HyperText Markup Language). Mobile support includes Webview Android, Firefox for Android, Opera Android, Chrome Android, Safari on iOS, and Samsung Internet (mark Tag in HTML).


## Accessibility Considerations

Accessibility considerations for the `<mark>` element require attention to ensure screen reader users receive appropriate information about highlighted content. By default, most screen readers do not announce marked text, which can result in accessibility barriers for users who rely on voice navigation (mark Tag in HTML).

To address this, developers can use CSS content property along with ::before and ::after pseudo-elements to generate announcements for screen readers (The Mark Text element - HTML: HyperText Markup Language). Implementing this technique ensures consistent highlighting functionality across all browsers and assistive technologies, providing equivalent access to highlighted content for all users.

The element should always be used in conjunction with proper semantic markup to convey its intended meaning clearly to both sighted and screen reader users. While the background color provides visual distinction, the text content must remain readable and accessible through alternative means (WebReference).

Best practices for implementing `<mark>` include ensuring sufficient contrast between the background color and text, providing alternative text or ARIA labels for screen reader users, and testing content across multiple browsers and assistive technologies (WebReference). Proper implementation ensures that the element maintains its accessibility benefits while providing clear, relevant highlighting for all users.


## Use Cases and Best Practices

The `<mark>` element finds particularly effective use in search result highlighting, where it can dynamically mark matching keywords within the surrounding text (WebReference, How to Use the HTML5 Mark Element). For example:

```html

<p>Looking for information on <mark>web development</mark>? Our tutorials cover everything from basic HTML to advanced frameworks.</p>

```

Implemented with JavaScript, this approach allows for real-time matching of user queries across web documents, providing immediate visual feedback (WebReference, How to Highlight Text in HTML: A Comprehensive Guide).

Highlighting important keywords also benefits content scanning, helping users quickly identify key concepts (WebReference, How to Highlight Text in HTML: A Comprehensive Guide):

```html

<p>Web development requires knowledge of multiple technologies, including <mark>HTML</mark>, CSS, and JavaScript.</p>

```

For inline citations and quotations, the element can draw attention to specific words or phrases while preserving the original text (WebReference, 4.6.19 The mark element — HTML5: Edition for Web Authors). For instance:

```html

<p>Modern web development requires a diverse skill set. As <mark>Tim Berners-Lee</mark> noted, "The future of the Web is <mark>semantics</mark>"</p>

```

This allows readers to focus on key points without altering the original quotation's structure (WebReference, 4.6.19 The mark element — HTML5: Edition for Web Authors). The element's limited scope ensures that only relevant text is highlighted, preventing unnecessary disruption to the document's flow (WebReference, How To Use the HTML5 Mark Element).


## Browser Support and Implementation

The `<mark>` element has been designed for cross-platform compatibility, with consistent support across desktop and mobile browsers since 2015 (HTML mark Tag). It functions as a paired tag, requiring both opening and closing markers, and supports a comprehensive array of global and event attributes (mark Tag in HTML).

The element's basic functionality - text highlighting with a yellow background - has reached widespread implementation across major desktop and mobile platforms. Browser support includes Chrome, Firefox, Safari, Edge, Internet Explorer, and Opera for desktop environments, while mobile support spans Webview Android, Firefox for Android, Opera Android, Chrome Android, Safari on iOS, and Samsung Internet (mark Tag in HTML).

The `<mark>` tag's technical requirements mirror its intended usage - it accepts phrasing content within flow content, making it compatible with a wide array of document structures. Developers can implement the element using standard HTML5 practices, with basic syntax including the `<mark>` and `</mark>` tags surrounding the text to be highlighted (mark Tag in HTML).

For developers working with older HTML versions, the `<mark>` element maintains backward compatibility through its implementation in HTML 4.01 Transitional and XHTML 1.0 Transitional standards. The element's core functionality remains consistent across these older standards, allowing for seamless integration into existing web projects (HTML: `<mark>` tag).

The element's implementation across browsers demonstrates its versatility as a semantic marking tool. Its support for global attributes and event handlers enables developers to enhance user interaction while maintaining document structure (mark Tag in HTML). As a fundamental HTML5 element, the `<mark>` tag represents text marked for reference or notation purposes, providing a standardized way to highlight content across modern web platforms (mark – marked (highlighted) text (NEW) - HTML5).

## References

- [HTML The HTML Document Root Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20HTML%20Document%20Root%20Element.md)
- [HTML Script Type Attribute](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Script%20Type%20Attribute.md)
- [HTML The Noscript Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Noscript%20Element.md)
- [HTML Marquee The Marquee Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Marquee%20The%20Marquee%20Element.md)
- [HTML bdi The Bidirectional Isolate Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20bdi%20The%20Bidirectional%20Isolate%20Element.md)