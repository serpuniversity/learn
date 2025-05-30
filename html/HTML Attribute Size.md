---

title: HTML size Attribute

date: 2025-05-29

---


# HTML size Attribute

In web development, correctly implementing HTML attributes is crucial for creating functional and user-friendly forms. This article focuses on the size attribute, which controls the width of input fields and the number of visible options in select elements. We'll explore how to use this attribute with different input types, examine its compatibility across major browsers, and clarify how it interacts with CSS styles. Understanding these aspects will help developers create more interactive and accessible web forms.


## Input Element Width

The size attribute for input elements determines the width of the text input field in characters. For instance, an input field with size="50" will display 50 characters.

The attribute value must be a non-negative integer greater than zero. In the HTML syntax, it appears as `<ElementName size="value">`.....`</ElementName>`, where ElementName can be text, password, email, URL, search, or tel.

For text input fields, the attribute controls how many characters are visible when editing the value. If no size is specified or an invalid value is provided, the input has no declared size, and the form control uses the default width based on the user agent.

CSS properties affecting width take precedence over the size attribute. This means that if both a size attribute and CSS width property are defined, the CSS property will be applied.

The attribute has been supported by major browsers since their inception. Version support across Chrome, Edge, Firefox, Safari, and Opera indicates compatibility back to the earliest versions of these browsers.


## Select Element Options Visibility

The size attribute for select elements determines the number of visible options in the drop-down list. To illustrate, consider a select element with a size of 3:

```html

<select size="3">

  <option value="merge"> merge sort </option>

  <option value="bubble"> bubble sort </option>

  <option value="selection"> selection sort </option>

  <option value="quick"> quick sort </option>

  <option value="insertion"> insertion sort </option>

</select>

```

This will display three options from the list of sorting algorithms at once, with a vertical scrollbar appearing if more options are available.

The attribute requires a valid non-negative integer greater than zero. No default value is specified, so if no size is provided, the select element may display all options or a browser-defined default number of options. The attribute takes precedence over CSS height properties, meaning that if both a size attribute and CSS height are defined, the size attribute will determine the number of visible options.


## Supported Elements

The size attribute applies to several HTML elements, including input, select, and the `<hr>` element. For input elements, it controls the visible width of text-based fields in characters. In the case of the `<hr>` element, the attribute sets the height of horizontal rules.

The attribute supports multiple input element types: text, password, email, URL, search, and tel. For these elements, a numeric value determines the character width. The default value is 4 characters. For example, a size of "50" would display an input field 50 characters wide:

```html

<input type="text" size="50">

```

This attribute has been supported by all major browsers since their inception. Version support across Chrome, Edge, Firefox, Safari, and Opera indicates compatibility back to the earliest versions of these browsers.

For select elements, the size attribute sets the number of visible options in the drop-down list. Like input elements, it requires a valid non-negative integer greater than zero. No default value is specified, so if no size is provided, the select element may display all options or a browser-defined default number of options.

The attribute's impact on visual appearance varies by element. For input elements, it controls the width of text input fields. For select elements, it determines the height, setting how many options are visible in the closed state. Each browser version listed (1.0 for each browser) confirms its long-standing support in all major browsers.


## Browser Support


### Browser Support

The size attribute is uniformly supported across all major browsers. The earliest support dates back to 1995 with Microsoft Edge and Internet Explorer, making it one of the most enduringly supported HTML attributes.

Chrome, Firefox, Safari, and Opera all provide consistent implementation, with version support tracking back to their respective origins: Chrome from 2008, Firefox from 2002, Safari from 2003, and Opera from 2006. This comprehensive support across modern and legacy browser versions ensures that developers can implement size attribute functionality without encountering cross-browser compatibility issues.


## Example Usage

The attribute requires a valid non-negative integer greater than zero. The attribute value must be exactly one positive integer without any leading or trailing whitespace. The text provides examples demonstrating proper usage:

For input elements, the attribute determines character width:

```html

<input type="text" name="name" size="20">

<input type="text" name="email" size="20">

<input type="submit" name="submit" value="Submit">

```

For select elements, the attribute sets the number of visible options:

```html

<select size="2">

  <option value="Soccer">Soccer</option>

  <option value="Hockey">Hockey</option>

  <option value="Tennis">Tennis</option>

  <option value="Golf">Golf</option>

</select>

```

No default value is specified for the attribute. If no size is provided, the input field may have no declared size, using the user agent's default width. For select elements, the browser may display all options or a default number of options if no size value is given.

The attribute's value takes precedence over CSS width properties. This means that if both a size attribute and CSS width property are defined, the CSS property will be overridden. The attribute also has no impact on constraint validation, ensuring that form processing remains consistent regardless of the size value specified.

## References

- [HTML The Disclosure Summary Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Disclosure%20Summary%20Element.md)
- [HTML li The List Item Element Demo](https://github.com/serpuniversity/learn/blob/main/html/HTML%20li%20The%20List%20Item%20Element%20Demo.md)
- [HTML Exportparts](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Exportparts.md)
- [HTML Attribute Placeholder](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Placeholder.md)
- [HTML xmp](https://github.com/serpuniversity/learn/blob/main/html/HTML%20xmp.md)