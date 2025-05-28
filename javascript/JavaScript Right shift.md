---

title: JavaScript Right Shift Operator (>>)

date: 2025-05-27

---


# JavaScript Right Shift Operator (>>)

The right shift operator (>>) in JavaScript performs bitwise shifts on numeric values, offering developers a powerful way to manipulate binary data. While its behavior is well-defined for positive numbers, the operator presents unique challenges when working with negative values and large integer types. Through a detailed examination of its implementation and usage patterns, this article reveals how JavaScript's right shift operator processes unsigned 32-bit integers and applies sign propagation to maintain consistent results across positive and negative inputs. Understanding this fundamental bitwise operation is crucial for developers working with low-level data manipulation in JavaScript, particularly when implementing efficient algorithms or optimizing numerical computations.


## Overview of the Right Shift Operator

The right shift operator (>>) in JavaScript performs a bitwise operation that shifts the bits of a number to the right. This operation is governed by specific rules that ensure consistent behavior across positive and negative numbers.

When performing a right shift, JavaScript first converts the left operand to an unsigned 32-bit integer. This means that any bits beyond the 32nd position are discarded, ensuring the operation works within a fixed bit width. The right operand is similarly converted to an unsigned 32-bit integer and then reduced to a value between 0 and 31 using a modulo operation.

The actual shift operation preserves the sign of the original number through sign propagation. For positive numbers, the most significant bit remains unchanged, effectively dividing the number by two for each shift position. This behavior can be observed in the following examples:

```javascript

9 >> 2; // 2

-9 >> 2; // -3

```

The division analogy applies when using the right shift operator to halve numbers, as demonstrated by the `divByTwo` function:

```javascript

function divByTwo(n) {

  return n >> 1;

}

divByTwo(5); // 2

divByTwo(-45); // -23

```

It's important to note that while the operator effectively divides numbers by two with each right shift, it always rounds down to the nearest integer, as shown in the final example above.


## Right Shift Operator Behavior

The right shift operator (>>) in JavaScript performs a bitwise operation that shifts the bits of a number to the right, with specific behavior for both positive and negative operands. This operation is defined in the ECMAScript 2026 Language Specification and has been supported in JavaScript environments since July 2015.

For positive numbers, the right shift operation divides the number by two for each position shifted, effectively performing integer division. The most significant bit remains unchanged, preserving the original value's magnitude. This behavior is illustrated in the divByTwo function, which correctly divides its input by two using right shift:

```javascript

function divByTwo(n) {

  return n >> 1;

}

```

The operator's effect on negative numbers differs from positive numbers through sign preservation. When shifting a negative number, the leftmost bit (sign bit) is replicated to fill the vacated positions, maintaining the number's negative value. This is demonstrated in the comparison between -9 >> 2, which yields -3, and -9 >>> 2, which produces 1073741821 using the unsigned right shift operator (discussed further in another section).

When applying the right shift operator, both operands are first converted to unsigned 32-bit integers. The right operand undergoes a modulo 32 operation to ensure the shift amount is between 0 and 31, inclusive. This conversion process ensures consistent behavior across different numeric representations, including those with more than 32 bits, where only the most significant 32 bits are considered.

The operator's conversion process affects how non-integer values are handled. Using `>> 0` to truncate numbers to integers can produce unexpected results due to this automatic conversion to 32-bit integers, potentially leading to loss of significant bits for numbers outside the range -2147483648 to 2147483647.


## Supported Browsers and Versions

The right shift operator is widely implemented across JavaScript environments, including all modern browsers and Node.js since July 2015. This bitwise operation has been standardized in the ECMAScript Language Specification and is available across various devices and platforms, with no known compatibility issues reported for the supported versions.

The operator works consistently across different numeric ranges and types. When applied to 32-bit integers, only the most significant 32 bits are considered, with any additional bits beyond this range being discarded. This ensures that the operation maintains consistent behavior regardless of the input number's original bit length.

For numbers outside the standard 32-bit integer range (-2147483648 to 2147483647), the right shift operation automatically truncates the value to fit within this range. Specifically, attempting to right shift a number by 0 bits results in the value being converted to a 32-bit integer, effectively removing any leading bits that do not fit within this size constraint.

The implementation details of the right shift operation involve multiple steps to ensure proper evaluation and conversion of the operands. First, both operands are converted to their respective integer types - the left operand becomes a 32-bit integer, while the right operand is converted to an unsigned 32-bit integer. The right operand undergoes a modulo 32 operation to ensure the shift amount is within the valid range of 0 to 31 bits.

The actual shift operation then occurs, with the left operand's bits being shifted to the right by the computed shift amount. For positive numbers, the most significant bit remains unchanged, preserving the original value's magnitude. In the case of negative numbers, the most significant bit is replicated to fill the vacated positions, maintaining the number's negative value through sign propagation.


## Operator Precedence and Usage

The right shift operator (>>) in JavaScript operates according to specific precedence rules that determine its evaluation order within expressions. Understanding these rules is crucial for predictable and precise computation.


### Precedence Rules

JavaScript operators fall into two categories: those with side effects (like assignment) and those that purely evaluate expressions. The right shift operator, along with most other bitwise and arithmetic operators, falls into the evaluation category.

The default precedence rule for operators is as follows:

- Multiplication (`*`) and division (`/`) have higher precedence than addition (`+`) and subtraction (`-`).

- The right shift operator (>>) has lower precedence than these arithmetic operations.


### Controlling Precedence with Parentheses

To ensure the right shift operator is evaluated in the desired order, developers can use parentheses to group expressions. For example:

```javascript

let result = 4 + 2 * (3 >> 1);

// This expression first evaluates (3 >> 1), then multiplies by 2, and finally adds 4

```

Without parentheses, the expression would be evaluated as:

```javascript

let result = 4 + ((2 * 3) >> 1);

// This would incorrectly shift the result of 6 (2 * 3) to the right by 1

```


### Safe Access with Optional Chaining

When dealing with potentially null or undefined objects, JavaScript provides the optional chaining operator (`?.`), which allows safe access to properties. However, this operator does not affect the evaluation order of bitwise operations unless used in conjunction with grouping operators.


### Practical Example

Consider the following function that calculates the nth power of 2 using right shift:

```javascript

function powOfTwo(n) {

  return 2 >> (32 - n);

}

```

This function works by shifting the value of 2 to the right by 32 - n positions. By controlling the order of operations with parentheses, it effectively calculates 2^(- (32 - n)), which is equivalent to 2^n.


### Final Considerations

While the right shift operator follows standard precedence rules, developers should be mindful of its behavior with negative numbers and large integer values. Always use parentheses when combining shift operations with other arithmetic operations to ensure consistent and predictable results.


## Right Shift Assignment Operator

The right shift assignment operator (>>=) combines the right shift operation with assignment, providing a concise way to perform in-place shifting. This operation is particularly useful for bitwise manipulation and can significantly simplify code by reducing the number of statements needed to shift values.


### Basic Usage and Functionality

The right shift assignment operator works by shifting the bits of the left operand to the right by the number of positions specified in the right operand and then assigning the result back to the left operand. This combination of operation and assignment is achieved through the syntax `x >>= y`, which is equivalent to `x = x >> y` but evaluated only once.


### Behavior with Positive and Negative Numbers

The operator behaves consistently with both positive and negative numbers by preserving the sign through sign propagation. For positive numbers, each right shift operation effectively divides the number by two, as demonstrated in the provided example where 5 right-shifted by 2 positions results in 1. Negative numbers also maintain their sign through the replication of the most significant bit during the shift process, as shown when -5 right-shifted by 2 positions results in -2.


### Compatibility and Support

The right shift assignment operator has been supported across browsers since July 2015, making it available in modern JavaScript environments including browsers and Node.js. This operator works consistently across different numeric ranges and types, maintaining proper behavior for both 32-bit integers and BigInt values.


### Implementation Details

When using the right shift assignment operator, both operands are converted to unsigned 32-bit integers. The right operand undergoes a modulo 32 operation to ensure the shift amount falls within the valid range of 0 to 31 bits. This conversion process ensures that the operation maintains consistent behavior across various numeric representations and bit lengths, providing reliable results for developers using different number types in their JavaScript code.

