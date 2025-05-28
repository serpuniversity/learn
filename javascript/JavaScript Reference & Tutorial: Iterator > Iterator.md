---

title: JavaScript Iterators and Their Protocols

date: 2025-05-26

---


# JavaScript Iterators and Their Protocols

JavaScript's iterator system provides a powerful framework for sequence traversal through the Symbol.iterator protocol. This article explores the fundamentals of iterators, from their basic structure to advanced usage patterns. We'll examine how custom iterators can extend JavaScript's capabilities, leveraging both generator functions and iterator classes. Along the way, we'll see how these iterator mechanisms power built-in functions like Array.prototype.map() and enable multiple iteration passes over the same data.


## Iterator Fundamentals

JavaScript's iterator system enables structured traversal of collections through the Symbol.iterator protocol. At its core, an iterator object implements a next() method that returns an object containing two key properties: value and done. The value property holds the current element of the sequence, while the done property indicates whether the iteration has completed (true) or is still ongoing (false).

To function correctly, iterators must adhere to specific syntax requirements. When creating an iterator, developers must bind the Symbol.iterator method to the appropriate context, as direct calls without binding can result in TypeError: Cannot convert undefined or null to object. For example, to obtain an iterator for an array, one must use array[Symbol.iterator].bind(array), ensuring proper context for method execution.

The iterable protocol extends this functionality by allowing objects to define their own iteration behavior through the Symbol.iterator method. This method returns an iterator object with a next() function, which must produce output in the format {value: any, done: boolean}. Built-in JavaScript types such as arrays, strings, maps, and sets all implement this protocol through their respective [Symbol.iterator] methods.

Developers can implement custom iterators through generator functions or iterator classes. Generator functions, which use function* syntax and the yield keyword, offer a convenient way to produce iterators with controlled state. For example, a simple custom iterator class might appear as follows:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  [Symbol.iterator]() {

    return {

      next() {

        if (this.index < this.data.length) {

          return { value: this.data[this.index++], done: false };

        } else {

          return { value: undefined, done: true };

        }

      }

    };

  }

}

```

This class demonstrates the essential elements of custom iterator implementation, including the [Symbol.iterator] method that returns an iterator object with a next() function. The next function manages the iterator's state and returns the appropriate value and done status for each iteration step.


## Using Iterators

Iterators facilitate clean iteration through JavaScript collections using 'for...of' loops and built-in functions like Array.prototype.map(). This functionality relies on the Symbol.iterator protocol, which returns an iterator object with a next() method that produces output in the format {value: any, done: boolean}.


### Custom Iterator Implementation

Developers can create custom iterators using generator functions or iterator classes. For example, a custom iterator class might be implemented as follows:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  [Symbol.iterator]() {

    return {

      next() {

        if (this.index < this.data.length) {

          return { value: this.data[this.index++], done: false };

        } else {

          return { value: undefined, done: true };

        }

      }

    };

  }

}

```

This implementation demonstrates the essential elements of custom iterator creation, including the [Symbol.iterator] method that returns an iterator object with a next() function.


### Built-in Iterator Support

JavaScript's built-in iterables, including strings, arrays, typed arrays, maps, and sets, all implement the Symbol.iterator method. For example:

```javascript

String.prototype[Symbol.iterator] = function*() {

  const string = this;

  for (let i = 0; i < string.length; i++) {

    yield string[i];

  }

};

console.log([...new String("hello")]); // Outputs: ["h", "e", "l", "l", "o"]

```

Custom iterables can be created by defining a method with the Symbol.iterator key. For example:

```javascript

const myIterable = {

  *[Symbol.iterator]() {

    yield 1;

    yield 2;

    yield 3;

  }

};

for (let value of myIterable) {

  console.log(value); // Outputs: 1, 2, 3

}

```


### Iterator Methods

The Iterator object contains several key methods:

- next(): Returns the next value in the iteration

- return(): Terminates the iteration and returns a specified value

- throw(): Throws an exception during iteration

These methods enable precise control over iteration processes, allowing developers to implement custom logic for sequence traversal.


### Iteration Protocols

The Symbol.iterator protocol defines the behavior of iterable objects, while the Iterator protocol governs the methods available on iterator objects. This dual-layer design provides both basic iteration functionality and hooks for custom behavior implementation.


## Iterator Protocol Implementation

The `[Symbol.iterator]` method is a static property representing the well-known symbol `Symbol.iterator`. This symbol enables objects to define their own iteration behavior. An object becomes iterable when it has an `[Symbol.iterator]` key, which must return an iterator object implementing the iterator protocol.

When an object needs to be iterated (like at the beginning of a `for...of` loop), its `[Symbol.iterator]()` method is called with no arguments. This method should return an iterator object that implements the iterator protocol, specifically containing a `next()` method returning an object with `value` and `done` properties.

Error handling shows that attempting to call `array[Symbol.iterator]()` directly without binding results in TypeError: Cannot convert undefined or null to object. Correctly binding the method using `.bind(arr)` resolves this issue. For example:

```javascript

const arr = [1, 2, 3];

const iterator = arr[Symbol.iterator].bind(arr);

console.log(iterator.next()); // { value: 1, done: false }

console.log(iterator.next()); // { value: 2, done: false }

console.log(iterator.next()); // { value: 3, done: false }

console.log(iterator.next()); // { value: undefined, done: true }

```


### Built-in Iterator Support

JavaScript's built-in iterables, including Array.prototype, String, Map, and Set, all implement the `[Symbol.iterator]` method. For example:

```javascript

String.prototype[Symbol.iterator] = function*() {

  const string = this;

  for (let i = 0; i < string.length; i++) {

    yield string[i];

  }

};

console.log([...new String("hello")]); // Outputs: ["h", "e", "l", "l", "o"]

```


### Custom Iterator Implementation

To create a custom iterable object, define a method with `[Symbol.iterator]` that returns an iterator object implementing the iterator protocol. For instance:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  [Symbol.iterator]() {

    return {

      next() {

        if (this.index < this.data.length) {

          return { value: this.data[this.index++], done: false };

        } else {

          return { value: undefined, done: true };

        }

      }

    };

  }

}

const customIterable = new CustomIterable([10, 20, 30]);

for (let value of customIterable) {

  console.log(value); // Outputs: 10, 20, 30

}

```


### Iterator Method Details

The iterator object's `next()` method receives a value that becomes the value of the corresponding `yield` expression. The iterator can implement `return(value)` and `throw(exception)` methods to indicate iteration completion and error conditions, respectively:

- `return` method returns an `IteratorResult` object with `done` set to `true` and `value` set to the passed value.

- `throw` method returns an `IteratorResult` object with `done` set to `true` and `exception` set to the error instance.

- The `next` method returns an `IteratorResult` object with `done` set to `false` and `value` set to the yielded value.


### Iterable Interface Requirements

For an object to be iterable, its `[Symbol.iterator]` method must return an iterator object implementing the iterator protocol. This method is typically implemented as a function returning the iterator object itself. When using an iterator, call `Symbol.iterator` on a collection to obtain an iterator object.


## Custom Iterators and Iterables

To create custom iterators, developers can use either generator functions or iterator classes. Generator functions employ function* syntax and the yield keyword to produce iterators with controlled state. For instance:

```javascript

function* numberGenerator(start, end) {

  for (let i = start; i < end; i++) {

    yield i;

  }

}

const gen = numberGenerator(1, 5);

console.log(gen.next()); // { value: 1, done: false }

console.log(gen.next()); // { value: 2, done: false }

console.log(gen.next()); // { value: 3, done: false }

console.log(gen.next()); // { value: 4, done: false }

console.log(gen.next()); // { value: undefined, done: true }

```

Generator functions offer a succinct way to implement iteration behavior while managing state. This example demonstrates creating a simple number generator that yields values from start to end.

For more complex iterator implementations, developers can define classes that explicitly manage their state through method calls. The implementation must return an object with a next() method that produces { value, done } pairs:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  *iterator() {

    while (this.index < this.data.length) {

      yield this.data[this.index++];

    }

  }

  [Symbol.iterator]() {

    return this.iterator();

  }

}

const customIterable = new CustomIterable([10, 20, 30]);

for (let value of customIterable) {

  console.log(value); // 10, 20, 30

}

```

This class demonstrates implementing both the iterator and iterable protocols. The iterator method generates sequential values, while the iterable method returns the iterator object.


### Custom Iterable Implementation

Developers can create custom iterables by combining iterator and iterable protocols. The example below illustrates defining an iterable object that wraps another collection:

```javascript

class CustomCollection {

  constructor(elements) {

    if (!Array.isArray(elements)) throw new TypeError('Elements must be an array');

    this.elements = elements;

  }

  *[Symbol.iterator]() {

    for (let element of this.elements) {

      yield element;

    }

  }

}

const collection = new CustomCollection(['a', 'b', 'c']);

for (let item of collection) {

  console.log(item); // 'a', 'b', 'c'

}

```

This class demonstrates proper iterator and iterable implementation, wrapping an array of elements and providing controlled access through the iterator protocol.


## Iterators in Practice

While the basic iterator functionality allows for simple value retrieval, advanced usage demonstrates its versatility in managing sequence traversal and stateful iteration. This section explores practical applications through code examples, highlighting both custom iterator creation and integration with built-in JavaScript functions.


### Custom Iterator with State Management

Developers can implement complex iteration logic using custom iterators. For instance, creating a sequence generator allows precise control over the iteration process:

```javascript

class CustomIterable {

  constructor(data) {

    this.data = data;

    this.index = -1; // Initialize index to -1 for first call

  }

  [Symbol.iterator]() {

    return (function*() {

      for (let element of this.data) {

        yield element;

      }

    }).call(this);

  }

}

const customIterable = new CustomIterable([10, 20, 30]);

for (let value of customIterable) {

  console.log(value); // 10, 20, 30

}

```

In this implementation, the iterator function uses `yield` to provide values while maintaining state through the index variable. This approach enables precise control over iteration flow.


### Integration with Built-in Functions

The power of iterators becomes evident when combined with built-in JavaScript functions. For example, the `Array.prototype.map()` method demonstrates this integration:

```javascript

const numbers = [1, 2, 3, 4];

const squares = numbers.map(function(number) {

  return number * number;

});

console.log(squares); // [1, 4, 9, 16]

```

Under the hood, `map()` creates an iterator for the source array, applying the callback function to each element. This demonstrates how iterators enable efficient and flexible collection manipulation.


### Multi-Iteration Support

Iterables can enable multiple iterations through a single collection. This behavior is particularly useful in scenarios requiring repeated traversal:

```javascript

class MultiIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  *iterableIterator() {

    while (this.index < this.data.length) {

      yield this.data[this.index++];

    }

  }

  [Symbol.iterator]() {

    return this.iterableIterator();

  }

}

const multiIterable = new MultiIterable([1, 2, 3]);

for (let value of multiIterable) {

  console.log(value); // 1, 2, 3

}

for (let value of multiIterable) {

  console.log(value); // 1, 2, 3

}

```

In this example, `MultiIterable` maintains its own state across multiple iterations, allowing for controlled access to the collection.


### Error Handling and Cleanup

Proper implementation includes comprehensive error handling to ensure stable iteration behavior. For instance, a custom iterable with error cleanup might look like this:

```javascript

class ErrorHandlingIterable {

  constructor(data) {

    this.data = data;

    this.index = 0;

  }

  *iterator() {

    try {

      while (this.index < this.data.length) {

        yield this.data[this.index++];

      }

    } catch (error) {

      console.error("Iteration error:", error);

    } finally {

      console.log("Iteration complete");

    }

  }

  [Symbol.iterator]() {

    return this.iterator();

  }

}

const errorIterable = new ErrorHandlingIterable([1, 2, "invalid", 4]);

for (let value of errorIterable) {

  console.log(value); // 1, 2, invalid

}

```

This implementation demonstrates robust error management, ensuring proper cleanup and status reporting during iteration.

