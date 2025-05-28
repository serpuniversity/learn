---

title: JavaScript TypeError: can't redefine non-configurable property

date: 2025-05-26

---


# JavaScript TypeError: can't redefine non-configurable property

In JavaScript, the behavior of objects and their properties is governed by a set of rules enforced at both runtime and through language semantics. While this can lead to more predictable applications, it also introduces challenges when developers need to modify or extend existing object structures. One specific challenge arises when working with non-configurable properties, which cannot be altered once defined. This article explores the implications of non-configurable properties, how they differ from other property attributes, and the common issues developers face when attempting to modify them. Through analysis of error messages, real-world examples, and best practices, we'll provide guidance on managing these properties effectively in modern JavaScript applications.


## Understanding Non-Configurable Properties

In JavaScript, non-configurable properties are those that cannot be deleted from an object and whose attributes (other than `writable`) cannot be changed. This behavior is enforced by the language specification and is the default for properties created using `Object.defineProperty()` unless explicitly set to configurable.

An object's properties are essentially references to values through an internal "[[Prototype]]" property, which was previously accessed via `__proto__`. When both `writable` and `configurable` flags are false, attempting to modify the property results in a "Cannot redefine property" error. For properties defined with `Object.defineProperty()`, non-configurability prevents changes to the property's flags and cannot be reversed once set to false.

The primary manifestation of this restriction occurs when attempting to redefine a property using `Object.defineProperty()`, as demonstrated in the following examples:

```javascript

let obj = Object.create({});

Object.defineProperty(obj, "foo", { value: "bar" });

Object.defineProperty(obj, "foo", { value: "baz" }); // TypeError: Cannot modify non-writable property 'foo'

```

```javascript

let obj = Object.create({});

Object.defineProperty(obj, "foo", { value: "bar", configurable: true });

Object.defineProperty(obj, "foo", { value: "baz", configurable: true });

```

To reconfigure a non-configurable property for redefinition, the property must be explicitly defined with the `configurable` flag set to true:

```javascript

let obj = Object.create({});

Object.defineProperty(obj, "foo", { value: "bar", configurable: true });

Object.defineProperty(obj, "foo", { value: "baz", configurable: true });

```

Once a property is marked as non-configurable, several restrictions apply, including inability to change the configurable, enumerable, or writable attributes, as well as restrictions on accessor properties. Developers are advised to explicitly set the configurable attribute to true when defining properties to maintain flexibility in property management.


## Common Error Messages

The specific error message for the "can't redefine non-configurable property" exception varies across different JavaScript environments. In V8-based systems (which power Chrome and Node.js), the error manifests as "TypeError: Cannot modify non-writable property [property name]". Firefox returns "TypeError: can't redefine non-configurable property [property name]", while Safari displays "TypeError: Attempting to define property on object that is not extensible".

The error can appear in both strict and sloppy mode, though the behavior differs. In strict mode, attempting to add new properties to a non-extensible object results in the TypeError, as demonstrated in the following example:

```javascript

let obj = Object.create({});

Object.defineProperty(obj, "foo", { value: "bar", configurable: true });

Object.defineProperty(obj, "foo", { value: "baz", configurable: true }); // Throws TypeError: Cannot redefine property: foo

```

In sloppy mode, the addition of the new property is silently ignored, preventing any attempt to modify the property:

```javascript

let obj = Object.create({});

Object.defineProperty(obj, "foo", { value: "bar", configurable: true });

Object.defineProperty(obj, "foo", { value: "baz", configurable: false }); // Silently ignored

```

Developers should be aware that the error message can vary between different browsers, making it essential to test across multiple environments. The key takeaway is that once a property is marked as non-configurable, changing its value or attempting to redefine it will result in a TypeError, unless the configurable flag is explicitly set to true during property definition.


## Common Causes of the Error

Developers typically encounter this error when attempting to modify properties on objects that have been explicitly set as non-configurable. This restriction is particularly common in scenarios where developers are working with objects that have their property descriptors frozen using `Object.preventExtensions()` or `Object.seal()` methods.

A key scenario leading to this error is the misuse of `Object.defineProperty()` without properly managing property attributes. When defining properties using this method, developers must account for the configurable flag, which, if set to false, prevents subsequent modifications to the property descriptor. As demonstrated in the provided examples, attempting to redefine a non-configurable property produces the expected "TypeError: can't redefine non-configurable property" message across most JavaScript environments.

The error also frequently appears when developers inadvertently create non-extensible objects using `Object.preventExtensions()`. In such cases, any attempt to add new properties results in the "TypeError: Cannot create property" message. This scenario highlights the importance of understanding how property descriptors affect object behavior and the potential consequences of locking object configurations.

Additionally, the error surfaces when developers work with private fields and methods, as these are inherently non-configurable. Changes to private field properties that are marked as non-configurable produce the expected error message, preventing developers from modifying these critical object components.

Understanding these common causes helps developers anticipate and prevent this error, ensuring more robust and flexible object management in their JavaScript applications.


## Solutions and Workarounds

The most effective solutions to this error involve understanding the nature of non-configurable properties and their implications. To prevent the error from occurring, developers should avoid using `Object.defineProperty()` to define non-configurable properties unless absolutely necessary, and always explicitly set the `configurable` flag to true when defining properties that may need to be modified later.

If the error occurs due to attempting to redefine a property that has already been defined as non-configurable, developers should review their code and ensure that property definitions are consistent across files and scopes. This may involve refactoring code to avoid multiple definitions of the same property or ensuring that all property definitions use the correct configuration settings.

For cases where the error appears when working with private fields and methods, developers should carefully manage property access using getter and setter methods, as these properties are inherently non-configurable and cannot be redefined. This approach ensures that the properties remain protected while allowing controlled access through the defined methods.

When encountering this error in specific development environments like ESP32 microcontrollers, developers should carefully manage object extensions and preventions using `Object.preventExtensions()` and `Object.seal()` methods. Ensuring that objects are properly configured to support property modifications can help prevent these errors while maintaining the intended object structure.

To prevent similar errors in the future, developers should:

1. Always check property attributes before attempting to modify them

2. Use explicit configuration settings when defining properties

3. Refactor code to avoid redundant property definitions

4. Manage private fields and methods using controlled access methods

5. Test code across multiple environments to ensure consistent behavior

6. Use strict mode when developing to catch potential issues early

