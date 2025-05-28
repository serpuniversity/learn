---

title: JavaScript Number toString() Method

date: 2025-05-26

---


# JavaScript Number toString() Method

JavaScript's `toString()` method offers a versatile approach to converting numbers into string representations across multiple bases and value types. This built-in functionality extends beyond basic arithmetic by supporting floating-point numbers, negative values, and even special cases like Infinity and NaN. The method's flexibility makes it particularly useful for formatting output, debugging, and integrating numeric data with text. By understanding how `toString()` handles various data types and conversion parameters, developers can harness its power for efficient and accurate numeric representation in their applications.


## Number Conversion Basics

The `toString()` method in JavaScript converts numbers into string representations while supporting various data types and bases. This versatile method is defined on the `Number.prototype` and can be called on number values, variables, or expressions. It converts numbers to their string representation using the default decimal system, but also supports custom bases from binary (base 2) to hexatridecimal (base 36).

When called without parameters, the method returns the standard string representation of the number. However, by specifying the radix parameter between 2 and 36, developers can convert numbers into different bases. For instance, `5.toString(2)` returns the binary string "101", while `213.toString(16)` produces the hexadecimal string "d5". The method's flexibility extends beyond basic numbers, as demonstrated by its ability to convert floating-point numbers (`9.7.toString()` returns "9.7"), negative numbers (`-20.toString()` returns "-20"), and even non-decimal number systems.

In practical applications, this method proves invaluable for formatting output, debugging, and integrating numeric values with text. For example, it enables developers to easily combine numerical data with descriptive labels, such as logging statements or dynamic content generation. The `toString()` method's broad compatibility across JavaScript implementations ensures consistent behavior in modern browsers and environments, making it a fundamental tool for data manipulation and presentation.


## Conversion Syntax and Parameters

Called with no arguments, the `toString()` method returns the standard string representation of the number. The method accepts a single parameter, `radix`, which specifies the base for representing numeric values and must be an integer between 2 and 36.

The method handles various number formats correctly, including floating-point numbers, negative numbers, and `Infinity`. For instance, `2512.toString()` returns '2512', '2512.toString(16)' returns '9d0', and `(-10).toString(2)` produces '-1010'. The method also processes floating point numbers effectively, as demonstrated by `(9.7).toString()` returning '9.7'.

The radix parameter enables conversion between different number systems. For example:

- `2.toString(2)` returns '10'

- `8.toString(8)` returns '10'

- `16.toString(16)` returns '10'

For non-decimal bases, the method uses letters of the alphabet to represent digits greater than 9: 'a' for 10, 'b' for 11, and so on up to 'z' for 35. This allows conversion to any base up to hexatridecimal (base 36). The method correctly handles negative numbers using positive binary representation with a preceding negative sign, unlike 2's complement notation.

The underlying representation for floating point numbers is base-2 scientific notation, but `toString()` uses the minimum number of significant figures needed to distinguish output from adjacent number values. For particularly large numbers, this can result in multiple valid string representations, with `toString()` typically choosing the form with the most trailing zeros for a given radix.

The method throws a `TypeError` if invoked on an object that is not a Number, making it safe for use on literal number values, variables, or numerical expressions. It returns "Infinity" for `Infinity` and "NaN" for `NaN`, while treating both 0 and -0 as "0".


## Common Usage Scenarios

The `toString()` method enables detailed number-to-string conversions across various bases supported by JavaScript. Basic usage demonstrates its versatility in generating standard and specialized numeric representations:

```javascript

let num = 2512;

console.log(num.toString()); // "2512"

console.log(num.toString(16)); // "9d0"

console.log((-10).toString(2)); // "-1010"

console.log(9.7.toString()); // "9.7"

```

The method handles floating-point numbers effectively by using the minimum significant figures needed for distinct representation at the specified radix. For example:

```javascript

let num = 1024.5;

console.log(num.toString()); // "1.0245e+3" (scientific notation for large numbers)

console.log(num.toString(8)); // "12o2.40625"

console.log(num.toString(16)); // "1.ne4"

```

Its support for bases beyond 10 allows for flexible numeric system conversion:

```javascript

let num = 27;

console.log(num.toString(2)); // "11011"

console.log(num.toString(8)); // "33"

console.log(num.toString(16)); // "1b"

```

This functionality extends to practical developers' applications like precise number formatting and cross-system representation, ensuring consistent behavior across modern JavaScript implementations while facilitating both common and specialized numeric operations.


## Performance Considerations

The performance of number-to-string conversion methods varies slightly across browsers, with the toString() method showing the best results in some cases. Benchmarks indicate that number + '' is typically the fastest method, capable of performing 1 million conversions in 0.1 seconds. However, the difference in speed is minimal and not overly significant.

Chrome demonstrates that number + '' is the fastest method, while Firefox executes .toString() about 100 times slower than '' + num. The performance results can vary significantly when repeated multiple times, so these benchmarks should not be considered overly conclusive.

For practical development, the fastest approach in Chrome is number + '', while in Firefox template string literals perform at the same speed. Both String(number) and number.toString() are approximately 95% slower than the fastest option.

When considering the toString() method specifically, it performs well across different radices, though scientific notation is used for radix 10 when the magnitude (ignoring sign) is 1021 or less than 10-6. The method handles negative numbers correctly using positive binary representation with a negative sign, rather than 2's complement notation.


## Supported Data Types

The `toString()` method extends beyond basic numbers, processing floating-point numbers, negative values, and handling special cases like `Infinity` and `NaN` according to their specific representations:

```javascript

console.log(9.7.toString()); // "9.7"

console.log((-20).toString()); // "-20"

console.log(Infinity.toString()); // "Infinity"

console.log(NaN.toString()); // "NaN"

```

For array conversion, the method concatenates elements into a single string:

```javascript

let arr = [ "Nathan", "Jack" ];

console.log(arr.toString()); // "Nathan,Jack"

```

When applied to boolean values, it returns "true" or "false":

```javascript

let bool = true;

console.log(bool.toString()); // "true"

```

The method handles null and undefined inputs by returning "null" and "undefined" respectively:

```javascript

console.log(null.toString()); // "null"

console.log(undefined.toString()); // "undefined"

```

JavaScript's coercion rules influence how non-number values are converted. For instance:

```javascript

console.log(Number("123")); // 123

console.log(Number("12.3")); // 12.3

console.log(Number("123e-1")); // 12.3

```

