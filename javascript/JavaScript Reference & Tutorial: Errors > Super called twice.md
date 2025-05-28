---

title: Understanding 'Super Called Twice' in JavaScript

date: 2025-05-26

---


# Understanding 'Super Called Twice' in JavaScript

In JavaScript object-oriented programming, the 'super' keyword plays a crucial role in method and property inheritance. However, the proper use of 'super' is governed by strict rules to prevent errors and maintain code clarity. This article explores common issues related to 'super', particularly the "super constructor called twice" error, and provides best practices for using 'super' in class inheritance. We'll examine typical error scenarios, such as improper event listener implementation, and discuss how to avoid common pitfalls when working with JavaScript class inheritance.


## The 'Super Called Twice' Error

The 'super' keyword in JavaScript serves as a bridge between an object's prototype and its inherited properties and methods. When an object requires access to its parent's properties or methods, the 'super' keyword allows it to do so in a way that maintains the object's prototype chain. This mechanism becomes particularly important when dealing with constructor functions and class inheritance, where instances need to call methods from their parent classes while maintaining proper scope and context.

The use of 'super' helps maintain code clarity and prevent undefined behavior by enforcing strict rules about method invocation. Modern JavaScript engines enforce these rules to prevent deeper recursion and improper constructor invocation, ensuring that each derived class constructor calls 'super()' exactly once before accessing any 'this' properties or returning the constructor.

The engine's enforcement of these rules is crucial for managing object creation and inheritance. By preventing multiple calls to 'super()', the engine ensures that objects are created with a clear and consistent prototype chain. This mechanism is essential for maintaining the integrity of object hierarchies and preventing potential errors that could arise from improper constructor calls.


## Error Handling and Reporting

The 'super() called twice' error occurs when JavaScript engines enforce strict rules around 'super' calls, preventing deeper recursion or improper constructor invocation. This error manifests differently across engines: V8-based environments report it as a ReferenceError, while Firefox specifically identifies it as a super constructor call error.

The error type is consistently a ReferenceError, indicating that 'super()' can only be called once per constructor invocation. This rule prevents multiple calls to 'super()', which would result in undefined behavior by invoking the parent constructor multiple times. Modern JavaScript engines enforce these rules to maintain code clarity and prevent logical errors that could arise from improper constructor calls.

This limitation ensures that objects are created with a clear and consistent prototype chain, preventing potential issues that could arise from improper constructor invocations. Understanding these constraints helps developers write more predictable and maintainable JavaScript code that leverages class inheritance effectively.


## Common Error Scenarios

The 'super' keyword in JavaScript is designed to call the constructor of the parent class and access its properties and methods. This mechanism is essential for working with inheritance in object-oriented programming. In the context of the example provided, the 'super' keyword is used in a class hierarchy where a Manager class extends an Employee class. When a Manager object is created, the 'super' keyword allows the child class to access and invoke functions on its parent class.

This functionality becomes particularly important when dealing with constructors in derived classes. The JavaScript language enforces strict rules around 'super' calls to prevent deeper recursion and maintain code clarity. Specifically, the 'super()' call must be called exactly once before accessing any 'this' properties or returning from the derived constructor.

A common scenario where developers encounter 'super called twice' errors involves event listeners in the context of the window and document objects. When working with event listeners, it's crucial to use proper function binding to maintain the correct context. For example, consider the following code snippet:

```javascript

function showAlert(message) {

  alert(message);

}

window.addEventListener('click', showAlert);

```

In this case, the showAlert function is defined in the window context, but it's called in the event listener context of the document. To prevent any issues, you should bind the function to ensure it maintains the correct 'this' context:

```javascript

window.addEventListener('click', showAlert.bind(window));

```

This binding ensures that the showAlert function maintains its intended behavior when called from the event listener context. The error often occurs when the function is passed as an anonymous function, such as:

```javascript

window.addEventListener('click', function() {

  showAlert('Click detected!');

});

```

In this case, the function is executed in the context of the document, while the showAlert function is defined in the window context. To resolve this, you should explicitly bind the function to the window context:

```javascript

window.addEventListener('click', showAlert.bind(window));

```

By using proper function binding techniques, developers can prevent 'super called twice' errors and ensure consistent behavior across different execution contexts.


## Best Practices for Inheritance

To prevent 'super constructor called twice' errors, derived class constructors must call super() exactly once before accessing any 'this' properties or returning from the constructor. This ensures that the parent constructor is called only once, maintaining proper object creation and inheritance.

The 'super()' call must be placed outside of any control flow structure to prevent multiple calls. In cases where multiple conditions may lead to super() calls, consider using an arrow function nested within the constructor to "save" the super() call. When calling this arrow function, the same rule applies: it can only be called once.

Common invalid cases include:

- Calling super() multiple times in the same constructor

- Calling super() in non-constructor contexts (e.g., class methods or functions)

- Not calling super() before accessing this properties or returning non-object values

Valid cases include:

- Calling super() before any constructor logic

- Using super() in an arrow function nested within the constructor

- Returning an object from the derived class constructor, allowing this to be used as the constructed object instead

Understanding these rules helps prevent errors like "must call super constructor before using 'this' in derived class constructor" and "super() called twice in derived class constructor," ensuring proper object creation and inheritance in JavaScript class hierarchies.


## Compiler and Engine Support

The JavaScript engine's strict rules around 'super' calls are implemented to prevent deeper recursion and maintain code clarity. The 'super()' call must be placed outside of any control flow structure, and the engine enforces this rule through compile-time and runtime checks.

When a derived class constructor needs to call super(), it must do so before accessing any 'this' properties or returning from the constructor. This rule applies across all modern JavaScript engines, including V8-based environments, Firefox, and Safari (although reporting details vary):

- V8-based engines: ReferenceError - super constructor may only be called once

- Firefox: ReferenceError - super() called twice in derived class constructor

- Safari: ReferenceError - super() can't be called more than once in a constructor

The language has evolved with multiple approaches to simplify invoking overridden methods. For example, some frameworks implement special `$super` parameters or use object's `constructor` attribute, while others employ verbose helper functions that maintain `_super` attribute values (2008 John Resig solution). However, these approaches introduce their own complexities and are generally less efficient than built-in language support.

The engine's enforcement of these rules prevents improper constructor invocations that could lead to undefined behavior. For example, it prevents scenarios where a derived class might unintentionally call the parent constructor multiple times, resulting in incorrect initialization state:

```javascript

class Base {

  constructor() {

    this.x = 1;

  }

}

class Derived extends Base {

  constructor() {

    console.log(this.x); // The Base constructor is not called yet, so this.x is undefined

  }

}

```

Modern engines enforce these rules regardless of framework usage, making proper 'super' call handling crucial for all JavaScript development, especially in frameworks like Backbone that rely heavily on prototypal inheritance mechanisms.

