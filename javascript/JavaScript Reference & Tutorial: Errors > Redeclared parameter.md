---

title: JavaScript Redeclaration Error: Formal Parameters

date: 2025-05-26

---


# JavaScript Redeclaration Error: Formal Parameters

JavaScript's variable declaration rules have evolved significantly since the language's inception, introducing let and const alongside the original var keyword. While these changes bring improved scope management and fewer common pitfalls, they've also introduced subtle issues that catch developers off guard. One such issue is the "redeclaration error" involving formal parameters - specifically, what happens when you try to declare a function parameter with the same name as a local variable. This article explores the specifics of this SyntaxError, its compatibility across browsers, and provides practical solutions to avoid these frustrating development roadblocks.


## Redeclaration Error Overview


### Error and Browser Compatibility

The "redeclaration of formal parameter" error is a SyntaxError that occurs when a function parameter with the same name is declared multiple times within the same function body using let. The specific error message varies by browser:

- Edge reports "Let/Const redeclaration"

- Firefox displays "SyntaxError: redeclaration of formal parameter"

- Chrome reports "SyntaxError: Identifier has already been declared"


### JavaScript Error Handling

All error objects in JavaScript, including SyntaxError, inherit from the base Error object. The SyntaxError object specifically inherits from the Error object, making it part of JavaScript's native error handling mechanism.


### Common Scenarios

The most common scenario is declaring a function parameter and then attempting to declare it again using let within the same function body. For example:

```javascript

function f(arg) {

  let arg = 'foo'; // SyntaxError: redeclaration of formal parameter "arg"

}

```

In this case, the inner let declaration conflicts with the outer function parameter. To avoid this error, you can either omit the let keyword if you're only modifying the parameter value:

```javascript

function f(arg) {

  arg = 'foo'; // No error

}

```

Alternatively, if you need to create a new variable within the function, you must use a different name:

```javascript

function f(arg) {

  let bar = 'foo'; // No error

}

```


### Variable Declaration Fundamentals

JavaScript provides three main keywords for variable declaration: var, let, and const. Understanding their behavior is crucial for avoiding redeclaration errors:

- var: Allows redeclaration but creates the same variable in the outer scope

- let: Does not allow redeclaration within the same scope, creating a new local variable

- const: Same behavior as let, with the additional restriction of preventing value reassignment

When declaring variables within function scopes, let and const require careful naming to avoid conflicts with function parameters. This is particularly important in modern JavaScript development where block-scoping (introduced by let and const) is standard practice.


## Error Messages and Browser Compatibility

The error messages vary by browser. Edge reports "Let/Const redeclaration," Firefox displays "SyntaxError: redeclaration of formal parameter," and Chrome reports "SyntaxError: Identifier has already been declared" (41).

The error type is SyntaxError, which specifically occurs when a variable name that is both a function parameter and declared again inside the function body using let. Prior to Firefox 49, this was thrown as a TypeError (bug 1275240).

All error objects in JavaScript, including SyntaxError, inherit from the base Error object. The SyntaxError object specifically inherits from the Error object, making it part of JavaScript's native error handling mechanism. This inheritance allows developers to use standard error handling techniques for SyntaxError objects.

The issue arises when the same variable name appears both as a function parameter and is declared again inside the function body using let. For example:

```javascript

function GFG(var_name) {

  let var_name = 'This is GFG';

  return var_name;

}

document.write(GFG());

```

This code produces a SyntaxError: Let/Const redeclaration in Edge, while Firefox displays SyntaxError: redeclaration of formal parameter "var_name" and Chrome reports SyntaxError: Identifier "var_name" has already been declared.

The error occurs in both V8-based browsers and Firefox, with slightly different error messages. Safari throws SyntaxError: Cannot declare a let variable twice: 'var_name'.

For developers working with older versions of Firefox, this error was initially reported as a TypeError. Developers can effectively handle this error using a try-catch block. For example:

```javascript

try {

  function f(arg) {

    let arg = 'foo';

  }

} catch (error) {

  console.error(error.message);

}

```

This approach allows developers to catch and handle the error while maintaining clean code structure.


## Common Scenarios and Solutions

The most common scenario is declaring a function parameter and then attempting to declare it again using let within the same function body. For example:

```javascript

function f(arg) {

  let arg = 'foo'; // SyntaxError: redeclaration of formal parameter "arg"

}

```

In this case, the inner let declaration conflicts with the outer function parameter. To avoid this error, you can either omit the let keyword if you're only modifying the parameter value:

```javascript

function f(arg) {

  arg = 'foo'; // No error

}

```

Alternatively, if you need to create a new variable within the function, you must use a different name:

```javascript

function f(arg) {

  let bar = 'foo'; // No error

}

```

A related issue occurs when using the var keyword in strict mode, where variable names that are also function parameters cannot be redeclared inside the function:

```javascript

'use strict';

function fun(varName) {

  let varName = 'This is GFG'; // Error Here

}

```

Output: TypeError: variable "varName" redeclares argument

The error arises when a function parameter is declared multiple times within the function body using let, which violates JavaScript's variable declaration rules. This rule allows optional initialization with the var statement but requires that let and const declarations be unique within their scope.

To avoid redeclaration errors, developers should follow these best practices:

1. Use different variable names for parameters and local variables

2. Avoid using let or const for parameter initialization

3. Use var for parameter initialization in strict mode

4. Understand the scope and lifetime of variables in JavaScript functions

By adhering to these guidelines, developers can prevent common redeclaration errors while maintaining clean and maintainable code.


## JavaScript Variable Declaration Fundamentals

JavaScript offers three primary keywords for variable declaration: var, let, and const. Each keyword has distinct characteristics regarding variable scope, initialization, and redeclaration.

The var keyword, introduced with JavaScript's initial release in 1995, remains supported for legacy browser compatibility. It provides function scope rather than block scope, meaning that var-declared variables maintain their value across multiple function calls. Multiple var declarations can occur without raising errors, as the same variable name retains its outer scope value. For example:

```javascript

function testVariable() {

  var x = 10;

  console.log(x);

  var x = 20;

  console.log(x);

  x = 30;

  console.log(x);

}

testVariable(); // Outputs: 10, 20, 30

```

Despite its flexibility, var should generally be avoided in modern JavaScript development due to its broader scope implications.

The let keyword introduces block scope, meaning that let-declared variables are confined to their nearest block (e.g., if statements, loops, function bodies). This scope type prevents variable hoisting, which can lead to more predictable and maintainable code. However, let variables cannot be redeclared within the same scope, though their value can be reassigned:

```javascript

let y = 10;

console.log(y); // Outputs: 10

let y = 20; // SyntaxError: Identifier 'y' has already been declared

y = 30;

console.log(y); // Outputs: 30

```

When declaring variables within function scopes, let follows block scope rules. This means that while the initial declaration can be omitted, any subsequent attempts to declare the same variable name using let will result in a SyntaxError.

The const keyword behaves similarly to let but introduces "read-only" semantics. Once assigned, a const variable's value cannot be reassigned, and the variable name cannot be redeclared:

```javascript

const z = 10;

console.log(z); // Outputs: 10

const z = 20; // SyntaxError: Identifier 'z' has already been declared

z = 30; // TypeError: Assignment to constant variable

```

Similar to let, const respects block scope. Therefore, attempting to redeclare a const variable within the same block scope will also result in an error.

The var keyword retains its value across multiple function calls due to its function scope, while let and const follow block scope rules. This difference is particularly important when determining how variables behave across nested function scopes:

```javascript

function scopeTest() {

  var x = 'outer';

  if (true) {

    var x = 'inner'; // Does not create a new variable, shadows the outer variable

    console.log(x); // Outputs: inner

  }

  console.log(x); // Outputs: inner

}

function scopeTestLet() {

  let y = 'outer';

  if (true) {

    let y = 'inner'; // Throws SyntaxError: Identifier 'y' has already been declared

    console.log(y); // Unreachable code

  }

  console.log(y); // Outputs: outer

}

```

Understanding these differences enables developers to choose the most appropriate declaration keyword based on their specific use case, ensuring both correctness and maintainability in their codebase.


## Advanced Topics

JavaScript's variable declaration rules evolve from the initial release of var in 1995 to the modern let and const keywords. Understanding these rules requires examining both redeclaration and reassignment capabilities across var, let, and const.

The var keyword, while widely supported for legacy browser compatibility, exhibits some unique behaviors. Multiple var declarations can occur without raising errors, as the same variable name retains its outer scope value. For example:

```javascript

function testVariable() {

  var x = 10;

  console.log(x);

  var x = 20;

  console.log(x);

  x = 30;

  console.log(x);

}

testVariable(); // Outputs: 10, 20, 30

```

Despite its flexibility, var should generally be avoided in modern JavaScript development due to its broader scope implications. The primary advantage of var is its function scope, which maintains variable values across multiple function calls. This behavior differs significantly from let and const, which observe block scope rules.

When redeclaring variables, JavaScript handles let and const with stricter constraints than var. The let keyword introduces block scope, meaning that let-declared variables are confined to their nearest block (e.g., if statements, loops, function bodies). This scope type prevents variable hoisting, which can lead to more predictable and maintainable code. However, let variables cannot be redeclared within the same scope, though their value can be reassigned:

```javascript

let y = 10;

console.log(y); // Outputs: 10

let y = 20; // SyntaxError: Identifier 'y' has already been declared

y = 30;

console.log(y); // Outputs: 30

```

The const keyword behaves similarly to let but introduces "read-only" semantics. Once assigned, a const variable's value cannot be reassigned, and the variable name cannot be redeclared:

```javascript

const z = 10;

console.log(z); // Outputs: 10

const z = 20; // SyntaxError: Identifier 'z' has already been declared

z = 30; // TypeError: Assignment to constant variable

```

While let and const follow block scope rules, their handling of redeclaration within nested scopes is crucial for developers to understand. The JavaScript engine allows redeclaration in nested blocks, with the redeclared variable going out of scope when exiting that block. This behavior is demonstrated in the following example:

```javascript

function fullName(first, last) {

  let first = 'John';

  if (true) {

    let value = 10; // Allowed redeclaration within nested block scope

    console.log(value); // Outputs 10

  }

  console.log(value); // Unreachable code

}

```

This example shows that declaring `value` within an if statement does not conflict with the function parameter value, as each declaration operates within its own block scope. This pattern works consistently whether the declaration remains inside or is moved outside the if statement, demonstrating the distinct scope handling of let and const.

The var keyword retains its value across multiple function calls due to its function scope, while let and const follow block scope rules. This difference is particularly important when determining how variables behave across nested function scopes:

```javascript

function scopeTest() {

  var x = 'outer';

  if (true) {

    var x = 'inner'; // Does not create a new variable, shadows the outer variable

    console.log(x); // Outputs: inner

  }

  console.log(x); // Outputs: inner

}

scopeTest(); // Outputs: inner

```

In this example, attempting to redeclare x within the if block shadows the outer variable value rather than creating a new scope. This behavior differs from let and const, which enforce strict scope boundaries and prevent redeclaration within the same block scope:

```javascript

function scopeTestLet() {

  let y = 'outer';

  if (true) {

    let y = 'inner'; // Throws SyntaxError: Identifier 'y' has already been declared

    console.log(y); // Unreachable code

  }

  console.log(y); // Outputs: outer

}

scopeTestLet(); // Outputs: outer

```

Understanding these scope differences enables developers to choose the most appropriate declaration keyword based on their specific use case, ensuring both correctness and maintainability in their codebase. Modern JavaScript development strongly recommends using let and const, leveraging their block scope and modern variable management features while avoiding the pitfalls of var's broader scope implications.

