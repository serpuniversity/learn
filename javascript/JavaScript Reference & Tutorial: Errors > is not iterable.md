---

title: JavaScript Reference & Tutorial: Errors > is not iterable

date: 2025-05-26

---


# JavaScript Reference & Tutorial: Errors > is not iterable

In JavaScript, iteration is a fundamental mechanism for processing collections of data. Whether you're traversing an array, navigating through a map, or extracting values from an iterable object, the language provides powerful tools for sequence manipulation. However, when you encounter an error message indicating that something "is not iterable," you might be scratching your head—after all, you're working with what looks like a perfectly normal array or collection.

This guide demystifies the world of JavaScript iteration, explaining why some objects behave like collections while others do not. You'll learn about the built-in iterable structures, how to create custom iterables, and what to do when things go wrong. We'll walk through common error scenarios, show you how to handle unexpected data types gracefully, and provide best practices for debugging and error propagation. By the end, you'll understand why JavaScript objects are special—and how to work with them effectively in your code.


## Understanding JavaScript Iteration

JavaScript's iteration mechanism is rooted in the language's fundamental design choices. Unlike arrays, strings, maps, and other built-in iterable types, plain objects `{}` are not inherently iterable. This distinction is crucial for understanding iteration errors and how to address them.


### Built-in Iterable Structures

According to the specification, arrays, strings, maps, sets, and arguments objects are the primary iterable structures in JavaScript. These objects implement the `Symbol.iterator` method, returning an iterator that conforms to the iterable protocol. For example, a simple array like `[1, 2, 3]` is iterable because it has an `[Symbol.iterator]()` method:

```javascript

const xs = [1, 2, 3];

for (let value of xs) {

  console.log(value); // logs 1, 2, 3

}

```


### Plain Objects and Iteration

Plain objects behave differently. They are optimized as key-value stores, with no inherent order or sequence for their properties. As noted in the documentation, iterating over an object using `for...in` allows access to enumerable properties but does not guarantee a specific order:

```javascript

const obj = { a: 1, b: 2, c: 3 };

for (let prop in obj) {

  console.log(prop); // Could be "a", "b", or "c" in any order

}

```


### Custom Iterables

To create custom iterables, developers must implement the `[Symbol.iterator]()` method, which returns an iterator object conforming to the iterable protocol. This allows for precise control over iteration behavior. For instance, a simple implementation might yield values from 1 to 3:

```javascript

var myIterable = {};

myIterable[Symbol.iterator] = function* () {

  yield 1;

  yield 2;

  yield 3;

};

for (let value of myIterable) {

  console.log(value); // logs 1, 2, 3

}

```


### Handling Non-Iterable Objects

When working with objects that need to be iterable, developers should use methods like `Object.keys()`, `Object.values()`, or `Object.entries()` to work with their properties. These methods ensure compatibility across both plain objects and built-in iterable types:

```javascript

const nestedObject = { a: { e: 1, f: 2 }, b: { g: 3 }, c: { h: 4, i: 5 } };

for (let levelOneKey of Object.keys(nestedObject)) {

  console.log(levelOneKey); // logs "a", "b", "c"

  let levelTwoObj = nestedObject[levelOneKey];

  for (let levelTwoKey of Object.keys(levelTwoObj)) {

    console.log(levelTwoKey); // logs property keys for each level

    console.log(levelTwoObj[levelTwoKey]); // logs property values for each level

  }

}

```

Understanding these fundamentals is essential for developing robust JavaScript applications that handle data sequences and collections effectively.


## Common Error Scenarios

The inability to iterate over objects can manifest in several common scenarios:


#### Undefined or Null Values

JavaScript expects values to be iterable objects when used in `for...of` loops, array destructuring, or functions like `Promise.all`. Attempting to iterate over `undefined` or `null` values will result in a `TypeError`. For example, treating an undefined variable as an iterable will trigger this error:

```javascript

const maybeArray = undefined;

for (const value of maybeArray) {

  console.log(value); // TypeError: undefined is not iterable

}

```


#### API Response Handling

API responses are a frequent source of iteration errors. If a call returns an empty object, the subsequent attempt to iterate will fail. This can be particularly problematic when dealing with optional or conditionally returned data:

```javascript

fetch('/api/data')

  .then(response => response.json())

  .then(data => {

    if (data) {

      for (const key of Object.keys(data)) {

        console.log(key); // Possible TypeError if data is unexpectedly empty

      }

    }

  });

```


#### Incorrect Assumptions about Data Types

Developers often make assumptions about data types, particularly when working with dynamic or external data. For instance, treating a non-array object as an array can lead to errors:

```javascript

const data = { items: [1, 2, 3] };

for (const item of data.items) {

  console.log(item); // Potential TypeError if data.items is not an array

}

```


#### Generator and Iterator Wrapping

Generators and iterator wrappers can introduce complexity in error handling. The `[Symbol.iterator]()` method must be properly implemented to return an object with a `next()` method that returns an `IteratorResult`. Mismatches in these expectations can propagate errors throughout your code:

```javascript

function* simpleGenerator() {

  yield 1;

  yield 2; // Generator must not throw an error here

}

for (const value of simpleGenerator()) {

  console.log(value);

}

```

Understanding these common scenarios helps developers implement robust iteration logic that can handle unexpected data structures and runtime conditions.


## Error Handling and Debugging

To effectively handle iteration errors, developers should implement several best practices:


### Pre-Iteration Validation

Before attempting iteration, always validate the data type and structure. This prevents errors when working with optional or external data:

```javascript

function safeIteration(obj) {

  if (typeof obj !== 'object' || obj === null) {

    console.error('Invalid iterable: ', obj);

    return [];

  }

  return Object.keys(obj); // Safely returns valid keys

}

```


### Error Handling in Iterators

Generators and custom iterators should include comprehensive error handling. The `finally` block ensures proper cleanup, while proper exception handling prevents premature termination:

```javascript

function* safeGenerator() {

  try {

    yield 1;

    yield 2;

    yield 3;

  } finally {

    // Cleanup code here

  }

}

for (const value of safeGenerator()) {

  console.log(value);

}

```


### Propagation of Iterator Errors

Both built-in and custom iterators must propagate errors correctly. Ensure that thrown errors are properly caught and handled:

```javascript

function* safeIterable() {

  try {

    yield 1;

    yield 2;

    yield 3;

  } catch (error) {

    console.error('Iteration error: ', error);

  }

}

for (const value of safeIterable()) {

  console.log(value);

}

```


### Correct Iterator Implementation

Custom iterables must implement the `[Symbol.iterator]` method correctly, returning an iterator object that conforms to the protocol:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

  }

  [Symbol.iterator]() {

    return {

      next() {

        return { done: true, value: 42 }; // Correct implementation

      }

    };

  }

}

for (const value of new CustomIterable([1, 2, 3])) {

  console.log(value); // Logs 42

}

```


### Debugging Tools and Practices

Use browser developer tools and logging to trace iteration errors. Tools like the console and debugging breakpoints help identify where and why iteration fails:

```javascript

console.log('Before iteration');

for (const value of someData) {

  console.log(value);

  console.log('During iteration');

}

console.log('After iteration');

```

By following these best practices, developers can create more robust and error-resistant JavaScript applications that handle iteration effectively.


## Iterator Protocol Implementation

To implement the iterator protocol, an object must define the `Symbol.iterator` method, returning an iterator object that adheres to the protocol specifications. This method, when called, should return an iterator object with a `next()` method that returns an `IteratorResult` object. According to the MDN Web Docs, the `next()` method must:

1. Return an object implementing the `IteratorResult` interface

2. The `IteratorResult` interface requires two properties:

   - `done` (a boolean indicating whether the iterator has completed its sequence)

   - `value` (the current value, which can be omitted if `done` is true)

3. Optionally, the `next` method can receive a value, though built-in language features do not pass any value

The implementation must handle both finite and infinite sequences, maintaining a proper state between iterations. Concurrent modifications to the underlying data structure during iteration can affect the sequence of visited elements. For example, removing an element during iteration may cause subsequent elements to shift positions.

Here is a breakdown of key points based on the provided documentation:


### Implementation Requirements

The `Symbol.iterator` method:

- Must return an iterator object

- The iterator object must have a `next()` method

- The `next()` method must return an `IteratorResult` object with a `done` property and optional `value` property

- Built-in language features will not pass any value to the `next` method


### Iterable Behavior

When implementing custom iterables, consider the following behavior:

- Concurrent modifications during iteration can affect the sequence of visited elements

- For collections like `Map`, deleted keys are indicated using "tombstone" values rather than shifting remaining elements

- Implementing similar behavior requires defining a `tombstone` symbol and modifying the iterator to handle deleted keys appropriately


### Built-in Iterator Behavior

The iterator protocol is applied consistently across built-in iterable types. For instance:

- String iterables return code points one by one

- Array-like collections (NodeList, HtmlCollection) are iterable

- Arguments objects are iterable, while plain objects are not without custom implementation


### Implementation Examples

A correct implementation that returns an empty sequence looks like this:

```javascript

class CustomIterable {

  [Symbol.iterator]() {

    return {

      next() {

        return { done: true, value: 42 };

      }

    };

  }

}

```

An incorrect implementation that causes a TypeError:

```javascript

const myInvalidIterable = {

  [Symbol.iterator]() { return 42; }

};

```


### Nested Iteration

Custom iterables can handle nested structures using methods like `Object.entries()` and recursion. For example:

```javascript

function* iterateNested(obj) {

  for (let [key, value] of Object.entries(obj)) {

    if (typeof value === 'object' && value !== null) {

      yield [key, ...[...iterateNested(value)]];

    } else {

      yield [key, value];

    }

  }

}

```

This approach maintains proper iterator behavior while handling complex data structures efficiently.


## Resources and Further Reading

Understanding why JavaScript objects are not iterable provides crucial insights into how to safely implement custom iterables and handle unexpected data structures. While `{}` objects cannot directly store ordered sequences, they excel at key-value storage and property lookup, making them distinct from built-in iterable types like arrays and maps.

For developers needing to iterate over objects, modern JavaScript offers several reliable methods. The `for...in` loop remains a fundamental tool, returning enumerable property names. When working with arrays of objects, `Object.keys()`, `Object.values()`, and `Object.entries()` offer particularly versatile solutions, each serving specific use cases.


### Custom Iterable Implementation

To create custom iterables, developers must implement the `Symbol.iterator` method, returning an iterator object that follows protocol specifications. Common pitfalls include incorrect iterator implementations and handling concurrent modifications. For example, the following code demonstrates a basic custom iterable:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

  }

  [Symbol.iterator]() {

    let index = 0;

    return {

      next() {

        if (index < this.data.length) {

          return { done: false, value: this.data[index++] };

        } else {

          return { done: true };

        }

      }

    };

  }

}

```


### Array-like Objects

Special attention is required when working with objects that "look like" arrays, such as `arguments`, NodeList, or HtmlCollection. These objects are technically iterable but require different handling than true arrays. Developers should use methods like `Array.from()` or `spread` syntax to convert them to true arrays when necessary.


### Future Directions

While the current implementation gap between `{}` objects and built-in iterables presents challenges, upcoming JavaScript versions may offer new solutions. The ES2015 specification introduced generator functions and the `await` keyword, demonstrating the ongoing evolution of JavaScript's Iterable interface and its relationship with {} objects.

