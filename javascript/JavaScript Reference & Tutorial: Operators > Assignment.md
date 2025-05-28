---

title: JavaScript Assignment Operators

date: 2025-05-27

---


# JavaScript Assignment Operators

The JavaScript assignment operator forms the foundation of variable manipulation in the language. From basic assignment to advanced bitwise operations, this article explores the nuances of JavaScript's assignment mechanisms. You'll learn how to assign values efficiently, manipulate binary data with bitwise operators, and handle truthy/falsy values with logical assignment. Understanding these concepts will help you write more concise, performant, and robust JavaScript code.


## Basic Assignment Operator

The basic assignment operator (=) assigns a value to a variable. This can be used for simple variable assignment or assignment chaining, where a single value can be assigned to multiple variables.


### Simple Assignment Example

```javascript

let a = 2;

const b = 3;

console.log(a); // 2

console.log(a = b + 1); // 4

```


### Chain Assignment

```javascript

const x = y = 5;

// Equivalent to

const x = (y = 5)

```

The assignment operator requires both operands to be valid assignment targets: an identifier, property accessor, or destructuring pattern. It evaluates the expression on the right side before assigning the value to the left side.


### Chaining Assignments

Chaining allows multiple variables to be assigned the same value in a single statement:

```javascript

let x = y = 5;

// x and y both become 5

```

Variables can store various data types, including strings, numbers, and booleans:

```javascript

let myStr = "Hello";

let myNum = 10;

let myBool = true;

```


### Operator Precedence

The assignment operator has a precedence of 2, meaning it binds more loosely than bitwise and logical operators but more tightly than arithmetic operators. This affects how expressions are evaluated:

```javascript

let x = 1;

let a = x && (x = 0); // a is 1, x is 0

```


### Undefined Behavior

Assigning to undefined properties results in a ReferenceError:

```javascript

(x = 2) // Sets x to 2

((false ? 1 : x) = 2) // Throws ReferenceError

```


### Variable Declaration Interaction

Assignment operators can interact with variable declarations:

```javascript

let a = 1;

let b = 2;

let c = 3 - (a = b + 1); // c is 0, a is 3

```


## Compound Assignment Operators

Compound assignment operators combine arithmetic or logical operations with variable assignment, simplifying expressions and reducing the need for intermediate variables. These operators include +=, -=, *=, /=, %=, and **=, each performing a specific operation before assigning the result back to the original variable.


### Addition Assignment (+=)

The addition assignment operator adds the value of the right operand to the variable on the left, then assigns the result back to the left variable. For example:

```javascript

let a = 2;

const b = 3;

console.log(a); // 2

console.log(a += b); // 5

```


### Subtraction Assignment (-=)

The subtraction assignment operator subtracts the right operand from the left and assigns the result back. For instance:

```javascript

let a = 5;

a -= 2; // a becomes 3

```


### Multiplication Assignment (*=)

This operator multiplies the variable by the right operand and assigns the product back:

```javascript

let a = 2;

a *= 3; // a becomes 6

```


### Division Assignment (/=)

Division assignment divides the variable by the right operand and assigns the quotient:

```javascript

let a = 10;

a /= 2; // a becomes 5

```


### Remainder Assignment (%=)

The remainder assignment operator calculates the remainder of dividing the variable by the right operand and assigns it back:

```javascript

let a = 7;

a %= 3; // a becomes 1

```


### Exponentiation Assignment (**=)

This operator raises the variable to the power of the right operand and assigns the result back:

```javascript

let a = 2;

a **= 3; // a becomes 8

```


### Operator Precedence

Like other arithmetic operators, these compound assignment operations follow the standard precedence rules. For example, in the expression `let a = 2 * 3 + 1;`, multiplication is performed first, resulting in `a` being 7. When using compound operators, the operation is performed before the assignment, as demonstrated in the example `let a = 2 * 3 + 1;` which is equivalent to `let a = (2 * 3) + 1;`.


## Bitwise Assignment Operators

The bitwise assignment operators perform logical operations on bits before assigning the result back to the variable. These operators include &=, |=, ^=, <<=, >>=, and >>>=, each performing a specific operation on the binary representation of the variable.


### Bitwise AND Assignment

The & operator compares each bit of the first operand to the corresponding bit of the second, producing a new value where each bit is set to 1 if both corresponding bits of the operands are 1, otherwise 0. The &= operator applies this operation and assigns the result back to the variable. For example:

```javascript

let x = 15; // Binary: 1111

x &= 9;     // Binary: 1001

console.log(x); // 9

```


### Bitwise OR Assignment

The | operator compares each bit of the first operand to the corresponding bit of the second, producing a new value where each bit is set to 1 if at least one corresponding bit of the operands is 1. The |= operator performs this operation and assigns the result back to the variable:

```javascript

let x = 15; // Binary: 1111

x |= 9;     // Binary: 1001

console.log(x); // 15

```


### Bitwise XOR Assignment

The ^ operator compares each bit of the first operand to the corresponding bit of the second, producing a new value where each bit is set to 1 if the corresponding bits of the operands are different. The ^= operator performs this operation and assigns the result back to the variable:

```javascript

let x = 15; // Binary: 1111

x ^= 9;     // Binary: 1001

console.log(x); // 6

```


### Left Shift Assignment

The << operator shifts the bits of the first operand to the left by the number of positions specified by the second operand, discarding excess bits and filling with zeros from the right. The <<= operator performs this operation and assigns the result back to the variable:

```javascript

let x = 7; // Binary: 0111

x <<= 2;   // Binary: 11100

console.log(x); // 28

```


### Right Shift Assignment

The >> operator shifts the bits of the first operand to the right by the number of positions specified by the second operand, copying the sign bit (leftmost bit) to fill in from the left. The >>= operator performs this operation and assigns the result back to the variable:

```javascript

let x = 7; // Binary: 0111

x >>= 1;   // Binary: 0011

console.log(x); // 3

```


### Unsigned Right Shift Assignment

The >>> operator shifts the bits of the first operand to the right by the number of positions specified by the second operand, discarding excess bits and filling with zeros from the left. This operation treats the operand as an unsigned number, so the sign bit is not preserved. The >>>= operator performs this operation and assigns the result back to the variable:

```javascript

let x = 7; // Binary: 0111

x >>>= 2;  // Binary: 000111

console.log(x); // 3

```


### Operator Precedence

All bitwise assignment operators follow the standard precedence rules, operating on 32-bit integers. The left-to-right evaluation order of these operators ensures that expressions are evaluated correctly:

```javascript

let x = 10;

x >>= 1; // x becomes 5

x &= 3;  // x becomes 1

```

These operators provide a powerful way to manipulate binary data directly within JavaScript, enabling low-level programming techniques and efficient bit-level operations.


## Logical Assignment Operators


### Logical AND Assignment (&&=)

The logical AND assignment operator (`&&=`) evaluates the right operand and assigns to the left if the left operand is truthy. It short-circuits the evaluation process, meaning that `x &&= y` is equivalent to `x && (x = y)`, with the left-hand side expression (`x`) only evaluated once.

No assignment occurs if the left-hand side is already not truthy, thanks to the short-circuiting behavior of the logical AND operator. Similarly to other ES2020 features, this operator works seamlessly with `const` variables and does not trigger setters when the left-hand side remains unchanged.


### Logical OR Assignment (||=)

The logical OR assignment operator (`||=`) works in the opposite manner. If the left operand is falsy, it performs the assignment using the right operand. The evaluation process also short-circuits, meaning that once a truthy value is found, subsequent expressions are ignored.

This operator provides a convenient way to safely assign values to variables, especially when dealing with optional properties or function return values. For example, when defining widget functionality in a JavaScript context, you might use this operator to ensure that if the widget is not defined, it will use a default implementation:

```javascript

this.myWidget = this.myWidget || (function() { // define widget })();

```

By understanding the nuances of these operators, developers can write more efficient and concise JavaScript code that handles various truthy and falsy values appropriately.


## Assignment Operator Precedence

Operator precedence determines the order in which different operators are evaluated in a complex expression. Arithmetic operators have higher precedence than assignment operators, meaning they're evaluated first. For example, in the expression `let result = 3 + 4 * 2;`, the multiplication (`*`) operator has higher precedence than the addition (`+`) operator. Therefore, the multiplication is performed first, followed by the addition: `let result = 3 + (4 * 2); let result = 3 + 8; let result = 11;`

Operators with the same precedence level are evaluated in a specific order based on their associativity:

- Operators that evaluate from left to right (Left Associativity) process their operands sequentially from left to right.

- Operators that evaluate from right to left (Right Associativity) process their operands sequentially from right to left.

The assignment operator (`=`) has right-to-left associativity. This affects expressions where multiple assignments are combined, such as `a = b = c;`. Here, the assignments are evaluated from right to left: `b = c;` (b becomes 3) and then `a = b;` (a becomes 3). As a result, after these assignments, all variables a, b, and c are set to 3.


### Operator Precedence Table

A deeper look at the operator precedence hierarchy shows that operators are grouped into eight categories, each with distinct evaluation rules:

1. Postfix++ / Postfix-- (First, Right-to-Left)

2. Unary !, - (First, Right-to-Left)

3. Multiplication *, Division /, Modulus % (Second, Left-to-Right)

4. Addition +, Subtraction - (Third, Left-to-Right)

5. Left-hand side of assignment = (Eighth, Right-to-Left)

6. Arithmetic Assignment +=, -=, *=, /=, %= (Eighth, Right-to-Left)

7. Exponentiation ** (First, Right-to-Left)

8. Conditional ? : (Seventh, Right-to-Left)

Understanding these rules helps developers write correct and efficient expressions. For example, when dealing with complex calculations like `3 + 5 * 2`, the multiplication is performed first due to its higher precedence: `3 + (5 * 2)` evaluates to 11. Proper operator placement and precedence knowledge ensures expressions behave as intended, especially in complex calculations and conditionals.

