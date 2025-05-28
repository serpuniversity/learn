---

title: CSS Media Queries

date: 2025-05-26

---


# CSS Media Queries

Responsive web design has evolved dramatically over the past decade, with CSS media queries at the heart of modern adaptive layouts. These powerful tools enable developers to create websites that intelligently respond to different devices and screen sizes, providing an optimized viewing experience regardless of how users access your content. By allowing styles to be applied based on specific device characteristics and environmental conditions, media queries have become essential for building truly responsive and accessible web applications. In this comprehensive guide, we'll explore the fundamentals of CSS media queries, including their syntax, supported features, and best practices for implementation across modern browsers. Whether you're just beginning to work with responsive design or looking to refine your existing approach, this detailed overview will help you master these crucial tools for building web applications that connect with users wherever they go.


## Basic Media Query Syntax

The CSS media query syntax enables developers to apply styles based on specific device characteristics and environmental conditions. A media query consists of an optional media type and one or more media feature expressions, combined using logical operators to create targeted display conditions.


### Basic Structure

A media query begins with the `@media` rule, followed by the media type and any number of media feature expressions. For example:

```css

@media screen and (min-width: 600px) {

  /* Styles for screen devices with minimum width of 600px */

}

```

Supported media types include "all" (default), "print," and "screen." The media type defines the broad category of device for which the media query applies.


### Media Feature Expressions

Media feature expressions describe specific characteristics of the user agent, output device, or environment. These features can be discrete (with keyword values) or range features (prefixed with "min-" or "max-"). Range features can be expressed using inclusive prefixes (`min-width`, `max-width`) or range syntax operators (`<=`, `>=`).


### Logical Operators

The media query syntax supports logical operators to compose complex conditions:

- **`and`** operator: Combines media types with features or multiple features within a single query

- **`or`** operator: Tests for a match among more than one feature (cannot be used on the same level as `and` and `not`)

- **`not`** operator: Negates a single media query or feature (applies to the entire media query rather than a single feature within a query)

- **`only`** operator: Prevents older browsers from applying styles unless they evaluate the media feature expressions (has no effect in modern browsers)


### Media Query Evaluation

A media query evaluates as true if:

1. The media type matches the device

2. All media feature expressions compute as true

3. Queries involving unknown media types are always false


### Implementation Example

The following code snippet demonstrates a basic media query that changes the background color based on screen width:

```css

@MEDIA screen AND (MIN-WIDTH: 800px) {

  body {

    background-color: lightblue;

  }

}

```

This example targets screen devices with a minimum width of 800 pixels, applying a light blue background color. Multiple media queries can be applied to create more complex responsive designs:

```css

@MEDIA screen AND (MAX-WIDTH: 600px) {

  body {

    background-color: lightgreen;

  }

}

@MEDIA screen AND (MIN-WIDTH: 601px) AND (MAX-WIDTH: 900px) {

  body {

    background-color: lightyellow;

  }

}

@MEDIA screen AND (MIN-WIDTH: 901px) {

  body {

    background-color: lightcoral;

  }

}

```

These examples illustrate how media queries can be used to create dynamic, responsive designs that adapt to different screen sizes and conditions.


## Common Media Features

The core media features enable fine-grained control over design adaptations based on device characteristics:


### Width and Height

The primary features for responsive layout design are `width` and `height`, which describe the viewport dimensions. These can be used with min- and max- prefixes to define specific breakpoint ranges:

```css

/* Min-width breakpoint */

@media screen and (min-width: 600px) {

  body {

    background-color: lightblue;

  }

}

/* Max-width breakpoint */

@media screen and (max-width: 600px) {

  body {

    background-color: lightgreen;

  }

}

/* Ranges with multiple conditions */

@media screen and (min-width: 601px) and (max-width: 900px) {

  body {

    background-color: lightyellow;

  }

}

/* Large desktop breakpoint */

@media screen and (min-width: 901px) {

  body {

    background-color: lightcoral;

  }

}

```


### Orientation

Detecting screen orientation is crucial for layout adjustments. The `orientation` feature distinguishes between portrait and landscape modes:

```css

/* Landscape orientation */

@media screen and (orientation: landscape) {

  /* Landscape-specific styles */

}

/* Portrait orientation */

@media screen and (orientation: portrait) {

  /* Portrait-specific styles */

}

```


### Aspect Ratio

The `aspect-ratio` feature allows targeting screens with specific width-to-height proportions:

```css

/* Specific aspect ratio */

@media screen and (aspect-ratio: 16/9) {

  /* Styles for 16:9 aspect ratio screens */

}

/* Multiple aspect ratios */

@media screen and (aspect-ratio: 4/3) and (min-width: 800px) {

  /* 4:3 aspect ratio with minimum width */

}

```


### Resolution and Device Pixel Ratio

Modern displays vary in resolution, and the `resolution` feature helps target high-DPI screens:

```css

/* High-DPI Retina display */

@media screen and (min-resolution: 2dppx) {

  /* Styles for high-resolution displays */

}

```


### Touchscreen Capabilities

The `hover` and `pointer` features enable design adjustments based on input method:

```css

/* Non-hover capability */

@media screen and (hover: none) {

  /* Styles for touchscreens without hover support */

}

/* Coarse pointer device */

@media screen and (pointer: coarse) {

  /* Styles for devices with less precise pointing */

}

```


### Color Scheme Detection

The `prefers-color-scheme` feature allows defining alternate color sets based on user system settings:

```css

/* Light mode */

@media (prefers-color-scheme: light) {

  body {

    background-color: white;

    color: black;

  }

}

/* Dark mode */

@media (prefers-color-scheme: dark) {

  body {

    background-color: black;

    color: white;

  }

}

```


## Logical Operators and Combining Conditions

Logical operators enable sophisticated style targeting through complex condition combinations. The "and" operator connects multiple conditions, with each feature needing to evaluate as true for the query to compute as true. As noted in the documentation, valid syntax includes both feature grouping and comma separation: "@media screen and (max-width: 600px), screen and (orientation: portrait)" (MDN). This dual approach allows for both nested groups and simplified conjunctions.

The "not" operator inverts single query meanings, while the "only" keyword specifically targets legacy browser compatibility - though as MDN explains, "only" has no effect in modern browsers. The "or" operator enables multiple condition testing, combining various features or device types: "@media (not (color)) or (hover)" efficiently targets monochrome displays or interactive devices (MDN).

These operators enable powerful querying capabilities, as demonstrated by the example "@media not all and (monochrome)" which effectively translates to "all devices except monochrome displays" (MDN). The ability to nest conditions and combine multiple features allows for precise targeting of specific device characteristics and usage contexts. For instance, a complete media query might look like "@media all and (not (hover)) and (max-width: 600px), print and (orientation: portrait)" to target devices without hover capability up to 600px width or portrait-oriented print devices (MDN).

The revised syntax of CSS3 Media Queries further enhances this functionality through the introduction of <, >, and = operators for more flexible value ranges. This advanced feature set enables developers to create highly targeted, responsive designs that adapt to a wide variety of device and environmental conditions.


## Browser Support and Fallbacks

Modern browsers fully support media queries, including all major desktop and mobile browsers as of the latest updates. Chrome versions 106 and above, Firefox 110 and up, and Safari 16.0 demonstrate comprehensive implementation across the latest browser releases.

For legacy browser support, developers have several effective strategies. Internet Explorer 8 and older versions can be targeted using conditional comments to load fallback styles:

```html

<!--[if lte IE 8]>

<link rel="stylesheet" href="fallback-styles.css">

<![endif]-->

```

This approach allows serving alternative CSS while maintaining compatibility with older browsers.

To ensure functionality across all devices, including older and less capable ones, developers should employ a mobile-first approach. This means starting with minimal styles and progressively enhancing them based on specific conditions:

```css

/* Base styles for mobile */

body { font-size: 14px; }

/* Tablet styles */

@media (min-width: 768px) { body { font-size: 16px; } }

/* Desktop styles */

@media (min-width: 1024px) { body { font-size: 18px; } }

```

By organizing styles in this way, developers can create a robust foundation that supports a wide range of devices while ensuring that older browsers receive usable, albeit simpler, stylesheets.

For more complex layouts that require precise control over component sizes, consider using container queries, which are supported by Chrome 105 and Safari 16.1. These queries allow elements to adapt based on their own size rather than just the overall viewport dimensions, providing greater flexibility for modern responsive design approaches.


## Accessibility Considerations

The CSS spec includes several features specifically designed to enhance accessibility through user preference detection. The `prefers-color-scheme` feature allows targeting between light and dark themes based on system settings, with modern browser support enabling dynamic theme switching.

The `prefers-reduced-motion` feature detects user preferences for minimizing visual effects, providing three possible values: `no-preference`, `reduce` (indicating preference for minimized movement), and `user-defined-preference`. This capability helps address needs for motion sensitivity, particularly for users with vestibular disorders or vertigo.

Implementation of these features is handled through straightforward media queries. For example, reducing motion effects can be achieved with:

```css

@media (prefers-reduced-motion: reduce) {

  * {

    animation-duration: 0 !important;

    transition-duration: 0 !important;

  }

}

```

This approach enables developers to create more inclusive designs that respect user preferences while maintaining clean, maintainable codebases. The ability to detect and respond to these user settings helps ensure that web content remains accessible and usable across a wide range of devices and usage contexts.

