---

title: Int32Array: JavaScript's 32-bit Signed Integer Array

date: 2025-05-26

---


# Int32Array: JavaScript's 32-bit Signed Integer Array

JavaScript's Int32Array provides efficient storage and manipulation of 32-bit signed integers, with native support across modern browsers and Node.js environments. This article explores the array's properties, constructor syntax, and methods for working with integer data in typed arrays.


## Overview of Int32Array

The `Int32Array` stores 32-bit signed integers, providing efficient memory management for handling large sets of numbers. Each element occupies 4 bytes of memory, with a value range from -2,147,483,648 to 2,147,483,647. It is a subclass of the hidden `TypedArray` class and inherits properties like `BYTES_PER_ELEMENT`, which returns the size of an element (4 bytes).

The constructor allows creating arrays in several ways: from length, another typed array, or an object. Additionally, it supports creating views of ArrayBuffer with byte offset and length parameters. Once created, elements can be accessed using standard array index notation or the object's methods.

The array provides several useful methods for data manipulation and analysis. These include `copyWithin` for copying sequences within the array, `entries` for returning key/value pairs, `every` for testing all elements, and `fill` for setting all elements to a static value. The prototype also offers methods like `slice` for creating subarrays, `some` for checking conditions, and `sort` for ordering elements. Each method is designed to work efficiently with the underlying binary data structure.


## Creating Int32Array Instances

The constructor requires the `new` keyword to be used, and attempting to call it without `new` results in a TypeError. The syntax includes several variations:

1. **From Length:** `new Int32Array(length)`

   ```javascript

   const int32 = new Int32Array(2);

   int32[0] = 42;

   console.log(int32[0]); // 42

   console.log(int32.length); // 2

   console.log(int32.BYTES_PER_ELEMENT); // 4

   ```

2. **From Array:** `new Int32Array(array)`

   ```javascript

   const x = new Int32Array([21, 31]);

   console.log(x[1]); // 31

   ```

3. **From TypedArray:** `new Int32Array(array)`

   ```javascript

   const y = new Int32Array(x);

   console.log(y[0]); // 21

   ```

4. **From ArrayBuffer:** `new Int32Array(buffer [, byteOffset [, length]])`

   ```javascript

   const buffer = new ArrayBuffer(32);

   const z = new Int32Array(buffer, 4, 4);

   console.log(z.byteOffset); // 4

   ```

5. **From Iterable:** `new Int32Array(iterable)`

   ```javascript

   const iterable = (function* () { yield* [1, 2, 3]; })();

   const int32FromIterable = new Int32Array(iterable);

   console.log(int32FromIterable); // Int32Array [1, 2, 3]

   ```

Each method returns a new Int32Array object with the specified initialization data. The constructor initializes the array to zeros unless explicit initialization data is provided. The constructor syntax and parameters are consistent with other TypedArray subclasses, including support for ArrayBuffer and typed array objects.


## Int32Array Methods and Properties

The Int32Array prototype provides several methods that extend its functionality, including powerful iteration capabilities and data manipulation tools. The `copyWithin` method efficiently copies sequences of array elements within the array, while `entries` returns a new Array Iterator object containing key/value pairs for each index.

The `every` method tests whether all elements in the array pass a provided function, allowing for conditional checks across the entire dataset. The `fill` method sets all elements of the array to a static value, providing a quick way to initialize or reset array contents. Additional methods include `slice` for creating subarrays, `some` for checking conditions on elements, and `sort` for ordering elements.

For developers working with typed arrays, the `set` method stands out for its efficiency in setting multiple typed array indices at once using data from another array or typed array. When the two typed arrays share the same underlying buffer, this operation can be particularly efficient, performing a fast memory move rather than individual assignments.

The `byteOffset`, `length`, and `BYTES_PER_ELEMENT` properties offer insight into the array's memory layout. The `byteOffset` property indicates the offset (in bytes) of the array from the start of its ArrayBuffer, while `length` represents the number of elements in the array. Each element occupies 4 bytes of memory, as defined by the `BYTES_PER_ELEMENT` property.

These properties and methods enable developers to work efficiently with 32-bit signed integer data in JavaScript, combining powerful data manipulation tools with direct memory access for performance-critical applications.


## Working with ArrayBuffer and Views

The Int32Array constructor creates typed arrays of 32-bit signed integers, initializing the array's contents to zero unless otherwise specified. The constructor's syntax offers multiple initialization options, including creating arrays from length, another typed array, an object, or an ArrayBuffer with optional byteOffset and length parameters.

When creating views of an ArrayBuffer, the `byteOffset` must be a multiple of 4, and the length must be an integer number of 32-bit elements. The underlying buffer can be accessed through the `.buffer` property, while `.byteLength` returns the total byte count, and `.byteOffset` indicates the array's starting position within the buffer.

The `INT32Array` class shares most methods with the general `TypedArray` class, including `copyWithin`, `entries`, `every`, and `fill`, but lacks the `flat`, `concat`, and `flatMap` methods due to its structure. It implements the Array iterator protocol through its `@@iterator` and `values` properties, allowing foreach loops and array methods like `includes`.

For developers needing more complex data manipulation, the `DataView` class provides a flexible alternative. This class enables direct memory operations through getter and setter methods, supporting both big-endian and little-endian byte orders. The `DataView` can read and write integers, floats, and other data types from any byte offset within an ArrayBuffer, offering precise control over binary data operations.


## Browser and Node.js Support

The Int32Array constructor provides full support across major browsers and Node.js starting from specific versions:


### Desktop Browsers

- Chrome: Version 7 and above

- Edge: Version 12 and above

- Firefox: Version 4 and above

- Internet Explorer: Version 10 and above

- Opera: Version 11.6 and above

- Safari: Version 5.1 and above

- WebView Android: Version 4 and below

- Chrome Android: Version 18 and above

- Firefox Android: Version 4 and above

- Opera Android: Version 12 and above

- Safari iOS: Version 4.2 and above

- Samsung Internet: Version 1.0 and above

- Node.js: Version 0.10 and above


### Mobile Browsers

- Chrome: Version 7 and above

- Edge: Version 12 and above

- Firefox: Version 4 and above

- Internet Explorer: Version 10 and above

- Opera: Version 11.6 and above

- Safari: Version 5.1 and above

- WebView Android: Version 4 and below

- Chrome Android: Version 18 and above

- Firefox Android: Version 44 and above

- Opera Android: Version 14 and above

- Safari iOS: Version 5 and above

- Samsung Internet Android: Version 1.0 and above

- Node.js: Version 0.12 and above


### Compatibility Notes

The constructor requires the `new` operator, as specified in ECMAScript 2015. Attempting to call it without `new` results in a TypeError exception. While the constructor has been widely implemented since July 2015, developers should ensure compatibility when targeting older versions of browsers and Node.js environments.

