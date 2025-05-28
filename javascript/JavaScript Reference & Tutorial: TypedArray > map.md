---

title: JavaScript TypedArray.prototype.map() Method

date: 2025-05-27

---


# JavaScript TypedArray.prototype.map() Method

JavaScript's TypedArray.prototype.map() method extends the functionality of the built-in Array.prototype.map() by applying transformation functions to elements in typed arrays. While similar in operation, this method offers specific behavior and characteristics tailored for typed array processing. From square roots to character conversion, this introduction explores how map() creates new arrays without altering the original data structure, making it a powerful tool for data manipulation in JavaScript applications.


## Overview

The map() method creates a new typed array populated with the results of calling a provided function on every element in the calling typed array. It operates similarly to Array.prototype.map() and shares the same algorithm. The method takes two parameters: a callback function and an optional thisArg.

The callback function is invoked for each element in the typed array and receives three arguments: currentValue, index (optional), and array (optional). The method processes elements before the first invocation and does not mutate the original array.

Implementation is provided by all major browsers, with full support since March 2016. It is based on ECMAScript specifications and is available across desktop and mobile browsers, including Chrome, Edge, Firefox, Opera, Safari, Android webview, Chrome Android, Firefox for Android, Opera Android, Safari iOS, Samsung Internet, WebView Android, Deno, and Node.js.


## Syntax and Parameters

The `map()` method creates a new typed array populated with the results of calling a provided function on every element in the calling typed array. This method takes two parameters: a callback function and an optional thisArg.

The callback function processes each element and receives three arguments: the currentValue (the element itself), the index (the position of the element), and the array (the original typed array being processed). It is important to note that the method operates on the calling typed array and returns a new typed array, leaving the original data structure unchanged.

The method's implementation across browsers follows ECMAScript standards, with full support available since March 2016. It is implemented in all major browsers including Chrome, Edge, Firefox, Opera, Safari, and their respective mobile variants. Node.js and specialized runtime environments like Deno also support this method.

The method supports additional features through the thisArg parameter, allowing developers to customize the context in which the callback function operates. This flexibility enables more complex transformations while maintaining the integrity of the original data structure.


## Behavior and Characteristics

The `map()` method processes elements in the typed array before the first invocation of the callback function, ensuring that appended elements after the call are not processed. Elements that are deleted before being visited are not included in the traversal, maintaining the integrity of the data structure throughout the operation.

The method's behavior when called with an object that's not a TypedArray instance creates a new typed array using the `TypedArray.from()` method. When called with a non-object, the parameter is treated as a number specifying the length of the typed array, with internal array buffering creation handling the underlying storage.

Each callback invocation operates on the typed array's values without direct mutation, making the method particularly suitable for generating derived data structures. The implementation across browsers follows ECMAScript standards, with full support available since March 2016 across major desktop and mobile platforms.


## Examples

The map() method creates a new typed array populated with the results of calling a provided function on every element of the calling typed array. This transformation results in a completely new typed array, leaving the original data structure unchanged.

The method's power comes from its flexibility in processing elements. For example, given a typed array of numbers, `map()` can be used to generate a new array where each element is the square root of the original value:

```javascript

const numbers = new Uint8Array([1, 4, 9]);

const roots = numbers.map(Math.sqrt);

console.log(roots); // Output: Uint8Array [1, 2, 3]

```

The operation can also handle custom functions with additional arguments:

```javascript

const numbers = new Uint8Array([1, 4, 9]);

const doubles = numbers.map((num) => num * 2);

console.log(doubles); // Output: Uint8Array [2, 8, 18]

```

Developers can leverage `map()` for more complex transformations, such as converting a typed array of Unicode code points to a string of characters:

```javascript

const codePoints = new Uint16Array([72, 101, 108, 108, 111]);

const message = String.fromCharCode(...codePoints.map(codePoint => codePoint));

console.log(message); // Output: "Hello"

```

The method's utility extends to more sophisticated operations, like filtering and transforming nested typed array structures. For instance, it can map a multi-dimensional typed array to a one-dimensional array of sums:

```javascript

const matrix = new Uint8Array([1, 2, 3, 4, 5, 6]);

const rowSums = matrix.buffer.slice(0, 6).map((row, idx) => row + matrix[idx + 6]);

console.log(rowSums); // Output: Uint8Array [5, 7, 9, 11, 13, 15]

```

These examples demonstrate the versatility of `map()`, allowing developers to perform complex data transformations while maintaining the integrity of the original data structure.

