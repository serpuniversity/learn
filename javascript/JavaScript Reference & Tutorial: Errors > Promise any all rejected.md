---

title: JavaScript Error Handling with Promises: any, all, and Rejected Promises

date: 2025-05-26

---


# JavaScript Error Handling with Promises: any, all, and Rejected Promises

JavaScript promises have revolutionized asynchronous programming, providing a robust framework for managing asynchronous operations. However, their core functionality leaves room for improvement, particularly in how they handle errors and incomplete operations. This article explores advanced promise management techniques, focusing on Promise.all, Promise.allSettled, and Promise.any - powerful tools that address the limitations of traditional promise handling while maintaining backwards compatibility with existing implementations. Through practical examples and detailed implementation strategies, you'll learn how to master asynchronous workflow management in JavaScript, ensuring your applications handle partial success and mixed promise outcomes with precision and reliability.


## Promise.all and its limitations in handling rejected promises

The native Promise.all function only waits for all promises to resolve successfully, immediately rejecting with the first error encountered. This behavior makes it unsuitable for scenarios where partial success is acceptable, or where some failures should not prevent the continuation of other tasks.

To understand why this short-circuits on the first error, consider the implementation details. When passed an array of promises, `Promise.all` maintains an internal counter that tracks how many promises have settled successfully. The counter is incremented for each fulfilled promise and decremented for each rejection. The function returns a single promise that resolves when the counter reaches the length of the original array, indicating all promises have settled.

Once any individual promise rejects, the counter is decremented, and the internal rejection handler is triggered. At this point, `Promise.all` cannot requeue the rejected promise for later resolution, as the promise's state has already transitioned from pending to rejected. This architectural limitation forces the function to immediately reject, as resolving multiple promises with mixed status is not defined in the Promise specification.

Developers often address this limitation by combining `Promise.all` with individual `.catch` blocks. By mapping each promise to its own `.catch` handler, you can capture specific errors while maintaining the overall promise array structure. For example:

```javascript

Promise.all(promises.map(p => p.catch(e => e))).then(...).catch(...);

```

This pattern allows you to examine all individual errors after all promises have settled, rather than having the error short-circuit the entire operation. However, as noted in one of the documents, this approach does not fully replicate `Promise.allSettled` functionality, particularly in handling empty promise arrays or mixed arrays containing both promises and non-promise values.

For developers implementing similar functionality, the ES6 specification's limitations make it challenging to create a compatible replacement. A practical alternative is to use existing polyfills like the one provided by the Bluebird library, which efficiently handles both promise and non-promise values while returning an array of settlement objects. This approach ensures backwards compatibility with existing promise-handling code while providing essential functionality missing from the native implementation.


## Handling multiple promise rejections with Promise.allSettled

The native Promise.allSettled function represents a significant advancement in promise-handling capabilities, introduced in ES2020. Unlike Promise.all, which only waits for all promises to resolve successfully and immediately rejects with the first error, Promise.allSettled returns an array of objects, each representing the completion status of a promise (fulfilled or rejected).

This fundamental difference enables more flexible asynchronous workflow management. For example, consider the following code snippet:

```javascript

const promises = [fetch('index.html'), fetch('https://does-not-exist/')];

const results = await Promise.allSettled(promises);

const successfulPromises = results.filter(p => p.status === 'fulfilled');

```

In this example, `Promise.allSettled` allows the request for 'index.html' to complete while immediately acknowledging that the request for 'https://does-not-exist/' will fail. The resulting `results` array clearly indicates the fate of each request, enabling precise subsequent operations based on individual promise outcomes.

As noted in the MDN documentation, Promise.allSettled's return value is particularly valuable when:

- You need to know the result of each promise in an array, regardless of whether they succeed or fail.

- You want to process partially successful operations without premature rejection.

- You're working in environments that don't support native Promise.allSettled (Node.js versions below 12.9.0 or older browsers) and prefer not to polyfill custom behavior.

The function's implementation internally maintains an array of objects, each containing the status property ("fulfilled" or "rejected") and either a value or reason property based on the outcome of the promise. This structured return format aligns with modern JavaScript's preference for explicit error handling and provides a clear path for subsequent processing of mixed promise outcomes.


## Alternate implementation approaches: Custom Promise.allSettled

Developers implementing custom promise handling solutions face significant challenges in replicating native Promise.allSettled functionality. While several approaches show promise, each has distinct strengths and limitations.

The first custom implementation demonstrates robust handling of both promise and non-promise values:

```javascript

const settle = (promise) => (promise instanceof Promise)

  ? promise.then(val => ({ value: val, status: "fulfilled" }), err => ({ reason: err, status: "rejected" }))

  : { value: promise, status: 'fulfilled' };

const allSettled = async (parr) => Promise.all(parr.map(settle));

```

This solution returns an array of objects, matching the native implementation's structure. However, it requires careful attention to promise instance checks to maintain correct behavior.

An alternative approach uses a single error accumulator and async function to manage multiple promises:

```javascript

const settledPromiseAll = function(promisesArray) {

  var savedError;

  const saveFirstError = function(error) {

    if (!savedError) savedError = error;

  };

  const handleErrors = function(value) {

    return Promise.resolve(value).catch(saveFirstError);

  };

  const allSettled = Promise.all(promisesArray.map(handleErrors));

  return allSettled.then(function(resolvedPromises) {

    if (savedError) throw savedError;

    return resolvedPromises;

  });

};

```

This implementation effectively handles mixed arrays and returns the first rejected promise if any are encountered, demonstrating backward compatibility with `Promise.all`.

Library-based solutions offer additional flexibility, as shown by the example using Promise-ax:

```javascript

const { createPromise } = require('promise-ax');

const promiseAx = createPromise();

const promise1 = Promise.resolve(4);

const promise2 = new Promise((resolve, reject) => setTimeout(reject, 100, new Error("error")));

const promise3 = Promise.reject("error");

const promise4 = promiseAx.resolve(8);

const promise5 = promiseAx.reject("errorAx");

```

These approaches enable developers to extend core promise capabilities while maintaining familiar behavior. However, careful consideration of implementation details is essential to ensure robust, maintainable asynchronous code.


## Promise.any: Handling rejection with the first successful promise

The Promise.any method represents an important advancement in JavaScript's promise-handling capabilities, offering a distinct approach to managing multiple promise resolutions. Unlike Promise.all, which requires all promises to resolve successfully, Promise.any returns the first fulfilled promise while rejecting with an AggregateError if all promises are rejected.

This behavior is particularly useful in scenarios where partial success is valuable, and individual failures should not prevent the continuation of other tasks. As noted in the MDN documentation, Promise.any allows all promises to run concurrently, but immediately stops upon the first successful resolution.

The implementation of this functionality differs from both Promise.all and Promise.race. While Promise.all waits for all promises to resolve successfully and rejects immediately upon encountering a single rejection, Promise.race returns the first settled promise (either resolved or rejected). In contrast, Promise.any focuses specifically on the first successful resolution, making it particularly effective for scenarios where a single successful outcome is sufficient.

The AggregateError rejection strategy provides valuable insights into the fate of all promises. When all promises are rejected, the returned AggregateError contains an array of all rejected reasons, allowing for precise error analysis. This structured error handling complements the promise's primary functionality, providing developers with both success and failure information.

Developers implementing custom solutions face several key challenges. The primary implementation approach involves maintaining an error accumulator and using an async function to manage multiple promises. This pattern effectively handles both successful resolutions and rejected promises, returning the first fulfilled value while collecting all rejection reasons.

For optimal implementation, libraries like Promise-ax offer valuable polyfill solutions. These library-based approaches enable developers to extend core promise capabilities while maintaining familiar behavior. However, as noted in the implementation documentation, careful attention to detail is essential to ensure robust, maintainable asynchronous code. This includes proper handling of promise instance checks and maintaining the order of promise results as they resolve.


## Error handling best practices

The Promise.reject() static method returns a `Promise` object that is rejected with a given reason. This method is widely available across many devices and browser versions, with compatibility since July 2015. Key features include:

- The `Promise` constructor can wrap a given value in a `Promise` object, handling errors using an `instanceof Error` for better debugging.

- The `Promise.prototype` object contains several instance properties, including `constructor`, `Symbol.toStringTag`, and instance methods like `catch`, `finally`, and `then`.

Developers can use `Promise.reject()` for selective error handling and debugging. For example:

```javascript

Promise.reject(new Error("fail")).then(resolved, rejected);

// Expected output: Error: fail

```

In custom promise implementations, proper error handling requires careful attention to promise instance checks. For instance, developers can create a custom promise constructor with error handling capabilities:

```javascript

class MyPromise {

  constructor(executor) {

    executor((value) => this.resolve(value), (reason) => this.reject(reason));

  }

  resolve(value) {

    // Implementation

  }

  reject(reason) {

    // Implementation

  }

}

```

When using `.then()` for promise chaining, developers should append rejection handlers using `.catch()`. This ensures that both fulfillment and rejection cases can be managed:

```javascript

const myFirstPromise = new Promise((resolve, reject) => {

  setTimeout(() => {

    resolve("Success!");

  }, 250);

});

myFirstPromise

  .then(successMessage => {

    console.log(`Yay! ${successMessage}`);

  })

  .catch(error => {

    console.error("Error:", error);

  })

  .finally(() => {

    console.log("Promise complete");

  });

```

For extended promise handling, developers can implement custom promise classes with error management capabilities. The following example demonstrates a basic custom promise constructor:

```javascript

class CustomPromise {

  constructor(executor) {

    executor((value) => this.fulfill(value), (reason) => this.reject(reason));

  }

  fulfill(value) {

    // Implementation

  }

  reject(reason) {

    // Implementation

  }

}

```

Best practices for error handling include:

1. Using `.catch()` to append rejection handlers and handle errors

2. Implementing custom promise classes with proper error management

3. Utilizing `Promise.reject()` for selective error handling and debugging

4. Ensuring all promise instances are correctly resolved or rejected

5. Using `.finally()` for cleanup operations regardless of promise outcome

