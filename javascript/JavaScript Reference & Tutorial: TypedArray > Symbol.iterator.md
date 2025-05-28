---

title: JavaScript TypedArray Iterator

date: 2025-05-27

---


# JavaScript TypedArray Iterator

JavaScript's TypedArray.@@iterator property provides default iterable behavior for typed array objects, allowing them to be consumed by iteration syntaxes like for...of loops and spread syntax. As an intrinsic language feature dating back to 2016, this implementation returns an array iterator function that yields typed array values without requiring additional parameters. The property operates according to the broader JavaScript iterable protocol, offering developers a standardized way to process array-like data structures efficiently.


## Introduction to TypedArray Iterator

TypedArray.@@iterator is an intrinsic property in JavaScript that provides default iteration behavior for typed arrays (ArrayBuffer views). As an inbuilt feature, it returns the initial value of the typed array's elements without requiring additional parameters.

The property operates according to the iterable protocol, specifically through the Symbol.iterator method. For typed arrays, this implementation returns an array iterator function, with the values() function serving as the default iterator behavior. This aligns with JavaScript's broader design pattern for creating iterable objects, though it's important to note that not all object types implement this functionality.

Browser compatibility for the TypedArray.@@iterator method dates back to September 2016, demonstrating its widespread adoption across modern JavaScript environments. Developers can access this functionality using the symbol notation: A[Symbol.iterator](). The returned iterator object will yield the value of each index in the typed array when its next() method is called, following the standard iterable protocol behavior.


## TypedArray.@@iterator Implementation

The typed array's @@iterator implementation returns an iterator object that yields the value of each index in the array. This aligns with JavaScript's broader design pattern for creating iterable objects, as both TypedArray and Array instances implement the iterable protocol through their @@iterator methods.

The return value of the @@iterator implementation is an iterator object that follows the standard iterable protocol behavior. When the iterator's next() method is called, it returns an object containing both the current value and a done flag. The value is the current element of the array, while the done flag indicates whether the iterator has reached the end of the collection.

The implementation requires no parameters, as it operates on the current state of the typed array. Like other iterable objects in JavaScript, the typed array's @@iterator method allows consumption by syntaxes expecting iterables, such as spread syntax and for...of loops.

The method has been widely available across browsers since September 2016, demonstrating its widespread adoption within the JavaScript ecosystem. This implementation leverages the underlying ArrayBuffer to provide efficient access to the array elements, as indexed properties on typed arrays consult the ArrayBuffer directly and never look at object properties.

The @@iterator method works in conjunction with TypedArray's standard array index syntax (bracket notation) to reference elements. However, it's important for developers to note that while standard array operations are efficient, creating large typed arrays through regular array operations can be less performant due to the need to copy data between the JavaScript heap and the ArrayBuffer.


## Iterating with Symbol.iterator

The Symbol.iterator property represents the well-known symbol Symbol.iterator and serves as the foundation for creating custom iterators in JavaScript. This built-in symbol is used to determine the method that returns the iterator for an object, allowing objects to be iterated over using language features like for...of loops and spread syntax.


### Implementation Details

To implement a custom iterator, the Symbol.iterator method must return an object with a next() method. The next() method should return an object containing both a value and a done property. The value property represents the current value of the iterator, while the done property indicates whether the iterator has reached the end of the collection.

For example, the Symbol.iterator method can be defined as follows:

```javascript

class MyIterable {

  *[Symbol.iterator]() {

    yield 1;

    yield 2;

    yield 3;

  }

}

const myIterable = new MyIterable();

for (const value of myIterable) {

  console.log(value);

}

```


### Non-well-formed Iterables

If an iterable's Symbol.iterator method does not return an iterator object, the iterable is considered non-well-formed. Using non-well-formed iterables may result in runtime exceptions or buggy behavior. An example of a non-well-formed iterable is:

```javascript

const nonWellFormedIterable = {};

nonWellFormedIterable[Symbol.iterator] = () => 1;

([...nonWellFormedIterable]); // TypeError: [Symbol.iterator]() returned a non-object value

```


### Built-in Support

TypedArray instances implement the iterable protocol through their Symbol.iterator method, returning an array iterator function. This allows typed arrays to be consumed by syntaxes expecting iterables, such as the spread syntax and for...of loops. The specification for this method is defined in ECMAScript 2026 Language Specification section # sec-%typedarray%.prototype-%symbol.iterator%.

The method works as follows:

```javascript

const A = new Uint8Array([5, 10, 15, 20, 25]);

const iterator = A[Symbol.iterator]();

console.log(iterator.next().value); // 5

console.log(iterator.next().value); // 10

// ...

```

The Symbol.iterator property has the following attributes:

- Writable: no

- Enumerable: no

- Configurable: no


### Browser Compatibility

The Symbol.iterator method has been available across browsers since September 2016, demonstrating its widespread adoption within the JavaScript ecosystem. This method is part of the iterable protocol and is used to make objects iterable, allowing iteration syntaxes like for...of to automatically call this method to obtain the iterator to loop over.


## Symbol.iterator in JavaScript Iteration

The Symbol.iterator property represents the well-known symbol Symbol.iterator and serves as the foundation for creating custom iterators in JavaScript. It allows objects to be iterated over using language features like spread syntax (`...`) and the `for...of` statement (MDN Web Docs, Making objects iterable in JavaScript, MDN Web Docs).

For example, an object representing a car with `.make`, `.model`, and `.year` properties can be made iterable by implementing the `[Symbol.iterator]()` method:

```javascript

const car = {

  make: "Toyota",

  model: "Camry",

  year: 2023,

  [Symbol.iterator]() {

    return Object.entries(this)[Symbol.iterator](); // Return iterator from Object.entries

  }

};

```

Using this implementation, the car object can be iterated over using a `for...of` statement:

```javascript

for (const [key, value] of car) {

  console.log(`${key}: ${value}`);

}

```

The Symbol.iterator property has the following attributes:

- Writable: no

- Enumerable: no

- Configurable: no

As of June 2023, browser support for Symbol.iterator has reached 100% according to caniuse.com, making it a widely adopted feature of the JavaScript language (caniuse.com, Symbol.iterator).


### Additional Implementation Details

When an object needs to be iterated (such as at the beginning of a `for...of` loop), its `[Symbol.iterator]()` method is called with no arguments. The returned iterator is used to obtain the values to be iterated (MDN Web Docs, Symbol.iterator).

For objects that are not built-in iterables, the `Object.entries()` static method can be used to iterate over their key-value pairs, though this method itself returns a two-dimensional array and needs to be wrapped in an iterator implementation (MDN Web Docs, Symbol.iterator). This can be achieved using the spread syntax and a generator function:

```javascript

const obj = { a: 1, b: 2, c: 3 };

const iterator = Object.entries(obj)[Symbol.iterator]();

while (true) {

  const { done, value } = iterator.next();

  if (done) break;

  console.log(value); // Logs ['a', 1], ['b', 2], ['c', 3]

}

```

This approach ensures that the object remains iterable while allowing iteration over its properties (MDN Web Docs, Symbol.iterator).

The iterable protocol allows some built-in types to have default iteration behavior, while others (such as `Object`) do not. Built-in iterables with default iteration include Array, TypedArray, String, Map, Set, arguments, and Intl.Segmenter.Segments (MDN Web Docs, Symbol.iterator). Methods like Array.from can convert iterable or array-like values into real arrays, providing flexibility in working with different data structures (MDN Web Docs, Symbol.iterator).

