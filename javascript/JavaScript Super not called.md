---

title: JavaScript Errors: super not called

date: 2025-05-26

---


# JavaScript Errors: super not called

JavaScript's class system enables powerful object-oriented programming through inheritance, with the `super` keyword playing a crucial role in managing base class references. This article explores the fundamental aspects of `super`, particularly its requirements and behaviors when called in class constructors. We'll examine how the `super()` call initializes the `this` object, its placement within constructor logic, and the cross-browser variations in error messaging. Additionally, we'll discuss optimization techniques for method calls and best practices for maintaining consistent inheritance behavior across different JavaScript environments.


## The 'super()' Call

The `super()` call is a fundamental aspect of JavaScript class inheritance, serving multiple important purposes. It's used to invoke the base class constructor, allowing the base class to initialize the `this` object, and can be called at various points within class constructors and method definitions.

The method must be called before accessing `this` in the derived class constructor and must be called during every execution of the constructor for a given instance, including when used in arrow functions nested within constructors. While the `super()` call itself does not require parameters, passing arguments to the base constructor is necessary if the base constructor requires them.

In cases where the derived class constructor does not return an object, calling `super()` is mandatory or the derived constructor will fail, as the base constructor cannot initialize `this` in the absence of a `super()` call. The `super()` call can occur at various points within the constructor's statement list, as the compiler automatically inserts a call before the first statement in the constructor body if `super()` is not explicitly called.

The `super()` call has different behaviors across JavaScript environments, particularly between V8-based environments like Chrome and Firefox and Safari. In V8 environments, the error message is "super() is only valid in derived class constructors," while in Firefox it appears as "SyntaxError: super() is only valid in derived class constructors" and in Safari as "SyntaxError: super is not valid in this context."

The call is a core part of JavaScript's prototypal inheritance model and affects performance when accessing inherited methods. The call tells the JavaScript engine to explicitly look for a method implementation in the parent class, improving performance by reducing the search depth through the inheritance chain. However, whether to use `super` depends on the specific implementation needs, as documented in the Mozilla Developer Network (MDN) Web Docs.


## Class Constructors and super

The super() call in JavaScript class constructors serves a crucial role in initializing the this object properly. It must be called before accessing this in the derived class constructor and can be invoked in various contexts:

The super() call can be defined in an arrow function nested within the constructor, making it a flexible tool for class inheritance (Mozilla Developer Network, July 2024).

A key requirement is that the base constructor must be called before accessing this in the derived constructor. If super() is not called, the parent constructor cannot initialize this, resulting in an invalid constructed object and causing a ReferenceError (MDN Web Docs).

When super() is not explicitly called, the compiler automatically inserts a call before the first statement in the constructor body. This ensures that the base constructor is always invoked, even when the programmer forgets to include the super() call manually (MDN Web Docs).

The call must occur before any throw or return statement, as these would prevent the remaining constructor code from executing (MDN Web Docs).

In the case where a derived class constructor returns an object rather than using this, calling super() is not strictly necessary, though it is still recommended best practice (MDN Web Docs). This allows for flexibility in constructor implementation while maintaining proper class initialization semantics.


## Super Error Messages and Cross-Browser Differences

The `super()` call has different behaviors across JavaScript environments, particularly between V8-based environments like Chrome and Firefox and Safari. In V8 environments, the error message is "super() is only valid in derived class constructors," while in Firefox it appears as "SyntaxError: super() is only valid in derived class constructors" and in Safari as "SyntaxError: super is not valid in this context."

The `super()` call is used to invoke the base constructor of a derived class, allowing the base class to initialize properties and call base class methods. The `super()` call has several important requirements and behaviors:

1. Where and when to call super: The call must be made before accessing `this` in the derived constructor and before any throw or return statement. If the derived constructor returns an object rather than using `this`, calling super() is not strictly necessary but is still recommended best practice (MDN Web Docs).

2. How often to call super: The `super()` method can only be called once for each `new` call to a derived class constructor (Mozilla Developer Network, July 2024).

3. Error handling: If super() is not called for a given derived class constructor and the derived constructor tries to access the value of `this`, or if the constructor has already returned and the return value is not an object, the error "must call super constructor before using 'this' in derived class constructor" will be thrown. This error applies specifically to Firefox and Safari browsers (MDN Web Docs).

Cross-browser differences in error messages reflect variations in how JavaScript engines implement class inheritance:

- V8-based engines display "super() is only valid in derived class constructors"

- Firefox shows "SyntaxError: super() is only valid in derived class constructors"

- Safari reports "SyntaxError: super is not valid in this context"

The Mozilla Developer Network (MDN) Web Docs state that super can be called in the constructor's statement list, and the compiler automatically inserts a call before the first statement if `super()` is not explicitly called. This automatic behavior ensures that the base constructor is always invoked, even when the programmer forgets to include the super() call manually (MDN Web Docs).

The Salsify approach, which defines a dynamic `super` property on base prototypes, offers several advantages: compatibility with IE 8 and older browsers, no performance overhead, and correct debugger frame behavior (Mozilla Developer Network, July 2024). This implementation demonstrates how the `super` keyword works across different JavaScript environments while maintaining compatibility and performance.


## super Keyword Fundamentals

The `super` keyword in JavaScript serves two main purposes: function call (`super(...args)`) and property lookup (`super.prop` and `super[expr]`). It can be accessed within methods of both classes and object literals.


### Function Call Behavior

The super function call invokes the method on the object literal's prototype chain. Key behaviors include:

- Requires at most one call per derived class constructor

- Must precede `this` access and constructor returns

- Works in methods defined using arrow functions, though `this` context is fixed

- Acts as a variable in method scope, creating closures

- Sets properties through `super` on `this`, not prototype objects


### Property Lookup Behavior

The super property lookup mechanism functions as follows:

- Resolves to the prototype object of the object literal or class

- Functions like Reflect.get(Object.getPrototypeOf(objectLiteral), "x", this)

- Not affected by unbinding and re-binding operations

- Example: `Base` class has `baseGetX()`, `Extended` class overrides `getX()` to call `baseGetX()`


### Method Implementation Variations

Different approaches exist for managing super method calls:

- Prototype.js uses a `$super` parameter, requiring framework detection

- CoffeeScript and TypeScript provide built-in `super` syntax

- Salsify defines a dynamic `super` property on base prototypes, supporting IE 8

- ES6 `Function.caller` approach maintains performance while providing compatibility


### Performance Considerations

Using `super` method calls can improve performance by directly accessing superclass methods through the prototype chain. This direct invocation reduces the search depth through the inheritance hierarchy, while whether to use `super` depends on implementation requirements:

- When overriding methods, the overridden method is called, not the lowest method in the inheritance tree

- Can enhance performance by several milliseconds, particularly for frequently called methods

- Whether to use `super` depends on specific use cases:

  - Perform additional actions after parent implementation: call super

  - Implement completely different logic: do not call super


### Compatibility and Best Practices

The `super` keyword has been available since March 2016 across many devices and browser versions. Best practices include:

- Always call super before accessing this in derived constructors

- Use super for consistent inheritance behavior

- Avoid redundant calls where possible

- Utilize available tools like IntelliJ IDEA's code inspection features

- Consider framework-specific implementations for consistent behavior

