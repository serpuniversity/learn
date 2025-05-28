---

title: JavaScript TypedArray.prototype.slice()

date: 2025-05-27

---


# JavaScript TypedArray.prototype.slice()

JavaScript's `TypedArray.prototype.slice()` method provides a powerful tool for extracting subsets of typed array data. This introduction examines the method's implementation, behavior, and compatibility across JavaScript environments, highlighting its role in consistent array manipulation across different typed array types. By understanding how `slice()` operates, developers can efficiently work with typed arrays while maintaining consistent array manipulation patterns.


## Method Overview

The `TypedArray.prototype.slice()` method returns a copy of a portion of a typed array as a new typed array object. It follows the same algorithm as `Array.prototype.slice()` and shares similar behavior patterns. The method accepts two optional parameters: `start` and `end`, which represent the zero-based indices for extracting elements from the original array.

The `start` parameter determines the index at which to begin extraction. It can accept both positive and negative integer values, with negative indices calculating from the end of the array. The `end` parameter specifies the index before which to end extraction, also accepting positive and negative integers. The extracted elements extend up to but do not include the end index.


### Syntax and Parameters

The method follows this syntax:

```javascript

typedarray.slice([begin[, end]])

```

Where:

- `begin` (optional) is the starting index for extraction. Negative values are supported, representing positions relative to the end of the array.

- `end` (optional) is the ending index for extraction, where extraction stops but is not included in the result. Negative values are also supported.


### Return Value

The method returns a new typed array containing the extracted elements. The returned array maintains the same element type and buffer as the original array but represents a subset of its elements.


### Implementation Details

The `slice` method does not modify the original typed array. Instead, it creates a shallow copy of the requested portion. This implementation provides consistent behavior with `Array.prototype.slice()`, ensuring compatibility with existing JavaScript patterns and algorithms.


## Parameters and Return Value

The `TypedArray.prototype.slice()` method returns a copy of a portion of a typed array as a new typed array object. The method accepts two parameters: `start` and `end`, which represent the zero-based indices for extracting elements from the original array. Both `start` and `end` can accept positive and negative integer values, with negative indices calculating from the end of the array.

The `start` parameter determines the index at which to begin extraction and is optional, with a default value of 0 if not provided. The `end` parameter specifies the index before which to end extraction and is also optional, with a default value of the original array's length. The extracted elements extend up to but do not include the end index, meaning the resulting array has elements from the start index up to the position immediately before the end index.


### Implementation Behavior

The `slice` method creates a shallow copy of the requested portion of the typed array, rather than modifying the original array. This behavior aligns with the implementation of `Array.prototype.slice()`, ensuring consistency with existing JavaScript patterns and algorithms. The method does not alter the original typed array, maintaining the immutability principle common to JavaScript array operations.


### Example Usage

The following example demonstrates using `slice()` with both positive and negative indices:

```javascript

var uint8 = new Uint8Array([1,2,3]);

uint8.slice(1); // Uint8Array [ 2, 3 ]

uint8.slice(2); // Uint8Array [ 3 ]

uint8.slice(-2); // Uint8Array [ 2, 3 ]

uint8.slice(0,1); // Uint8Array [ 1 ]

```

This implementation provides flexibility in array manipulation while maintaining the performance and memory efficiency expected in typed array operations.


## Method Implementation

The implementation of `TypedArray.prototype.slice()` closely mirrors that of `Array.prototype.slice()`, sharing the same algorithm and behavior patterns. Introduced in September 2016, this method provides consistent array manipulation capabilities across devices.

The method accepts two parameters: `start` and `end`, representing the zero-based indices for extracting elements from the original array. Both parameters can accept positive and negative integer values, with negative indices calculating from the end of the array. The `start` parameter determines the index at which to begin extraction and is optional, with a default value of 0 if not provided. The `end` parameter specifies the index before which to end extraction and is also optional, with a default value of the original array's length. The extracted elements extend up to but do not include the end index.

Crucially, the `slice` method creates a shallow copy of the requested portion of the typed array, rather than modifying the original array. This maintains the immutable property common to JavaScript array operations while preserving the efficiency of typed array manipulations. When a new element is added to either the original or copied array, the other remains unaffected.


## Polyfill Example

The polyfill for Node v0.12 implements the `slice` method for TypedArray objects by delegating to the native `Array.prototype.slice()` method. This approach ensures compatibility with older Node versions while maintaining the expected behavior of array slicing.

The polyfill is available via npm and can be installed with the command `npm install typedarray-slice`. It's designed to be simple, requiring no explicit export and only adding the `slice` method to TypedArray prototypes.

While the original polyfill implementation used the `subarray` method to create a live view of the array, the modern polyfill for Node v0.12 instead creates a shallow copy of the requested portion. This ensures that the sliced array maintains the same type as the original array, preserving the specific TypedArray semantics.


### Implementation Details

The polyfill's implementation mirrors that of the native `Array.prototype.slice()` method, including handling for both positive and negative indices. It correctly implements the algorithm where the second parameter represents the end index (not the length), as documented in MDN Web Docs.

The polyfill handles cases where the start index is greater than or equal to the end index by returning an empty array. This ensures consistent behavior with the native implementation, which also returns an empty array in such cases.


### Browser Compatibility

The polyfill maintains compatibility with Node versions 0.10 and 4+, which already contained functional `slice` implementations. This wide compatibility range ensures that developers using older versions of Node can use the polyfill without additional complexity.


### Example Usage

The polyfill can be used in applications requiring TypedArray slicing across different Node versions. The following example demonstrates its usage:

```javascript

const TypedArraySlice = require('typedarray-slice');

const uint8 = new Uint8Array([1, 2, 3]);

console.log(uint8.slice(1)); // Uint8Array [ 2, 3 ]

console.log(uint8.slice(2)); // Uint8Array [ 3 ]

console.log(uint8.slice(-2)); // Uint8Array [ 2, 3 ]

console.log(uint8.slice(0, 1)); // Uint8Array [ 1 ]

```


## Behavior Differences

The `slice()` method in JavaScript TypedArray instances differs from regular arrays in how it interprets the second parameter. Unlike `Array.prototype.slice()`, which uses the second parameter as the length of the slice, TypedArray's `slice()` treats this parameter as an ending index. This difference in interpretation affects how slicing operations behave, particularly when working with multiple elements or iterating through large arrays.

The method's handling of indices extends these differences further. While both array types support both positive and negative indexing, TypedArray's implementation of negative indices operates from the end of the array. This behavior is consistent across all TypedArray types and is reflected in the method's algorithm, which clamps negative indices during computation.

These implementation details impact how developers interact with TypedArray instances, especially when performing operations that involve multiple slices or conversions between different array representations. Understanding these differences is crucial for developers working with typed arrays across different JavaScript environments and versions, particularly when implementing polyfills or extending array functionality.

