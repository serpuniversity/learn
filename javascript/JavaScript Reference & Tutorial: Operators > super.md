---

title: Understanding the 'super' Keyword in JavaScript

date: 2025-05-27

---


# Understanding the 'super' Keyword in JavaScript

In object-oriented programming, managing relationships between parent and child classes requires tools that enable code reuse, method overriding, and property inheritance. JavaScript's `super` keyword provides a powerful mechanism for achieving these goals, bridging the gap between parent and child classes in a flexible and intuitive manner. This article explores the various uses of `super`, from constructor invocation to method chaining, and discusses best practices for its implementation across different JavaScript environments and versions. Through detailed examples and analysis of ES6's class system, we'll uncover how `super` builds on earlier JavaScript patterns while addressing their limitations, ultimately enabling developers to create more robust and maintainable object-oriented programs.


## Introduction to super

The 'super' keyword in JavaScript serves as a bridge between parent and child classes in object-oriented programming, allowing subclasses to extend and build upon their superclass functionality. At its core, 'super' enables several key capabilities:

1. **Parent Constructor Invocation**: Perhaps the most fundamental use of 'super' in classes is to call the parent constructor. This is demonstrated in the basic inheritance example provided in the documentation, where class 'B' has a constructor that sets 'this.name', and class 'A' extends 'B' while also initializing 'this.age'. The 'A' constructor includes 'super(name)', which ensures that the 'name' property is correctly set when creating an instance of 'A'.

2. **Method Access**: In addition to invoking constructors, 'super' allows access to parent class methods. For example, the 'A' class from our earlier example includes a 'printName' method that calls 'super.printn()', effectively chaining to the 'printn' method of the 'B' class. This exemplifies method overriding while maintaining the parent's functionality.

3. **Property Access**: While primarily designed for methods, 'super' can also access parent class properties, as demonstrated in the class inheritance example where a private 'name' property in the 'Artist' class is accessed through a getter method in the 'Musician' class. However, it's important to note that private fields (marked with a '#' prefix) are not directly accessible via 'super'.

4. **Constructor Functionality**: When a subclass constructor needs to execute code before or after calling the superclass constructor, 'super' provides the necessary mechanism. The documentation highlights that while classes offer syntactic sugar for prototypical inheritance through constructor functions, this approach still requires careful management of constructor calls.


### Best Practices and Implementation Considerations

To effectively use 'super', developers should follow these guidelines:

1. **Constructor Order**: Always call 'super()' before using 'this' in the constructor, and before the constructor returns. This ensures that the parent class is properly initialized before the subclass can proceed.

   

2. **Method Chaining**: When overriding methods that call 'super', ensure you handle arguments correctly. The documentation recommends using the spread operator '...' to pass all arguments through to the parent method, maintaining flexibility and compatibility with changes in argument structure.

3. **Prototype Considerations**: Although 'super' appears to operate on the class or object literal it's declared in, its reference is determined by the prototype chain. This means that when working with inherited classes, 'super' will always refer to the correct parent prototype, even when intermediate prototypes are modified.

4. **Error Handling**: If 'super' is called outside of a method implementation, it will result in a SyntaxError. Developers should ensure that 'super' is used consistently within method bodies and not treated as a standalone variable.

By understanding these principles and best practices, JavaScript developers can leverage the 'super' keyword to create robust, maintainable object-oriented programs.


## Using super in class constructors

In JavaScript class inheritance, the `super` keyword serves as a bridge between parent and child classes, enabling effective code reuse and object hierarchy management. This functionality supports both constructor-based and method-based inheritance patterns.


### Constructor Invocation

When extending a parent class, child constructors typically need to initialize their own properties while also calling the parent constructor. The `super` keyword facilitates this process by allowing child constructors to execute `super(arg1, arg2, /* ... */ argN)` to call the parent constructor. This ensures that the parent's constructor logic runs before the child's constructor continues execution.

For example, in the Rabbit-Animal inheritance scenario, the Rabbit constructor calls `super()` to properly initialize itself while the parent Animal constructor handles common initialization logic.


### Method Chaining

In addition to constructor invocation, `super` enables method chaining, allowing child class methods to invoke parent class methods while maintaining access to their own arguments. Using the syntax `super.method(...args)`, child methods can extend or modify parent functionality while preserving their original behavior.

This pattern is particularly useful when implementing method overriding, where a child class provides a different implementation of a method while still calling the parent's version. The Musician example demonstrates this pattern, where the subclass extends the Artist class's constructor while calling `super(name)` to maintain the inherited functionality.


### Prototype Considerations

The `super` keyword operates on the prototype chain, meaning its reference is determined by the class or object literal in which it's declared. When working with inherited classes, `super` always refers to the correct parent prototype, even when intermediate prototypes are modified. This consistent reference mechanism enables reliable method and property access across complex inheritance hierarchies.


### Browser Support

As of June 2017, modern browsers fully support the `super` keyword, with Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38 all providing comprehensive implementation. For developers targeting older environments or specific browser versions, polyfills and transpilers like Babel can enable reliable `super` functionality across broader deployment scenarios.


## Best practices for super usage

'super' should be called before using 'this' in a constructor, and before the constructor returns. This ensures that the parent class is properly initialized before the subclass can proceed.

The browser support for 'super' extends back to June 2017, with all modern browsers - Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38 - fully implementing the functionality. This consistency across major browser versions means that the 'super' keyword can be relied upon in contemporary web development without compatibility concerns.

When defining methods using class syntax, developers should use the spread operator (...arguments) to pass all arguments to the parent constructor. This approach provides flexibility: if the number of arguments in the parent constructor changes, the child constructor remains unaffected, requiring updates only in code that directly interacts with the constructor signatures.

This best practice is rooted in JavaScript's class implementation history. Introduced in ES2015 to address shortcomings in ES5's class implementation, 'super' builds on Python's 2.x version while improving upon existing solutions in the JavaScript ecosystem. The keyword's functionality operates on the prototype chain, meaning that when working with inherited classes, 'super' always refers to the correct parent prototype, even when intermediate prototypes are modified.

For developers targeting older environments or specific browser versions, polyfills and transpilers like Babel can enable reliable 'super' functionality across broader deployment scenarios. The keyword's syntax allows for constructor calls (super(...args)), property lookups (super.prop), and method invocations (super.method(...args)), providing robust support for various inheritance patterns.


## super vs. prototype inheritance

These examples demonstrate that while the `super` keyword simplifies many aspects of JavaScript inheritance, developers working with older JavaScript versions or environments must implement their own solutions to achieve similar functionality. A notable implementation, described by Ivo Wetzel, uses a combination of prototype manipulation and function proxies to maintain correct prototype references across multiple inheritance chains.

The fundamental challenge in emulating `super` lies in maintaining consistent prototype references while allowing recursive method calls. Most attempts to implement this functionality fall short of one or more criteria:

1. The naive implementation using `child.prototype.$super = parent.prototype` fails when `C.prototype` is overwritten, breaking the reference between parent and child prototypes.

2. More sophisticated approaches, such as Ivo Wetzel's solution, maintain correct prototype references while supporting recursive super calls across multiple inheritance chains. However, these implementations typically break one of the specified criteria:

   - They may not correctly handle changes to parent prototypes (criteria 1)

   - They often require additional code to manage meta functionality (criteria 3)

   - They may not work in ES5 mode without compilation (criteria 4)

Despite these limitations, these implementations provide valuable insights into JavaScript's inheritance mechanisms. The most practical approach appears to be a combination of prototype manipulation and function proxies, as demonstrated by the solution described by Ivo Wetzel.

The JavaScript class system's `super` functionality relies on consistent prototype references and correct function scoping. When implementing custom solutions, developers must carefully consider how changes to prototype chains affect method access and function calls. This complexity highlights the challenges in replicating JavaScript's built-in inheritance mechanisms while maintaining compatibility with older JavaScript versions and environments.


## History and implementation of super

The 'super' keyword was introduced in ECMAScript 2015 to address limitations in the previous ES5 implementation of JavaScript classes. Unlike ES5's class system, which required explicit constructor chaining through prototype manipulation, ES6's 'super' keyword provides a more intuitive and flexible approach to class inheritance.

Building on Python's 2.x implementation of the 'super' keyword, ES6's version solves several key issues while maintaining compatibility with existing JavaScript patterns. As noted in the specification documentation, 'super' allows both method invocation (`super(...args)`) and property lookup (`super.prop` and `super[expr]`), providing powerful capabilities for working with class hierarchies.

Modern JavaScript engines have provided consistent support for this feature since March 2016, with popular browsers implementing the required functionality. Current implementations maintain several important properties: 'super' is not a variable but a function call mechanism, and it determines its reference based on the class or object literal in which it's declared, rather than the object the method is called on.

The keyword's behavior closely mirrors Python's implementation, where 'super' points to the base method from where it's called, without requiring explicit arguments. This design choice simplifies inheritance patterns while maintaining flexibility. The specification also clarifies that 'super' must be called before the 'this' keyword and before the constructor returns, ensuring proper initialization order in class hierarchies.

