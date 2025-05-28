---

title: JavaScript Promise finally() Method

date: 2025-05-27

---


# JavaScript Promise finally() Method

JavaScript's Promise API has evolved significantly since its introduction, offering developers powerful tools for managing asynchronous operations. The addition of the finally() method in ECMAScript 2018 represents a crucial enhancement to the Promise object, providing a standardized way to execute cleanup code regardless of whether a Promise is fulfilled or rejected. This feature, while semantically similar to existing try-catch-finally blocks, offers distinct benefits in the realm of promise-based programming.

By examining the implementation details, behavior patterns, and practical applications of finally(), we gain valuable insights into modern JavaScript error handling and resource management. Understanding this method's nuances allows developers to write more maintainable, efficient, and cross-browser-compatible code, taking full advantage of the latest JavaScript standards.


## Syntax and Basic Usage

The finally() method of the Promise object returns a callback when a Promise is settled, meaning the promise has either been fulfilled or rejected. It's crucial to understand that this method executes regardless of the outcome of the promise, making it ideal for cleanup code that should run regardless of whether the promise succeeded or failed. This behavior mirrors how a local try-catch-finally block operates in JavaScript, ensuring your application's resources are properly managed in all scenarios.

The method takes a single parameter, onFinally, which is a function that runs when the Promise becomes settled. As demonstrated in the code example provided, even if a promise is rejected with an error, the finally() block will still execute:

```javascript

let task = new Promise((resolve, reject) => {

  setTimeout(() => {

    reject("Promise has been rejected!");

  }, 2000);

});

task

  .then(data => {

    console.log(data); // This will not run

  }, error => {

    console.log("Error:", error); // This runs when rejected

  })

  .finally(() => {

    console.log("This is finally() block that is executed after Promise is settled"); // This always runs

  });

```

When considering how to use finally(), it's important to note that the returned promise from the .finally() method always reflects the final state of the original promise. This means if the original promise was rejected, the finally() block will still complete execution without affecting the rejection status. Conversely, if the original promise was fulfilled, the finally() block will run after any existing then() or catch() handlers.

The method is particularly useful for removing visual loading indicators or clearing up resources after what may be a complex series of asynchronous operations. As one development resource noted, "the finally block executes after the try block (or then in Promises) and catch block have completed, making it the perfect spot for cleanup or final code execution."


## Execution Behavior and Context

The finally() method of JavaScript Promises operates similarly to a local try-catch-finally block in JavaScript, executing a specified function regardless of whether a Promise is fulfilled or rejected. This behavior ensures that your application's resources are properly managed in all scenarios without affecting the original promise's settled state.

To understand the execution context of finally(), it's helpful to consider both its implementation in standard JavaScript control structures and its specific behavior in promise chains:


### Comparison to Local Control Structures

The behavior of finally() mirrors JavaScript's local try-catch-finally structure, executing the finally block after the try block (or then method in Promises) and catch block have completed. This ensures that cleanup or final code execution occurs regardless of the promise's outcome. The finally handler is appended to the promise chain, operating as a final step that runs before any subsequent handlers in the chain.


### Promise Chain Execution

In a promise chain, the finally() block executes after the promise has settled, taking precedence over both then() and catch() handlers. As demonstrated in the code examples provided, the final message in the finally() block will always be printed after any preceding then() or catch() operations:

```javascript

let task = new Promise((resolve, reject) => {

  setTimeout(() => {

    reject("Promise has been rejected!");

  }, 2000);

});

task

  .then(data => {

    console.log(data);

  }, error => {

    console.log("Error:", error);

  })

  .finally(() => {

    console.log("This is finally() block that is executed after Promise is settled");

  });

```

This output sequence shows that the finally() block runs after any error handling but before the promise state is completely resolved:

```

Error: Promise has been rejected!

This is finally() block that is executed after Promise is settled

```


### Returning Values and Error Handling

It's important to note that the return value of the finally() handler does not affect the resulting promise's value. This means that any cleanup operations performed in the finally() block are independent of the promise's fulfillment or rejection status. As the MDN documentation explains, the finally() method's return value is ignored unless it returns a rejected promise, making it ideal for operations that do not produce a meaningful result.

For cases where you need to perform asynchronous cleanup that affects the promise chain, you can structure your code to explicitly handle success and error paths:

```javascript

function myDoStuff(params) {

  return actuallyDoStuff(params)

    .then((result) => {

      return doFinalization().then(() => {

        return "myTransformation " + result;

      });

    },

    (err) => {

      return doFinalization().then(() => {

        throw err;

      }, () => {

        throw err;

      });

    }

  );

}

```

In this implementation, both the success and error paths call doFinalization() and handle its promise resolution or rejection, ensuring proper cleanup while maintaining the promise chain structure.


## Lifecycle Integration and Best Practices

The finally() method offers a clean way to handle cleanup code compared to duplicating it in then() and catch() blocks. It allows developers to ensure resources are properly managed regardless of the promise's outcome, making the code more maintainable and less error-prone.

To effectively use finally(), it's recommended to place cleanup logic in this method rather than the then() or catch() blocks. This pattern helps avoid duplicating cleanup code across multiple handlers and keeps the promise chain structure clear. The method can handle both synchronous and asynchronous cleanup operations, making it flexible for various use cases.

For scenarios where you need to perform operations that affect the promise chain, the method allows chaining both success and error handling within the finally block. This structure maintains the promise chain's integrity while ensuring proper cleanup. The finally() method's return value is ignored unless it returns a rejected promise, making it ideal for operations that don't produce a meaningful result but are crucial for resource management.

Developers should note the method's compatibility across modern browsers, with full support available since June 2020. As with any new language feature, testing with Jest or similar frameworks may require additional considerations to ensure accurate behavior. The method's specification can be found in the ECMAScript standard documentation, though developers may find the MDN implementation to be community-edited and less formal.


## Compatibility and Implementation Details

The `finally()` method is an ECMAScript 2018 feature that provides consistent native implementation across all major browsers since June 2020. As of early 2023, support includes Chrome 63, Edge 79, Firefox 78, Safari 12, and Opera 50. However, Internet Explorer lacks native support, making it an important consideration for compatibility across older browser versions.

In the current JavaScript environment, the method's behavior closely mirrors that of traditional try-catch-finally blocks. Both structures allow for the execution of cleanup code regardless of whether an exception is thrown or caught. This parallelism in behavior ensures that developers can leverage familiar patterns while benefiting from the promise-based structure of modern JavaScript applications.

The method's core functionality remains consistent across both try-catch blocks and Promise chains, with the primary difference being the specific syntax used to define the finally handler. While try-catch blocks use a single finally clause, Promise chains require the explicit .finally() method call. This syntax difference reflects the fundamental difference between block-based and chain-based error handling in JavaScript, though both mechanisms share the same underlying behavior of executing final cleanup code.

TypeScript developers can fully utilize the method by including `"es2018.promise"` in their `tsconfig.json` file, which enables the necessary type definitions. For scenarios where native support is not available, reliable polyfills are widely available via npm repositories, ensuring consistent behavior across all target environments.

