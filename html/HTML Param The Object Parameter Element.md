---

title: HTML `<param>`: The Object Parameter Element

date: 2025-05-29

---


# HTML `<param>`: The Object Parameter Element

The `<param>` tag enables developers to associate parameters with object elements, offering flexibility through attributes like name, value, valuetype, and type. While this valuable tool for embedded content management has maintained support across major browsers since HTML 3.2, it's important to understand its proper usage and limitations as web standards continue to evolve.


## Introduction to `<param>`

The `<param>` tag enables developers to associate parameters with object elements, where it must appear before any flow content. This tag supports essential attributes, including name and value, both of which are required for its proper function.

The name attribute defines the parameter's identifier, while the value attribute contains its corresponding information. These attributes follow no specific format restrictions, allowing developers to specify any appropriate content. The `<param>` element itself carries no content; instead, it acts as a container for these attribute pairs.

A critical feature of the `<param>` tag is its ability to handle different types of parameter values through its valuetype attribute. This attribute accepts three possible values: data (the default), ref, and object. When valuetype is set to data, the parameter value is treated as a simple string. If ref is specified, the value represents a URI that won't be resolved to a full URL, with the responsibility of resolution falling to the Java class handling the object. Setting valuetype to object enables the PARAM to reference identifiers of separate OBJECT elements within the same document, facilitating complex interactions between different content pieces.

The type attribute allows developers to specify the Internet media type of the resource referenced by the value attribute. This can help ensure that embedded objects receive the correct data they need to function properly. While supported in all major browsers since HTML 3.2, `<param>` has been deprecated in modern web standards and is maintained primarily for compatibility purposes. Despite its age, this element remains a practical tool for passing runtime parameters to embedded objects and plugins.


## Syntax and Basic Usage

The `<param>` tag is used to define parameters for object elements, appearing before flow content and requiring both name and value attributes. Both the name and value attributes accept any appropriate content without format restrictions. While the tag carries no content itself, it acts as a container for these attribute pairs.

The `<param>` tag supports several important attributes beyond name and value:

- Type: Specifies the Internet media type of the resource referenced by the value attribute. This helps ensure embedded objects receive the correct data they need to function properly.

- Valuetype: Specifies the type of the value attribute, accepting three possible values: data (the default), ref, and object. When valuetype is set to data, the parameter value is treated as a simple string. If ref is specified, the value represents a URI that won't be resolved to a full URL - the responsibility for resolution falls to the Java class handling the object. Setting valuetype to object enables the PARAM to reference identifiers of separate OBJECT elements within the same document, facilitating complex interactions between different content pieces.

The `<param>` tag employs a simple syntax, appearing as a void element without an end tag:

`<param attribute="value" />`

The opening `<param>` tag must contain exactly one attribute. The void element syntax requires a start tag but prohibits an end tag. This structural requirement aligns with HTML5's classification of `<param>` as a void element.


## Parameter Object in DOM

The Parameter object represents an HTML `<param>` element and provides methods to access and manipulate parameter attributes through JavaScript. This object enables developers to interact with `<param>` elements in the Document Object Model (DOM), allowing for dynamic modification of parameter values and attributes.

To access a `<param>` element, developers can use the document.getElementById() method, returning a Parameter object that can then be manipulated through its properties. For example:

```javascript

var x = document.getElementById("myParam");

```

Alternatively, developers can create a `<param>` element using document.createElement("PARAM"), providing a JavaScript object with attributes as its second parameter. This approach allows for programmatically constructing parameter elements before adding them to the DOM.

The Parameter object supports two primary properties: name and value. These properties allow developers to set or retrieve the corresponding attributes of a `<param>` element:

```javascript

// Accessing the name value

var x = document.getElementById("myParam").name;

// Creating a param element

var x = document.createElement("PARAM");

x.setAttribute("name", "autoplay");

x.setAttribute("value", "true");

```

Developers can also query the document for all `<param>` elements using methods like getElementsByTagName(), though these elements display with display: none by default in most browsers. The Parameter object's DOM interface aligns with the HTML5 specification, providing direct access to the element's attributes through its interface definition:

interface HTMLParamElement : HTMLElement {

  attribute DOMString name;

  attribute DOMString value;

};

This alignment ensures developers can reliably interact with `<param>` elements across modern browsers, including Google Chrome 5.0, Internet Explorer 8.0, Firefox 3.6, Safari 5.0, and Opera 10.6, among others.


## Browser Support and Standards

The `<param>` element has been supported in major browsers since HTML 3.2, with the W3C HTML 3.2 Specification and WDG HTML 3.2 Reference both dating the element's inclusion to this early standard. While the element has maintained support across all major browsers, it has evolved alongside changes in web standards and browser capabilities.

The element's functionality has centered on two primary contexts, as detailed in the W3C HTML 4.01 Specification and the W3C HTML 4.01 Transitional document. When used with the value attribute, `<param>` allows developers to pass URIs to embedded objects without resolving them to full URLs, with the responsibility for resolution falling to the Java class handling the object. This feature has proven particularly useful for managing resources like images or multimedia files that may require partial URIs.

When valuetype is set to "object," `<param>` enables the element to reference identifiers of separate OBJECT elements within the same document. This capability has proven valuable for creating complex interactions between different content pieces, allowing developers to manage and reference external resources through a single parameter element.

The element's specifications have consistently maintained its role as a container for runtime parameters, with the W3C HTML 4.01 Frameset document confirming its empty content model and void element status. This structural design aligns with its intended use as a descriptor for object parameters, providing a clear interface for passing configuration information to embedded content while maintaining separation from flow content.

As a component of the HTML5 Web Components suite, the `<param>` element has incorporated features from its earlier specifications while maintaining compatibility with legacy implementations. The HTML5 specification explicitly defines its DOM interface as an extension of the HTMLElement interface, providing direct access to name and value properties through JavaScript. This compatibility has ensured that existing applications continue to function while allowing for modern development practices.

## References

- [HTML Date And Time Formats Used In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Date%20And%20Time%20Formats%20Used%20In%20HTML.md)
- [HTML Attribute Maxlength](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Maxlength.md)
- [HTML Script The Script Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Script%20The%20Script%20Element.md)
- [HTML big The Bigger Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20big%20The%20Bigger%20Text%20Element.md)
- [HTML pre The Preformatted Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20pre%20The%20Preformatted%20Text%20Element.md)