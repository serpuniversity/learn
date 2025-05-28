---

title: JavaScript Array entries() Method

date: 2025-05-26

---


# JavaScript Array entries() Method

JavaScript's Array.entries() method offers a powerful way to iterate over array elements, providing direct access to both index and value through key-value pairs. This introduction will explore how entries() works with different array types, including sparse arrays and array-like objects, and showcase its integration with modern JavaScript features like destructuring and the spread operator. We'll also examine its browser compatibility and performance advantages, demonstrating why entries() is a valuable addition to any JavaScript developer's toolkit.


## Array entries() Basics

The Array.entries() method returns a new Array iterator object containing key/value pairs for each index in the array, consisting of an array where each sub-array contains a key and its corresponding value. When called on a standard array, it generates an iterator that yields these index-value pairs in sequence, starting from index 0 and incrementing by 1.

The iterator object returned by Array.entries() contains a built-in next() method, which returns an object with two properties: done (a boolean indicating whether iteration has completed) and value (an array containing the current index and value pair). This iterator works seamlessly with sparse arrays, treating empty slots as undefined and allowing iteration over both standard and sparse arrays.

Array.entries() provides several useful features when working with arrays. It can be used directly with the for...of loop to access both index and value of each element, as demonstrated in the example where "Tech", "On", "The", and "Net" are iterated through using entries(). The method also supports array destructuring within the loop, as shown in the TypeScript example where student names and indices are accessed simultaneously. Additionally, entries() can be combined with the spread operator to create a new array of index-value pairs or used in conjunction with array methods for more complex data manipulations.


## Usage with for...of Loop

The for...of loop, when used with Array.entries(), allows direct access to both the index and value of each element in a sequence. This method returns an iterator that yields key-value pairs, making it particularly useful for iterating over arrays and accessing their indices alongside the values.

As demonstrated in the TypeScript example, this pattern enables clear and concise iteration through arrays:

```javascript

const students: string[] = ["Pankaj", "Ram", "Shravan"];

const iterator = students.entries();

for (let entry of iterator) {

    const [index, value] = entry;

    console.log(`Index: ${index}, Value: ${value}`);

}

```

This results in output that clearly shows each student's index and name:

```

Index: 0, Value: Pankaj

Index: 1, Value: Ram

Index: 2, Value: Shravan

```

The method also supports advanced use cases through combination with other array features. For instance, it can be used in conjunction with array destructuring and the spread operator for more complex manipulations:

```javascript

const languages = ["HTML", "CSS", "JavaScript", "ReactJS"];

const iterator = languages.entries();

for (const [index, language] of iterator) {

    console.log(`Language at index ${index}: ${language}`);

}

```

This pattern works seamlessly across modern browsers, including Chrome, Edge, Firefox, Opera, and Safari, as well as providing support for array-like objects and iterable structures.


## Integration with Array Destructuring

The entries() method in JavaScript returns an iterator containing key/value pairs for each index in the array. When combined with array destructuring, it offers a powerful way to access both the index and value of each element.

Here's an example demonstrating basic usage:

```javascript

const fruits = ["Banana", "Orange", "Apple", "Mango"];

let iterator = fruits.entries();

for (let entry of iterator) {

    console.log(entry);

}

```

This outputs:

```

[0, 'Banana']

[1, 'Orange']

[2, 'Apple']

[3, 'Mango']

```

By combining entries() with array destructuring, we can access both index and value simultaneously:

```javascript

const foods = ["pizza", "burger", "pasta"];

let entriesIterator = foods.entries();

for (let [index, food] of entriesIterator) {

    console.log(`Food at index ${index}: ${food}`);

}

```

This produces the output:

```

Food at index 0: pizza

Food at index 1: burger

Food at index 2: pasta

```

Destructuring can also integrate with the spread operator to create new arrays:

```javascript

const numbers = [1, 2, 3];

const allEntries = [...numbers.entries()];

console.log(allEntries);

```

This example demonstrates combining entries() with other array methods for more complex manipulations:

```javascript

const names = ["Alice", "Bob", "Charlie"];

const filteredEntries = [...names.entries()].filter(([index, name]) => name.startsWith('A'));

console.log(filteredEntries);

```

The entries() method works with all modern browsers since Chrome 38, Edge 12, Firefox 28, Safari 8, and Opera 25. It supports both dense and sparse arrays, returning undefined for indexes without defined values in non-array objects. The returned iterator can be used in for...of loops, while keeping the original array unchanged and providing efficient access to index-value pairs.


## Iteration Features and Examples

The Array.entries() method returns an iterator that yields key-value pairs for each index in the array, making it particularly useful for iterating over arrays while maintaining access to both index and value. This iterator can be used directly in for...of loops for simple key-value pair iteration or with other array methods for more complex manipulations.

For example, consider the following code that demonstrates basic usage:

```javascript

const languages = ["HTML", "CSS", "JavaScript", "ReactJS"];

const iterator = languages.entries();

for (const [index, language] of iterator) {

    console.log(`Language at index ${index}: ${language}`);

}

```

This produces the output:

```

Language at index 0: HTML

Language at index 1: CSS

Language at index 2: JavaScript

Language at index 3: ReactJS

```

The method also supports advanced use cases through combination with other array features. For instance, it can be used in conjunction with the spread operator to create new arrays:

```javascript

const numbers = [1, 2, 3];

const allEntries = [...numbers.entries()];

console.log(allEntries);

```

This example demonstrates combining entries() with other array methods for more complex manipulations:

```javascript

const names = ["Alice", "Bob", "Charlie"];

const filteredEntries = [...names.entries()].filter(([index, name]) => name.startsWith('A'));

console.log(filteredEntries);

```

Modern browsers support Array.entries() starting from Chrome 38, Edge 12, Firefox 28, Safari 8, and Opera 25. It works with both dense and sparse arrays, returning undefined for indexes without defined values in non-array objects. The returned iterator can be used with for...of loops while keeping the original array unchanged, providing efficient access to index-value pairs.


## Browser Support and Compatibility

The Array.entries() method returns an iterator that works with both dense and sparse arrays, maintaining compatibility across various data structures. When called on an array, it generates an iterator yielding key-value pairs, where each pair consists of an array containing the current index and value. The method supports iteration over array-like objects, returning undefined for indexes without defined values in non-array objects.

The browser compatibility for Array.entries() extends back to July 2015, with support in Chrome 38, Edge 12, Firefox 28, Safari 8, and Opera 25. The method works consistently with all modern browsers, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. Internet Explorer does not support this feature.

The iterator created by Array.entries() can be used directly with the for...of loop for simple key-value pair iteration. It maintains the original array structure unchanged while providing efficient access to index-value pairs. The returned iterator object includes a next() method that returns an object with two properties: done (a boolean indicating whether iteration has completed) and value (an array containing the current index and value pair). This functionality works with array-like objects, iterating through them as specified in the ECMAScript Language Specification.

For developers working with older browser versions or non-array objects, the Array.prototype.entries.call() method allows calling entries() on array-like objects. This approach ensures compatibility while maintaining the benefits of the entries() functionality. The method's support for sparse arrays and array-like objects makes it a versatile tool for modern JavaScript development, particularly when working with dynamic data structures.

