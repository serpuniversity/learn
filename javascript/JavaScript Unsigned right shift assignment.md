---

title: JavaScript's Unsigned Right Shift Assignment Operator (>>=)

date: 2025-05-27

---


# JavaScript's Unsigned Right Shift Assignment Operator (>>=)

JavaScript's unsigned right shift assignment operator (>>=) provides developers with a powerful tool for manipulating numeric values through bitwise operations. While similar in syntax to other shift operators, this particular operation introduces distinct behavior when handling negative numbers, making it essential for developers working with bitwise logic. Understanding the nuances of the >>= operator is crucial for implementing correct bitwise operations in JavaScript, as its implementation is defined by the ECMAScript specification and consistently supported across major platforms.


## Basic Usage and Behavior

The unsigned right shift assignment operator (>>=) performs a right shift operation on the value of a variable by the number of bits specified in an expression. Unlike the signed right shift operator, it fills the new positions with zeroes rather than maintaining the sign of the value.

The basic operation of the operator can be broken down into these steps:

1. The variable's value is shifted right by the specified number of bits.

2. The rightmost bits are discarded.

3. Zeroes are inserted into the empty positions on the left.

4. The resulting value is assigned back to the original variable.

For positive numbers, the behavior of unsigned right shift is relatively straightforward:

- Shifting the binary representation of 4 (0100) right by 2 positions yields 1 (0001).

However, for negative numbers, the operator produces a positive result through the zero-filling process:

- Shifting -14 (binary: 
11111100) right by 2 positions results in 1073741820 (binary: 
100000110110000000000000).

The operator's implementation details are consistent across JavaScript environments, with the ECMAScript specification providing the formal definition and behavior expectations. All major browsers and platforms support the operator, though specific implementation versions may vary.


## Syntax and Example Code

The syntax for the unsigned right shift assignment operator (>>=) follows the pattern: result >>>= expression. This operation is functionally equivalent to result = result >>> expression, where result is any variable and expression is any expression.

The operator performs a bitwise right shift operation on the value of the variable by the number of bits specified in the expression. The shifted value is then assigned back to the original variable, making it particularly useful for modifying numeric values while preserving their structure.

For example, consider the following code snippet:

let a = 16

let b = 2

console.log(`${a}>>>=${b} is ${a >>>= b}`)

This will output: 16>>>=2 is 4

The operation can be demonstrated with various numeric values, as shown below:

let a = 6

let b = 3

c = a >>> b

console.log(`${a}>>>${b} is ${c}`)

console.log(`${15}>>>${2} is ${15 >>> 2}`)

console.log(`${10}>>>${1} is ${10 >>> 1}`)

The output will be:

6>>>3 is 0

15>>>2 is 3

10>>>1 is 5

The operator works consistently across all major JavaScript environments, with implementation details defined in the ECMAScript specification. It has been available across browsers since July 2015 and maintains compatibility with both standard and BigInt numeric types, with appropriate behavior for each.


## How It Differs from Signed Right Shift

The unsigned right shift (>>>) operator behaves distinctly from its signed counterpart (>>) in several key ways. While both operators shift the bits of a number's binary representation, the unsigned right shift fills the empty positions with zeros regardless of the original sign, always producing a positive result (or zero for zero-value inputs). This fundamental difference arises from how each operator handles negative inputs.

When both operands are positive, the two operators produce identical results. For example, shifting the positive number 9 right by 2 positions yields 2 in both cases (9 >>> 2 === 2 and 9 >> 2 === 2). However, when negative inputs are involved, the operators produce distinct results. Shifting -9 right by 2 positions using the signed right shift operator results in -3 (which is interpreted as 11111111111111111111111111111101 in binary, maintaining the sign). In contrast, the unsigned right shift operator produces a positive result, yielding 1073741821 (binary: 
100000110110000000000000), effectively discarding the sign information.

This behavior is particularly important for developers working with bitwise operations, where the distinction between signed and unsigned values can significantly impact the expected output. Understanding the implications of using >>> versus >> is crucial for correct implementation of bitwise logic in JavaScript.


## Examples of Usage

Examples demonstrating the behavior of the unsigned right shift assignment operator are as follows:

Positive numbers are shifted as expected, preserving their positive nature:

```javascript

let a = 9

a >>>= 2

console.log(a) // Output: 2

```

This operation shifts the binary representation of 9 (00000000000000000000000000001001) right by two positions, resulting in 2 (00000000000000000000000000000010).

Negative numbers transform into positive results through the zero-filling process:

```javascript

let b = -14

b >>>= 2

console.log(b) // Output: 1073741820

```

Starting from -14 (11111111111111111111111111110110 in two's complement), the operator shifts the bits right by two positions, resulting in 1073741820 (100000110110000000000000 in binary).

This behavior is further illustrated with multiple values:

```javascript

let c = -16

c >>>= 4

console.log(c) // Output: 1073741824

let d = 6

d >>>= 3

console.log(d) // Output: 0

```

The operator's behavior with BigInts demonstrates its handling of numbers with more significant bits:

```javascript

let e = 9n

e >>>= 2n

console.log(e) // Output: 2n

let f = -9n

f >>>= 2n

console.log(f) // Output: 1073741821n

```

These examples illustrate the operator's consistent behavior across different numeric types and values, maintaining the documented zero-filling process for negative inputs while performing standard bit shifting for positive values.


## Browser Support and Specifications

The operator has been available across browsers since July 2015, with consistent support across all major platforms. The operator works by performing the shift operation on the value of the left operand by the number of bits specified in the right operand, then assigning the result back to the left operand.

The operator is defined by the ECMAScript specification (ECMA-262) and has been implemented across all supported environments, including desktop browsers, mobile devices, and Node.js. The compatibility data shows full support across Chrome, Edge, Firefox, Internet Explorer, Opera, and Safari, with compatibility extending back to version 1 of most browsers.

The operator's implementation follows the syntax x >>= y, which is equivalent to x = x >> y. The expression on the left side is evaluated only once, making it particularly efficient for repeated operations. This behavior differs from some other operators that may require multiple evaluations of their left-hand operands.

For developers working with different numeric types, the operator handles BigInt values consistently while maintaining compatibility with standard numbers. The behavior is defined by the specification and has been implemented across all supported environments, allowing developers to use the operator with confidence in their JavaScript applications.

