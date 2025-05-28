---

title: JavaScript Iterator: filter

date: 2025-05-26

---


# JavaScript Iterator: filter

JavaScript's `filter()` method provides a powerful way to process array elements based on specific conditions. By returning a new array containing only the elements that pass a given test, `filter()` enables developers to perform complex data manipulations with concise code. Whether you're working with numerical data, strings, or custom objects, this versatile method offers a reliable solution for filtering collections in modern JavaScript applications.


## filter Method Overview

The `filter()` method creates a new array containing elements that meet a specified condition. It operates by iterating through array elements and applying a callback function to each element. The original array remains unchanged, and only elements for which the callback returns true are included in the new array.

The method follows a for loop structure where, for each iteration of the index i, if the callback function returns true, the element at index i is pushed into the new array. The method itself returns this new array containing only the filtered elements.

The syntax for `filter()` is:

```javascript

_array_.filter(_function(currentValue, index, arr), thisValue_)

```

Here, `function` represents a callback function that processes each element. The function receives three parameters: `currentValue`, `index`, and `arr`, though the index and arr parameters are optional. This structure allows for flexible implementation of filtering logic.

The return value is a shallow copy of the original array containing elements that pass the specified condition. The method supports various types of arrays, including numbers, strings, and objects, making it a versatile tool for data filtering in JavaScript applications.


## filter Implementation

The `filter()` method operates by applying a callback function to each element of an array and constructing a new array containing only the elements for which the callback function returns a truthy value. This process involves iterating through the array and pushing elements that meet the specified condition into a new array.

The method's implementation requires the callback function to accept three parameters: the current element (`element`), its index (`index`), and the array (`arr`). These parameters enable flexible filtering logic and are consistent across array and typed array implementations.

The filter method's behavior is demonstrated through various examples across different data types:

- Filtering numbers: `numberArray.filter(item => item > 20)`

- Filtering strings: `stringArray.filter(item => item.includes("example"))`

- Filtering objects: `objectArray.filter(({ premium }) => premium)`

This versatile implementation supports a wide range of filtering scenarios, from basic value comparisons to complex object property checks, while maintaining compatibility across array and typed array instances.


## filter Examples and Usage

The `filter()` method creates a new array containing elements that pass a specified condition. It works with any kind of array, including numbers, strings, and objects, making it a versatile tool for data filtering in JavaScript applications.


### Filtering with Numbers

The method can process arrays of numbers based on various criteria:

- Extract numbers greater than 20: `numberArray.filter(item => item > 20)`

- Include numbers equal to or less than 20: `numberArray.filter(item => item <= 20)`

- Filter multiples of nine: `numberArray.filter(item => item % 9 === 0)`


### Filtering with Strings

String operations require more complex handling compared to numbers, but the basic filtering logic remains consistent:

- Filter strings longer than 2 characters: `stringArray.filter(item => item.length > 2)`

- Remove strings shorter than 2 characters: `stringArray.filter(item => item.length >= 2)`

- Find strings containing "arr" (case-insensitive): `stringArray.filter(item => item.toLowerCase().includes("arr"))`


### Filtering with Objects

The filtering process works similarly to string arrays, using common object properties:

- Select console objects: `consoleObjectArray.filter(item => item.type === "console")`

- Filter objects with names longer than 5 characters: `longerNameObjectArray.filter(item => item.name.length > 5)`

- Obtain console objects from before 2018: `newerConsolesArray.filter(item => item.year > 2017)`

These examples demonstrate the method's range of capabilities, from basic value comparisons to complex property checks, while maintaining compatibility across array and typed array instances. The filtering process constructs a shallow copy of the original array containing elements that pass the specified condition.


## filter Method Details

The filter method operates through a callback function applied to each element of an array. It accepts two parameters: the first as a function to execute for each element, and the second as an optional context value to use when executing the callback function.

The provided callback function must return a truthy value to keep the element in the resulting array, and a falsy value otherwise. The callback function receives three arguments: the current element (`element`), the index of that element (`index`), and the array on which `filter` was called (`array`). Additionally, a fourth parameter allows specifying an optional context value (`thisArg`).

The method returns a shallow copy of the given array containing only the elements that pass the specified condition. It maintains compatibility across various array and typed array implementations while supporting sparse arrays by calling the callback function only for array indexes with assigned values.

The filter implementation demonstrates its versatility through multiple usage examples, including filtering numbers, strings, and objects based on specific criteria. The method supports ES5 boolean properties, treating booleans as truthy or falsy values and processing them accordingly.


## Performance Considerations

The core implementation of the filter method is efficient and compatible across various array types, including sparse arrays, which only call the callback function for assigned values. The method's performance is generally strong, as demonstrated by its widespread support across browsers since July 2015. However, developers have implemented alternative in-place filtering strategies to optimize specific use cases.

One approach uses a while loop to iterate through the array, as shown in this example:

```javascript

function filterInPlace(a, condition) {

  let i = 0, j = 0;

  while (i < a.length) {

    const val = a[i];

    if (condition(val, i, a)) a[j++] = val;

    i++;

  }

  a.length = j;

  return a;

}

```

This method creates a new array of filtered elements, leaving the original array empty. While effective, it doesn't optimize memory allocation as desired. A more sophisticated implementation uses the Array.prototype.forEach method:

```javascript

function filterInPlace(a, condition, thisArg) {

  let j = 0;

  a.forEach((e, i) => {

    if (condition.call(thisArg, e, i, a)) {

      if (i !== j) a[j] = e;

      j++;

    }

  });

  a.length = j;

  return a;

}

```

This version efficiently compacts arrays with empty slots, implements the thisArg parameter, and avoids unnecessary assignments when no elements fail the condition test. These in-place alternatives maintain array references for other aliases, making them useful for specific scenarios while demonstrating the robustness of JavaScript's array manipulation capabilities.

