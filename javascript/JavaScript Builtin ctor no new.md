---

title: JavaScript Error: Builtin ctor no new

date: 2025-05-26

---


# JavaScript Error: Builtin ctor no new

JavaScript constructors play a crucial role in object creation and initialization, following specific conventions and behaviors. This article explores the proper usage of the `new` keyword with constructors, explaining how it enables correct object instantiation and property initialization. We'll examine the underlying mechanics of constructor functions, demonstrate best practices for creating and using objects, and address common errors that arise when `new` is overlooked.


## Overview of JavaScript Constructors

Constructor functions in JavaScript serve as templates for creating objects with similar properties and behaviors. These functions, which are typically named with a capital letter, follow specific conventions and operating rules to create multiple instances of the same object type.

When a constructor function is executed with the `new` keyword, JavaScript performs several key actions:

1. It creates a new, empty object

2. It assigns this object to the `this` context within the constructor function

3. It executes the constructor function's body with the new object as `this`

4. It returns the newly created object

The primary purpose of this process is to allow developers to create multiple similar objects efficiently. For example:

```javascript

function User(name) {

  this.name = name;

  this.isAdmin = false;

}

let user = new User("Jack");

console.log(user.name); // Jack

console.log(user.isAdmin); // false

```

In this case, the `User` constructor function creates a new object with a `name` property and an `isAdmin` property set to `false`. The `new` keyword ensures that each user object is created with these properties initialized correctly.

While any function can technically be used as a constructor, following the convention of using capital letters for constructor names helps maintain consistency and readability in code. This convention is particularly important when working with built-in JavaScript constructors like `Array`, `Object`, and `Map`.

Using `new` with constructors is essential for several reasons:

- It ensures proper object instantiation

- It allows for the correct setting of `this` context within constructor functions

- It enables the use of constructor functions as prototypes for multiple object instances

Attempting to create objects without using `new` can lead to unexpected behavior and errors. For example, calling `Object()` without `new` creates a function object instead of an empty object instance:

```javascript

let obj = Object();

console.log(typeof obj); // function

```

To understand why using `new` is crucial, consider the following examples:


### Built-in Constructor Rules

JavaScript provides several built-in constructors that require proper usage with the `new` keyword. These include:

```javascript

new Object() // Creates an empty object

new Array() // Creates an empty array

new Map() // Creates an empty map

new Set() // Creates an empty set

new Date() // Creates a date object

new RegExp() // Creates a regular expression

new Function() // Creates a function object

```

Attempting to use these constructors without `new` results in specific errors or unexpected behavior:

```javascript

let map = Map(); // TypeError: calling a built-in Map constructor without new is forbidden

let date = Date(); // Returns the current date as a string

let func = Function(); // Returns a function object

```


### Common Constructor Errors

A common constructor-related error occurs when attempting to call a class constructor without the `new` keyword. This results in the "class constructors must be invoked with 'new'" error. For example:

```javascript

class Car {

  constructor(make, model, year) {

    this.make = make;

    this.model = model;

    this.year = year;

  }

}

Car(); // TypeError: Car() is not a constructor

new Car(); // Invalid, should be new Car(make, model, year)

```

This error occurs because JavaScript treats class constructors as always being constructors, preventing them from being called as regular functions. This distinction helps maintain consistency in object creation and prevents potential bugs.


### Alternative Constructor Implementation

While it's possible to create alternative constructor implementations that don't require `new`, these approaches have significant limitations and drawbacks:

```javascript

function thing() {

  if (!(this instanceof thing)) {

    return new thing(arguments, "lazy");

  }

  var args = (arguments.length > 0 && arguments[arguments.length - 1] === "lazy") ? arguments[0] : arguments;

  this.prop1 = (args.length > 0) ? args[0] : "nope";

  this.prop2 = (args.length > 1) ? args[1] : "nope";

}

```

This implementation attempts to handle both standard and "lazy" instantiation methods, but it introduces several problems:

- It's slower than using `new`

- It requires additional complexity to manage different instantiation patterns

- It may lead to unexpected behavior, especially when `new` is already being used consistently

Best practices for constructor usage include:

- Always use `new` with constructor functions

- Follow the convention of naming constructor functions with capital letters

- Avoid alternative implementations unless absolutely necessary

- Understand the implications of using `new` vs. not using it


## Built-in Constructor Rules

JavaScript's built-in constructors behave distinctly when called with or without the `new` operator. According to the MDN Web Docs, constructor functions must be literal names and cannot use async methods, generators, accessors, or class fields (constructor properties).

When a constructor is called with `new`, JavaScript creates a new empty object, assigns it to the `this` context, executes the constructor's body, and returns the created object. This process allows constructors to properly initialize new object instances. For example:

```javascript

function User(name) {

  this.name = name;

  this.isAdmin = false;

}

let user = new User("Jack");

console.log(user.name); // Jack

console.log(user.isAdmin); // false

```

In contrast, calling a constructor without `new` behaves differently:

- `new Object()` creates an empty object

- `new Array()` creates an empty array

- `new Map()` creates an empty map

- `new Set()` creates an empty set

- `new Date()` creates a date object

- `new RegExp()` creates a regular expression

- `new Function()` creates a function object

However, attempting to call these constructors without `new` results in specific errors or unexpected behavior:

```javascript

let map = Map(); // TypeError: calling a built-in Map constructor without new is forbidden

let date = Date(); // Returns the current date as a string

let func = Function(); // Returns a function object

```

The specification requires that all modern constructors be called with `new`, including these built-in constructor functions. Other constructors and primitive wrappers can be called with or without `new`, but return different types in each case. This behavior is documented on every constructor page.

For environments without native `Object.create` support, the ES5-shim library provides a compatible implementation. The text also presents alternative approaches to constructor implementation that avoid requiring `new`, though these are generally slower and less efficient.

The primary requirement for using built-in constructors is to always include the `new` keyword when creating objects. This ensures proper object instantiation, correct `this` context setting, and the ability to use constructor functions as prototypes for multiple object instances.


## Common Constructor Errors

The "class constructors must be invoked with 'new'" error occurs when a class constructor is called without the `new` prefix. This exception highlights a fundamental difference between function calls and constructor calls in JavaScript. As described by the MDN Web Docs, all class constructors must be invoked with `new`, ensuring that the constructor's object-creation process takes place.

To demonstrate the error, consider the following example:

```javascript

class Foo {

  constructor() {

    this.x = 42;

  }

}

// Correct

const instance = new Foo();

console.log(instance.x); // 42

// Incorrect

Foo(); // TypeError: class constructors must be invoked with 'new'

```

In the first case, `new Foo()` creates a new instance and assigns its properties correctly. However, attempting to call `Foo()` without `new` results in the "TypeError: class constructors must be invoked with 'new'" error, as shown in the second case.

This error also applies to JavaScript's built-in constructors. For example:

```javascript

const map = new Map(); // Correct

console.log(map.size); // 0

const malformedMap = Map(); // TypeError: calling a built-in Map constructor without new is forbidden

```

While `new Map()` creates an empty map as intended, the incorrect `Map()` call produces a TypeError, demonstrating the strict requirement for using `new` with these constructors.

The `new` operator plays a crucial role in constructor functionality by creating a new object and assigning it to the `this` context within the constructor function. Attempting to bypass this mechanism can lead to unexpected behavior or specific error messages. For example:

```javascript

function User(name) {

  this.name = name;

  this.isAdmin = false;

}

// Using 'new'

const user = new User("John");

console.log(user.name); // John

console.log(user.isAdmin); // false

// Attempting to construct without 'new'

User("Jane"); // No output, user object not created

```

In the first case, `new User("John")` correctly creates a new user object with the specified properties. However, simply calling `User("Jane")` without `new` does not create a new object, demonstrating the importance of using the correct syntax for constructor calls.


## Alternative Constructor Implementation

While it's technically possible to create alternative constructor implementations that avoid requiring the `new` keyword, these approaches come with significant limitations and drawbacks. As noted by some developers, creating "true constructors" that can handle variable argument lists without `new` requires additional complexity and slower performance compared to conventional `new`-based constructors.

One common approach involves checking if `this` is an instance of the constructor using the following pattern:

```javascript

function Ctor() {

  if (!(this instanceof Ctor)) {

    return new Ctor();

  }

  // regular construction code

}

```

This mechanism ensures consistent constructor behavior whether `new` is used or not. However, it's important to note that using this approach can introduce subtle bugs. For example, consider the following scenario:

```javascript

var x = new Ctor();

// Later...

var y = Ctor();

```

In this case, the first `new` creates a new instance, while the second `Ctor()` call creates a constructor function. This difference in behavior can lead to unexpected results.

The text also presents a more complex implementation that demonstrates handling arguments without using `new`:

```javascript

function thing() {

  if (!(this instanceof thing)) {

    return new thing(arguments, "lazy");

  }

  var args = (arguments.length > 0 && arguments[arguments.length - 1] === "lazy") ? arguments[0] : arguments;

  this.prop1 = (args.length > 0) ? args[0] : "nope";

  this.prop2 = (args.length > 1) ? args[1] : "nope";

}

```

This implementation allows for both `new` and "lazy" instantiation methods. However, as noted in the original text, this approach is slower than using `new`. Additionally, while this implementation helps maintain consistency, it requires careful handling of undefined properties to avoid introducing errors.

The ECMAScript specification defines specific behaviors for built-in constructors when called as plain functions. While most built-in constructors work as expected when called as functions, their behavior differs from when used as constructors with the `new` operator. For example, calling `String`, `Date`, or `Number` as functions converts values to native strings, numbers, and objects respectively. The `Date` constructor behaves specially as there is no other reasonable behavior.

It's worth noting that using the `new` operator is generally faster and more efficient than alternative approaches. While some developers prefer to throw errors when constructors are called without `new`, this approach can complicate debugging efforts, especially when examining stack traces to identify and fix issues.


## Best Practices and Conclusion

As noted in the ECMAScript specification, constructors must adhere to strict naming conventions and functionality requirements. According to the official documentation, constructor functions must be literal names and cannot employ async methods, generators, accessors, or class fields. This strict implementation prevents potential misuse of constructor syntax and ensures consistent behavior across different JavaScript implementations.

To maintain proper object instantiation while avoiding the `new` keyword, developers might consider the alternative implementation discussed in the "Avoiding new operator in JavaScript" article. The third solution presented there allows for constructors with variable argument lists, using `Object.create(Make.prototype)` to create instances and applying the constructor's `apply` method to the created object with provided arguments. However, the text emphasizes that while this approach works, some developers prefer to enforce strict `new` usage by throwing errors when constructors are called without it.

The developer preferences vary between forcing new usage and allowing alternatives, as demonstrated by the comments from @Raynos suggesting error-throwing practices. However, the text advises caution with this approach, noting that it can complicate debugging efforts, particularly when examining stack traces to identify and address issues. The ECMAScript specification consistently requires using `new` with constructors to ensure proper object creation and maintain expected behavior.

