---

title: JavaScript ReferenceError: Deprecated caller or arguments usage

date: 2025-05-26

---


# JavaScript ReferenceError: Deprecated caller or arguments usage

The JavaScript language has evolved significantly over the years, introducing new features and refining existing ones to improve security and reliability. One aspect of this evolution involves the restricted behavior of certain properties in strict mode, a programming environment that enforces more precise semantics. This article explores the deprecated usage of Function.caller and Function.arguments, properties that enable access to the calling function and arguments, respectively. While these properties were once freely accessible, modern JavaScript environments enforce strict restrictions on their use, resulting in TypeError exceptions when accessed in non-compliant code. Understanding these changes is crucial for developers working in strict mode, as it affects both named function references and the automatically created arguments object. Through detailed examination of error scenarios and technical implementation, this article provides insights into why these properties are restricted and how developers can avoid common pitfalls associated with their deprecated usage.


## Error Mechanism

Function.caller and Function.arguments are properties that allow access to the calling function and function arguments, respectively. In a standard JavaScript environment, Function.caller returns the function that invoked the current function, while Function.arguments provides an array of the current function's arguments.

In strict mode, these properties are restricted to prevent dangerous access patterns and maintain code privacy. The restricted access results in a TypeError when attempting to read these properties. This restriction applies to all major browsers, though the exact error messages vary:

- Edge: TypeError: 'arguments', 'callee' and 'caller' are restricted function properties and cannot be accessed in this context

- Firefox: Warning: ReferenceError: deprecated caller usage

- Safari: TypeError: 'callee' and 'caller' cannot be accessed in strict mode

The restricted access is part of JavaScript's strict mode implementation, which modifies behavior and semantics from the standard environment. While Function.caller remains accessible directly on named function references, Function.arguments can still be accessed using arguments[0], arguments[1], etc., as these properties are automatically created by JavaScript within every function.


## Error Manifestation Across Browsers

The error manifests differently across browsers:

EDGE: TypeError: 'arguments', 'callee' and 'caller' are restricted function properties and cannot be accessed in this context

Firefox: Warning: ReferenceError: deprecated caller usage

SAFARI: TypeError: 'callee' and 'caller' cannot be accessed in strict mode

The restricted access results in a TypeError when attempting to read these properties in strict mode. This implementation varies between browsers:

- Edge explicitly blocks direct access to 'arguments', 'callee', and 'caller' properties

- Firefox issues a warning to indicate deprecated caller usage

- Safari prevents access to both 'callee' and 'caller' properties in strict mode

These differences in error manifestation reflect the varying approaches browsers take to enforce JavaScript standards, particularly when strict mode is enabled. The direct blocking of property access in Edge and Safari represents a stricter enforcement of JavaScript's restricted behavior, while Firefox's warning approach provides developers with more context about the deprecated usage.


## Strict Mode and JavaScript's Restricted Variation

In strict mode, these properties are part of a restricted variation of JavaScript that modifies behavior and semantics from the standard environment. This restricted version prevents access to Function.caller and Function.arguments to enforce stricter code practices and maintain privacy.

These properties pose significant security risks through data leakage, as they expose function call information that can compromise code privacy. The properties are also non-standard, making their behavior inconsistent across implementations. From an optimization standpoint, their unpredictable nature hampers efficient function processing, particularly in complex call stacks or recursion scenarios.

The restricted access applies consistently across major browser implementations, though the specific error messages differ:

- Edge blocks direct access to 'arguments', 'callee', and 'caller' properties

- Firefox provides a warning for deprecated caller usage

- Safari prevents access to both 'callee' and 'caller' properties in strict mode

Understanding this restriction is crucial for developers working in environments that enable strict mode, as code that inadvertently accesses these properties will fail to execute. This includes both named function references and automatically created arguments objects, though developers can still access arguments using the standard arguments[0], arguments[1], etc. pattern.


## Specific Error Scenarios

The following examples demonstrate the specific scenarios that trigger the deprecated caller or arguments usage error in JavaScript strict mode:


### Function.caller Usage

Attempting to access the caller function within strict mode results in a TypeError:

```javascript

function GFG_Fun() {

  return GFG_Fun.caller; // Error here

}

GFG_Fun();

```

This call to GFG_Fun() produces the error message: "TypeError: 'caller', 'callee', and 'arguments' properties may not be accessed on strict mode functions or the arguments objects for calls to them"


### Function.arguments Usage

Accessing the function arguments object similarly triggers a TypeError in strict mode:

```javascript

function f(n) {

  g(n - 1);

}

function g(n) {

  console.log(`before: ${g.arguments[0]}`);

  if (n > 0) {

    f(n);

  }

  console.log(`after: ${g.arguments[0]}`);

}

f(2);

console.log(`returned: ${g.arguments}`); // TypeError: 'caller', 'callee', and 'arguments' properties may not be accessed on strict mode functions or the arguments objects for calls to them

```


### Recursive Function Call Example

A recursive function call using arguments.callee demonstrates the error:

```javascript

const sillyFunction = function (recursed) {

  if (this !== globalThis) {

    console.log("This is:", this);

  } else {

    console.log("This is the global");

  }

  if (!recursed) {

    return arguments.callee(true);

  }

};

sillyFunction(); // This is the global // This is: [object Arguments]

function foo(n) {

  if (n <= 0) {

    return;

  }

  arguments.callee(n - 1); // Error here

}

foo(5);

```

The second call to foo() produces the same TypeError as previously mentioned.


### Module Context Example

In ES6 modules, the use of new Function to create a function that logs the caller demonstrates the error:

```javascript

let fn = new Function('e', ' new Function('console.log(arguments.callee.caller)')()')

fn(5);

```

These examples illustrate the specific circumstances under which JavaScript strict mode prohibits accessing Function.caller and Function.arguments, resulting in the deprecated caller or arguments usage error.


## Performance and Security Implications

These properties are deprecated primarily due to their potential for data leakage. By exposing the function caller and arguments, these properties can compromise code privacy and security. The unrestricted access to function call information poses a significant risk of data exposure, making them difficult to use safely in modern JavaScript environments.

From an implementation standpoint, these properties are also problematic. Their inconsistent behavior across browser implementations makes them challenging to optimize effectively. Function optimization processes are complicated by the unpredictable nature of these properties, particularly in complex call stacks or recursive scenarios.

The deprecation decision reflects a broader trend in JavaScript development toward stricter code practices and enhanced security standards. While these properties have historical significance in certain contexts, their reliability and performance implications have led to their removal from standard JavaScript behavior. Modern JavaScript development strongly encourages avoiding these properties in favor of safer alternatives.

