---

title: Array.prototype.findLastIndex: Working with Last Elements in JavaScript Arrays

date: 2025-05-26

---


# Array.prototype.findLastIndex: Working with Last Elements in JavaScript Arrays

In JavaScript, the Array.prototype.findLastIndex method provides a powerful way to search arrays from end to beginning, allowing developers to efficiently find the last occurrence of specific values or elements meeting certain criteria. By operating in reverse order, this method can significantly reduce the number of iterations needed to locate desired elements, particularly in large or complex data structures. Understanding how to use findLastIndex effectively can improve the performance and readability of your code, making it especially useful for operations that require processing elements from the end of an array.


## Introduction to findLastIndex

The findLastIndex method, new to JavaScript arrays as of ECMAScript Stage 3, allows developers to search arrays from the end for the last element matching a given condition. This functionality is particularly useful for operations that require processing elements in reverse order, such as finding the last occurrence of a specific value or filtering through data structures where end-to-end analysis is necessary.

The method takes a callback function as its primary parameter, which receives three arguments: the current element, its index, and the array itself. This allows for flexible condition checking during the search process. If the callback function returns true for an element, findLastIndex returns the index of that element. If no matches are found, it returns -1.

Browser support for findLastIndex includes Chrome 97, Edge 97, Firefox 104, Safari 15.4, and Opera 83, making it widely accessible across modern web applications. For users on older browsers or specific environments where the method is not natively available, polyfills from core-js and es-shims can provide compatibility through array-iteration-from-last.js.


## Basic Usage and Syntax

The findLastIndex method performs its search in reverse order, making it particularly useful for operations that require processing elements from end to beginning. It returns the index of the first element that satisfies the provided testing function, and returns -1 if no elements match the criteria.

The method's behavior is consistent with its sibling methods: find and findIndex. Like find, it returns the first element that matches the condition when applied to elements, not just their indices. In contrast, findLastIndex returns the index of this element, matching the behavior of findIndex.

For example, given the array `let age = [13, 20, 15, 45, 1, 44, 80]`, both findLastIndex and find will check elements from right to left. When searching for the index of 80, findLastIndex returns 6, while find returns 0 - demonstrating their identical functionality when returning indices.

The implementation details emphasize performance and efficiency, particularly for large arrays or those with multiple matching elements. By operating in reverse order, findLastIndex can quickly locate the desired element with fewer iterations compared to methods that require linear traversal from the beginning. This is especially beneficial when the matching element is likely to be found near the end of the array.


## callbackFn Parameter Details

The callback function receives four parameters: element, index, array, and thisArg. The element parameter refers to the current element being processed in the array. The index parameter represents the index of the current element within the array.

The callback function operates on each element in reverse order, starting from the last element of the array and moving towards the first. This is particularly useful for operations that depend on the sequence of elements, such as finding the last index of a specific value or performing calculations that require processing elements from end to beginning.

The array parameter provides access to the entire array being searched, which can be useful when the callback function needs to perform operations that involve multiple elements or when working with complex data structures.

The thisArg parameter, if provided, is passed as the this value when executing the callback function. This allows the callback function to maintain its context when called within the reverse iteration process.

The callback function should return a truthy value to indicate that the current element satisfies the condition. If the condition is met, findLastIndex returns the index of that element. If no elements match the criteria, findLastIndex returns -1.


## Supported Browsers and Polyfills

As a JavaScript method, findLastIndex enjoys wide compatibility across modern browsers, with support in Chrome 97, Edge 97, Firefox 104, Safari 15.4, and Opera 83. For users on older browsers or specific environments where native support is lacking, compatibility can be restored through core-js and es-shims polyfills via their array-iteration-from-last.js package.

The underlying algorithm iterates over the array in reverse order, making it particularly efficient for large datasets or those with multiple matching elements. This reverse iteration approach enables the method to quickly locate the desired element with fewer overall iterations compared to linear traversal from the beginning.

For environments where native support is unavailable, developers can implement the functionality using custom JavaScript functions. For example, the following user-defined implementation iterates through the array from the end to the beginning, checking each element against a provided condition:

```javascript

const findLastIndex = (array, predicate) => {

  for (let i = array.length - 1; i >= 0; i--) {

    if (predicate(array[i])) {

      return i;

    }

  }

  return -1;

}

```

This custom implementation mirrors the native method's functionality while providing flexibility for specific use cases. It iterates over the array in reverse order, checking each element against the provided predicate function. If a match is found, it returns the current index. If no matches are found after checking all elements, it returns -1.


## Advanced Examples and Use Cases

The findLastIndex method's capabilities extend beyond basic usage, offering powerful tools for advanced array manipulation. One practical application is identifying the last positive number before a trough in a sequence of numbers, as demonstrated in the following example:

```javascript

const numbers = [3, -1, 1, 4, 1, 5, 9, 2, 6];

const lastTrough = numbers

  .filter((num) => num > 0)

  .findLastIndex((num, idx, arr) => {

    return idx > 0 && idx < arr.length - 1 && num >= arr[idx - 1] && num >= arr[idx + 1];

  });

console.log(lastTrough); // 6

```

This code snippet illustrates how findLastIndex can traverse an array in reverse, applying complex conditions to identify specific elements.

The method also handles sparse arrays effectively, as shown in this example:

```javascript

console.log([1, , 3].findLastIndex((x) => x === undefined)); // 1

```

In addition, findLastIndex maintains its generic nature when working with non-array objects, as this example demonstrates:

```javascript

const arrayLike = { length: 3, 0: 2, 1: 
7.3, 2: 4, 3: 3 };

console.log(Array.prototype.findLastIndex.call(arrayLike, (x) => Number.isInteger(x))); // 2

```

This flexibility, combined with its efficient reverse iteration approach, makes findLastIndex particularly useful for operations that require processing elements from end to beginning, such as identifying the last prime number in an array:

```javascript

function isPrime(element) {

  if (element % 2 === 0 || element < 2) {

    return false;

  }

  for (let factor = 3; factor <= Math.sqrt(element); factor += 2) {

    if (element % factor === 0) {

      return false;

    }

  }

  return true;

}

console.log([4, 6, 8, 12].findLastIndex(isPrime)); // -1

console.log([4, 5, 7, 8, 9, 11, 12].findLastIndex(isPrime)); // 5

```

These examples showcase the method's versatility in handling various data structures and performing complex operations efficiently.

