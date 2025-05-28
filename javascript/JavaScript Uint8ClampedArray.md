---

title: Uint8ClampedArray - JavaScript

date: 2025-05-27

---


# Uint8ClampedArray - JavaScript

The Uint8ClampedArray represents a specialized typed array for handling RGB color data, with each element representing an 8-bit unsigned integer between 0 and 255. This article explores the array's construction methods, properties, and behavior, including its unique value clamping mechanism.


## Introduction to Uint8ClampedArray

The Uint8ClampedArray represents a one-dimensional array containing data in RGBA order, with integer values between 0 and 255 inclusive. It is part of the JavaScript TypedArrays group, which includes other typed array types like Uint8Array, Uint16Array, and Int32Array.

The array's contents are initialized to 0 unless explicitly provided. Each element is an 8-bit unsigned integer, and the array can be created using several constructors:

- From a length: new Uint8ClampedArray(2)

- From an array: new Uint8ClampedArray([21, 31])

- From another TypedArray: new Uint8ClampedArray(x)

- From an ArrayBuffer: new Uint8ClampedArray(buffer, 1, 4)

- From an iterable: new Uint8ClampedArray((function* () { yield* [1, 2, 3]; })())

The constructor method only accepts the new keyword, and calling it without the new operator will result in a TypeError. The Uint8ClampedArray has a BYTES_PER_ELEMENT property that returns 1, indicating 8-bit elements.

When assigning values to elements, the array "clamps" the values to the 0-255 range. If a value is less than 0, it is set to 0; if greater than 255, it is set to 255. Non-integer values are rounded to the nearest integer before storage.


## Creating Uint8ClampedArray Instances

The Uint8ClampedArray constructor creates typed array objects representing fixed-length binary data buffers, storing values as 8-bit unsigned integers within the 0-255 range. Values outside this range are automatically clamped to 0 or 255, and non-integer values are rounded to the nearest integer before storage.

The constructor supports multiple creation methods:

1. `new Uint8ClampedArray()`: Creates an array with an internal buffer capacity for the specified length.

2. `new Uint8ClampedArray(length: u32)`: Creates an array with a buffer size matching the specified number of elements.

3. `new Uint8ClampedArray(buffer: &[JsValue], byte_offset: u32)`: Creates a view of the given buffer starting at the specified byte offset.

The constructor behaves similarly to other TypedArray constructors, with the same parameters and exceptions. Values can be initialized from:

- Another typed array

- An array-like object

- An ArrayBuffer with optional byte offset and length

- An iterable object

All constructor arguments are required to be used with the new keyword; attempting to call it without new throws a TypeError. The constructor supports basic polyfill functionality in older environments, ensuring compatibility across modern JavaScript implementations.


## Properties and Methods

The constructor creates a new typed array object representing a fixed-length raw binary data buffer, storing values as 8-bit unsigned integers. It supports five primary construction methods:

1. From a length: new Uint8ClampedArray(2)

2. From an array: new Uint8ClampedArray([21, 31])

3. From another TypedArray: new Uint8ClampedArray(x)

4. From an ArrayBuffer: new Uint8ClampedArray(buffer, 1, 4)

5. From an iterable: new Uint8ClampedArray((function* () { yield* [1, 2, 3]; })())

The constructor behaves similarly to other TypedArray constructors, with identical parameters and exception handling. Creating an instance without the new keyword results in a TypeError.

The array has two read-only properties:

- `byteOffset`: Represents the offset (in bytes) of the array from the start of its ArrayBuffer, set at construction time

- `length`: Represents the number of elements in the array, fixed at construction time

Instance methods include:

- `copyWithin(target, start, end)`: Copies a sequence of elements from start to end to target, with optional target offset

- `entries()`: Returns an iterator of index-item pairs for each element in the array

- `every(callback, thisArg)`: Tests if callback returns true for all elements

- `fill(value, start, end)`: Fills all elements with value, limited by start and end indices

- `filter(callback, thisArg)`: Returns a new array containing items where callback returns true

- `find(callback, thisArg)`: Returns the first item where callback returns true

- `findIndex(callback, thisArg)`: Returns the index of the found item, -1 if not found

- `forEach(callback, thisArg)`: Calls callback for each element

- `includes(searchElement)`: Determines if the array includes a certain element

- `indexOf(searchElement)`: Returns the first index of the element, or -1 if not found

- `join(separator)`: Joins all elements of the array into a string using separator

- `keys()`: Returns an iterator of keys for each index in the array

- `values()`: Returns an iterator of the array's items

The prototype methods closely follow ECMAScript 262 specifications, ensuring compatibility with standard array operations. All instance properties and methods are read-only except for the constructor reference, which remains the Uint8ClampedArray constructor.


## Browser Compatibility

Uint8ClampedArray is supported across multiple browsers and platforms, demonstrating broad compatibility. The array type, which represents 8-bit unsigned integers clamped to the range 0-255, is available in various environments, including desktop and mobile browsers, as well as Node.js environments.

Browser support begins with version 7 of Chrome for desktop, followed by Edge 12, Firefox 4, IE 10, Opera 11.6, and Safari 5.1. Mobile support includes Chrome 39 and later for Android, Edge 14 and later for Windows Phone, Firefox 52 and later for Android, Opera 26 and later for Android, and Safari 10 for iOS. For server-side JavaScript environments, Node.js versions 0.10 and later provide full support.

The constructor function, which creates typed array objects representing fixed-length binary data buffers, requires the use of the new keyword. Attempting to call it without new results in a TypeError, a behavior consistent with other TypedArray constructors. The constructor accepts multiple initialization methods, including creating an array from length, array, TypedArray, ArrayBuffer, or iterable objects, as demonstrated in examples from the core-js polyfill and MDN Web Docs.


## Key Differences from Other TypedArrays

While similar to other TypedArray types, Uint8ClampedArray introduces specific behavior for value assignments:

1. Value Clamping: Upon assignment, the array "clamps" values to the 0-255 range. Values less than 0 become 0, and values greater than 255 become 255. Non-integer values are rounded to the nearest integer before storage.

2. Element Size: Each element is an 8-bit unsigned integer, matching the constructor's implementation in JavaScript and Rust. This consistent element size differentiates it from other TypedArray types like Uint8Array and Uint16Array.

3. ArrayBuffer Access: The array provides direct access to its underlying ArrayBuffer via the `buffer` property, offering raw memory manipulation capabilities. This feature is consistent across TypedArray implementations but emphasizes Uint8ClampedArray's binary data handling.

The constructor method creates arrays with a fixed element size of 1 byte (8 bits), as defined by the `BYTES_PER_ELEMENT` property. However, the implementation details differ between environments:

- In JavaScript, the constructor accepts various initialization methods, including creating from length, array, TypedArray, ArrayBuffer, or iterable objects.

- The Rust implementation provides specific constructor methods for different initialization scenarios, such as creating from length, typed array, object, or ArrayBuffer with byte offset and length.

These differences in implementation detail further highlight the specialized nature of Uint8ClampedArray while maintaining consistency in core functionality across environments.

