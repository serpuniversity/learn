---

title: JavaScript Set Methods: values()

date: 2025-05-27

---


# JavaScript Set Methods: values()

JavaScript's Set object provides a specialized structure for managing collections of unique values while maintaining the order of insertion. This article explores the values() method, which returns an Iterator object containing the set's values, allowing for controlled iteration while maintaining internal optimizations for unique value storage. Through detailed examples and performance considerations, we'll examine how this method enables efficient traversal and ordered iteration, distinguishing it from similar array methods while highlighting its role in modern JavaScript development.


## Overview of Set and values() Method

The Set object in JavaScript offers a specialized structure for managing collections of unique values. Unlike arrays, which can contain duplicates, each value within a Set occurs only once. The object maintains the insertion order of values, making it particularly useful for scenarios requiring both uniqueness and ordered iteration.

To create a Set, you can pass an array to the `new Set()` constructor, or use the spread operator to transform sets into arrays. The constructor also accepts an iterable as an argument, allowing flexible initialization from various data sources.

A Set's properties include `size`, which returns the number of elements, and `has()`, which checks for element existence. The `add()` method appends new elements while `delete()` removes specified elements, returning the deleted value. As a built-in object, Set inherits methods and properties from both `Object.prototype` and `Function.prototype`.

Value equality in Sets is determined by the SameValueZero algorithm, which treats NaN as equal to itself and compares other values using the === operator's semantics. This implementation ensures consistent handling of unique values, including edge cases with 0 and -0 representations.

The values() method returns an Iterator object containing the set's values, allowing controlled iteration over the collection's elements. This mechanism enables efficient traversal while maintaining the internal implementation's optimizations for unique value storage.


## Syntax and Usage of values()

The `values()` method returns a new Iterator object containing all items in the set in the order they were inserted. Unlike properties like `keys()` and `entries()`, `values()` directly provides an Iterator with the values of each element in the set, making it particularly useful for ordered iteration scenarios.

To retrieve and iterate over Set values using this method, simply call `set.values()` on your Set object. This will give you an Iterator that you can use with `.next()` to access each value sequentially. For example:

```javascript

const myset = new Set();

myset.add("California");

myset.add("Seattle");

myset.add("Chicago");

const setIterator = myset.values();

console.log(setIterator.next().value); // California

console.log(setIterator.next().value); // Seattle

console.log(setIterator.next().value); // Chicago

```

For scenarios requiring more control over the iteration process, you can use a while loop with `.next()`:

```javascript

const myset = new Set();

myset.add("California");

myset.add("Seattle");

myset.add("Chicago");

const setIterator = myset.values();

let i = 0;

while (i < myset.size) {

  console.log(setIterator.next().value);

  i++;

}

```

This approach ensures efficient traversal while maintaining the internal implementation's optimizations for unique value storage. The method works across all modern browsers, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, making it widely accessible for practical use cases.


## Example Usage of values()

The values() method returns a new Iterator object containing all items in the set in the order they were inserted. This feature is part of ECMAScript6 and has been supported in all modern browsers since June 2017. The method provides an efficient way to iterate over the collection's elements while maintaining the internal implementation's optimizations for unique value storage.


### Example Usage

The values() method is particularly useful for ordered iteration scenarios. It allows developers to directly access the values of each element in the set, providing more control over the iteration process. For instance:

```javascript

let mySet = new Set();

mySet.add("California");

mySet.add("Seattle");

mySet.add("Chicago");

const iterator = mySet.values();

for (let city of iterator) {

  console.log(city);

}

```

This example demonstrates how to retrieve and iterate over Set values using the values() method. The method returns an Iterator object that can be directly used in a for...of loop to access each value sequentially.

Alternatively, you can use the `.next()` method to manually control the iteration process:

```javascript

let mySet = new Set();

mySet.add("California");

mySet.add("Seattle");

mySet.add("Chicago");

const iterator = mySet.values();

while (iterator.next().value) {

  console.log(iterator.next().value);

}

```

This approach provides flexibility while maintaining efficient traversal of the set's elements. The values() method works across all modern browsers, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, making it widely accessible for practical use cases.


## Comparison with Array Methods

The values() method represents an important distinction between Set and Array data structures in JavaScript. While Arrays allow duplicate elements and maintain order through zero-based indexing, Sets prioritize uniqueness and preserve insertion order through their underlying hash table implementation.

Performance considerations highlight key differences between the two structures. Arrays exhibit slower lookups and membership tests compared to Sets, particularly as the collection size increases. This is particularly relevant when comparing operations like `Array.prototype.includes` to Set's `has` method, which generally demonstrates faster performance when comparing arrays of similar length.

Both data structures maintain different approaches to element access and iteration. While Arrays enable indexing with `[]` notation, Sets do not support direct element access due to their hash-based implementation. This limitation necessitates the use of iteration methods like values(), while Arrays can be accessed using the bracket notation or through methods like `forEach()`.

The distinction between key-value pairs also shapes their functionality. Array elements consist of value-key pairs with numerical indices, while Sets store unique values without associated keys. This structural difference influences operations such as filtering and mapping, where Array's flexibility with key types provides more direct access to elements than Sets' value-only approach.

Developers must consider these factors when selecting between the two structures for specific use cases. Sets excel when uniqueness and efficient operations are prioritized, while Arrays remain essential for collections requiring indexing and key-value pair functionality. Both structures continue to evolve according to ECMAScript specifications, maintaining their respective roles in modern JavaScript development.


## Future Outlook for Set Methods

According to the ECMAScript 2026 Language Specification, the Set object in JavaScript is defined to ensure the uniqueness of a list of values, with insertion order corresponding to the order of successful add() method calls. This fundamental structure forms the basis of the Set's functionality, providing developers with a reliable method for managing collections of unique items.

The Set object maintains an average access time better than O(N), allowing for implementation as hash tables (O(1) lookup), search trees (O(log(N)) lookup), or other efficient data structures. This optimized performance is particularly beneficial for operations requiring quick value lookup and membership testing.

The ECMA262 specification outlines several key aspects of Set's implementation, including the SameValueZero algorithm for value equality. This algorithm treats NaN as equal to itself and compares other values using the === operator's semantics, ensuring consistent handling of unique values, including edge cases with 0 and -0 representations.

The constructor syntax supports both empty set creation and initialization from iterable objects, although attempting to call the constructor without the new keyword throws a TypeError. This restrictive approach helps maintain the integrity of the Set structure, preventing accidental misuse through incorrect usage patterns.

