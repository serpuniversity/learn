---

title: JavaScript isNaN() Function

date: 2025-05-26

---


# JavaScript isNaN() Function

The JavaScript isNaN() function provides a way to check if a value is NaN (Not-a-Number), but its behavior can be confusing due to type coercion. Here's what you need to know about using this function correctly.


## Basic Usage of isNaN()

The isNaN() function checks if a value is NaN (Not-a-Number) by converting the value to a number first. Here's how it handles different types of inputs:


### Numeric Values

- Returns false for all actual numbers, including integers and floating-point numbers

- Example: `isNaN(42) === false`

- Example: `isNaN(-3.14) === false`


### Non-numeric Strings

- Returns true for strings that cannot be converted to numbers

- Example: `isNaN("hello") === true`

- Example: `isNaN("123") === false` (This is a string representation of a number, not the number itself)


### Special JavaScript Values

- Returns true for strings representing NaN, such as "NaN"

- Example: `isNaN("NaN") === true`

- Returns true for undefined values

- Example: `isNaN(undefined) === true`

- Returns true for null values

- Example: `isNaN(null) === false` (null is not the same as NaN)


### Array and Object Inputs

- Returns false for empty arrays

- Example: `isNaN([]) === false` (As shown in the original behavior analysis)

- Returns true for objects, including empty objects

- Example: `isNaN({}) === true`


### Mathematical Operations

- Returns true for results of invalid mathematical operations (e.g., 0/0)

- Example: `isNaN(0/0) === true`

The function uses type coercion to convert values to numbers before testing, which can lead to counterintuitive results with certain inputs. For a more precise check that works across all JavaScript environments, including modern ones and Node.js, developers are advised to use the built-in isNaN() function.


## Behavior with Various Value Types

The function's behavior for non-numeric arguments can be confusing. For example, an empty string is coerced to 0, while a boolean is coerced to 0 or 1. Both values are not NaN, but they don't evaluate to NaN, so `isNaN()` returns false. This behavior extends to other non-numeric strings like "2005/12/12", "undefined", and "NaN" which also return false when passed to `isNaN()`.

Understanding coercion is crucial for avoiding confusion, as demonstrated by the behavior of `isNaN(parseInt([1,2,3]))`, which returns false because the array is coerced to a string representation, while `isNaN([1,2,3])` returns true. This behavior can lead to unexpected results when working with numeric values that don't evaluate to NaN.

A better approach for checking if a value is truly NaN is to use the expression `x !== x`, which directly tests for NaN based on its unique property of being the only value that is not equal to itself. The MDN Web Docs provide an alternative solution that works across ECMAScript versions: `Number.isNaN(x)` for ECMAScript-6 users, or a polyfill that combines both methods for consistency: `Number.isNaN = Number.isNaN || (function(value) { return value !== value; })`.

While `isNaN()` handles many common cases, including division by zero (`0/0`), it's important to note that it returns true for strings like "Hello" and objects like `{}`, making it less reliable than `Number.isNaN()` when performing strict numeric checks.


## Differences from Number.isNaN()


### Differences in Handling Non-Number Arguments

Whereas `isNaN()` coerces all arguments to numbers before testing, `Number.isNaN()` treats non-number inputs as false. For example:

```javascript

isNaN(NaN) === true  // NaN is coerced to itself, true

Number.isNaN(NaN) === true  // Direct NaN check, true

isNaN([]) === false  // Empty array coerces to 0, false

Number.isNaN([]) === false  // Direct check, false

isNaN({}) === true  // Object coerces to NaN, true

Number.isNaN({}) === false  // Direct check, false

```


### Edge Cases

`Number.isNaN()` handles edge cases more reliably:

- Returns true for all non-number values including objects and strings

- `Number.isNaN(null) === false`  (null is distinguished from NaN)

- `Number.isNaN(undefined) === false` (undefined is not NaN)

- `Number.isNaN("") === false` (Empty string coerces to 0)

- `Number.isNaN(true) === false` (Boolean true coerces to 1)


### Method Implementation

The `Number.isNaN()` method provides a safer alternative with consistent behavior across environments:

```javascript

Number.isNaN = Number.isNaN || function(value) {

  return value !== value;  // Direct NaN check

}

```


### Best Practices

For robust NaN checking, especially with object inputs, use Number.isNaN() instead:

```javascript

const value = {};  // Example non-number value

if (Number.isNaN(value)) {

  console.log("Value is not a number");

} else {

  console.log("Value is a number or can be converted to one");

}

```

This approach ensures accurate NaN detection while avoiding type coercion pitfalls.


## Handling Common Value Types

The function returns true for non-numeric string values like "NaN", "undefined", and "{}", as well as for undefined values. However, it returns false for numeric values including integers and floating-point numbers, as seen in the examples `isNaN(42) === false` and `isNaN(-3.14) === false`.

For array and object inputs, the function behaves as follows:

- Returns false for empty arrays: `isNaN([]) === false`

- Returns true for objects, including empty objects: `isNaN({}) === true`

Specifically, the function treats the following values as described:

- Strings that cannot be converted to numbers return true: `isNaN("hello") === true`, `isNaN("123") === false` (Note: The string "123" evaluated to a number, not a string representation of a number)

- Empty strings evaluate to 0, which is not NaN: `isNaN("") === false`

- Boolean values coerce to 0 or 1, which are not NaN: `isNaN(true) === false`, `isNaN(false) === false`

The behavior of `isNaN()` with mathematical operations is consistent for values that evaluate to NaN:

- Returns true for division by zero: `isNaN(0/0) === true`

- Returns false for valid mathematical results: `isNaN(12) === false`, `isNaN(-3.14) === false`


## ECMAScript and Browser Support

The function's support across browsers has been robust, with full implementation in all major modern browsers including Chrome, Firefox, Safari, and Opera. Notable support extends to Internet Explorer since June 2017, making it a widely available tool for developers.

However, it's crucial to understand that while `isNaN()` works across all these environments, its behavior with certain inputs can differ from browser to browser due to variations in JavaScript engine implementations. Common edge cases include strings with trailing spaces (like "2 ") and unexpanded fractions (like "1/2"), where the function may return inconsistent results.

For developers working across multiple environments, the provided examples demonstrate how `isNaN()` can yield unexpected outcomes:

```javascript

var numex = "2 ";

alert(isNaN(numex)); // Returns false in modern browsers, true in older implementations

numex = "1/2";

alert(isNaN(numex)); // Returns true in modern browsers, false in older implementations

```

To ensure consistent behavior, particularly with user input, developers are advised to use regular expressions to normalize input strings before using `isNaN()`. The text provides an effective approach for cleaning up input:

```javascript

numex = "2 I think";

alert(isNaN(numex.replace(/\D/g, ''))); // Returns false after stripping non-digit characters

```

This approach helps maintain reliable NaN checking across different JavaScript environments, while still leveraging the widely available `isNaN()` function.

