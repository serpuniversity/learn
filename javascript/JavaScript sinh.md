---

title: JavaScript Math sinh() Function

date: 2025-05-26

---


# JavaScript Math sinh() Function

The JavaScript Math.sinh() function implements the hyperbolic sine calculation using the formula (e^x - e^(-x)) / 2, returning the hyperbolic sine of a given number. This implementation, part of ECMAScript6, has been widely supported across modern browsers since 2017 and is essential for mathematical computations involving hyperbolic functions. Through detailed exploration of its definition, properties, and usage patterns, this article provides a comprehensive understanding of Math.sinh(), its mathematical foundations, and its practical applications in JavaScript programming.


## Definition and Syntax

Math.sinh() is a static method of the Math object in JavaScript, meaning it is called using `Math.sinh()` rather than as a method of an object instance. The function takes a single numeric argument and returns the hyperbolic sine of that number.

The hyperbolic sine function follows the mathematical definition:

\[ \sinh(x) = \frac{e^x - e^{-x}}{2} \]

where \( e \) is Euler's number, approximately 2.71828. This formula is used to calculate the hyperbolic sine for any input value.

When given specific numeric inputs, Math.sinh() behaves as follows:

- \(\sinh(0)\) returns 0

- \(\sinh(1)\) returns approximately 1.1752

- \(\sinh(-1)\) returns approximately -1.1752

- \(\sinh(2)\) returns approximately 3.6269

- \(\sinh(-2)\) returns approximately -3.6269

- \(\sinh(\infty)\) returns Infinity

- \(\sinh(-\infty)\) returns -Infinity

- \(\sinh("Harry")\) returns NaN (Not a Number)

The function supports both positive and negative numeric inputs, returning Infinity or -Infinity for inputs approaching positive or negative infinity, respectively. Non-numeric inputs and empty inputs result in a return value of NaN.


## Mathematical Properties

The hyperbolic sine function, defined as sinh(x) = (e^x - e^-x) / 2, shares several properties with trigonometric functions. These properties can be understood through the identities:

1. cosh^2 x - sinh^2 x = 1

2. sinh 2x = 2 sinh x cosh x

The first identity can be proven by substituting the definitions of cosh x and sinh x and expanding:

cosh2x - sinh2x = (e^2x + 2 + e^-2x - e^2x + 2 - e^-2x) / 4

= 4 / 4

= 1

The second identity arises directly from the definitions:

2 sinh x cosh x = (e^x - e^-x)(e^x + e^-x) / 2

= (e^2x + 1 - 1 - e^-2x) / 2

= (e^2x - e^-2x) / 2

= sinh 2x

These properties, similar to those of trigonometric functions, provide a basis for understanding and using the sinh function in mathematical and practical contexts.


## Usage and Examples

The sinh() function operates on radian inputs and accepts both real and complex numbers, with real inputs producing real results and complex inputs producing complex results. The function supports scalar, vector, matrix, and multidimensional array inputs, making it versatile for various applications in mathematics, engineering, and physics.

Key behaviors of the function include:

- sinh(0) = 0

- sinh(x) = -sinh(-x)

- For large positive x, sinh(x) approaches ex/2

- For large negative x, sinh(x) approaches -e-x/2

When applied to specific values, the function demonstrates the following:

- sinh(-1) = -1.1752011936438014

- sinh(0) = 0

- sinh(1) = 1.1752011936438014

- sinh(2) = 3.626860407847019

- sinh(20) approaches Infinity due to the function's exponential nature

The function returns Infinity for inputs approaching positive infinity and -Infinity for inputs approaching negative infinity. Non-numeric inputs or empty inputs result in a return value of NaN (Not a Number).

The function's implementation in JavaScript demonstrates its support for various numeric inputs, including zero, positive numbers, and negative numbers. It accurately calculates the hyperbolic sine using the formula:

\[ \sinh(x) = \frac{e^x - e^{-x}}{2} \]

The method's syntax Math.sinh(x) correctly computes the hyperbolic sine for a given numeric input, with the result being the same type as the input (number, BigNumber, or Complex).


## Special Cases and Edge Behavior

The sinh function handles several special cases and edge inputs consistently across its implementation in JavaScript. For inputs approaching infinity, the function accurately returns Infinity or -Infinity based on the sign of the input:

- Math.sinh(Infinity) returns Infinity

- Math.sinh(-Infinity) returns -Infinity

When presented with non-numeric inputs or empty values, the function correctly returns NaN (Not a Number):

- Math.sinh("Harry") returns NaN

- Math.sinh() returns NaN

The function's behavior with very large inputs demonstrates its implementation of the hyperbolic sine's exponential nature:

- For large positive x, sinh(x) approaches ex/2

- For large negative x, sinh(x) approaches -e-x/2

This property remains consistent with the mathematical definition of the hyperbolic sine function, which always produces values between the graphs of ex/2 and e-x/2. The function's implementation in JavaScript effectively maintains these mathematical properties across valid and edge-case inputs.


## Browser Support and Specifications

The Math.sinh() method returns the hyperbolic sine of a number, implementing the formula:

sinh(x) = (e^x - e^(-x)) / 2

Availability:

The method is part of ECMAScript6 (ES6) and was supported in all modern browsers beginning June 2017. Current browser compatibility includes:

- Chrome 51

- Edge 15

- Firefox 54

- Safari 10

- Opera 38

Implementation:

- Works across many devices and browser versions, with functionality available since July 2015

- Supports various numerical inputs, including zero, positive numbers, and negative numbers

- Returns Infinity for positive Infinity input and -Infinity for negative Infinity input

- Returns NaN for non-numeric or empty input

Usage:

The function supports scalar, vector, matrix, and multidimensional array inputs, demonstrating its versatility in mathematical and practical applications. Examples include:

- Math.sinh(0) = 0

- Math.sinh(1) = approximately 1.1752

- Math.sinh(2) = approximately 3.6269

- Math.sinh(20) approaches Infinity due to the function's exponential nature

