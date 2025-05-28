---

title: JavaScript Strict Equality: Behavior and Best Practices

date: 2025-05-27

---


# JavaScript Strict Equality: Behavior and Best Practices

When developers compare values in JavaScript, they have two primary options: the strict equality operator (===) or the loose equality operator (==). While both perform comparisons, they do so with fundamentally different behaviors that can significantly impact your code's logic. The strict equality operator requires both value and type to be identical for a true result, performing no implicit type conversion. In contrast, the loose equality operator performs value comparison with implicit type coercion, converting one operand to match the other's type before comparing. This technical difference leads to distinct outcomes in various comparison scenarios, making strict equality particularly useful for precise value matching while requiring developers to handle certain edge cases carefully.


## Definition and Basic Behavior

The strict equality operator (===) requires both the value and type of the operands to be identical for a true result. Unlike the loose equality operator (==), === performs no implicit type conversion, returning false immediately if the types differ.

When comparing two values of different types, === treats them as distinct, even for JavaScript's special cases. For example, a boolean value will never be strictly equal to a number, despite both being "truthy" in a loose equality check. Numerical representations of truth, such as true/1 and false/0, are considered different under strict equality.

The behavior of === with NaN is particularly noteworthy. Since NaN values are not equal to themselves, any comparison with NaN using === will result in false, including NaN === NaN. This differs from the behavior with other values where self-comparison returns true (e.g., 5 === 5).

For comparing string and number values, === requires explicit type conversion if the operands are not already of the same type. This ensures that identical numerical strings and their numeric representations are not considered equal, maintaining the distinction between data types.


## Comparison with Loose Equality

The loose equality (==) operator performs value comparison with implicit type coercion when faced with different operand types. This means that if the types of two values being compared differ, JavaScript automatically converts one to match the other's type before performing the comparison. This behavior stands in contrast to strict equality (===), which requires both value and type to match exactly without any type conversion.

The conversion process follows specific rules: if one operand is a string and the other is a number, the string is converted to a number. Similarly, JavaScript converts boolean values to numbers (true becomes 1, false becomes 0) and treats null and undefined as loosely equal to each other. For objects, the conversion attempts to reference equality rather than value equality, meaning two different object references would be considered unequal even if their properties were identical.

Here are some examples that demonstrate the key differences between the two operators:

```javascript

console.log(21 == 21); // true

console.log(21 == '21'); // true, string coerced to number

console.log(true == 1); // true, boolean coerced to number

console.log(null == undefined); // true, both represent "empty" values

```

In each case, the loose equality operator returns true by performing type conversion to achieve a common type, whereas the strict equality operator would return false for all of these comparisons due to the fundamental type differences.


## Handling Different Data Types

Strict equality (===) requires both value and type to match for a true result. It performs no implicit type conversion and returns false immediately if the types differ, making it particularly useful when comparing values of different types. For example, the comparison true === true returns true, while true === 1 returns false, as the types differ despite the values being numerically equivalent.

When comparing null and undefined values, strict equality treats them as distinct. These special "empty" values must both be null or undefined to return true, as demonstrated by the statement null === undefined, which evaluates to false. This behavior is important to note when writing code that requires strict type matching.

The operator handles different types of numerical values with care. When comparing +0 and -0, strict equality treats them as the same value, returning true for the comparison +0 === -0. However, strict equality distinguishes NaN from all other values, including itself, making NaN === NaN false. This detail is crucial for numerical comparisons where preserving the distinction between different NaN values might be important.

For comparing string and number values, strict equality requires explicit type conversion if the operands are not already of the same type. This ensures that identical numerical strings and their numeric representations are not considered equal, maintaining the distinction between data types. For instance, the comparison "5" === 5 returns false, demonstrating that strict equality enforces type matching in addition to value equality.


## Special Cases and Considerations

Special cases and considerations for strict equality (===) include handling of NaN, signed zeros, and object comparisons as follows:

NaN values are never equal to themselves, making NaN === NaN false. This behavior differs from other values where self-comparison returns true (e.g., 5 === 5). For example:

```javascript

console.log(NaN === NaN); // false

```

JavaScript treats zero and signed zeros as equal, with signed zeros being equal only if both are numbers. This means +0 === -0 returns true, but +0 === '0' returns false due to type mismatch:

```javascript

console.log(+0 === -0); // true

console.log(+0 === '0'); // false

```

When comparing strings and numbers, strict equality requires explicit type conversion if the operands are not already of the same type. This ensures that identical numerical strings and their numeric representations are not considered equal, maintaining the distinction between data types.

Object comparisons treat references as distinct unless comparing identical objects. Primitive values are compared by converting objects to their primitive equivalents. This means:

```javascript

const obj1 = { foo: 'bar' };

const obj2 = { foo: 'bar' };

console.log(obj1 === obj2); // false

console.log(obj1.toString() === obj2.toString()); // true

```

These special cases highlight the importance of understanding strict equality's behavior when working with numbers, strings, and objects to ensure accurate value comparisons in JavaScript code.


## Best Practices

Strict equality (===) is the preferred choice when comparing values of different types, as it requires both value and type to match. This is particularly important for boolean values, where === allows for clear differentiation between true/1 and false/0, avoiding unexpected results that might occur with loose equality (==).

When comparing strings and numbers, explicit type conversion is necessary for accurate comparisons. For instance, "5" === 5 returns false, correctly identifying the difference between a string representation of a number and its numeric counterpart. This distinction maintains the integrity of data type separation in comparisons.

The operator's behavior with NaN is crucial for numerical comparisons requiring precise value matching. While both NaN === NaN and NaN == NaN return false, this consistency ensures that NaN values are handled correctly when using strict equality.

When comparing objects, === requires both the type and value to match. Two different instances of stdClass, for example, are not strictly equal, even if they contain identical properties. Developers should use === for comparing specific properties or the underlying data of objects, as demonstrated by the recommendation to use $this->assertSame($expected->getID(), $actual->getID()) for comparing object properties.

The === operator also correctly handles edge cases with signed zeros and object references. While +0 === -0 returns true due to JavaScript's handling of zero and signed zeros, === treats NaN values as distinct, with NaN === NaN returning false. This behavior ensures accurate comparisons in scenarios where preserving the distinction between different NaN values might be important.

