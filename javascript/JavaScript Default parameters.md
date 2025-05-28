---

title: Default Parameters in JavaScript Functions

date: 2025-05-26

---


# Default Parameters in JavaScript Functions

In JavaScript, function parameters often require explicit checks for missing or undefined values, cluttering the function body with validation code. The default parameter feature, introduced in ES6, streamlines this process by allowing developers to initialize parameters with fallback values. This powerful syntax enhancement simplifies function signatures while maintaining compatibility with older JavaScript environments. Through a combination of explicit examples and detailed behavior explanations, this article explores how default parameters work, their interaction with various data types, and best practices for leveraging this feature in modern JavaScript development.


## Syntax and Behavior

The default parameter feature allows JavaScript functions to initialize formal parameters with specified values when no argument or `undefined` is passed. This behavior works in modern JavaScript environments, including ES6, where parameters can be initialized directly with default values.

In ES6, default parameters are defined using the syntax: `function foo(x = defaultValue1, y = defaultValue2) { ... }`. When a function is called with fewer arguments than parameters, the missing parameters receive their corresponding default values. For example, in the function `greet(name, greeting = 'Hello')`, the greeting parameter defaults to "Hello" if no value is provided.

Default parameters evaluate at call time, creating a new scope for each function call. This scope relationship allows earlier parameters to be referenced in later default parameter initializers. However, functions and variables declared in the function body cannot be referenced from default value parameter initializers, as attempting to do so results in a runtime `ReferenceError`.

The initialization of default parameters occurs synchronously without evaluating `await` or `yield` expressions. Each default parameter lives in its own scope, which is a parent of the scope created for the function body. This means that objects created in default parameters are recreated every time the function is called, unlike with the `arguments` object, which has limited array methods.

The feature applies across various data types, including numbers, strings, booleans, objects, arrays, and null values. Any expression can be used for default values, making the syntax flexible yet powerful for function parameter initialization.


## Evaluation and Scope

Default parameters in JavaScript functions introduce an additional scope at call time. This scope allows expressions in default parameter values to reference hoisted variables and functions declared in the function body. In the absence of this additional scope, expressions in parameters would either access value `undefined` for hoisted variables or attempt to initialize functions with their function bodies, leading to `ReferenceError`.

Function parameters default to `undefined`, and default parameter values provide a mechanism to assign different default values. The evaluation occurs synchronously and does not support `await` or `yield` expressions. While parameters default to `undefined`, passing `null` to a function parameter does not trigger the default value unless explicitly defined, as demonstrated in the `example` function where `param2` was not defined when passed `null`.

The parameters form a left-to-right assignment sequence, meaning that later parameters can reference earlier parameters in their default value expressions. The parameter list creates its own scope that is a parent of the function body's scope, allowing earlier parameters to be referenced in later default parameter initializers while preventing later parameters from referencing earlier ones before they are initialized. This scoping behavior ensures that function code operates consistently across various JavaScript environments, with the feature available across browsers since September 2016.

The parameter evaluation creates a new object each time the function is called, as demonstrated in the `multiply` function where `b` defaults to `1` when no second argument is provided. This mechanism enables JavaScript's first-class function capabilities while maintaining consistency with the language's existing semantics for function parameters and arguments.


## Use Cases and Best Practices

Default parameters in JavaScript functions simplify function syntax and improve code readability by providing default values for missing arguments. Consider the following examples demonstrating this feature:

Function with multiple default parameters:

```javascript

function sum(a = 1, b = 2) {

  return a + b;

}

console.log(sum()); // Output: 3

console.log(sum(4)); // Output: 6

console.log(sum(5, 7)); // Output: 12

```

Passing a function as a default value:

```javascript

const multiplyBy10 = () => 10;

function calculate(x, y = multiplyBy10()) {

  return x * y;

}

console.log(calculate(2)); // Output: 20

```

Handling undefined values:

```javascript

function greet(name = "Guest") {

  return "Hello, " + name;

}

console.log(greet()); // Output: Hello, Guest

console.log(greet(undefined)); // Output: Hello, Guest

```

DOM element creation with default parameters:

```javascript

function createElement({ tag = 'div', content = 'Default Content', classes = [] }) {

  const element = document.createElement(tag);

  element.textContent = content;

  element.classList.add(...classes);

  return element;

}

const myElement = createElement({ tag: 'section', content: 'Custom Section' });

document.body.appendChild(myElement);

```

The feature allows for flexible value assignment, supporting numbers, strings, booleans, objects, arrays, and null values. Any expression can be used for default values, making the syntax powerful for function parameter initialization.

For complex configurations, default parameters enable concise object initialization through property shorthands. Consider the following example:

```javascript

function createConfig({ target = 'defaultTarget', type = 'unknown', data = {} }) {

  return { target, type, data };

}

const config = createConfig({ type: 'image', data: { id: 42 } });

console.log(config); // Output: { target: 'defaultTarget', type: 'image', data: { id: 42 } }

```

The implementation ensures consistent behavior across function calls, with each default parameter object being recreated independently. This mechanism allows for robust handling of missing or undefined values while maintaining clear function syntax.


## Common Pitfalls and Workarounds

Default parameters in JavaScript can lead to unexpected behavior when handling falsy values like null or false. For example, when a function is called without an argument, the default value is used - but this behavior differs from how the arguments object handles values. While the arguments object treats null as a valid argument, default parameters do not assign default values to null parameters.

To handle these cases, developers can use the === operator to check for exact null values before using default parameters. This approach ensures that functions expect the correct data types and handle unexpected input. For example:

```javascript

function getCandy(options = {}) {

  const { kind = requiredParam('kind'), size = requiredParam('size'), upperKind = (kind === null ? null : kind.toUpperCase()), callback = function noop() {}, } = options

}

```

In this function, if kind is explicitly passed as null, it is preserved as null. Otherwise, it attempts to convert to uppercase. This approach maintains the benefits of default parameters while avoiding unexpected behavior when dealing with falsy values.


### Best Practice: Handling Falsy Values

To effectively use default parameters while managing falsy values, developers should:

- Use strict equality (===) to check for null values

- Provide clear documentation for expected input types

- Use the arguments object for fallback values when necessary

- Avoid using default parameters for unused or optional arguments


## ES6 Features and Compatibility

The introduction of default parameters in ES6 simplified JavaScript function syntax while maintaining compatibility with earlier versions of the language. This feature allows formal parameters to be initialized with default values if no value or undefined is passed, reducing the need for explicit checks within function bodies.

The ES6 syntax introduced the ability to directly initialize parameters with default values using the syntax: `function foo(x = 11, y = 31) {...}`. Default values can be expressions, including function calls, that are lazily evaluated at call time. For example, function bar uses default value expressions: `function bar(val) { console.log("bar called!"); return y + val; }`.

These default values are assigned only when parameters are omitted or undefined, with special handling for null and undefined. While null coerces to 0 and undefined is treated as missing, special care is required when using default parameters with higher-order functions like forEach, map, and reduce. As demonstrated in the example `['1', '2', '3'].map(parseInt)`, default parameters can create bugs when the function called has optional parameters, such as parseInt's second parameter (radix).

To achieve similar functionality in pre-ES2015 JavaScript, alternative methods like the following were commonly used:

```javascript

function foo(a, b) {

  a = typeof a !== 'undefined' ? a : 42;

  b = typeof b !== 'undefined' ? b : 'default_b';

  // ...

}

```

This method allows passing in any value, including false or null, since typeof null == "object". Modern implementations handle these cases differently, with default parameters replacing falsy values like null while preserving behavior for truthy values.

The feature's syntax allows for complex configurations through property shorthands, particularly in object creation. For example, the createElement function demonstrates this approach:

```javascript

function createElement({ content = 'Very default', classNames = ['module-text', 'special'] } = {}) {

  const element = document.createElement(tag);

  const text = document.createTextNode(content);

  element.classList.add(...classNames);

  element.appendChild(text);

  return element;

}

```

This approach improves code readability and reduces function body complexity by making default configurations explicit in the function signature.

