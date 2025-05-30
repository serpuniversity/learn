---

title: HTML readonly Attribute

date: 2025-05-29

---


# HTML readonly Attribute

The readonly attribute enables developers to create input fields that users can view but not modify directly, striking a balance between read-only and fully disabled controls. This article explores the attribute's functionality across various HTML elements, its compatibility with different input types, and its interaction with form controls and JavaScript. We'll examine how readonly attributes behave in conjunction with disabled controls, their impact on form validation, and best practices for implementing dynamic readonly functionality through scripting.


## Basic Functionality

The readonly attribute specifies that an input or textarea field is only readable - the user cannot modify it. When a field is read-only, users can highlight it and copy text from the field, but cannot change the control's value (1, 2). The attribute restricts users from altering a field's value until certain conditions are fulfilled, such as selecting a checkbox (3, 4).

The attribute applies to the following HTML elements: `<input>` and `<textarea>` (5, 6). The attribute syntax is simply `<tag readonly>`/`<tag readonly="readonly">` (7).

By default, the attribute is supported across all major browsers starting with versions 1.0 of their respective engines: Chrome (9), Firefox (2), IE/Edge (9), Opera (1.1), and Safari (3) (8). In HTML5, the attribute was introduced and it is supported across all modern browsers (9). For XHTML, attribute minimization is forbidden, and the readonly attribute must be defined as `<input readonly="readonly" />` (10).

The attribute allows for conditional read-only functionality. For example, a form will still submit an input field that is readonly, but will not submit an input field that is disabled (6, 11). This attribute provides flexibility for controlling user interaction while maintaining form functionality (11).

Scripting can enable or disable the readonly status of an element (12). For instance, the following JavaScript code demonstrates how to enable editing of a read-only input field when a checkbox is selected:

```html

.enableInput = function() {

  var checkbox = document.getElementById("checkbox");

  var inputField = document.getElementById("input");

  if (checkbox.checked) {

    inputField.removeAttribute("readonly");

  } else {

    inputField.setAttribute("readonly", true);

  }

}

```

This demonstrates the attribute's role in maintaining interactivity while preventing direct user modification, as intended (13).


## Browser Support and DTD Compatibility

The readonly attribute behaves as a boolean attribute, where its presence alone indicates a read-only state (14). The attribute requires no specific value - an element with just "readonly" present has the same effect as "readonly=readonly" (15, 16).

In HTML, the attribute minimizes to the attribute name itself (17). This contrasts with XHTML requirements, where the attribute must explicitly state its value, such as "readonly='readonly'" (18). Both forms are well-formed - browsers check for attribute presence rather than specific value assignment in boolean attributes (19).

The attribute applies to multiple input types including text, number, date, and textarea elements (20, 21). While the attribute enables dynamic readonly functionality through JavaScript (22), its core behavior remains consistent across different input types (23).


### Browser Implementation

The attribute follows consistent implementation across major browsers. When present, the attribute prevents direct user modification while maintaining element functionality (24). The browsers consistently handle the attribute based on its presence rather than specific value assignment (25).

For JavaScript interaction, the property should be set to true rather than the string "true" (26). While browsers allow both attributes="readonly" and attributes="true", best practice recommends using attributes="readonly" for readability and maintainability (27).

The attribute affects event handling similarly across implementations. Both read-only and read-write controls trigger associated event handlers, while disabled controls generally do not (28). This uniform handling across implementations ensures predictable behavior for developers (29).


## Usage with Different Input Types

The readonly attribute applies to a variety of input types including text, number, date, and textarea elements, though it is not supported for select elements, button elements, or file input types. When applied, the attribute makes the control non-editable while maintaining functionality for tabbing, highlighting, and copying text (1, 2).

The attribute works consistently across all major browsers introduced in 2002 for Firefox and later across other engines since 1995 (3). Modern browser support is comprehensive, with no known exceptions to supported input types as of the latest specifications (4).

When applied to specific input types, the attribute behaves consistently with the following behaviors:


### Text Input

A read-only text input field displays its value and allows copying but prevents direct modification through user input (5). The field still participates in form submission when the form is submitted (6).


### Number Input

Similar to text inputs, read-only number inputs display their values and allow copying but prevent direct modification (7). These fields also submit their values when part of a form submission (8).


### Date Input

Read-only date inputs display their selected date value and allow copying but prevent direct modification through user input (9). These fields include date validation and continue to validate when the form is submitted (10).


### Textarea

Read-only textareas display their contents and allow copying but prevent direct modification through user input (11). These fields submit their contents when part of a form submission (12).

The attribute maintains its functionality across different browsers and versions with no reported inconsistencies in implementation or behavior (13). This consistency across input types and browser implementations enables developers to maintain predictable and reliable form interaction patterns.


## Interaction with Other Form Controls

The readonly attribute's behavior changes when combined with the disabled attribute. A read-only field maintains its functionality as focusable and still participates in form submissions. In contrast, disabled controls cannot receive focus and are not submitted with the form (1).

This distinction is crucial for developers implementing interactive forms. The readonly attribute allows for conditional editing based on user actions, such as selecting a checkbox (3). JavaScript can dynamically enable or disable the readonly status of elements, providing flexible control over user interaction (11).

The attribute interacts with form validation in specific ways. When an element is read-only, its value cannot be updated by the user and does not participate in constraint validation (10, 20). This means that read-only fields are exempt from mandatory value requirements (12).

These differences allow developers to implement advanced form behaviors. For example, a form might include multiple sections, with fields disabled until specific conditions are met. Simultaneously, other fields could remain read-only while still maintaining form functionality (9, 11). This granular control over user interaction enables sophisticated form workflows while maintaining basic functionality (8).


## JavaScript and readonly Attributes

JavaScript offers dynamic control over readonly status through the attribute's inherent boolean nature. The attribute's presence alone indicates a read-only state, meaning both attributes="readonly" and attributes="" achieve the same effect (14, 15). Both forms are well-formed, with browsers checking for attribute presence rather than specific value assignment (19).

From a scripting perspective, the property should be set to true rather than the string "true" to accurately represent the boolean nature of the attribute (26). While browsers allow both attributes="readonly" and attributes="true", best practice recommends using attributes="readonly" for clarity and maintainability (27).


### Enabling and Disabling readonly Status

JavaScript enables or disables readonly status through .removeAttribute() and .setAttribute() methods (12). The provided example illustrates enabling editing of a read-only input field when a checkbox is selected:

```html

.enableInput = function() {

  var checkbox = document.getElementById("checkbox");

  var inputField = document.getElementById("input");

  if (checkbox.checked) {

    inputField.removeAttribute("readonly");

  } else {

    inputField.setAttribute("readonly", true);

  }

}

```

This demonstrates the attribute's role in maintaining interactivity while allowing for dynamic control over user modification (13).


### Focus and Form Submission Behavior

The attribute retains focusability while preventing direct modification (10, 20). Both read-only and read-write controls trigger associated event handlers, while disabled controls generally do not (28). This consistent handling across implementations ensures reliable form interaction patterns (29).


### Support Across Browser Implementations

All modern browsers support readonly attributes since their introduction in HTML 4.01 (3, 22). The attribute maintains consistent behavior across implementations, with no reported inconsistencies in handling across different browsers and versions (13).

## References

- [HTML h1 h6 The HTML Section Heading Elements](https://github.com/serpuniversity/learn/blob/main/html/HTML%20h1%20h6%20The%20HTML%20Section%20Heading%20Elements.md)
- [HTML id](https://github.com/serpuniversity/learn/blob/main/html/HTML%20id.md)
- [HTML The External Object Element Demo](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20External%20Object%20Element%20Demo.md)
- [HTML Itemscope](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Itemscope.md)
- [HTML Attribute For](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20For.md)