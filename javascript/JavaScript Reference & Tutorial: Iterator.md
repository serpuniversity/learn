---

title: Iterators and Iterables in JavaScript

date: 2025-05-26

---


# Iterators and Iterables in JavaScript

JavaScript's iterator and iterable features enable powerful and flexible collection traversal. While these concepts are fundamental to modern JavaScript development, mastering them unlocks advanced techniques for data processing and manipulation. This article explores the technical details of iterators and iterables, from their basic implementation to their role in JavaScript's iteration protocol. Along the way, we'll see how these mechanisms enable elegant solutions to common programming challenges, from custom collection types to efficient data processing pipelines.


## Iterator Fundamentals

Iterators and iterables are core JavaScript concepts that enable controlled iteration over collections. While not as well-known as functions or objects, iterators provide a powerful tool for flexible and controlled looping.

An iterator is an object returned by the Symbol.iterator method, containing a next() function that produces an object with value and done properties. Each call to next() returns the next value in the sequence and sets done to false until iteration completion, when value becomes undefined and done is true.

The Symbol.iterator key defines the default iterator for an object, typically implemented as a function returning the iterator object itself. When a collection's Symbol.iterator method is called, it returns an iterator object with two key properties: value (containing the current array element) and done (indicating completion with true).

Iterables implement the Symbol.iterator method to define their iteration behavior, allowing them to be used in for...of constructs. While not all collections can provide consumers directly, JavaScript's ES6 iteration protocol enables custom data structures to define their own iteration mechanisms. This allows greater control over the iteration process and enables developers to create custom constructs with standardized access to elements.

The built-in JavaScript methods map(), forEach(), and filter() utilize iterators internally to process collections, while language features like String objects and URLSearchParams objects implement default iterators that return code points or sequence elements one by one. Even plain objects, which are not inherently iterable, can be made iterable through custom iterator methods.

Understanding iterators and iterables unlocks greater innovation and efficiency in JavaScript development, providing a robust foundation for building flexible and powerful data traversal mechanisms.


## Iterator Protocol Implementation

The iterator protocol requires implementation of a `next()` method that returns an object with two key properties: `value` and `done`.

The `next()` method provides the next value in the sequence and indicates whether iteration has completed. The returned object contains `value`, which holds the current element, and `done`, a Boolean flag that becomes true when all values have been generated.

For example, consider an iterator processing an array `nums` [1, 5, 16]:

1. The first call to `iter.next()` returns `{ value: 1, done: false }`, indicating the start of iteration.

2. The second call returns `{ value: 5, done: false }`, continuing to the next element.

3. The third call produces `{ value: 16, done: false }`, completing the sequence before the final call.

4. The fourth call returns `{ value: undefined, done: true }`, marking the end of iteration.

While creating custom iterators requires advanced programming skills, JavaScript provides built-in iterators for certain data structures, handling their own iteration mechanisms internally.

The iterator object is typically generated through the Symbol.iterator method, which returns an iterator object containing a next() function. This function produces an object with value (containing the current array element) and done (indicating completion with true) upon each call.


## Built-in Iterators and their Use Cases

Arrays, strings, and other built-in JavaScript objects implement the iterator protocol through their respective methods. For arrays, the built-in iterator method returns an iterator object with a `next()` function that produces an object containing the current element and a `done` flag.

Strings, as iterable objects, implement their own iterator through the `@@iterator` symbol, returning code points one by one when iterated over. URLSearchParams objects demonstrate dynamic iterator behavior: when elements are deleted, the iterator changes its behavior to avoid skipping elements.

Custom iterables can implement their own iterator logic through the `[Symbol.iterator]` method. For example, consider an object that iterates over an array:

```javascript

const iterable = {

  values: [1, 2, 3, 4, 5],

  [Symbol.iterator]: function() {

    let index = 0;

    return {

      next: function() {

        if (index < this.values.length) {

          let temp = { value: this.values[index], done: false };

          index++;

          return temp;

        } else {

          return { value: undefined, done: true };

        }

      }.bind(this)

    };

  }

}

```

This custom iterable allows for controlled iteration over its values, with the iterator object maintaining its state between calls to `next()`. The `done` property becomes true when iteration is complete, and subsequent calls return an object with `value` set to `undefined`.

JavaScript's iterator protocol supports both finite and infinite sequences, allowing developers to create custom iteration mechanisms for their data structures. While not all collections can provide consumers directly, the built-in iteration protocol enables custom data structures to define their own iteration mechanisms, providing greater control over the iteration process and enabling the creation of complex data traversal patterns.


## Iterables and Iterable Objects

The `[Symbol.iterator]()` method enables objects to be used in `for...of` loops by returning an iterator object. Native JavaScript iterables, including arrays, strings, and ES6 Maps, implement this method to support iteration.

An iterable object contains a `[Symbol.iterator]()` method that returns an iterator object conforming to the iterator protocol. This method must return an object with `next()` and `return()` methods, allowing controlled access to the iterable's values. The `next()` method returns an object with `value` and `done` properties, where `done` becomes true when iteration completes.

To create a custom iterable, the `[Symbol.iterator]()` method can return either `this` (for single-iteration) or a new iterator (for multiple iterations). For example, the `IterableObject` class demonstrates this concept by implementing `[Symbol.iterator]()` to return `Object.values(this)`:

```javascript

const iterable = {

  values: [1, 2, 3, 4, 5],

  [Symbol.iterator]: function() {

    return Object.values(this);

  }

};

```

When working with iterators, it's important to note that they maintain state between calls to `next()`. The `IterableObject` example uses a closure to track the iteration state, as demonstrated in the following code:

```javascript

const myIterable = {

  i: 0,

  [Symbol.iterator]() {

    let that = this;

    return {

      next() {

        if (that.i < 5) {

          return { value: that.i++, done: false };

        } else {

          return { value: undefined, done: true };

        }

      }

    };

  }

};

for (let value of myIterable) {

  console.log(value);

}

```

This code generates the sequence 0, 1, 2, 3, 4, as expected. The `Symbol.iterator` property returns an iterator object with a `next()` method that produces values from 0 to 4 before completing.

JavaScript's built-in types provide native iterators through various methods. Arrays use `[@@iterator]()`, strings use `@@iterator`, and ES6 Maps provide `entries()`, `values()`, and `keys()` methods. These native implementations enable seamless integration with `for...of` loops and other iteration constructs.

When implementing custom iterables, it's crucial to follow the established iterator protocol. The `next` method must return an object implementing the `IteratorResult` interface, which consists of `done` (a boolean) and `value` properties. This standardized approach ensures compatibility with JavaScript's iteration mechanisms while allowing for custom iteration behavior.


## Advanced Iterator Topics

Concurrent modifications to iterables can affect iteration behavior. JavaScript's iterator protocol allows safe iteration even when underlying data changes. When an iterable is modified during iteration, the iterator may skip elements or produce unexpected results.

For example, consider an array being modified during iteration:

```javascript

const counter = { value: 0 };

const arr = [1, 2, 3, 4, 5];

for (let iterator = 0; iterator < 5; iterator++) {

  setTimeout(() => {

    console.log(arr[iterator]);

    counter.value++;

  }, 500);

}

setInterval(() => {

  arr.pop();

}, 1000);

```

This code attempts to log each array element in sequence. However, due to asynchronous execution and array modifications, the output may vary between runs. Concurrent modifications can lead to skipping elements or unexpected iteration behavior.

State management in custom iterators is crucial for maintaining correct iteration behavior. Iterators maintain their state between calls to next(), allowing them to track position and iteration progress. This state management enables efficient and controlled iteration over collections.

The `Symbol.iterator` property plays a key role in managing iterator state. Custom iterator implementations often use closures to capture iterator state, ensuring consistent behavior across multiple iterator invocations. The example code snippet demonstrates a simple counter mechanism using iterator state:

```javascript

let counter = 0;

for (let value of counter) {

  console.log(value); // Logs 0, 1, 2, 3, 4

  counter++;

}

```

In this example, the iterator state is maintained through a counter variable, ensuring each iteration returns the current value and increments the counter. Proper state management is essential for custom iterator implementations to function correctly across multiple iteration cycles.

