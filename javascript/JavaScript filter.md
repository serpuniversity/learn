---

title: JavaScript TypedArray Filter Method

date: 2025-05-27

---


# JavaScript TypedArray Filter Method

JavaScript's TypedArray filter() method allows developers to create new typed arrays containing only elements that pass a specified test. This powerful utility operates similarly to the Array.prototype.filter() method, offering a consistent approach to data filtering while maintaining type safety. In this article, we'll explore the filter() method's capabilities, including its callback function parameters, behavior when processing typed arrays, and how to use it to filter elements based on specific conditions. Whether you're working with Int8Array, Uint16Array, or any other numeric type, understanding this method can significantly enhance your ability to process and manipulate typed array data efficiently.


## Filter Method Overview

The filter() method in TypedArrays creates a new array containing elements that pass a specified test implemented by a callback function. This method operates similarly to Array.prototype.filter() and has the same algorithm.


### Callback Function Parameters

The callback function receives three parameters: element (current element being processed), index (element's index), and array (the array being filtered). The function should return a truthy value to keep the element in the resulting typed array, and a falsy value otherwise.


### Filter Behavior

The filter() method returns a copy of the given typed array containing only elements for which the callback function returns true. Elements not visited by the callback remain unchanged in the original array.


### Syntax and Parameters

The method has two syntax options:

- filter(callbackFn)

- filter(callbackFn, thisArg)

The callbackFn function is called with three arguments: element, index, and array. The thisArg parameter allows specifying a value to use as this when executing the callback function.


### Example Usage

The method creates a new typed array with the elements that pass the test. It does not execute the function for empty elements and does not change the original array. If no elements pass the test, an empty typed array is returned.


## Callback Function Parameters

The callback function receives three parameters: element (the current element being processed in the array), index (the index of the current element being processed in the array), and array (the array filter() was called upon). The function should return a truthy value to keep the element in the resulting typed array, and a falsy value otherwise.

The typed array filter() method operates similarly to Array.prototype.filter(), with the same algorithm and implementation details. Both methods call a provided callback function once for each element in a typed array and construct a new typed array of all the values for which the callback returns a true value.

The callback function is only invoked for indexes of the typed array that have assigned values, and not for empty slots or deleted elements. Elements appended to the typed array after the call to filter() begins will not be visited by the callback. The method does not mutate the original typed array.

The method accepts an optional thisArg parameter, which specifies a value to use as this when executing the callback function. If no thisArg is provided, undefined will be passed as this. The callback function receives three arguments: element, index, and array. The method is defined in the ECMAScript (ECMA-262) specification and is fully supported across modern browsers since July 2013.


## Filter Behavior

The method returns a new typed array containing only elements for which the callback function returns true. Existing elements whose values change or are deleted will be visited with their value at the time filter() visits them. Elements appended to the typed array after the call to filter() begins will not be visited by the callback.

The callback function receives three parameters: the value of the element, the index of the element, and the typed array object being traversed. If a thisArg parameter is provided, it will be passed to callback when invoked, for use as its this value. Otherwise, the value undefined will be passed.

The method does not mutate the original typed array and does not execute the callback function for empty elements. Elements that do not pass the callback test are simply skipped and not included in the new typed array. If no elements pass the test, an empty typed array is returned.


## Syntax and Parameters

The filter() method has two syntax options: filter(callback) and filter(callback, thisArg). The callback function should return true to keep an element, and false to filter it out.

The callback function receives three arguments: element (the current element being processed in the typed array), index (the index of the current element being processed in the typed array), and array (the typed array filter() was called upon). This matches the behavior of Array.prototype.filter(), which calls the callback function with arguments (element, index, array).

The method constructs a new typed array of all the values for which the callback returns true. Only elements with assigned values are processed; elements that have been deleted or never assigned will not be visited by the callback. Elements appended to the typed array after the call to filter() begins will also not be visited by the callback.

The callback function can use the provided thisArg value as its this context when executing. If thisArg is not provided, undefined will be passed as this. The callback is only executed for non-empty elements and does not mutate the original typed array.

The method has widespread browser support across modern devices and versions, with full implementation available since July 2013. It is defined in the ECMAScript (ECMA-262) specification and operates similarly to other array filtering methods like every() and some().


## Examples

The method operates on typed arrays and accepts a testing function as its parameter, returning a copy of the typed array containing only elements that pass the test. It processes each element with the provided function, which returns true for elements to include in the new array and false otherwise. The method constructs the new array based on the elements that satisfy the condition specified by the testing function.

The filter() method can be used with different typed arrays, such as Int8Array, Uint16Array, or Float32Array, allowing developers to perform operations on various numeric types while maintaining type safety. The method's behavior with typed arrays is consistent with its behavior on regular JavaScript arrays, making it a versatile tool for data processing tasks.

The following examples demonstrate the method's usage:


### Filtering Odd Elements

```javascript

const oddFilter = (element, index, array) => element % 2 != 0;

const originalArray = new Int8Array([1, 3, 5, 7, 9]);

const filteredArray = originalArray.filter(oddFilter);

console.log(filteredArray); // Output: [1, 3, 5, 7, 9]

```


### Filtering Negative Values

```javascript

const negativeFilter = (element, index, array) => element < 0;

const mixedArray = new Int8Array([-10, 20, -30, 40, -50]);

const filteredArray = mixedArray.filter(negativeFilter);

console.log(filteredArray); // Output: [-10, -30, -50]

```


### Filtering Divisible by 2

```javascript

const divisibleBy2Filter = (element, index, array) => element % 2 == 0;

const oddArray = new Int8Array([1, 3, 5, 7, 9]);

const filteredArray = oddArray.filter(divisibleBy2Filter);

console.log(filteredArray); // Output: []

```

These examples illustrate the method's flexibility across different numeric types and its ability to produce both empty and populated filtered arrays based on the specified conditions.

