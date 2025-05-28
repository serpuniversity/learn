---

title: JavaScript Bitwise AND Assignment Operator

date: 2025-05-27

---


# JavaScript Bitwise AND Assignment Operator

In JavaScript, the bitwise AND assignment operator provides a powerful tool for manipulating integer values at the bit level. This operator, represented by &=, efficiently combines a comparison of binary digits with an immediate assignment of the result back to the original variable. Understanding its behavior and implementation details is crucial for developers working with low-level numerical operations or specialized data representations. This article explores the technical aspects of the bitwise AND assignment, from its syntax and implementation to its role in modern JavaScript development.


## Overview of Bitwise AND Assignment

The bitwise AND assignment operator (x &= y) performs a bitwise AND operation on two operands and assigns the result back to the left operand (x). This operation works with both standard integers and bigint values, providing consistent behavior across JavaScript implementations.


### Operator Implementation

The operator implementation follows the general pattern of `x = x & y`. However, the key difference is that both operands are evaluated only once. This means that if the left operand is not a simple variable but a more complex expression, this single evaluation can improve performance compared to evaluating the expression twice with a regular assignment.


### Example Usage

The operator works as follows in practice:

```javascript

let a = 5; // Binary: 00000000000000000000000000000101

a &= 2; // Binary: 00000000000000000000000000000010

console.log(a); // Output: 0

```

For bigint values, the behavior is similar:

```javascript

let b = 5n; b &= 2n;

console.log(b); // Output: 0n

```

These examples demonstrate how the operator updates the value of the left operand based on the bitwise AND operation with the right operand.


### Browser and Specification Support

The bitwise AND assignment operator has been available across browsers since July 2015. It is formally specified in the ECMAScript 2026 Language Specification, Section 11.14.3, ensuring consistent behavior across JavaScript implementations.


## Operator Syntax and Usage

The bitwise AND assignment (&=) operator performs a bitwise AND operation on both operands and assigns the result to the left operand. This operation works with both regular integers and bigint values, providing consistent behavior across JavaScript implementations.

The syntax for the operator is straightforward: a &= b, where a is the left operand and b is the right operand. The operator implementation follows the pattern a = a & b, but with the key difference that both operands are evaluated only once. This single evaluation can improve performance compared to evaluating the expression twice with a regular assignment.

The bitwise AND operation works by comparing each pair of bits from the two operands. If both corresponding bits are 1, the result has a 1 in that position; otherwise, the result has a 0. For example, considering the binary representations of 15 (1111) and 9 (1001):

- 15 & 9 results in 9 (1001).

This operation effectively masks off any bits in the left operand that are not present in the right operand's corresponding position. For instance, when working with values that can only be represented within 10 bits, applying the operation with 1023 (1111111111) ensures the result remains within this 10-bit range.

The operator works consistently across modern JavaScript implementations, with compatibility dating back to July 2015. It forms part of the ECMAScript 2026 Language Specification, Section 11.14.3, ensuring consistent behavior across all compliant implementations.


## Bitwise Operation Details

The bitwise AND operation compares each pair of bits from two operands. It returns a one in each bit position for which both operands have ones, and zero otherwise. For example, for the binary representations of 12 (01100) and 25 (11001), the result of 15 & 9 is 9 (00001001).

The operator treats its operands as 32-bit binary digits, performing operations on these binary representations and returning standard JavaScript numerical values. When applied to numbers with more than 32 bits, the most significant bits are discarded, and the operation is performed on the remaining 32 bits.

The operator works consistently across modern JavaScript implementations, with compatibility dating back to July 2015. It forms part of the ECMAScript 2026 Language Specification, Section 11.14.3, ensuring consistent behavior across all compliant implementations.

For negative numbers, JavaScript represents them using the two's complement method in memory. The bitwise AND operation can be used to mask values, effectively treating the operands as if they were within a specific range. For example, applying the operation with 1023 (1111111111) ensures the result remains within a 10-bit range, as documented in the ECMAScript specification.


## Example Usage

The bitwise AND assignment operator works consistently across modern JavaScript implementations, with compatibility dating back to July 2015. It forms part of the ECMAScript 2026 Language Specification, Section 11.14.3, ensuring consistent behavior across all compliant implementations.

For standard integers, the operator treats its operands as 32-bit binary digits. When applied between 12 (01100) and 25 (11001), the result of 12 & 25 is 0, demonstrating how the operator returns 0 when no corresponding bits are 1 in the same position.

The operator works similarly for bigint values. When applied between 5n and 2n, the result is 0n, matching the behavior for standard integers.

The operator effectively masks values by performing bitwise AND with specific numbers. For instance, applying the operation with 1023 (1111111111) ensures the result remains within a 10-bit range, effectively limiting values from -2147483648 to 2147483647. This functionality allows for efficient "wrapping" of values between 0 and 1023, as demonstrated in examples where a variable is incremented and then bitwise ANDed with 1023.

When working with negative numbers, JavaScript uses the two's complement method for representation. The operator correctly handles these cases, operating on the binary representations and returning standard JavaScript numerical values or BigInts as appropriate. For example, the operation maintains correct results when applied to values like -2147483648 and 2147483647, demonstrating its compatibility with the full range of representable JavaScript numbers.


## Browser Support and Specifications

The bitwise AND assignment (`&=`) operator performs bitwise AND on two operands and assigns the result to the left operand. It works consistently across modern JavaScript implementations, with compatibility dating back to July 2015. The operator is defined in the ECMAScript 2026 Language Specification, specifically section 11.14.3.


### Operator Behavior and Precedence

The operator behaves as `x = x & y`, but with the key difference that both operands are evaluated only once. This single evaluation can improve performance compared to evaluating the expression twice with a regular assignment. In terms of operator precedence, bitwise operations generally have higher precedence than arithmetic operations, following the standard order of operations in JavaScript.


### Operand Handling and Data Types

The operator works with both standard integers and bigint values. The engine handles any other operand types by casting them to either 32-bit integers or bigint. For values exceeding 32-bit limits, the engine calculates modulo 2^32 to manage overflow. This means that when working with numbers outside the 32-bit range, bitwise operations will wrap around using modulo arithmetic.


### Common Use Cases

Bitwise operations enable advanced algorithms, particularly in areas like cryptography and efficient integer representation of multiple Boolean variables through bitmasking. In JavaScript, these operations are less common than in languages like C, but they remain useful in specific scenarios.

For example, bitmasking allows representing multiple Boolean statuses using a single integer. In JavaScript, this often results in more intuitive, less error-prone code compared to traditional object representation. The Node.compareDocumentPosition function returns a bitmask that requires bitwise operations to interpret correctly. Understanding the underlying bitwise operations is crucial for correctly interpreting these values.

