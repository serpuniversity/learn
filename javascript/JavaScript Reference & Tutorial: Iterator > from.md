---

title: JavaScript Iterators and Iterables

date: 2025-05-27

---


# JavaScript Iterators and Iterables

JavaScript's iterator and iterable features transform the language into a powerful tool for sequence processing and data manipulation. From simple array iteration to complex custom collection traversal, these mechanisms enable developers to work with data in flexible, stateful ways. The iterator protocol provides a consistent interface for accessing sequence elements, while built-in support for iterables makes it easy to work with arrays, strings, and other collections. For those building custom data structures or implementing advanced iteration logic, JavaScript's iterator framework offers a robust foundation for creating efficient, maintainable code.


## Iterator Fundamentals

An iterator in JavaScript is an object that implements the Iterator protocol through its `next()` method. This method returns an object containing two properties: `value`, which holds the current element in the sequence, and `done`, a boolean indicating whether the iteration has completed.

When the iterator is first created, calling `next()` returns an object with `value` representing the initial element and `done` set to false. Subsequent calls move to the next element in the sequence, updating the `value` property accordingly. The iterator continues processing until it reaches the end of the sequence, at which point `value` becomes `undefined` and `done` is set to `true`. Subsequent calls to `next()` return the same object with `value` set to `undefined` and `done` set to `true`, indicating the end of iteration.

To implement a custom iterator, developers typically use a closure to maintain state between calls to the `next()` method. The method returns an object with `value` and `done` properties, allowing for fine-grained control over iteration behavior. Common patterns include using an index variable to track progress through an array or collection, returning key-value pairs for object iteration, and implementing custom logic to control sequence traversal.

JavaScript provides several built-in iterator implementations for common data structures. Arrays, strings, and certain collection objects like Map and Set automatically generate iterators through their `Symbol.iterator` methods. These built-in iterators enable straightforward iteration using standard language features like the `for...of` loop. However, for more complex data structures or custom iteration logic, developers must implement their own iterator objects.


## Symbol.iterator and Built-in Iterables

JavaScript objects become iterable through the Symbol.iterator method, which serves as the entry point for iteration. When an object needs to be iterated, its Symbol.iterator method is called with no arguments, returning an iterator object that provides access to the object's contents.

The Symbol.iterator method returns an iterator object that follows a specific structure: on each call to its next() function, it must return an object containing two properties: value and done. The value property holds the current element in the sequence, while the done property is a boolean indicating whether the iteration has completed. When the iteration has finished, value becomes undefined and done is set to true.

This mechanism applies to built-in iterable types like arrays and strings. For example, accessing an array's Iterator through its Symbol.iterator property allows for iteration using the for...of loop:

```javascript

var temp = [1,2,3]

var iterator = temp[Symbol.iterator]()

for (let value of iterator) { console.log(value) }

```

In addition to arrays, strings, and typed arrays, other built-in iterables include map and set collections. These objects automatically implement the Symbol.iterator method, enabling straightforward iteration using standard language features. However, plain objects require explicit implementation of this method to become iterable.

The process of obtaining an iterable object follows a simple pattern: first, the Symbol.iterator method is called on the target object. If the method is not defined directly on the object, the search shifts to its prototype chain. For JavaScript's native data structures, this prototype chain ultimately points to the built-in iterator methods defined on:Array.prototype, String.prototype, or Map.prototype (for example).

The resulting iterator object can be used with various JavaScript features that expect an iterable, including the for...of loop and spread syntax. When used in these contexts, the iterator's next() method is called internally to retrieve each value in sequence, making it easy to work with iterables while abstracting away the underlying iteration logic.


## Custom Iterator Implementation

Creating custom iterators requires careful management of state across multiple calls to the next() method. The basic structure involves maintaining an internal index or pointer that tracks the current position within the collection. For example, a simple counter iterator might look like this:

```javascript

function makeIterator(array) {

  let nextIndex = 0;

  return {

    next() {

      return nextIndex < array.length ? {

        value: array[nextIndex++],

        done: false

      } : {

        done: true

      };

    }

  };

}

```

This implementation uses a closure to encapsulate the current index, ensuring that each iteration step advances correctly from the previous call. More complex logic can be implemented using similar patterns, often involving additional state variables or more sophisticated data structures.

For custom iterable objects, developers typically implement the Symbol.iterator method to define their own iteration behavior. This method returns an iterator object that implements the next() method according to the specific requirements of the collection. For instance, the following example demonstrates an iterator that processes elements in reverse order:

```javascript

class SimpleClass {

  #data;

  constructor(data) {

    this.#data = data;

  }

  [Symbol.iterator]() {

    let nextIndex = this.#data.length - 1;

    return {

      next() {

        if (nextIndex < 0) return { done: true };

        return { value: this.#data[nextIndex--], done: false };

      }

    };

  }

}

```

This class provides a simple example of how to implement custom iterable behavior, ensuring that each iteration produces the correct sequence while maintaining proper state between call invocations.

When creating complex iterable objects, developers must be aware of potential issues with concurrent modifications during iteration. Built-in iterator implementations use a copying strategy to maintain iteration safety, but custom implementations need explicit management of these scenarios. For example, the provided documentation includes an implementation that uses a tombstone value to handle deletions while preserving iteration ordering:

```javascript

class MyIterable {

  #data;

  constructor(data) {

    this.#data = data;

  }

  delete(deletedKey) {

    for (let i = 0; i < this.#data.length; i++) {

      if (this.#data[i][0] === deletedKey) {

        this.#data[i] = tombstone;

        return true;

      }

    }

    return false;

  }

  *[Symbol.iterator]() {

    for (let i = 0; i < this.#data.length; i++) {

      if (this.#data[i] !== tombstone) {

        yield this.#data[i];

      }

    }

  }

}

```

This implementation demonstrates how to safely handle deletions within an iterable structure, ensuring that iteration continues correctly even when elements are modified during processing.


## For...of Loop Compatibility

Iterator methods provide powerful functionality for working with iterable objects, including built-in tools for modifying and filtering sequences during iteration. The `.map()` method creates a new iterator helper object that transforms each element in the original iterator using a provided mapping function. Similarly, the `.filter()` method produces an iterator yielding only elements for which a given filtering function returns truthy.

Built-in iterator objects can be looped over using the for...of syntax, demonstrating JavaScript's flexible handling of custom iteration logic. For example, an array can be iterated over using either a standard for loop or a for...of loop:

```javascript

let arr = [1, 2, 3];

for (let i = 0; i < arr.length; i++) {

  console.log(arr[i]);

}

for (let value of arr) {

  console.log(value);

}

```

Both approaches produce identical output, demonstrating the language's ability to adapt standard iteration patterns to work with custom iterator implementations.

Nested iterable processing becomes particularly powerful when combined with generator functions and the yield* syntax. This capability allows for complex data structures to be processed in a sequential, controlled manner:

```javascript

function* nestedGenerator() {

  yield* [1, 2, 3];

  yield* [4, 5, 6];

}

for (let value of nestedGenerator()) {

  console.log(value);

}

```

This example demonstrates how generators can process multiple nested collections while maintaining the overall flow of iteration.

Data generation capabilities are a key strength of JavaScript's iterator system. For instance, a simple range operator can be implemented using generator functions:

```javascript

function* range(start, end, inc) {

  for (let i = start; i < end; i += inc) {

    yield i;

  }

}

for (let value of range(1, 10, 2)) {

  console.log(value);

}

```

This implementation demonstrates how generators can be used to create custom data generation functions, extending the built-in iterator functionality.

The Iterator protocol also supports advanced state management techniques. For example, a counter function can be implemented using generator functions to maintain internal state between iteration steps:

```javascript

function* counter(start = 0) {

  let current = start;

  while (true) {

    yield current++;

  }

}

const it = counter();

console.log(it.next().value); // 0

console.log(it.next().value); // 1

```

This example illustrates how generators can be used to implement state machines, providing a flexible alternative to external state management libraries.


## Generators and Iterable Enhancements

Generators provide an advanced iteration framework that extends JavaScript's iterator capabilities. These functions use the `function*` syntax and the `yield` keyword to create a special iterator that can be reused across multiple iteration steps. While standard iterators require explicit termination with `{done: true}`, generators automatically handle iteration completion and provide a more expressive way to write iterative algorithms.

Key features of generator functions include:

- Suspension point: The `yield` keyword allows execution to pause at specific points, returning control to the calling context. This enables generators to produce multiple values over multiple calls to their `next()` method.

- State preservation: Generator functions maintain their internal state between calls, allowing complex iteration logic to be implemented using closure-scoped variables.

- Cleanup mechanisms: The `finally` block ensures proper cleanup code is executed when generators are suspended or terminated, preventing resource leaks in asynchronous operations.


### Iterable Interface and Iterator Protocols

JavaScript's iterable interface requires objects to implement the `Symbol.iterator` method, which returns an iterator object conforming to the Iterator protocol. This protocol mandates that iterator objects return objects with `value` and `done` properties on each call to their `next()` method. The `value` property holds the current element, while `done` indicates whether iteration has completed.

User-defined iterable objects can implement custom iteration logic by returning new iterator objects for each invocation. This approach allows advanced state management and multiple iteration passes over the same data structure. For example, the following custom iterable class demonstrates stateful iteration using private properties:

```javascript

class CustomIterable {

  #data = [1, 2, 3];

  [Symbol.iterator]() {

    let index = 0;

    return {

      next() {

        return index < this.#data.length ? { value: this.#data[index++], done: false } : { done: true };

      }

    };

  }

}

```


### Iterator Helpers and Collection Operations

The iterator system includes a collection of helper methods for common iteration patterns. These methods operate on iterator objects and provide functional programming capabilities without modifying the underlying data structure. For example:

```javascript

function* generateNaturalNumbers(start = 0, step = 1) {

  let current = start;

  while (true) {

    yield current++;

  }

}

for (let number of generateNaturalNumbers(1, 2)) {

  console.log(number);

}

```

The example above demonstrates a generator function used to create an infinite sequence of natural numbers with customizable start and step values. This approach enables concise implementation of complex iteration logic while maintaining the iterator protocol's core principles.

