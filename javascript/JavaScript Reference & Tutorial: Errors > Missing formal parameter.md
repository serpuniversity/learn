---

title: JavaScript Errors: Missing Formal Parameter

date: 2025-05-26

---


# JavaScript Errors: Missing Formal Parameter

JavaScript's function parameters play a crucial role in shaping how functions interact with the code around them. Whether you're building complex applications or simple scripts, understanding how to correctly declare and use function parameters is essential. However, navigating the language's syntax rules can be tricky, especially when working with formal parameters - those defined in a function declaration.

This guide will help you avoid a common JavaScript error: "missing formal parameter." You'll learn what makes a valid parameter, how to properly declare and call functions with parameters, and what common mistakes to watch out for. We'll also explore related syntax issues to ensure your functions work smoothly in all parts of your code.


## What is a Formal Parameter?

In JavaScript function declarations, formal parameters must be identifiers - which are names that represent values in the code. These identifiers can contain letters, digits, underscores (_), or dollar signs ($), but cannot begin with a digit. Common mistakes that cause the "missing formal parameter" error include passing numbers or strings directly instead of variable names, and using invalid characters in parameter names.

For example, attempting to declare a function like `function example(123) {}` will result in a syntax error, as the parameter must be an identifier such as `function example(number) {}`. Similarly, using invalid characters in parameter names like `function example(x@) {}` will also produce a syntax error.

Function calls require providing values for these identifier parameters, though the function declaration itself must use valid identifiers. For instance, while `function example(x) { return x + 1; }` is correct, calling it with a direct value like `example(3)` is appropriate syntax. The error will occur if the function declaration tries to use a value where an identifier is expected.


## Common Causes of the Missing Formal Parameter Error

The "missing formal parameter" error occurs when your function declaration is missing valid parameters. This can happen during function declaration or when the browser cannot determine the arguments passed. The error indicates that the function requires arguments that can accept different possible values, not fixed string values.

Common causes include:

1. Function syntax errors with commas: For example, `function example(a, , b) { return a + b; }` will produce the error when called. The correct syntax should be `function example(a, b) { return a + b; }`.

2. Arrow function errors: When an arrow function lacks parameter definitions: `const exampleFunction = (a, , b) => a + b;` will trigger the error. The corrected version should be `const exampleFunction = (a, b) => a + b;`.

3. Function constructor misuse: Incorrect usage of the Function constructor like `const exampleFunction = new Function('a', '', 'b', 'return a + b');` will result in the error. The proper implementation is `const exampleFunction = new Function('a', 'b', 'return a + b');`.

4. Invalid parameter names: Using names that don't start with a letter, dollar sign, or underscore, such as `function example(x@) {}`, will also produce the error.

5. Repetitive parameter declaration: Declaring the same variable name as both a function parameter and inside the function body using let assignment can cause the "redeclaration of formal parameter" error: `function example(x) { let x = 'value'; }`.

The error can be resolved by ensuring all parameter lists meet the following criteria:

- Use valid parameter names consisting of letters, digits, underscores, or dollar signs

- Avoid extra commas in the parameter list

- Prevent malformed destructuring assignments in the parameter list


## Correcting Missing Formal Parameter Errors

To address these errors effectively, it is crucial to ensure that all required arguments are passed when calling or declaring functions. JavaScript function parameters must be identifiers, not numbers, strings, or objects. This means that while function calls provide the values for these identifiers, the function declarations must use valid identifier names consisting only of letters, digits, underscores, or dollar signs.

When declaring functions using the Function constructor, it's important to correctly format the parameter list. This includes avoiding extra commas and ensuring proper punctuation. For example, incorrect usage like `new Function('a', '', 'b', 'return a + b;')` should be corrected to `new Function('a', 'b', 'return a + b;')`.

The error can also occur when using destructuring assignments in parameter lists. Incorrect usage such as `function({x, y,}) { ... }` should be corrected to ensure proper formatting and syntax, as demonstrated in the correct version: `function({x, y}) { ... }`.

Developers should avoid using numbers as parameter names entirely, as shown in the failed example `function(12, 9) { ... }`. The correct implementation requires passing identifiers, as in the corrected versions: `function(number) { ... }` and `function(greeting) { ... }`.

To resolve these errors, developers should check their function declarations for proper parameter syntax and ensure that all required arguments are being passed in function calls. This includes verifying that all parameter names adhere to the valid identifier rules specified in the ECMA-262 specification, specifically avoiding numbers at the beginning of identifier names and ensuring proper formatting for special cases like destructuring assignments.


## Additional JavaScript Syntax Errors Related to Function Parameters


### Additional JavaScript Syntax Errors Related to Function Parameters

JavaScript function parameter syntax issues can lead to multiple syntax errors. Understanding these related errors is crucial for effective debugging and coding.


#### Malformed Formal Parameter Error

This error occurs when the argument list of a Function() constructor call is not valid. Specific error messages vary by browser:

- Edge: SyntaxError: Expected {x}

- Firefox: SyntaxError: malformed formal parameter

The argument list can contain invalid characters in parameter names, incorrect punctuation, or malformed destructuring assignments:

```javascript

function example(x, y@) { return x + y; } // Invalid character in parameter name

function example(x,, y) { return x + y; } // Incorrect punctuation

function example({x, y,}) { return x + y; } // Malformed destructuring assignment

```

Correct implementations avoid these issues:

```javascript

function example(x, y) { return x + y; }

function example({x, y}) { return x + y; }

```


#### Redefinition of Formal Parameter Error

This error occurs when the same variable name is declared as both a function parameter and in the function body using a `let` assignment:

```javascript

function example(x) { let x = 'value'; } // SyntaxError: Identifier "x" has already been declared

```

To fix this error, avoid redeclaring the same variable name within the same function scope:

```javascript

function example(x) { let y = 'value'; } // Correct implementation

```

Understanding these errors helps developers ensure proper JavaScript function syntax and avoid common pitfalls in parameter declaration and usage.

