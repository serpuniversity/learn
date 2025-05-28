---

title: JavaScript TypedArray.prototype.forEach() Method

date: 2025-05-27

---


# JavaScript TypedArray.prototype.forEach() Method

JavaScript's TypedArray provides a powerful way to work with binary data, offering both performance advantages and type safety over traditional arrays. A key method in this API is TypedArray.prototype.forEach(), which allows developers to efficiently iterate over typed array elements while maintaining the type information of the underlying data. This article explores the details of this method, comparing it to its counterpart in regular arrays and demonstrating its usage with various data types and array structures.


## Understanding TypedArray.prototype.forEach()

The TypedArray.prototype.forEach() method provides a convenient way to execute a function for each element in a typed array. Like its counterpart in regular arrays, this method follows the same algorithm but is specifically designed for typed arrays, ensuring type safety and performance optimizations for binary data.

When working with typed arrays, you can access three valuable pieces of information within your callback function:

1. The current element being processed (`element`)

2. The index of the current element (`index`)

3. A reference to the array being iterated over (`array`)

This method signature closely mirrors its counterpart in regular arrays, making it straightforward to adapt existing forEach logic for typed array use cases. While the syntax remains consistent—accepting either a simple callback or a callback with an additional `thisArg` context parameter—it's essential to note that the method itself returns undefined, matching its behavior in both native array and typed array implementations.

Understanding these fundamentals sets the stage for leveraging TypedArray.prototype.forEach() effectively in JavaScript development, particularly when working with binary data structures that benefit from typed array optimizations.


## Method Syntax and Parameters

The TypedArray.prototype.forEach() method follows the same syntax and parameter structure as its counterpart in regular arrays, making it familiar for developers already proficient in JavaScript iteration techniques. The method requires either a single callback function or extends with an optional `thisArg` context parameter, matching the native Array.prototype.forEach() implementation.

The method accepts three parameters within the callback function:

1. `element`: The current value of the array element being processed

2. `index`: The index of the current element in the array (optional)

3. `array`: A reference to the array on which forEach was called (optional)

This parameter structure ensures developers have full context while iterating over typed array elements, enabling efficient manipulation and processing of binary data structures.

The method operates similarly to its non-typed array equivalent, with key differences in variable naming and method availability. While the native implementation has been widely available since July 2013 across modern browsers, the typed array version brings this functionality directly to binary data structures, optimizing performance and type safety for developers working with ArrayBuffer data.


## Callback Function Arguments

The callback function within TypedArray.prototype.forEach() receives three parameters: currentValue, index (optional), and array (optional). The function signature closely mirrors its counterpart in native arrays, providing developers with full context while iterating over typed array elements.

The callback function takes three arguments:

1. currentValue: The current value of the array element being processed

2. index: The index of the current element being processed in the array (optional)

3. array: A reference to the array being iterated over (optional)

This parameter structure allows for efficient manipulation and processing of binary data structures, matching the functionality provided by the native Array.prototype.forEach() implementation. The method operates similarly across different browsers, with consistent behavior and performance optimizations for typed arrays.

For developers working with typed arrays, understanding these callback arguments is crucial for effective implementation of iteration logic, particularly when processing binary data structures that benefit from typed array optimizations.


## Method Characteristics and Behavior

The method returns undefined, consistent with both native array and typed array implementations. This behavior aligns with JavaScript's iteration patterns, where array methods typically do not return new values but perform their operations in place.

One key characteristic of the method is its non-mutating nature—it does not alter the original typed array. This aligns with JavaScript's array methods, where iteration typically focuses on side effects rather than modifying the underlying data structure directly.

Browser compatibility for this method is excellent, with widespread support across modern browsers since September 2016. The method works consistently across all supported browsers, matching the behavior of the native Array.prototype.forEach() implementation.


### Additional Considerations

The method's behavior regarding empty slots in sparse arrays is consistent with other array methods. For deleted indexes, the method correctly skips those elements, as the implementation uses `Object.hasOwnProperty.call(this, i)` to ensure it only processes existing properties.

The characteristic of early termination via loop statements like `for`, `for...of`, and `for...in` applies equally to this method. Similarly, the lack of direct support for `continue` or `return` statements to break the loop flow is consistent with JavaScript's array iteration patterns.


## Example Usage

let A = new Uint8Array([1, 3, 5, 7])

let B = new Uint8Array([2, 4, 6, 8])

function callback(element, index, array) {

  console.log(`a[${index}] = ${element}`)

}

A.forEach(callback)

B.forEach(callback)

// Output:

// a[0] = 1

// a[1] = 3

// a[2] = 5

// a[3] = 7

// a[0] = 2

// a[1] = 4

// a[2] = 6

// a[3] = 8

The method works consistently across different data types. For example, with a Float32Array:

let values = new Float32Array([1.2, 3.4, 5.6, 7.8])

values.forEach((value, index, array) => {

  console.log(`values[${index}] = ${value}`)

})

// Output:

// values[0] = 1.2

// values[1] = 3.4

// values[2] = 5.6

// values[3] = 7.8

The method also functions correctly with sparse arrays:

let sparseArray = new Uint8Array([1, 3, , 7])

let numCallbackRuns = 0

sparseArray.forEach((element) => {

  console.log({element})

  numCallbackRuns++

})

// Output:

// { element: 1 }

// { element: 3 }

// { element: 7 }

// { numCallbackRuns: 3 }

The behavior with non-object parameters is consistent with the native Array.prototype.forEach() implementation:

let array = [1, 2, 3, 4]

array.forEach((element, index, array) => {

  console.log(array[index])

})

// Output:

// 1

// 2

// 3

// 4

