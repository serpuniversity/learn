---

title: CSS Pseudo-classes and Pseudo-elements

date: 2025-05-26

---


# CSS Pseudo-classes and Pseudo-elements

The power of CSS lies not only in its ability to style web content but in its sophisticated mechanisms for targeting specific states and elements. Pseudo-classes and pseudo-elements extend CSS capabilities, allowing developers to create highly interactive and responsive designs without altering HTML structure. These specialized selectors enable intricate styling based on element state, position, and content, providing a flexible framework for building dynamic user interfaces.


## Introduction to Pseudo-classes

Pseudo-classes and pseudo-elements are specialized CSS selectors that target elements in specific states or conditions, often acting as if they modify the HTML directly. These powerful tools enable more dynamic and interactive styling without altering the original HTML structure, making them essential for creating responsive and user-friendly web applications.


### Basic Usage and Syntax

Pseudo-classes are defined using a colon prefix followed by the specific state, such as `:hover`, `:focus`, or `:visited`. They can be applied directly to HTML elements or combined with standard CSS selectors. For example, the following code targets all paragraph elements that are also first children of their parent containers:

```css

p:first-child {

  color: blue;

}

```


### Common Pseudo-classes

The most frequently used pseudo-classes include `:hover`, `:active`, and `:focus`, which respectively apply styles when an element is hovered over, clicked, or focused. The `:visited` pseudo-class styles links based on whether they have been previously visited by the user.


#### Example Usage

```css

button:hover {

  background-color: lightblue;

  color: white;

}

input:focus {

  border: 2px solid blue;

  outline: none;

}

a:visited {

  color: purple;

}

```


### Advanced Pseudo-classes

Additional pseudo-classes offer more sophisticated state-based styling. These include `:only-child`, `:nth-child`, and form-related selectors like `:valid` and `:invalid`.


#### Form Validation

```css

input:valid {

  border: 2px solid green;

}

input:invalid {

  border: 2px solid red;

}

```


### CSS Pseudo-elements

While similar in syntax, pseudo-elements act as if they insert new elements into the document structure. The most common pseudo-elements are `::before` and `::after`, which allow injecting content before or after elements.


#### Example Usage

```css

::before,

::after {

  content: "";

  display: block;

  width: 10px;

  height: 10px;

  background-color: blue;

}

```

These elements can be styled independently and are particularly useful for generating decorative elements like arrows or icons without modifying the HTML.


## Key Pseudo-classes

Pseudo-classes enable rich user interaction through specific states that aren't directly tied to the HTML structure. They allow for dynamic styling based on user actions or document conditions.


### Interactive Pseudo-classes

- **Hover** applies styles when a user hovers over an element. This is commonly used for button states or interactive elements, as demonstrated by changing a button's background color and text color:

```css

button:hover {

  background-color: lightblue;

  color: white;

}

```

- **Active** styles elements during the click action. For instance, this example changes the button's background to dark blue while pressed:

```css

button:active {

  background-color: darkblue;

  color: white;

}

```

- **Focus** applies styles when an element receives focus through keyboard navigation or focus mechanisms. This is illustrated by adding a blue border and removing the default outline on focus:

```css

input:focus {

  border: 2px solid blue;

  outline: none;

}

```

- **Visited** targets links that have been previously visited by the user, allowing designers to differentiate between new and old links. The default usage of `a:visited` sets the text color to purple:

```css

a:visited {

  color: purple;

}

```


### Additional Interactive Pseudo-classes

- **Link States** include :link for regular links and :hover for links while being hovered, providing a foundation for link styling. The following example changes link colors based on visit status:

```css

a:visited {

  color: purple;

}

a:link {

  color: green;

}

```

- **Focus Visible** helps ensure that focused elements remain visible even when custom styles obscure the default focus indicator. This is demonstrated by adding an orange outline when focus is visible:

```css

button:focus-visible {

  outline: 3px solid orange;

}

```


## Special Pseudo-classes

The :not() pseudo-class stands out for its ability to exclude elements based on specific criteria. For example, it allows targeting all links without a class attribute through `a:not([class]) { color: blue; }`, and ensures images with alt attributes retain proper visibility through `img:not([alt]) { outline: 10px red; }`.

Other condition-based selectors include :empty, which matches elements with no children or content, such as setting a green background for empty divs: `div:empty { background-color: green; }`. This is particularly useful for styling elements that should be visually distinct when they contain no data.

Input pseudo-classes offer detailed control over form elements. :enabled and :disabled style active and inactive elements respectively, as shown by gray backgrounds for disabled inputs: `input:disabled { background-color: lightgray; }`. The :checked pseudo-class highlights selected checkboxes and radio buttons, while :required applies styles to mandatory fields, for example with red borders: `input:required { border: 2px solid red; }`.

Additional structural pseudo-classes handle sibling relationships and element types. :last-child matches the last element of its kind within a parent, while :nth-of-type(n) selects specific instances, allowing for targeted styling based on position. Together, these advanced selectors enable precise control over complex document structures without modifying the underlying HTML.


## Pseudo-element Usage

The ::before and ::after pseudo-elements enable inserting content and styling specific parts of elements using pure CSS. These elements act as if they insert new content into the document structure, allowing for sophisticated styling without modifying the HTML.


### Insertion and Styling

::before inserts content before the start tag of an element, while ::after adds content after the end tag. Both can insert various types of content, including strings of text, icons, and empty strings. The content can be styled independently using properties like display, width, height, and background-color.


### Practical Applications

A common use case is creating CSS-only arrows through generated content. The following example demonstrates inserting and styling arrow icons before and after list items:

```css

li::before {

  content: url(arrow-left.png);

  margin-right: 10px;

}

li::after {

  content: url(arrow-right.png);

  margin-left: 10px;

}

```

The ::first-letter and ::first-line pseudo-elements target specific parts of block-level elements. ::first-line styles the first line of text, while ::first-letter styles the first letter. Both can be combined with other CSS properties, as shown in this example:

```css

p::first-letter { color: #ff0000; font-size: 200%; }

p::first-line { color: #0000ff; font-variant: small-caps; }

```


### Chaining Selectors

Pseudo-elements can be used in combination with other selectors for precise targeting. For example, the following code applies styles to the first line of the first paragraph within an article:

```css

article p:first-child::first-line {

  color: blue;

  font-weight: bold;

}

```


### Browser Support

Modern browsers support both single- and double-colon syntax for compatibility. However, developers should be aware of accessibility concerns when inserting text with ::before and ::after, as screen readers may not announce the inserted content. Instead, developers often use these elements for visual indicators that do not affect screen reader output.


## Advanced Pseudo-classes

The :checked pseudo-class targets checkboxes and radio buttons when they are selected. For example, a red outline can be applied using:

```css

input:checked {

  outline: 5px solid red;

}

```

This allows for distinct styling of form elements when they are selected by the user. Similarly, :disabled and :enabled pseudo-classes handle the styling of form elements based on their enabled state. The following example sets light gray backgrounds for disabled inputs:

```css

input:disabled {

  background-color: lightgray;

}

```

The :required pseudo-class matches form fields marked as required, enabling designers to provide visual feedback with red borders:

```css

input:required {

  border: 2px solid red;

}

```

Extended functionality includes :valid and :invalid, which style form fields based on the validity of their input types. The :in-range and :out-of-range pseudo-classes target inputs within or outside the valid range, respectively. Additionally, :read-only and :read-write match elements that are read-only or editable, while :first-child, :last-child, and :nth-child(n) select specific instances of elements based on their position in a parent.

Accessibility considerations include the :focus-visible pseudo-class, which applies styles only when focus is visible. This helps in differentiating between elements that are focused via keyboard navigation and those focused via mouse interactions, enhancing usability for assistive technologies.

