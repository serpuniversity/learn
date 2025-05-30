---

title: HTML `<menu>` Tag

date: 2025-05-29

---


# HTML `<menu>` Tag

The HTML `<menu>` tag presents an essential mechanism for organizing interactive command structures within web pages. Whether you're developing a set of navigation options, a context-sensitive menu, or a comprehensive command interface, this semantic element offers a powerful way to define lists of user actions. From simple command lists to complex hierarchical menus, the `<menu>` tag provides the foundation for building engaging and accessible interactive elements. In this article, we'll explore the fundamental aspects of the `<menu>` tag, from its basic structure to advanced usage patterns, helping you harness its capabilities for your web development projects.


## Overview of `<menu>` Element

The `<menu>` element represents an unordered list of commands, similar in functionality to the `<ul>` element. It consists of either `<li>` (list item) elements or flow content, representing commands that users can perform or activate. The element is fundamental for creating toolbars, context menus, and other interactive command lists.

The `<menu>` element requires two key attributes: type and label. The type attribute determines the menu's functionality, with options for "toolbar" (indicating a tool bar), "context" (for context menus), or simply omitting the attribute, which defaults to representing a list of commands. The label attribute provides a visible label for the menu, enhancing accessibility and usability.

In terms of content structure, a menu can contain:

- Zero or more `<li>` elements, each representing a command

- Flow content describing available commands

- Nested `<menu>` elements to create hierarchical or submenu structures

The element's basic usage follows the `<ul>` structure, with both start and end tags required:

```html

<menu>

  <li>Command 1</li>

  <li>Command 2</li>

  <li>Command 3</li>

</menu>

```

For interactive elements, the `<menu>` tag can include JavaScript functionality, such as:

```html

<menu>

  <menuitem label="Alert" onclick="alert('Welcome to TutorialsPoint')">Left Click On me.</menuitem>

</menu>

```

This structure enables dynamic interactions, allowing users to perform actions by clicking or selecting menu items. The element's support for nested menus and complex command structures makes it adaptable for various interactive applications, from simple navigation menus to comprehensive command interfaces.


## Basic Usage and Structure

The `<menu>` tag represents an unordered list of commands and supports both `<li>` elements and flow content. It requires both start and end tags and can contain zero or more `<li>` elements or flow content describing available commands. The element supports several attributes, including type and label.

The type attribute determines the menu's function, with options for "toolbar" (indicating a tool bar), "context" (for context menus), or no value, which represents a list of commands. The label attribute provides a visible label for the menu, enhancing accessibility and usability.

The HTML `<menu>` tag is designed to create menus for user interactions, such as right-click context menus or navigation menus. It supports global and event attributes and has specific constraints, including that a menu with type "toolbar" cannot appear as a descendant of the a element or button element.

Basic usage examples demonstrate the element's functionality. For instance, a simple menu with list items can be created as follows:

```html

<menu>

  <li>HTML</li>

  <li>JAVA</li>

  <li>C++</li>

</menu>

```

Interactive elements can include JavaScript functionality, such as creating a menu option that triggers a JavaScript alert:

```html

<menu>

  <menuitem label="Alert" onclick="alert('Welcome to TutorialsPoint')">Left Click On me.</menuitem>

</menu>

```

This structure enables dynamic interactions, allowing users to perform actions by clicking or selecting menu items. The element's support for nested menus and complex command structures makes it adaptable for various interactive applications, from simple navigation menus to comprehensive command interfaces.


## Menu Types and Attributes

The menu element represents a list of commands, with a content model that allows either zero or more li elements or flow content. The element's primary attributes are type and label. The type attribute determines the menu's function, with options for "toolbar" (indicating a tool bar), "context" (for context menus), or no value, which represents a list of commands that is neither a context menu nor a tool bar.

The label attribute provides the menu's label, enhancing accessibility and usability. Browser compatibility is robust across modern browsers, with support confirmed for Chrome, Firefox, Safari, Internet Explorer, Microsoft Edge, and Opera.

The element's DOM interface is defined as:

interface HTMLMenuElement : HTMLElement {

  attribute DOMString type;

  attribute DOMString label;

}

In its implementation, the menu element supports nested menus for creating hierarchical or submenu structures. For example, a toolbar might contain three primary menu buttons (File, Edit, Help), each with its own nested menu of specific commands. This structure enables sophisticated menu architectures while maintaining semantic clarity. The typical default display properties are defined as:

menu { display: block; list-style-type: disc; margin-before: 1em; margin-after: 1em; margin-start: 0; margin-end: 0; padding-start: 40px; }

The element's versatility extends to various interactive applications, from simple navigation menus to comprehensive command interfaces. It supports keyboard interactions through proper nesting and ARIA roles, ensuring accessibility for users with disabilities. The `<menu>` tag's semantic functionality distinguishes it from unordered lists, providing a dedicated HTML construct for representing command and menu structures.


## Browser Compatibility and Display

The `<menu>` element is supported across modern browsers including Chrome, Firefox, Safari, Internet Explorer, Microsoft Edge, and Opera. It behaves similarly to the `<ul>` element in both browser rendering and accessibility tree representation, maintaining semantic equivalence.

The element's display properties default to block-level styling with list-like characteristics. The typical CSS properties applied are:

display: block;

list-style-type: disc;

margin-block-start: 1em;

margin-block-end: 1em;

margin-inline-start: 0;

margin-inline-end: 0;

padding-inline-start: 40px;

The `<menu>` tag can contain nested menus to create hierarchical or submenu structures, with the recommended practice of using semantic HTML for accessibility purposes. Each `<menu>` element should represent commands or options rather than block-level elements.

Accessibility considerations include proper nesting, ARIA role usage, and ensuring keyboard navigation support. The element's structure requirements for nested lists must follow the correct UL`<LI>`UL pattern, preventing the incorrect nested list structure: UL`<LI>`UL`<LI>`. This ensures proper rendering and accessibility across different browser versions and assistive technologies.


## Accessibility and Best Practices

To ensure accessibility, the `<menu>` element should contain commands or options rather than block-level elements. Each menu should represent a single set of related commands, with proper nesting to create hierarchical structures. For example, a toolbar might contain three primary buttons (File, Edit, Help), each with its own nested menu of specific commands.

The element's structure requirements for nested lists must follow the correct UL`<LI>`UL pattern to prevent the incorrect nested list structure: UL`<LI>`UL`<LI>`. This ensures proper rendering and accessibility across different browser versions and assistive technologies. Browser compatibility is confirmed for Chrome, Firefox, Safari, Internet Explorer, Microsoft Edge, and Opera, with support across all major HTML doctypes.

Accessibility best practices include using proper nesting, ARIA roles, and providing keyboard support. The element's implicit ARIA role is "list," with permitted ARIA roles including directory, group, listbox, menu, menubar, none, presentation, radiogroup, tablist, toolbar, or tree. While the element supports basic browser rendering, semantic HTML is recommended for enhanced accessibility. The element's text has similar capabilities to `<ul>`, maintaining semantic equivalence across different content models.

From a development perspective, the element supports both global and event attributes, with additional support for disable, tabindex, and contenteditable properties. The element can contain `<li>`, `<script>`, and `<template>` elements, though `<li>` elements are required for palpable content. The compact attribute is supported in earlier versions of Internet Explorer and Netscape, though its effectiveness is limited in modern browsers.

## References

- [HTML Attribute Placeholder](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Placeholder.md)
- [HTML Tabindex](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Tabindex.md)
- [HTML Using Microdata In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20Microdata%20In%20HTML.md)
- [HTML rb The Ruby Base Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20rb%20The%20Ruby%20Base%20Element.md)
- [HTML Autocorrect](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Autocorrect.md)