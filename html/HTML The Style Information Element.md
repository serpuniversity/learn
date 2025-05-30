---

title: HTML Style Information Element

date: 2025-05-29

---


# HTML Style Information Element

The `<style>` tag in HTML enables developers to apply CSS directly to their content, offering powerful styling capabilities while maintaining document structure. This article explores the tag's attributes, supported properties, and best practices for web development, covering essential aspects of HTML styling from basic implementation to advanced responsive design techniques.


## HTML `<style>` Tag

The `<style>` tag defines style information for an HTML document, allowing developers to apply CSS directly to their content. It must be placed inside the `<head>` section of the document and supports two attributes: media and type. The media attribute specifies which media/device the media resource is optimized for, while the type attribute defines the styling language as a MIME type, defaulting to text/css.

The `<style>` tag can contain multiple style elements, with styles applied in the order they appear. Styles defined within `<style>` tags override earlier styles with the same property if the later style has higher specificity. For example, a style applied with the scoped attribute limits the scope of its styles to the parent element and its children, potentially reintroduced in future updates.

Developers can use `<style>` elements for small-scale projects or dynamic styling through scripting. While modern web documents rarely need the type attribute, the media attribute enables conditional styling based on media features like viewport width via media queries. For instance, the attribute value "all and (max-width: 600px)" applies styles to all media types when the viewport's width is 600 pixels or narrower. This functionality can be tested using browser Developer Tools.


## CSS Properties and Values

The CSS properties supported by the `<style>` tag encompass a wide range of formatting options, allowing developers to control nearly every aspect of an HTML document's presentation. These properties include fundamental elements such as color, font-family, and font-size, as well as more specific attributes like border, padding, and margin.

The color property determines the text color of an HTML element, while font-family specifies the font type. Font size can be adjusted using the font-size property, which supports various units including pixels, ems, and percentages. The border property defines the appearance of a border around HTML elements, while padding and margin control the space between text and borders, as well as the distance between elements.

When applied through the `<style>` tag, these properties exert cumulative effects based on their specificity and order of declaration. For example, setting a style rule like "h3 { color: red; font-size: 25px; font-style: italic; }" would apply red text with italic styling to all `<h3>` elements. A subsequent rule targeting a specific width, such as "h3 { color: green; font-size: 30px; font-weight: bolder; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; }" when the viewport width is 500px or less, would override the initial properties while maintaining the green color and increased font size.

These fundamental CSS properties form the basis for effective HTML styling, enabling developers to create both simple and complex visual presentations while maintaining the document's semantic structure. The `<style>` tag's support for these properties, combined with its flexibility through media queries and specific attribute targeting, provides web developers with robust tools for creating consistent, responsive designs across multiple pages and devices.


## Internal vs. External CSS

In HTML, style information can be applied through three primary methods: inline styles, embedded style sheets, and external style sheets. Each approach offers distinct advantages and considerations for web development.

Inline styles, defined using the style attribute within HTML elements, are the most specific form of styling, overriding both embedded and external styles. While powerful for precise control, inline styles are generally discouraged due to their maintenance challenges and potential repetition across multiple elements. For example:

```html

<h1 style="color: blue;">A Blue Heading</h1>

<p style="color: red;">A red paragraph.</p>

```

Embedded style sheets, defined within the `<head>` section using the `<style>` tag, offer improved maintainability by centralizing style definitions. Multiple `<style>` elements can be included within a single document. However, these styles have higher specificity than inline styles and lower priority than external stylesheets. Example syntax:

```html

<head>

<style>

body { background-color: powderblue; }

h1 { color: blue; }

p { color: red; }

</style>

</head>

```

External style sheets provide the greatest flexibility and maintainability by separating style definitions from content. These are referenced using the `<link>` element or the @import rule within `<style>` tags. External stylesheets must be saved with a .css extension and can be referenced via full URLs or relative paths. The preferred method for applying styles across multiple pages, external sheets allow for centralized updates through a single file modification:

```html

<!DOCTYPE html>

<html>

<head>

<link rel="stylesheet" href="styles.css">

</head>

<body>

<h1>This is a heading</h1>

<p>This is a paragraph.</p>

</body>

</html>

```

The choice between these stylesheets depends on project scope and maintenance requirements. Inline styles are best for temporary or single-use styling, while embedded styles sheets offer improved readability for small projects. For larger developments, external style sheets provide the most scalable solution through centralized management and improved performance.


## Media Queries and Responsive Design

Media queries within `<style>` tags enable developers to apply different styles based on screen size and device type. The `<style>` element supports the media attribute, which allows styles to be applied conditionally based on viewport size. For example, the attribute value "all and (max-width: 600px)" indicates that the styles apply to all media types (screen and print) and activate when the viewport's width is 600 pixels or narrower.

To implement media queries, web developers can define styles using standard CSS syntax within `<style>` tags. The browser applies these styles based on the specified media conditions. Here is an example demonstrating the use of media queries with the `<style>` tag:

```html

<!DOCTYPE html>

<html lang="en">

<head>

<style>

h3 { color: red; font-size: 25px; font-style: italic; }

</style>

<style media="all and (max-width: 500px)">

h3 { color: green; font-size: 30px; font-weight: bolder; }

</head>

<body>

<h3>Responsive heading</h3>

</body>

</html>

```

In this example, the initial style declaration sets red text with an italic font for all `<h3>` elements. When the viewport width is 500 pixels or less, the media query condition is met, and the subsequent style declaration overrides the previous properties while maintaining the green color and increased font size.

Developers can use media queries to create flexible, responsive designs that adapt to various screen sizes and devices. The MDN Web Docs specify that the `<style>` element has been available across many devices and browser versions since July 2015, though some features may have varying levels of support. The element supports global attributes and includes specific attributes like media, which defines the media types for which the style is applied. The media attribute accepts media queries, allowing for precise control over when styles are applied based on device characteristics.


## Common Styling Mistakes

While the `<style>` tag provides powerful styling capabilities, several common mistakes can undermine its effectiveness and efficiency. The first major issue is improper syntax, particularly with missing or incorrect punctuation. For instance, failing to separate property-value pairs with semicolons or forgetting to close curly braces can prevent styles from rendering correctly.

A second frequent error is overuse of inline styles, which can make HTML documents cluttered and difficult to maintain. The `<style>` tag is specifically designed for internal styling, and applying styles through HTML elements (e.g., `<h1 style="color:red;">`This is a heading`</h1>`) is generally discouraged due to its high specificity and integration with content. While inline styles are necessary for immediate display requirements, they should be used sparingly and preferably only for critical or one-time styling needs.

Another common mistake is insufficient understanding of CSS specificity rules. Developers often struggle when later style declarations override earlier ones due to higher specificity. For example, a style applied with higher selector weight (e.g., ID selectors) will override more generic rules. To avoid this, it's important to understand selector precedence and use more specific selectors only when necessary.

The misuse of the type attribute represents a third frequent error. Although it defines the styling language as a MIME type (defaulting to text/css), modern web documents rarely require this attribute. Its inclusion can sometimes cause parsing issues, especially in older browsers. When using external stylesheets, always validate URLs and paths to ensure correct file references.

Finally, developers often overlook proper attribute usage, particularly with media queries and the deprecated scoped attribute. While the media attribute enables conditional styling based on viewport size, its implementation requires careful consideration of media feature syntax. Similarly, the scoped attribute, which limits style application to parent elements and children, should be used judiciously as it may affect cross-element styling requirements. Always test media queries across multiple devices and screen sizes to ensure consistent rendering.

These common errors highlight the importance of following best practices for efficient CSS development. By maintaining proper syntax, avoiding inline styles where possible, understanding specificity rules, using appropriate attributes, and thoroughly testing styles across devices, developers can create maintainable, efficient, and effective web designs using the `<style>` tag.

## References

- [HTML Colgroup The Table Column Group Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Colgroup%20The%20Table%20Column%20Group%20Element.md)
- [HTML Fieldset The Field set Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Fieldset%20The%20Field%20set%20Element.md)
- [HTML pre The Preformatted Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20pre%20The%20Preformatted%20Text%20Element.md)
- [HTML Iframe The Inline Frame Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Iframe%20The%20Inline%20Frame%20Element.md)
- [HTML Spellcheck](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Spellcheck.md)