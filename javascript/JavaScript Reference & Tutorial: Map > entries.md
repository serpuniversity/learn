---

title: JavaScript Map entries() Method

date: 2025-05-26

---


# JavaScript Map entries() Method

In JavaScript, the `Map` data structure provides a robust way to store and manipulate collections of key-value pairs. As part of the ECMAScript 6 (ES6) standard, the `Map` API includes several useful methods for managing these collections, such as `set`, `get`, and `delete`. However, when it comes to iterating over the contents of a Map, developers face an important choice: should they use the simpler `keys()` and `values()` methods, or opt for the more comprehensive `entries()` method?

This article examines the `entries()` method in depth, highlighting its capabilities and usage patterns. We'll explore how it returns an iterator containing the `[key, value]` pairs for each element in the map, maintaining the insertion order. Along the way, we'll compare `entries()` to other iteration methods, discuss its browser support, and show how it enables more flexible processing of map data.


## Introduction to Map Entries

The `entries()` method returns an iterator object containing the `[key, value]` pairs for each element in a JavaScript Map. This method does not modify the original map. The syntax is `map.entries()`, with no parameters. The method returns an iterable object representing the map's entries.

The method was introduced in ECMAScript 6 (ES6), which was supported in all modern browsers since June 2017. Current browser support includes:

- Chrome 51

- Edge 15

- Firefox 54

- Safari 10

- Opera 38

Internet Explorer does not support `map.entries()`.

This method is particularly useful when you need to iterate over the key-value pairs of a Map in the order they were inserted. Here's how you can use it:

```javascript

let myMap = new Map();

myMap.set(0, 'geeksforgeeks');

myMap.set(1, 'is an online portal');

myMap.set(2, 'for geeks');

let iterator_obj = myMap.entries();

console.log(iterator_obj.next().value); // [0, 'geeksforgeeks']

console.log(iterator_obj.next().value); // [1, 'is an online portal']

console.log(iterator_obj.next().value); // [2, 'for geeks']

```

In this example, the `myMap.entries()` call returns an iterator object that yields each key-value pair in the map. The `next().value` method retrieves the next pair, showing how the entries method maintains the insertion order of the map.


## Usage and Examples

The entries() method returns an iterable iterator object containing the [key, value] pairs for each element in the map, maintaining the insertion order. This allows developers to access and process the key-value pairs in the sequence they were originally added to the map.


### Iterating with for...of Loops

The for...of loop provides a simple way to iterate over the key-value pairs returned by entries(). Here's an example demonstrating this usage:

```javascript

let myMap = new Map();

myMap.set(0, 'geeksforgeeks');

myMap.set(1, 'is an online portal');

myMap.set(2, 'for geeks');

for (let entry of myMap.entries()) {

  console.log(entry);

}

// Output:

// [0, 'geeksforgeeks']

// [1, 'is an online portal']

// [2, 'for geeks']

```

This loop directly iterates over the [key, value] pairs, making it straightforward to process each entry in the map.


### Using Array.from for Conversion

While entries() returns an iterator, sometimes you need to work with an actual array of [key, value] pairs. The Array.from function provides a simple way to convert the iterator to an array:

```javascript

let myMap = new Map();

myMap.set('name', 'Mozilla');

myMap.set('url', 'https://www.mozilla.org');

let entriesArray = Array.from(myMap.entries());

console.log(entriesArray);

// Output: [["name", "Mozilla"], ["url", "https://www.mozilla.org"]]

```

This conversion allows you to use array-specific methods or easily pass the data to functions expecting an array.


### Side-by-Side Comparison

For comparison with other iteration methods, here's how you might use entries() versus keys() and values():

```javascript

let myMap = new Map();

myMap.set('a', 1);

myMap.set('b', 2);

myMap.set('c', 3);

console.log([...myMap.entries()]); // [["a", 1], ["b", 2], ["c", 3]]

console.log([...myMap.keys()]);   // ["a", "b", "c"]

console.log([...myMap.values()]); // [1, 2, 3]

```

While keys() and values() provide simpler iteration patterns (returning just keys or values), entries() offers the full [key, value] pair information in the order they were inserted.


## Browser Support

The `entries()` method returns a MapIterator object containing the [key, value] pairs for each element in the map, maintaining the insertion order. This method is available across modern browsers since June 2017, as indicated by the browser support data provided in the ECMAScript 6 implementation.

This iterator can be used to directly access the key-value pairs in the order they were added to the map. For example:

```javascript

let myMap = new Map();

myMap.set('name', 'Mozilla');

myMap.set('url', 'https://www.mozilla.org');

let iteratorObj = myMap.entries();

console.log(iteratorObj.next().value); // ["name", "Mozilla"]

console.log(iteratorObj.next().value); // ["url", "https://www.mozilla.org"]

```

The method also allows developers to convert the iterator to an array using Array.from, facilitating easy processing of the map's entries:

```javascript

let entriesArray = Array.from(myMap.entries());

console.log(entriesArray);

// Output: [["name", "Mozilla"], ["url", "https://www.mozilla.org"]]

```

Despite its wide support in modern browsers, `map.entries()` is not available in Internet Explorer, aligning with the ECMAScript 6 implementation notes that the technology is experimental and may not be fully supported in all environments.


## Comparison with Other Iteration Methods

The `entries()` method returns an iterator containing the [key, value] pairs for each element in the map, maintaining insertion order. This differs from the `keys()` and `values()` methods, which return iterators containing only keys and values, respectively.


### Key Differences in Return Values

The `entries()` method provides full key-value pair information, while `keys()` and `values()` return simpler iterators. Here's a comparison in action:

```javascript

let myMap = new Map();

myMap.set('name', 'Mozilla');

myMap.set('url', 'https://www.mozilla.org');

console.log([...myMap.entries()]); // [["name", "Mozilla"], ["url", "https://www.mozilla.org"]]

console.log([...myMap.keys()]);   // ["name", "url"]

console.log([...myMap.values()]); // ["Mozilla", "https://www.mozilla.org"]

```


### Performance and Use Cases

The `Map` structure excels in scenarios requiring frequent additions and removals of key-value pairs. The `entries()` method enables efficient looping capabilities through its iterator protocol, supporting both direct iteration and function-based processing.

For instance, the `forEach()` method iterates over entries with a callback function that receives the value, key, and map object:

```javascript

myMap.forEach((value, key, map) => {

  console.log(`Key: ${key}, Value: ${value}`);

});

```

This structure facilitates easy replacement of `Map` with `Set` in scenarios where unique values are sufficient, as each value appears only once in a Set.


### Security Considerations

The `Map` object is designed for safe use with user-provided keys and values, unlike `Object`, which contains prototype keys that could collide with user values. This difference is crucial for preventing object injection attacks.


### Browser Support and Implementation Notes

The `entries()` method has been available since ECMAScript 6 and supports modern browsers, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. Internet Explorer does not support this method, aligning with the specification's requirements for efficient performance and data structure implementation.

