---

title: JavaScript ES6 Classes: Private Properties

date: 2025-05-26

---


# JavaScript ES6 Classes: Private Properties

Private properties and methods represent a significant advancement in JavaScript's object-oriented capabilities, introduced through the `#` prefix syntax in ES6 classes. These language-level privacy features build upon earlier workarounds while maintaining JavaScript's dynamic nature. Understanding their implementation and scope restrictions is crucial for developers navigating the evolving JavaScript landscape, particularly when targeting modern browsers that support ES2019 class field declarations and beyond.


## Private Properties Overview

JavaScript ES6 classes introduce a formal mechanism for private properties through the `#` prefix syntax. While this syntax enforces privacy at the language level, access control is primarily achieved through scope and reflection limitations rather than traditional access modifiers.

The private scope operates within the class body, preventing direct access from outside code. However, the language restricts access in specific ways:

- Private properties cannot be accessed before calling `super()`

- Derived classes can inherit methods but not directly access private fields

- Instances can access private properties through the class name, but attempting to access them directly throws a `TypeError`

Implementations prior to ES2022 used various workarounds:

- Scoped variables within constructors

- WeakMap associations for instance-level privacy

- JSDoc's `@private` tag for IDE visibility control

Current best practices recommend:

- Using `#` prefix for private fields and methods

- Declaring getters and setters for controlled access

- Implementing methods outside constructor scope for performance

The language continues to evolve, with ES2019 adding official support through class field declarations and ES2022 expanding to private getters and setters. However, developers must remain aware of browser compatibility, with older engines requiring polyfills for full support.


## Implementation Methods

The introduction of private properties in JavaScript ES6 classes represents a significant step towards more robust object-oriented programming practices. However, their implementation relies heavily on JavaScript's lexical scoping rules and language limitations rather than traditional access control mechanisms.

While private properties are accessible through reflection in many languages, JavaScript enforces privacy primarily through scope and language restrictions. The most effective techniques maintain privacy through constructor-based encapsulation while providing controlled access via getter and setter methods. As demonstrated by modern frameworks and libraries, these properties can significantly enhance code organization and functionality.

Key implementation approaches include:

1. Constructor-based encapsulation: Using `let` and `const` declarations within constructors to create private fields, as demonstrated by the Car class example. This approach ensures that each instance maintains its own private state.

```javascript

class Car {

  constructor(milesDriven) {

    this._milesDriven = milesDriven;

  }

  drive(distance) {

    this._milesDriven += distance;

  }

  get milesDriven() {

    return this._milesDriven;

  }

}

```

2. WeakMap association: For improved performance, developers can use WeakMaps to associate private data with class instances, ensuring each instance maintains its own isolated storage.

```javascript

class Something {

  constructor(message) {

    const privateMap = new WeakMap();

    privateMap.set(this, { message });

  }

  say() {

    console.log(privateMap.get(this));

  }

}

```

3. Private field syntax: ES2022 introduced official support for private class fields using the # prefix. This feature enables concise and standardized implementation while maintaining robust privacy controls.

```javascript

class Something {

  #property;

  constructor(message) {

    this.#property = message;

  }

  #privateMethod() {

    return 'hello world';

  }

  getPrivateMessage() {

    return this.#property;

  }

}

```

These implementation patterns demonstrate the evolving landscape of JavaScript's private property functionality, from workarounds in early ES6 implementations to the standardized approach introduced in ES2022. As browser support continues to expand, developers can increasingly rely on these language features to implement secure and maintainable object-oriented patterns in their JavaScript applications.


## Private Field Syntax

The `#` prefix introduced in ES2022 Class Fields proposal enables concise and standardized implementation of private fields in JavaScript classes. Unlike traditional property names, private fields are integral to the class structure and cannot have name clashes with public properties. These fields must be declared in the class body and cannot be created on the fly, allowing the language to perform static analysis for enhanced security.

In terms of functionality, private fields behave equivalently to normal properties. Within the class, they can be accessed using the field name through dot notation. Attempting to access them outside the class results in a syntax error, though the Chrome console allows such access as a DevTools-only relaxation of this restriction. This enforced privacy ensures that private fields remain protected from external interference.


### Declaration and Initialization

Private fields require the `[[DefineOwnProperty]]` semantic, preventing base class setters from invoking derived class fields. This differs from using `this.field = ...` in constructors, where the language enforces strict privacy controls. Fields must be initialized before use, with access to uninitialized fields throwing a `TypeError`. Developers can declare empty class fields as placeholders for static analysis and documentation purposes.


### Class Access Restrictions

The language enforces hard privacy on private fields, ensuring that class methods cannot access private fields of instances unless they belong to the same class or subclass. Nonexistent private properties throw errors rather than returning `undefined`, providing strong type safety guarantees. The `in` operator can be used to check for private property existence without employing `try`/`catch` blocks, allowing robust property checking in controlled contexts.


### Instance Differences

When evaluating class declarations, instance fields are initialized before the constructor runs, while static methods and accessors are installed beforehand. This initialization order ensures predictable behavior for field dependencies. Each instance maintains its own isolated storage through either scoped variable declarations or WeakMap associations, as demonstrated by modern implementation patterns. As the language continues to evolve, developers can increasingly rely on these features to implement secure and maintainable object-oriented patterns in their JavaScript applications.


## Access Control

JavaScript's access control mechanisms for private properties and methods enforce privacy primarily through lexical scoping and language-level restrictions, rather than traditional access modifiers found in languages like Java or C#. While modern JavaScript engines provide strong privacy guarantees, the implementation details differ significantly from classical object-oriented programming paradigms.

Private properties and methods fall under the scope of the class itself, restricted to the class body and its immediate subclasses. Unlike static or protected members, private fields are "hard private" and cannot be accessed from outside the class, including derived classes. This encapsulation ensures that private members remain protected from external interference, though JavaScript's dynamic nature allows some flexibility through reflection capabilities in development tools.

The official class field syntax requires properties to be declared within the class body using the `#` prefix. These properties cannot be legally referenced outside the defining class, with access restricted to the `this` context within class methods. While modern JavaScript engines enforce these privacy rules through language-level checks, older engines may require polyfills to support private fields and methods.

The implementation relies heavily on static scoping rules, preventing direct access to uninitialized fields and ensuring that private properties cannot be modified before their defining constructor has finished execution. Similarly, derived classes cannot access private fields of superclass instances unless they inherit the same class or subclass directly. Instance-level privacy can be maintained through scoped variables within constructors or WeakMap associations, though these patterns are subject to the same fundamental scoping rules enforced by the language.

Within the class itself, private properties and methods can be accessed through the class name or the `this` context. For example, a class might declare a private field using `#property`, which would be accessible only through `this.#property` within the class body. This pattern allows for robust property access while maintaining strict encapsulation rules enforced by the language itself.


## Special Cases and Considerations

Private properties and methods in JavaScript ES6 classes operate under strict scoping rules enforced by the language itself. These rules ensure that private members remain encapsulated, though they differ significantly from classical object-oriented programming paradigms.


### Inheritance and Scope

Private properties and methods are not inherited by subclasses. The language enforces this rule through static scoping, preventing access to private members of base classes from derived classes. When accessing private properties, developers must use the class name directly, as shown in the following example:

```javascript

class BaseClass {

  #privateField = "I'm private";

  getPrivateField() {

    return this.#privateField;

  }

}

class DerivedClass extends BaseClass {

  getPrivateField() {

    return this.getPrivateField(); // Accessing through public method

  }

}

const instance = new DerivedClass();

console.log(instance.getPrivateField()); // => "I'm private"

console.log(instance.#privateField); // TypeError: Cannot access member of #privateField on an instance of BaseClass

```


### Static Fields and Methods

Static fields and methods represent a special case in JavaScript class implementation. These properties are associated with the class itself rather than instances, allowing for shared configuration information and utility methods. Unlike private fields, static members cannot be accessed through instance references, as demonstrated in this example:

```javascript

class MyClass {

  static myStaticField = true;

  static myStaticMethod() {

    console.log("A static method.");

  }

}

const myInstance = new MyClass();

console.log(myInstance.myStaticField); // undefined

myInstance.myStaticMethod(); // Uncaught TypeError: myStaticMethod is not a function

```

Developers should use static members for creating utility methods that operate on class instances or perform shared configuration. The language's restriction on static member access ensures that these properties remain encapsulated within the class structure.


### Method Implementation Details

Class methods can include both private instance methods and private static methods. These methods follow the same syntax requirements as public getters and setters, including support for generator, async, and async generator functions. For private static methods, developers must access them through the class name rather than instance references:

```javascript

class Something {

  static #privateStaticMethod() {

    return 42;

  }

  static getPrivateStaticField() {

    return this.#privateStaticMethod();

  }

}

console.log(Something.getPrivateStaticField()); // => 42

console.log(new Something().getPrivateStaticField()); // Uncaught TypeError: Something.getPrivateStaticField is not a function

```

The `#` prefix allows developers to define private getters and setters directly in class fields, providing concise syntax for controlled access. For example:

```javascript

class Something {

  #decoratedMessage = "hello world";

  get #decoratedMessage() {

    return this.#decoratedMessage;

  }

  set #decoratedMessage(msg) {

    this.#decoratedMessage = msg;

  }

}

const instance = new Something();

console.log(instance.#decoratedMessage); // => undefined

instance.#decoratedMessage = "hello universe";

console.log(instance.#decoratedMessage); // => "hello universe"

```


### Performance Considerations

While modern JavaScript engines enforce strong privacy controls, developers must consider the impact of implementation patterns on performance and memory usage. The official class field syntax requires careful consideration of instance field initialization order and method declaration scope to ensure efficient execution.

The text notes that private methods are not accessible on the `.prototype` property of their class, addressing concerns about multiple inheritance and method overriding. This design choice helps maintain encapsulation while allowing for flexible class hierarchies.

