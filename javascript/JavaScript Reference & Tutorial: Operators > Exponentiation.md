---

title: JavaScript Exponentiation Operator (**)

date: 2025-05-27

---


# JavaScript Exponentiation Operator (**)

The JavaScript exponentiation operator (`**`) introduced in ECMAScript 2016 simplifies working with powers, offering a more intuitive syntax than the `Math.pow()` method. Common to languages like Python and Ruby, this operator provides concise solutions for raising numbers and BigInt values to various powers while maintaining predictable behavior across different scenarios. Understanding its syntax, operator precedence, and handling of special cases is crucial for writing efficient and bug-free JavaScript code that correctly processes both standard numbers and the larger values supported by BigInt.


## Exponentiation Operator Syntax and Basic Usage

The exponentiation operator (`**`) was introduced in ECMAScript 2016 to make JavaScript's exponentiation syntax more consistent with other languages like Python, Ruby, and Perl. It provides a more concise alternative to the `Math.pow()` method, as demonstrated in the examples:

```javascript

// Basic usage

console.log(2 ** 3); // 8

console.log(3 ** 2); // 9

console.log(5 ** 3); // 125

console.log(10 ** 0); // 1

```

The operator follows specific precedence rules, evaluating higher than multiplication and division but lower than unary operators. This means in expressions like `a * b ** c`, the exponentiation would be evaluated before the multiplication.

When working with numbers and BigInt values, the operator demonstrates consistent behavior across different scenarios:

```javascript

// Number operations

console.log(2 ** -1); // 0.5

console.log(0 ** 3); // 0

console.log(0 ** -1); // Infinity

console.log((-0) ** -1); // -Infinity

console.log(NaN ** 3); // NaN

console.log(NaN ** 0); // 1

// BigInt operations

console.log(2n ** 1024); // Infinity

console.log(1n ** Infinity); // NaN

console.log(2n ** 2); // 4n

console.log(BigInt(2) ** 2n); // 4n

console.log("2n" ** 2); // NaN

```


## Operator Precedence and Associativity

The exponentiation operator follows specific rules for operator precedence and associativity that affect how expressions are evaluated. In the absence of parentheses, the operator has a precedence lower than multiplication and division but higher than unary operators. This means that in expressions containing both operations, the exponentiation will be evaluated first.

For example, `a * b ** c` calculates the exponentiation before the multiplication, resulting in `a * (b ** c)`. Similarly, when combining exponentiation with other operations, parentheses can override precedence to create grouped expressions. For instance, `(a + b) * c` and `a * c + b * c` produce different results based on how the expression is grouped.

The operator demonstrates right-associativity, meaning that when multiple exponentiation operators appear in an expression, they are evaluated from right to left. This affects how nested exponentiation operations are processed. For example, `a ** b ** c` is equivalent to `a ** (b ** c)` rather than `(a ** b) ** c`.

Understanding operator precedence and associativity is crucial for writing correct and predictable JavaScript code, particularly when mixing exponentiation with other arithmetic operations. While the basic rules align with established mathematical conventions, the right-associative property of the exponentiation operator sets it apart from some other programming languages, where exponentiation might follow left-associative rules.


## Working with Number and BigInt Data Types

JavaScript's exponentiation operator (`**`) handles both standard numbers and BigInt values, with specific rules for mixing data types in calculations. The operator accepts values of the `number` type and the `[bigint]` type, offering consistency with other languages through its right-associative nature (a ** b ** c equals a ** (b ** c)).

When both operands are coerced to numeric values, the operator performs standard exponentiation, as demonstrated in the examples: 2 ** 3; // 8 and 3 ** 2.5; // 15.588457268119896. However, attempting to mix numbers and BigInts results in errors: 2n ** 2; // TypeError: Cannot mix BigInt and other types, use explicit conversions, and 2 ** 2n; // TypeError: Cannot mix BigInt and other types, use explicit conversions.

To perform mixed-type calculations, explicit conversions are necessary. For instance, 2n ** BigInt(2); returns 4n, while Number(2n) ** 2 produces 4. The operator's handling of special cases follows logical patterns: 0 ** 3 results in 0, 0 ** -1 returns Infinity, and (-0) ** -1 produces -Infinity. For non-numeric inputs, NaN ** 2 yields NaN, and NaN ** 0 returns 1 to preserve backward compatibility.

When working with both number and BigInt types, the following rules apply:

- When both operands become BigInts, the operation occurs between BigInt values: 2n ** 1024; // Infinity

- When one operand becomes BigInt and the other becomes number, a TypeError is thrown: 2 ** 2n; // TypeError: Cannot mix BigInt and other types, use explicit conversions

- To resolve type conflicts, use explicit conversions: 2n ** BigInt(2); // 4n or Number(2n) ** 2; // 4


## Handling Special Cases and Edge Conditions

Zero raised to a positive power results in 0, while any positive number raised to the power of 0 returns 1. Negative exponents yield fractional results: 2 ** -3 equals 1/8. The operator correctly handles special cases, returning Infinity for 0 ** -1 and -Infinity for (-0) ** -1. When both operands become BigInts, the operation results in Infinity, as demonstrated by 2n ** 1024. Mixing Number and BigInt values throws a TypeError; for example, 2 ** 2n produces this error, while explicit conversions resolve the issue: 2n ** BigInt(2) returns 4n, and Number(2n) ** 2 yields 4.

The operator's handling of non-numeric inputs follows logical patterns: NaN ** 3 results in NaN, while NaN ** 0 returns 1 to preserve backward compatibility. When working with both number and BigInt types, JavaScript coerces strings to numbers where possible: 2 ** "3" evaluates to 8, while 2 ** "hello" produces NaN due to the non-numeric string input.

Parentheses play a crucial role in operator precedence and associativity. The ** operator associates to the right, meaning that 2 ** 3 ** 2 is evaluated as 2 ** (3 ** 2), resulting in 512. This differs from left-associative languages where (2 ** 3) ** 2 would yield 64. Unary operators require careful placement: -(2 ** 2) returns -4, while (-2) ** 2 produces 4. Understanding these nuances ensures correct exponentiation calculations across various input types and scenarios.

