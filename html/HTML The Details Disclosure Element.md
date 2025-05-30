---

title: Using HTML's `<details>` Element for Interactive Content

date: 2025-05-29

---


# Using HTML's `<details>` Element for Interactive Content

Web developers constantly seek ways to enhance user experience while maintaining a clean, intuitive interface. The HTML `<details>` element offers a powerful solution for this need, providing an interactive way to reveal or hide content based on user action. Unlike traditional accordion menus or JavaScript-based solutions, the `<details>` element creates a native widget that works seamlessly across browsers and devices, while offering robust accessibility features that benefit all users. This comprehensive guide walks you through the element's capabilities, from its basic structure and behavior to advanced styling options that can transform your web pages.


## What is the `<details>` Element?

The `<details>` element creates a disclosure widget that allows users to expand or collapse content on demand. This widget is rendered with a clickable triangle that indicates its open or closed state, with the disclosure information appearing when the triangle is activated.

This HTML container requires a `<summary>` element to function properly, which serves as both the widget's label and its interactive trigger. The `<details>` element can contain any valid HTML content, including text, images, lists, and tables, though the actual structure often includes a `<summary>` element followed by the expandable content.

The widget maintains its appearance across different platforms and screen readers, though the specific behavior can vary based on the browser and assistive technology in use. Most modern browsers support the element, with the latest versions of Chrome, Firefox, and Edge providing full functionality. Internet Explorer versions prior to 11 do not support the `<details>` element.

By default, the widget displays only the disclosure triangle and label. When clicked or activated through keyboard input, the widget toggles between its open and closed states, revealing or hiding its contents. The open state can be controlled programmatically using the `open` attribute, though this attribute's presence or absence is typically managed automatically based on user interaction.

The element's visual appearance is highly customizable using CSS. The default styling includes a blue border, green text, and a red border for the expanded summary. These styles can be modified using standard CSS properties, with the ability to create custom markers using pseudo-elements like `::marker`. Modern browsers also support advanced styling techniques, including animations and transitions, while maintaining compatibility with older systems.


## Basic Syntax and Usage

The `<details>` element functions as a container for HTML content that can be hidden or revealed through user interaction. It requires a `<summary>` element as its first child, which functions as both the visible label and the interactive trigger for expanding or collapsing the content.

Basic syntax follows a simple structure:

`<details>`

  `<summary>`Click to toggle`</summary>`

  <!-- Content to be revealed or hidden -->

`</details>`

The content within the `<details>` element can include any valid HTML, such as text, images, lists, or tables. While the `<summary>` element always remains visible, the content within the `<details>` tag is controlled by the widget's open/closed state.

To determine the widget's visibility:

- When the `<details>` element contains the open attribute, all content is displayed by default

- When the open attribute is omitted, only the `<summary>` content is visible initially

Interaction with the widget:

- Clicking the `<summary>` element toggles the widget between open and closed states

- The open attribute is automatically added or removed based on user interaction

- Keyboard users can navigate to the summary using tab and toggle the widget with enter or space keys


## Attributes and Behavior

The `<details>` element supports several attributes and behaviors that control its function and appearance. The most commonly used attribute is `open`, which can be added to the element to make it visible by default. When present, the `open` attribute causes the details to be displayed immediately upon loading the page. When absent, the details are hidden until the user interacts with the disclosure widget.

The element's behavior is primarily controlled through its relationship with the browser and assistive technologies. The content inside the `<details>` element is considered "flow content" and can include any valid HTML components, though a `<summary>` element must serve as the first child. The browser automatically applies `display: list-item` to the `<summary>` element, causing it to appear with a default list item style.

JavaScript can be used to programmatically control the widget's state. For example, adding or removing the `open` attribute allows developers to expand or collapse the widget based on user actions or other triggers. The element also supports event attributes, with names beginning with "on" followed by the event name. These attributes can be used to specify scripts to run when specific events occur, such as when the widget is toggled open or closed.

The default appearance of the widget includes a rotating black triangle representing the open/closed state, with the summary text displayed adjacent to the triangle. The summary text itself appears in bold and maintains negative margins to position properly relative to the triangle. When the widget is in the open state, the summary element receives additional styling, including a border at the bottom to separate it visually from the revealed content below.


## Accessibility and Screen Readers

The `<summary>` element functions as the interactive trigger for the `<details>` widget, serving as the primary interface for users of assistive technologies. Screen readers typically announce the summary as having a "button" role, though some platforms may identify it as "summary" or "disclosure triangle" based on the specific browser and assistive technology combination.

Keyboard navigation to the summary element works consistently across modern implementations, allowing users to tab through interactive elements and toggle the widget's state with Enter or Space key presses. The element maintains standard focus styles and behavior, ensuring consistent user experience regardless of activation method.

For improved accessibility, developers can enhance the widget's functionality by adding additional ARIA attributes. The `role` attribute can define document structure or landmark roles, such as `region` for generic landmark elements. The `aria-labelledby` attribute can associate the summary's text with a specific ID, providing more detailed labeling when necessary.

Modern browsers handle the `aria-expanded` state automatically, removing the need for developers to manage it explicitly. The widget continues to function properly in browser reader mode, though JavaScript-based implementations require special considerations to maintain both styling and interactivity. Legacy browsers like Internet Explorer 11 still require support, though the native `<details>` element typically maintains compatibility without additional scripting.

The element's core functionality remains robust across different platforms and assistive technologies, making it a valuable tool for creating native, accessible disclosure widgets in web development.


## Styling and Customization

The basic styling of `<details>` elements relies on the browser's default presentation, which includes displaying only the disclosure triangle and summary in the closed state. When open, the element expands to display its contents, maintaining a consistent height based on its closed state.

Additional styling can be applied through CSS to customize various aspects of the widget. The default display property of the `<details>` element is `block`, and developers can adjust its layout using standard CSS properties. The `<summary>` element is initially styled with a bold text weight and negative margins to align properly with the disclosure triangle. When the widget is open, the summary element receives additional styling, including a bottom border to separate it from the revealed content.

Customization options include modifying the background color, border, and padding through general `<details>` styles:

details {

  padding: 10px;

  border: 5px solid #f7f7f7;

  border-radius: 3px;

  background-color: #e4eaef;

}

For the summary element, developers can apply distinct background and text colors:

summary {

  background-color: #2196F3;

  color: white;

  padding: 10px;

}

The disclosure triangle can be customized using the `::marker` pseudo-element, though Safari only supports the non-standard `::-webkit-details-marker` pseudo-element:

summary::marker {

  color: #e162bf;

  font-size: 
1.2em;

}

Developers using Internet Explorer 11 or Safari should be aware of browser limitations when customizing these elements. Modern browsers support advanced styling techniques, including animations and transitions, while maintaining compatibility with older systems.

## References

- [HTML The Table Caption Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Table%20Caption%20Element.md)
- [HTML Marquee The Marquee Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Marquee%20The%20Marquee%20Element.md)
- [HTML Class](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Class.md)
- [HTML Relpreconnect](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relpreconnect.md)
- [HTML Attribute min](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20min.md)