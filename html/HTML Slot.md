---

title: HTML `<slot>` Tag

date: 2025-05-29

---


# HTML `<slot>` Tag

Web components represent a significant advancement in web development, enabling the creation of reusable, encapsulated components that maintain their styling and behavior within a single, isolated DOM tree. A crucial aspect of web components is the `<slot>` element, which serves as a placeholder for content that can be dynamically inserted into custom elements. This article explores the technical implementation of `<slot>` elements, their interaction with shadow DOM, and best practices for styling slotted content while maintaining encapsulation. Through detailed examples and technical specifications, we'll examine how `<slot>` elements enable flexible content insertion while preserving the benefits of web component encapsulation.


## The `<slot>` Element and Web Components

The `<slot>` element acts as a placeholder in web components, letting developers encapsulate reusable HTML elements. It's part of the Web Components suite, which enables custom HTML tags with encapsulated styles and markup. Unlike templates, which declare reusable fragments, slots serve as specific content placeholders within web components.

Key technical details about slots include:

- Each slot has a unique name attribute, though unnamed slots default to an empty string

- Slot names must be unique within each shadow root; otherwise, matching content is assigned to the first slot with that name

- Slotted content maintains its original semantic structure and ARIA attributes

- The ::slotted() pseudo-element targets slotted content for styling purposes

- Content positioning follows light DOM element order, with unnamed slot content appearing after named slots with matching names

Developers define slots within shadow DOM trees using `<slot>` elements with optional name attributes. The shadow DOM creates separate DOM trees for encapsulation. When creating custom elements:

1. Attach a shadow root using `attachShadow({mode: 'open'})`

2. Define slot templates in the shadow root

3. Use the `<slot>` element to specify content placeholders

4. Assign light DOM elements to slots using the slot attribute

For example:

```html

<!-- Custom element definition -->

<info-box>

  <template>

    <div slot="content">Default content</div>

    <slot name="content"></slot>

  </template>

</info-box>

```

This structure allows for flexible content insertion while maintaining element isolation. The shadow DOM's encapsulation prevents style and script clashes between standard and shadow DOM trees.


## slot vs template: Key Differences

The `<slot>` tag and `<template>` element serve distinct purposes in web development. While `<slot>` elements act as placeholders within web components, `<template>` elements declare reusable HTML fragments that are instantiated later, often wrapped around `<slot>` elements to create placeholder content.

Developers use `<slot>` elements to define specific content regions within web components. These placeholders maintain their original semantic structure and ARIA attributes, ensuring compatibility with assistive technologies. The `<slot>` element supports multiple named slots, allowing developers to map content from the light DOM into distinct placeholders within the shadow DOM.

Key features of `<slot>` elements include:

- Support for named slots via the `name` attribute

- Fallback content display if no matching slot is found

- Integration with shadow DOM for encapsulated content trees

- Use of ::slotted() pseudo-elements for targeted styling

- Preservation of original element semantics and ARIA attributes

The `<template>` element serves as the container for reusable HTML fragments, which can later be instantiated and inserted into the shadow DOM using JavaScript. Together, these elements enable developers to create flexible, modular web components with encapsulated content and styles.


## Slot Placement and Content Handling

To define slot content, include HTML structure inside the element with a slot attribute whose value matches the slot's name. For example:

```html

<my-paragraph>

  <span slot="my-text">Let's have some different text!</span>

</my-paragraph>

```

or

```html

<my-paragraph>

  <ul slot="my-text">

    <li>Let's have some different text!</li>

    <li>In a list!</li>

  </ul>

</my-paragraph>

```

The name and slot attributes default to the empty string, assigning unnamed content to the unnamed slot (default slot). The shadow DOM creates separate DOM trees for encapsulation, allowing developers to create scalable and modular web components.

When multiple named slots are defined, content from the light DOM is mapped to specific placeholders using the slot attribute. For example:

```html

<slot name="header"></slot>

<slot name="content"></slot>

<slot name="footer"></slot>

```

These slots can receive content through various means, including direct insertion between tags or use of the template element for more complex structures.

The `slotchange` event allows developers to respond to changes in slot content, providing programmatic access to the dynamic nature of web components. Together with CSS pseudo-elements like ::slotted() and ::part(), developers can style both slotted content and the container element itself while maintaining encapsulation.


## Shadow DOM and Content Encapsulation

The shadow DOM creates separate DOM trees for encapsulation, allowing developers to create scalable and modular web components while maintaining encapsulation. Web components consist of three core technologies: Custom Elements, Shadow DOM, and HTML Templates. The Shadow DOM specifically enables developers to create isolated DOM trees that prevent style and script clashes between the shadow tree and the standard DOM tree.

Key features of shadow DOM include:

- Content encapsulation: Elements within the shadow DOM maintain their original styles and structure while being processed separately from the main document DOM.

- Controlled content flow: The shadow DOM allows developers to define specific content regions using `<slot>` elements, enabling dynamic content insertion while preserving semantic integrity.

- Event isolation: The shadow DOM's encapsulation prevents event listeners and event bubbling issues between the light DOM and shadow DOM.

- Scoped styling: The shadow DOM enables developers to apply styles to specific content regions without affecting the main document's style hierarchy.

When implementing slot functionality, developers should consider the following best practices:

1. Unique slot names: Ensure each slot within a shadow root has a unique name to avoid content mapping conflicts.

2. Fallback content: Include default content within the `<slot>` element to provide fallback options when no matching content is available.

3. Content semantics: Preserve the original semantic structure and ARIA attributes of slotted content to maintain accessibility and compatibility with assistive technologies.

4. Shadow DOM attachment: Attach the shadow root using the `attachShadow({mode: 'open'})` method to enable content encapsulation and isolation.


## Styling Slotted Content

Styling content within `<slot>` elements requires a combination of Shadow DOM techniques and pseudo-elements. The `<slot>` element itself cannot be styled directly, but slotted content can be targeted using the ::slotted() pseudo-element within the Shadow DOM.

For deeper styling from the main document, developers can use the part attribute combined with the ::part() pseudo-element. This approach enables more precise control over both slotted content and the custom element's structure while maintaining encapsulation.

The ::slotted() pseudo-element provides direct access to slotted content, allowing developers to style specific elements or apply inline styles. For instance, to style a slotted `<p>` element specifically, a developer could use:

```css

::slotted(p) {

  font-weight: bold;

  color: blue;

}

```

The :host pseudo-class targets the custom element itself, while the :host([highlight]) selector applies styles when a specific attribute is present on the custom element. Together, these tools enable developers to maintain encapsulation while providing targeted styling options for both slotted content and the custom element structure.

Understanding these styling techniques is crucial for building modular and maintainable web components. By combining ::slotted() and ::part(), developers can ensure that their custom elements maintain their encapsulated structure while still allowing for flexible and controlled content styling.

