---

title: JavaScript String fontcolor() Method

date: 2025-05-26

---


# JavaScript String fontcolor() Method

The JavaScript String.fontcolor() method, implemented since JavaScript 1.0, creates HTML <font> elements with specified color attributes. While widely supported across major browsers, its use is discouraged due to <font> elements being deprecated in HTML5. Modern development should instead utilize CSS properties for text styling, though the fontcolor() method remains functional for backward compatibility.


## Overview of String.fontcolor()

The fontcolor() method creates an HTML <font> element with a specified color. It was implemented in JavaScript 1.0 and works with strings, using the syntax string.fontcolor(color_value), where color_value can be a color name or value (doc2).

The method generates <font> elements with the color attribute set to the specified value, producing output like <font color="red">Hello world</font> (doc5). It supports color values in RGB, hex triplet formats, and color names (doc3). For example, "FA8072" represents salmon color in hex format (doc7).

As a string method, fontcolor() operates on specific string instances rather than modifying the original string value (doc1). Its usage demonstrates how it wraps text in <font> tags with the specified color attribute (doc5).

The method has consistent browser support across major browsers, including Internet Explorer 7, Firefox 3.6, Google Chrome 7, Safari 5.0.1, and Opera 10 (doc4). However, its implementation creates HTML 4.01 <font> elements, which are deprecated in HTML5 and should not be used for new development (doc4, doc10, doc11).


## Syntax and Parameters

The method syntax for String.fontcolor() is string.fontcolor(color_value), where color_value can be a color name or value. This attribute value can be specified using color names (like 'red'), hexadecimal color codes (preceded by a pound sign, #0000ff), or RGB values (rgb(0,255,0)).

The method creates a string that embeds the original string value within an HTML <font> element, where the color attribute is set to the specified color value. For example, "hello world".fontcolor("red") produces the string <font color="red">hello world</font>.

The method supports multiple representations for color values. It accepts simple color names, hexadecimal color codes preceded by a pound sign (#0000ff), and RGB values (rgb(0,255,0)). For instance, the hexadecimal value FA8072 represents salmon, and the method can process this value as "FA8072".

All major browsers support the fontcolor() method, with compatibility dating back to JavaScript 1.0 implementation. However, as highlighted in multiple sources (doc4, doc10, doc11), the method generates HTML 4.01 <font> elements, which are deprecated in HTML5 and should not be used for new development. Modern web development should instead utilize CSS properties for text styling needs (doc4, doc11).


## Usage Examples

The _setup_ option of TinyMCE's _addClass()_, _select()_, and _removeClass()_ methods demonstrates how the font color change mechanism triggers through the _blur_ (when the user clicks away from the editor) and _focus_ (when the user returns to the editor) events. This functionality provides flexibility for developers who need to highlight text when users interact with their content.

For example, developers can create gold and silver text effects, or design neon font effects using JavaScript, even though the fontcolor() method is not recommended for new development. Production implementations would require thorough testing and accessibility verification, as noted in the TinyMCE documentation.

Developers who need to change warning text color in TinyMCE's rich text editor can use the following JavaScript function:

```javascript

function changeFontOkay() {

  const newFontColor = document.getElementsByTagName('body');

  newFontColor.setAttribute('class', 'greenOkayText');

}

```

This function updates the body's class attribute, which is defined in CSS as:

```css

body {

  color: green;

}

```

The fontcolor() method creates HTML 4.01 <font> elements, which are deprecated in HTML5. Modern web development should use CSS properties for text styling. For example, the alternative approach using CSS spans creates more flexible and controlled text color changes than the <font> tag.

Here's how you can implement this alternative approach in your JavaScript code:

```html

<div id="textholder"></div>

<script>

  var container = document.getElementById('textholder');

  container.append(givemecolor('green', "Hello I'm green"));

  container.append(givemecolor('red', "Hello I'm red"));

  function givemecolor(thecolor, thetext) {

    var span = document.createElement('span');

    span.style.color = thecolor;

    span.innerText = thetext;

    return span;

  }

</script>

```

This approach ensures that your text remains compatible with modern web standards while providing the desired color changes.


## Browser Support and Compatibility

Despite consistent support across browsers for nearly two decades, the fontcolor() method has never been standardized and may no longer function in future browser updates. As noted in the W3C's HTML 4.01 specification, the <font> tag on which it relies has been officially deprecated since 1999. Modern JavaScript development frameworks and browsers are progressively removing support for these outdated elements.

While still functional in current releases of major browsers, the method's reliance on deprecated <font> tags makes it incompatible with HTML5 standards. As stated in the JavaScript String fontcolor Method documentation, "The method generates HTML 4.01 <font> elements, which are deprecated in HTML5 and should not be used for new development."

The method's behavior and compatibility vary between different JavaScript engines and versions. For instance, when passed invalid or missing color parameters, it applies default styling instead of returning an error. This unpredictable behavior further highlights the need for developers to transition to modern text styling methods.

For developers who need to support older browsers but avoid deprecated elements, alternative approaches using <span> tags and CSS styling are recommended. These methods provide more control and flexibility while maintaining compatibility with current and future web standards.


## Alternatives and Best Practices

Modern JavaScript development follows web standards set by the World Wide Web Consortium (W3C), which officially deprecated the <font> element in HTML 4.01 specifications published in 1999 (doc1). This element, including its use in JavaScript's fontcolor() method, is not supported in HTML5 standards and should be avoided for new development (doc4, doc10, doc11).

The fontcolor() method creates HTML 4.01 <font> elements with color attributes, matching the syntax fontcolor(color_value) (doc5). It accepts color values as color names, hexadecimal codes (preceded by #), or RGB values (doc3). For example, "FA8072" represents salmon color in hex format, and the method processes this value correctly (doc7).

When passed invalid or missing color parameters, the method applies default styling instead of returning an error, demonstrating its unpredictable behavior (doc4, doc5). For modern development, developers should use CSS properties for text styling, as recommended by multiple sources (doc2, doc11).


### Alternative Approaches

Modern approaches to text styling employ the <span> element with CSS classes for better control and flexibility. This method maintains compatibility with current and future web standards. For instance, to change text color, developers can use the following JavaScript approach:

```javascript

function givemecolor(thecolor, thetext) {

  var span = document.createElement('span');

  span.style.color = thecolor;

  span.innerText = thetext;

  return span;

}

```

This function creates a <span> element with the desired color style attribute, providing a clear separation between content and presentation (doc9).


### Best Practices

To avoid deprecated elements and ensure compatibility, developers should transition from <font> to modern styling techniques. The W3C's recommendation aligns with best practices in JavaScript development, prioritizing standards-compliant methods for text styling (doc2, doc11). The shift to CSS class-based styling allows for more maintainable and adaptable text presentation across different projects and frameworks.

