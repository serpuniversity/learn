---

title: AggregateError: Managing Multiple JavaScript Errors

date: 2025-05-26

---


# AggregateError: Managing Multiple JavaScript Errors

JavaScript's error handling has evolved significantly with the introduction of AggregateError, a specialized error type designed for managing multiple errors in a single structured object. This powerful feature, introduced in ECMAScript 2026, addresses common needs in modern JavaScript development, such as form validation and parallel API requests. However, its recent addition to the language specification means developers must understand its capabilities and proper usage to leverage this important functionality effectively. Together, we'll explore how AggregateError works, how to use it correctly, and when it's the right tool for managing multiple JavaScript errors.


## What is AggregateError?

AggregateError is a JavaScript error type specifically designed to handle situations where multiple errors need to be collected and reported as a single error object. This includes scenarios like form validation, where multiple validation errors need to be grouped together, or when multiple API requests fail, requiring a unified error response.

The constructor for AggregateError requires an iterable of errors and can optionally take a message and an options object. The errors property contains an array of the errors that were aggregated, with each error maintaining its original properties and behavior. This allows for a detailed error structure while maintaining compatibility with existing error handling mechanisms.

A practical example demonstrates its usage within a Promise context:


## Core Concepts and Usage

The AggregateError constructor can be called with or without the new keyword, creating a new instance in both cases. It accepts three parameters: an iterable of errors, an optional message, and an optional options object containing a cause property.

The constructor signature allows for multiple valid calls:

- new AggregateError(errors, message)

- new AggregateError(errors, message, options)

- AggregateError(errors)

- AggregateError(errors, message)

- AggregateError(errors, message, options)

The constructor creates an AggregateError instance with the following properties:

- A constructor property matching the AggregateError constructor

- A name property set to "AggregateError"

- An errors property containing an array of the aggregated errors, maintaining their original properties and behavior

When creating an AggregateError instance, the constructor takes the following parameters:

- errors: An iterable of errors, which may not be TypeError instances

- message: An optional human-readable description of the aggregate error

- options: An optional object with a cause property indicating the specific cause of the error

Here's a practical example demonstrating constructor usage in a Promise context:

```javascript

try {

  throw new AggregateError([new Error("some error")], "Hello");

} catch (e) {

  console.log(e instanceof AggregateError); // true

  console.log(e.message); // "Hello"

  console.log(e.name); // "AggregateError"

  console.log(e.errors); // [ Error: "some error" ]

}

```


## AggregateError Methods and Properties

The AggregateError constructor creates a new AggregateError instance with the specified parameters, using either the new keyword or without it. The constructor accepts an iterable of errors, an optional message, and an optional options object.

The errors property contains an array of the aggregated errors, maintaining their original properties and behavior. The constructor function has the following properties:

- A constructor property matching the AggregateError constructor

- A name property set to "AggregateError"

- An errors property containing an array of the aggregated errors, maintaining their original properties and behavior

The constructor specification is defined in the ECMAScript 2026 Language Specification, section sec-aggregate-error-constructor. The AggregateError object inherits instance methods from its parent Error and has the following properties:

- constructor: The constructor function that created the instance object

- name: Represents the name for the type of error, with an initial value of "AggregateError"

- errors: An array representing the errors that were aggregated

The AggregateError object also has the standard Error properties and methods, including:

- message: Used by AggregateError.prototype.message to display the message of error, with a default value of an empty string

- name: Used by AggregateError.prototype.name to display the name of error, with an initial value of "AggregateError"

Some key usage examples demonstrate the object's functionality:

```javascript

// Single error message example

try {

  throw new AggregateError([new Error("some error")], "Hello");

} catch (e) {

  console.log(e instanceof AggregateError); // true

  console.log(e.message); // "Hello"

  console.log(e.name); // "AggregateError"

  console.log(e.errors); // [ Error: "some error" ]

}

// Multiple errors example

const errors = [new Error("Error 1"), new Error("Error 2"), new Error("Error 3")]

throw new AggregateError(errors, "Multiple errors occurred");

// AggregateError with options example

try {

  throw new AggregateError([new Error("some error")], "Hello", { cause: errors[0] });

} catch (e) {

  console.log(e.cause === errors[0]); // true

}

```

Note that while AggregateError provides robust error handling capabilities, its browser compatibility is limited to modern browsers. For broader compatibility, developers should consider using polyfills like those available in core-js or implementing custom error aggregation logic.


## Best Practices and Considerations

AggregateError excels in scenarios where multiple errors need to be reported together, such as form validation or parallel API requests. This error type consolidates multiple validation errors into a single feedback message, providing a better user experience by giving users feedback on all issues at once.

The primary use case for AggregateError is when an operation encounters multiple failures simultaneously. For instance, if Promise.any() receives multiple promises that all reject, it returns a single AggregateError object containing information about all the failed promises. This feature debuted in ECMAScript 2026, making it widely available across modern browsers since September 2020.

Developers should use AggregateError when multiple errors are possible and need to be handled together. It streamlines error reporting by allowing a single try-catch block to handle all aggregated errors, making debugging easier with comprehensive error information.

However, due to its relatively recent introduction, broad compatibility requires either modern browsers or polyfills like core-js's implementation of ECMAScript promises. When using polyfills, developers may need to adjust their constructor syntax. For example, in environments like Opera, Internet Explorer, Edge, or Node.js, the following approach is necessary:

```javascript

const AggregateError = require('es-aggregate-error');

try {

  throw new AggregateError([new Error("some error")], "Hello");

} catch (e) {

  console.log(e instanceof AggregateError); // true

  console.log(e.message); // "Hello"

  console.log(e.name); // "AggregateError"

  console.log(e.errors); // [ Error: "some error" ]

}

```

This approach ensures consistent behavior across different JavaScript environments while leveraging the powerful error aggregation capabilities of AggregateError.


## Browser Support and Polyfills

AggregateError has achieved wide browser support, especially since its introduction in September 2020. The feature is now available across desktop browsers including Chrome 85+, Firefox 79+, and Safari 14+, though it remains unsupported in Internet Explorer, Edge, and Opera.

For mobile browsers, support is more robust, with full compatibility in Chrome 85, Firefox 79, and Safari 14. Server-side support is non-existent, with Node.js lacking built-in implementation.

Developers facing compatibility issues can turn to polyfills like core-js's ECMAScript promises implementation or es-shims' separate package. The core-js solution requires no special syntax, while es-shims requires importing the es-aggregate-error module.

The AggregateError constructor and prototype methods are well-established across supported environments, though older browsers and Node.js versions require polyfills for proper functionality. Its role in modern JavaScript development is particularly valuable for operations that may encounter multiple failures simultaneously, such as form validation or parallel API requests.

