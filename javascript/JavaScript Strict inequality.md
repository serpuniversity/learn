---

title: JavaScript Strict Inequality: Understanding Value and Type Comparison

date: 2025-05-27

---


# JavaScript Strict Inequality: Understanding Value and Type Comparison

In JavaScript, the equality operators (== and ===) determine whether two values are considered equal or not. While the loose equality operator attempts to coerce values to a common type before comparing them, the strict equality operator requires both value and type to match exactly. This fundamental difference leads to distinct behaviors when comparing various data types, including numbers, strings, objects, and special values like NaN and null. Understanding these differences is crucial for writing accurate and predictable JavaScript code, as the choice between loose and strict comparison operators can significantly affect your program's behavior.


## Strict Inequality Operator (!==) vs Equality Operators

The strict inequality operator (!==) and its counterpart (==) serve distinct purposes in JavaScript, particularly regarding how they handle value and type comparisons.

When comparing variables of different types, the strict inequality operator checks both the value and the data type of the variables, providing more predictable results. For example, when comparing `var1 = 5` and `var2 = '5'`, the statement `var1 !== var2` evaluates to true because their data types are different—var1 is a number, while var2 is a string.

This behavior stands in contrast to the loose equality operator (==), which performs type coercion before comparing the values. In the same example, `var1 == var2` would evaluate to true because JavaScript converts the string '5' to the number 5 before comparing.


### Comparison Rules Across Different Data Types

The strict inequality operator handles comparisons between different data types by attempting to convert the operands to the same type before comparing. However, if the resulting types still differ after conversion, the operator returns false. For instance, comparing `2 !== '2'` returns true because, although both values are numerically equivalent, their data types are different—a number and a string.

The strict inequality operator also considers objects' internal references rather than merely comparing their properties. As demonstrated in the examples, two objects with identical properties (`{name: "Ram"}`) will not be considered equal if they reference different memory locations: `(d !== e)` evaluates to true, but `(f !== e)` evaluates to false since f and e reference the same object.


### Browser Compatibility and Implementation

The strict inequality operator's implementation across browsers demonstrates its widespread support, with consistent behavior since July 2015. The operator works identically to the abstract equality operator except for the strict type checking, making it compatible with all modern JavaScript environments.


## Comparison Algorithm and Data Type Handling

The strict inequality operator (!==) employs a specific algorithm to compare operands, which first checks if the types of both operands match. If the types differ, the operator immediately returns false, as demonstrated by the examples provided: `a === '100' returns false` and `a === true returns false` due to type differences between number and string, and number and boolean, respectively.

When comparing numeric values, the operator follows precise rules, as explained in the documentation: it returns true only if both operands are numbers and match in value, including handling +0 and -0 as equivalent. This strict comparison ensures that values like 2 and 2 return true, while 2 and "2" return false, maintaining the separation between numeric and string types.

The comparison algorithm also extends to handling of special values: both NaN and null require exact matching to return true. For objects, the comparison examines reference equality rather than property values, meaning two objects with identical properties will be considered unequal if they reference different memory locations: both `d !== e` and `f !== e` demonstrate this behavior based on object identity rather than property comparison.

The algorithm's string handling strictly compares character sequences for equality, while Boolean values require both to be true or both false for a match. This ensures that comparisons between different types of values remain consistently unambiguous, making strict inequality a reliable tool for scenarios where type safety is crucial.


## Examples and Practical Usage

The strict inequality operator's behavior becomes particularly apparent when comparing different data types. For instance, `var1 = 5` and `var2 = '5'` demonstrate that `var1 !== var2` evaluates to true because their data types differ—var1 is a number, while var2 is a string. This strict comparison ensures that values like 2 and '2' remain distinct, maintaining the separation between numeric and string types.

When both operands are numbers, the operator follows precise rules: it returns true only if both operands are numbers and match in value, including handling +0 and -0 as equivalent. This strict comparison ensures that values like 2 and 2 return true, while 2 and '2' return false, maintaining the separation between numeric and string types.

The operator's behavior extends to special values and object comparisons. Both NaN and null require exact matching to return true. For objects, the comparison examines reference equality rather than property values. As demonstrated, two objects with identical properties (`{name: "Ram"}`) will not be considered equal if they reference different memory locations: `(d !== e)` evaluates to true, but `(f !== e)` evaluates to false since f and e reference the same object.

The operator's implementation has demonstrated consistent behavior across modern JavaScript environments since July 2015. All major browsers, including Chrome, Edge, Firefox, Opera, and Safari, support the operator's functionality as specified in the core language specification.


## Browser Compatibility and Implementation

The strict inequality operator's implementation across browsers demonstrates its widespread support, with consistent behavior since July 2015. All major browsers, including Chrome, Edge, Firefox, Opera, and Safari, support the operator's functionality as specified in the core language specification.

All of these browsers implement the strict inequality operator using the same fundamental principles: comparing both value and type, with no implicit type conversion. For instance, comparing `2 !== '2'` returns true because, although the numeric values are equivalent, their data types differ—a number and a string.

The operator's implementation follows a standardized algorithm across all supported browsers. This uniformity ensures that developers can rely on consistent behavior across different environments. For example, when comparing `true` and `1`, `true !== 1` returns true, demonstrating the operator's strict type checking even when the values appear to be numerically equivalent.


## Best Practices and Recommendations

Based on JavaScript best practices, developers should use strict inequality (!==) for most comparison operations. This approach aligns with the language's core philosophy of clear and predictable behavior. Here's why strict inequality is recommended:


### When to Use Strict Inequality

The strict inequality operator should be used whenever you need to explicitly check both value and type. This includes comparisons between different data types, object references, and special values like NaN and null. For example, instead of checking `a == null`, you should use `a === null` for more precise results.


### Exception for Special Cases

The only common exception to strict type checking is when performing null checks, where `a == null` remains a valid practice. This pattern is even used in jQuery 1.9.1 with 43 occurrences. The JSHint syntax checker provides the `eqnull` relaxing option specifically for this use case.


### Performance Considerations

The strict equality operator (`===`) has the same performance as other value checks when types are already the same. However, it excels in situations where types differ, directly returning false without unnecessary type conversion. This makes it particularly useful in scenarios where optimizing performance is crucial.


### Following Community Standards

The JavaScript community generally recommends using strict equality throughout codebases, with specific exceptions noted. While some tools like JSLint may suggest unnecessary changes, the broader consensus supports the use of `===` for its predictable behavior and clear intent.

In conclusion, developers should prioritize strict inequality checks for most comparison operations, leveraging its precision and predictability. The language's core operators are designed with these principles in mind, making strict type checking the recommended approach for modern JavaScript development.

