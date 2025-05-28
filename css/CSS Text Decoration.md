---

title: CSS Text Decoration

date: 2025-05-26

---


# CSS Text Decoration

The CSS Text Decoration module revolutionizes web text appearance through its comprehensive decoration properties. From basic underlines to complex wavy lines, these properties offer unprecedented control over text styling. This guide explores the module's capabilities, from foundational properties like text-decoration-line to advanced effects controlled through text-underline-position and text-underline-offset.


## Introduction to Text Decoration

The CSS Text Decoration module includes properties for controlling the appearance of text through decorative lines. These properties enable comprehensive text decoration control, including colors, styles, and line types. The text-decoration property, as a shorthand for multiple related properties, allows developers to apply complex decoration effects efficiently.


### Main Decoration Properties

The foundational properties include text-decoration-line, text-decoration-color, and text-decoration-style. These control the type of decoration, its color, and style respectively, allowing for precise customization of text appearance. For example:

```html

<p style="text-decoration: underline dotted red;">This text has a red, dotted underline.</p>

```


### Additional Properties

The module also introduces several additional properties for more specific effects. Text-underline-offset controls the distance of the underline from the text, while text-underline-position determines the underline's position relative to the baseline. These properties work together to enable fine-tuning of decorative effects.


### Browser Support

The text-decoration property demonstrates robust cross-browser compatibility, supported since CSS1 and enhanced in CSS3. Modern implementations fully support the property's functionality, making it a reliable choice for decorative text effects across platforms and versions.


## Main Text Decoration Properties

The main text decoration properties in CSS provide precise control over how text appears on a webpage. These properties include text-color, text-align, text-shadow, text-spacing, and text-transform, though the latter three are not specific to text decoration.


### Text Color

The text-color property sets the color of the text using color names, hexadecimal values, or RGB values. For example:

```css

p {

  text-color: #0000ff; /* Blue text */

}

```


### Text Alignment

Text alignment controls the horizontal positioning of text within a block or table-cell element. Common values include left, right, center, and justify. For instance:

```css

p {

  text-align: center;

}

```


### Text Shadow

Text shadow creates a shadow effect around the text, adding depth and visual interest. The syntax allows specifying horizontal and vertical offsets, blur radius, and color. Example:

```css

h1 {

  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);

}

```


### Text Spacing

Text spacing includes adjusting the space between characters and words. Letter-spacing controls the space between characters, while word-spacing controls the space between words. For example:

```css

p {

  letter-spacing: 2px;

  word-spacing: 5px;

}

```


### Text Transformation

Text transformation modifies the capitalization of text through operations like uppercase, lowercase, and capitalize. For example:

```css

p {

  text-transform: uppercase;

}

```

These properties work together with the core text decoration properties to create complex, visually appealing text effects. The text-decoration property itself acts as a shorthand for combining text-decoration-line, text-decoration-color, and text-decoration-style, enabling developers to apply these effects efficiently.


## Additional Text Decoration Properties

The text-decoration module provides a comprehensive set of properties for text decoration, including text-decoration-line, text-decoration-color, text-decoration-style, and text-decoration-thickness.

Text-decoration-line determines the type of decoration applied to text, with options including none, underline, overline, line-through, and blink. This property establishes the kind of line decoration to be used for the text.

Text-decoration-color sets the color of the decoration line, requiring a value for text-decoration-line to be specified. Possible values include color names, hexadecimal codes, or RGB values, allowing precise control over the decoration's appearance.

Text-decoration-style defines the style of the text decoration line, with options including solid, dotted, dashed, double, ridge, inset, outset, and wavy. The property requires a value for text-decoration-line and works in conjunction with text-decoration-color to produce the desired effect.

Text-decoration-thickness controls the thickness of the decoration line, requiring a value for text-decoration-line to be specified. The property accepts length values (px, pt, in, cm), auto (browser chooses appropriate width), or a percentage (percentage of 1em in the current font).

The text-decoration property enables efficient application of these decoration effects through a shorthand syntax, combining text-decoration-line, text-decoration-color, text-decoration-style, and text-decoration-thickness in a single declaration. This shorthand approach streamlines the process of applying complex text decoration effects.


## Shorthand Property Usage

The text-decoration property is a powerful shorthand that combines the functionality of text-decoration-line, text-decoration-color, text-decoration-style, and text-decoration-thickness into a single declaration. This allows developers to apply complex decoration effects efficiently, as demonstrated in the following examples:

```css

h2 {

  text-decoration: underline dashed green;

}

```

This code would apply a green, dashed underline to all h2 elements. Alternatively, developers can use the individual property syntax for greater flexibility:

```css

h2 {

  text-decoration-line: underline;

  text-decoration-style: dashed;

  text-decoration-color: green;

}

```

The property accepts various values for each component:

- text-decoration-line: none, underline, overline, line-through, blink

- text-decoration-style: solid, dashed, dotted, double, wavy

- text-decoration-color: color name, hexadecimal, rgb

- text-decoration-thickness: length value (px, pt, in, cm), auto, percentage

Some key points about the property's behavior:

- It applies to all HTML elements

- The DOM syntax is object.style.textDecoration="underline"

- Browser compatibility spans multiple versions, with support beginning in CSS1 and enhanced in CSS3

- The shorthand syntax can combine multiple values in any order, allowing for extensive customization options


## Browser Support and Compatibility

The text-decoration property has achieved broad compatibility across browser versions and platforms, with initial support beginning in CSS1 and further developments in CSS3. Browser implementation closely follows the specifications outlined in the CSS Text Decoration Module Level 3, though some advanced features have yet to reach widespread adoption.

As of modern standards, the property fully supports the implementation of underline, overline, line-through, and blink effects through its four primary components: text-decoration-line, text-decoration-color, text-decoration-style, and text-decoration-thickness. The shorthand syntax effectively combines these components into a single declaration, as demonstrated in examples from multiple sources.

Current cross-browser compatibility extends to all major platforms, including desktop and mobile implementations from Chrome, Firefox, Safari, and Edge. The property function is tested through native browser support mechanisms, such as the window.getComputedStyle method referenced in documentation examples. This consistent implementation provides reliable text decoration functionality across modern web development environments.

