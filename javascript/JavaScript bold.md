---

title: JavaScript String Formatting: The bold() Method

date: 2025-05-26

---


# JavaScript String Formatting: The bold() Method

JavaScript's string formatting capabilities have evolved significantly since the language's early days, with modern APIs offering more flexible and standards-compliant alternatives to traditional methods. One such legacy feature is the bold() method, which wraps text in <b> tags for bold display. While still functional in current browsers, this method has been deprecated and is no longer recommended for new development. Understanding its behavior and limitations is crucial for modern JavaScript developers transitioning to more maintainable text formatting practices.


## Introduction to String Formatting in JavaScript

In JavaScript, string formatting options include methods that create HTML elements around the text, such as bold(). This approach allows for displaying text as bold using the <b> tag. When invoked on a string object, the bold() method returns a copy of the string with <b> tags surrounding it.

For example, when applied to a new String instance containing "Hello world", the bold() method produces "<b>Hello world</b>". Similarly, concatenating multiple strings and applying bold() generates "<b>Hello, World!</b>". The method maintains its functionality in various scenarios, including when the original string contains other HTML elements, as demonstrated by the output "<b>Hello, <em>World!</em></b>".

Despite its utility, the bold() method is deprecated in modern JavaScript. The latest specification places it under HTML wrapper methods, which are considered legacy features maintained for compatibility reasons. As noted by the Mozilla Developer Network, this feature may be removed from web standards at any time, and developers are encouraged to transition their code to alternative approaches where possible.

The method's implementation creates the <b> tag directly, making it a direct translation of the HTML element for displaying bold text. However, the method's status as deprecated means it should be used cautiously, particularly in new development projects. Modern JavaScript practices increasingly favor CSS-based styling for text formatting, with HTML wrapper methods like bold() reserved for limited compatibility scenarios.


## The bold() Method and Its Usage

The bold() method produces a string that includes the original string within a <b> element, making it display in bold in HTML5. This method is deprecated and only standardized for compatibility purposes. Modern JavaScript practices increasingly favor CSS-based styling for text formatting, with HTML wrapper methods like bold() reserved for limited compatibility scenarios.


### Implementation Example

To demonstrate its implementation, consider the following JavaScript code:

```javascript

var totn_string = 'TechOnTheNet';

console.log(totn_string.bold());

```

This will output: <b>TechOnTheNet</b>


### Usage with Multiple Strings

The method can also concatenate multiple strings before applying bold formatting:

```javascript

let str1 = "Hello, ";

let str2 = "World!";

console.log((str1 + str2).bold()); // Output: <b>Hello, World!</b>

```


### Handling Existing HTML Elements

When applied to strings containing other HTML elements, the bold() method maintains its functionality:

```javascript

let str = "Hello, <em>World!</em>";

console.log(str.bold()); // Output: <b>Hello, <em>World!</em></b>

```


### Browser Compatibility

The method is available in all modern browsers and continues to function as expected. However, its deprecated status means developers are encouraged to transition to alternative approaches, particularly for new development projects.


## Method Implementation and Browser Compatibility

The bold() method creates the HTML <b> element, as documented in the Mozilla Developer Network (MDN) resources. It returns a string embedded within these tags, causing the text to display as bold according to HTML5 standards. The method's implementation simply wraps the original string in <b> and </b> tags, producing an output like "<b>Original Text</b>" when called.

The method follows the JavaScript specification detailed in ECMAScript 2026, section "String.prototype.bold." This indicates its official implementation and compatibility across modern browser environments. The MDN documentation explicitly notes that the method is deprecated and only maintained for compatibility purposes, suggesting developers avoid its use in new projects and consider alternative approaches.

The method's behavior remains consistent across all modern browsers, as stated in the MDN documentation. However, its deprecated status means this functionality may be removed from web standards at any time, aligning with the Mozilla resources' guidance on its eventual removal from web standards. When implementing text formatting, developers are advised to use DOM APIs like `document.createElement` instead of relying on deprecated methods like bold().


## Alternatives to the bold() Method

The bold() method has been deprecated and is no longer recommended for use in JavaScript development. For modern text formatting, developers should consider alternative methods that provide more flexibility and control.

The simplest alternative is to use HTML <b> tags directly. This approach requires setting the innerHTML property of a DOM element, rather than formatting the string directly. For example:

```javascript

document.getElementById('myDiv').innerHTML = '<b>' + userInput + '</b>';

```

CSS provides several more versatile options for text formatting. The font-weight property allows specifying bold levels directly:

```javascript

Object.style.fontWeight = "bold";

```

This method applies bold styling to the entire element containing the text. Modern JavaScript development typically encourages using these CSS-based approaches rather than modifying strings with deprecated methods.

For cases where text needs to be dynamically formatted, there are several robust solutions available:

1. Regular Expression Replacement: The developer can create a function that replaces occurrences of the substring with wrapped <b> tags using regular expressions. This approach provides precise control over which text is formatted.

2. ES6+ Solution: Using the replace() method with a regular expression allows replacing all occurrences of the substring with the wrapped version. This approach works in environments supporting ES6 or later.

3. Pure JavaScript Case-Insensitive Solution: For developers who need to preserve case sensitivity, a custom function can convert both the string and query to uppercase for comparison while maintaining the original case in the result.

These modern approaches offer more flexibility, maintainability, and alignment with current web development standards. While the deprecated bold() method may still function in existing codebases, its lack of support in newer JavaScript specifications and the potential removal from web standards make it unsuitable for new development projects.


## Best Practices for String Formatting

Modern JavaScript development increasingly favors CSS-based styling over HTML wrapper methods like bold(). The font-weight property provides precise control over text boldness, with available values including normal, lighter, bold, bolder, and specific numerical values. This approach offers greater flexibility compared to the deprecated bold() method.

For developers needing to make specific parts of a string bold, several modern solutions are available. Regular expression replacement allows precise control over which text is formatted, as demonstrated in various code snippets. The ES6 solution uses `str.replace()` with regular expressions to find all occurrences of the substring and wrap them in <b> tags. The ES12 solution utilizes the new `replaceAll()` method for simpler replacement when supported.

When implementing text formatting, developers are advised to use DOM APIs like `document.createElement` rather than relying on deprecated methods. Modern approaches provide better performance, maintainability, and alignment with current web development standards. While the deprecated bold() method may still function in existing codebases, its lack of support in newer JavaScript specifications and potential removal from web standards make it unsuitable for new development projects.

