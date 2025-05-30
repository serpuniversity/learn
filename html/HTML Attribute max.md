---

title: HTML max Attribute

date: 2025-05-29

---


# HTML max Attribute

HTML input validation is crucial for ensuring data integrity and user experience, particularly when collecting numerical or date-based information. The `max` attribute offers an effective solution by establishing upper value limits for various input types, including number, range, date, and time. This article explores the implementation and compatibility of the `max` attribute across different input types and elements, providing practical guidance for developers while examining its limitations and best practices.


## The HTML max Attribute

The `max` attribute in HTML constraints the upper limit of input values for various field types, including number, range, date, datetime-local, month, time, and week inputs. It establishes a maximum value that can be entered, either as a numeric value or a date string, and operates harmoniously with the `min` attribute to define ranges.

For numerical inputs, the `max` attribute accepts a simple number, while date inputs require a specific format such as "yyyy-mm-dd" (for full dates) or "yyyy-mm" (for months). This attribute is particularly valuable for validating user inputs, ensuring that forms receive data within predefined limits.

The attribute demonstrates robust compatibility across major browsers, though specific version requirements exist. All supported browsers—Chrome 4.0+, Edge 12.0+, Firefox 16.0+, Opera 10.6+, and Safari 5.1+—offer reliable support for `max`, making it a widely implementable feature for web development projects.


## Usage with Numeric Input Types

The `max` attribute works with number, range, date, datetime-local, month, time, and week input types to specify maximum values. For numerical inputs, it accepts a simple number, while date inputs require a specific format such as "yyyy-mm-dd" or "yyyy-mm". The attribute can be used together with the `min` attribute to create a range of valid values.

On the `<input>` element, the attribute can take two values: a number or a date. When used with the `min` attribute, it creates a valid range of values. For example, the following HTML code demonstrates usage with both `min` and `max` attributes on `<input type="date">` and `<input type="number">`:

```html

<!DOCTYPE html>

<html>

<body>

<h2>HTML min and max Attributes in Input Fields</h2>

<form>

  <label for="min">Date of Birth:</label>

  <input id="min" name="min" type="date" min="1995-12-31"><br><br>

  <label for="max">Age:</label>

  <input type="number" id="max" name="max" min="0" max="100">

  <input type="submit" value="Submit">

</form>

</body>

</html>

```

The attribute demonstrates robust compatibility across major browsers, with the following version requirements: Chrome 5.0+, Firefox 16.0+, Edge 10.0+, Safari 5.1+, and Opera 12.1+. The attribute is automatically converted to the appropriate type when used with `<progress>` and `<meter>` elements, with `<progress>` elements requiring a value greater than zero and `<meter>` elements requiring a value greater than the minimum value.


## Usage with Progress and Meter Elements

For the `<progress>` element, the max attribute describes the total work required by the task indicated by the element. It must have a value greater than zero and be a valid floating-point number, with a default value of 1 if not specified. The attribute is particularly useful for displaying progress bars where the total work is known and finite.

The `<meter>` element uses the max attribute to define the upper numeric bound of the measured range. This attribute is essential for providing context to the gauge reading, as it must be greater than the minimum value (set with the min attribute). The meter element can include additional attributes to describe different points of interest within the range, including low, high, and optimum values.

Both `<meter>` and `<progress>` elements automatically convert the max attribute to the appropriate type when used. For `<meter>`, this ensures the gauge displays correctly within its range, while for `<progress>`, it accurately represents the total amount of work. The max attribute requires careful consideration when working with floating-point numbers, as demonstrated in the HTML5 specification's discussion of numeric precision. Developers are advised to use the step attribute with appropriate values to ensure proper input validation and display.


## Browser Compatibility

The max attribute is supported across major browsers, with specific version requirements for each element type. Version compatibility details are as follows:

- For number and range inputs: Chrome 5.0+, Firefox 16.0+, Edge 10.0+, Safari 5.1+, and Opera 12.1+

- For date inputs: Chrome 10.0+, Firefox 16.0+, Edge 12.0+, Safari 10.0+, and Opera 12.1+

- For datetime-local, month, time, and week inputs: Chrome 16.0+, Firefox 16.0+, Edge 12.0+, Safari 10.0+, and Opera 12.1+

As the attribute applies to `<input>`, `<meter>`, and `<progress>` elements, version requirements vary:

- `<input>`: Chrome 5.0+, Firefox 16.0+, Edge 12.0+, Safari 5.1+, and Opera 12.1+

- `<meter>`: Chrome 8.0+, Firefox 6.0+, Edge 12.0+, Safari 11.0+, and Opera 60+

- `<progress>`: Chrome 8.0+, Firefox 6.0+, Edge 12.0+, Safari 11.0+, and Opera 60+

The HTML5 specification removed any existing limitations on attribute length, allowing for practical considerations rather than arbitrary constraints. While the specification places no specific limit on the length of attribute values, implementors may enforce practical limits based on system resources and performance considerations.


## Attribute Limitations

While HTML5 has no explicit limits on attribute value length, practical constraints exist, particularly when working with floating-point numbers. The specification clearly states that "this version of HTML returns to a non-SGML basis," with no limits on tag names, attribute names, or attribute values.

The max attribute, which works with number, range, date, datetime-local, month, time, and week input types, demonstrates this practical limit when used with floating-point numbers. When the attribute value is set to a float like 21.1, browsers display a popup stating the value must be less than 21. The solution recommended by the HTML specifications is to use the step attribute with a value of 0.1 or any, allowing input fields to accept values up to 21.1 while maintaining proper floating-point functionality.

The attribute value consists of one or more characters other than space, quotation marks, apostrophes, greater-than sign, solidus, and control characters. For attribute names, the syntax allows any mix of lower- and uppercase letters that form an ASCII case-insensitive match. Attribute values can contain text and character references, with no explicit size limit mentioned for HTML attributes.

For data-* attributes specifically used in HTML5, these values are stored in a DOMStringMap object, which has no inherent limits. The getter and setter methods for DOMStringMap accept two DOMString parameters: name and value, with the value parameter mapped directly to a JavaScript String. The maximum length of a JavaScript String varies by implementation, but testing has shown that setting strings up to 10 million characters long works in modern browsers like Firefox 3.5.2 and Internet Explorer 7, with no reported issues until reaching approximately 50 million characters.

In terms of practical usage, the attribute value size is constrained by browser implementation rather than HTML specification. For example, the entire application's properties (currently 430K) can be set as an HTML attribute using `<a onclick="...">` syntax, though the implementation is noted as "a little unreadable." This indicates that while there is no theoretical limit, developers should consider their specific use case and potential performance impacts when setting attribute values.

