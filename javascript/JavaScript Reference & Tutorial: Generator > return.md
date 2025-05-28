---

title: JavaScript Generators: return Statement

date: 2025-05-26

---


# JavaScript Generators: return Statement

JavaScript generators provide a powerful mechanism for creating manageable, iterable sequences of values. These functions allow developers to control the flow of execution through a complex algorithm, pausing and resuming operations as needed. At their core, generators are built around the yield statement, which enables the return of intermediate values and the suspension of function execution. However, the return statement within a generator introduces additional complexity by managing the termination of generator operations and the handling of cleanup tasks.

When a generator function encounters a return statement, it immediately halts execution and returns a final value, setting the generator's completion state. This basic behavior is crucial for controlling the termination of generator operations and returning meaningful results to the caller. However, the true power of return statements in generators lies in their interaction with try...finally blocks. By combining return with error handling constructs, developers can perform critical cleanup tasks before generator termination, ensuring that resources are properly released and state is preserved.

Understanding the nuances of return statements in JavaScript generators is essential for writing robust, maintainable iterator-based code. Whether managing complex algorithmic operations or performing resource-intensive tasks, the ability to control generator termination and perform cleanup tasks makes these powerful features indispensable for modern JavaScript development.


## return Statement in Generators

When a return statement is encountered in a generator function, it causes the generator to exit and return a value, setting the generator's completion state. In its simplest form, calling the return method without arguments sets the generator's value property to undefined and its done property to true, indicating that the generator has completed its execution.

The return statement behaves similarly to a normal return statement when used as part of a yield expression. For example, consider the generator function `generateSequence()`, which yields the numbers 1 and 2 before returning 3:

```javascript

function *generateSequence() {

  yield 1;

  yield 2;

  return 3;

}

```

When this generator is executed using the `next()` method, it returns an object with the value and done properties:

```javascript

let generator = generateSequence();

let one = generator.next(); // { value: 1, done: false }

let two = generator.next(); // { value: 2, done: false }

let three = generator.next(); // { value: 3, done: true }

```

In this case, the third call to `next()` returns the completion value 3 with done set to true, indicating that the generator has reached its termination point.

The return statement's behavior can be customized using a try...finally block. When the yield expression is wrapped in a try...finally block, the return statement causes execution to proceed to the finally block before returning. If the generator is suspended within a try block, the finally block will execute, allowing cleanup tasks to be performed. In this configuration, the return value of the finally block can become the value of the returned object, providing flexibility for controlled termination of generator operations.


## return Method Behavior

When called without arguments, the return method sets the value property to undefined and the done property to true, indicating that the generator has completed its execution. This behavior occurs regardless of whether the generator is in a completed state or still suspended when the return method is called.

The return statement's behavior changes if the yield expression is wrapped in a try...finally block. In this configuration, the return method causes execution to proceed to the finally block. If the generator is suspended within a try block, the finally block will execute, allowing cleanup tasks to be performed. The return value of the finally block can become the value of the returned object, providing flexibility for controlled termination of generator operations.

The return method preserves the completion state of the generator. If called while the generator is in the "completed" state (i.e., after all yield expressions have been executed), it sets the done property to true and returns the current value property. If called while the generator is suspended, it sets the done property to false and returns the current value property. This means that subsequent calls to the next() method on the generator will continue to return the current value and set done to false until all yield expressions have been exhausted, at which point calling next() will return { value: undefined, done: true }.


## return with try...finally Block

In scenarios where the yield expression is wrapped within a try...finally block, the return method's behavior diverges from its typical operation. Instead of immediately terminating generator execution, it causes control flow to proceed to the finally block. If the generator's execution has paused within a try block, the finally block will be executed, facilitating proper cleanup procedures.

This unique behavior allows developers to perform necessary cleanup tasks before generator termination. For example, consider a generator function responsible for processing network requests. By combining return with try...finally, developers can ensure that all open connections are properly closed before the generator concludes its operations:

```javascript

function* processRequests() {

  try {

    for (let request of requestQueue) {

      yield handleRequest(request);

    }

  } finally {

    closeAllSockets();

  }

}

```

In this configuration, should the closeAllSockets() function require execution regardless of program flow (such as in the event of generator termination or error), the finally block ensures its invocation.


## Generators and Completion State

The return() method in JavaScript generators acts as if a return statement is inserted in the generator's body at the current suspended position. It finishes the generator and allows it to perform any cleanup tasks when combined with a try...finally block. This method returns an object with two properties: done (a boolean indicating whether the generator function's control flow has reached the end) and value (the value returned or the value yielded from the finally block if the yield expression is wrapped in a try...finally block).

When called without an argument, the method returns an object with done set to true and value set to undefined, indicating that the generator has completed its execution. If called while the generator is suspended, it sets done to false and returns the current value property, allowing the generator to continue execution until all yield expressions have been exhausted. In this state, calling next() on the generator will return { value: undefined, done: true }.

The return() method can be called after the generator is in a "completed" state. While the generator remains in this state, the method's primary effect is to allow cleanup tasks to be performed through try...finally blocks. The generator's status changes from suspended to closed when all yields are processed and a return statement is encountered, at which point subsequent calls to next() will return { value: undefined, done: true }.

