---

title: JavaScript Operator Precedence and Evaluation

date: 2025-05-27

---


# JavaScript Operator Precedence and Evaluation

JavaScript operators determine how expressions are evaluated through a combination of precedence levels and associativity rules. While parentheses allow explicit control over the evaluation order, understanding operator precedence ensures expressions are parsed correctly when nested or combined. The evaluation hierarchy begins with parentheses, followed by exponentiation, multiplication/division, and finally addition/subtraction, all of which follow left-to-right (left-associative) rules except for exponentiation's right-associativity. Mastering these principles is essential for writing efficient and reliable JavaScript code.


## Basic Operator Precedence

In JavaScript, operator precedence determines the order in which operations are performed in an arithmetic expression. This precedence follows a specific order, with parentheses having the highest precedence and addition/subtraction having the lowest.

The precedence levels of operators are as follows:

1. Grouping ()

2. Exponents (**

3. Multiplication (*) and Division (/)

4. Addition (+) and Subtraction (-)

When operations have the same precedence, they are evaluated from left to right. For example, in the expression 10 + 5 * 2, multiplication is performed first, resulting in 10 + 10, which equals 20.

The following table presents the operator precedence levels and their associated operations:

| Precedence Level | Operator | Usage | Reading Direction | Precedence from Highest to Lowest |

|------------------|----------|-------|------------------|---------------------------------|

| 19               | Parentheses ( ) | Member Access ( . ) and Computed Member Access ( [ ] ) | Function Call ( ( ) ) | Postfix Increment and Postfix Decrement |

| 18               | Logical NOT and Bitwise NOT | Multiplication, Division, and Remainder | Addition and Subtraction | Bitwise Left Shift |

| 17               | Function Call ( ( ) ) | Postfix Increment and Postfix Decrement | Logical NOT and Bitwise NOT | Member Access ( . ) and Computed Member Access ( [ ] ) |

| 16               | None | None | Left-associativity | Right-associativity |

Operator associativity determines how operators of the same precedence are processed. The two types of associativity are left-to-right (left-associativity) and right-to-left (right-associativity). For example, assignment operators are right-associative, so in the statement a = b = 5, b is assigned first, then a receives the value of b (5).

The evaluation order is always left-to-right, regardless of associativity. When operators have different precedence levels, the operator with the highest precedence is evaluated first. For instance, in the expression 3 + 4 * 2, the multiplication operator (*) has higher precedence than the addition operator (+), so the multiplication is performed first: 3 + (4 * 2).


## Special Case: Assignment Operators

JavaScript assignment operators have specific evaluation rules that affect how values are assigned in expressions. These operators evaluate right-to-left (right-associative), meaning that in the statement `a = b = 5;`, the rightmost assignment is evaluated first: `b = 5`, followed by `a = 5`.

The result of an assignment expression is based on the values of its operands before the operation. For example, when evaluating `y = x = f()`, the function call `f()` is executed first, printing "F!" and returning the value 2. This value is then assigned to `x`, and subsequently to `y`, resulting in both variables containing 2 after the assignment.

Chaining assignments can lead to unexpected behavior, especially within variable declarations using `const`, `let`, or `var`. Only the outermost variable is declared; variables within the assignment chain are not declared by these statements. For example, in `const [a, b] = f();`, only `f()` is assigned as an array to `a` and `b` are not declared by the `const` statement.

The evaluation of expressions involving assignments always follows this right-associative rule, ensuring consistent behavior regardless of the surrounding context or variable declarations. Understanding these rules is essential for writing correct and efficient JavaScript code, as they determine the order in which expressions are evaluated, potentially affecting the outcome of complex operations.


## Complex Expression Evaluation

JavaScript follows a well-defined precedence order for operators, with parentheses having the highest precedence and addition/subtraction the lowest. When multiple operators of the same precedence appear in an expression, they are evaluated from left to right, a process known as left-associativity.

The evaluation hierarchy is as follows:

1. Parentheses: The order of operations can be explicitly controlled using parentheses, which have the highest precedence. For example, in the expression (3 + 5) * 2, the addition is performed first due to the parentheses.

2. Exponentiation: The exponentiation operator (**) has the second-highest precedence and is right-associative. This means that in expressions like 2 ** 3 ** 2, the operation is evaluated from right to left: (3 ** 2) ** 2.

3. Multiplication and Division: These operators have the same precedence and are left-associative. In the expression 6 / 3 / 2, the division operations are performed left to right: (6 / 3) / 2.

4. Addition and Subtraction: These operators have the lowest precedence and are also left-associative. For example, in the expression 10 + 5 - 2, addition and subtraction are performed from left to right: (10 + 5) - 2.

When operators of different precedence levels appear in the same expression, the higher-precedence operators are evaluated first. For instance, in the expression 3 + 4 * 2, the multiplication operator (*) has higher precedence than the addition operator (+), so the multiplication is performed first: 3 + (4 * 2).

The evaluation of complex expressions can be further clarified using parentheses. For example, in the expression 5 + 3 * 2 ** 2 / 4, exponentiation is performed first: 5 + 3 * 4 / 4. Then, following left-associativity, multiplication and division are evaluated from left to right: 5 + 12 / 4. Finally, addition is performed: 5 + 3, resulting in a total of 8.

Understanding operator precedence and associativity is crucial for writing correct and efficient JavaScript code. It determines the order in which expressions are evaluated, potentially affecting the outcome of complex operations. Best practices include using parentheses to clarify expressions, being aware of operator precedence and associativity, and prioritizing bracket and dot notation operations due to their higher precedence.


## Operator Association and Evaluation Order

Operator precedence establishes the order in which different operators are evaluated, ensuring expressions are parsed correctly. However, when operators of the same precedence appear in the same expression, their evaluation order depends on their associativity: left-to-right (left-associative) or right-to-left (right-associative).

Most operators, including arithmetic operations (multiplication, division, addition, subtraction), have left-associativity. This means that when multiple operators of the same precedence are present, they are evaluated from left to right. For example, in the expression 10 + 5 * 2, the multiplication is performed first: 10 + (5 * 2).

The exponentiation operator (**) is an exception, being right-associative. This means that when multiple exponentiation operators appear in an expression, they are evaluated from right to left. For instance, the expression 2 ** 3 ** 2 is interpreted as 2 ** (3 ** 2), resulting in 512 rather than 64 if evaluated from left to right.

Parentheses (()) provide the highest precedence by explicitly controlling the order of evaluation. Any expression enclosed in parentheses is evaluated first, regardless of the operators involved. For example, in the expression (2 ** 3) ** 2, the inner exponentiation is evaluated first, resulting in 64 rather than the 8 that would be obtained from evaluating 2 ** (3 * 2).

Understanding operator association is crucial for predicting the outcome of complex expressions. When operators of the same precedence appear in the same expression, their evaluation order follows these rules:

- Left-associative operators (arithmetic operations, shift operators) are processed left to right

- Right-associative operators (exponentiation) are processed right to left

- Parentheses allow precise control of evaluation order, overriding precedence rules

These rules ensure consistent behavior in JavaScript expressions, allowing developers to predict and control the order of operations when writing complex code.

