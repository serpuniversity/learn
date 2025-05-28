---

title: JavaScript Array Type Checking

date: 2025-05-26

---


# JavaScript Array Type Checking

JavaScript arrays are fundamental data structures that enable developers to store and manipulate collections of items. However, accurately identifying arrays in JavaScript can be surprisingly challenging due to the language's flexible type system and the presence of array-like objects. This article explores the most reliable methods for checking if a variable is an array, comparing native functionality with alternative implementations and discussing the intricacies of JavaScript's array type checking.


## Built-in Array Type Check

The most modern and recommended approach for checking if a variable is an array in JavaScript is to use the Array.isArray() method. This built-in JavaScript function is available in modern environments and provides reliable results. For example:

```javascript

let myArray = [1, 2, 3];

console.log(Array.isArray(myArray)); // Output: true

```

The method returns false for non-array values, including objects, numbers, strings, and undefined. For example:

```javascript

console.log(Array.isArray({})); // Output: false

console.log(Array.isArray(123)); // Output: false

console.log(Array.isArray('Array')); // Output: false

console.log(Array.isArray(undefined)); // Output: false

```

For environments that lack native support, including older versions of Internet Explorer, Array.isArray() can be implemented using the following polyfill:

```javascript

if (typeof Array.isArray === 'undefined') {

  Array.isArray = function(obj) {

    return Object.prototype.toString.call(obj) === '[object Array]';

  };

}

```

Mozilla recommends using Array.isArray() over other methods like constructor property checks, as it provides consistent behavior across different JavaScript implementations. The method is specifically designed to handle arrays as a distinct data type, distinguishing them from array-like objects like NodeLists or the arguments object.


## Array.isArray Method

The Array.isArray() method is a static method that determines whether a given value is an array. It employs a branded check similar to the in operator, using a private property initialized by the Array constructor. This method accurately differentiates between actual Array instances and objects with Array.prototype in their prototype chain, where instanceof Array would incorrectly identify them as arrays.

Key features include:

- Correctly identifying Array objects created via constructor syntax or literal syntax

- Accepting empty arrays, arrays with elements, and arrays created with new Array()

- Rejecting objects with Array.prototype in their prototype chain but that are not actual arrays

- Returning false for non-array values including {}, null, undefined, numbers, strings, and TypedArray instances

The method's implementation leverages ECMAScript 5 standards and has been widely available across browsers since July 2015. For most modern JavaScript applications, the native Array.isArray() implementation provides the most reliable and efficient means of array detection.


## Alternative Implementation

The most modern and recommended approach for checking if a variable is an array in JavaScript is the Array.isArray() method, which is available in modern JavaScript environments. This built-in function provides reliable results and is specifically designed to handle arrays as a distinct data type.

For older JavaScript libraries or environments without native support for Array.isArray(), w3schools' method offers a practical alternative:

```javascript

function isArray(o) {

    return o.constructor.toString().indexOf("Array") > -1;

}

```

This implementation checks if the object's constructor property contains the string "Array". While this method works for many cases, it has limitations - it fails for objects extended with custom constructors and encounters errors when checking for null.

An efficient approach for environments without native support is to combine instanceof and constructor property checks:

```javascript

function isArray(array) {

    return array instanceof Array;

}

```

This method verifies if the variable instance appears in the constructor's prototype chain. However, as noted by Val, it doesn't work for objects extended with custom constructors and throws an error when testing null values. The recommended practice is to first verify that the object is not null before attempting to check its type.

For extended compatibility, older JavaScript versions or environments lacking native support can implement Array.isArray() using a polyfill:

```javascript

if (typeof Array.isArray === 'undefined') {

    Array.isArray = function(obj) {

        return Object.prototype.toString.call(obj) === '[object Array]';

    };

}

```

This polyfill provides a reliable array check by comparing the object's internal representation to the expected '[object Array]' string. Modern frameworks like jQuery and Underscores provide their own implementations for similar functionality.


## Compatibility and Polyfills

The Array.isArray() method offers reliable cross-browser compatibility, with widespread availability in modern browsers since ECMAScript 5. For environments lacking native support, polyfills provide a practical solution.

The most maintainable approach combines instance checks with constructor verification:

```javascript

function isArray(array) {

  return array instanceof Array;

}

```

This method safely determines array type for most use cases. For broader compatibility, consider the following polyfill:

```javascript

if (typeof Array.isArray === 'undefined') {

  Array.isArray = function(obj) {

    return Object.prototype.toString.call(obj) === '[object Array]';

  };

}

```

For extended functionality, frameworks like jQuery and Underscore offer their own implementations:

```javascript

var isArray = Array.isArray || function(obj) {

  return !!(obj && obj.concat && obj.unshift && !obj.callee);

};

```

Advanced implementations may combine multiple checks for enhanced reliability. The recommended practice is to first validate non-null values before performing type checks:

```javascript

function isArraySafe(value) {

  return value !== null && Array.isArray(value);

}

```

These approaches provide robust array detection while maintaining compatibility across various JavaScript environments.


## Additional Considerations

For environments with native Array.isArray() support, the most performant method is:

```javascript

function isArray(o) {

    return o.constructor === Array;

}

```

This constructor property check is approximately 20x faster than using `toString()` for primitive types and has fewer edge cases. However, for objects extended with custom constructors, this method can produce false positives.

An extended compatibility approach, while not ideal for all cases, can be:

```javascript

function isArray(o) {

    return o.constructor === Array && o.constructor.toString().indexOf("Array") > -1;

}

```

This combined check reduces false positives by verifying both constructor properties and function names.

For detailed array type checking, developers can implement comprehensive tests:

```javascript

function isArray(obj) {

    return obj !== null &&

           typeof obj === 'object' &&

           Array.isArray(obj) &&

           obj.length > 0 &&

           typeof obj.splice === 'function' &&

           !(obj.propertyIsEnumerable('length'));

}

```

This implementation combines multiple reliable checks for enhanced accuracy and robustness.

