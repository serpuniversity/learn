---

title: JavaScript Reference & Tutorial: Errors > Not defined

date: 2025-05-26

---


# JavaScript Reference & Tutorial: Errors > Not defined

JavaScript's undefined value serves as a placeholder for uninitialized variables, yet improper variable management can lead to frequent "not defined" errors. This guide explores the nuances of undefined values, common causes of reference errors, and best practices for maintaining robust JavaScript code. Whether you're encountering mysterious uncaught errors or troubleshooting complex library interactions, this comprehensive overview will help you develop more reliable and maintainable JavaScript applications.


## Basic Concepts

JavaScript uses the keyword undefined to represent uninitialized variables. When a variable is declared using var, let, or const but not assigned a value, it holds the value undefined until assigned. For example:

```javascript

let a;

console.log(a); // Output: undefined

a = 5;

console.log(a); // Output: 5

```

The undefined value serves as a default state for variables before they receive a meaningful value. Variables declared with let or const maintain their undefined state until explicitly assigned a value.

A common mistake is accessing variables before they are declared. In JavaScript, variables must be declared before being used. For instance:

```javascript

console.log(b); // Output: Uncaught ReferenceError: b is not defined

let b = 'Hello';

```

This error occurs because JavaScript looks for the variable b in the current scope but finds nothing. Understanding scope is crucial: var variables have function or global scope, while let and const have block scope.

JavaScript also uses undefined to represent properties or array elements that do not exist:

```javascript

let person = { name: "John", age: 30 };

console.log(person.address); // Output: undefined

let fruits = ["apple", "banana", "orange"];

console.log(fruits[3]); // Output: undefined

```

In these cases, accessing a non-existent property or element returns the value undefined, indicating that the object or array lacks the specified property or element.

JavaScript distinguishes between undefined and not defined errors through proper variable declaration and scope management. Understanding these concepts is essential for effective JavaScript development.


## Common Causes

The most frequent reason for 'not defined' errors in JavaScript is referencing a variable, function, or identifier that has not been declared or does not exist within the current scope. This occurs when a variable is accessed before it has been declared, or when attempting to use a library variable before the library has been loaded.

The error can appear in several scenarios:

1. A variable is referenced before declaration:

```javascript

console.log(myVariable); // ReferenceError: myVariable is not defined

let myVariable = 'error fixed';

```

1. A variable is accessed in a scope where it is not available:

```javascript

function outerFunction() {

  let innerVariable = 'inner';

  console.log(innerVariable); // Output: 'inner'

}

outerFunction();

console.log(innerVariable); // ReferenceError: innerVariable is not defined

```

1. A library variable is accessed before the library is loaded:

```javascript

$("myElement"); // ReferenceError: $ is not defined

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

```

To resolve these issues, developers should ensure variables are declared before being accessed, and that all required libraries are loaded before attempting to use their variables. This includes properly sequencing script tags in HTML, using document loading events to delay execution until dependencies are available, and avoiding typos in variable names.


## jQuery-Specific Errors

The "$" symbol in JavaScript and jQuery requires a link to files to run, unlike plain JavaScript. When using jQuery, attempting to call "$" before declaring the function results in a "ReferenceError: $ is not defined" error. This occurs because JavaScript does not recognize "$" when jQuery hasn't loaded yet, even with $(document).ready().

Several factors can cause this issue:

- Incorrect path to jQuery library

- Corrupted jQuery library file

- Working offline

- Conflict with other libraries

To resolve these issues, developers should:

1. Ensure jQuery is included and loaded correctly

2. Check for typos

3. Manage library conflicts using jQuery's noConflict() method

4. Clear browser cache during development

The error most commonly occurs when jQuery code is executed before the jQuery library file has loaded. To fix this, the jQuery code should be executed only after the jQuery library file has finished loading. This ensures proper access to the jQuery object.

When using jQuery, always place the jQuery library script tag at the top of the HTML file, before any scripts that reference jQuery. For example:

```html

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>

  $(document).ready(function() {

    // jQuery code here

  });

</script>

```

Using the noConflict() method can help manage conflicts with other libraries that might use the $ symbol. After calling noConflict(), use jQuery instead of $ in your code. For example:

```javascript

var jq = $.noConflict();

jq(document).ready(function() {

  jq('#myElement').doSomething();

});

```

In cases where the issue persists, check that all jQuery functions are wrapped in a document.ready or window.onload function to ensure they run after the library has loaded. For example:

```javascript

window.onload = function() {

  // Your jQuery code here

};

```

To troubleshoot, verify that the jQuery script tag is not placed in the footer, where it might execute before the page is fully loaded. Instead, place it in the head section or before any dependent scripts.

For scenarios where scripts are generated dynamically or loaded asynchronously, use a loading indicator or event listener to delay execution until jQuery is available. This ensures consistent behavior across different development environments and configurations.


## Code Examples

The MDN Web Docs provides detailed information about JavaScript syntax errors, including the ReferenceError. This error occurs when attempting to access variables or identifiers that are not declared or do not exist within the current scope.


### Case Studies

The documentation demonstrates that undeclared variables result in ReferenceError. For example:

```javascript

let a;

console.log(a); // Output: undefined

a = 5;

console.log(a); // Output: 5

```

In this scenario, accessing `a` before assignment triggers undefined behavior but no error. However, attempting to use the variable outside its scope or before declaration leads to ReferenceError:

```javascript

console.log(b); // Output: Uncaught ReferenceError: b is not defined

let b = 'Hello';

```

The documentation also notes that undeclared global variables become implicit globals when assigned, while block-scoped variables (let and const) cause ReferenceError if accessed before declaration:

```javascript

if (false) {

  var a = 1;

}

console.log(a); // Output: 1 (due to var's function scope)

let b;

console.log(b); // Output: Uncaught ReferenceError: b is not defined

```


### Property and Array Access

Accessing non-existent properties or out-of-bounds array elements returns undefined, not triggering ReferenceError:

```javascript

let person = { name: "John", age: 30 };

console.log(person.address); // Output: undefined

let fruits = ["apple", "banana", "orange"];

console.log(fruits[3]); // Output: undefined

```

However, referencing symbols without initializing them results in ReferenceError:

```javascript

const symbol = Symbol();

console.log(symbol.description); // Output: Uncaught TypeError: Property 'description' of symbol #<Symbol> is not a function

```


### Function Behavior

Functions returning undefined without explicit return statements behave as expected:

```javascript

function greet() {

  console.log("Hello!");

}

let result = greet();

console.log(result); // Output: undefined

```

Attempting to use undeclared functions causes ReferenceError:

```javascript

console.log(notDefinedFunction()); // Output: Uncaught ReferenceError: notDefinedFunction is not defined

```


### Scope and Visibility

The text emphasizes the importance of variable scope, noting that undeclared variables can become global when assigned:

```javascript

var x = 10;

console.log(window.x); // Output: 10

let y;

console.log(y); // Output: undefined

y = 20;

console.log(window.y); // Output: undefined

```

Understanding these distinctions helps developers write more robust JavaScript code by properly managing variable declaration and scope.


## Best Practices


### Proper Variable and Function Declaration

To prevent "not defined" errors, always declare variables and functions before using them. JavaScript automatically assigns undefined to undeclared variables during initialization. For example:

```javascript

let a;

console.log(a); // Output: undefined

a = 5;

console.log(a); // Output: 5

```

When a variable is declared but not assigned before use, JavaScript treats it as undefined. However, attempting to access an undeclared variable results in a ReferenceError:

```javascript

console.log(b); // Output: Uncaught ReferenceError: b is not defined

let b = 'Hello';

```


### Understanding Scope and Visibility

JavaScript variables have different scopes based on their declaration:

- var: Function scope or global scope

- let and const: Block scope

Declare variables within the smallest possible scope to limit their visibility. For example, declaring a variable inside an if block limits its accessibility:

```javascript

if (false) {

  var a = 1;

}

console.log(a); // Output: 1 (due to var's function scope)

let b;

console.log(b); // Output: Uncaught ReferenceError: b is not defined

```


### Managing Library and Function Dependencies

Ensure all required libraries and dependencies are loaded before using their variables or functions. For jQuery, place the library script tag at the top of the HTML file and wrap code in document ready functions:

```html

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>

  $(document).ready(function() {

    // Your jQuery code here

  });

</script>

```


### Handling Typos and Name Conflicts

Double-check variable and function names for typos. A simple typo can cause a "not defined" error:

```javascript

console.log(mesage); // ReferenceError: mesage is not defined

let message = "Hello, world!";

console.log(message); // Output: Hello, world!

```


### Error Monitoring and Debugging

Use error monitoring tools like Rollbar to track and debug JavaScript errors in real-time. These tools help identify and resolve issues across different environments and configurations.


### Best Practices Summary

1. Always declare variables before use.

2. Use appropriate scope (var, let, const) based on variable behavior.

3. Ensure library dependencies are loaded before use.

4. Check for typos in variable names.

5. Use document.ready functions for jQuery compatibility.

6. Implement proper error handling and monitoring.

