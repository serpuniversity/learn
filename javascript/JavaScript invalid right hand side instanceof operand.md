---

title: Understanding JavaScript's instanceof Operator

date: 2025-05-26

---


# Understanding JavaScript's instanceof Operator

JavaScript's instanceof operator serves as a critical tool for determining object types, yet its implementation and behavior contain complexities that often confound developers. From its fundamental operation as an internal method invocation to its unreliable handling of primitive values and custom error classes, understanding instanceof requires navigating a nuanced landscape of JavaScript's prototype inheritance model. This comprehensive guide illuminates the operator's correct usage, common pitfalls, and best practices, equipping developers with the knowledge to wield this powerful type-checking tool effectively.


## Basic Usage and Purpose of instanceof

The instanceof operator is a fundamental feature of JavaScript that allows developers to determine whether one object is an instance of another constructor. At its core, instanceof checks if an object's prototype chain contains the prototype property of a specified constructor function. When used correctly, it returns true if the object is of the expected type.

For example, the expression "color1 instanceof String" would return true if color1 is a String object, while "color2 instanceof String" would return false if color2 is not a String object. This behavior is consistent across modern JavaScript environments, though subtle differences exist between older and newer implementations.

Under the hood, instanceof employs the [[HasInstance]] internal method of the function object, passing in the object we're testing. This method examines whether the function's prototype property appears anywhere in the target object's prototype chain - if found, it returns true, indicating that the object is of the specified type.

A common misconception is that instanceof relies on the constructor property being explicitly set in the prototype object. In fact, this property is not used in the determination process. Instead, instanceof directly examines the internal [[Prototype]] property of the object, following the prototype chain to establish its true type.

The operator's behavior extends beyond basic object and string checks to accommodate complex types and custom classes. In the case of classes, instanceof operates similarly, checking whether the constructor's prototype is present in the object's prototype chain.

Understanding instanceof's limitations is crucial for effective JavaScript development. The operator is particularly unreliable when dealing with primitive values, returning false for comparisons like "{} instanceof String" while returning true for "new String('') instanceof String". These quirks underscore the importance of using instanceof judiciously, particularly when dealing with objects that may have their prototype properties reassigned.


## Common Errors with instanceof

The fundamental requirement for instanceof to function correctly is that the right-hand operand be a constructor object possessing a prototype property and capable of invocation. Common mistakes include using non-object right-hand sides, invalid callables, and improperly defined constructor functions.

For example, attempting to compare against an empty string evaluates to a TypeError: "Geeks instanceof ""; // TypeError: invalid 'instanceof' operand "". Similarly, comparing numeric primitives against constructors yields unexpected results: "42 instanceof 0; // TypeError: invalid 'instanceof' operand 0".

Primitive values, particularly strings, present special challenges when used with instanceof. Direct comparisons against string literals return false: "test instanceof String; // false", while creating a new instance through the constructor correctly identifies the type: "new String('') instanceof String; // true".

The instanceof operator's functionality extends to array and object instances but behaves differently for function types. All functions inherit from Object, making typeof preferred for determining function types: "typeof Object === 'function'; // true".

In cases where custom error classes are defined by extending built-in Error types, instances may fail instanceof checks when targeting ES3 or ES5 environments. This occurs due to differences in prototype handling between the target version and ES2015+. The underlying issue, tracked in GitHub issue #13965, requires explicitly setting constructor prototypes or updating compilation targets to resolve.


## Exception Handling with instanceof

The JavaScript Exception "Invalid 'instanceof' Operand" occurs when the right-hand side operand of the instanceof operator is invalid. This can manifest as a TypeError with various messages depending on the environment, such as "Right-hand side of 'instanceof' is not an object" in Chrome or "TypeError: invalid 'instanceof' operand" in Firefox.

The error arises primarily from three conditions:

1. The right-hand operand is not an object

2. It is not callable and lacks a Symbol.hasInstance method

3. It is callable but its prototype property is not an object (e.g., arrow functions)

To illustrate, the expression "test instanceof ""; // TypeError: invalid 'instanceof' operand "" fails because an empty string is not a constructor object. Similarly, 42 instanceof 0 // TypeError: invalid 'instanceof' operand 0 returns an error, as numbers cannot be used as constructor objects.

The instanceof operator expects the right-hand side operand to be a constructor object with a prototype property and must be callable. When these conditions are not met, JavaScript raises a TypeError to prevent execution of invalid operations and maintain language consistency.

Despite its strict requirements, instanceof's functionality extends to various JavaScript constructs. All functions inherit from Object, allowing typeof to be preferred for determining function types: typeof Object === 'function' // true. Arrays also demonstrate instanceof's capabilities: arr instanceof Array returns true as arrays inherit from Object in the prototype chain.


##  instanceof and Error Objects

Custom error classes in JavaScript and TypeScript can cause issues with instanceof when targeting ES3 or ES5 environments, due to differences in prototype handling.

In JavaScript, custom errors are typically created by extending the built-in Error object, either in JavaScript or TypeScript. This works fine with newer targets, but when compiling for ES3 or ES5, the instanceof operator fails for custom errors. This issue started with TypeScript version 2.1 and is tracked in GitHub issue #13965.

The fundamental problem occurs because the proper prototype chain isn't established when creating custom errors. When you extend built-in errors like DatabaseError, you need to explicitly set the prototype to fix instanceof issues. This means that both your custom error class and any subclasses extending it must manually adjust their prototype properties to ensure correct instanceof behavior.

For example, consider this simplified custom error class:

```javascript

class DatabaseError extends Error {

  constructor(message) {

    super(message);

    this.name = this.constructor.name;

    Object.setPrototypeOf(this, new.target.prototype);

  }

}

```

In this example, the `Object.setPrototypeOf` call ensures that the custom error maintains the correct prototype chain, allowing instanceof checks to work properly. This is crucial for maintaining error handling logic that depends on specific error types.

The recommended approach is to upgrade your compilation target to ES2015 or later, which resolves these issues by properly handling prototype chains. This upgrade not only fixes instanceof problems but also aligns with modern JavaScript best practices.


## Best Practices for instanceof

The instanceof operator's reliability diminishes when applied to primitive values, returning false for comparisons like "{} instanceof String" while returning true for "new String('') instanceof String". To address these inconsistencies, developers should utilize the typeof operator when working with primitive values, as it provides more accurate type information.

For instance, instead of using "color instanceof String", the recommended approach is "typeof color === 'string'". This change yields the expected result: "typeof '' === 'string'" evaluates to true, while "typeof 42 === 'number'" correctly identifies the primitive number type.

The operator's effectiveness is further compromised when dealing with non-object values, such as strings, numbers, or uncallable objects. These cases trigger a TypeError, as demonstrated by the following examples:

```javascript

"Geeks" instanceof ""; // TypeError: invalid 'instanceof' operand ""

function GFG() { }

let gfg = GFG();

let x = new GFG();

x instanceof gfg; // TypeError: Right-hand side of 'instanceof' is not an object

```

To avoid these errors, ensure the right-hand side operand is a constructor function with a prototype property. This requirement extends to custom error classes, where instances may fail instanceof checks when targeting ES3 or ES5 environments. The proper solution involves explicitly setting the prototype property or upgrading the compilation target to ES2015+, as detailed in the GitHub issue #13965.

The operator's behavior with class instances highlights its limitations when distinguishing between primitive and class object types. While "a instanceof B" returns true when a.__proto__ == B.prototype, this result occurs regardless of how a was created - whether through new B() or B(). This inconsistency underscores the need for alternative type-checking approaches when working with complex object hierarchies.

