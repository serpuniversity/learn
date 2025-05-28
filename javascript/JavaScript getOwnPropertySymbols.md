---

title: JavaScript Object getOwnPropertySymbols Method

date: 2025-05-26

---


# JavaScript Object getOwnPropertySymbols Method

JavaScript objects can contain a diverse array of property types, including standard strings and numbers, as well as more specialized features like symbol properties. Released as part of ECMAScript 6 (ES6), the Object.getOwnPropertySymbols() method provides a standardized way to access these symbol properties directly. This article explores how to use this method, what it returns, and how it fits into broader JavaScript object enumeration capabilities.


## Introduction

The Object.getOwnPropertySymbols() method returns an array of all symbol properties present in a given object. This built-in JavaScript method has been a standard feature since ES6 and is supported across modern browsers, including Chrome 34, Edge 12, Firefox 31, and Safari 9.

When called on an object with no symbol properties, the method returns an empty array. It becomes particularly useful for identifying and working with symbol properties in an object's prototype chain. For example, given the following object with both local and global symbol properties:

```javascript

let obj = {};

const a = Symbol("a");

const b = Symbol.for("b");

obj[a] = "localSymbol";

obj[b] = "globalSymbol";

console.log(Object.getOwnPropertySymbols(obj));

// Output: [Symbol(a), Symbol(b)]

```

This output demonstrates that `Object.getOwnPropertySymbols()` returns an array containing the symbol properties defined directly on the object. The method works similarly to `Object.getOwnPropertyNames()`, which returns an array of string properties, but includes symbol properties that `Object.getOwnPropertyNames()` cannot access.

The order of symbols returned by `getOwnPropertySymbols` follows a specific structure determined by their insertion order. For objects containing symbols, the returned array includes properties added as `Symbol()` and `Symbol.for()` keys. The method is part of the ECMAScript 2026 Language Specification and provides developers with a standardized way to work with symbol properties in their applications.


## Method Syntax and Parameters

The method takes a single parameter: `obj`, which is the target object. It returns an array of all symbol properties found directly upon the given object. This can be demonstrated through the following examples:

```javascript

const object1 = {};

let vala = Symbol('geek1');

let valb = Symbol.for('geek2');

object1[vala] = 'localSymbol';

object1[valb] = 'globalSymbol';

const objectSymbols = Object.getOwnPropertySymbols(object1);

console.log(objectSymbols.length); // Output: 2

console.log(objectSymbols); // Output: [Symbol(geek1), Symbol(geek2)]

```

For objects containing multiple symbol properties, the method returns an array with all matching symbols:

```javascript

const object1 = {};

let vala = Symbol('geek1');

let valb = Symbol.for('geek2');

let valc = Symbol.for('geek3');

object1[vala] = 'localSymbol';

object1[valb] = 'globalSymbol';

object1[valc] = 'globalSymbol';

const objectSymbols = Object.getOwnPropertySymbols(object1);

console.log(objectSymbols.length); // Output: 3

console.log(objectSymbols); // Output: [Symbol(geek1), Symbol(geek2), Symbol(geek3)]

console.log(objectSymbols[0]); // Output: Symbol(geek1)

console.log(objectSymbols[2]); // Output: Symbol(geek3)

console.log(objectSymbols[1]); // Output: Symbol(geek2)

```

The symbol properties are returned in the order they were inserted into the object, providing a clear structure for working with symbol-based properties. This ordered retrieval is particularly useful when dealing with objects that have both string and symbol keys:

```javascript

let objMixed = { [vala]: 'Symbol-based value', normalKey: 'String-based value' };

let symbolKeys = Object.getOwnPropertySymbols(objMixed);

let stringKeys = Object.keys(objMixed);

console.log('Symbol keys:', symbolKeys); // Output: [Symbol(geek1)]

console.log('String keys:', stringKeys); // Output: [normalKey]

```

The method effectively works as a complement to `Object.keys()`, allowing developers to handle objects with mixed property types while ensuring that symbol-based properties are properly identified and accessed.


## Return Value and Usage

When called on an object with no symbol properties, the method returns an empty array. This demonstrates the method's reliable behavior when working with objects that have not been explicitly assigned any symbol properties.

The syntax and parameters of the method remain consistent across implementations, with the primary function being to return an array of symbol properties found directly upon the given object. The method works similarly to `Object.getOwnPropertyNames()`, which returns an array of string properties, but includes symbol properties that `Object.getOwnPropertyNames()` cannot access.

Understanding the method's behavior with different object types is crucial for effective implementation. For example, when applied to objects with both string and symbol keys, the method returns symbol properties in the order they were inserted:

```javascript

let objMixed = { [vala]: 'Symbol-based value', normalKey: 'String-based value' };

let symbolKeys = Object.getOwnPropertySymbols(objMixed);

let stringKeys = Object.keys(objMixed);

console.log('Symbol keys:', symbolKeys); // Output: [ Symbol(geek1) ]

console.log('String keys:', stringKeys); // Output: [ normalKey ]

```

The `Object.getOwnPropertySymbols()` method plays a complementary role to `Object.keys()`, allowing developers to handle objects with mixed property types while ensuring symbol-based properties are properly identified and accessed. This functionality is particularly valuable when dealing with objects that contain both string and symbol keys, as it provides clear separation between the two property types.


## Browser Support and Polyfill

This polyfill supports modern browsers including Android 2.x+, iOS5+, Windows Phone 7+, FirefoxOS 1.0+, Opera Mini, and various other Webkit-based or Chrome-based browsers. It works seamlessly with Object.assign and is compatible with Node.js 0.6 and higher versions.

The polyfill maintains core functionality while ensuring compatibility with Object.getOwnPropertyNames, which will not display symbol properties. It's noteworthy that core-js also includes symbol support as part of its partial polyfill implementation.

The method functions correctly in all supported browsers since its addition in September 2015. For instance, Chrome 34, Edge 12, Firefox 31, and Safari 9 all fully support the method. Compatibility extends to Android WebViews at version 37 and Chrome Android since 34, making it suitable for a wide range of mobile and desktop environments.


## Related Methods and Concepts

The `Object.getOwnPropertySymbols()` method returns an array of all symbol properties found directly upon a given object. This feature is widely available and has been supported across browsers since September 2015, with full compatibility in Chrome 34, Edge 12, Firefox 31, and Safari 9.

When called on an object with no symbol properties, the method returns an empty array. It becomes particularly useful for identifying and working with symbol properties in an object's prototype chain. For example, given an object with both local and global symbol properties:

```javascript

let obj = {};

const a = Symbol("a");

const b = Symbol.for("b");

obj[a] = "localSymbol";

obj[b] = "globalSymbol";

console.log(Object.getOwnPropertySymbols(obj));

// Output: [Symbol(a), Symbol(b)]

```

This output demonstrates that `Object.getOwnPropertySymbols()` returns an array containing the symbol properties defined directly on the object. The method works similarly to `Object.getOwnPropertyNames()`, which returns an array of string properties, but includes symbol properties that `Object.getOwnPropertyNames()` cannot access.

Understanding the method's behavior with different object types is crucial for effective implementation. For example, when applied to objects containing both string and symbol keys, the method returns symbol properties in the order they were inserted:

```javascript

let objMixed = { [vala]: 'Symbol-based value', normalKey: 'String-based value' };

let symbolKeys = Object.getOwnPropertySymbols(objMixed);

let stringKeys = Object.keys(objMixed);

console.log('Symbol keys:', symbolKeys); // Output: [ Symbol(geek1) ]

console.log('String keys:', stringKeys); // Output: [ normalKey ]

```

The method works as a complement to `Object.keys()`, allowing developers to handle objects with mixed property types while ensuring that symbol-based properties are properly identified and accessed.

The property order returned by `getOwnPropertySymbols` follows a specific structure determined by their insertion order. This applies specifically to symbol keys, as expando-capable keys (which are numerically sorted) are not symbols. For instance, when an object contains multiple symbols:

```javascript

let obj = {};

const a = Symbol('a');

const b = Symbol('b');

const c = Symbol('a');

obj[a] = 'value1';

obj[b] = 'value2';

obj[c] = 'value3';

console.log(Object.getOwnPropertySymbols(obj)); // Output: [Symbol(a), Symbol(b), Symbol(a)]

```

The returned array reflects the order in which the symbols were inserted into the object.

Related methods such as `Object.getOwnPropertyNames()`, `Reflect.ownKeys()`, and `JSON.keys()` offer additional functionality for property enumeration in JavaScript objects. For example, `Reflect.ownKeys()` returns an array of all own property keys (including both enumerable and non-enumerable properties), while `JSON.keys()` provides keys for JSON representation.

The method functions correctly in all supported browsers since its addition in September 2015. For instance, Chrome 34, Edge 12, Firefox 31, and Safari 9 all fully support the method. Compatibility extends to Android WebViews at version 37 and Chrome Android since 34, making it suitable for a wide range of mobile and desktop environments.

