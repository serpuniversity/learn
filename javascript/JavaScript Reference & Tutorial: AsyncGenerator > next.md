---

title: JavaScript AsyncGenerator.next() Method

date: 2025-05-26

---


# JavaScript AsyncGenerator.next() Method

JavaScript's AsyncGenerator API extends the capabilities of generators by handling asynchronous operations seamlessly. This article focuses on the `next()` method, which returns the next value in the sequence produced by an async generator. We'll explore how to use `next()` to control the generator's flow, handle asynchronous operations, and understand its behavior when working with promises.


## AsyncGenerator.next() Method Overview

The `next()` method of AsyncGenerator instances returns the next value in the sequence. It can take an optional value parameter, which is used to modify the generator's internal state. This method returns a Promise that resolves to an object with two properties: value and done. The done property indicates whether the generator has completed, while value contains the yielded or returned value.


### Example Usage

The following example demonstrates the practical implementation of the next() method with both regular values and sent values to the generator:

```javascript

async function* asyncGenerator() {

  yield 3;

  yield 5;

  yield 3;

}

const generator = asyncGenerator();

generator.next().then(result => {

  console.log(result.value);

  console.log(result.done);

});

generator.next().then(result => {

  console.log(result.value);

  console.log(result.done);

});

generator.next().then(result => {

  console.log(result.value);

  console.log(result.done);

});

```

This outputs:

```

3 false

5 false

3 false

```

In this example, the generator produces three values, with the done property remaining false until the generator has produced all its values.


## Method Syntax and Parameters

The next() method has the simple syntax AsyncGenerator.prototype.next([value]), where value is optional and used to modify the internal state of the generator. This method returns a Promise that resolves to an object with two properties: value and done. The done property indicates whether the generator has completed, while value contains the yielded or returned value.


### Formal Specification

According to the ECMAScript 2026 Language Specification, section sec-asyncgenerator-prototype-next, the method accepts the following:

- **value** (optional): An optional value used to modify the internal state of the generator.

The method returns a Promise that resolves to an Object with the following properties:

- **done**: A boolean indicating whether the generator has completed.

- **value**: The yielded or returned value from the generator.


### Practical Implementation

The method works as demonstrated in the following implementation:

```javascript

async function* createAsyncGenerator() {

  yield delayedValue(500, 1);

  yield delayedValue(500, 2);

  yield delayedValue(500, 3);

}

const asyncGen = createAsyncGenerator();

asyncGen.next().then(res => console.log(res)); // { value: 1, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 2, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 3, done: false }

asyncGen.next().then(res => console.log(res)); // { value: undefined, done: true }

```

This behavior differs from regular generators, as noted in the documentation: "Async generator methods always yield Promise objects." This is important for handling asynchronous operations within the generator.


## Return Value

The next() method returns an object representing the IteratorResult interface, with two properties: value and done. When called with a value, it behaves as if a return value; statement is inserted at the current suspended position. The method returns a Promise that resolves with an object containing:

- done: A boolean indicating whether the generator function's control flow has reached the end (true) or if more values can be produced (false), with the condition that this only applies if the return is captured in a try...finally block and there are more yield expressions in the finally block.

- value: The value passed to return() or, if the yield expression is wrapped in a try...finally block, the value yielded/returned from the finally block.

If called without a value argument and the generator has completed, the promise resolves as if the next() method had been called. The value returned is undefined. The method can still be called after the generator is in a "completed" state, but the generator will remain in this state.

For regular generators, the done property indicates whether the generator is past the end of its control flow, while the value contains the yielded or returned value. This difference between regular and async generators is important for handling asynchronous operations within the generator.


## Example Usage

The `next()` method of AsyncGenerator instances returns the next value in the sequence, as demonstrated in the following example:

```javascript

async function* createAsyncGenerator() {

  yield delayedValue(500, 1);

  yield delayedValue(500, 2);

  yield delayedValue(500, 3);

}

const asyncGen = createAsyncGenerator();

asyncGen.next().then(res => console.log(res)); // { value: 1, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 2, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 3, done: false }

asyncGen.next().then(res => console.log(res)); // { value: undefined, done: true }

```

In this example, the generator produces three values, after which the `done` property becomes true.

A crucial aspect of the `next()` method is its handling of asynchronous operations, as shown in this modified version of the example:

```javascript

async function* createAsyncGenerator() {

  yield new Promise(resolve => setTimeout(resolve, 1000, 1));

  yield new Promise(resolve => setTimeout(resolve, 1000, 2));

  yield new Promise(resolve => setTimeout(resolve, 1000, 3));

}

const asyncGen = createAsyncGenerator();

asyncGen.next().then(res => console.log(res)); // { value: 1, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 2, done: false }

asyncGen.next().then(res => console.log(res)); // { value: 3, done: false }

asyncGen.next().then(res => console.log(res)); // { value: undefined, done: true }

```

Here, the generator waits for each promise to resolve before producing the next value, demonstrating how async generators handle asynchronous operations.

The method also allows sending values to the generator using the value parameter, as shown in this example:

```javascript

async function* createAsyncGenerator() {

  while (true) {

    await sleep(500);

    const value = yield;

    console.log(value);

  }

}

async function main() {

  const asyncGen = createAsyncGenerator();

  console.log(await asyncGen.next()); // { value: undefined, done: false }

  console.log(await asyncGen.next(2)); // { value: undefined, done: false }

}

```

In this case, the generator waits for a value to be sent before continuing execution, printing the received value to the console.

To prevent an AsyncGenerator from yielding after its completion, the `return()` method can be used, as demonstrated in this example:

```javascript

async function* createAsyncGenerator() {

  for (let i = 0; i < 4; i++) {

    yield i;

  }

}

const asyncGen = createAsyncGenerator();

asyncGen.next().then(res => console.log(res)); // { value: 0, done: false }

console.log(await asyncGen.return()); // { value: undefined, done: true }

```

After calling `return()`, subsequent calls to `next()` will immediately resolve to `{ value: undefined, done: true }`, indicating that the generator has completed.

