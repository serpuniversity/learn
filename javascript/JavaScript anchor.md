---

title: JavaScript String anchor() Method

date: 2025-05-27

---


# JavaScript String anchor() Method

Creating HTML anchor elements has traditionally been handled through JavaScript methods, with the anchor() method being one such approach. This article explores the functionality of the anchor() method, its syntax, and parameter requirements. We'll examine how it generates HTML <a> elements with specific name attributes, providing examples of its usage. Additionally, we'll discuss the method's limitations, deprecation status, and why developers are encouraged to use modern DOM APIs like document.createElement() for creating anchor tags.


## Creating HTML Anchors

The anchor() method creates an HTML <a> element with the provided name attribute. This string method requires a single parameter: the name attribute value for the <a> element.

The method syntax is string.anchor(anchor_name), where anchor_name is a string value that becomes the name attribute of the <a> element. It returns a string containing the <a> element, with the original string value enclosed in <a> and </a> tags as the hyperlink text, and the anchor_name parameter used as the name attribute.

For example, the code "GFG".anchor("anchorname") returns <a name="anchorname">GFG</a>. Similarly, "GeeksForGeeks".anchor("anchorname") returns <a name="anchorname">GeeksForGeeks</a>. The original string value is embedded within the <a> and </a> tags, with the anchor_name used as the name attribute.

This method has been deprecated since JavaScript 1.0 and may no longer function in modern browsers. For valid HTML, developers are encouraged to use DOM APIs like document.createElement() instead. Support is limited to Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10.


## Method Syntax and Parameters

The anchor() method creates an HTML <a> element with the provided name attribute. It requires a single parameter: the name attribute value for the <a> element. The method syntax is string.anchor(anchor_name), where anchor_name is a string value used as the name attribute.

The method returns a string containing the <a> element, with the original string value enclosed in <a> and </a> tags as the hyperlink text, and theanchor_name parameter used as the name attribute. For example, "GFG".anchor("anchorname") returns <a name="anchorname">GFG</a>, while "GeeksForGeeks".anchor("anchorname") returns <a name="anchorname">GeeksForGeeks</a>. The original string value is embedded within the <a> and </a> tags, with the anchor_name used as the name attribute.

The method does not change the value of the original string. It is specifically designed to create a hyperlink target (the "name" attribute) rather than generating clickable links. For valid HTML, developers are encouraged to use DOM APIs like document.createElement() instead. Support is limited to Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10.


## Deprecation Notice

The anchor() method is deprecated and may stop working in browsers at any time. This string method creates an HTML <a> element with the provided name attribute. It requires a single parameter: the name attribute value for the <a> element.

The method syntax is string.anchor(anchor_name), where anchor_name is a string value used as the name attribute. It returns a string containing the <a> element, with the original string value enclosed in <a> and </a> tags as the hyperlink text, and the anchor_name parameter used as the name attribute. For example, "GFG".anchor("anchorname") returns <a name="anchorname">GFG</a>, while "GeeksForGeeks".anchor("anchorname") returns <a name="anchorname">GeeksForGeeks</a>. The original string value is embedded within the <a> and </a> tags, with the anchor_name used as the name attribute.

The method creates invalid HTML because the <a> element no longer allows the name attribute. For valid HTML, developers should use DOM APIs like document.createElement() instead. Support for the method is limited to Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10. The method is not supported in modern browsers and is included in the ECMAScript 2026 Language Specification only for compatibility purposes.


## Example Usage

The anchor() method returns a string containing an <a> element with the original string value as the hyperlink text and the specified name attribute. For example, "GFG".anchor("anchorname") returns <a name="anchorname">GFG</a>, while "GeeksForGeeks".anchor("anchorname") returns <a name="anchorname">GeeksForGeeks</a>. The original string value is embedded within the <a> and </a> tags, with the anchor_name used as the name attribute.

When creating anchor tags in JavaScript, it's important to consider best practices for event handling and HTML creation. While the method can generate valid anchor tags, modern approaches recommend using the DOM API's document.createElement() method for more control and security. For example, to create an anchor tag with JavaScript, you can use the following code:

```javascript

var text = "Learn JavaScript";

document.write(document.createElement('a').assign({name: "txtanchor", innerText: text}));

```

This approach creates a new anchor element, sets its name attribute, and appends the text content. It provides better control over the DOM structure and avoids potential security issues associated with inline event handlers or direct string concatenation.

The anchor() method has been deprecated since JavaScript 1.0 and is not recommended for use in modern web development. It is included in the ECMAScript 2026 Language Specification only for compatibility purposes and may cease to function in browsers at any time. For valid HTML, developers should use DOM APIs like document.createElement() instead. Support for the method is limited to Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10, while modern browsers do not support it.


## Browser Compatibility

The method returns a string containing an <a> element with the original string value as the hyperlink text and the specified name attribute. For example, "GFG".anchor("anchorname") returns <a name="anchorname">GFG</a>, while "GeeksForGeeks".anchor("anchorname") returns <a name="anchorname">GeeksForGeeks</a>. The original string value is embedded within the <a> and </a> tags, with the anchor_name used as the name attribute.

When creating anchor tags in JavaScript, it's important to consider best practices for event handling and HTML creation. While the method can generate valid anchor tags, modern approaches recommend using the DOM API's document.createElement() method for more control and security. For example, to create an anchor tag with JavaScript, you can use the following code:

```javascript

var text = "Learn JavaScript";

document.write(document.createElement('a').assign({name: "txtanchor", innerText: text}));

```

This approach creates a new anchor element, sets its name attribute, and appends the text content. It provides better control over the DOM structure and avoids potential security issues associated with inline event handlers or direct string concatenation.

