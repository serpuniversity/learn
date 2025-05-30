---

title: HTML dirname Attribute

date: 2025-05-29

---


# HTML dirname Attribute

The dirname attribute in HTML provides a crucial mechanism for submitting text directionality information with form submissions. While most web developers are familiar with standard form elements like text inputs and text areas, few understand how to ensure that their content's directionality is preserved during form submission. This attribute allows developers to specify whether form fields should display text in left-to-right (LTR) or right-to-left (RTL) direction, making it essential for international websites that support multiple writing systems. In this article, we'll explore how the dirname attribute works, its compatibility across different browsers, and provide practical examples of how to implement it in your HTML forms.


## dirname Attribute Overview

The dirname attribute provides a mechanism for submitting text directionality information with HTML form submissions. For both input and textarea elements, the attribute requires the element's name followed by ".dir", with values limited to "ltr" (left-to-right) and "rtl" (right-to-left).


### Attribute Requirements and Values

The dirname attribute mandates that the attribute value precisely match the element's name followed by ".dir". This ensures proper identification and processing of the directionality information during form submission. The supported values are strictly "ltr" and "rtl", reflecting the fundamental text directionality options in writing systems.


### Browser Support and Implementation

The attribute functions consistently across modern browsers, including Chrome, Edge, Firefox, IE, Opera, and Safari. Implementation follows the guidelines set forth in the HTML Living Standard Specification, ensuring compatibility and predictability across different environments.

Browser support varies by element type. The attribute is fully supported for input elements across all modern browsers, introduced in version 17 of Chrome. For textarea elements, support began with Chrome version 79.0, though complete compatibility requires the use of specific input types as detailed in the specification.


### Default Behavior and Inheritance

When a form control lacks a explicit dir attribute, the browser determines directionality based on inherited properties from parent elements or user-agent default settings. Specifically, elements display content as right-to-left (RTL) when the first strongly typed character is Hebrew or Arabic, and left-to-right (LTR) when the first character is Latin.

The directionality system incorporates several mechanisms for dynamic text handling:

- For block-level elements, direct assignment of dir="rtl" or dir="ltr" controls text direction.

- Inline content uses the dir="auto" value, which determines direction based on the first strongly typed character within the element.

- The bdi element allows isolation of inline content directionality, particularly useful for mixed-language text where correct direction assignment is essential.


## Attribute Syntax and Usage

The dirname attribute requires the input field name followed by ".dir". Its value can be "ltr" (left-to-right) or "rtl" (right-to-left). It can be applied to `<input>` and `<textarea>` elements to ensure correct text directionality during form submission.

For input elements, the attribute takes the form `dirname="name.dir"`, where "name" is the control element's name followed by ".dir". This allows the browser to submit both the input value and its directionality. The value can be either "ltr" or "rtl", making it particularly useful for fields whose directionality is unknown but important for later processing.

Implementing the attribute is straightforward. In the case of input elements, the syntax is as follows:

```html

<input name="myname" dirname="myname.dir">

```

Textarea elements follow a similar pattern:

```html

<textarea name="explanation" dirname="explanation.dir"></textarea>

```

The attribute enables form controls to submit with two name/value pairs: the first is the name and value, while the second uses dirname as the name with ltr (left-to-right) or rtl (right-to-left) value sent by the browser upon form submission. This bidirectional communication ensures that servers receive accurate directionality information along with the input data.

While the attribute works seamlessly with modern browsers including Chrome, Edge, Firefox, IE, Opera, and Safari, it's important to note the specific implementation details. For example, the attribute requires Chrome version 17 or later and began supporting textareas in version 79.0. Implementation details vary between browsers, with explicit support documented for use cases involving Hebrew, Arabic, and other right-to-left languages.


## Browser Support

The dirname attribute demonstrates robust cross-browser compatibility across modern web platforms. Both input and textarea elements support the directive, with specific implementation nuances for each.

For input elements, support begins in Chrome version 17, with full compatibility across all modern browsers. The attribute usage follows the precise pattern of input name followed by ".dir", with values restricted to "ltr" or "rtl". Example implementations confirm consistent behavior across Chrome, Edge, Firefox, IE, Opera, and Safari.

Textarea elements adopt similar syntax but face limited browser support, with initial implementation in Chrome version 79.0. As of the latest update, full compatibility exists in Chrome, Edge, and Safari, while Firefox and Internet Explorer exclude support. Opera maintains compatibility with both input and textarea elements, though version details vary across browsers.

The attribute's core functionality consistently pairs the input value with its corresponding directionality upon form submission. For example, an input field with "/dir" attribute submission produces a URL-encoded pair where the first key-value represents the original input and the second specifies directionality:

```url

https://example.com/form?name-field=John Doe&name-field.dir=ltr

```

This bidirectional communication ensures form processing understands both content and its presentation requirements, particularly crucial for languages requiring distinct left-to-right and right-to-left handling.


## Form Submission Example

The dirname attribute demonstrates its functionality through a simple form example, with both input and textarea elements demonstrating its use.


### Input Field Example

The following HTML demonstrates an input field with dirname implementation:

```html

<!DOCTYPE html>

<html>

<head>

<style>

h1 { color: green; }

</style>

</head>

<body>

<form action="/action_page.php">

<h1> GeeksforGeeks </h1>

<h2> HTML dirname attribute </h2>

First name: <input type="text" name="fname" dirname="fname.dir"> <input type="submit" value="Submit">

</form>

<p> After the Submission of the form, the text direction of the input field will also be submitted. </p>

</body>

</html>

```

In this example, the form submission includes two fields: the original input value and its directionality. The resulting URL-encoded submission appears as follows:

```url

https://example.com/form?fname=John Doe&fname.dir=ltr

```


### Textarea Field Example

The following HTML demonstrates a textarea field with dirname implementation:

```html

<!DOCTYPE html>

<html>

<head>

<style>

h1 { color: green; }

</style>

</head>

<body>

<form action="/action_page.php">

<h1> GeeksforGeeks </h1>

<h2>HTML dirname attribute</h2>

<textarea name="Geeks" dirname="geeks.dir" placeholder="write something here"></textarea>

<input type="submit" value="Submit">

</form>

<p> After the Submission of the form, the text direction of the Textarea field will also be submitted. </p>

</body>

</html>

```

This example illustrates a form submission with the textarea name and its directionality:

```url

https://example.com/form?Geeks=written content&geeks.dir=ltr

```

The examples cover both `<input>` and `<textarea>` elements, demonstrating the attribute's functionality across different form fields. The browser compatibility table shows the attribute's support across modern browsers, with full support in Chrome, Edge, Safari, and Opera, while Firefox and Internet Explorer do not implement this feature.


## Directionality Determination

The browser determines directionality for elements without a specified dir attribute through several mechanisms:


### Parent Element Inheritance

When an element lacks a dir attribute, the browser looks to its parent elements for directionality information. This inheritance follows the structure from the nearest parent with a dir attribute down to the specific element in question. The attribute applies to various structural elements including paragraphs, tables, and forms.


### Document-Level Direction

For document-level directionality, the browser must be explicitly told what to expect. This is typically achieved by setting the dir attribute on the html element, either to "ltr" (left-to-right) or "rtl" (right-to-left). Once set at the html tag level, directionality percolates down to all block elements unless explicitly overridden.


### Bidirectional Text Handling

For inline stretches of bidirectional text, the browser requires special handling. The attribute causes the browser to skip text in certain container elements like bdi, script, style, and textarea, as well as text with a dir attribute. This allows the browser to correctly interpret and render bidirectional content.


### Automatic Direction Determination

The browser automatically determines directionality based on the content's first strong character. For input elements, this is achieved through the dir="auto" attribute, which causes the input field to adjust its direction based on the first strong character. This mechanism helps ensure that subsequent input fields adjust correctly to changes in text direction.


### Cross-Browser Compatibility

Webkit browsers keep lines containing no strong directional characters right-aligned, while Blink and Gecko browsers left-align such lines. The specification indicates that this behavior is likely to standardize across all browsers in the future.


### Example Implementation

The following HTML demonstrates an input field with automatic direction determination and dirname implementation:

```html

<input type="text" name="comment-input" dir="auto" dirname="comment-direction" value="Hello" />

```

When submitted, the form includes two fields: comment-input with value "Hello" and comment-direction with value "ltr":

```url

https://www.example.com/submit?comment-input=Hello&comment-direction=ltr

```

The browser compatibility information shows that support exists across modern browsers, with specific implementation details varying between Chrome, Edge, Safari, and Opera. Internet Explorer and Firefox do not implement this feature.

## References

- [HTML Abbr The Abbreviation Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Abbr%20The%20Abbreviation%20Element.md)
- [HTML Head The Document Metadata Header Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Head%20The%20Document%20Metadata%20Header%20Element.md)
- [HTML bdi The Bidirectional Isolate Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20bdi%20The%20Bidirectional%20Isolate%20Element.md)
- [HTML The Output Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Output%20Element.md)
- [HTML The Ruby Annotation Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Ruby%20Annotation%20Element.md)