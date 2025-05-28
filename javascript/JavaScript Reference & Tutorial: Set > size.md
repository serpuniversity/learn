---

title: JavaScript Set size Property

date: 2025-05-26

---


# JavaScript Set size Property

JavaScript's Set object provides an efficient way to store and manipulate unique collections of elements. This article explores the `Set.size` property, which returns the number of distinct elements in a Set. Through detailed examples and explanations, we'll see how `Set.size` accurately counts unique values, treats NaN as equal to itself, and maintains consistent behavior across different data types and operations.


## Introduction to Set.size

The Set.size property returns the number of elements in a JavaScript Set object, accurately reflecting the count of distinct (unique) elements. For example, creating a set with multiple occurrences of the same value (like [10, 10, 20, 40, 60, 60]) reports 4 unique elements: 10, 20, 40, and 60.

When working with an empty set, Set.size returns 0. This behavior is demonstrated in the following code snippet:

```javascript

const set = new Set([]);

console.log(set.size); // Output: 0

```

The property calculates the number of unique values in the set, as shown in this example:

```javascript

const set = new Set([10, 10, 20, 40, 60, 60]);

console.log(set.size); // Output: 4

```

Set.size follows the SameValueZero algorithm for value equality, treating NaN as equal to itself while comparing other values according to the === operator's semantics. This ensures consistent comparison across different types of values, including primitives and object references.


## Syntax and Return Type

The syntax for accessing Set.size is simple: mySet.size, returning the number of elements in the set as a Number. This property returns the size of the set as a static value, making it easy to determine the number of unique elements at any point.

The size property can be used to get the current size of the set, similar to how array.length provides the number of elements in an array. For example:

```javascript

let mySet = new Set();

mySet.add(23);

mySet.add(12);

console.log(mySet.size); // Output: 2

```

When creating a set from an array or string, the size property reflects the number of unique elements. For instance:

```javascript

let mySet = new Set(["Tom", "Alsvin", "Eddie"]);

console.log(mySet.size); // Output: 3

```

The property works consistently across various data types. When used with a string, it counts each unique character:

```javascript

let mySet = new Set("javascript");

console.log(mySet.size); // Output: 10

```

The size property is particularly useful for checking if a set contains any elements, returning 0 for an empty set:

```javascript

let mySet = new Set([]);

console.log(mySet.size); // Output: 0

```


## Behavior with Duplicates

The Set.size property accurately reflects the number of distinct elements in a set, ignoring any duplicates that may be added. For example, when creating a set with multiple occurrences of the same value (like [10, 10, 20, 40, 60, 60]), it reports 4 unique elements: 10, 20, 40, and 60.

The property maintains consistent behavior across various operations and data types. When working with an empty set, it returns 0 as expected. This is demonstrated in the following examples:

```javascript

const set = new Set([]);

console.log(set.size); // Output: 0

const set = new Set([10, 10, 20, 40, 60, 60]);

console.log(set.size); // Output: 4

```

The SameValueZero algorithm governs value equality within the set, treating NaN as equal to itself while comparing other values according to the === operator's semantics. This ensures consistent comparison across different types of values, including primitives and object references:

```javascript

const set = new Set([NaN, 1, 2]);

console.log(set.size); // Output: 2

```

The size property remains unchanged after performing operations that do not add new unique elements. For instance, attempting to add an already existing element returns false and does not affect the size:

```javascript

const set = new Set([1, 2, 3]);

console.log(set.size); // Output: 3

const success = set.add(1); // Add existing element

console.log(success); // Output: false

console.log(set.size); // Output: 3

```

Comparisons with other collection types demonstrate the property's unique functionality. While Array.length returns the number of elements in an array, Set.size specifically counts unique elements in a set, making it particularly useful for detecting duplicates or ensuring data uniqueness:

```javascript

const array = [1, 2, 3, 3, 4];

console.log(array.length); // Output: 5

const set = new Set(array);

console.log(set.size); // Output: 4

```


## Browser Support

All major browsers supported Set.size from June 2017, with implementation across Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. The feature has robust browser compatibility, with support dating back to July 2015.

The property works consistently across various types of input. When creating a set from an array or string, it returns the number of unique elements. For instance, `new Set(["Tom", "Alsvin", "Eddie"])` returns a size of 3, while `new Set([])` returns 0 for an empty set.

Set.size is an ECMAScript 2026 Language Specification feature, providing a reliable method for determining the number of distinct elements in a set. This functionality enables developers to efficiently manage and query unique data collections.


## Comparison with Array.length

The key difference between Set.size and array.length lies in their respective implementations and intended use cases. While array.length returns the number of elements in an array, including any undefined values, Set.size specifically counts the number of unique elements in a set.

This distinction is crucial, as demonstrated by the following examples:

```javascript

const array = ['car1', 'car2', 'car3', undefined, 'car100'];

console.log(array.length); // Outputs 97, as it counts all elements, including undefined

const set = new Set(array);

console.log(set.size); // Outputs 5, as it counts only the unique values

```

In array.length's implementation, the property reflects the total count of elements, including undefined or repeated values. In contrast, Set.size provides a reliable method for determining the number of distinct elements, as shown in the example below:

```javascript

const set = new Set([10, 10, 20, 40, 60, 60]);

console.log(set.size); // Outputs 4, correctly counting unique elements

const array = [1, 2, 3, 3, 4];

console.log(array.length); // Outputs 5, counting all elements

const arraySet = new Set(array);

console.log(arraySet.size); // Outputs 4, counting unique elements

```

This differentiation makes Set.size particularly useful for detecting duplicates or ensuring data uniqueness, while array.length remains a valuable tool for determining the total number of elements in an array. The property's implementation across various data types ensures consistent behavior, whether working with primitive values, object references, or mixed collections.

