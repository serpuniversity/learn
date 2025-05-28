---

title: Bad continue: JavaScript Error Handling Guide

date: 2025-05-26

---


# Bad continue: JavaScript Error Handling Guide

JavaScript's `continue` statement offers a powerful way to control loop iteration, allowing developers to skip current loop executions under specific conditions. However, misusing this feature can lead to cryptic syntax errors, most notoriously the "Bad continue" error. This guide explores the fundamental requirements for using `continue` statements correctly, explains how different JavaScript environments interpret these errors, and provides practical solutions for writing maintainable, error-free code.


## Bad continue Error Explanation

The "Bad continue" error in JavaScript is a SyntaxError that occurs specifically when a `continue` statement is used outside of a loop structure. According to MDN Web Docs, the language specification requires labeled statements to be loops, meaning that the `continue` statement must be within a loop context to function correctly.

The error manifests differently across browsers:

- In V8-based environments (Chrome, Node.js), it produces messages like "SyntaxError: Illegal continue statement: no surrounding iteration statement" and "SyntaxError: Illegal continue statement: 'label' does not denote an iteration statement."

- Firefox throws "SyntaxError: continue must be inside loop."

- Safari reports "SyntaxError: continue is only valid inside a loop statement" and issues specific errors for undefined labels, such as "Cannot continue to the label 'label' as it is not targeting a loop."

The fundamental issue, as explained by MDN Web Docs, is that while the `continue` statement is designed to terminate execution of the current iteration of a loop and continue with the next iteration, it can only do so within the boundaries of a loop structure. Attempting to use it elsewhere results in the syntax error. This restriction applies whether the statement is used with or without labels, though labeled statements require additional considerations regarding scope and nesting.


## Error Occurrence Context

A "Bad continue" error occurs when a `continue` statement is used outside of a loop structure. The `continue` statement must be within a loop's boundaries to function correctly, with MDN Web Docs explicitly stating that labeled statements require them to be loop statements.

The error manifests differently across browsers: V8-based environments like Chrome and Node.js return messages such as "SyntaxError: Illegal continue statement: no surrounding iteration statement" and "SyntaxError: Illegal continue statement: 'label' does not denote an iteration statement." Firefox's error message is simply "SyntaxError: continue must be inside loop," while Safari reports "SyntaxError: continue is only valid inside a loop statement" and issues specific errors for undefined labels like "Cannot continue to the label 'label' as it is not targeting a loop."

The error can occur when attempting to use a continue statement with an undefined label, as demonstrated in the MDN example:

```

js label: { for (let i = 0; i < 10; i++) { continue label; // SyntaxError: Illegal continue statement: 'label' does not denote an iteration statement } }

```

In labeled loops, the label must reference a containing loop statement, and using it with a non-loop statement results in a syntax error.

Douglas Crockford's opinion, as noted in the discussions surrounding the use of continue statements, stems from his belief in not allowing assignment within conditionals, as JSlint does not permit this feature. The error type is SyntaxError, with the JavaScript specification strictly requiring the `continue` statement to be within a loop structure.


## Solution and Best Practices

The "Bad continue" error in JavaScript occurs when a `continue` statement is used outside of a loop structure. This syntax error prevents the `continue` statement from reaching its intended destination, which is to terminate the current iteration of a loop and proceed to the next iteration. The `continue` statement must be used within a loop's boundaries to function correctly, and attempting to use it elsewhere results in a syntax error.

To fix these errors, developers should ensure that `continue` statements are always placed within loop structures. If a loop contains multiple `continue` statements, consider refactoring the code to improve readability and maintainability. For example, Douglas Crockford suggests that complex loops can be simplified by extracting inner loops into separate functions, making the code more manageable and easier to understand.

When working with labeled statements and nested loops, developers must ensure that the labeled statement refers to a containing loop statement. If the label is undefined or references a non-loop statement, a `SyntaxError: label not found` will be thrown. To prevent these errors, always verify that labels correctly reference loop statements and that loops do not span across function boundaries.

Developers can further improve their JavaScript code by following these best practices:

1. Use `continue` when you have a clear and logical condition for skipping iterations, as this helps in understanding the flow of the loop and makes the code more readable.

2. Avoid overusing `continue` to prevent making the code harder to follow. Ensure its use is justified and adds value to the loop's logic.

3. Document usage of `continue` with comments, especially in complex loops, as this aids in future maintenance and for other developers reading your code.

4. Use labeled statements with `continue` when working with nested loops to control flow more precisely, but maintain their use at a minimum to avoid confusion.

5. Test thoroughly after adding `continue` statements to ensure the loop behaves as expected, as this helps catch any logical errors that might arise.

By following these guidelines, developers can effectively use `continue` statements to control loop flow and write clean, efficient JavaScript code while maintaining optimal performance and readability.


## Exception Handling

To handle and prevent "continue must be inside loop" errors, developers should ensure that `continue` statements are always placed within loop structures. If a loop contains multiple `continue` statements, consider refactoring the code to improve readability and maintainability.

For labeled statements and nested loops, always verify that labels correctly reference loop statements and maintain their use at a minimum to avoid confusion. Specifically, the `continue` statement cannot be used at the top level of a script, module, function's body, or static initialization block.

When working with arrays or collections, developers can implement custom range checking functions to validate input values and ensure they fall within the desired range. This can prevent range errors and help identify potential issues before they occur.

Additionally, developers should maintain consistency in using `continue` within their codebase. Consistent patterns help maintain readability and predictability of the code.

To avoid misuse, consider alternative approaches to using `continue` within `forEach()` loops. For instance, use `return` instead of `continue` or convert the loop to a `for...of` loop.

By following these guidelines and best practices, developers can effectively control loop flow and write clean, efficient JavaScript code while maintaining optimal performance and readability.

