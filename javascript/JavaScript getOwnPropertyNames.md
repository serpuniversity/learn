---

title: JavaScript Object.getOwnPropertyNames() - Retrieve All Object Properties

date: 2025-05-27

---


# JavaScript Object.getOwnPropertyNames() - Retrieve All Object Properties

JavaScript's `Object.getOwnPropertyNames()` method offers developers a powerful tool for comprehensive object property manipulation and debugging. While similar methods like `Object.keys()` provide valuable functionality, `getOwnPropertyNames()` stands out by returning all property names - including non-enumerable ones - in the order they were inserted. This introduction will explore the method's basic usage, compare it to related functions, and demonstrate its importance in modern JavaScript development, particularly for working with complex object structures and ensuring consistent property enumeration across implementations.


## Basic Usage

The `Object.getOwnPropertyNames()` function allows developers to retrieve all property names from an object, including those that are not enumerable. This method is particularly useful for comprehensive property manipulation and debugging, as it provides a complete list of an object's properties, unlike `Object.keys()`, which only returns enumerable properties.

According to the documentation, the function works by returning an array of strings representing the names of the object's properties. These properties are returned in the order they were inserted, providing consistent behavior when iterating through an object's properties. The method accepts a single parameter - the object from which to retrieve property names - and returns an array of strings.

For example, when applied to a simple object literal, as shown in the documentation examples, `Object.getOwnPropertyNames()` correctly identifies and returns all property names, whether or not they are enumerable. This functionality makes it particularly valuable for working with complex object structures that may contain non-enumerable properties.

The method's broad compatibility across modern browsers and its support for both string-keyed and symbol-based properties make it a versatile tool for JavaScript development, though developers should be aware that it does not return properties symbol-based non-enumerable properties.


## Comparison with Object.keys()

The primary distinction between `Object.getOwnPropertyNames()` and `Object.keys()` lies in their handling of property enumerability. While `Object.keys()` returns only the enumerable properties of an object, `getOwnPropertyNames()` includes both enumerable and non-enumerable properties, making it a more comprehensive property accessor.

This difference becomes particularly relevant when working with certain types of objects. For example, the `Error` constructor creates objects that contain non-enumerable properties that `Object.keys()` misses, as demonstrated in the example where `Object.keys(new Error('some msg'))` returns an empty array while `Object.getOwnPropertyNames(new Error('some msg'))` correctly identifies the "stack" and "message" properties.

The method's behavior also differs subtly in how it processes various object types. When dealing with array-like objects, `getOwnPropertyNames()` properly identifies non-enumerable properties like length, which `Object.keys()` typically ignores. In the case of function objects, both methods return enumerable properties, but `getOwnPropertyNames()` provides a complete list of all properties, including those modified with `Object.defineProperty()`.

The original insertion order of properties is preserved in the returned array, matching the behavior of `for...in` loops. However, this order guarantee varies between implementations - for instance, Node.js does not currently enforce key ordering in its implementation of `getOwnPropertyNames()`.

Developers should note that while `getOwnPropertyNames()` provides comprehensive property information, it requires careful handling with certain object types. Null-prototype objects created with `Object.create(null)` lack access to the `hasOwnProperty()` method, making alternative solutions necessary for checking property existence. In these cases, either `Object.hasOwn()` (where available) or an external object's `hasOwnProperty()` function should be used.


## Property Order and Inheritance

The `Object.getOwnPropertyNames()` method returns an array of strings corresponding to the enumerable and non-enumerable properties found directly upon the given object, with the ordering of the enumerable properties consistent with the ordering exposed by a `for...in` loop or `Object.keys()` over the properties of the object.

Non-negative integer keys are added to the array in ascending order first, followed by string keys in the order of their insertion. This property order preservation allows developers to maintain the original insertion order of the object's properties, though it's important to note that the exact behavior can vary between implementations - for example, Node.js does not enforce key ordering in its implementation of `getOwnPropertyNames()`.

The method's property retrieval includes both enumerable and non-enumerable properties, making it particularly useful for comprehensive property manipulation and debugging. However, it's crucial to understand that property inheritance through prototype chains is not automatically followed. To access inherited properties, developers must explicitly check an object's [[Prototype]] using `Object.getPrototypeOf()`, as the `__proto__` property is deprecated.

For practical implementations, the MDN documentation provides several relevant examples, including checking for property existence and differentiating between direct properties and inherited properties. The method's behavior with symbol properties is worth noting: while `getOwnPropertyNames()` returns all properties including non-enumerable ones, symbol properties are not included unless accessed through `Object.getOwnPropertySymbols()`. This distinction makes the method a robust tool for object introspection and property-based manipulation in JavaScript development.


## Handling Special Cases

The `Object.getOwnPropertyNames()` method returns all properties present in a given object except for those symbol-based non-enumerable properties. The method accepts a single parameter, obj, which holds the object whose enumerable and non-enumerable properties are to be returned.

As demonstrated in the documentation examples, the method returns an array of strings corresponding to the properties found directly in the given object. When applied to a simple object literal, `Object.getOwnPropertyNames()` correctly identifies and returns all property names, whether or not they are enumerable.

For array-like objects, the method properly identifies non-enumerable properties like length, which `Object.keys()` typically ignores. In the case of function objects, both methods return enumerable properties, but `getOwnPropertyNames()` provides a complete list of all properties, including those modified with `Object.defineProperty()`.

The method is particularly useful for working with complex object structures that may contain non-enumerable properties. However, it's important to understand that property inheritance through prototype chains is not automatically followed. To access inherited properties, developers must explicitly check an object's [[Prototype]] using `Object.getPrototypeOf()`, as the `__proto__` property is deprecated. The example provided in the documentation shows that calling `Object.getOwnPropertyNames(Object.getPrototypeOf(x))` on an empty array `x` returns an array containing inherited properties including `length`, `constructor`, and several other standard array methods.

In cases where symbol properties are present, the method returns all properties including non-enumerable ones, though symbol properties are not included unless accessed through `Object.getOwnPropertySymbols()`. This distinction makes the method a robust tool for object introspection and property-based manipulation in JavaScript development. The method's broad compatibility across modern browsers makes it a versatile tool for JavaScript development, though developers should be aware that it does not return properties symbol-based non-enumerable properties.


## Best Practices and Alternatives

The `Object.getOwnPropertyNames()` method provides several advantages that make it suitable for specific JavaScript development needs. While `hasOwnProperty()` remains widely used for simple property checks, `getOwnPropertyNames()` offers a more comprehensive approach to object property manipulation and introspection.


### Compatibility and Implementation Details

As mentioned in the documentation, the method has been supported across browsers since July 2015 and is implemented consistently across modern environments. For developers targeting older browsers, the method's availability in all major contemporary browsers ensures broad compatibility without significant implementation changes.


### Best Practices

For practical implementation, developers are advised to use `Object.hasOwn()` where available, particularly in browsers that support it. This modern alternative provides clearer semantic meaning while maintaining consistent behavior across objects. When working with null-prototype objects created using `Object.create(null)`, developers should use either `Object.hasOwn()` or an external object's `hasOwnProperty` function to check property existence.


### Property Filtering and Usage

To work effectively with `getOwnPropertyNames()`, developers should understand its relationship with other property access methods. For scenarios requiring only enumerable properties, combining the method with `Array.prototype.filter()` can efficiently remove enumerable keys from a full property list. For comprehensive property manipulation, developers can use the method in conjunction with `Object.keys()` to first retrieve non-enumerable properties, then filter out those not directly on the object using `Object.hasOwn()`.

The method's primary value lies in its ability to provide a complete property list, making it essential for debugging, object serialization, and comprehensive property enumeration. Its consistent property order across implementations, particularly with string keys followed by non-negative integers in ascending order, allows developers to maintain predictable iteration patterns.

