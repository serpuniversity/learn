---

title: Uint16Array in JavaScript: A Comprehensive Guide

date: 2025-05-27

---


# Uint16Array in JavaScript: A Comprehensive Guide

JavaScript's Uint16Array provides a powerful tool for working with 16-bit unsigned integers, offering efficient memory management and performance optimizations through typed array capabilities. Understanding how to create, manipulate, and utilize Uint16Array objects is crucial for developers working with numerical data, binary structures, or performance-sensitive applications in modern JavaScript. This guide explores the fundamentals of Uint16Array creation, core methods, and browser support, helping developers harness this essential feature for efficient data processing in their projects.


## Introduction to Uint16Array

Uint16Array represents 16-bit unsigned integers in JavaScript and initializes its contents to 0. It provides several creation methods:

- `new Uint16Array(length)`: Creates an empty array of the specified length

- `new Uint16Array(typedArray)`: Creates a Uint16Array view of another typed array

- `new Uint16Array(object)`: Creates a Uint16Array from key-value pairs in an object

- `new Uint16Array(buffer, byteOffset, length)`: Creates a Uint16Array view of an ArrayBuffer with specified offset and length

The byte length of each element is 2, as defined by the static property `BYTES_PER_ELEMENT`. This array can be created from various sources, including another typed array, an ArrayBuffer, or an iterable object.

The constructor can only be called with the new keyword. Creating a Uint16Array from an object creates a new typed array using the same length as the source buffer. For example, if creating a Uint16Array from a buffer containing 4 'a' characters (0x61 = 97), the resulting array will contain four 97 values, demonstrating the two-byte per element storage.


## Creation Methods

new Uint16Array() creates a new Uint16Array object with default length 0. The constructor can be called with several parameters:

- Length: new Uint16Array(2) creates an empty Uint16Array with the specified length

- Array: new Uint16Array([21, 31]) creates a Uint16Array from an array of values

- TypedArray: new Uint16Array(x) creates a Uint16Array from another TypedArray

- ArrayBuffer: new Uint16Array(buffer) creates a Uint16Array from an ArrayBuffer

- Iterable: new Uint16Array((function* () { yield* [1, 2, 3]; })()) creates a Uint16Array from an iterable object

The constructor requires the new operator for construction, and calling it without new now throws a TypeError. The constructor takes no exceptions.

The Uint16Array can be created from various sources:

- Length: new Uint16Array(2)

- Array: new Uint16Array([21, 31])

- Another TypedArray: new Uint16Array(x)

- ArrayBuffer: new Uint16Array(buffer, 0, 4)

- Iterable: new Uint16Array((function* () { yield* [1, 2, 3]; })())

The constructor has five argument variants for creating TypedArray:

1. ArrayBuffer with optional byteOffset and length: new Uint16Array(buffer, 0, 4)

2. Array or array-like object for copying content: new Uint16Array([21, 31])

3. Another TypedArray for copying values: var y = new Uint16Array(x)

4. Numeric length for creating typed array of that many elements: new Uint16Array(2)

5. No arguments creates zero-length typed array: new Uint16Array()


## Core Methods and Properties

The Uint16Array prototype provides a suite of methods for array manipulation and iteration, including:

- Array iteration methods: forEach(), map(), filter(), some(), every()

- Searching methods: indexOf(), lastIndexOf()

- Mapping methods: entries(), keys(), values()

- Reordering methods: reverse()

- Element manipulation: fill(), set()

Element access follows standard array syntax with additional methods for bulk operations:

- copyWithin(target, start, end) - Copies a sequence of elements within the array

- subarray(begin, end) - Returns a new typed array view of a portion of the original array

- slice(start, end) - Returns a new array containing a portion of the original array

The array maintains its length and provides several read-only properties:

- buffer - Returns the ArrayBuffer referenced by the Uint16Array

- byteLength - Returns the length of the array in bytes

- byteOffset - Returns the offset from the start of the buffer in bytes

Additional properties include:

- BYTES_PER_ELEMENT - Returns the size in bytes of an item in the array (2 for Uint16Array)

- name - Returns the string "Uint16Array"

TypedArray inheritance includes standard methods for transforming binary data, such as:

- from(arrayLike) - Creates a new Uint16Array from an array-like or iterable object

- of(element1, element2, ...) - Creates a new Uint16Array with the specified elements

The array's operations are designed for efficient memory access and manipulation, with methods like set() allowing bulk data transfer between arrays. This makes Uint16Array particularly suitable for working with binary data structures and performing numerical computations in JavaScript.


## Typed Array Inheritance

Uint16Array inherits from TypedArray, inheriting properties and methods that define its behavior and functionality. Key inherited properties include:

- buffer: Returns the underlying ArrayBuffer that the view references

- byteOffset: Represents the offset, in bytes, of the view from the start of its buffer

- byteLength: Represents the length, in bytes, of the view

- length: Represents the number of elements in the array

TypedArray provides several utility functions for working with binary data, including static methods:

- from(arrayLike): Creates a new Uint16Array from an array-like or iterable object

- of(element1, element2, ...): Creates a new Uint16Array with the specified elements

The constructor property returns the Uint16Array constructor function, and the BYTES_PER_ELEMENT static property returns 2, indicating the storage size per element. This fixed-size attribute makes Uint16Array suitable for scenarios requiring precise memory management and performance optimizations.

Browser compatibility for Uint16Array started in Chrome 7, Firefox 4, and Safari 5.1, with broad support across modern desktop and mobile browsers. The constructor requires the new keyword for creation, and attempting to create a Uint16Array without new throws a TypeError, ensuring proper constructor usage and preventing common initialization errors.


## Browser Support and Polyfills

The Uint16Array constructor provides comprehensive support across modern desktop and mobile browsers, with full compatibility starting from Chrome 7, Edge 12, Firefox 4, and Safari 5.1. This includes both desktop and mobile versions of major browsers, with detailed support breakdowns for specific versions available through the official documentation.

The constructor requires the new keyword for creation, and attempting to create a Uint16Array without it will throw a TypeError. Support for creating from iterables began in Chrome 39, Edge 14, Firefox 52, and Safari 10, expanding the array's initialization capabilities.

For filling operations, while-loops demonstrate significantly better performance than the fill() method, particularly for lengths matching four-byte boundaries. An optimized approach for these cases uses a combination of Uint32Array and shared buffers to double the filling speed.

The typed array's properties and methods operate on a fixed byte size of 2 per element, making it particularly efficient for precise memory management and performance-critical applications. The core functionality, including the essential methods for data manipulation and array iteration, maintains consistent behavior across implementations, ensuring reliable cross-browser compatibility.

