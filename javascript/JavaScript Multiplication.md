---

title: Multiplication in JavaScript

date: 2025-05-27

---


# Multiplication in JavaScript

Multiplication is a fundamental operation in programming, enabling developers to perform arithmetic calculations efficiently. In JavaScript, the multiplication operator provides a straightforward way to multiply numbers, but it also introduces complexities when dealing with different numeric types and special values. This article explores JavaScript's multiplication capabilities, from basic arithmetic to its behavior with numbers, BigInts, and special values like Infinity and NaN.


## JavaScript Multiplication Operator

The multiplication operator in JavaScript, represented by the asterisk (*), functions by taking two operands and returning their product. Both operands must be numbers or convertible to numbers; otherwise, a TypeError will be thrown when attempting to mix types such as BigInt with number.

The operator follows standard arithmetic precedence, operating after parentheses and before addition and subtraction. When used in expressions, it processes from left to right as per JavaScript's arithmetic evaluation rules.


### Handling of Numbers and BigInts

When both operands are numbers, JavaScript performs straightforward multiplication. However, when one or both operands are BigInts, the multiplication operator handles these specifically. If both operands become BigInts during evaluation, the operation results in a BigInt. If one operand becomes a BigInt and the other a number, a TypeError is thrown unless explicit type conversion occurs.

For instance, `2n * 2n` correctly returns `4n`, demonstrating BigInt multiplication. Attempting to multiply a BigInt with a number directly results in a TypeError: `2n * 2` throws an error, requiring explicit conversion: either using `2n * BigInt(2)` or `Number(2n) * 2`.


### Edge Cases and Operator Behavior

The operator correctly handles multiplication with Infinity, returning Infinity when either operand is Infinity and the other is a finite number. However, multiplying Infinity by 0 results in NaN, demonstrating the operator's ability to return special numeric values when appropriate.

The multiplication operator supports standard JavaScript arithmetic assignments with its *= counterpart, making it versatile for both simple calculations and more complex mathematical operations in the language.


## Multiplication Methods

JavaScript supports multiple methods for performing multiplication, offering developers flexibility in how they approach numerical calculations. The language's multiplication operator, represented by the asterisk (*), performs straightforward arithmetic on numeric operands. Additionally, developers can create custom functions or employ arrow functions to implement multiplication logic.


### Custom Function Implementation

Developers can implement multiplication using basic functions, where the function accepts two parameters and returns their product. For example:

```javascript

function multiply(a, b) {

  return a * b;

}

console.log(multiply(3, 5)); // Output: 15

```

Arrow functions provide a concise alternative for defining multiplication logic:

```javascript

const multiply = (a, b) => a * b;

console.log(multiply(3, 5)); // Output: 15

```


### String-Based Multiplication Method

A clever string-based approach demonstrates how JavaScript's .repeat() method can be used to multiply numbers. This method creates a string consisting of a single character "i", repeats this string a times, and then repeats the resulting string b times. The length of the final string represents the product of a and b:

```javascript

const multiply = (a, b) => {

  return ("i").repeat(a).repeat(b).length;

}

console.log(multiply(3, 5)); // Output: 15

```

This string-based approach, while creative, is noted for its slower performance compared to traditional multiplication methods.


## Multiplication with Numeric Types

JavaScript's multiplication operator (*) takes two operands and returns their product. Both operands must be numbers or convertible to numbers; otherwise, a TypeError will be thrown when attempting to mix types, as demonstrated by the following example:

```javascript

console.log(2n * 2); // Throws TypeError: Cannot mix BigInt and other types, use explicit conversions

console.log(Number(2n) * 2); // 4

```

The operator correctly handles different numeric types:

- For integers and floating-point numbers, both fall under JavaScript's unified Number data type.

- When both operands are numbers, straightforward multiplication occurs.

- If one or both operands are BigInts, the operator handles these specifically:

  - If both become BigInts, the operation results in a BigInt.

  - If one becomes a BigInt and the other a number, a TypeError is thrown unless explicit type conversion occurs.

```javascript

console.log(2n * 2n); // 4n

console.log(NaN * 100); // NaN

console.log(Infinity * 0); // Infinity

console.log("hello" * 20); // NaN

console.log("100" * 100); // 10000

```

The * operator performs arithmetic coercion for the operands, converting them to numeric values before multiplication. This means that even if the operands are not initially numbers, they will be converted for the operation. For example:

```javascript

console.log("100" * 100); // 10000

console.log("100" * "200"); // 20000

```

In these cases, the string operands are converted to numbers before the multiplication takes place. If both operands are strings that represent numbers, they are also converted to numbers:

```javascript

console.log("10.5" * 2); // 21

console.log(10.5 * "2"); // 21

console.log(10 * "2.5"); // 25

```

When both operands are strings that cannot be converted to numbers, the result is NaN (Not-a-Number):

```javascript

console.log("hello" * 20); // NaN

console.log("100" * "hello"); // NaN

```

JavaScript automatically handles the distinction between integers and floating-point numbers without requiring explicit declaration types. The multiplication operator works across various numeric values, returning appropriate results based on the nature of the operands.


## Multiplication with Strings

When applied to strings, JavaScript's multiplication operator functions through string concatenation, repeating the string a number of times specified by the second operand. This operator combines its two numerical operands into a single value by appending copies of the first operand to itself based on the second operand's integer value.

The operator creates an empty string and repeats a specified character the number of times defined by the second operand. It then concatenates this string the number of times defined by the first operand, effectively creating a new string equal to the original character repeated multiple times. The final step measures this constructed string's length, which directly corresponds to the mathematical product of the two operands.

For example, evaluating `"hello" * 3` results in a string of length 15, since "hello" is repeated three times ("hellohellohello"). This string construction approach leverages JavaScript's existing string manipulation methods to provide a unique interpretation of multiplication when applied to textual data.


## Special Cases and Considerations


### Handling with Mathematical Constants and Functions

The language provides a full-featured set of math functions through the Math object, including basic methods like Math.random(), Math.floor(), and Math.ceil(). These functions enable complex mathematical operations alongside simple multiplication. For instance:

```javascript

console.log(Math.random() * 100); // Generates random number between 0 and 100

console.log(Math.floor(10.9)); // Rounds down to 10

console.log(Math.ceil(10.1)); // Rounds up to 11

```


### Special Cases and Edge Conditions

The multiplication operator processes several special cases and edge conditions:

- **Infinity Handling**: The operator correctly handles multiplication involving Infinity, returning Infinity when one operand is Infinity and the other is a finite number. However, multiplying Infinity by 0 results in NaN:

  ```javascript

  console.log(Infinity * 100); // Infinity

  console.log(Infinity * 0); // NaN

  ```

- **NaN Values**: When either operand is NaN, the result is always NaN:

  ```javascript

  console.log(NaN * 100); // NaN

  console.log(100 * NaN); // NaN

  ```

- **Large Integers**: JavaScript uses the Number type for all numbers, including integers and floating-point numbers. For very large integers, the language employs the BigInt type, which requires explicit conversion between number and BigInt types:

  ```javascript

  console.log(2n * 2n); // 4n

  console.log(Number(2n) * 2); // 4

  console.log(2n * BigInt(2)); // 4n

  ```

- **Type Conversion**: The operator performs automatic type conversion for operands, allowing operations between different numeric types:

  ```javascript

  console.log("100" * 100); // 10000

  console.log(10 * "2.5"); // 25

  console.log("hello" * 20); // NaN

  ```

These special cases and edge conditions demonstrate JavaScript's comprehensive approach to handling mathematical operations, making the language robust for both simple and complex calculations.

