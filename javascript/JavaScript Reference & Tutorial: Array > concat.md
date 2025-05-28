---

title: JavaScript Array concat Method

date: 2025-05-26

---


# JavaScript Array concat Method

JavaScript's array concat method provides a flexible way to merge multiple arrays and values into a single new array. This powerful utility creates shallow copies of the original arrays, preserving their structure while allowing developers to combine data from various sources. The method's widespread compatibility across modern browsers makes it a versatile tool for array manipulation in JavaScript applications.


## Syntax and Parameters

The concat() method returns a new array by merging two or more values/arrays. Its syntax is `arr.concat(value1, value2, ..., valueN)`, where `arr` is an array. The method can take an arbitrary number of arrays and/or values as arguments. It creates a new array and populates it with elements from the original array and any additional arguments, returning a new array without modifying the existing arrays.

The method supports merging with arrays, primitives, and array-like objects. When concatenating with primitives, the values are added as-is. For array-like objects with Symbol.isConcatSpreadable set to truthy, elements are added individually. The concat() method does not recurse into nested array arguments, creating a shallow copy of the original array. It preserves empty slots from source arrays and treats the this value and other arguments in the same way, working with plain objects and array-like objects.

The method has been widely supported across modern browsers since July 2015, with compatibility available on Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. The concat() method is particularly useful when dealing with non-array sources, as demonstrated in JavaScript's Array.prototype.myConcat implementation, where the method handles both arrays and non-array values effectively.


## Example Usage

Array concatenation in JavaScript operates through the `concat()` method, which merges two or more arrays into a new array without altering the original arrays. The method accepts multiple arguments, allowing the joining of one or more arrays and value inputs.

Basic usage involves simply passing arrays to be joined:

```javascript

let num1 = [11, 12, 13], num2 = [14, 15, 16], num3 = [17, 18, 19];

console.log(num1.concat(num2, num3)); // Output: [11, 12, 13, 14, 15, 16, 17, 18, 19]

```

It can also concatenate an array with individual values or other array-like objects:

```javascript

let alpha = ["a", "b", "c"];

console.log(alpha.concat(1, [2, 3])); // Output: ['a', 'b', 'c', 1, 2, 3]

```

The method processes nested arrays by creating a shallow copy, maintaining the original order and structure:

```javascript

let num1 = [[23]];

let num2 = [89, [67]];

console.log(num1.concat(num2)); // Output: [[23], 89, [67]]

```

The `concat()` method demonstrates robust compatibility across modern browsers, supported since July 2015 in Chrome, Edge, Firefox, Safari, and Opera. The method also handles non-array inputs effectively, as shown in the spread operator comparison where it maintains array structure when merging with nested arrays.


## Common Pitfalls

The concat method creates a new array rather than modifying the original arrays, making it distinct from the push method. While both methods can be used to combine arrays, push directly modifies the existing array and returns its new length, while concat returns a new array without altering the originals.

When working with nested arrays, concat creates a shallow copy, preserving the original structure and gaps. The method handles various input types - merging arrays, adding primitives, and working with array-like objects. For merging arrays with different data types, concat allows combining arrays containing numbers, strings, and other values into a single new array.

The method is particularly useful when implementing pure functions, as it avoids side effects by producing a new array rather than modifying existing ones. This behavior aligns with functional programming principles, where functions should not alter their input arguments.

While the method works similarly to other array operations, it can behave differently when used within loops. For example, when using a for loop to merge arrays, concat requires saving the result to a variable or returning it, as opposed to push, which directly modifies the array being referenced. This difference in behavior is crucial for developers working with array manipulation in JavaScript.


## Browser Support

Supported in all modern browsers, the Array.prototype.concat method has demonstrated compatibility across multiple devices and browser versions since its implementation in July 2015. The method works seamlessly with Chrome, Edge, Firefox, Safari, and Opera, providing developers with reliable array merging capabilities across these major browsers.

The implementation closely follows ECMAScript 2026 Language Specification, which defines the method's behavior. As noted by MDN Web Docs, the method creates a new `Array` instance through its syntax `concat(value1), concat(value1, value2), concat(value1, value2, ...)` where `value1`, `value2`, ..., `valueN` are optional arguments representing arrays or values to be added to the given array.

The method's behavior aligns with its non-modifying nature, returning a new array without altering the original arrays. This functionality allows developers to create pure functions that produce new data structures without side effects. The method gracefully handles various input types, merging arrays, adding primitives, and working with array-like objects while maintaining reference retention with nested arrays.

