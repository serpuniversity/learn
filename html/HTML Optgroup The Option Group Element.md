---

title: The HTML `<optgroup>` Element: Creating Groupings for Dropdown Menus

date: 2025-05-29

---


# The HTML `<optgroup>` Element: Creating Groupings for Dropdown Menus

The `<optgroup>` element is a valuable tool for organizing options within HTML dropdown menus, yet many developers underutilize its potential. By structuring options into logical groups, we improve both accessibility and user experience. From basic usage to advanced applications, this exploration covers everything you need to know about `<optgroup>`, including its attributes, accessibility best practices, and support across different browsers.


## Introduction to `<optgroup>`

The `<optgroup>` element groups related options within a `<select>` element, improving readability and accessibility. This element serves to visually organize options, particularly useful in dropdown menus with many items (Source: MDN Web Docs). While the `<optgroup>` element requires both start and end tags, the end tag can be omitted under specific conditions: when followed immediately by another `<optgroup>` element, or when the parent element has no more content (Source: MDN Web Docs).

The element's primary function is to group items in selection lists, which can include both multi-select lists and combo boxes (Source: WebAIM). Within a `<select>` element, related options should be semantically grouped using `<optgroup>` to improve usability, particularly for screen reader users (Source: HTML: HyperText Markup Language).

The `<optgroup>` element features several key attributes:

- `label`: A mandatory attribute specifying the group name, which is displayed in the dropdown menu

- `disabled`: A Boolean attribute that prevents all options within the group from being selected

- `multiple`: Allows multiple options to be selected within the group

- `size`: Controls the number of options displayed at once, with scrolling possible when this value is greater than the number of options (Source: HTML: HyperText Markup Language).

For example, a dropdown menu for browsers could be structured as follows:

```html

<select>

  <optgroup label="Firefox">

    <option value="2.0">Firefox 2.0 or higher</option>

    <option value="1.5">Firefox 1.5.x</option>

    <option value="1.0">Firefox 1.0.x</option>

  </optgroup>

  <optgroup label="Microsoft Internet Explorer">

    <option value="7.0">Microsoft Internet Explorer 7.0 or higher</option>

    <option value="6.x">Microsoft Internet Explorer 6.x</option>

    <option value="5.x">Microsoft Internet Explorer 5.x</option>

    <option value="4.x">Microsoft Internet Explorer 4.x</option>

  </optgroup>

  <optgroup label="Opera">

    <option value="9.0">Opera 9.0 or higher</option>

    <option value="8.x">Opera 8.x</option>

    <option value="7.x">Opera 7.x</option>

  </optgroup>

  <option>Safari</option>

  <option>Other</option>

</select>

```

This structure maintains semantic organization while providing clear groupings for users (Source: WebAIM).


## Basic Usage and Structure

The `<optgroup>` element requires both start and end tags, with the end tag being optional under specific conditions: when followed immediately by another `<optgroup>` element, or when the parent element has no more content (Source: MDN Web Docs).


### Basic Structure

The element contains related `<option>` elements directly inside it, with the group labeled using the `label` attribute. Each `<optgroup>` element must be directly inside a `<select>` element. For example:

```html

<select>

  <optgroup label="Firefox">

    <option value="2.0">Firefox 2.0 or higher</option>

    <option value="1.5">Firefox 1.5.x</option>

    <option value="1.0">Firefox 1.0.x</option>

  </optgroup>

  <optgroup label="Microsoft Internet Explorer">

    <option value="7.0">Microsoft Internet Explorer 7.0 or higher</option>

    <option value="6.x">Microsoft Internet Explorer 6.x</option>

    <option value="5.x">Microsoft Internet Explorer 5.x</option>

    <option value="4.x">Microsoft Internet Explorer 4.x</option>

  </optgroup>

  <optgroup label="Opera">

    <option value="9.0">Opera 9.0 or higher</option>

    <option value="8.x">Opera 8.x</option>

    <option value="7.x">Opera 7.x</option>

  </optgroup>

  <option>Safari</option>

  <option>Other</option>

</select>

```

This structure maintains semantic organization while providing clear groupings for users (Source: WebAIM).


### Content and Attributes

The element supports the following attributes:

- `label`: A mandatory attribute specifying the group name, which is displayed in the dropdown menu

- `disabled`: A Boolean attribute that prevents all options within the group from being selected

- `multiple`: Allows multiple options to be selected within the group (Source: MDN Web Docs)

- `size`: Controls the number of options displayed at once, with scrolling possible when this value is greater than the number of options (Source: HTML: HyperText Markup Language).

Option groups can contain one or more `<option>` elements directly. The group label is displayed in the dropdown menu, typically styled prominently (Source: MDN Web Docs). While the `<label>` attribute provides the group name, the actual option content is presented to users, with screen readers sometimes being able to interpret the label information (Source: H85: Using `<optgroup>` to group `<option>` elements inside a `<select>`).

The element's specifications categorize it as flow content, phrasing content, interactive content, listed, labelable, resettable, and submittable. Its structure permits custom content including `<button>`, `<legend>`, and `<hr>` elements for visual separation (Source: The HTML Select element - HTML: HyperText Markup Language).


## Attributes and Customization

The `<optgroup>` element supports two primary attributes that developers can use to customize their dropdown menus:


### label

The `label` attribute is mandatory for every `<optgroup>` element. It specifies the group name, which is displayed in the dropdown menu. This attribute provides a descriptive label for the group of options. For example:

```html

<optgroup label="Programming Languages">

  <option value="C"> C </option>

  <option value="C++"> C++ </option>

  <option value="Java"> Java </option>

</optgroup>

```

In this example, the dropdown menu would display the label "Programming Languages" followed by the programming languages as separate options.


### disabled

The `disabled` attribute is a Boolean attribute that prevents all options within the group from being selected. When this attribute is present, the browser typically grays out the control and prevents it from receiving browsing events like mouse clicks or focus-related actions. For example:

```html

<optgroup label="Scripting Language" disabled>

  <option value="JavaScript"> JavaScript </option>

  <option value="PHP"> PHP </option>

  <option value="Shell"> Shell </option>

</optgroup>

```

In this case, the "Scripting Language" group and all its options would be disabled, preventing users from selecting any of the languages in this group.


### Styling with CSS

The `<optgroup>` element itself supports basic styling through CSS. While the label content is typically displayed inline with the options, custom styling can be applied to the entire group. For example:

```html

<select>

  <optgroup>

    <option value="C"> C </option>

    <option value="C++"> C++ </option>

    <option value="Java"> Java </option>

  </optgroup>

</select>

<style>

  optgroup {

    color: green;

    background-color: aquamarine;

  }

</style>

```

This example applies green text color and aquamarine background to the entire `<optgroup>` element, creating a visual distinction between different groups in the dropdown menu.


## Accessibility and Best Practices

Grouping related options improves usability for users navigating dropdown menus, particularly those with disabilities (WCAG 1.3.1 Success Criterion) (Source: WebAIM). To enhance accessibility, developers should group logically related options together and provide meaningful labels for each group (Source: H85: Using OPTGROUP to group OPTION elements inside ...).


### Best Practices

- Use the `label` attribute to describe the group of options, providing context for both sighted and screen reader users (Source: WebAIM). The label should give a clear indication of the options included in the group.

- Avoid creating nested groupings unless absolutely necessary, as this may complicate the user interface (Source: OPTGROUP - Option Group). Each `<optgroup>` element should contain directly related options and maintain a clear organizational structure.

- When disabling an entire group, use the `disabled` attribute to prevent selection while maintaining clear communication (Source: OPTGROUP - Option Group). This attribute should be used sparingly to maintain usability for all users.

- Consider how the groupings will be presented to users, ensuring that the label is descriptive enough to help users quickly locate the options they need (Source: The HTML Select element - HTML: HyperText Markup Language).


### Test Procedure

To ensure that related options are properly grouped, developers should:

1. Identify groups of related options within the dropdown menu

2. Group these options using the `<optgroup>` element, providing a meaningful label for each group (Source: H85: Using optgroup to group option elements inside a select). This process helps to visually break up long lists and improve navigation for all users.

By following these guidelines, developers can create more accessible and user-friendly dropdown menus that effectively organize related options for their users.


## Advanced Usage

While the specification only allows one level of grouping within a `<select>` element and does not support nested `<optgroup>` elements, the `<optgroup>` element has proven highly effective for managing complex selection lists (Source: The HTML Select element - HTML: HyperText Markup Language).

Implementing multiple levels of grouping requires careful consideration of user experience. When nesting `<optgroup>` elements, each additional level increases complexity and may require users to navigate through multiple layers of organization (Source: OPTGROUP - Option Group).

Browser compatibility with the `<optgroup>` element has improved significantly since its introduction in HTML 4.0. Modern browsers provide consistent support for the element's basic functionality, including grouping and labeling options (Source: The HTML Select element - HTML: HyperText Markup Language). However, authors should remain aware that older browsers may lack full support, particularly for features like nested groupings or advanced styling options.

For developers working with legacy systems, the MDN Web Docs provide detailed information on the element's DOM interface and supported attributes (Source: `<optgroup>`: The Option Group element - MDN Web Docs). This documentation also highlights the element's ARIA role of "group," which can aid screen reader users in navigating complex selection lists (Source: H85: Using optgroup to group option elements inside a select).

In practical applications, authors can test their implementation using WebAIM's recommended procedure: first identifying groups of related options, then grouping them with `<optgroup>` elements (Source: H85: Using optgroup to group option elements inside a select). This approach helps ensure that related options are properly organized for both sighted and screen reader users, while maintaining a clear and logical structure for the selection list (Source: H85: Using OPTGROUP to group OPTION elements inside ...).

## References

- [HTML The Graphics Canvas Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Graphics%20Canvas%20Element.md)
- [HTML Anchor](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Anchor.md)
- [HTML Allowing Cross Origin use Of Images And Canvas](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Allowing%20Cross%20Origin%20use%20Of%20Images%20And%20Canvas.md)
- [HTML Script Type Attribute](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Script%20Type%20Attribute.md)
- [HTML Attribute Autocomplete](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Autocomplete.md)