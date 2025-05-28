---

title: JavaScript Inequality Operators

date: 2025-05-27

---


# JavaScript Inequality Operators

In JavaScript, comparing values requires understanding the nuances of the language's type system. The equality and inequality operators handle value comparisons in different ways, offering both convenience and potential pitfalls. This article explores the != and !== operators, explaining how they work, their differences, and when to use each. You'll learn how these operators handle type coercion, compare mixed data types, and interact with special values like null and undefined. Understanding their behavior is crucial for writing reliable JavaScript code that avoids unexpected type conversion issues.


## Introduction to Inequality Operators

JavaScript's inequality operators, != and !==, compare values while handling the nuances of JavaScript's type system. The != operator represents "Loose Inequality," which means "Not Equal." It returns true when the values of the operands are not equal, performing type conversion if the operands are of different types. For example, 16 != '16' evaluates to false because 16 and '16' are considered equal due to type coercion.

The !== operator represents "Strict Inequality," meaning "Strictly Not Equal." This operator checks both value and data type without performing any type coercion, making it more reliable for comparison tasks where type consistency is important. For instance, 16 !== "16" would return true, as it requires both value and type to match between operands.

The soft inequality operator (!=) works by attempting type conversion for its operands before comparison. If either operand is a string that represents a number, JavaScript will convert the string to a number for comparison. The hard inequality operator (!==) first checks the data types of the operands before comparing their values, providing more predictable behavior in type-sensitive applications.


## Non-Strict Inequality (!=)

The != operator performs type coercion to compare values, making it useful for cases where values of different types might actually represent the same numeric quantity. For example, comparing a number with its string representation:

```javascript

16 != '16'; // Evaluates to false, as both the value and type match after coercion

```

When comparing operands of the same data type, the operator works as you would expect, returning true only if the values are different:

```javascript

16 != 17; // Evaluates to true

```

The operator's type coercion behavior extends to objects, treating two distinct object references as not equal unless their properties perfectly match:

```javascript

object1 != object2; // Evaluates to true for two different objects

object1 != object1; // Evaluates to false for the same object reference

```

It's important to note that while the != operator can be convenient for quickly checking for non-equality across different types, it may lead to unexpected results due to type coercion. In most cases, the === operator is recommended for its strict value and type checking, avoiding potential bugs related to automatic type conversions.


## Strict Inequality (!==)

The strict inequality operator (!==) checks both value and data type without performing type coercion, making it more reliable for comparison tasks where type consistency is important. For example, comparing the integer 5 with a string representation of the number 5:

```javascript

5 !== "5" // Evaluates to true

```

In this case, the operator requires both the value and type to match between operands, demonstrating its stricter comparison rules. The operator works as follows:

1. For number types: No type conversion occurs. The operator compares the values directly.

2. For mixed types: The operator requires both value and type to match for a true result. For example:

   ```javascript

   var1 = 0 // number

   var2 = false // string

   var1 !== var2 // Evaluates to true because the data types are different

   ```

The === operator provides a safer alternative to the == operator by requiring both value and type to match. This prevents the unexpected results that can occur due to automatic type conversions. For instance, comparing an integer and its string representation:

```javascript

16 === "16" // Evaluates to false, demonstrating strict type and value matching

```

While the loose inequality operator (!=) can be convenient for quickly checking for non-equality across different types, the strict inequality operator (!==) provides more reliable results unaffected by type coercion. This makes it the recommended choice in most cases where type consistency matters.


## Comparison Examples

The inequality operator (!=) performs type coercion to compare values, making it useful for cases where values of different types might actually represent the same numeric quantity. For example:

```javascript

16 != '16'; // Evaluates to false, as both the value and type match after coercion

```

When comparing operands of the same data type, the operator works as you would expect, returning true only if the values are different:

```javascript

16 != 17; // Evaluates to true

```

The operator's type coercion behavior extends to Boolean and number values, considering 0 as a falsy value. For example:

```javascript

0 != false; // Evaluates to false, as both the value and type match after coercion

```

JavaScript treats 0 and false as equivalent when comparing to Boolean values:

```javascript

0 != false; // Evaluates to false

1 != true;   // Evaluates to false

false != 0;  // Evaluates to false

true != 1;   // Evaluates to false

```

The inequality operator also handles null and undefined values properly:

```javascript

null != undefined; // Evaluates to false

```

When comparing numbers and strings that represent numbers, the operator will convert the string to a number for comparison:

```javascript

16 != ' 16 '; // Evaluates to false, after trimming the string and converting it to a number

```

This behavior extends to more complex values, where JavaScript's type conversion rules come into play. For instance:

```javascript

{} != '[]'; // Evaluates to true, as they are different data types

{} != {};   // Evaluates to false, as they are the same data type

```

The strict inequality operator (!==) checks both value and data type without performing type coercion, providing more reliable comparison results. For example:

```javascript

5 !== "5" // Evaluates to true, as the data types are different

```

When comparing operands of the same data type, the operator requires both value and type to match for a true result:

```javascript

16 !== 16; // Evaluates to false, as both value and type are the same

```

The operator works as follows for different data types:

- For number types: No type conversion occurs, comparing values directly

- For string and number combinations: The string is converted to a number if possible

- For Boolean and number values: True converts to 1, false converts to 0

- For mixed types: The operator requires both value and type to match

For example:

```javascript

16 !== '16'; // Evaluates to false, as the types are different even though the values match

16 !== 16;   // Evaluates to false, as both value and type are the same

false !== 0; // Evaluates to true, as the data types are different

{} !== {};   // Evaluates to false, as both value and type are the same

null !== false; // Evaluates to true, as the data types are different

```


## Summary of Inequality Operators

JavaScript's inequality operators, != and !==, offer developers flexible ways to compare values while navigating the language's nuanced type system. The != operator, or "soft inequality," performs type coercion before comparison, making it useful for cases where different types might represent the same numeric value. For example:

```javascript

16 != '16' // false, as both the value and type match after coercion

```

The !== operator, or "hard inequality," avoids type coercion entirely, requiring both value and type to match for a true result:

```javascript

5 !== "5" // true, as the data types are different

```

Key points to remember:

- For number types, the != operator compares values directly without conversion. In contrast, the !== operator also checks the data type.

- Mixed types are converted to a common type before comparison. For instance, comparing a number and a string will result in the string being converted to a number.

- Booleans and numbers are treated specially: true converts to 1, false converts to 0, and 0 is considered equivalent to false in comparisons.

- null and undefined are distinct: null == undefined returns true, but null === undefined is false.

- The === and !== operators provide strict value and type checking, while the == and != operators perform implicit type conversions that can lead to unexpected results.

