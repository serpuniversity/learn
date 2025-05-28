---

title: JavaScript Int16Array: Reference & Tutorial

date: 2025-05-26

---


# JavaScript Int16Array: Reference & Tutorial

Working with binary data in JavaScript has become increasingly important as web applications handle more complex tasks, from game development to real-time data processing. While JavaScript traditionally operates on text and objects, the language has evolved to include typed arrays, which allow efficient manipulation of binary data structures. The Int16Array constructor, introduced in ECMAScript 6, represents a significant advancement in this area, specifically designed for handling 16-bit signed integers.

This article explores the capabilities of Int16Array, starting with its basic functionality and initialization methods. We'll examine how it stores and represents data, particularly noting its default use of platform-native byte order (Little Endian). The article then delves into the core methods and properties of Int16Array, demonstrating how to manipulate and access 16-bit integers efficiently.

We'll also cover more advanced topics, including conversion between typed arrays and buffers, and the array methods that enable sophisticated data operations. Whether you're developing games, implementing real-time data processing, or working with binary file formats in the browser, the Int16Array provides powerful tools for handling 16-bit signed integers in JavaScript.


## Introduction to Int16Array

The Int16Array constructor creates typed arrays of 16-bit signed integers, a feature introduced in ECMAScript 6 (ECMA-262). By default, these arrays are initialized to 0, providing an efficient way to represent and manipulate 16-bit integers in JavaScript.

The constructor supports multiple initialization methods:

- From length: new Int16Array(2) creates an array with two elements, each 2 bytes in size.

- From array: new Int16Array([21, 31]) creates an array from an existing array of values.

- From TypedArray: var x = new Int16Array([21, 31]); var y = new Int16Array(x) copies values from one Int16Array to another.

- From ArrayBuffer: var buffer = new ArrayBuffer(8); var z = new Int16Array(buffer, 0, 4) initializes an array from a buffer with 4 elements.

The constructor syntax and parameters are designed to be flexible, allowing for various initialization approaches. All constructors return an Array Iterator object containing the values for each index in the array, with the initial value of the @@iterator property matching the values property.


### Data Representation and Byte Order

Int16Array stores data in platform-native byte order, which is Little Endian by default. This means that for the value 654456543456, the array would represent it as [6, 5, 4, 4, 5, 6, 5, 4, 3, 4, 5, 6]. However, if you need control over byte order, it's recommended to use DataView instead.


### Byte Offset and Length Properties

Each Int16Array instance has two read-only properties: byteOffset, which represents the offset (in bytes) of the array from the start of its ArrayBuffer, and length, which represents the number of elements in the array. These properties allow developers to understand and manipulate the array's position within its underlying buffer.


### Array Methods

The Int16Array provides several essential methods for data manipulation and access:

- from() creates a new Int16Array from an array-like or iterable object.

- sort() sorts the elements of the array in place and returns the array.

- subarray() returns a new TypedArray on the same ArrayBuffer store with the same element types.

- values() returns a new Array Iterator object that contains the values for each index in the array.

- copyWithin() copies a sequence of array elements within the array.

- fill() fills all elements of the array from a start index to an end index with a static value.

These methods provide a robust foundation for working with 16-bit signed integers in JavaScript, offering both efficient data manipulation and convenient access patterns.


## Constructor and Initialization

The Int16Array constructor creates typed arrays of 16-bit signed integers using the platform's native byte order. The constructor supports several initialization methods for creating these arrays:

1. From Length: new Int16Array(2) creates an array with two elements, each 2 bytes in size, initialized to 0.

2. From Array: new Int16Array([21, 31]) creates an array from an existing array of values.

3. From TypedArray: var x = new Int16Array([21, 31]); var y = new Int16Array(x) copies values from one Int16Array to another.

4. From ArrayBuffer: var buffer = new ArrayBuffer(8); var z = new Int16Array(buffer, 0, 4) initializes an array from a buffer with 4 elements.

The constructor returns an Array Iterator object containing the values for each index in the array. The initial value of the @@iterator property is the same function object as the initial value of the values property.

The constructor takes up to three parameters: object, buffer, and byteOffset. For example, new Int16Array(buffer, byteOffset, length) creates an array from an ArrayBuffer with a specified byte offset and length. It also supports the following static properties: BYTES_PER_ELEMENT (which returns 2), length (static property with value 3), name (returns "Int16Array"), and prototype properties for the constructor function, buffer, byteLength, and byteOffset.

The constructor throws exceptions for invalid usage, including TypeError when called without the 'new' keyword, RangeError when length is negative, byteOffset is negative or greater than the buffer size, or length exceeds the buffer size. These constraints ensure proper initialization while maintaining the integrity of the underlying ArrayBuffer.


## Core Methods and Properties

The Int16Array prototype inherits from %TypedArray%.prototype and includes several key properties for understanding and manipulating the array's structure:

- `constructor`: Returns the Int16Array constructor function

- `buffer`: A read-only property representing the ArrayBuffer referenced by the Int16Array

- `byteLength`: A read-only property representing the length (in bytes) of the Int16Array from the start of its ArrayBuffer

- `byteOffset`: A read-only property representing the offset (in bytes) of the Int16Array from the start of its ArrayBuffer

- `length`: A read-only property representing the number of elements in the Int16Array

The prototype also includes essential methods for array manipulation:

- `copyWithin()`: Copies the sequence of array elements within the array to the position starting at target. The copy is taken from the index positions of the second and third parameters, respectively.

- `entries()`: Returns a new Array Iterator object that contains key/value pairs for each index in the array

- `every()`: Tests whether all elements in the array pass a provided function

- `fill()`: Fills all elements of the array from a start index to an end index with a static value

- `filter()`: Creates a new array consisting of elements that pass a test implemented by the provided function

- `find()`: Returns the value of the first element in the array that passes a test implemented by the provided function

- `findIndex()`: Returns the index of the first element in the array that passes a test implemented by the provided function

- `flatMap()`: Applies a provided transformation function to each element of this array and returns the resulting array

- `forEach()`: Calls a provided function once for each array element

- `includes()`: Determines whether an array includes a certain element, returning true or false as appropriate

- `indexOf()`: Returns the first index at which a given element can be found in the array, or -1 if it is not present

- `join()`: Returns a string created by concatenating all of the elements in an array, separated by commas or a specified separator string

- `keys()`: Returns a new Array Iterator object that contains the keys for each index in the array

- `lastIndexOf()`: Returns the last index at which a given element can be found in the array, or -1 if it is not present

- `map()`: Creates a new array populated with the results of calling a provided function on every element in the calling array

- `pop()`: Removes the last element from an array and returns that element

- `push()`: Adds new elements to the end of an array and returns the new length of the array

- `reverse()`: Reverses the elements of an array in place

- `shift()`: Removes the first element from an array and returns that element

- `slice()`: Returns a section of an array as a new array

- `some()`: Returns true if any element of the array satisfies the provided testing function

- `sort()`: Sorts the elements of an array in place and returns the array

- `splice()`: Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements

- `toLocaleString()`: Returns a localized string representing the array and its elements

- `toString()`: Returns a string representing the array and its elements

- `values()`: Returns a new array iterator object that contains the values for each index in the array

- `with()`: Returns a new typed array with the element at the index replaced with the specified value


## Data Operations and Manipulation


### Array Manipulation Methods

The Int16Array provides several methods for efficient data manipulation, including:

- `copyWithin()`: Copies a sequence of array elements within the array to the position starting at target. This method is particularly efficient for large datasets, as it performs the copy operation directly within the underlying buffer.

- `set()`: Sets multiple typed array indices at once using data from another array or typed array. This method can be significantly more efficient for fast memory moves when the source and destination arrays share the same underlying buffer.

- `subarray()`: Creates a new typed array view referencing the same buffer with a narrower span. This allows developers to work with specific sections of the original array without duplicating data.


### Array Access and Modification

Int16Array elements can be accessed using standard array index notation, which retrieves corresponding bytes from the underlying buffer and interprets them as 16-bit integers. Bracket notation returns `undefined` for out-of-bounds indices without accessing the object, and attempts to write to such properties have no effect.

When viewing a resizable buffer, typed arrays automatically resize to fit the underlying buffer when resized. This behavior ensures that all typed array views remain valid and up-to-date with changes to the buffer's size.

The prototype inherits from `%TypedArray%.prototype` and includes essential properties for understanding the array's structure:

- `buffer`: A read-only property representing the ArrayBuffer referenced by the Int16Array

- `byteLength`: A read-only property representing the length (in bytes) of the Int16Array from the start of its ArrayBuffer

- `byteOffset`: A read-only property representing the offset (in bytes) of the Int16Array from the start of its ArrayBuffer

- `length`: A read-only property representing the number of elements in the Int16Array


### Conversion Between Typed Arrays and Buffers

Int16Array instances can easily convert between typed arrays and buffers using several methods:

- The constructor can take an ArrayBuffer, byte offset, and length to create a typed array view of a specific portion of the buffer.

- The `buffer` property returns the underlying ArrayBuffer, allowing direct access to the raw binary data.

- The `byteLength` and `byteOffset` properties provide information about the array's position within the buffer, enabling precise data manipulation.

These capabilities make the Int16Array a powerful tool for working with binary data in JavaScript, offering both efficiency and flexibility in data representation.


## Iteration and Representation

The Int16Array provides multiple access patterns for its contents, offering both standard array indexing and specialized methods for iteration. Developers can retrieve elements using standard array index notation, which interprets bytes from the underlying buffer as 16-bit integers. Out-of-bounds index accesses return `undefined`, and attempts to write to non-existent indices have no effect.

The array includes several built-in methods for iteration and data access:

- `copyWithin()`: Copies a sequence of array elements within the array to a specified target position.

- `entries()`: Returns a new Array Iterator object containing key/value pairs for each index in the array.

- `every()`: Tests whether all elements in the array pass a provided function.

- `fill()`: Fills all elements of the array from a start index to an end index with a static value.

- `filter()`: Creates a new array consisting of elements that pass a test implemented by the provided function.

- `find()`: Returns the value of the first element in the array that passes a test implemented by the provided function.

- `findIndex()`: Returns the index of the first element in the array that passes a test implemented by the provided function.

- `forEach()`: Calls a provided function once for each array element.

- `includes()`: Determines whether an array includes a certain element, returning true or false as appropriate.

- `indexOf()`: Returns the first index at which a given element can be found in the array, or -1 if it is not present.

- `keys()`: Returns a new Array Iterator object that contains the keys for each index in the array.

- `lastIndexOf()`: Returns the last index at which a given element can be found in the array, or -1 if it is not present.

- `map()`: Creates a new array populated with the results of calling a provided function on every element in the calling array.

- `pop()`: Removes the last element from an array and returns that element.

- `push()`: Adds new elements to the end of an array and returns the new length of the array.

- `reverse()`: Reverses the elements of an array in place.

- `shift()`: Removes the first element from an array and returns that element.

- `slice()`: Returns a section of an array as a new array.

- `some()`: Returns true if any element of the array satisfies the provided testing function.

- `sort()`: Sorts the elements of an array in place and returns the array.

- `splice()`: Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

- `toLocaleString()`: Returns a localized string representing the array and its elements.

- `toString()`: Returns a string representing the array and its elements.

- `values()`: Returns a new array iterator object that contains the values for each index in the array.

These methods offer flexible and efficient ways to manipulate and access Int16Array data, making them suitable for both simple and complex operations on 16-bit signed integer arrays.

