---

title: JavaScript's flatMap Method: Mapping and Flattening Arrays

date: 2025-05-26

---


# JavaScript's flatMap Method: Mapping and Flattening Arrays

The flatMap method in JavaScript merges mapping and flattening operations into a single, efficient step. This powerful array manipulation tool was introduced in ES2019 and offers significant performance advantages over separate map and flat methods. Our exploration examines how flatMap works, its browser support, and provides practical examples of its implementation.


## flatMap Method Overview

The flatMap method in JavaScript combines mapping and flattening operations on arrays, serving as a more efficient alternative to separate map and flat methods. This functionality was added to JavaScript in ES2019 (ECMAScript 10) and is fully supported in modern browsers including Chrome, Edge, Firefox, Opera, and Safari.


### How flatMap Works

The method operates by first applying a mapping function to each element of the source array. This mapping function can return either an array or a non-array value. If it returns an array, these arrays are then flattened into a single resulting array. Importantly, flatMap only performs a single level of flattening—it reduces the depth of the resulting array by one level.


### Example Usage

```javascript

let numbers = [1, 2, 3, 4, 5];

let resultingArray = numbers.flatMap((element) => element + 1);

console.log(resultingArray); // [2, 3, 4, 5, 6]

```

In this example, the mapping function adds 1 to each element. The resulting array contains the transformed values without any additional nesting.


### Browser Support and Polyfills

flatMap functionality is widely supported in modern browsers as of January 2020 (Chrome 69, Edge 79, Firefox 62, Safari 12, Opera 56). For environments where the method is not natively supported or required to maintain compatibility with older browsers, polyfills are available through various libraries and frameworks. These polyfills enable the same functionality by combining manual mapping and flattening operations.


## Array flatMap Implementation

The Array.prototype.flatMap method combines the functionality of map and flat in a single operation. It returns a new array formed by applying a callback function to each element of the input array and then flattening the result by one level.

Implementations of the flatMap method vary in their specific approach while maintaining the core functionality. For array operations, the method maps each element using the provided callback function and flattens the result. Strings require additional handling as they are rejected by the flatMap method; two workarounds are to wrap the string in an array or use Iterator.from to convert it properly.

The native implementation supports a flexible callback function that receives the current value, its index, and the array itself as arguments, though the array parameter is optional. This flexibility allows for complex transformations beyond simple value modifications.

The method iterates through the array, applying the callback to each element and collecting the results in a new array. The standard implementation uses Array.prototype.map to apply the callback and then reduces the result with Array.prototype.concat to perform the single-level flattening.

Alternative implementations exist for environments that lack native flatMap support. These include a generic approach using Array.prototype.map and .reduce, JLRishe's implementation using Array.concat.apply, and serhii's implementation reducing the array directly. For older browsers or environments, several polyfills are available, including those from core-js and es-shims.


## flatMap Method Syntax and Behavior

The flatMap method takes two parameters: a callback function and an optional thisArg value. The callback function processes each element of the array, with three optional parameters: the current element, its index, and the array itself. The method returns a new array after mapping each element using the callback.

The syntax for using flatMap is as follows:

```javascript

let resultingArray = array.flatMap(callback(currentValue), thisArg)

```

The callback function structure allows for flexibility in array transformations:

```javascript

function callbackFn(element, index, array) {

  return newElement

}

```

Here's a detailed breakdown of its behavior:

- The method applies the callback function to each element of the array, producing either an array or a non-array value.

- Arrays returned by the callback are flattened into a single resulting array.

- The default behavior removes one level of nesting, though empty slots in the source array are ignored.

Like the native implementation, Lodash's flatMap operates similarly:

```javascript

_.flatMap([1,2,3,4,5], i => i%2 !== 0 ? [i] : [])

```

The method's ability to handle array-like objects demonstrates its utility in various scenarios. For instance, merging two Map objects into one can be achieved through:

```javascript

const merged = new Map([map1, map2].values().flatMap((x) => x))

console.log(merged.get("a")) // 1

console.log(merged.get("e")) // 5

```

While the native method processes single and multi-element arrays efficiently, alternative implementations using reduce provide similar functionality:

```javascript

const flatMap = (f, xs) => xs.map(f).reduce(concat, [])

```

These flexibility options make flatMap a powerful tool for array manipulation in JavaScript.


## flatMap Method Parameters and Return Value

The `flatMap` method combines mapping and flattening operations into a single step. It applies a callback function to each element of the array and then flattens the result into a new array. When using this method, the callback function may return either an array or a non-array value - arrays returned by the callback are flattened into the final result.

The method accepts two parameters: a required `callbackFn` and an optional `thisArg`. The `callbackFn` function processes each array element, with four potential arguments: the current element (`element`), its index (`index`), the array itself (`array`), and the `thisArg` value (which defaults to `undefined`).

A key aspect of the method is its behavior with empty slots in the source array. These empty slots are ignored, unlike the broader `map` and `flat` methods, which process all elements including empty ones.

The method operates efficiently by combining the functionality of `map` and `flat` into a single operation. This allows it to produce the same results as a sequence of `map` followed by `flat(depth: 
1)`, but with potential performance benefits.

For alternative implementations, developers can use the `reduce` approach provided in the documentation:

```javascript

const flatMap = (f, xs) => xs.map(f).reduce(concat, [])

```

This method chains together the mapping and flattening operations efficiently, though it may not match the exact performance characteristics of the native implementation.


## Browser Support and Polyfills

Browser support for Array.prototype.flatMap has been expanding since its introduction in ES2019. As of January 2020, the method is natively supported in Chrome 69, Edge 79, Firefox 62, Safari 12, and Opera 56. However, for environments where native support is unavailable, several polyfill options are available.

Mozilla's implementation of flatMap processes each array element using a callback function, producing either an array or a non-array value. Arrays returned by the callback are flattened into the final result. The function accepts two parameters: a required callbackFn and an optional thisArg. The callbackFn processes each array element, accepting up to four arguments: the current element, its index, the array itself, and the thisArg value (which defaults to undefined).

The method handles empty slots in the source array by ignoring them. This differs from the broader map and flat methods, which process all elements including empty ones. Alternative implementation approaches include using Array.prototype.map followed by Array.prototype.reduce for combining mapping and flattening operations.

For string elements, the method specifically rejects string primitives returned from callbackFn. Two workarounds are provided: wrapping the string in an array ([String(x)]) or using Iterator.from to convert the string to a proper iterator. Modern JavaScript implementations maintain compatibility with these requirements, ensuring consistent behavior across supported browsers and environments.

