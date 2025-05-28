---

title: CSS Counters: Creating and Styling Numbered Lists and Counters

date: 2025-05-26

---


# CSS Counters: Creating and Styling Numbered Lists and Counters

CSS counters provide a powerful mechanism for automatically numbering HTML elements, allowing developers to create consistent and flexible numbering schemes across web pages. Whether you need to generate simple sequential numbers or complex hierarchical structures, these techniques enable precise control over how and where counters appear on your site. This guide walks you through the basics of counter operations, demonstrates how to implement nested and custom counter styles, and helps you overcome common challenges in counter usage. By the end, you'll be able to apply these techniques confidently to enhance your web development projects with sophisticated numbering solutions.


## Basic Counter Operations

CSS counters enable automatic numbering of HTML elements through CSS variables. To implement counters, follow these steps:

1. **Initialize a Counter**: Use the `counter-reset` property to set the counter to zero initially. For example:

   ```css

   .counter { counter-reset: my-counter; }

   ```

2. **Apply the Counter to Elements**: Increment the counter using the `counter-increment` property. For example, to number elements in an unordered list:

   ```css

   li { counter-increment: my-counter; }

   ```

3. **Display the Counter Value**: Use the `counter()` or `counters()` functions in the `content` property to display the counter value. For example:

   ```css

   li::before { content: counter(my-counter) ". "; }

   ```

Counters can be nested using the `counters()` function with a separator string. The function syntax is:

```css

counters(counter-name, separator, counter-style)

```

Where:

- counter-name: The name of the counter to be incremented

- separator: The character used to separate counter values (default is a period)

- counter-style: The style of the counter value (default is decimal)

The `counter-display` property controls how counters are rendered, supporting various styles including numeric, alphabetic, and custom styles defined with `@counter-style`.

Counters can be scoped using the `contain` property. The `counter-increment` property supports both positive and negative increments, allowing for reverse counting.


## Nested and Custom Counter Styles

CSS counters enable complex numbering schemes through nested counters and custom styles. The counters() function combines multiple counters into a string with a specified separator, while custom styles are defined using the @counter-style rule.

Nested counters can span multiple levels, as demonstrated in the following example:

```css

body {

  counter-reset: section;

}

h1 {

  counter-reset: subsection;

}

h1::before {

  counter-increment: section;

  content: "Section " counter(section) ". ";

}

h2::before {

  counter-increment: subsection;

  content: counter(section) "." counter(subsection) " ";

}

```

This code creates a hierarchical counter system where each <h1> element resets the subsection counter while incrementing the main section counter.

Custom counter styles can be defined using various system descriptors:

```css

@counter-style my-counter-style {

  system: alphabetic;

  symbols: "A" "B" "C";

  suffix: ". ";

}

ul {

  list-style-type: my-counter-style;

}

li::marker {

  content: counter(my-counter, my-counter-style) ". ";

}

```

This creates a custom alphabetic counter style with uppercase letters and a trailing period.

The counters() function supports multiple parameters:

```css

counters(counter-name, separator, counter-style)

```

Where:

- counter-name: The name of the counter to be incremented (e.g., my-counter)

- separator: The character used to separate counter values (default is a period)

- counter-style: The style of the counter value (default is decimal)

Additional features include:

- Cyclic: Repeats characters from symbols set

- Fixed: Writes characters from symbols set once

- Numeric: Uses custom positional system

- Alphabetic: Uses custom alphabetical system

The pad descriptor specifies the minimum width for counter representations:

```css

@counter-style padded-counter {

  system: numeric;

  symbols: "0" "1" "2" "3" "4" "5" "6" "7" "8" "9";

  pad: 2 "0";

}

ul {

  list-style-type: padded-counter;

}

li::marker {

  content: counter(my-counter, padded-counter) ". ";

}

```

This creates a numeric counter with two-digit padding.


## Counter Property Usage

CSS counters derive their values through a series of properties that control their behavior:

- The `counter-reset` property initializes counters, which can be applied to individual elements or multiple counters with initial values. For instance:

  ```css

  .counter-reset-single { counter-reset: my-counter; }

  .counter-reset-multiple { counter-reset: section page 3 topic; }

  ```

- The `counter-increment` property manages counter values, accepting an increment amount (default 1) or supporting negative values for decrementing. This example demonstrates both positive and negative increments:

  ```css

  .increment-example { counter-increment: section 2; } /* Increment by 2 */

  .decrement-example { counter-increment: section -1; } /* Decrement by 1 */

  ```

- The `counter-set` property directly assigns values to counters, with restrictions on using reserved keywords. Correct usage appears as follows:

  ```css

  .counter-set-example { counter-set: my-counter 10; } /* Set to 10 */

  ```

Counter values display through the `counter()` or `counters()` functions within `content` properties. These functions accept different parameters to customize output:

- Basic counter display: `counter(<counter-name>)` or `counter(<counter-name>, <counter-style>)`

- Nested counter display: `counters(<counter-name>, <separator>)` or `counters(<counter-name>, <separator>, <counter-style>)`

Additional counter functionality includes:

- Scope management with the `contain` property

- Incremental styles like cyclic, fixed, numeric, and alphabetic systems

- Minimum width padding with the `pad` descriptor


## Common Counter Challenges

Developers often encounter challenges when implementing CSS counters, particularly with cross-browser compatibility and dynamic content insertion. A notable issue arises when attempting to create multi-level counters with different styles at each level. As seen in the example from the MDN documentation, managing nested levels without additional classes requires careful CSS selector specificity:


## Counter Styling Options

The CSS `list-style-type` property allows for various built-in counter styles, including `decimal`, `decimal-leading-zero`, `lower-roman`, `upper-roman`, `lower-alpha`, and `upper-alpha`. These styles enable developers to achieve common numbering formats without additional configuration.

For more complex requirements, developers can use the `counter-reset` and `counter-increment` properties to create custom counters. The `counter-reset` property initializes counters with a name and optional initial count (defaulting to 0), while the `counter-set` property directly assigns specific counts to elements.

The `counters()` function combines multiple counters into a string with a specified separator. It accepts three parameters: counter-name, separator, and counter-style. The function supports various counter styles, including numeric, alphabetic, and custom styles defined using the `@counter-style` rule.

Custom counter styles can implement several descriptors:

- system: Specifies how to use the counter symbols

- symbols: Defines the characters used in the counter style

- prefix: Character attached before marker representation and negative sign

- suffix: Character attached after marker representation and negative sign

- range: Specifies range of counter values, with values outside range falling back to a fallback style

- pad: Specifies minimum width for representations, padding shorter ones

- fallback: Specifies fallback counter style

- speak-as: Specifies how screen readers should read counter style (optional)

Supported system values include:

- cyclic: Repeats characters from symbols set

- fixed: Writes characters from symbols set once

- numeric: Uses custom positional system (base-2, base-8, base-16, etc.)

- alphabetic: Uses custom alphabetical system

The `counters()` function can be used in two primary contexts:

1. As a value for the `counter-increment` property in list items

2. As a content value for pseudo-elements such as `::marker` and `::before`

The `::marker` pseudo-element represents the counter in list items, while the `::before` pseudo-element can be used as an alternative with similar functionality but limited to font-related properties. Both pseudo-elements allow customization through the `content` property, which can take the form of the `counter()` or `counters()` functions.

The `pad` descriptor specifies minimum width for representations, while the `fallback` descriptor provides a style for values outside the defined range. The `speak-as` descriptor controls how screen readers interpret counter styles, though it is optional.

