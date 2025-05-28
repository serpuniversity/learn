---

title: JavaScript Boolean.toString() Method

date: 2025-05-26

---


# JavaScript Boolean.toString() Method

The Boolean.toString() method in JavaScript provides a straightforward way to convert boolean values to their string representations ("true" or "false"). While its implementation details are interesting, the method's practical applications extend beyond simple value conversion to support essential JavaScript functionality. In this exploration, we'll examine how to use Boolean.toString(), understand its behavior across different contexts, and compare it with alternative conversion methods in terms of performance and utility.


## Method Overview

The Boolean.toString() method converts a boolean value to its string representation, specifically returning "true" for true and "false" for false. This method operates on boolean values directly or through their corresponding Boolean object wrappers. For example, new Boolean(true).toString() returns "true", while new Boolean(false).toString() returns "false". The method can also be called directly on boolean primitive values, though its implementation for these cases follows the same algorithm as the initial toString implementation rather than the Boolean object's overridden method.

JavaScript's native boolean values and their wrapper objects both support this method, allowing for seamless conversion between boolean logic and string representation across the language's core functionality. This built-in method provides a standardized way to handle boolean values in contexts requiring string inputs, such as debugging, data serialization, or API interactions.


## Method Implementation

The method returns 'true' for boolean true and 'false' for boolean false. It operates similarly for boolean primitives and Boolean object wrappers, though its implementation for primitive values follows the native boolean's algorithm rather than the Boolean object's overridden method.

When called directly on a boolean object, the method returns "Overridden" rather than the expected true or false. For example, new Boolean(true).toString() actually returns "Overridden", even though it behaves correctly in practice by returning "true".

As documented in the specification, the method returns the numeric code unit value of the string "C" converted to a String of four hexadecimal digits. This implementation detail is important for understanding the method's underlying mechanics, particularly when considering its relationship to Object.prototype.toString() and Boolean.prototype.toString().

The method throws errors for non-boolean values, as demonstrated by attempts to convert undefined, NaN, or non-boolean objects. However, it's worth noting that all objects become true in boolean context, meaning they can be coerced to true using techniques like !!x or Boolean(x).

Within the broader context of JavaScript's boolean conversion process, the toString() method plays a crucial role in bridging the gap between boolean logic and string representation. Its behavior is consistent across browsers, making it a reliable choice for situations requiring explicit boolean-to-string conversion.


## Browser Support

The Boolean.toString() method is supported in all modern browsers, including Chrome, Edge, Firefox, Safari, and Opera, with full compatibility in Internet Explorer. This method's implementation across browsers demonstrates JavaScript's design philosophy of maintaining consistent behavior while allowing for efficient execution in various host environments.

The method functions identically in all supported browsers, returning "true" for boolean true and "false" for boolean false. This uniformity is crucial for developers working across different browser platforms, ensuring that boolean-to-string conversion behaves predictably regardless of the specific environment.

The widespread support for this method across browsers underscores its importance in JavaScript's ecosystem. As a built-in functionality of both primitive boolean values and Boolean object wrappers, it enables seamless integration with web development practices, from simple form validation to complex data serialization scenarios.


## Method Usage

The conversion of Boolean values to strings in JavaScript can be achieved through multiple methods, each with its own advantages and use cases. The most direct approach is to call the .toString() method on the boolean value, as demonstrated in the following example:

```javascript

let bool = true;

let result = bool.toString(); // returns "true"

```

This method works consistently across all boolean values and their wrappers, though it's important to note that its performance is generally slower than alternative approaches:

```javascript

const time = 10000000

console.time('toString')

for(let i = 0; i < time; i++) true.toString()

console.timeEnd('toString')

```

Another common approach is to use the template literal syntax:

```javascript

let bool = true;

let result = `${bool}`; // returns "true"

```

This method provides a concise way to convert boolean values while maintaining performance. It works particularly well in modern JavaScript environments and TypeScript versions 2.9.0-dev.20180327 and later.

```javascript

const booleanVal = true;

const stringBoolean = `${booleanVal}`;

```

For situations where absolute performance is critical, developers often opt for the simple addition operation:

```javascript

let bool = true;

let result = bool + ""; // returns "true"

```

This approach is the fastest of the basic methods, though it may not be as clear in intent as the other options.

In addition to these basic methods, developers have several more complex options available. They can use a ternary operator to explicitly return "true" or "false" strings:

```javascript

myString = myBool ? "true" : "false";

```

Or implement a custom function that handles the conversion:

```javascript

function booleanToString(b) {

  return b.toString();

}

```

These methods provide flexibility for handling boolean values in various contexts, from simple string concatenation to more complex data processing scenarios.


## Performance Considerations

When comparing the performance of different methods for converting boolean values to strings in JavaScript, several approaches demonstrate varying levels of efficiency. The most direct method, utilizing the addition operator, proves to be the fastest option:

```javascript

let bool = true;

let result = bool + ""; // returns "true"

```

This approach achieves optimal performance while maintaining clarity in code intent. For reference, benchmarking the simplest method against the toString() method reveals significant performance differences:

```javascript

const time = 10000000

console.time('toString')

for(let i = 0; i < time; i++) true.toString()

console.timeEnd('toString')

console.time('String(bool)')

for(let i = 0; i < time; i++) String(true)

console.timeEnd('String(bool)')

```

The addition-based conversion (using either + operator or template literals) proves consistently faster than the built-in toString() method, making it the preferred choice for high-performance applications where string representations of boolean values are required. This method's speed advantage stems from its core JavaScript implementation, directly converting the boolean value to a string without the overhead associated with method calls.

