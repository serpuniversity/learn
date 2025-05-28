---

title: JavaScript Reference & Tutorial: Errors > Duplicate parameter

date: 2025-05-26

---


# JavaScript Reference & Tutorial: Errors > Duplicate parameter

JavaScript functions can contain multiple parameters with the same name, where later parameters override earlier ones. While this behavior is permitted in non-strict mode, it's fundamentally problematic and should be avoided. This article explores the intricacies of duplicate parameter names in JavaScript, examining how different JavaScript engines handle them, discussing the implications for code clarity, and offering best practices to maintain robust, maintainable JavaScript codebases.


## Duplicate parameter names in JavaScript

JavaScript allows functions to have multiple parameters with the same name, where later parameters override earlier ones. This behavior is error-prone and should be avoided.

In non-strict mode, JavaScript permits this behavior, though the second occurrence of a parameter name shadows the first. For example:

```javascript

function f(a, a) {

  console.log(a)

}

```

In strict mode, duplicate parameter names are illegal, causing an immediate syntax error. The text notes that TypeScript provides similar functionality, with the ID js/duplicate-parameter-name and Kind problem, and a security severity of error and precision of very-high.

The behavior of duplicate parameters is defined in the ECMAScript Language Specification, with specific rules for strict mode and modern JavaScript features like default parameters and rest operators. Modern engines like V8, Firefox, and Safari handle this differently, with stricter checks in modern JavaScript and strict mode environments.

To avoid this issue, the article recommends renaming conflicting parameters to maintain code clarity and avoid unintentional variable shadowing. The recommended solution is to use distinct names for each parameter, for example:

```javascript

function func(a, b, c) { console.log(a, b, c); }

const logger = function (a, b, c) { console.log(a, b, c); };

```


## Error handling and compatibility

Duplicate parameter errors behave differently across browsers and JavaScript engines, with stricter checks present in modern JavaScript and strict mode environments. This behavior stems from distinct parsing rules applied by engines like V8, Firefox, and Safari.

In non-strict function declarations, JavaScript permits duplicate parameter names, where later parameters override earlier ones. For example:

```javascript

function f(a, a) { console.log(a) }

```

However, in strict mode, both function declarations and expressions with duplicate parameter names throw an immediate SyntaxError. Modern engines like V8 and Firefox enforce these stricter rules, while Safari applies additional constraints particularly to functions using default parameter values, rest parameters, or destructuring:

```javascript

function g(x, { name: x }) { console.log(x) } // Throws error in Safari

function h() { return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] } // Valid in Safari

```

According to the ECMAScript specification, when checking function parameters, engines must confirm that all parameter names are unique within the same function scope. This rule applies to all forms of function declarations and expressions, including those utilizing default parameter values, rest parameters, or object destructuring.

To demonstrate these constraints:

```javascript

function invalid(f, f) { "use strict" } // Throws error in all modern browsers

function valid(x, { y: x }) { console.log(x, y) } // Logs x from object destructuring

```

Violations of this rule typically manifest as syntax errors during parsing, preventing the creation of invalid function scopes. The specification also notes that while some constructs like `function (x, [x]) { ... }` are explicitly allowed, others leading to name conflicts must be avoided.

Developers attempting to handle these errors often implement global error catching with `window.onerror` but may face limitations when stack traces are empty, particularly in older browsers or browser extensions. Alternative approaches include using comprehensive error tracking tools like Bugsnag, Sentry, or NewRelic, which provide more detailed context for tracking and resolving such issues.


## Best practices and recommendations

Duplicate parameters with the same name can lead to unexpected behavior in JavaScript functions. While older versions of JavaScript allowed this behavior, modern engines and strict mode enforce stricter rules to prevent shadowing and improve code clarity.

In non-strict function declarations, JavaScript permits duplicate parameter names, where the second parameter shadows the first. For example:

```javascript

function f(a, a) {

  console.log(a)

}

```

However, in strict mode, both function declarations and expressions with duplicate parameter names throw an immediate SyntaxError. Modern engines like V8, Firefox, and Safari enforce these stricter rules, particularly when using features like default parameter values, rest parameters, or destructuring:

```javascript

function g(x, { name: x }) { console.log(x) } // Throws error in Safari

function h() { return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] } // Valid in Safari

```

Best practice is to rename conflicting parameters to maintain code clarity and avoid unintentional variable shadowing. For functions using `reduce`, consider using `_` for omitted parameters and naming the other parameter as `__` (double underscore):

```javascript

objects.reduce((prev_items, curr_items_obj, _, __) => {

  // Function body

});

```

JavaScript's linting rules, particularly "noDuplicateParameters" in tools like Biome, help identify and prevent these issues while maintaining compatibility with older code.


## Technical details and specifications

According to the ECMAScript Language Specification, when declaring function parameters, the interpreter checks for duplicate names. If a function contains multiple parameters with the same name, it may result in an error depending on the execution context.


### Non-Strict Mode Behavior

In non-strict mode, JavaScript allows functions to have multiple parameters with the same name. The later parameter shadows any earlier ones with the same name. For example:

```javascript

function f(a, a) { console.log(a) }

```

This function would successfully declare and execute, with the second 'a' parameter shadowing the first. If both parameters were accessed, only the second 'a' would be referenced.


### Strict Mode Behavior

Strict mode enforces stricter rules for function declarations and expressions. If a source code matches the function parameter syntax and is in strict mode, additional error checking occurs during parsing. This leads to an immediate SyntaxError for duplicate parameter names:

```javascript

function f(a, a) { "use strict"; console.log(a) } // Throws SyntaxError

```


### Modern JavaScript Features

The specification includes specific rules for modern JavaScript features including default parameters and rest operators. For instance:

```javascript

function f(x, { name: x }) { console.log(x) } // Throws error in Safari

```

Here, the second 'x' parameter conflicts with the destructured parameter, resulting in a SyntaxError. Similarly, functions using default parameter values or rest parameters must ensure unique parameter names:

```javascript

function f(x, [x]) { ... } // Allowed

function g(x, { y: x }) { ... } // Throws error in Safari

```


### Parameter Binding Behavior

When a function parameter is bound multiple times, the last occurrence takes precedence. This applies to both function declarations and expressions. For example:

```javascript

function f(first, second, first) { return [first, second] }

f(1, 2, 3) // Returns [3, 2]

f(1, 2)    // Returns [undefined, 2]

```

The second and third occurrences of 'first' parameter bind to the same variable, with the third taking precedence.


### Linting and Validation

JavaScript development tools enforce these rules through linting. The Biome linter includes a "noDuplicateParameters" rule within the "lint/suspicious" diagnostic category. This rule helps developers maintain clean, error-free code by identifying and preventing duplicate parameter issues.

