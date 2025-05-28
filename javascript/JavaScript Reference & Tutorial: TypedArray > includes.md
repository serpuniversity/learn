---

title: JavaScript TypedArray includes Method

date: 2025-05-27

---


# JavaScript TypedArray includes Method

The includes() method for JavaScript TypedArray instances offers a powerful way to search for values within numeric arrays. Whether you're working with simple integers or complex floating-point numbers, this method provides the flexibility and accuracy you need to locate specific values efficiently. This article will explore how TypedArray.includes works, including its parameter requirements, value comparison rules, and special handling for floating-point NaN values. You'll learn how to use this method effectively for both standard and floating-point arrays, and understand how it interacts with different TypedArray types and JavaScript environments.


## Method Signature and Parameters

The includes() method of TypedArray instances determines whether a typed array includes a certain value among its entries, returning true or false as appropriate. This method works similarly to Array.prototype.includes() and follows the SameValueZero algorithm for value comparisons, where values of zero are all considered to be equal regardless of sign, but false is not considered the same as 0. NaN values are specifically handled for Float32 and Float64 arrays, with new Uint8Array([NaN]).includes(NaN) returning false while both new Float32Array([NaN]).includes(NaN) and new Float64Array([NaN]).includes(NaN) return true.

The method has two parameters: searchElement (the value to search for) and fromIndex (the optional zero-based index at which to start searching, converted to an integer). The method returns a boolean value which is true if the value searchElement is found within the typed array (or the part of the typed array indicated by the index fromIndex, if specified).

The implementation has different behaviors based on the receiver type (Array vs. TypedArray) and provides flexibility in browser support and implementation across different JavaScript environments. The method is supported in Chrome 47, Edge 14, Firefox 43, Opera 34, Safari 10, and their mobile versions, as well as Node.js 6.0.0 and later. Compatibility with other environments can be extended through polyfills, such as the one provided in core-js.

The method's syntax allows for two usage patterns: includes(searchElement) for searching the entire array, and includes(searchElement, fromIndex) for specifying a starting position. When both parameters are provided, the method searches for the searchElement starting from the specified fromIndex within the typed array. The fromIndex parameter can be negative to count back from the end of the array, with an effective range of -array.length <= fromIndex < array.length. If fromIndex is not provided or is less than -array.length, it defaults to 0, causing the entire array to be searched.


## Method Behavior and Algorithm

When both parameters are provided (searchElement and fromIndex), the method searches for the searchElement starting from the specified fromIndex within the typed array, returning true if found and false otherwise. The method works similarly to Array.prototype.includes(), using the SameValueZero algorithm for value comparisons, where values of zero are all considered to be equal regardless of sign, but false is not considered the same as 0. The implementation supports the full range of valid indices, including negative indices that count back from the end of the array.

The method returns false when the specified searchElement is not found within the typed array. For example, calling includes(20) on a Uint8Array with values [10, 40, 30, 50, 80, 100] would return false. It returns true when the searchElement is found, as seen in the example where includes(4) on a Uint8Array with values [1, 2, 3, 4, 5, 6, 7, 8] returns true. When both searchElement and fromIndex parameters are passed, the method starts searching for the searchElement from the specified fromIndex position, as demonstrated with a Uint8Array containing [1, 2, 3, 5, 7, 9, 6, 8, 11, 15] where searching for 2 starting from index 3 returns false.


## Special Cases and Considerations


### Special Cases and Considerations

The includes() method handles special cases for Float32 and Float64 arrays regarding NaN values. For instance, new Uint8Array([NaN]).includes(NaN) returns false, since the NaN passed to the constructor gets converted to 0. However, both new Float32Array([NaN]).includes(NaN) and new Float64Array([NaN]).includes(NaN) return true. This behavior demonstrates how the method treats NaN values specifically for floating-point arrays.


### Browser Support and Implementation

The method provides flexibility across different JavaScript environments through robust browser support. It is fully implemented in Chrome 47, Edge 14, Firefox 43, Opera 34, Safari 10, and compatible versions for mobile devices and Node.js environments. Implementation details allow optimization based on the receiver type, supporting both Array and TypedArray instances through distinct function implementations. This structure enables efficient shared function implementations across array types while maintaining flexibility in browser support and cross-environment compatibility.


## Common Usage Examples

The includes() method works similarly across different typed array types, including Uint8Array, Float32Array, and their respective variants. For instance, checking new Uint8Array([10, 40, 30, 50, 80, 100]).includes(20) returns false, while new Uint8Array([1, 2, 3, 5, 7, 9, 6, 8, 11, 15]).includes(4) returns true.

When combined with the fromIndex parameter, the method provides flexible searching capabilities. For example, with a Float32Array new Float32Array([3.14, 2.71, 1.61]), calling includes(2.71, 1) returns true, demonstrating the method's ability to start searching from a specific index.

The method's implementation handles various data types efficiently, as shown with a Float32Array([1.1, 2.2, 3.3]).includes(2.2) returning true. Similarly, a Uint8Array([65, 66, 67]).includes(66) returns true, illustrating its compatibility with different typed array implementations.


## Performance and Optimization

The JavaScript TypedArray includes method demonstrates optimization possibilities based on receiver type (Array vs. TypedArray) through various implementation details. Notably, the spec allows optimization where intermediate writes remain invisible for both Array and TypedArray receivers, enabling efficient implementation across different JavaScript environments.

When comparing Array.from and TypedArray.from methods, regular arrays can pre-instantiate the new array and dynamically adjust its length, while TypedArrays require accurate determination of the number of elements at instantiation time. This difference affects algorithmic details and implementation strategies.

The ES6 specification references the same algorithm for both Arrays and TypedArrays where applicable, allowing implementations to share the same code level between functions while maintaining distinct implementations if desired. Modern JavaScript engines perform function optimizations based on receiver and argument types, and the author suggests that differentiating function objects introduces unnecessary complexity.

For TypedArray constructors, the implementation requires careful handling of various input types. When called with an object that's not a TypedArray instance, a new typed array is created using the TypedArray.from method. If called with a non-object, the parameter treats the number as the length of the typed array. Implementation details include creating an internal array buffer of the specified size, filled with zeros, and handling exceptions for invalid inputs such as TypeError and RangeError.

The TypedArray constructor uses a Symbol.species property to create derived objects, while subclasses have static properties like BYTES_PER_ELEMENT to return the element size. When creating views from ArrayBuffer or SharedArrayBuffer instances, the implementation handles byteOffset and length parameters to specify the memory range. This process ensures correct length determination and proper memory access for all TypedArray subclasses.

