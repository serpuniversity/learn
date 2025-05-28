---

title: JavaScript Async/Await and Generator Basics

date: 2025-05-26

---


# JavaScript Async/Await and Generator Basics

JavaScript's async/await and generator features transform how developers handle asynchronous operations, with each offering distinct benefits and use cases. Understanding their syntax requirements and proper implementation is crucial for writing efficient, maintainable code that reliably manages asynchronous tasks. This article explores the fundamentals of these powerful JavaScript constructs, comparing their key differences and providing best practices for implementation in modern applications.


## 'await' and 'yield' syntax in JavaScript

The `await` and `yield` keywords in JavaScript have specific syntax requirements in function definitions. While `yield` allows generator functions to return multiple values at different time intervals and manage their internal state, `await` enables JavaScript to wait for promises to settle.


### Function Declarations and Await

To use `await` in JavaScript, the containing function must be declared with the `async` keyword. This ensures that the function always returns a promise, making `await` operations valid within its scope. For example:

```javascript

async function fetchData(url) {

  const response = await fetch(url);

  return await response.json();

}

```


### Error Handling and Syntax

Using `await` within a non-async function context will result in a SyntaxError. The same applies to `yield` in certain contexts, such as parameter default expressions:

```javascript

function defaultParamsExample(a = await new Promise((resolve) => resolve(10))) {

  console.log(a);

}

```

This code will produce a SyntaxError because `await` is not allowed in parameter default expressions. Valid alternatives include using nullish coalescing assignment (`??=`) for default values or converting the function to an async generator.


### Generator vs Async/Await: Basic Differences

While both generators and async/await handle asynchronous operations, their implementations and syntax differ. Generator functions create iterators that can pause and resume execution using the `yield` keyword. In contrast, `async` functions return promises and use the `await` keyword to wait for asynchronous operations.


### Best Practices

The `async` keyword transforms a function into a coroutine that always returns a promise. This makes it essential for writing asynchronous code that's both readable and maintainable. The `await` keyword should only be used within async functions, as demonstrated in this example:

```javascript

async function processItems(items) {

  for await (const item of items) {

    await processItem(item);

  }

}

```

This structure ensures that each await operation waits for its promise to settle before proceeding to the next iteration.


## Function declarations and async/await

The use of `await` requires the containing function to be declared with the `async` keyword. This ensures that the function always returns a promise, making `await` operations valid within its scope. For example:

```javascript

async function fetchData(url) {

  const response = await fetch(url);

  return response.json();

}

```

The async keyword transforms a function into a coroutine that always returns a promise. This makes it essential for writing asynchronous code that's both readable and maintainable. To demonstrate the requirement for async functions, consider the following comparison:


### Valid Usage

```javascript

async function processData() {

  const data = await fetchData('/api/v1/data');

  console.log(data);

}

```


### Invalid Usage Results in SyntaxError

```javascript

function processData() {

  const data = await fetchData('/api/v1/data'); // SyntaxError: await is only valid in async function

  console.log(data);

}

```

The async keyword has two primary effects: it makes the function always return a promise, and it enables the use of await within that function. Understanding this relationship between async and await is crucial for effectively implementing asynchronous operations in JavaScript.


## Error Handling with async/await

`await` requires the executing context to be `async` in nature. To use `await`, the function declaration must be marked as `async`. The current implementation of async/await only supports the `await` keyword inside `async` functions.

The key error scenarios include using `await` in parameter default expressions and attempting to await the promise of a file's content directly. For example:

```javascript

async function start(a, b = await fetchInitialValue()) {

  // This will throw a SyntaxError

}

```

In this case, valid alternatives include using nullish coalescing assignment (`??=`) for default values:

```javascript

async function start(a, b = await fetchInitialValue() ?? 'default') {

  // This is valid

}

```

Or converting the function to an async generator:

```javascript

async function* start() {

  const b = await fetchInitialValue();

  // Generator logic here

}

```

For error handling, consider using `try...catch` blocks:

```javascript

async function fetchData(url) {

  try {

    const response = await fetch(url);

    return await response.json();

  } catch (error) {

    console.error("Failed to fetch data:", error);

  }

}

```

The `async` keyword makes the function always return a promise, and allows `await` to be used within its scope. This structure ensures that dependent code waits for asynchronous operations to complete before proceeding.

When using `async` with `.forEach()`, be aware that the code after `.forEach()` will run before the code after the first `await` inside the loop. To maintain proper asynchronous flow, consider using `Promise.all` to wait for all tasks simultaneously:

```javascript

repositories.forEach(async repo => {

  const commits = await getCommits(repo);

  displayCommit(commits);

});

// Equivalent using Promise.all

await Promise.all(repositories.map(async repo => {

  const commits = await getCommits(repo);

  displayCommit(commits);

}));

```

In later Node.js versions (>=14), top-level `await` is allowed with either `{ "type": "module" }` specified in `package.json` or with file extension `.mjs`. This allows for more modular and readable asynchronous code at the top level of modules.


## Generator vs async/await: Basic Differences

JavaScript's async/await functionality builds on top of generator machinery, even though async/await is implemented natively in the V8 engine with release 5.5. This means that under the hood, async/await uses generator techniques to manage asynchronous operations.

The key difference between the two lies in their fundamental design and use case. While generators create iterators that can pause and resume execution, async/await provides a more synchronous-like syntax for handling promise chains. This makes async/await particularly well-suited for writing readable and maintainable asynchronous code, especially when working with multiple promise-based operations.


### Basic Operations

Both async/await and generators handle asynchronous operations, but they approach this task differently. A generator function uses the yield keyword to pause its execution and return a result to its caller. Later, the caller can pass a new value back to the generator using generator.next(), which becomes the result of the yield expression. If an error occurs, the caller can throw it, which appears to be thrown by the yield expression.

The await keyword in async/await functions serves a similar purpose, but it operates within specific constraints. When used in an expression, async function execution pauses until the promise is settled (fulfilled or rejected). If the promise fulfills, await returns the resolved value. If the promise rejects, await throws the rejection reason as an error. This means that while both keywords can be used to wait for asynchronous operations, they differ in their handling of promise resolution and error propagation.


### State Management

Generator functions maintain their internal state between calls using the IteratorResult object, which contains value and done properties. Each call to the generator's next() method returns this object, allowing the generator to resume where it left off. In contrast, async functions always return a promise that resolves to whatever value they return or throws an error. This fundamental difference in return behavior makes async functions particularly useful for managing the overall flow of asynchronous operations.


### Practical Considerations

In their native implementations, async/await functions in modern JavaScript engines perform better than traditional generators. This improvement is most noticeable when dealing with multiple promise-based operations, as async/await allows developers to write more concise and readable code. However, for scenarios requiring complex state management or sequential asynchronous operations with immediate resolution, generators remain a powerful tool in JavaScript's asynchronous toolkit.


## Best Practices for async/await

When working with async/await in JavaScript, it's crucial to understand the specific requirements and limitations of the syntax. This includes recognizing that `await` can only be used inside `async` functions and that non-async functions will result in a SyntaxError, as demonstrated in this example:

```javascript

async function start() {

  try {

    await fetchInitialValue();

  } catch (error) {

    console.error("Error during fetch:", error);

  }

}

```

The `async` keyword transforms a function into a coroutine that always returns a promise, making it essential for managing asynchronous operations effectively.

Returning promises directly from async functions is generally considered less optimal than using `return await`. This approach, while valid, can be less efficient due to the overhead of intermediate promise handling. As noted in MDN documentation:

```javascript

async function fetchData(url) {

  const response = await fetch(url);

  return response.json(); // Direct return vs return await response.json()

}

```

The preferential use of `return await` is particularly important when dealing with multiple asynchronous operations. Consider the following comparison:

```javascript

async function processMultiple() {

  const firstResult = await firstAsyncOperation();

  const secondResult = await secondAsyncOperation();

  return combinedResult(firstResult, secondResult);

}

```

Using separate `await` calls as shown above, rather than combining operations into a single promise chain, allows for more efficient error handling and easier management of independent asynchronous tasks.


### Promises and Async Functions

When working with promises, it's important to understand how async/await handles their resolution and rejection. According to the specification, `await` behaves as follows:

1. When the awaited promise fulfills, `await` returns the resolved value.

2. When the awaited promise rejects, an exception is thrown with the rejection reason.

This behavior allows for simplified error handling through the use of try/catch blocks:

```javascript

async function processWithCatch() {

  try {

    const result = await complexOperation();

    // Handle successful operation

  } catch (error) {

    // Handle operation failure

  }

}

```

The combination of `async` functions and top-level `await` provides powerful capabilities for modern JavaScript development, particularly when used with module systems or in environments supporting ECMAScript modules. As noted in the official documentation:

```javascript

await fetch('/data.json')

  .then(response => response.json())

  .catch(error => console.error('Fetch error:', error));

```

In later Node.js versions (>=14), the use of top-level `await` has expanded to include `.mjs` file extensions or the `"type": "module"` configuration in package.json, enabling more modular and maintainable asynchronous code structures.

