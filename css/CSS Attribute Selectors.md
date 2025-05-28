---

title: CSS Attribute Selectors: Target Elements Based on Their Attributes

date: 2025-05-26

---


# CSS Attribute Selectors: Target Elements Based on Their Attributes

CSS attribute selectors offer precise control over which HTML elements receive specific styles, allowing developers to target elements based on their attribute presence, value, or substring content. These selectors enable efficient management of complex HTML structures, particularly in content management systems where auto-generated class names add complexity. This article explores the essential attribute selectors, demonstrating how to target elements by attribute presence, exact value, substring content, and attribute prefixes. Through practical examples and case studies, we will demonstrate how to use these selectors effectively while maintaining optimal performance.


## Basic Attribute Selectors

The fundamental structure of an attribute selector consists of the attribute name enclosed in square brackets [attribute]. This basic selector targets all elements with that specific attribute. For example, [type] would match any element containing a type attribute.

To target elements with a specific attribute-value pair, use the syntax [attribute="value"]. This ensures that the selected elements have both the attribute and the exact value specified. For instance, [type="submit"] would style all submit buttons.

More specific requirements can be achieved through various attribute value selectors:

- [attribute~="value"] matches elements where the attribute value contains a specific word, with the value separated by spaces. This selector is useful for matching elements within a space-separated list of words. For example, [title~="flower"] would match elements with a title containing "flower", regardless of its position in the list.

- [attribute|="value"] matches elements where the attribute value is exactly equal to the specified value or begins with that value followed by a hyphen. This is particularly useful for language attributes, allowing for matches like [lang|="en"] to target elements with lang="en-US" or lang="en-GB".

- [attribute^="value"] matches elements where the attribute value begins with the specified substring. For example, [class^="top"] would select elements with a class starting with "top".

- [attribute$="value"] matches elements where the attribute value ends with the specified substring. This can be used to target specific elements within a document structure, such as [class$="test"] selecting elements whose class ends with "test".

- [attribute*="value"] matches elements where the attribute value contains the specified substring anywhere within the value. For instance, [class*="room"] would select elements whose class contains "room" in any position.

These selectors offer significant advantages for managing HTML structures, particularly in content management systems where auto-generated class names can cause issues. They enable precise targeting of elements without relying on class or ID attributes, promoting cleaner markup and more maintainable CSS stylesheets.


## Attribute Value Selectors

The [attribute="value"] selector targets elements with both the attribute and the exact value specified. For example, [type="submit"] styles all submit buttons.

To match elements where the attribute value contains a specific word, use [attribute~="value"]. This works with space-separated values, matching elements like [title~="flower"] that contain "flower" regardless of its position in the list.

The [attribute|="value"] selector matches elements where the attribute value is exactly equal to the specified value or begins with that value followed by a hyphen. This is particularly useful for language attributes, allowing for matches like [lang|="en"] to target elements with lang="en-US" or lang="en-GB".

The [attribute^="value"] selector matches elements where the attribute value begins with the specified substring. For example, [class^="top"] selects elements with a class starting with "top". Similarly, [attribute$="value"] matches elements where the attribute value ends with the specified substring, as in [class$="test"] selecting elements whose class ends with "test".

The [attribute*="value"] selector matches elements where the attribute value contains the specified substring anywhere within the value. For instance, [class*="room"] selects elements whose class contains "room" in any position. These selectors provide significant advantages for managing HTML structures, particularly in content management systems where auto-generated class names can cause issues.


## Substring Matching Selectors

The three main types of attribute selectors covered in this lesson allow web developers to target elements based on the presence, value, or substring matching of their attributes. These selectors provide a powerful way to style elements without relying solely on class or ID attributes, making them particularly useful for managing auto-generated class names in content management systems.

**Presence Selectors**

The most basic use of attribute selectors, represented by `[attr]`, matches any element that contains the specified attribute, regardless of its value. For example, using `[title]` would select all elements containing a title attribute, except the first one, as demonstrated in the MDN documentation.

**Value Selectors**

For elements with specific attribute values, the `[attr="value"]` structure targets matches exactly. This is particularly useful for styling form elements, as shown in the example: `input[type="text"] { width: 150px; display: block; margin-bottom: 10px; background-color: yellow; }`. This selector ensures that only elements with a type attribute set to "text" will be affected by the styling.

**Substring Matching Selectors**

The most versatile subset of attribute selectors allows matching based on attribute values containing specific substrings. For example, `[href*="example"]` would match any element with an href attribute containing "example" anywhere in its value. This capability is demonstrated in the MDN documentation with examples like [href^="tel:"], which selects telephone links with a background color of #2196f3 and applies a phone icon image.

These substring matching selectors also support additional patterns for precise targeting:

- `[attr^="value"]` matches elements where the attribute value begins with the specified substring. For instance, `[class^="box-"]` selects elements with a class starting with "box-".

- `[attr$="value"]` matches elements where the attribute value ends with the specified substring. The example `[class$="-box"]` matches both sports-sidebar and arts-sidebar classes.

- `[attr*=value]` matches elements where the attribute value contains the specified substring anywhere within the string. The example `[class*="room"]` selects elements whose class contains "room" in any position.

The substring matching selectors can be combined with other attributes for even more precise targeting, such as `input[type="text"][required]`, which selects required text input fields. While these selectors generally perform slower than class and ID selectors, their enhanced targeting capabilities significantly improve code maintainability and HTML structure management.


## Hyphenated and Special Attribute Selectors

Hyphenated attribute selectors allow matching elements based on attribute names containing specific prefixes. For instance, the selector [class|="articlepromo"] applies specific styles to elements with class attributes that start with "articlepromo". This selector structure enables targetted styling for elements with related class naming conventions.

The [attr^="value"] selector matches elements where the attribute value begins with the specified substring. Following the MDN documentation's examples, [class^="box-"] selects elements with a class attribute starting with "box-". The [attr$="value"] selector performs the opposite operation, matching elements where the attribute value ends with the specified substring. Using the provided documentation's example, [class$="-box"] matches elements with class attributes ending in "-box", including both sports-sidebar and arts-sidebar classes.

The most versatile substring matching capability is provided by [attr*=value], which matches elements where the attribute value contains the specified substring anywhere within the string. The [class*="box"] selector demonstrates this functionality by selecting elements whose class attributes contain "box" in any position. These selectors can be combined with others for more specific targeting, as shown in the example [input[type="text"][required]], which selects required text input fields while [input[type="text"]] applies styles to all text input fields.

The MDN documentation provides detailed examples of these selectors in action, including [href^="tel:"] for telephone links with a specific background color and phone icon image, [href$="5555"] for links ending in 5555 with distinct styling, and [class$=sidebar] for elements ending with "-sidebar" classes. The attribute selector framework extends beyond these basic examples, supporting additional functionality through CSS3 and CSS4 pseudo-classes and elements.

These selectors offer powerful capabilities for managing complex HTML structures, particularly in scenarios requiring precise attribute matching rather than relying on class or ID attributes. However, developers should weigh the benefits against potential performance considerations, especially when targeting large document structures, as the substring matching selectors generally perform slower than class and ID selectors.


## Case Sensitivity and Browser Support

By default, CSS attribute selectors are case sensitive. This means that [title="example"] would only match elements with the exact case of "example", including capitalization. To perform case-insensitive matching, add the "i" flag after the attribute name. For example, [data-state="open" i] would match <div data-state="open"></div>, <div data-state="Open"></div>, <div data-state="OPEN"></div>, <div data-state="oPeN"></div>, allowing for flexible matching of attribute values regardless of their case.

The attr() function extends attribute selectors by enabling dynamic content generation based on attribute values. For instance, .el::before { content: attr(data-prefix) ": "; } would insert the value of the data-prefix attribute before the pseudo-element content. This function supports optional "type" and "fallback" features, enhancing its functionality for conditional styling based on attribute values.

Browser compatibility spans all modern browsers, including Internet Explorer down to version 7, making attribute selectors widely accessible. While these selectors work seamlessly with the cascade and :not() selector for targeted styling, developers should consider creating separate stylesheets for older IE versions. The MDN documentation provides comprehensive support through a dedicated test page at https://css-tricks.com/examples/AttributeSelectors/, demonstrating practical applications while highlighting potential limitations in older browser implementations.

The attribute selector framework extends beyond basic usage, supporting sophisticated pattern matching. For example, [href$=".org"] would select links ending with ".org", while [href*="example"] matches any link containing "example" anywhere in its URL. These capabilities prove particularly valuable when managing complex HTML structures, especially in content management systems where auto-generated class names can cause issues. However, developers should maintain awareness of potential performance implications, particularly when targeting large document structures, as substring matching selectors generally perform slower than class and ID selectors.

