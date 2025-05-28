---

title: JavaScript Errors > Not a function

date: 2025-05-26

---


# JavaScript Errors > Not a function

JavaScript errors can be frustrating roadblocks in web development, and one of the most common culprits is the "TypeError: is not a function" exception. This error typically appears when your code tries to call a value as a function, but that value isn't actually a function at all. Whether you're working on a massive framework project or a simple script, running into this error can halt your progress.

This guide will walk you through the mechanics of why this error occurs, common causes, and how to fix it. You'll learn to recognize the specific patterns that trigger these errors and develop strategies to prevent them in your code. By the end, you'll be equipped to handle this error and several related issues that can trip up even experienced JavaScript developers.


## Understanding the 'is not a function' Error

This JavaScript exception occurs when there was an attempt to call a value from a function, but the value is not actually a function. The error typically happens when code expects you to provide a function, but that doesn't happen. Possible causes include typos in the function name or objects that don't have the function.

For example, if you mistakenly type `document.getElementByID` instead of `document.getElementById`, you'll receive this error. Similarly, attempting to use an object that doesn't contain a specific function will also trigger this exception. For instance, trying to call the `map` function on an object instead of an array will result in a "TypeError: obj.map is not a function".

The error specifically occurs when JavaScript attempts to call a value that is not a function. The message format in modern browsers tends to be either "TypeError: Object doesn't support property or method {x}" (Edge), or "TypeError: "x" is not a function". This error occurs in various contexts, such as when a property is called on an object like a function, but is not actually a function. It can also occur when a function is called on an object that does not actually contain the function, or when the correct function name is misspelled.

To illustrate common issues, consider these examples:

```javascript

// Incorrect function name

var elem = document.getElementByID('ID'); // TypeError: document.getElementByID is not a function

var elem = document.getElementById('ID'); // Correct

// Attempting to call a property as function

var foo = { bar: 5 };

console.log(foo.bar()); // TypeError: foo.bar is not a function

console.log(foo.bar); // Correct

// Function called on object that doesn't contain it

var foo = { bar: function() { console.log("bar called"); } };

foo.baz(); // TypeError: foo.baz is not a function

foo.bar(); // Correct

```

The error can also surface when using JavaScript's built-in methods expecting callback functions. For example, attempting to use `Array.prototype.map` on an object instead of an array will trigger the error. This includes various methods like `every()`, `some()`, `forEach()`, `map()`, `filter()`, `reduce()`, `reduceRight()`, and `find()`.

Understanding these scenarios can help developers write more robust and error-free JavaScript code.


## Common Causes of 'is not a function' Errors

The most common causes of "TypeError: 'x' is not a function" errors fall into three main categories: typos in function names, incorrect object usage, and attempting to call functions on non-object values.

Typos in function names are a frequent cause of these errors. For example, using `document.getElementByID` instead of the correct `document.getElementById` will produce the error:

```javascript

var elem = document.getElementByID('ID'); // Incorrect

var elem = document.getElementById('ID');  // Correct

```

The error message specifically highlights the misspelled function name:

```javascript

TypeError: document.getElementByID is not a function

```

Incorrect object usage also frequently triggers these errors. The JavaScript `Array` object has built-in methods like `map`, `filter`, and `reduce`, but other objects do not. Attempting to call these methods on a non-array object results in the error:

```javascript

var foo = { bar: function() { console.log("bar called"); } };

foo.baz(); // Incorrect function name

foo.bar(); // Correct function name

```

The error message clearly indicates the name of the non-existent function:

```javascript

TypeError: foo.baz is not a function

```

Finally, trying to call functions on non-object values can also produce these errors. In JavaScript, only functions are callable. Attempting to call a property of an object as if it were a function will produce the error. This includes using parentheses to perform multiplication where they are not needed:

```javascript

2 * (3 + 5) // Correct

2 * (3 + 5) // Incorrect, produces "TypeError: 2 * (3 + 5) is not a function"

```

These errors typically occur in one of several common scenarios:

- Circular dependencies between files

- Missing or incorrectly imported script libraries

- Local variable name conflicts with function names

- Functions defined within other function scopes and not properly exposed

- Objects that do not contain the expected functions


## Fixing 'is not a function' Errors

To resolve "is not a function" errors, it's crucial to identify and address the specific cause of the error. Here are practical steps to help diagnose and fix these common issues:


### Correct Function Calls

First, ensure that you are calling the correct function with the right syntax. Check for typos in function names and verify that parentheses are used correctly. For example, the following code contains a typo that causes a "TypeError: document.getElementByID is not a function" error:

```javascript

var elem = document.getElementByID('ID'); // Incorrect

var elem = document.getElementById('ID');  // Correct

```


### Verify Object Usage

Ensure that you are calling functions on objects that actually contain those functions. Attempting to call an array method on an object will produce a "TypeError: obj.map is not a function" error. For instance:

```javascript

var foo = { bar: 5 };

console.log(foo.bar()); // Uncaught TypeError: foo.bar is not a function

console.log(foo.bar); // Correct

```


### Check Callback Function Arguments

When using functions that require callback arguments, ensure those callbacks actually exist. For example, using `Array.prototype.map` on an object instead of an array will trigger the error:

```javascript

[1, 2, 3].map(x => x * 2) // [2, 4, 6]

{1: 2, 2: 3}.map(x => x * 2) // TypeError: "object" is not a function

```


### Examine Function Scope

Pay particular attention to function scope, especially when dealing with nested functions. Consider the following example where a function within a scope is not accessible:

```javascript

var x = function() {

  var y = function() {

    alert('fired y');

  }

}

// Global scope cannot access y because it is closed over in x and not exposed

// y is not a function error triggered

x.y();

```

The correct approach is to ensure that nested functions are properly exposed:

```javascript

function Scorm_API_12() {

  var Initialized = false;

  this.LMSInitialize = function(param) {

    errorCode = "0";

    if (param == "") {

      if (!Initialized) {

        Initialized = true;

        errorCode = "0";

        return "true";

      } else {

        errorCode = "101";

      }

    } else {

      errorCode = "201";

    }

    return "false";

  }

  // some more functions, omitted

}

var API = new Scorm_API_12();

```


### Debugging Tips

When encountering these errors, use the following debugging techniques:

- Carefully review the error message and examine the surrounding code

- Check for typos in function names and object property accesses

- Verify that all required script libraries are correctly imported

- Ensure that functions passed as arguments actually exist

- Make sure that functions are within the correct scope

By methodically checking these areas, developers can effectively identify and resolve "is not a function" errors in their JavaScript code.


## Error Prevention Strategies

The most effective strategy for preventing "is not a function" errors is careful variable declaration and proper scope management. Ensure that all variables are defined before referencing them to avoid undefined or out-of-scope issues. In strict mode, this means using `var`, `let`, or `const` to declare all variables, as failing to do so will result in a `ReferenceError`.

To address specific error scenarios:

1. Circular dependencies between files can cause function references to be unavailable. Resolve these by restructuring your code to minimize dependencies or by using module patterns that ensure proper initialization.

2. Missing or incorrectly imported script libraries can leave required functions undefined. Always verify that all necessary libraries are correctly included and loaded before use.

3. Local variable name conflicts with function names should be avoided by using distinct names for variables and functions. If a conflict occurs, refactor the code to use unique identifiers.

4. Functions defined within other function scopes must be properly exposed to the outer scope if they need to be accessed. This requires explicit return statements or correct use of prototype inheritance.

For automated error detection, consider implementing static analysis tools in your CI pipeline. These tools can catch issues like uninitialized variables before deployment, helping prevent runtime errors. Code editors and IDEs with syntax highlighting and code completion features can also significantly reduce the occurrence of these errors by providing real-time feedback on coding mistakes.

In cases where functions are passed as arguments, ensure that the callback function actually exists to avoid runtime errors. This includes checking for the presence of required methods on arrays or objects before calling them. Common built-in methods that require callback functions include `every()`, `some()`, `forEach()`, `map()`, `filter()`, `reduce()`, `reduceRight()`, and `find()`. Always verify that these methods are available on the appropriate object type.


## Additional JavaScript Error Insights

JavaScript reference errors can be broadly categorized into four main types, according to the MDN JavaScript documentation. These errors occur when JavaScript tries to access a variable that doesn't exist, hasn't been defined, or doesn't exist in the current scope:

1. **Undeclared or Undefined Variable**: This occurs when a variable reference cannot be found or is not declared. New developers often commit these errors by forgetting to define the variable. For example:

```javascript

console.log(str); // Uncaught ReferenceError: str is not defined

```

To fix this, ensure all variables are declared before use. For instance:

```javascript

var str = "Hello World";

console.log(str); // Output: Hello World

```

2. **Reserved Identifier**: Using reserved words as variable names can also trigger reference errors. While not directly related to function calls, this issue is worth noting as it can affect variable accessibility throughout your code.

These reference errors can typically be caught at build time if your code is properly structured. Understanding the specific cause of the error helps prevent similar mistakes in the future, allowing you to spend more time on productive coding activities.


### JavaScript Syntax Errors: Additional Considerations

The language's strict mode further restricts the types of errors you can encounter. In strict mode, referencing an undeclared variable throws a `ReferenceError`. Attempting to use reserved identifiers as variable names will also trigger these errors. For example:

```javascript

function text() {

  let str = "Hello World";

  return str;

}

console.log(str); // Uncaught ReferenceError: str is not defined in strict mode

```


### Function and Object Usage

Understanding how functions and objects work in JavaScript is crucial for avoiding related errors. Consider the following examples:

- **Conflicting Property and Function Names**: In class definitions, properties and functions with the same name can cause confusion. For instance:

```javascript

class Dog {

  constructor(name) {

    this.name = name; // Property

  }

  bark() {

    return `${this.name} barks!`; // Function

  }

}

const myNewDog = new Dog("Cassidy");

myNewDog.name("Cassidy"); // TypeError: myNewDog.name is not a function

```

The solution is to use different property names to avoid this conflict.

- **Incorrect Object Usage**: The `Array.prototype.map` method is a common target for these errors. It works only with `Array` objects, as shown here:

```javascript

const numbers = [1, 2, 3];

const doubled = numbers.map(x => x * 2); // [2, 4, 6]

const obj = {}; // Not an array

obj.map(x => x * 2); // TypeError: obj.map is not a function

```

Always ensure that you are calling functions on objects that actually contain those functions.


### Common Pitfalls with jQuery and WordPress

Developers using WordPress and its jQuery implementation may encounter peculiarities. The "Uncaught TypeError: $ is not a function" error specifically occurs when executing functions incorrectly within WordPress's environment. This demonstrates how specific framework implementations can introduce their own set of unique challenges.

By understanding these broader aspects of JavaScript errors, you can develop more robust code that handles these issues effectively.

