---

title: JavaScript Async/Await: for-await...of Statements

date: 2025-05-27

---


# JavaScript Async/Await: for-await...of Statements

JavaScript's async/await syntax has transformed Promise-based asynchronous programming, offering a more intuitive way to handle non-blocking operations while maintaining code readability. By allowing developers to write asynchronous code that looks synchronous, these features have significantly improved the maintainability and performance of modern JavaScript applications. This article explores how async/await works with for-await...of statements, explaining how these constructs can be used to efficiently process asynchronous iterables while maintaining consistent iteration patterns across synchronous and asynchronous data sources. We'll examine the structure and behavior of for-await...of, its handling of promises and values, and best practices for using these constructs in real-world applications. Additionally, we'll discuss performance considerations and compatibility across different platforms, helping developers make informed decisions about when to use these powerful features.


## Async/Await Fundamentals

JavaScript's async/await syntax reimagines promise-based asynchronous programming to appear more synchronous, significantly enhancing code readability and maintainability. When applied to functions, the async keyword transforms them into promise-returning functions, making it possible to use the await keyword within their bodies.

The await expression within an async function behaves as if the function is synchronous, allowing the execution to pause at that point and wait for the promise to resolve. This syntax simplifies handling asynchronous operations, as demonstrated in real-world uses like JSON data fetching and GitHub user lookups. Asynchronous operations that would otherwise require complex promise chaining become straightforwardly expressed with await.

JavaScript's async functions return promises by default, automatically wrapping non-promise return values in resolved promises. This automatic behavior reduces boilerplate code and makes it unnecessary to explicitly return promises in many cases.

The use of await requires a function to be declared with async, making it syntactically clear which parts of the code are dealing with asynchronous operations. While await can technically be used with any expression that returns a promise, it's specifically designed for situations where the function's result is dependent on the resolution of previous asynchronous operations, such as in the original GitHub user lookup example.

Developers should prefer await-based asynchronous operations over traditional .then/catch chaining when possible, as it results in more linear, readable code. However, it's important to note that await operations still run in the event loop, meaning they don't consume CPU resources while waiting for promises to resolve. This allows the JavaScript engine to perform other tasks during the waiting period.


## for await...of Structure

The for await...of statement extends the capabilities of standard for-of loops to work with asynchronous iterables, making it possible to consume async iterables and standard iterables in a consistent manner. This hybrid functionality allows developers to work with asynchronous data streams while maintaining familiar iteration patterns.


### Structure and Behavior

The statement operates by internally awaiting the emitted values from sync iterables or generators, wrapping the next(), return(), and throw() methods into resolved or rejected promises. It follows a sequential processing model, where each iteration awaits the previous promise to resolve before proceeding. This behavior is particularly useful when working with data streams or asynchronous operations that yield values one at a time.


### Handling Promises and Values

When iterating over an async iterable, the for await...of statement waits for each value to resolve as a promise before assigning it to the loop control variable. If the iterable yields rejected promises, the statement throws an error, similar to a throw statement. For sync iterables or generators, it internally awaits emitted values before assignment, ensuring consistent behavior across different iterable types.


### Iteration Control

The loop supports standard control flow statements like break and continue, providing flexibility in handling varying iteration requirements. The structure maintains compatibility with existing iterator protocols, wrapping sync iterators into async iterators and handling the asynchronous wrapping of next() methods. This design choice ensures that the statement works seamlessly with both standard and async iterables while providing the necessary asynchronous behavior.


### Browser and Platform Support

The for await...of statement is supported across major platforms, with full compatibility in modern browsers and Node.js versions. As of the latest specifications, it's implemented in Chrome 63, Firefox 57, Opera 50, Safari 11, and Node.js 10.0.0, providing broad support for developers looking to implement asynchronous iteration in their applications.


## Handling Promises and Rejections

When using for await...of, the loop waits for each promise to resolve before moving to the next iteration, ensuring that dependencies between iterations are maintained. This sequential processing model prevents unexpected results that could occur if iterations were executed concurrently.

The behavior of for await...of with promises mirrors that of the await keyword in async functions: upon encountering a promise, it waits for it to resolve before proceeding. If a rejected promise is encountered, the loop throws an error, similar to a throw statement, and terminates the iteration process.

For sync iterables or generators, for await...of internally awaits emitted values before assignment. This ensures compatibility with existing iterator protocols while providing necessary asynchronous behavior. The loop maintains this pattern even when dealing with objects that implement the async iterator protocol, though some developers find this functionality less intuitive than expected.

When handling rejected promises, for await...of immediately throws the error, preventing further iteration. This behavior differs from for...of, which continues execution after encountering a rejected promise. To ensure that finally blocks are always called when working with sync generators that yield rejected promises, developers should use for await...of. If async generators yield rejected promises, for await...of properly calls the finally block, ensuring that allocated resources are properly freed.


## Performance Considerations

Each iteration of an async function containing a for await...of statement waits for the previous asynchronous operation to complete before proceeding, ensuring that operations remain in sequence. This behavior maintains the intended execution order and prevents unexpected results that could occur with concurrent execution.

This sequential processing model is particularly important when dependencies exist between iterations. For instance, processing new records sequentially requires maintaining order to ensure that results from one iteration can affect subsequent operations. The engine defers execution of each iteration to the next event loop tick, allowing the JavaScript engine to handle other tasks while waiting for promises to resolve.

When combined with functions like fs.readFile, each asynchronous operation waits for the previous one to complete before initiating the next call. This deferred execution prevents premature processing of subsequent operations, ensuring that asynchronous dependencies remain respected throughout the loop.

While for await...of provides convenient syntax for iterating over async iterables, the underlying mechanism of sequential promise execution maintains compatibility with existing iterator protocols. This approach ensures that both async and sync iterables can be processed using the same loop construct, providing flexibility in handling different data sources while preserving the desired execution order.


## Best Practices

For scenarios where promises are generated sequentially and dependencies exist between iterations, use the for await...of structure as shown in the following example:

```javascript

const items = [1000, 2000, 3000, 4000];

const promises = items.map(e => somethingAsync(e));

(async() => {

  console.time("first way");

  const results = await Promise.all(promises);

  for (const res of results) {

    console.log(res);

  }

  console.timeEnd("first way");

  console.time("second way");

  for await (const res of promises) {

    console.log(res);

  }

  console.timeEnd("second way");

})();

```

This approach ensures that all asynchronous operations complete before proceeding, maintaining the intended execution order. The for await...of statement allows for both sequential and parallel execution patterns depending on the nature of the data source.

However, when working with independent promises in an array, use Promise.all for improved performance. The following example demonstrates this best practice:

```javascript

const promises = Array.from({length: 1000}, (_, i) => new Promise(resolve => setTimeout(() => resolve(`Promise ${i}`), 100)));

async function processPromises() {

  const results = await Promise.all(promises);

  console.log(results);

}

processPromises();

```

In this case, firing off all promises simultaneously with Promise.all allows the JavaScript engine to handle multiple asynchronous operations in parallel, potentially reducing overall execution time. This approach is particularly effective when dealing with independent tasks that can be executed concurrently.

