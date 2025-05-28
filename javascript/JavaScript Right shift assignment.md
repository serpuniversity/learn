---

title: JavaScript Right Shift Assignment Operator

date: 2025-05-27

---


# JavaScript Right Shift Assignment Operator

The right shift assignment operator (>>=) is a fundamental bitwise operation in JavaScript, combining bit manipulation with value assignment. This article explores the operator's behavior with both numbers and BigInts, demonstrating how it maintains the sign of variables while shifting bits. Through various examples and comparison with related operators, we'll examine its consistent behavior across different operand types and explore best practices for its use in JavaScript development.


## Right Shift Assignment Operator (>>=)

The right shift assignment operator (>>=) performs a bitwise right shift operation on its left operand by the number of positions specified in the right operand. This operation maintains the sign of the variable by using the sign bit to fill the vacated positions on the left, while bits shifted off the right end are discarded.


### Operator Behavior with Positive and Negative Numbers

When applied to positive numbers, the right shift operator effectively divides the number by two for each shift position, truncating any fractional part. For negative numbers, the operator performs a sign-preserving shift, ensuring the result maintains the same sign as the original value through the sign bit.


### Example Operations

To illustrate, consider the following operations:

```javascript

let a = 14; // Binary: 00000000000000000000000000001110

a >>= 2; // Shift right by 2 positions

console.log(a); // Output: 3 (Binary: 
00000000000000000000000000000011)

let b = -14; // Binary: 11111111111111111111111111110010

b >>= 2; // Shift right by 2 positions

console.log(b); // Output: -3 (Binary: 
11111111111111111111111111111101)

```

The operator maintains consistent behavior across number and BigInt types, with no truncation applied to BigInts and infinite leading 0 or 1 bits for positive and negative values, respectively.


### Browser Support

Browser compatibility for the right shift assignment operator is extensive, supported since browser versions as early as 1997 in Internet Explorer 3, with complete modern support across all major browsers and Node.js environments.


## Examples and Usage

The right shift assignment operator (>>=) combines the right shift operation with value assignment in a single step. This operator shifts the bits of the left operand to the right by the number of positions specified by the right operand and then assigns the resulting value back to the left operand. The operation preserves the sign of the variable by using the sign bit to fill the vacated positions on the left, while bits shifted off the right end are discarded.

Here are several examples demonstrating the operator's behavior with both numbers and BigInts:

```javascript

let a = 9; // Binary: 00000000000000000000000000001001

a >>= 2;   // Shift right by 2 positions

console.log(a); // Output: 2 (Binary: 
00000000000000000000000000000010)

let b = -9; // Binary: 11111111111111111111111111111011

b >>= 2;    // Shift right by 2 positions

console.log(b); // Output: -3 (Binary: 
11111111111111111111111111111101)

```

The operator maintains consistent behavior across different operand types. For example:

```javascript

let c = 14; // Binary: 00000000000000000000000000001110

c >>= 2;    // Shift right by 2 positions

console.log(c); // Output: 3 (Binary: 
00000000000000000000000000000011)

let d = -14; // Binary: 11111111111111111111111111110010

d >>= 2;     // Shift right by 2 positions

console.log(d); // Output: -3 (Binary: 
11111111111111111111111111111101)

```

The operator also handles positive numbers correctly:

```javascript

let e = 8; // Binary: 00000000000000000000000000001000

e >>= 3;   // Shift right by 3 positions

console.log(e); // Output: 1 (Binary: 
00000000000000000000000000000001)

```

BigInt examples demonstrate consistent behavior:

```javascript

let f = 9n; // Binary: 00000000000000000000000000001001

f >>= 2n;   // Shift right by 2 positions

console.log(f); // Output: 2n (Binary: 
00000000000000000000000000000010)

let g = -9n; // Binary: 11111111111111111111111111111011

g >>= 2n;    // Shift right by 2 positions

console.log(g); // Output: -3n (Binary: 
11111111111111111111111111111101)

```

These examples show that the right shift assignment operator consistently preserves the sign of the value while correctly shifting the bits as specified.


## Browser Support

The right shift assignment operator (>>=) demonstrates consistent and widespread compatibility across JavaScript environments. As detailed in the browser compatibility specifications, the operator is supported in all major desktop browsers including Chrome, Edge, Firefox, Internet Explorer, Opera, and Safari, with support dating back to the initial release of JavaScript in 1997. This foundational support extends to mobile platforms through webview and specific apps, with notable versions beginning from Android webview 1 and Opera Android 10.1.

The operator's functionality aligns with the ECMAScript 262 specification, ensuring consistency across both desktop and Node.js environments. For example, as demonstrated in the documentation, 9 >> 2 yields 2, while -9 >> 2 yields -3, consistently handling both positive and negative integers. The behavior is equally robust with BigInt values, as seen in the example where 9n >> 2n produces 2n.

All documented implementations adhere to the operator's fundamental behavior of shifting bits to the right while preserving the sign through the sign bit, with excess rightmost bits being discarded and vacant leftmost positions filled accordingly. The operator's syntax and functionality have not changed since the initial browser release, making it a reliable choice for bitwise operations in modern JavaScript applications.


## Comparison with Other Shift Operators

The right shift assignment operator (>>=) operates similarly to the bitwise right shift operator (>>) but with the added functionality of assigning the result back to the original variable. For both numbers and BigInts, the operator shifts the bits of the left operand to the right by the number of positions specified in the right operand, using the sign bit to fill vacated positions on the left and discarding bits shifted off the right end.

In contrast, the left shift assignment operator (<<=) shifts bits to the left, filling vacated positions on the right with zeros. The unsigned right shift assignment operator (>>>=) also shifts bits to the right but fills vacated positions with zeros regardless of the sign bit, providing distinct behaviors for positive and negative values.

To illustrate these differences, consider the following examples:

```javascript

let num1 = 5; // Binary: 00000000000000000000000000000101

num1 <<= 2;   // Left shift by 2 positions

console.log(num1); // Output: 20 (Binary: 
0000000000000000000000000010100)

let num2 = -5; // Binary: 11111111111111111111111111111011

num2 >>= 2;    // Sign-preserving right shift by 2 positions

console.log(num2); // Output: -3 (Binary: 
11111111111111111111111111111101)

let num3 = -5; // Binary: 11111111111111111111111111111011

num3 >>>= 2;   // Zero-fill right shift by 2 positions

console.log(num3); // Output: 1073741822 (Binary: 
01111111111111111111111111111110)

```


## Best Practices and Considerations

When using the right shift assignment operator (>>=), several best practices and considerations are important to keep in mind:


### Operator Precedence and Associativity

The operator has right-to-left associativity and follows standard operator precedence rules. This means that in expressions like `x >>= y >> z`, the shift operations are performed from right to left, making the expression equivalent to `x >>= (y >> z)`. Understanding operator precedence helps ensure correct expression evaluation.


### Comparison with Other Shift Operators

The right shift assignment operator behaves similarly to the bitwise right shift operator (>>) but with the added functionality of assignment. For both number and BigInt types, it shifts bits to the right, using the sign bit to fill vacated positions on the left and discarding bits shifted off the right end. In contrast, the left shift assignment operator (<<=) shifts bits to the left, while the unsigned right shift assignment operator (>>>=) fills vacated positions with zeros regardless of the sign bit.


### Interaction with Logical Operators

The right shift assignment operator can interact with logical operators in unexpected ways due to their different evaluation mechanisms. For example, while the logical AND assignment operator (&&=) assigns the right value only if the left value is truthy, the right shift assignment operator always performs the assignment regardless of the left value's truthiness. This difference in behavior can affect the outcome of combined operator expressions.


### Edge Cases and Potential Pitfalls

Care must be taken when using the right shift assignment operator with floating-point numbers, as JavaScript typically uses integers for bitwise operations. While the operator can handle floating-point values, the resulting integer approximation can lead to unexpected behavior. For example, `10.5 >>= 1` results in `5`, not `5.25`, due to JavaScript's rounding rules for bitwise operations.

BigInt values provide more reliable behavior for large integer arithmetic, but developers must ensure proper type handling to avoid unexpected results when mixing number and BigInt types in the same expression.

