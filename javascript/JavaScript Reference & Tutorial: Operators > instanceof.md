---

title: instanceof Operator in JavaScript

date: 2025-05-27

---


# instanceof Operator in JavaScript

JavaScript's instanceof operator provides a powerful mechanism for determining object types through prototype chain analysis. While seemingly simple, this operator's behavior reveals fundamental aspects of JavaScript's prototypal inheritance model. Understanding how instanceof works requires examining its basic usage, internal operations, and the conditions that can lead to unexpected results. This article explores these aspects, explaining why instanceof is essential for JavaScript development while highlighting its limitations and performance considerations.


## Basic Usage and Syntax

The instanceof operator checks if an object is an instance of a specified constructor function, returning true if the object's prototype chain includes the constructor's prototype. This operator serves as a key mechanism for JavaScript's prototypal inheritance model, allowing developers to determine if one object is an instance of another.

At its core, instanceof operates by traversing the prototype chain of an object, comparing it to the prototype properties of candidate constructors. This comparison relies on the internal [[Prototype]] property that links objects together in JavaScript's prototype chain.

For example, consider the following code:

```javascript

function Person(name) {

  this.name = name;

}

let p1 = new Person('John Doe');

console.log(p1 instanceof Person); // Output: true

console.log(p1 instanceof Object); // Output: true

```

In this case, both true results are accurate because the `p1` object's prototype chain includes both `Person.prototype` and `Object.prototype`.

The operator's behavior extends to various JavaScript constructs and built-in classes. For instance:

```javascript

let arr = [1, 2, 3];

console.log(arr instanceof Array); // true

console.log(arr instanceof Object); // true

```

Here, `arr instanceof Array` returns true because Array prototype is part of the prototype chain, while `arr instanceof Object` returns true for the same reason.

However, instanceof demonstrates nuanced behavior when working with string primitives and objects:

```javascript

const pets = { amount: 4 };

console.log(pets instanceof String); // false

console.log(pets instanceof Number); // false

console.log(pets instanceof Object); // true

```

In this case, despite `pets` being an object, its prototype chain does not include String or Number prototypes, resulting in false returns for those checks.

The operator's effectiveness can vary across different execution contexts or realms, particularly when working with complex prototype chains. For example:

```javascript

[] instanceof window.frames[0].Array // false

```

This inequality occurs because Array.prototype differs between realms, demonstrating the importance of proper scope and context when using instanceof for cross-context operations.


## Internal Working and Prototype Chain

The instanceof operator operates by checking if a constructor function's prototype property appears in the prototype chain of an object. This determination is made through the object's internal [[Prototype]] property, which is automatically set when using the new operator to create an instance of an object.

When the new operator is used to create a new object, its [[Prototype]] property is explicitly set to the specified constructor function's prototype. For example, in the code snippet:

```javascript

function Person(name) {

  this.name = name;

}

let p1 = new Person('John Doe');

```

The [[Prototype]] property of `p1` is automatically set to `Person.prototype`, making `p1 instanceof Person` evaluate to true. Similarly, `p1 instanceof Object` returns true because `Person.prototype` is linked to `Object.prototype` in the prototype chain.

The operator's functionality extends to ES6 class definitions. In the example:

```javascript

class Person {

  constructor(name) {

    this.name = name;

  }

}

let p1 = new Person('John');

```

The prototype chain for `p1` again links `p1`, `Person.prototype`, and `Object.prototype`.

instanceof demonstrates nuanced behavior with string primitives and objects. For instance:

```javascript

const pets = { amount: 4 };

console.log(pets instanceof String); // false

console.log(pets instanceof Number); // false

console.log(pets instanceof Object); // true

```

Here, despite `pets` being an object, its prototype chain does not include String or Number prototypes, resulting in false returns for those checks.

A critical aspect of instanceof's behavior relates to the constructor function's Symbol.hasInstance method. This method allows for custom logic in determining whether an object belongs to a specific class or inheritance hierarchy.

In certain cases, instanceof can reveal unexpected results due to the JavaScript runtime's handling of function prototypes. For example, the operator's behavior can differ when working across different execution contexts or realms, as demonstrated by the inequality:

```javascript

[] instanceof window.frames[0].Array // false

```

This difference occurs because Array.prototype varies between realms, highlighting the importance of proper scope and context when using instanceof for cross-context operations.


## Type Checking Behavior

The Symbol.hasInstance method plays a crucial role in determining whether an object is an instance of a specific class. This method allows for custom logic in instance checks and provides greater flexibility than traditional constructor-based checking. As described in the documentation, the presence and implementation of Symbol.hasInstance can significantly influence instanceof behavior. For example, when a subclass redefines Symbol.hasInstance to return false, as shown in the Android class implementation, instances of that subclass will no longer be recognized as instances of the parent class.

The operator's type checking capabilities demonstrate nuanced behavior across various JavaScript constructs. While it correctly identifies instances of built-in classes and custom constructors, instanceof treats functions as first-class citizens in its prototype chain analysis. This behavior can be observed when checking objects created with the new operator against their constructor functions:

```javascript

var obj = new Object();

console.log(obj instanceof Object); // true

console.log(obj instanceof Function); // false

var func = new Function();

console.log(func instanceof Function); // true

console.log(func instanceof Object); // true

```

These examples illustrate that instanceof treats objects created by constructor functions as distinct from their underlying function types. Additionally, the operator exhibits consistent behavior across different execution contexts, allowing for reliable cross-context type checks when properly scoped.

The operator's type checking mechanism effectively distinguishes between primitive values and their object representations:

```javascript

var strPrimitive = "Hello";

var strObject = new String("Hello");

console.log(strPrimitive instanceof String); // false

console.log(strObject instanceof String); // true

console.log(strObject instanceof Object); // true

console.log(strPrimitive instanceof Object); // false

```

These examples highlight that instanceof correctly identifies object representations while treating primitive values as distinct types. Understanding these nuances enables developers to effectively use instanceof for type checking while avoiding common pitfalls.


## Common Pitfalls and Special Cases


### Common Pitfalls and Special Cases

The operator's behavior varies significantly when working with primitive types versus object representations. While instanceof correctly identifies object representations (e.g., `new String('Hello') instanceof String` returns true), it fails to distinguish between primitive values and their object counterparts (e.g., `String('Hello') instanceof String` returns false).

Another critical consideration is the treatment of functions as first-class citizens in prototype chain analysis. While `instanceof` correctly identifies object instances (`{} instanceof Object` returns true), it returns false for function instances (`function(){} instanceof Object` returns false), requiring developers to employ alternative methods for function type checking.

Cross-context operations demonstrate the operator's nuanced behavior. In different execution environments, prototype properties can vary, leading to unexpected results. For instance, `[] instanceof window.frames[0].Array` returns false due to realm-specific prototype differences. This variation underscores the importance of proper scope handling when performing cross-context type checks.

The operator's behavior extends to various constructors and object creation methods. While simple prototype assignments maintain expected behavior (e.g., `D.prototype = new C(); var o3 = new D(); o3 instanceof C` returns false), modifying prototype properties can lead to unexpected outcomes (e.g., `C.prototype = {}; var o2 = new C(); o2 instanceof C` returns true). This demonstrates the potential pitfalls of altering prototype chains.


## Performance Considerations

Performance testing consistently shows that `typeof` is generally faster than `instanceof`, making it the preferred choice for simple type checks while `instanceof` remains essential for complex prototype chain analysis.

The benchmark results demonstrate that `typeof` is approximately 1.198 times faster than `instanceof` when checking if an object is an instance of `Array`. While the performance difference can vary depending on the JavaScript engine used, it is particularly pronounced in certain implementation details.

The fundamental reason for this difference lies in how the two operators function. The `instanceof` operator always follows an object's prototype chain, which impacts performance based on inheritance depth. For short inheritance chains, such as `{} instanceof Object`, the performance penalty is minimal, but for longer chains, the overhead increases.

The operator's performance characteristics are further influenced by how it handles different JavaScript constructs. For example, the behavior of `instanceof` with functions differs significantly from strings: while `typeof` correctly identifies function types, `instanceof` only works properly when the function is created using the `new` keyword. This distinction makes `typeof` generally safer for determining function type across both declaration and constructor forms.

Understanding these performance considerations is crucial for developers implementing type checks in JavaScript. While `instanceof` offers powerful capabilities for prototypal inheritance analysis, its use should be carefully balanced with performance implications, particularly in applications where frequent type checks are required.

