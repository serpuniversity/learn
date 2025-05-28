---

title: CSS3 Variables and JavaScript: Dynamic Styling with Custom Properties

date: 2025-05-26

---


# CSS3 Variables and JavaScript: Dynamic Styling with Custom Properties

In modern web development, creating maintainable and responsive stylesheets requires techniques that go beyond traditional CSS approaches. CSS3 variables provide a powerful solution, allowing developers to define reusable style values that can be updated dynamically through JavaScript. This article explores how to leverage CSS variables with JavaScript for dynamic styling, including best practices for implementation and real-world applications in theme switching and responsive design.


## Introduction to CSS Variables

The :root selector enables the definition of global CSS variables that can be accessed throughout the entire stylesheet. For example:

```css

:root {

  --main-color: #42b983;

  --text-size: 16px;

}

body {

  background-color: var(--main-color);

  font-size: var(--text-size);

}

```

To update these variables at runtime, developers can use JavaScript to manipulate the `style` property of the `document.documentElement` (or `:root` in CSS). The `getComputedStyle` method can be used to retrieve the current value of a CSS variable, while setting the `style` property allows for updating the variable's value.

This approach enables developers to create more flexible and maintainable CSS stylesheets, especially in complex applications where multiple components may need to access and update shared styles dynamically. By defining values once and reusing them throughout the stylesheet, developers can reduce redundancy and improve code organization.

The ability to create variables with local or global scope offers significant advantages. Global variables can be accessed throughout the document using the :root selector, while local variables are scoped to the specific selector where they are declared. For example:

```css

body {

  background-color: var(--blue);

}

h2 {

  border-bottom: 2px solid var(--blue);

}

.container {

  color: var(--blue);

  background-color: var(--white);

  padding: 15px;

}

button {

  background-color: var(--white);

  color: var(--blue);

  border: 1px solid var(--blue);

  padding: 5px;

}

```

CSS variables have access to the DOM, allowing them to be changed with JavaScript. To set a variable, developers can use the `document.documentElement.style.setProperty()` method, including the double dashes (`--`) to indicate a CSS variable. For example:

```javascript

document.body.style.setProperty('--blue', 'lightblue');

```

The `var()` function provides a convenient way to insert the value of a CSS variable into style properties. It works with both global variables accessed through :root and local variables scoped to specific selectors. For example:

```css

:root {

  --blue: #1e90ff;

  --white: #ffffff;

}

.main-content {

  background-color: var(--blue);

  color: var(--white);

  padding: 10px;

}

```

By following best practices such as using consistent naming conventions and organizing variables into logical groups, developers can create maintainable and efficient CSS stylesheets that leverage the power of custom properties. The approach reduces redundancy, improves maintainability, and enables dynamic styling based on user interactions or responsive design requirements.


## Accessing CSS Variables in JavaScript

To access CSS variables from JavaScript, developers typically employ one of two primary methods. The most common approach involves using the `getComputedStyle` method in conjunction with `getPropertyValue`, as demonstrated in this example:

```javascript

const computedStyle = getComputedStyle(document.documentElement);

const variableValue = computedStyle.getPropertyValue('--blue');

```

This method ensures that the code remains maintainable and adheres to the Don't Repeat Yourself (DRY) principle. It's particularly useful when CSS variable values differ across various media queries, as it prevents duplication of code.

For more targeted variable access, developers can use the `document.querySelector` method to find specific elements before accessing their computed styles:

```javascript

const element = document.querySelector('.specific-element');

const variableValue = getComputedStyle(element).getPropertyValue('--white');

```

The DOM's accessibility allows JavaScript to both retrieve and modify CSS variable values dynamically. As shown in this snippet:

```javascript

// Get the root element

const root = document.querySelector(':root');

// Get a variable value

function getVariableValue() {

  const style = getComputedStyle(root);

  alert(style.getPropertyValue('--blue'));

}

// Set a variable value

function setVariableValue() {

  root.style.setProperty('--blue', 'lightblue');

}

```

These foundational techniques enable developers to efficiently manage and update CSS styles through JavaScript, supporting everything from responsive design adjustments to dynamic theming based on user input.


## Setting CSS Variables with JavaScript

The :root selector enables the definition of global CSS variables that can be accessed throughout the entire stylesheet. For example:

```css

:root {

  --main-color: #42b983;

  --text-size: 16px;

}

body {

  background-color: var(--main-color);

  font-size: var(--text-size);

}

```

To update these variables at runtime, developers can use JavaScript to manipulate the `style` property of the `document.documentElement` (or `:root` in CSS). The `getComputedStyle` method can be used to retrieve the current value of a CSS variable, while setting the `style` property allows for updating the variable's value.

For local variables, which are scoped to specific selectors, developers can use the `document.querySelector` method to find the target element before accessing its computed styles:

```javascript

const element = document.querySelector('.specific-element');

const variableValue = getComputedStyle(element).getPropertyValue('--white');

```

The CSS var() function provides a convenient way to insert the value of a CSS variable into style properties. It works with both global variables accessed through :root and local variables scoped to specific selectors. For example:

```css

:root {

  --blue: #1e90ff;

  --white: #ffffff;

}

.main-content {

  background-color: var(--blue);

  color: var(--white);

  padding: 10px;

}

```

This approach enables developers to create more flexible and maintainable CSS stylesheets, especially in complex applications where multiple components may need to access and update shared styles dynamically.

To set a CSS variable, developers can use either the `getCSSVar` helper function from the Splendid UI library or the `style.setProperty` method directly:

```javascript

// Using Splendid UI library

import { setCSSVar } from 'splendid-ui';

setCSSVar('.element', '--variable', 'blue');

// Using native JavaScript

const element = document.querySelector('.element');

element.style.setProperty('--variable', 'blue');

```

The `setProperty` method requires the variable name to include double dashes (`--`) to indicate a CSS custom property. For global variables, developers can target `document.documentElement` or `document.body`:

```javascript

document.body.style.setProperty('--blue', 'lightblue');

```

This approach offers several advantages over traditional CSS approaches. It allows users to customize styles through the user interface, enables efficient color management, and simplifies responsive design updates. The technique has proven effective in practical applications, allowing developers to build dynamic theming systems and responsive designs with improved maintainability.


## CSS Variable Best Practices

CSS variables offer significant improvements in readability and maintainability over traditional CSS approaches. By defining a value once and reusing it throughout the stylesheet, developers can improve code organization and reduce redundancy. For example, a large website with multiple repeated color values can be updated more efficiently by changing a single variable definition rather than performing manual search and replace operations across CSS files.

The naming convention for CSS variables is crucial for maintaining project consistency. Developers should choose meaningful names that indicate the variable's purpose or role. The example of using --main-text-color instead of #00ff00 demonstrates how custom properties enhance semantic clarity. Teams should establish a consistent naming convention, such as camel case or kebab case, and apply it consistently throughout the project.

To effectively manage CSS variables, developers should group related properties into logical categories. This organizational strategy improves maintainability and makes it easier to locate specific styles when needed. For instance, all color-related variables can be organized together, followed by typography-related properties and other style categories.

When working with CSS variables, it's important to understand the difference between global and local scope. Global variables are defined using the :root selector and can be accessed throughout the entire stylesheet. Local variables are scoped to specific selectors and can be used to create more targeted CSS styling. The example demonstrates how to define local variables within specific elements, such as .product-name { --primaryColor: #5f58bf; color: var(--primaryColor); }

For consistent styling across websites and applications, developers can create unified theme systems that utilize these custom properties. When the primaryColor variable changes, all elements that reference it update automatically. This approach simplifies theming and ensures a consistent visual experience across the application.


## Real-World Applications

A practical implementation of CSS variables can be seen in theme switching functionality. For example, a website might allow users to select between light and dark modes. As shown in the code snippet:

```html

<body data-theme="light">

  <input type="color" id="primaryColor">

  <input type="color" id="secondaryColor">

  <input type="color" id="neutralColor">

  <script>

    const colorInputs = document.querySelectorAll('input')

    colorInputs.forEach(input => input.addEventListener('input', updateStyles))

    function updateStyles() {

      const primaryColor = this.value

      document.documentElement.style.setProperty('--primaryColor', primaryColor)

      document.documentElement.style.setProperty('--secondaryColor', primaryColor)

      document.documentElement.style.setProperty('--neutralColor', primaryColor)

      // Additional styling updates can be applied here

    }

  </script>

</body>

```

This implementation uses color picker inputs to allow users to customize the theme through the website's interface, demonstrating how CSS variables can enhance user interaction. The use of consistent naming conventions and logical grouping of variables improves code maintainability while enabling dynamic styling based on user input.

In the context of responsive design, CSS variables offer several advantages. Traditional CSS approaches often require multiple color or sizing declarations across different selectors, which can become cumbersome to maintain. By defining these values once as CSS variables, developers can significantly reduce redundancy and improve code organization. This approach aligns with best practices for maintainable CSS stylesheets, as mentioned in the Splendid UI documentation.

The effectiveness of CSS variables in dynamic styling is further demonstrated through practical applications. As shown in the OpenReplay example, these custom properties enable developers to change both style values and component implementations based on theme selections. The performance benefits of this approach become particularly evident in larger applications, where managing theme changes through CSS variables requires fewer React re-renders compared to traditional context management approaches.

