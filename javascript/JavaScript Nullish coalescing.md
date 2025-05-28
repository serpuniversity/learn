---

title: JavaScript Nullish Coalescing Operator (??)

date: 2025-05-27

---


# JavaScript Nullish Coalescing Operator (??)

JavaScript's nullish coalescing operator (??) offers a powerful solution for handling undefined and null values, distinguishing itself from the traditional logical OR operator through stricter type checking. This introduction explores the fundamentals of the nullish coalescing operator, comparing its behavior with the logical OR, and examining its applications in default value assignment, property access, and modern JavaScript development practices.


## Fundamentals of Nullish Coalescing

The nullish coalescing operator, ??, is designed to handle situations where the left operand might be unintentionally left unassigned (null) or missing a value (undefined). Unlike the logical OR, which returns the second expression if the first expression is falsy, the nullish coalescing operator returns the second expression only when the first one is null or undefined.

This operator provides better type safety by considering null and undefined as the only nullish values. While the logical OR would treat 0, empty strings, and false as valid, the nullish coalescing operator maintains strict handling of null and undefined, making it particularly useful for cases where these specific values need to be distinguished from other falsy inputs.

The operator's evaluation process follows a straightforward pattern: if the left operand is nullish (null or undefined), it returns the right operand; otherwise, it returns the left operand. This behavior makes it particularly effective for default value assignment, where you want to ensure that a variable receives a defined value when the initial assignment might be missing.

For example, consider a function that retrieves query parameters from URL parameters:

```javascript

function getQueryParam(name) {

  const value = window.location.search ?? null;

  return value[name] ?? null;

}

```

In this case, the function first checks if window.location.search is defined. If not, it returns null instead of an empty string, providing a more accurate representation of the absence of a query parameter.


## Operator Syntax and Evaluation

The nullish coalescing operator (??) follows a specific evaluation pattern: it checks whether the left-hand side operand is null or undefined. If the left operand is nullish, it returns the right-hand side operand. Otherwise, it returns the left-hand side operand. This behavior is distinct from the logical OR operator (||), which returns the first truthy value in a series of expressions.

The operator's syntax requires careful consideration of operator precedence. While it has the fifth-lowest precedence, it cannot be directly combined with AND or OR operators in the same expression without causing syntax errors. For instance, the expression `exp1 && exp2 ?? exp3 || exp4` is invalid and would result in a syntax error. To properly combine these operators, developers must use parentheses to ensure correct evaluation, as in `(exp1 && exp2 ?? exp3) || exp4`.

A key aspect of the operator's functionality is its treatment of falsy values. Unlike the logical OR, which returns its left operand if it is falsy (including 0, empty strings, and false), the nullish coalescing operator returns the left operand only when it is strictly null or undefined. This distinction makes it particularly useful for scenarios where null and undefined need to be handled separately from other falsy values.

For example, consider the following expressions:

- `expression1() ?? expression2()`: If `expression1()` returns null, the operator returns `expression2()`.

- `expression1() || expression2`: If `expression1()` returns an empty string, the OR operator returns `expression2`.

This fundamental difference in handling falsy values makes the nullish coalescing operator particularly effective for safe default value assignment. Modern JavaScript development typically recommends using ?? for such scenarios, as it provides more precise control over value handling compared to the traditional OR operator.


## Behavior Comparison with Logical OR

The nullish coalescing operator (??) and the logical OR operator (||) differ fundamentally in how they handle falsy values. While the OR operator returns its left operand if it is falsy, the nullish coalescing operator returns its left operand only when it is strictly null or undefined.

This distinction becomes particularly important when dealing with values that are intentionally set to false. For instance, consider the following expressions:

- `expression1() ?? expression2()` will return `expression2()` only if `expression1()` returns null or undefined.

- `expression1() || expression2` will return `expression2()` if `expression1()` returns false, an empty string, or 0.

The nullish coalescing operator's handling of falsy values makes it particularly useful in scenarios where null and undefined need to be treated as distinct from other falsy values. As noted in the documentation, "the nullish coalescing operator (??) is useful for creating default values when the left operand should only be null or undefined."

Modern JavaScript development typically recommends using the nullish coalescing operator over the logical OR for such scenarios. This is because the nullish coalescing operator provides more precise control over value handling, as explained in the MDN Web Docs: "It's not possible to combine both the AND (&&) and OR operators directly with ??, requiring parentheses for precedence."

The operator's behavior is consistent across various data types, returning the right operand only when the left operand is null or undefined. For example:

- In the expression `0 ?? 1`, the result is 0, as 0 is not nullish.

- Similarly, in `false ?? true`, the result is false, maintaining strict nullish value handling.


## Use Cases and Best Practices

The nullish coalescing operator significantly enhances JavaScript's ability to handle default values while maintaining strict type checks. It provides a concise alternative to traditional null checks and ternary operators, making the code more readable and maintainable.

One primary use case is safely setting default values for function parameters:

```javascript

function processItems(items = []) {

  items = items ?? []; // Always starts with an empty array

  // Process items here

}

```

This pattern ensures that the function always receives a valid array, handling cases where the caller might forget to provide an argument.

The operator also excels in property access, particularly when dealing with potential null values:

```javascript

const user = { name: 'John' };

const isAdmin = user?.isAdmin ?? false; // Checks for null or undefined, returning false if absent

```

This idiom safely retrieves the isAdmin property, treating its absence as a falsey value while distinguishing it from explicitly defined null or undefined states.

Modern frameworks and libraries have adopted the nullish coalescing operator extensively. For example, Angular's router uses it to safely retrieve query parameters:

```javascript

const page = parseInt(router.query.page) ?? 1;

```

This pattern ensures that the page variable always contains a valid integer, handling cases where the query parameter might be missing or invalid.

The operator's behavior with numbers deserves particular attention. While the logical OR operator would treat 0 as a valid default, the nullish coalescing operator maintains strict null and undefined checking:

```javascript

const quantity = getQuantity() ?? 1; // Returns 1 only if getQuantity returns null or undefined

```

This distinction is crucial in scenarios where 0 might have a specific meaning, such as indicating the absence of an item rather than the value zero.


### Operator Precedence and Combined Usage

Developers must be aware of the operator's precedence when combining it with other logical operators. Directly nesting the nullish coalescing operator with logical OR can result in unexpected behavior:

```javascript

let value = null ?? 0 || 'default'; // Evaluates to 'default', not '0 || default'

```

To correctly chain these operators, developers should use parentheses:

```javascript

let value = (null ?? 0) || 'default'; // Evaluates to '0', as intended

```

This pattern ensures the nullish coalescing operator has the opportunity to evaluate before the logical OR.


### Browser Support and Compatibility

While the nullish coalescing operator has become widely supported across modern browsers, developers working with legacy environments should be aware of compatibility issues. The operator requires at least ECMAScript 2020 support, which may not be present in older browser versions. For these cases, developers can use Babel or other transpilation tools to ensure compatibility while leveraging the new operator in modern environments.

