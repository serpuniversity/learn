---

title: JavaScript TypedArray.prototype.reverse() Method

date: 2025-05-27

---


# JavaScript TypedArray.prototype.reverse() Method

JavaScript's TypedArray API extends the core Array functionality to specialized numeric data types, providing efficient storage and manipulation of binary data. The TypedArray.prototype.reverse() method offers an essential operation for array processing: reversing the order of elements in place. While array reversal seems straightforward, its implementation interacts intricately with JavaScript's typed array model, requiring careful handling of data types and buffer management. This article explores the reverse method's behavior across different typed array types, examines its compatibility with modern browsers, and highlights the key differences between its implementation on true typed arrays and array-like objects.


## Method Overview

The `TypedArray.prototype.reverse()` method reverses the elements of a typed array in place. This method modifies the original typed array directly, returning a reference to it rather than creating a new array.

The algorithm used by `reverse()` is the same as that of `Array.prototype.reverse()`, swapping the positions of elements from the beginning and end of the array until they meet in the middle. The method works with various typed array types, including Int32Array, Uint8Array, Uint8ClampedArray, Uint16Array, and Uint32Array.

When called on non-array objects, `reverse()` reads the length property and swaps indices between 0 and length / 2, deleting destination properties without corresponding source properties. This behavior differs from the method's implementation on actual typed arrays, which operates on the array's buffer and returns a new array. The original typed array's type and length are preserved during this process.


## Syntax and Usage

The `reverse()` method has the syntax `typedArray.reverse()`, taking no parameters. This method modifies the original typed array directly, returning a reference to the reversed array rather than creating a new one.

The method works by swapping the positions of elements from the beginning and end of the array until they meet in the middle. This same algorithm is used by the Array.prototype.reverse() method.

The `reverse()` method can be called on various typed array types, including Int32Array, Uint8Array, Uint8ClampedArray, Uint16Array, and Uint32Array. When called on non-array objects, it reads the length property and swaps indices between 0 and length / 2, deleting destination properties without corresponding source properties.

This method has been available since September 2016 across multiple devices and browser versions. It operates directly on the typed array's buffer and returns a reference to the original typed array, preserving its type and length properties.


## Supported TypedArray Types

The reverse method works with a variety of typed array types, including Int32Array, Uint8Array, Uint8ClampedArray, Uint16Array, and Uint32Array. These types store numbers in different formats based on their type:

- Unsigned integer arrays (Uint8Array, Uint16Array, Uint32Array) store numbers directly in binary format.

- Signed integer arrays (Int8Array, Int16Array, Int32Array) use two's complement representation.

- Floating-point arrays (Float16Array, Float32Array) use IEEE 754 format. Float32Array uses 23 bits for the mantissa and 8 bits for the exponent, while Float16Array uses 10 bits for the mantissa and 5 bits for the exponent.

When a TypedArray is created as a view of a resizable buffer, its size behaves differently based on construction method:

- Length-tracking arrays automatically resize to fit the underlying buffer as it is resized.

- Non-length-tracking arrays maintain their original size and require explicit resizing.

The method specifically works by swapping the positions of elements from the beginning and end of the array until they meet in the middle, with the first element becoming the last and vice versa. This same algorithm is used by the Array.prototype.reverse() method.


## Browser Compatibility

The reverse method can be called on any typed array instance and returns a new typed array containing the elements in reversed order. This behavior is consistent with the Array.prototype.reverse() method. The method's syntax is `typedArray.toReversed()`, and it takes no parameters.

The return value of the method is a new typed array containing the reversed elements. The method is not generic and can only be called on typed array instances. It is defined in the ECMAScript 2026 Language Specification, section sec-%typedarray%.prototype.toreversed.

The method demonstrates basic support across modern browsers, with the following implementations meeting the basic compatibility requirement:

- Chrome 110+ and Edge 110+ (Desktop and Mobile)

- Firefox 115+ and Safari 16+ (Desktop and Mobile)

- Chrome Android 110+, Firefox for Android 115+, and Safari on iOS 16+ (Mobile)

- Samsung Internet 21.0+ and WebView Android 110+ (Mobile and Server)

- Deno 1.31+ and Node.js 20.0.0+ (Server)

As with the reverse method, this implementation works across the latest devices and browser versions since July 2023. Modern applications can use this method to create new reversed typed arrays without modifying the original data structure.


## Reversing Non-typed Array Objects

When called on non-array objects, the `reverse()` method reads the `length` property and swaps indices between 0 and `length / 2`, deleting destination properties without corresponding source properties. This behavior differs from what happens with actual typed arrays, which operate on the array's buffer and return a new array while preserving the original's type and length properties.

The method works by iterating from the start of the array to the midpoint (excluding), swapping each element with its counterpart from the end of the array at the same distance. For example, if given an array of length 6, it would swap index 0 with index 5, index 1 with index 4, and index 2 with index 3.

This approach causes issues with arrays of even length, as the middle elements are swapped incorrectly. A simple in-place reversal function would need to account for this distinction, either by using a different midpoint calculation or handling even-length arrays separately.

The method's behavior on non-array objects demonstrates how JavaScript's language specification treats array-like objects versus true arrays, with methods implemented differently based on the object's constructed type and capabilities.

