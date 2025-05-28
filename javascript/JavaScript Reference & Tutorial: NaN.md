---

title: JavaScript NaN Property

date: 2025-05-27

---


# JavaScript NaN Property

In JavaScript, the NaN (Not-a-Number) property stands out as a unique value that represents the outcome of mathematical operations that produce undefined or nonsensical results. This fundamental concept is crucial for developers to understand, as JavaScript's handling of NaN influences everything from basic arithmetic operations to complex data transformations. The property's quirks, such as its inability to equal itself (NaN !== NaN), make it a fascinating case study in how programming languages manage mathematical indeterminacies. By exploring the origins, behavior, and proper handling of NaN, we can write more robust, error-tolerant JavaScript code that gracefully handles the unexpected results of numerical operations.


## Introduction to NaN

The NaN property in JavaScript represents Not-a-Number and serves as a legal value of type Number. This unique representation allows JavaScript to handle mathematical operations that produce undefined or nonsensical results without crashing the program.

When performing impossible calculations such as dividing zero by zero or taking the square root of a negative number, JavaScript returns NaN to signal that something has gone wrong with the operation. The value NaN specifically arises in three main scenarios:

1. When attempting to convert non-numeric strings to numbers, as demonstrated by Number("banana") resulting in NaN

2. During arithmetic operations with incompatible types, such as 7 * "blabla"

3. In cases where the operation is mathematically undefined, like Math.sqrt(-1)

The global property NaN is equivalent to the Number.NaN property and has several distinctive attributes:

- Writable: no

- Enumerable: no

- Configurable: no

- Values resulting in NaN include:

  - Failed number conversion: parseInt("blabla"), Number(undefined)

  - Math operations with non-real results: Math.sqrt(-1)

  - Indeterminate forms: 0 * Infinity, 1 ** Infinity, Infinity / Infinity, Infinity - Infinity

  - Method calls where operands get coerced to NaN: 7 ** NaN

  - Invalid values represented as numbers: new Date("blabla").getTime(), "".charCodeAt(1)


### Comparisons and Behaviors

One of NaN's most notable properties is that it is not equal to itself: NaN === NaN returns false, while NaN != NaN returns true. This behavior is consistent across all modern browsers and is a key aspect of how NaN functions within JavaScript's number system.

When performing relational comparisons with NaN, all comparison operations with NaN return false. For example, 1 < NaN, NaN == 1, and NaN > 1 all evaluate to false. This property makes NaN unique among JavaScript values, as every other value correctly reports inequality for itself.


### Handling NaN

The global isNaN() function has been available since the first edition of ECMAScript, dating back to 1997. This function converts the value to a number before testing it, making it distinct from Number.isNaN(). While both functions return true for NaN, only Number.isNaN() correctly identifies Number.NaN and returns false for other values. For example, Number.isNaN("NaN") returns false, while isNaN("NaN") returns true.

Developers should use Number.isNaN() or the global isNaN() function to detect NaN values. The recommended practice is to avoid direct comparisons to NaN using === or !==, as these will always return false for NaN. Instead, use the following patterns:

- Checking for NaN: if (Number.isNaN(value)) { ... }

- Non-NaN check: if (!Number.isNaN(value)) { ... }


## NaN's Unique Properties

This peculiar property stems from JavaScript's implementation of the IEEE 754 standard for floating-point arithmetic, which introduced NaN as a special value to represent undefined or unrepresentable results. This design choice allows NaN to propagate through calculations, transforming useful numerical results into meaningless values. For example, any operation involving NaN yields NaN, demonstrating this contagious nature.

The unique behavior of NaN being unequal to itself (NaN !== NaN) serves an important practical purpose. This property prevents false equivalences that would occur if calculations returned null or undefined instead of NaN. When JavaScript encounters an operation that produces an undefined result, such as dividing zero by zero or taking the square root of a negative number, it signals the error by returning NaN. This allows programmers to identify and handle such cases in their code.

NaN behaves similarly to other floating-point limitations, acting as a placeholder for computations that exceed the language's mathematical capabilities. Just as early computing hardware faced challenges with representing fractions and irrational numbers, modern JavaScript builds upon a framework that balances practicality with performance constraints. Understanding these origins helps explain why NaN appears in specific scenarios like string-to-number conversions, division by zero, and invalid arithmetic operations, while acknowledging its role as a necessary if imperfect solution to complex computational problems.


## Detecting NaN

The global isNaN() function determines whether a value is NaN (Not-a-Number) by converting it to a number if necessary. This function supports various data types including number, BigNumber, bigint, Fraction, Unit, and Array or Matrix input, evaluating element-wise for Matrix input. The function returns true if the value is NaN after conversion and false otherwise.

Key points about the isNaN() function include:

1. It coerces non-numeric arguments to numbers before testing, which can lead to counterintuitive results. Empty strings become 0, and boolean primitives become 0 or 1.

2. It returns true for NaN arguments and false for other values that coerce to valid non-NaN numeric values, such as empty strings and boolean primitives.

3. The function is part of the global object and handles NaN values through arithmetic operations that produce undefined or unrepresentable results.

For precise testing of NaN values, developers should use Number.isNaN(), which returns true if the input value is a number and NaN, or false otherwise. The function does not force-convert the parameter to a number, making it safer for values that would normally convert to NaN but are not actually the same value as NaN.


## Operations That Yield NaN

JavaScript's `NaN` (Not-a-Number) property represents a value that is not a valid number, reflecting mathematical operations that generate undefined or unrepresentable results. Understanding where `NaN` arises and how to detect it is crucial for robust JavaScript development, particularly in mathematical computations and data transformations.


### Key Scenarios Producing NaN

- **Division by zero**: The operation `0 / 0` results in `NaN`, symbolizing an arithmetic indeterminacy. Similarly, multiplication of infinity by zero yields `NaN`.

- **Type coercion with invalid operations**: Attempts to add a number to a non-numeric string, such as `7 + "apple"`, also produce `NaN`.

- **Mathematical limits**: Operations with infinity, like `Infinity / Infinity` or `1 ** Infinity`, return `NaN`. Additionally, taking the square root of a negative number leads to this special value: `Math.sqrt(-1)` produces `NaN`.


### Detection and Handling

JavaScript provides multiple mechanisms to identify `NaN` values. The most reliable approach is to use `Number.isNaN()`, which returns true only for the number `NaN` and false for other values that may coerced to NaN or represent valid numbers. For general JavaScript compatibility, the global `isNaN()` function is also effective but coerces its argument to a number before testing, which can lead to unexpected results with certain inputs.


### Operations Involving NaN

Any mathematical operation involving `NaN` propagates this value, making `NaN` contagious. For example, `NaN + 5` results in `NaN`. This behavior ensures that invalid computations do not produce silent errors but requires developers to implement explicit checks to handle or isolate these values. The `isNaN()` function provides a straightforward way to detect whether an operation has produced a non-numeric result, allowing programmers to take appropriate corrective action in their code.


### Historical Context

The IEEE 754 standard, published in 1985, established `NaN` as a special floating-point value to represent undefined or unrepresentable results. This standard built upon early computing challenges with representing fractions and irrational numbers, creating a consistent arithmetic model that has become fundamental to modern programming languages. While the existence of `NaN` introduces complexities in numerical computations, its implementation has become so widely adopted that most contemporary programming languages default to treating mathematical errors as `NaN` when more precise alternatives would be impractical or unwieldy.


## Best Practices for Handling NaN

Developers should implement several best practices to effectively handle NaN values in JavaScript:


### Validate Input Data

Always validate input data before performing calculations. This helps prevent NaN values from propagating through your code. For example:

```javascript

function safeDivide(a, b) {

  if (b === 0) {

    return 'Division by zero not allowed';

  }

  let result = a / b;

  return isNaN(result) ? 'Invalid division' : result;

}

```


### Use Conditional Checks

Implement explicit checks to avoid operations that might yield NaN. This ensures your code handles invalid inputs gracefully:

```javascript

let value = NaN;

console.log(value === NaN); // Outputs: false

console.log(Number.isNaN(value)); // Outputs: true

```


### Use isNaN() Function

The global isNaN() function should be used to check for NaN values. It converts the value to a number before testing, making it suitable for various data types:

```javascript

console.log(isNaN(12)); // false

console.log(isNaN(0 / 0)); // true

console.log(isNaN(12.3)); // false

console.log(isNaN("Geeks")); // false

console.log(isNaN("13/12/2020")); // false

console.log(isNaN(-46)); // false

console.log(isNaN(NaN)); // true

```


### Prefer Number.isNaN() for Precise Checks

For safer type checking, prefer Number.isNaN(). This method returns true only for the number NaN, while global isNaN() correctly identifies Number.NaN and returns false for other values:

```javascript

let value = NaN;

console.log(Number.isNaN(value)); // true

console.log(isNaN(value)); // true

```


### Avoid Direct NaN Comparisons

Direct comparisons to NaN using === or !== will always return false for NaN. Instead, use the following patterns:

- Checking for NaN: if (Number.isNaN(value)) { ... }

- Non-NaN check: if (!Number.isNaN(value)) { ... }


### Handle Type Coercions Carefully

Be aware that JavaScript coerces non-numeric arguments to numbers before testing them, which can lead to unexpected results. For example, empty strings become 0, and boolean primitives become 0 or 1:

```javascript

console.log(Number("")); // 0

console.log(Number(true)); // 1

```


### Implement Error Handling

For calculations that might produce NaN, implement error handling mechanisms. This prevents silent failures and ensures your application can recover from errors gracefully:

```javascript

function clean(x) {

  if (x === Number.NaN) {

    return null;

  }

  if (isNaN(x)) {

    return 0;

  }

}

console.log(clean(Number.NaN)); // Expected output: 0

```


### Follow Best Practices

Adhere to consistent coding standards and best practices when working with NaN values. This ensures your code remains maintainable and robust across different development environments and JavaScript versions:

```javascript

function sanitize(x) {

  if (isNaN(x)) {

    return Number.NaN;

  }

  return x;

}

```

