---

title: JavaScript String strike() Method

date: 2025-05-27

---


# JavaScript String strike() Method

The strike() method in JavaScript offers a straightforward way to apply strikethrough formatting to text through the use of <strike> HTML tags. While this functionality has been part of JavaScript since version 1.0, its reliance on tags now deprecated in HTML5 makes it a method whose time has passed. Despite its current compatibility across major browsers, developers are encouraged to explore modern alternatives that align with current web standards. This article examines the method's functionality, implementation, and compatibility while highlighting why its use is no longer recommended for new projects.


## strike() Method Overview

The strike() method is a JavaScript string method that formats text to appear as struck-out or deleted content. It achieves this by wrapping the text in <strike> HTML tags, which visually represents the struck-through appearance. This functionality dates back to JavaScript 1.0, though the method has since become deprecated and is no longer recommended for use.

The method behaves as a standard string prototype method, requiring no parameters and returning a new string object with the <strike> tags applied. For example, calling `str.strike()` on a string "Hello world" produces the output `<strike>Hello world</strike>`. The method preserves existing markup, so a string containing HTML elements like `<strong>bold</strong>` would result in `<strike><strong>bold</strong></strike>` when the strike() method is applied.

While the method works across major browsers including Internet Explorer 7, Firefox 3.6, Chrome 7, Safari 5.0.1, and Opera 10, its use is discouraged due to the <strike> tag's removal from the HTML5 specification. As a deprecated feature, it may cease to function in browsers at any time, making alternative methods more suitable for modern web development projects.


## Method Implementation and Syntax

The strike() method creates a string wrapped in <strike> tags and returns it. It requires no parameters and is implemented in JavaScript 1.0. The method produces the same output as the HTML <strike> tag, making it appear as though the text has been struck out.

When invoked through a specific string instance, as in `str.strike()`, the method returns a copy of the original string enclosed in <strike> and </strike> tags. This functionality works across major browsers including Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10. However, since the method creates <strike> tags which are not supported in HTML5, its use is discouraged in modern web development projects.


## Example Usage

The strike() method can be used to create strikethrough text in several ways. For basic usage, you can directly call the method on a string variable, as shown in Example 1 where "Hello, World!" is converted to `<strike>Hello, World!</strike>` (Document 0). For concatenation, you can apply the method to combined strings, as demonstrated in Example 2 where "Hello, " and "World!" become `<strike>Hello, World!</strike>` (Document 0).

The method preserves existing markup, so applying it to a string containing HTML elements like <strong>bold</strong> will result in `<strike><strong>bold</strong></strike>`, as shown in Example 3 (Document 0). This makes it compatible with strings that may already contain formatted text.

For those looking to implement alternative strikethrough functionality, the method can be extended to create custom functionality. Document 9 provides two custom implementation examples: one using Unicode combining characters and another that maintains the original string's structure while applying the strikethrough effect through CSS classes.

However, developers should note that the strike() method is deprecated and no longer recommended for use in modern web development (Document 7). As an alternative, MDN recommends using the <del> element for deleted content or the <s> element for content that is no longer accurate or relevant (Document 7). The method remains available for compatibility purposes, but its usage is discouraged due to its removal from the HTML5 specification (Document 8).

The strike() method can also be extended through custom prototypes, as shown in Example 4 where a new method is added to String.prototype (Document 9). This allows developers to create consistent styling across their applications while also providing a way to remove the strikethrough effect through simple string operations (Document 9).


## Browser Compatibility

The strike() method is supported in major browsers including Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10. However, the method's functionality has been deprecated and may cease to work in browsers at any time due to its removal from the HTML5 specification (Document 8).

The method returns a string embedded in a <strike> element (`<strike>str</strike>`), causing the text to appear as struck-out (Document 0). It is implemented in JavaScript 1.0 and requires no parameters (Document 2).

When applied to a specific string instance (e.g., `str.strike()`), the method returns a copy of the original string enclosed in <strike> and </strike> tags (Document 0). For example, applying the method to "Hello world" produces `<strike>Hello world</strike>` (Document 0).

The method preserves existing markup, so applying it to a string containing HTML elements like <strong>bold</strong> results in `<strike><strong>bold</strong></strike>` (Document 0). This behavior makes it compatible with strings that may already contain formatted text.

For developers seeking alternative strikethrough functionality, the method creates a string that embeds the original string in a <strike> element (Document 11). While this method remains available for compatibility purposes, its usage is discouraged due to the <strike> tag's removal from the HTML5 specification (Document 11).

Modern web development should use the <del> element for deleted content or the <s> element for content that is no longer accurate or relevant instead of the strike() method (Document 11).


## Deprecation Notice

The strike() method has been deprecated and may cease to function in browsers at any time due to its removal from the HTML5 specification. While the method continues to work across major browsers including Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10, developers are strongly advised to use alternative methods for strikethrough formatting.

For developers seeking modern alternatives, the HTML <del> element is recommended for deleted content, while the <s> element should be used for content that is no longer accurate or relevant. Both of these elements provide proper semantic meaning and are supported in current web standards.

As a deprecated feature, the strike() method creates strings with <strike> tags, which are not supported in HTML5. For developers who need to maintain compatibility with older browsers while following modern standards, MDN provides several recommended approaches. These include using the <del> element for deleted content or the <s> element for content that needs to appear struck through.

