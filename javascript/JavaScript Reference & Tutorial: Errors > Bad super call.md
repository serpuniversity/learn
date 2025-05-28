---

title: JavaScript Super Call Best Practices

date: 2025-05-26

---


# JavaScript Super Call Best Practices

JavaScript's `super` keyword transforms class inheritance through refined constructor calls and method references. From precise initialization chaining to consistent method overriding, this article illuminates `super`'s fundamental role in modern JavaScript while guiding developers through its syntactic nuances and best practices.


## Super Call Fundamentals

The `super` keyword revolutionizes JavaScript's class inheritance through syntactic improvements over traditional prototypal inheritance. In ES6 syntax, `super` functions both as a constructor call and method reference, replacing the need for manual prototype assignments.

Constructor Implementation

The `super` constructor call, as demonstrated in the Animal-Gorilla example, enables precise initialization chaining. The Gorilla constructor must call `super(name)` to properly instantiate with a `name` property, while also setting its own `isGorilla` flag. This pattern ensures that derived class constructors always begin with `super()` unless explicitly opting out for specific reasons.

Method Access

Within method definitions, `super` acts as both a function call and property reference. For instance, in the `trout` class extending `fish`, `super()` would access the fish prototype's methods directly. This dual functionality simplifies instance property access while maintaining clear inheritance relationships.

Property Assignment

A critical detail is that `super()` must be the first statement in the derived constructor, followed by property assignments. Attempting to set properties before calling `super()` results in an undefined `this` context, as shown in the alternative trout constructor example. This restriction ensures consistent initialization order across classes.

Browser Support

Modern browsers support `super` since June 2017, with versions 51+ for Chrome, Edge 15, Firefox 54, Safari 10, and Opera 38. However, developers targeting older environments should avoid relying on `super()` and instead use traditional prototype assignment methods.


## Super Call Restrictions

In JavaScript class inheritance, the `super` keyword requires precise adherence to several fundamental restrictions. These requirements ensure proper constructor chaining and method overriding, although they can introduce complexities in certain scenarios.


### Static Method Calling

Static methods within a class hierarchy can be invoked using `super`, enabling consistent documentation and implementation among derived classes. For example, a square class extending a base shape class can maintain a unified logging mechanism through static method invocation. This approach simplifies inheritance while preserving core functionality.


### Field Property Access

Super property access behaves distinctly based on whether fields are static or instance-level. Instance fields set on an object map directly to the instance rather than the prototype, allowing for clean encapsulation and separation of concerns. In contrast, static fields accessed through `super` resolve to the superclass prototype, enabling shared attribute management across related classes.


### Method Reading Behavior

Reading from super properties follows a predictable pattern, behaving similarly to Reflect.get(Object.getPrototypeOf(objectLiteral), "x", this). This consistency ensures that unbinding or rebinding methods doesn't alter the super reference, maintaining intended inheritance behavior.


### Constructor Implementation

The `super` constructor call serves a critical role in class initialization, particularly when dealing with complex argument handling. In cases where a derived class constructor requires multiple parameters, utilizing the spread operator through `super(...arguments)` offers a robust solution. This approach ensures proper argument passing while maintaining clear constructor semantics.


### Property Deletion Restrictions

Developers encounter specific limitations when working with `super.prop` and `super[expr]` constructions. Direct deletion attempts are prohibited, throwing a ReferenceError when attempting to remove super properties. This restriction prevents unintentional interference with superclass state while maintaining controlled property management.


### Method Overriding Best Practices

To effectively implement method overriding while maintaining proper constructor chaining, developers should follow these guidelines:

1. Position `super()` as the first statement in derived class constructors to ensure consistent initialization order.

2. Use the spread operator (`super(...arguments)`) for argument passing when extending constructors with additional parameters.

3. Implement static method calls through `super` to maintain consistent documentation and behavior across class hierarchies.

4. Handle instance and static fields separately, ensuring instance properties bind directly to the instance while static fields reference the prototype chain.


### Practical Considerations

While the modern JavaScript environment supports these patterns, developers targeting older environments should consider alternate inheritance approaches. Traditional prototype assignment methods offer compatibility while maintaining clear class relationships. For complex requirements, third-party libraries or frameworks may provide additional solutions, balancing modern features with broader compatibility needs.


## Super Call Best Practices

Super method invocations behave consistently across different JavaScript environments, making them reliable for maintaining inheritance relationships. However, developers should be aware of several best practices to ensure compatibility and maintain the intended inheritance patterns.

Prototype.js Approach Integration

For developers using Prototype.js, the library introduces a `$super` parameter as the first argument to methods. While this approach adds complexity through framework-specific magic, it provides a robust solution for maintaining inheritance relationships. Modern JavaScript frameworks often generate similar wrapper functions, making this pattern less relevant for direct code implementation but valuable for understanding inheritance patterns.

Constructor Call Variations

Developers can implement constructor calls in several ways, with TypeScript offering a stricter approach compared to ES6. By allowing other code in constructors before `super` calls while preventing `this` access, TypeScript provides a safeguard against "call super" anti-patterns identified by Martin Fowler. This stricter rule provides additional clarity in constructor implementation, though it may require developers to learn more complex constructor rules than "Don't use `this` before calling `super`."

Method Implementation Best Practices

To implement overridden methods effectively while maintaining proper constructor chaining, developers should follow these guidelines:

1. Position `super()` as the first statement in derived class constructors to ensure consistent initialization order.

2. Use the spread operator (`super(...arguments)`) for argument passing when extending constructors with additional parameters.

3. Implement static methods through `super` to maintain consistent documentation and behavior across class hierarchies.

4. Handle instance and static fields separately, ensuring instance properties bind directly to the instance while static fields reference the prototype chain.

Super Property Access

The `super` keyword supports both function calls and property lookups. For instance, within method definitions, use `super()` to directly access the superclass's prototype methods. This dual functionality simplifies instance property access while maintaining clear inheritance relationships.

Performance Considerations

While TypeScript's stricter rules offer valuable clarity, developers should consider performance implications when choosing between different implementation approaches. The Salsify approach, which uses `Object.defineProperty` and avoids wrapper functions, demonstrates a more efficient implementation without the need for `Function.caller` or debugger frames. Modern JavaScript engines increasingly optimize these patterns, making earlier concerns about performance less relevant in most practical scenarios.


## Super Call Implementations

The JavaScript ecosystem presents multiple approaches to handling super calls, each with its own trade-offs and compatibility considerations. Understanding these alternatives helps developers choose the most appropriate implementation strategy for their projects.


### Prototype.js Approach

This approach introduces a special `$super` parameter as the first argument to methods, relying on framework-specific magic to detect and pass overridden implementations. While this provides robust inheritance management, it requires wrapper functions around every method, potentially impacting performance through additional try/finally block setup. The complexity of managing these wrapper functions represents a significant barrier for direct implementation, though their principles influence modern inheritance patterns.


### CoffeeScript and TypeScript Approaches

CoffeeScript and TypeScript both offer built-in support through their respective `super` keywords. However, TypeScript's implementation aligns more closely with classical inheritance patterns, using a syntax similar to Java. These approaches provide straightforward method calls and require fewer boilerplate changes during migration. The TypeScript implementation, while stricter in constructor handling ("Don't use this before calling super"), introduces additional complexity for developers learning modern JavaScript inheritance patterns.


### Salsify Approach

Developed by Salsify, this implementation defines a dynamic `super` property on base prototypes, requiring `Object.defineProperty` support and `Function.caller`, both of which will be deprecated in ES6. Unlike Prototype.js, this approach avoids wrapper functions entirely, demonstrating a simpler implementation that worked reliably in older environments. However, its reliance on `Function.caller` and use of `Object.defineProperty` limits its relevance for modern development while offering a practical solution for maintaining compatibility with older JavaScript engines.


### Modern Implementation Considerations

Developers approaching this functionality from a modern perspective should prioritize simplicity and maintainability. The ES6 specification provides the most direct solution through its built-in `super` keyword, while third-party libraries can offer additional functionality without requiring deep framework dependencies. For most projects, the native ES6 implementation offers the best balance of functionality and compatibility, although careful consideration of target environments remains crucial for broader deployment strategies.


## Super Call Frequently Asked Questions


### Always Call Super in Overridden Methods

In environments like iPhone and Android SDKs, it's essential to call `super` in every overridden method to prevent program crashes. This requirement is specific to these environments and is not a general object-oriented design practice. Martin Fowler's article "Call Super" (http://www.martinfowler.com/bliki/CallSuper.html) discusses this anti-pattern in detail.


### Setting Up Inheritance Without Classes

JavaScript's prototype-based inheritance model provides everything needed to call super methods without explicit class definitions. When overriding methods, an object simply grabs the function with the same name from its prototype and applies it. This approach works but can be verbose, particularly when working with complex composite views.


### Constructor Behavior and this

Before calling `super`, a subclass constructor must not use `this`. However, developers can work around this restriction by wrapping `super` calls in function calls that refer to `this`. TypeScript's stricter rule ("Don't use this before calling super") is aimed at preventing common errors but introduces complexity for developers learning modern JavaScript inheritance patterns.


### Modern Implementation Considerations

For new JavaScript projects, the language's built-in `super` keyword in ES6 is the recommended approach. While third-party libraries like Prototype.js offer framework-specific solutions, their complexity is generally unnecessary for most modern applications. The Salsify approach demonstrates a simpler implementation but requires `Object.defineProperty` support and `Function.caller`, both of which will be deprecated in ES6.


### Common Pitfalls and Best Practices

The `super()` invocation can only be used in derived class constructors and must appear before any other constructor code. It specifically cannot be called in class methods or functions used as constructors. The spread operator (`super(...arguments)`) provides a concise solution for passing arguments to the parent constructor, but developers should be aware that tools might need to analyze code to determine the argument names if this pattern becomes widespread.

