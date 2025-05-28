---

title: JavaScript Set: entries

date: 2025-05-26

---


# JavaScript Set: entries

A JavaScript Set is a powerful data structure for managing unique values. Whether you're removing duplicates from an array or performing complex set operations, understanding how to work with Sets is essential. In this article, we'll explore how to create and manipulate Sets, including how to use the `entries()` method for iterating through their contents. We'll also look at Set operations, properties, and methods, along with practical examples to help you master this fundamental JavaScript feature.


## JavaScript Set Overview

The JavaScript Set is a collection specifically designed to store unique values, with each value occurring only once in the collection. This data structure is particularly useful for managing collections of distinct items, performing membership checks, and finding sets' intersections and differences.


### Creating a Set

A Set can be created in several ways. The most common approach is to pass an array to the Set constructor:

```javascript

const numberSet = new Set([1, 2, 3, 2]); // Only 1, 2, 3 will be stored, as Sets automatically remove duplicates

```

Alternatively, you can create an empty Set and use the `add()` method to populate it:

```javascript

const mySet = new Set();

mySet.add("John");

mySet.add("Sherlock");

mySet.add("Watson");

mySet.add("Moriarty");

console.log(mySet); // Output: Set(3) {"John", "Sherlock", "Watson"}

```


### Set Operations

The Set object provides several methods for managing its contents. To check if a value exists, use `has()`. To remove a value, use `delete()`. The `size` property indicates how many unique elements are in the set.

JavaScript Sets maintain the order of elements based on their insertion sequence, which can be convenient for predictable iteration. They support advanced operations like union, intersection, and difference, making them a powerful tool for various data processing needs.


## Creating a Set

The `Set()` constructor creates Set objects in JavaScript. It can be called with or without an iterable object as an argument. If an iterable object is provided, all of its elements are added to the new Set. If no iterable object is provided or its value is null, the new Set is empty.

Creating a Set is straightforward using the constructor with an array:

```javascript

const numberSet = new Set([1, 2, 3, 2]); // Only 1, 2, 3 will be stored, as Sets automatically remove duplicates

```

Alternatively, you can create an empty Set and use the `add()` method to populate it:

```javascript

const mySet = new Set();

mySet.add("John");

mySet.add("Sherlock");

mySet.add("Watson");

mySet.add("Moriarty");

console.log(mySet); // Output: Set(3) {"John", "Sherlock", "Watson"}

```


### Creating Sets from Iterables

Sets can be initialized using any synchronous iterable, including arrays, strings, and iterators. The spread syntax can be used to initialize sets from iterables:

```javascript

const arraySet = new Set([1, 2, 3, 2]); // Only 1, 2, 3 will be stored

console.log(arraySet); // Output: Set(3) {1, 2, 3}

```

Strings are also iterable, so you can create a set from them directly:

```javascript

const charSet = new Set("javascript");

console.log(charSet); // Output: Set(8) {"j", "a", "v", "a", "s", "c", "r", "i"}

```


### Generator Support

Generators can be used to create sets, and the Set constructor can filter out repeated values from a generator:

```javascript

function* generateValues() {

  yield 1;

  yield 2;

  yield 1;

  yield 3;

}

const generatorSet = new Set(generateValues());

console.log(generatorSet); // Output: Set(3) {1, 2, 3}

```


### Iteration and Size

The `size` property returns the number of unique elements in the set. You can list all elements using a `for..of` loop:

```javascript

const letters = new Set(["a","b","c"]);

let text = "";

for (const x of letters) {

    text += x;

}

console.log(text); // Output: "abc"

```


### Object-Based Sets

While not recommended due to potential limitations, JavaScript sets can be created using objects with property names as values:

```javascript

let set = {};

if (!'Tom' in set) {

  set.Tom = true;

}

```

However, this approach is generally less efficient and less idiomatic than using the `Set` constructor. Modern JavaScript practice strongly recommends using the `Set` constructor for creating sets.


## Set Methods and Properties


### Implementation Considerations

The `Set` object provides a robust foundation for working with collections of unique values, implementing methods and properties that enable efficient value management and iteration. Developers should be aware that while basic operations like checking membership (`has()`) and adding elements (`add()`) are straightforward, more complex operations require careful implementation due to the underlying object-oriented nature of JavaScript.


### Custom Implementation

Implementing a custom set-like structure requires careful attention to several key aspects: ensuring the correct implementation of the `size` property, providing a reliable `has()` method, and implementing the `keys()` method to return an iterator of the set's elements. The text "Ways to create a Set in JavaScript" illustrates both correct and incorrect approaches, demonstrating that while ES6 introduced standardized support for Sets, developers still need to understand the underlying principles to implement equivalent functionality in older environments.


### Browser Compatibility

All major modern browsers support Sets, with the feature availability dating back to July 2015. However, Internet Explorer does not support Sets, and developers working across platforms should ensure compatibility. The `Set` object inherits from `Set.prototype`, which provides essential methods and properties for common operations, making it a versatile tool for various JavaScript applications.


## The entries() Method

The `entries()` method returns an iterator object containing [value, value] arrays for each element in the set, providing a convenient way to access all elements while maintaining the order of insertion. The method conforms to the specification for iterable objects, making Sets compatible with other iterable structures in JavaScript.

When called, `entries()` returns an iterator object with the following properties:

- `next()`: Returns an object with `value` and `done` properties. The `value` property contains the next array `[value, value]`, and `done` is false until all entries have been iterated over.


### Iteration Example

```javascript

const set1 = new Set();

set1.add(42);

set1.add("forty two");

const iterator1 = set1.entries();

for (const entry of iterator1) {

  console.log(entry); // Array [42, 42]

  console.log(entry); // Array ["forty two", "forty two"]

}

```


### Performance Considerations

The `entries()` method maintains O(1) time complexity for accessing elements, making it efficient for iterating through sets. It returns the elements in the order they were inserted, which can be crucial for maintaining data integrity during operations.


### Browser Support

The method is supported across modern browsers since June 2017, with full compatibility dating back to July 2015. Internet Explorer, however, does not support this feature, and developers should ensure compatibility in cross-browser environments.


## Browser Support

All major modern browsers support Sets, with full compatibility since June 2017. The feature availability dates back to July 2015, though Internet Explorer does not support Sets and lacks some of the ES6 features. Sets inherit from Set.prototype, which provides essential methods and properties for common operations.

The Set constructor can initialize sets from various sources, including arrays, strings, and iterators. For example, you can create a set from a string using `new Set("firefox")`, which results in a set containing each character as a unique value. The order of elements in a set follows their insertion sequence, which is particularly important for maintaining data integrity during operations.

The `entries()` method returns an iterator object containing [value, value] arrays for each element in the set, making Sets compatible with other iterable structures in JavaScript. When called, it returns an iterator object with a `next()` method that returns an object with `value` and `done` properties. The `value` property contains the next array `[value, value]`, while `done` is false until all entries have been iterated over. This method maintains O(1) time complexity for accessing elements, ensuring efficient iteration through sets.

