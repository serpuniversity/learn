---

title: JavaScript this Keyword

date: 2025-05-27

---


# JavaScript this Keyword

JavaScript's "this" keyword can be both powerful and frustratingly unpredictable, depending on how you use it. Whether you're working with objects, constructors, or event handlers, grasping "this" is crucial for writing clean, modular code. This guide walks you through the ins and outs of "this" in different contexts, from method invocation to constructors and event handling, helping you avoid common pitfalls in your JavaScript development journey.


## this in Method Context

In the context of object methods, this keyword refers to the object itself. This allows the method to access and manipulate the object's properties and other methods. For example, consider an object `person` with a method `fullName`:

```javascript

const person = {

  name: 'John Doe',

  fullName: function() {

    return this.name;

  }

}

console.log(person.fullName()); // Outputs: John Doe

```

The value of `this` inside the `fullName` method is the `person` object, enabling direct access to its properties.

When a function is defined on an object at creation, this keyword changes based on how the function is called:

```javascript

const obj = {

  property: 42,

  method: function() {

    return this.property;

  }

}

console.log(obj.method()); // Outputs: 42

const standalone = obj.method;

console.log(standalone()); // Outputs: undefined

```

In the second case, `this` inside `method` no longer refers to `obj` because the function was called standalone, not as an object property.

Explicit binding can be achieved using `call()`, `apply()`, or `bind()` methods. These methods allow specifying the value of `this`:

```javascript

function greet(greeting) {

  console.log(this.name + ', ' + greeting + '!');

}

const member = { name: 'John' };

greet.call(member, 'Hello'); // Outputs: John, Hello!

```

In this example, `call()` is used to explicitly set `this` to the `member` object.

Understanding the value of `this` is crucial for effective JavaScript coding, especially when working with arrow functions, class constructors, and class methods. As noted in the documentation, the use of `this` can vary significantly based on function context and execution environment.


## this in Global and Strict Mode

In strict mode, the value of `this` becomes undefined when called as a normal function. This affects how developers approach function creation and invocation. For instance, consider a basic function used in the global scope:

```javascript

function sayHello() {

  console.log("Hello " + this.name);

}

// In non-strict mode

sayHello(); // Outputs: Hello undefined

// In strict mode

function sayHello() {

  'use strict';

  console.log("Hello " + this.name);

}

sayHello(); // Outputs: Uncaught ReferenceError: this is undefined

```

The behavior of `this` in nested functions differs from non-strict to strict mode. In the first example, the inner function correctly references the global object's `window` property. However, in strict mode, the inner function would also encounter an undefined `this`:

```javascript

function outer() {

  console.log(this === window); // true in non-strict, false in strict

  function inner() {

    console.log(this === window); // true in non-strict, false in strict

  }

  inner();

}

outer(); // In strict mode

```

Understanding these nuances helps developers avoid common pitfalls when writing modular JavaScript code. The use of `this` in event handlers and DOM interactions requires special attention, as the default behavior might not match expectations in strict mode.


## this through Function Calls

The use of these methods allows developers to explicitly set the value of this, providing flexibility in function execution and argument passing. Call() and apply() invoke the function immediately with specific arguments, while bind() creates a new function with a fixed this value for later use. These methods are particularly useful for event handling, where they ensure correct context and arguments for handlers.

For example, the formatted() method in the game object demonstrates how apply() changes the this context from the window object to the game object:


## this in Constructors

When an object is created using the `new` keyword, the value of `this` is set to the newly created object. This allows constructor functions to initialize and configure new object instances. Consider the following example:

```javascript

function Product(name, price) {

  this.name = name;

  this.price = price;

}

const myProduct = new Product("Coffee Mug", 15.99);

console.log(myProduct.name); // Coffee Mug

console.log(myProduct.price); // 15.99

```

In this code, `this` inside the `Product` constructor function refers to the `myProduct` object. The function properties `name` and `price` are assigned to the new object's attributes.

The `apply()` method demonstrates this behavior in action. When called on the `info` object inside the `game` object, `apply()` changes the `this` context from the global object to the `newGame` object:

```javascript

const newGame = {

  id: "uniqueId",

  info: {

    title: "Game Title",

    extraName: "Additional Name"

  }

};

function formatted(str) {

  return str.toUpperCase();

}

const info = newGame.info;

formatted.apply(info, ['Welcome']); // Output: [ 'Welcome' ]

```

In this example, `apply()` passes the array `['Welcome']` as arguments to the `formatted` function, while setting `this` to the `info` object. This correctly formats the "Welcome" string using the `info` object's methods.

Understanding these principles is crucial for effective JavaScript object-oriented programming. The use of `this` in constructor functions enables developers to create flexible, reusable object blueprints that can be instantiated multiple times with different configurations.


## Understanding this through Examples

The JavaScript "this" keyword presents several gotchas that developers must navigate. Its value depends on how a function is called rather than just how it's defined, leading to behavior that can be counterintuitive until fully understood.


### Default Behavior and Global Context

In simple function invocations in non-strict mode, "this" refers to the global object (usually "window" in browsers). This can lead to unexpected results when properties are added to "this":

```javascript

console.log(this === global); // true in Node.js

this.color = 'Red';

console.log(global.color); // 'Red'

```


### Method vs Constructor Context

Common mistakes occur when "this" is used inconsistently between methods and constructors. For example, assuming "this" inside a method refers to the constructor's context:

```javascript

function User(name) {

  this.name = name;

  this.getInfo = function() {

    return this.name;

  }

}

const user = new User('Alice');

console.log(user.getInfo() === user.name); // true

```


### Event Handling and Function Borrowing

Event handlers can provide misleading behavior, as "this" points to the element that triggered the event, not the object hosting the handler:

```javascript

document.getElementById('button').addEventListener('click', function() {

  console.log(this === document.getElementById('button')); // true

});

```


### Gotchas with Binding

Even when using the "call()", "apply()", or "bind()" methods, "this" behavior can still be surprising. For instance, forgetting to invoke the bound function immediately or using it incorrectly can lead to wrong results:

```javascript

function show() {

  console.log(this === window); // true

}

show.call({}); // Still logs true

```


### Best Practices

To avoid these pitfalls, developers should explicitly set "this" using "bind()" when creating object methods, and use arrow functions where possible to inherit the correct "this" context. Understanding the four types of bindings (default, implicit, explicit, and "new") is essential for mastering "this" in complex JavaScript applications.

