---

title: JavaScript TypedArray.prototype.findLast() Method

date: 2025-05-27

---


# JavaScript TypedArray.prototype.findLast() Method

The JavaScript TypedArray.prototype.findLast() method represents a significant advancement in array processing capabilities, specifically for TypedArray instances. Introduced in ECMAScript 2023, this method provides developers with a powerful tool for reverse iteration and conditional element retrieval. Unlike traditional findLastIndex() methods that traverse arrays from start to end, findLast() processes data in reverse order, offering new possibilities for data analysis and manipulation.

This introduction sets the stage for a detailed exploration of findLast(), examining its syntax, behavior, and implementation across various TypedArray types. We'll analyze its performance in different testing scenarios, compare it to related methods like findLastIndex(), and discuss its compatibility across modern browsers. Through practical examples and technical specifications, we'll demonstrate how this new method can enhance JavaScript development for working with typed arrays.


## Introduction to findLast() Method

The findLast() method is part of ECMAScript 2023 standards and operates specifically on TypedArray instances. It iterates through the array in reverse, making it distinct from similar methods that traverse arrays from start to end.

The core functionality of findLast() involves executing a callback function for each element, returning the first element that satisfies a given condition. This is achieved through a testing function that receives three parameters: the current element, its index, and the array itself. The method returns either the matching element or undefined if no match is found.

For example, findLast() can be used to locate specific values in an array. In one demonstration, the method successfully identified 2012 as the last leap year in a sequence of integers [2001, 2004, 2005, 2006, 2009, 2012, 2015]. In another example, attempting to find negative numbers in [1, 10, 5, 6, 7, 8, 9, 10] correctly returned undefined.


## Syntax and Parameters

The findLast() method operates on TypedArray instances and employs a reverse iteration approach, similar to its counterpart findLastIndex(). It executes a callback function for each element, returning either the matching element or undefined if no match is found.


### Method Parameters

The findLast() method accepts two parameters:

1. **callbackFn**: A function that tests each element. It should return a truthy value for matching elements and a falsy value otherwise. The function receives three arguments: the current element being processed, its index, and the array itself.

2. **thisArg** (optional): A value to use as this when executing the callback function.


### Method Syntax

The method syntax follows this pattern:

```javascript

findLast(callbackFn)

OR

findLast(callbackFn, thisArg)

```

The provided examples illustrate its usage effectively. The method successfully identified 2012 as the last leap year in the sequence [2001, 2004, 2005, 2006, 2009, 2012, 2015]. In another example, attempting to find negative numbers in [1, 10, 5, 6, 7, 8, 9, 10] correctly returned undefined.


### Method Behavior

Similar to Array.prototype.findLast(), findLast() begins its search at the last element and works its way backward. The method processes all elements in the array, including those in sparse arrays. However, it does not modify the original array.


## Example Usage

To further illustrate the findLast() method's functionality, several usage scenarios demonstrate its application with different typed array types and testing functions.


### Example 1: Finding the Last Even Number

The method successfully identifies the last even number in an array of integers. For instance, given the array `[-1, 2, 8, 5, 12, 3]`, findLast() returns 12, the largest even number in the sequence.


### Example 2: Searching for Leap Years

The findLast() method can also locate specific values within ranges, such as identifying leap years in a sequence. Applying this to the array `[2001, 2004, 2005, 2006, 2009, 2012, 2015]`, the method correctly returns 2012 as the last leap year.


### Example 3: Handling No Matching Elements

In cases where no elements meet the criteria, findLast() returns undefined, maintaining consistency with its counterpart methods. Using the array `[1, 2, 3, 4, 5, 6, 7, 8]` and a testing function for negative numbers, the method correctly returns undefined, as expected.


### Additional Examples

Further demonstrating its capabilities, the findLast() method effectively:

- Identifies the index of the last even number in `[2002, 2004, 2005, 2006, 2007, 2012]`, returning 7.

- Locates the index of the last leap year in `[2002, 2004, 2005, 2006, 2007, 2012]`, correctly identifying index 5. The isLeapYear() function checks for leap years by verifying divisibility rules.

- Demonstrates its behavior when no elements satisfy the testing function, returning -1 for the array `[1, 2, 3, 4, 5, 6, 7, 8]` when searching for negative numbers.


## Comparison with findLastIndex()

The findLastIndex() method, which is available across browsers since August 2022, operates similarly to findLast() but returns the index of the last element that passes the test instead of the element itself. This method processes the array from end to beginning and returns -1 if no elements satisfy the testing function.


### Implementation Details

The method accepts the same parameters as findLast(), including the callback function and an optional thisArg value. The callback function should return a truthy value for matching elements and a falsy value otherwise, receiving three arguments: the current element, its index, and the array itself.


### Examples

The method operates consistently with its counterpart in various scenarios. For instance, when searching for the last even number in the typed array [2002, 2004, 2005, 2006, 2007, 2012], findLastIndex() correctly returns 7. Similarly, the method identifies the last leap year index in the same array by returning 5 when using the isLeapYear() function.

In cases where no elements satisfy the testing function, findLastIndex() returns -1, matching its behavior in non-typed array contexts. This is demonstrated when applying a negative number test to the Uint8Array [1, 2, 3, 4, 5, 6, 7, 8].


## Browser Support

findLast() compatibility extends across major browsers, with initial support rolling out in Chrome, Edge, Firefox, Opera, and Safari platforms. The method seamlessly processes typed array instances, including Int8Array, Uint8Array, and similar data structures, using reverse iteration to find matching elements.

The feature's implementation across these browsers maintains consistency with Array.prototype.findLast(), utilizing the same algorithm for processing and returns. As of the latest updates, the method effectively handles both modern device configurations and various browser versions, ensuring compatibility with existing development environments.

Browser support compatibility notes highlight existing polyfill implementations in core-js, allowing developers to implement the feature in environments where native support may be limited. This ensures broad applicability for developers working across different project requirements and browser versions.

