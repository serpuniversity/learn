---

title: HTML Multiple Attribute

date: 2025-05-29

---


# HTML Multiple Attribute

The HTML multiple attribute revolutionizes form functionality by enabling users to select multiple options from dropdowns, upload multiple files, and enter multiple email addresses. This guide explores how to implement and optimize multiple across select elements and input types, while ensuring cross-browser compatibility and proper validation.


## The HTML Multiple Attribute

The multiple attribute enables form controls to accept multiple values, enhancing user functionality for select elements and specific input types. For select elements, this attribute transforms standard dropdowns into multi-select lists, supporting both option and email input types. When applied to input elements of type file or email, it enables users to select multiple files or compose emails with multiple recipients.

The attribute affects display and functionality across modern browsers, though keyboard accessibility requirements vary. For select elements, most browsers display scrolling lists instead of single-line dropdowns when multiple is enabled. In input elements, the attribute allows file selection beyond single-file uploads and enables comma-separated email address entry, with validation to highlight invalid inputs.

Implementation requires specific syntax: `<tag multiple>`. The attribute supports both `<input>` and `<select>` elements across multiple HTML versions and browsers, with consistent support documented for recent versions of Chrome, Edge, Firefox, Safari, and Opera. While the attribute enhances usability through extended functionality, its effective implementation requires consideration of user guidance and platform-specific selection methods.


## Using Multiple in Select Elements

The multiple attribute transforms select elements into multi-select dropdowns, allowing users to choose multiple options from a predefined list. This functionality requires specific syntax in the form of `<select multiple="multiple">`...`</select>`. The attribute significantly enhances usability by enabling users to select multiple languages in a dropdown, upload multiple files at once, or enter multiple email addresses.

Implementing the multiple attribute properly affects how select elements display across different browsers. Most browsers, including Chrome, Edge, Firefox, Safari, and Opera, display scrolling lists instead of single-line dropdowns when multiple is enabled. This design change helps users manage longer lists of options. For instance, a typical implementation might look like this:

```html

<select name="favoriteSports" multiple="multiple" size="10">

  <option>Soccer</option>

  <option>Hockey</option>

  <option>Golf</option>

  <option>Polo</option>

  <option>Formula One</option>

</select>

```

Users can select multiple options by holding down Ctrl (Windows) or Command (Mac) and clicking desired options. Keyboard users can make multiple selections by focusing on the select element, using the Up and Down cursor keys, and selecting non-contiguous items with the Space key. The select element retains its functionality for holding a single selection, but users benefit from the additional ability to select multiple options as needed.


## Multiple with File and Email Inputs

For email input, the multiple attribute allows users to include zero (if not also required), one or more comma-separated email addresses. The value must be a list of properly-formed comma-separated email addresses, with trailing and leading whitespace removed from each address in the list.

When used with the input type=file, users can select one or more files using platform-specific methods (e.g., holding down Shift or Control and clicking). Without the attribute, users can only select a single file per input.

To demonstrate proper implementation, consider the following examples:

```html

<input type="email" multiple name="emails" id="emails" list="dwarf-emails" required size="64" />

```

This element allows users to select multiple email addresses, with validation to display invalid input in lightcoral background color.

```html

<input type="file" name="uploads" accept=".jpg, .jpeg, .png, .svg, .gif" multiple />

```

This file input allows users to select multiple image files, with browser support documented for recent versions of Chrome, Edge, Firefox, Safari, and Opera.

Understanding the attribute's specifications is crucial for developers implementing multi-select functionality. While the attribute enables powerful multi-selection capabilities, developers should consider user guidance and platform-specific selection methods to ensure functionality and accessibility across different browsers and devices.


## Browser Support and Compliance

The HTML multiple attribute is supported across modern browsers for select elements and input types including file and email. The attribute enables enhanced functionality by allowing multiple selections in forms, supported by most recent versions of Chrome, Edge, Firefox, Safari, and Opera.


### Syntax and Usage

The attribute is applied using specific syntax: `<tag multiple>`, with support documented across multiple HTML versions and doctypes. For select elements, the attribute transforms standard dropdowns into multi-select lists, while for input types, it enables multiple file uploads and comma-separated email address entry. The attribute requires proper validation for email inputs, ensuring each address is properly formed and leading/trailing whitespace is removed.


### Display and Functionality

In select elements, enabling the multiple attribute changes the display from single-line dropdowns to scrolling lists, with most browsers supporting this functionality across their versions. For file and email inputs, the attribute enables platform-specific multiple selection methods, such as holding down Shift or Control and clicking. The attribute follows the HTML specification and browser compatibility guidelines, with detailed support documented in the HTML standards.

In select elements, most browsers provide native support for multiple selection, including keyboard accessibility features such as Ctrl/Command + click for selecting multiple options and space-based selection for non-contiguous items. For file input elements, the attribute allows multiple file selection through platform-specific mouse operations, while email inputs accept comma-separated addresses with proper validation. The attribute adheres to HTML standards and browser compatibility guidelines, with detailed implementation guidance provided in the HTML specifications.

## References

- [HTML Comments](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Comments.md)
- [HTML The Document Title Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Title%20Element.md)
- [HTML Optgroup The Option Group Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Optgroup%20The%20Option%20Group%20Element.md)
- [HTML Blockquote The Block Quotation Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Blockquote%20The%20Block%20Quotation%20Element.md)
- [HTML Class](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Class.md)