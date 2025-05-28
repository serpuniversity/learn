---

title: Set.prototype.forEach(): JavaScript Reference & Tutorial

date: 2025-05-26

---


# Set.prototype.forEach(): JavaScript Reference & Tutorial

JavaScript's Set data structure provides an efficient way to store and manage unique values. While basic Set operations like adding and removing elements are straightforward, working with the contents of a Set often requires iteration. The Set.prototype.forEach() method fills this need by executing a provided function for each element. This article explores the functionality, implementation, and best practices of using Set.prototype.forEach(), comparing it to alternative iteration methods and discussing its behavior with asynchronous functions.


## Method Overview

The Set.prototype.forEach() method executes a provided function once for each element in the set, in insertion order. It takes two parameters: a callback function and an optional thisArg. The callback function receives three arguments: the value of the element, the value of the element's index (which is the same as the value), and the set being iterated.

The method is available across multiple devices and browsers, having been implemented since July 2015. It logs set elements during iteration and supports Chrome, Edge, Firefox, Opera, and Safari. The method's implementation follows ECMAScript 2026 Language Specification, applying to Set objects and using the method signature void forEach(IterationCallback callbackfn, thisArg?).

For example, the method can be used to display set values as shown below:

```javascript

let fruits = new Set();

fruits.add("Mango");

fruits.add("Banana");

fruits.add("Papaya");

fruits.add("Grapes");

function display(i, set) {

  console.log(i);

}

fruits.forEach(display); // Output: Mango, Banana, Papaya, Grapes

```

When using async functions with forEach, it's important to note that the method fires blocks of code in parallel rather than executing them sequentially.


## Syntax and Parameters

The `forEach` method of Set instances executes a provided function once for each value in the set, maintaining the insertion order of elements. This built-in function processes each set element by invoking a supplied callback function, which receives three parameters: the current element's value, the element's key (which is the same as its value), and the Set object being traversed.


### Implementation and Behavior

The method processes set elements through the callback function with a consistent pattern: 

- The first parameter represents the element's value.

- The second parameter is the element's key, which equals its value in a Set context.

- The third parameter provides the Set object being iterated.

The callback function can be customized to perform various operations on the set elements. For example, it can be used to transform set values into a new array or perform additional computations.


### Browser Support and Usage

The method demonstrates consistent behavior across modern browsers, including Chrome, Edge, Firefox, Opera, and Safari. It has been available since July 2015, making it a reliable choice for JavaScript development. The implementation follows ECMAScript 2026 Language Specification and can be used with both client-side and server-side JavaScript development.


### Example Usage

To illustrate its usage, consider a basic example where the method is used to display set values:

```javascript

let fruits = new Set();

fruits.add("Mango");

fruits.add("Banana");

fruits.add("Papaya");

fruits.add("Grapes");

function display(i, set) {

  console.log(i);

}

fruits.forEach(display); // Output: Mango, Banana, Papaya, Grapes

```

This demonstrates the method's ability to iterate over a Set and execute a callback function for each element, in the order they were inserted.


## Examples and Usage

The `forEach` method provides flexibility for set iteration through its callback function, which receives three parameters: the current element's value, the element's key (which is the same as the value), and the Set object being traversed. This pattern allows developers to perform various operations on set elements, as demonstrated in the following examples:


### Array Conversion

To convert a Set to an array, developers can use the spread operator with the `values()` method:

```javascript

const mySet = new Set([1, 2, 3]);

const resultArray = [...mySet.values()]; // [1, 2, 3]

```


### Element Operations

The callback function can be customized to perform operations on set values, such as creating a new array with transformed values:

```javascript

const mySet = new Set(['Apple', 'Banana', 'Cherry']);

const newSet = new Set();

mySet.forEach(value => {

  newSet.add(value.toUpperCase());

});

const resultArray = Array.from(newSet); // ['APPLE', 'BANANA', 'CHERRY']

```


### Performance Considerations

When working with async functions, it's important to note that `forEach` executes blocks of code in parallel rather than sequentially. This behavior differs from standard iteration methods and should be considered when designing asynchronous operations:

```javascript

const set = new Set([1, 2, 3]);

set.forEach(async value => {

  await doSomething(value);

});

```

The specific implementation details may vary between browsers, though the method demonstrates consistent behavior across modern browsers.


### Duplicate Removal

Set objects can efficiently remove duplicates from arrays, as shown in this example:

```javascript

const numbers = [1, 2, 3, 3, 4, 4, 5];

const uniqueNumbers = [...new Set(numbers)]; // [1, 2, 3, 4, 5]

```


### String Operations

The method preserves case sensitivity for string operations, allowing for case-sensitive comparisons:

```javascript

const strings = ['apple', 'Banana', 'APPLE'];

const uniqueStrings = [...new Set(strings)]; // ['apple', 'Banana', 'APPLE']

```


## Performance and Browser Compatibility

According to performance tests, the `forEach` method is slightly slower than the traditional `for` loop. While modern JavaScript engines have optimized both, the `for` loop remains marginally more efficient. This difference becomes more pronounced when working with complex operations or large datasets.

Browser compatibility is another factor to consider. While `forEach` has been available since July 2015 across multiple browsers, it is not supported in Internet Explorer versions less than 9. For wider compatibility, developers may need to implement browser shims. This historical requirement of supporting older browsers adds to the development complexity.

The choice between `forEach` and `for` loops depends heavily on the specific use case. For simple array manipulations and when working with modern browsers, `forEach` offers improved readability and maintainability. Its three-argument signature provides a clear structure for iterating over elements, keys, and the array itself.

However, for operations that require breaking out of the loop early or when performance is critical, the traditional `for` loop remains the better choice. The ability to directly manipulate array indices and use the `break` statement provides flexibility that `forEach` lacks. Modern JavaScript development increasingly favors the `for of` loop for daily requirements, though this choice depends on individual coding preferences and project needs.


## Best Practices and Limitations

The `forEach` method offers improved readability and maintainability through its simplified syntax and callback function structure. However, it lacks several key capabilities that developers may need, particularly when working with complex data structures or requiring early termination of loops.

One significant limitation is the inability to break out of the loop early. Unlike traditional `for` loops, which support `break` and `return` statements, `forEach` requires alternative approaches for early termination. This limitation can make it less suitable for scenarios where conditional exit points are necessary, such as validating input or searching for specific elements.

Performance considerations also influence the choice between `forEach` and traditional loops. While modern JavaScript engines have optimized both constructs, `for` loops generally demonstrate slightly better performance due to their direct manipulation of array indices. The difference is most pronounced when dealing with complex operations or large datasets. For applications requiring maximum efficiency, developers should weigh the readability benefits of `forEach` against the performance advantages of traditional loops.

When working with complex data structures like Maps or Sets, developers must be particularly mindful of iteration limitations. The method cannot modify the collection during iteration, which can complicate operations that require concurrent updates. Additionally, it cannot access previous or next elements in the collection, requiring developers to implement custom logic using traditional for loops when these capabilities are needed.

The choice between these iteration methods depends heavily on the specific use case. For simple array manipulations and modern browser development, the built-in conveniences of `forEach` offer significant advantages. It requires fewer lines of code, maintains variable scope within the callback, and reduces the likelihood of accidental errors.

For applications requiring explicit control over iteration, particularly when breaking out of loops or modifying collections during iteration, traditional for loops remain the better choice. The direct access to array indices and the ability to use the `break` statement provide essential functionality that `forEach` lacks. Modern JavaScript development increasingly favors the `for of` loop for daily requirements, though this choice depends on individual coding preferences and project needs.

