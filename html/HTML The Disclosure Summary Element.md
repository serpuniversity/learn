---

title: The HTML Summary Element

date: 2025-05-29

---


# The HTML Summary Element

The `<summary>` element plays a crucial role in HTML by enabling expandable content through its interactive interface. This introduction will explore the element's definition, structure, and accessibility features, alongside its support across modern and legacy browsers.


## Definition and Purpose

The `<summary>` element functions as a clickable interface for toggling additional content within a `<details>` element. It must be the first child of the `<details>` element, serving as both a summary and a caption for the contained content. The element's content can include heading text, plain text, or any HTML suitable for a paragraph.

Each `<summary>` element must contain discernible text to ensure accessibility for screen reader users. This can be achieved through visible inner text, a title attribute, an aria-label attribute, an aria-labelledby attribute referencing visible text, or omitting the `<summary>` element entirely and allowing the user agent to supply a localized "Details" string as the summary.

When a user clicks or otherwise activates the `<summary>` element, it toggles the parent `<details>` element between open and closed states. This action also triggers a toggle event on the `<details>` element, providing opportunities for further customization through JavaScript or additional styling. Modern browsers fully support this functionality, but legacy browser compatibility remains important, particularly for older versions of Internet Explorer.

The `<summary>` element inherits global attributes common to all HTML elements but does not have specific attributes of its own. Its default display property is list-item, which presents the disclosure widget with an icon, typically a triangle. Web developers can customize this style through CSS; for instance, setting display to block removes the disclosure triangle while maintaining the button-like appearance through the element's pointer cursor property.


## Syntax and Structure

The `<summary>` element must be the first child of a `<details>` element, serving as a container's primary interface for expanding or collapsing its content. This relationship can be demonstrated through the following basic structure:

A `<details>` element contains a `<summary>` as its first child, followed by the collapsible content. For example:

```html

<details>

  <summary>FAQ: Frequently Asked Questions</summary>

  <p>What should I do if I can't log in?</p>

  <p>How do I purchase a product?</p>

  <!-- Additional FAQ answers -->

</details>

```

The `<summary>` element's content appears as a clickable label, with the associated `<details>` content hidden by default. When the user activates the `<summary>` - which triggers a toggle event on the parent `<details>` element - the content appears. This interaction is consistent across modern browsers, though behavior may vary in legacy implementations like Internet Explorer 11.

Accessibility considerations suggest that while user agents typically expose the `<summary>` element with an implicit "button" role, developers maintain flexibility by allowing any role and global ARIA attributes. However, proper implementation requires providing discernible text for screen reader users, using methods such as inner text content, aria-label attributes, or aria-labelledby attributes referencing visible text.

The `<summary>` element's default style includes `display: list-item`, giving it a list-item appearance complete with a disclosure triangle. Web developers have the flexibility to customize this display through CSS. While the element's basic functionality - acting as a button-like interface for collapsed content - remains consistent across browsers, variations in platform, browser, and screen reader combinations can affect how the element's state is communicated to assistive technology users.


## Accessibility and Semantics

The `<summary>` element automatically functions as a button for assistive technologies, though it can be customized with additional ARIA attributes for enhanced accessibility. User agents typically expose the element with an implicit "button" role, but developers maintain flexibility by allowing any role and global ARIA attributes. The element can accept attributes including `aria-disabled` and `aria-haspopup`, though authors must consider contextual accessibility implications.

The exposure of `<summary>` to assistive technologies varies across platforms and screen reader combinations. Common announcements include "button," "summary," or "disclosure triangle." Modern screen readers generally support this element, with browser compatibility including JAWS, Narrator, NVDA, Orca, TalkBack, VoiceOver (iOS and macOS), Chrome, Edge, Firefox, Safari, and Voice Access (Android).

When implementing custom styles, developers must ensure that the element's semantics remain intact. The default style of display: list-item includes the disclosure widget icon, typically a triangle. Removing this icon through CSS requires careful consideration to maintain proper state communication with assistive technologies. The element's importance is further emphasized by its role in the HTML5 specification, which explicitly states that headings are allowed within the `<summary>` element.


##  Styling and Display

The `<summary>` element's default display property is list-item, presenting the disclosure widget with an icon, typically a triangle. Developers can customize this style through CSS, removing the disclosure triangle while maintaining the button-like appearance through the element's pointer cursor property.

For positioning the disclosure marker, developers have several options. The marker defaults to being positioned inside the text, but changing the list-style-position to outside allows adding space between the marker and text, though this approach requires left margin and padding adjustments and is not supported in Safari.

The icon shape can also be customized using the list-style-type property. For example, developers can change the marker to a down arrow for the closed state and an up arrow for the open state. However, Safari does not natively support this approach.

To remove the marker entirely, developers have multiple options. The most straightforward is to set the list-style to none. For Safari-specific solutions, developers can use the pseudo-element summary::-webkit-details-marker { display: none; } or set the display property to block, flex, or another value.

Additional customization options include using background images as markers, though this requires careful consideration of system compatibility. Web developers should maintain the element's semantic role as an interactive button, ensuring that any style changes preserve proper state communication with assistive technologies.


## Browser Support and Compatibility

All modern browsers fully support the `<summary>` element since January 2020. The element functions consistently across major platforms and screen readers, though implementation details vary.

Web developers have encountered some differences in browser behavior, particularly with handling the toggle event, exposing the element to assistive technologies, and enforcing rendering rules. For example, while browsers automatically place `<summary>` as the first child of `<details>`, developers should verify this behavior in their specific use cases.

The `<summary>` element provides robust accessibility support through various screen readers. Common announcements include "button," "summary," and "disclosure triangle." Compatibility extends to JAWS, Narrator, NVDA, Orca, TalkBack, VoiceOver (iOS and macOS), Chrome, Edge, Firefox, Safari, and Voice Access (Android).

However, developers must be aware of browser and screen reader combinations that may affect behavior. For instance, Safari has limitations in customizing the disclosure marker through CSS while maintaining proper state communication with assistive technologies.

Although modern browsers handle most aspects of `<summary>` implementation, legacy support remains important. Internet Explorer 11 requires special consideration due to its limited support for modern HTML features. Developers should implement fallbacks or polyfills for older browsers where necessary.

