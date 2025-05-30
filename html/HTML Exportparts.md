---

title: HTML Exportparts

date: 2025-05-29

---


# HTML Exportparts

The exportparts attribute represents a crucial aspect of shadow DOM manipulation, enabling developers to expose specific parts of a component's shadow tree to the parent document. This capability is essential for creating reusable web components that maintain encapsulation while allowing targeted styling and interaction from external contexts. By mastering exportparts, developers can achieve finer-grained control over shadow tree accessibility, paving the way for more modular and themable web applications. The attribute's implementation builds upon existing shadow DOM concepts while introducing unique challenges and opportunities for component developers.


## exportparts Attribute Overview

The exportparts attribute enables the sharing of parts of an element's shadow DOM with a containing document. This functionality is particularly useful for creating reusable components that need to expose specific parts of their shadow tree to the DOM outside the current structure.

The attribute operates by allowing shadow tree parts to be visible outside the shadow DOM, with its value defined as a comma-separated list of part-name mappings. Each mapping consists of the original part name followed by a colon and the external name. For example, the attribute `exportparts="part1:exposed1, part2:exposed2"` will expose two parts, with their original names remaining unchanged while they are accessible under the specified external names in the parent document.

Developers commonly use this attribute in nested components to control which parts of their shadow tree should be accessible to the parent document. A practical example demonstrates its usage in a template where the nested component template contains a `<card-component>` with distinct header, body, and footer elements. The parent document can then use the `exportparts` attribute to control which of these elements are exposed, as shown here:

```html

<template id="ancestor-component">

  <nested-component exportparts="part1:exposed1, part2:exposed2"></nested-component>

</template>

```

In this configuration, shadow tree parts are exposed with the same names they originally carried, allowing precise control over which elements from the shadow tree become accessible to the parent document's styling and selection capabilities.


## Part Mapping Syntax

The `exportparts` attribute enables shadow tree parts to be visible outside the shadow DOM, with its value defined as a comma-separated list of part-name mappings. Each mapping consists of the original part name followed by a colon and the external name (e.g., `exportparts="part1:exposed1, part2:exposed2"`).

This syntax allows each part to be exposed with a unique name, as demonstrated in the example code:

```html

<template id="ancestor-component">

  <nested-component exportparts="part1:exposed1, part2:exposed2"></nested-component>

</template>

```

In this configuration, shadow tree parts are exposed with the same names they originally carried, allowing precise control over which elements from the shadow tree become accessible to the parent document's styling and selection capabilities.

The attribute works by assigning different names to parts when exporting, with the input string being parsed according to specific microsyntax rules. Each mapping is separated by commas, and the first string specifies the part name within the shadow tree, while the second string specifies the external name.

For example, a nested component template might contain:

```html

<template id="card-component-template">

  <style>

    :host {

      /* styles */

    }

  </style>

  <slot name="header"></slot>

  <slot name="content"></slot>

  <slot name="footer"></slot>

</template>

```

And the nested component could be used in the parent document as follows:

```html

<ancestor-component>

  <card-component>

    <header>Header Content</header>

    <content>Main Content</content>

    <footer>Footer Content</footer>

  </card-component>

</ancestor-component>

```

The `exportparts` attribute in the ancestor component would expose the card component's parts as specified, allowing the parent document to style and select these elements using CSS.


## Element Example

In this example, the `exportparts` attribute is used to demonstrate how multiple parts of a custom element's shadow DOM can be exposed and styled from the parent document. The `exportparts` attribute in the ancestor component is used to expose parts of the nested component with specific names.

```html

<template id="ancestor-component">

  <card-component exportparts="card__header:header, card__body:body, card__footer:footer"></card-component>

</template>

```

In this configuration, the `exportparts` attribute is used to expose the header, body, and footer parts of the `card-component` with the names "header," "body," and "footer" respectively. This allows the parent document to style these parts using CSS selectors.

```css

::part(header) {

  font-weight: bold;

}

::part(body), ::part(footer) {

  font-weight: bold;

}

```

The `card-component` defines its structure using shadow DOM with separate slots for header, body, and footer content:

```html

<template id="card-component-template">

  <style>

    :host {

      /* styles */

    }

  </style>

  <slot name="card__header"></slot>

  <slot name="card__body"></slot>

  <slot name="card__footer"></slot>

</template>

```

When the parent document includes both the ancestor and card components, the exported parts become available for styling:

```html

<ancestor-component>

  <card-component>

    <slot name="card__header">Card Header</slot>

    <slot name="card__body">Card Body</slot>

    <slot name="card__footer">Card Footer</slot>

  </card-component>

</ancestor-component>

```

The resulting styling applies bold text to all exported parts, demonstrating how the `exportparts` attribute enables precise control over which shadow tree elements are exposed and accessible from the parent document. This example highlights the practical application of the `exportparts` attribute in creating reusable, themable web components.


## CSS Styling and Selection

The `part` attribute makes shadow tree elements visible to their parent DOM, while the `exportparts` attribute enables shadow tree parts to be visible outside the shadow DOM. Together, these allow CSS to select and style specific elements within a shadow tree using the `::part` pseudo-element.

The `part` attribute is particularly useful for components that need to expose specific parts of their shadow tree to external styling. For example, a nested component template might contain:

```html

<template id="card-component-template">

  <style>

    :host {

      /* styles */

    }

  </style>

  <slot name="header"></slot>

  <slot name="content"></slot>

  <slot name="footer"></slot>

</template>

```

When the parent document uses an `exportparts` attribute to expose these parts, CSS can then style them specifically. For instance, the parent document might include:

```html

<ancestor-component>

  <card-component>

    <header>Header Content</header>

    <content>Main Content</content>

    <footer>Footer Content</footer>

  </card-component>

</ancestor-component>

```

With the `exportparts` attribute set as follows:

```html

<template id="ancestor-component">

  <card-component exportparts="header, content, footer"></card-component>

</template>

```

The parent document can style these parts using the `::part` pseudo-element:

```css

::part(header) { font-weight: bold; }

::part(content), ::part(footer) { font-weight: bold; }

```

This demonstrates how the `exportparts` attribute enables precise control over which shadow tree elements are exposed and accessible from the parent document's styling.

The attribute works by assigning different names to parts when exporting, as shown in the example: `exportparts="part1:exposed1, part2:exposed2"`. This allows each part to be exposed with a unique name. The attribute is particularly powerful for creating reusable components that need to expose specific parts of their shadow tree to the DOM outside the current structure.

When working with multiple parts, it's essential to use commas to separate them, not spaces. For example:

```html

<my-component>

  <other-component exportparts="theme-btn, theme-dropdown"></other-component>

</my-component>

```

The shadow tree is an isolated structure where identifiers, classes, and styles cannot be reached by selectors or queries belonging to the regular DOM. The `exportparts` attribute enables targeting CSS styles from outside to the shadow tree through two HTML attributes: `part` and `exportparts`. The attribute works by parsing its value according to specific microsyntax rules, with each mapping specifying the original part name and the external name separated by a colon (:).

The `part` name map contains string keys and ordered set values, while the shadow root's part element map keys are strings and values are ordered sets of elements. These maps are updated when elements are added or removed, or when part name lists/maps change. While the requirement for ordered values may be revised, this mechanism provides a robust foundation for shadow tree part management and styling.


## Browser Support and Implementation

The exportparts attribute is supported across multiple device types and browser versions since July 2020, with browser support aligned with the release timeline for shadow DOM features. Browser compatibility follows the standard deployment lifecycle for W3C specifications, ensuring consistent implementation across major browser engines.

The attribute's functionality requires careful implementation to maintain the integrity of shadow tree isolation while enabling controlled access from the parent document. According to the CSS Working Group guidelines, implementations must adhere to the Candidate Recommendation (CR) process, with detailed implementation reports and testcases submitted to W3C before releasing unprefixed features. This ensures compatibility with evolving standards while maintaining robust testing protocols.

The attribute leverages fundamental WebIDL (Web Interface Definition Language) mechanisms for structured attribute setting and getting. Each part mapping is parsed according to specific microsyntax rules, with implementation details defined in the specification's structured naming conventions. The attribute works by creating an internal map of part name mappings, where the first string specifies the part name within the shadow tree and the second string specifies the external name. This map is updated dynamically as elements are added or removed, ensuring real-time synchronization between shadow tree structure and exposed part names.

## References

- [HTML The Inline Code Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Inline%20Code%20Element.md)
- [HTML Script Type Attribute](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Script%20Type%20Attribute.md)
- [HTML The Embed External Content Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Embed%20External%20Content%20Element.md)
- [HTML The Strong Importance Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Strong%20Importance%20Element.md)
- [HTML The Graphics Canvas Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Graphics%20Canvas%20Element.md)