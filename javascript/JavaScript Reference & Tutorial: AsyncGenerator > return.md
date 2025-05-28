---

title: JavaScript AsyncGenerator: Understanding the return() Method

date: 2025-05-26

---


# JavaScript AsyncGenerator: Understanding the return() Method

AsyncGenerators in JavaScript offer powerful mechanisms for managing asynchronous operations through iteration and suspension. While they share many similarities with regular generators, AsyncGenerators include advanced features specifically designed for asynchronous programming. One such feature is the return() method, which enables developers to terminate generator execution early and perform necessary cleanup. This method operates similarly to generator return statements but with promise-based resolution, making it essential for controlling asynchronous operations before their natural completion. The return() method's behavior, including its effect on promise resolution and generator state, is crucial for developers implementing robust asynchronous workflows.


## return() Method Basics

The return() method in AsyncGenerators allows for early termination and cleanup, operating similarly to regular generators but with promise-based resolution. It functions by inserting a return statement at the current suspended position, akin to how the return statement works within generator functions.

When invoked, return() completes the current iteration before considering the return call itself. If provided with a value, it returns a promise resolving with an object containing {done: true, value: returnValue}. Without a value argument, the promise resolves as if the next() method has been called, placing the generator in a "completed" state.

This method can be called at any point during iteration, including after the generator has completed. In the latter case, it returns an undefined value by default. However, additional values can still be returned after the generator has finished execution.

The return() method enables proper cleanup through combination with try...finally blocks, allowing controlled termination of asynchronous operations before their natural completion. This functionality, widely supported across devices and browser versions since January 2020, offers a powerful mechanism for managing async generator lifecycles and ensuring resource cleanup.


## return() Method Behavior

When return() is called on an async generator, the current iteration completes before the return call is processed. This ensures that any pending asynchronous operations are resolved before the generator's execution is terminated.

The method returns a promise that resolves with an object containing two properties: done (a boolean indicating whether control flow has reached the end of the generator) and value (the provided value or the value from the finally block if yielded/returned).

If the return() method is called without a value argument, it behaves as if the next() method has been called, placing the generator in a "completed" state. This allows the generator to perform any necessary cleanup through try...finally blocks.

The return() method can be called at any point during iteration, including after the generator has completed. In the latter case, it returns undefined by default. However, additional values can still be returned after completion by yielding a value before the generator finishes.

This behavior is consistent across devices and browser versions, with full support since January 2020. The implementation ensures proper cleanup through combination with try...finally blocks, allowing controlled termination of asynchronous operations before their natural completion.


## return() Method Examples

Consider the following example, demonstrating the behavior of return() within an async generator:

```javascript

async function* generateNumbers() {

  yield 1;

  yield 2;

  yield 3;

}

const asyncGen = generateNumbers();

async function runExample1() {

  const firstResult = await asyncGen.next();

  const returnResult = await asyncGen.return("Stopped");

  const finalResult = await asyncGen.next();

  console.log(firstResult);

  console.log(returnResult);

  console.log(finalResult);

}

runExample1();

```

This code sequence produces the expected output:

```

{ value: 1, done: false }

{ value: 'Stopped', done: true }

{ value: undefined, done: true }

```

The generator completes its first iteration and then processes the return() call, yielding the provided value "Stopped" in the final iteration.

To further illustrate the impact of return() after generator completion, examine the following:

```javascript

async function* generateValues() {

  yield 10;

  yield 20;

  yield 30;

}

const asyncGen = generateValues();

async function runExample() {

  const firstResult = await asyncGen.next();

  console.log(firstResult);

  const secondResult = await asyncGen.next();

  console.log(secondResult);

  const thirdResult = await asyncGen.next();

  console.log(thirdResult);

  const returnResult = await asyncGen.return("Finished");

  console.log(returnResult);

}

runExample();

```

The output demonstrates this behavior:

```

{ value: 10, done: false }

{ value: 20, done: false }

{ value: 30, done: false }

{ value: 'Finished', done: true }

```

In both cases, the return() method correctly terminates the generator and returns the specified value through the final iteration.

The flexibility of return() is further exemplified by its compatibility with `generator.send()`:

```javascript

async function* generateValues() {

  const value1 = yield 10;

  console.log(`Received value: ${value1}`);

  const value2 = yield 20;

  console.log(`Received value: ${value2}`);

}

const asyncGen = generateValues();

const firstResult = await asyncGen.next();

await asyncGen.return("Finished");

```

Here, calling return() after the first yield resumes execution at the `yield 20` statement, allowing the generator to receive and process the "Finished" value before terminating.

These examples highlight the utility of return() in controlling generator execution and facilitating proper cleanup through combination with try...finally blocks.


## return() Method in Practice

The return() method in AsyncGenerators should be combined with try...finally blocks to ensure proper cleanup and termination. This combination allows generators to perform necessary cleanup tasks before completing execution.

When using return(), consider the effect of yield statements on generator state. In the example where return() is called after yielding ++n, the generator behaves differently than when yielding n++. This demonstrates that return() should be used carefully in combination with yield statements to control generator flow.

In scenarios where an AsyncGenerator needs to be stopped before completion, the return() method provides a reliable mechanism for controlled termination. For instance, a wrapper object can use return() to stop iteration while preserving the generator's ability to perform cleanup tasks.

The method's behavior with rejected promises varies based on loop type. When using for await...of with generators containing rejected promises, the loop will throw and not call finally blocks. In contrast, for...of loops retain the promise structure, allowing finally blocks to be executed.

When working with asynchronous operations, consider the impact of top-level code running synchronously up to the first await. This behavior affects error handling and promise chain construction, particularly in scenarios with unhandled promise rejection errors.


## return() Method and Cancellation

The `return()` method in AsyncGenerators enables external cancellation through the `AbortSignal` API, providing a controlled mechanism for stopping asynchronous operations before their natural completion. By returning a promise that resolves with {done: true, value: undefined}, the method allows generators to perform any necessary cleanup when combined with a try...finally block.

The method's cancellation mechanism works through the underlying promise structure. When an abort signal is received, the generator's internal promise is cleared, preventing further yield operations and allowing the cleanup block to execute. For example, in the given implementation:

```javascript

function timer(time, cancelled) {

  let handle;

  return new Promise((resolve, reject) => {

    handle = setTimeout(resolve, time);

    cancelled.then(() => clearTimeout(handle));

  });

}

```

The `clearTimeout` function is used to cancel the pending timer when the abort signal resolves, effectively stopping the generator before its natural completion.

This cancellation approach is consistent with the broader JavaScript promise system, where rejection is used to signal termination. The TC39 proposal for promise cancellation, while withdrawn, influenced the current implementation, which uses rejection semantics to interrupt generator operations. Modern JavaScript engines, including those in current browsers and Node.js versions, implement this behavior reliably.

For developers implementing cancellable generators, the `AbortSignal` API provides a standardized approach to controlling asynchronous operations. This mechanism allows generators to handle cancellation signals in a way that's consistent with modern JavaScript practices, ensuring proper cleanup and termination of asynchronous tasks.

