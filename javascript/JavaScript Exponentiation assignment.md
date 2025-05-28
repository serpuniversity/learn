---

title: JavaScript Exponentiation Assignment Operator

date: 2025-05-27

---


# JavaScript Exponentiation Assignment Operator

JavaScript's exponentiation assignment operator (**) introduces a powerful feature for concise mathematical operations, allowing developers to raise numbers to powers and assign the result back to the original variable. This guide explores the operator's usage, syntax, and implementation across various browsers, highlighting its compatibility with both floating-point numbers and BigInts for arbitrary-precision arithmetic. You'll learn how the operator's right-associative precedence rules affect expression evaluation, enabling efficient chaining of exponentiation operations while maintaining consistency with JavaScript's broader operator hierarchy. The article also examines the operator's behavior in edge cases, such as raising NaN values to powers and handling negative bases, providing valuable insights into its implementation and mathematical foundations.


## Basic Usage and Syntax

The exponentiation assignment operator (**) in JavaScript allows numbers (including BigInt) to be raised to a power and the result to be assigned back to the original variable, making it a powerful tool for concise mathematical operations.

This operator follows right-associative precedence, meaning expressions like `a ** b ** c` are evaluated as `a ** (b ** c)` (1). The operator has higher precedence than multiplication and division, but lower than unary operators, aligning with JavaScript's property access operator precedence (2). However, this differs from traditional mathematical notation, where parentheses are typically required when writing `(-x)^n` (3).

When used with numbers, the operator behaves similarly to `Math.pow()`, returning the base raised to the exponent. For example, `2 ** 3` results in 8, while `10 ** -1` gives 0.1 (4). Supported browsers include Chrome 52, Edge 14, Firefox 52, Opera 39, and Safari 10.1 (5).

BigInt support allows for arbitrary-precision arithmetic. When both operands are BigInts, the operation returns the same type. For example, `2n ** 3n` results in 8n, while `2n ** 1024n` produces a very large number without overflowing to Infinity (6). Mixing BigInt and number operands throws a TypeError, as demonstrated by attempting to compute `2n ** 2` as a number, which fails (7).

The operator handles various edge cases according to established mathematical principles. Any number raised to the power of 0 returns 1, while 0 raised to any positive power results in 0. Notably, 0 ** 0 returns 1, following standard mathematical conventions (8). Positive numbers raised to negative powers yield their reciprocal; for instance, 2 ** -1 results in 0.5 (9). The behavior with NaN is well-defined: any exponentiation involving NaN returns NaN, while NaN ** 0 specifically returns 1 (10).


## Precedence and Evaluation Order

The exponentiation assignment operator (**) in JavaScript is designed with specific precedence rules that align with broader language patterns while maintaining consistency with mathematical notation conventions. The operator's placement in the precedence hierarchy makes it more like unary operators rather than lower-precedence binary operators, which can affect how expressions are evaluated.

In JavaScript, the exponentiation operator binds tighter than unary operators but is at the same precedence level as other arithmetic operations. This differs from traditional mathematical notation, where exponentiation has higher precedence than unary operations. The language's grammar rules ensure that expressions like -2 ** 2 evaluate to -4, matching common mathematical expectations (1).

The current design follows established patterns in other programming languages, including JavaScript's property access operators. While this may lead to some expressions requiring additional parentheses for clarity, the design choice aims to minimize potential confusion compared to alternative precedences that could cause more widespread issues (2).

The operator's right-associative nature affects how expressions with multiple exponentiations are evaluated. For instance, when incrementing before exponentiation, the expression `++x ** y` is parsed as `(++x) ** y`, aligning with the language's general precedence rules (3). This behavior allows for more intuitive chaining of exponentiation operations while maintaining consistency with JavaScript's broader operator hierarchy (4).

Developers should be aware that certain combinations of unary and exponentiation operations require careful placement of parentheses to achieve the desired evaluation order. The operator's precedence places it higher than multiplication and division but lower than unary operators, making it particularly important to consider when writing complex mathematical expressions in JavaScript (5).


## Special Cases and Considerations

The exponentiation operator (**) in JavaScript behaves uniquely when combined with unary operators, a key distinction from traditional mathematical notation (1). This design follows historical precedence patterns in languages like C and other C-derived languages, where unary operators bind tighter than binary operators, with the notable exception of the dot operator and square brackets (2).

When a unary operator precedes the base number, the expression is parsed differently than in mathematical notation. In JavaScript, -2 ** 2 evaluates to 4, matching Bash behavior but differing from other languages that yield -4 (3). This precedence rule means that expressions like -x ** y must be written as either (-x)**y or -(x**y) to avoid syntax errors, highlighting the operator's impact on code structure (4).

The operator's behavior with negative bases is well-defined: -2 ** 3 returns -8, while -2 ** 0 returns 1, following mathematical conventions (5). The unary + operator attempts to convert operands to numbers, as demonstrated by +true returning 1 and +"3" returning 3 (6). In contrast, the unary - operator negates its operand, and combining it with exponentiation requires careful placement of parentheses to maintain intended behavior (7).

For logical expressions, the NOT operator (!) returns true for non-null and non-zero values, while OR (||) returns the first truthy operand or false if all operands are falsy (8). These operators work consistently across operands, including nullish values and numeric expressions, demonstrating the language's clear evaluation rules (9). The nullish coalescing operator (??) returns its first operand if it's neither null nor undefined, otherwise returning the second operand, further illustrating JavaScript's operator precedence and behavior with special values (10).


## Use Cases and Common Applications

The exponentiation assignment operator's primary application is squaring numbers, as demonstrated by the concise expression `a ** 2` (1). However, its utility extends to complex calculations in various domains:


### Easing Functions

Easing functions in animation and graphics use smooth curves to control the speed of changes over time. For example, an easing function might implement the equation `position = 0.5 * (1 - (1 - time)**2)`, where `time` ranges from 0 to 1 (2).


### Graphics Curves

In computer graphics, parabolic curves can be generated using `y = x**2`, allowing developers to create smooth arcs and trajectories. These curves are fundamental in pathfinding algorithms and projectile motion calculations (3).


### Interest Calculations

Financial applications frequently use exponentiation for interest calculations, especially with compounding interest. The formula `A = P * (1 + r)**t` calculates the future value of an investment, where `P` is the principal amount, `r` is the annual interest rate, and `t` is the time in years (4).


### Game Simulations

In game development, physics engines often use exponentiation for calculating velocity dampening or exponential decay. For instance, a damping factor might be applied using `velocity *= 0.5 * (1 + (timeStep)**-2)`, ensuring smooth deceleration while maintaining numerical stability (5).

The operator's efficiency and readability make it particularly valuable in these applications, where concise mathematical expressions can significantly impact performance and maintainability (6). While direct translation from mathematical notation might require additional parentheses, the operator's high precedence ensures correct evaluation in most cases (7).


## History and Implementation

The decision to include exponentiation assignment in JavaScript emerged from deliberations among language experts who considered historical precedence in other languages and the broader patterns of operator behavior in C and related languages (1). This design choice aligns with the general pattern where unary operators bind tighter than binary operators, a convention that has influenced JavaScript's grammar rules since its inception (2).

However, the committee faced significant opposition from proponents of mathematical notation consistency, who pointed out that traditional algebraic languages like FORTRAN, Algol 60, and BASIC followed different precedence patterns (3). They argued that maintaining these historical precedences would create more intuitive and predictable syntax, as demonstrated by comparisons with other languages where unary operators consistently bind tighter than exponentiation (4). For example, both PHP and Python yield -4 when evaluating -2 ** 2, aligning with the behavior of Haskell and D, where the language grammar specifically enforces right-associative parsing for expressions using both ** and unary - operators (5).

The debate centered on the balance between adherence to mathematical conventions and the practical implications for JavaScript developers (6). While the Mozilla Developer Network advocates for using the functional form Math.pow as less confusing in JavaScript expressions (7), the final implementation established exponentiation assignment operators with identical precedence to unary operators and lower precedence than increment operators (8). This design retained right-associative chaining, a pattern that had not previously caused confusion in JavaScript (9).

The implementation across major browsers followed this specification, with supported versions beginning in Chrome 52, Edge 14, Firefox 52, Opera 39, and Safari 10.1 (10). Implementation considerations included error handling mechanisms that would produce SyntaxErrors in rare cases rather than runtime bugs, and guidance to force over-parenthetical behavior in expressions where precedence might otherwise cause semantic ambiguities (11).

