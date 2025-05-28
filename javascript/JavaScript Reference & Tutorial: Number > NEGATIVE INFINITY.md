---

title: Number.NEGATIVE_INFINITY Property in JavaScript

date: 2025-05-26

---


# Number.NEGATIVE_INFINITY Property in JavaScript

In JavaScript, the Number.NEGATIVE_INFINITY property represents negative infinity, a value lower than any other number. Understanding this concept is crucial for developers working with numerical boundaries and error handling in their applications. This article explores the properties and behavior of NEGATIVE_INFINITY, including its comparison and numerical operations, and provides practical examples of its usage in JavaScript code.


## Understanding NEGATIVE_INFINITY

The Number.NEGATIVE_INFINITY property in JavaScript represents negative infinity, which is a value lower than any other number. When accessed using Number.NEGATIVE_INFINITY, it returns -Infinity. This property is a static attribute of the Number object and cannot be accessed directly from a variable using the variable.NEGATIVE_INFINITY syntax.


### Basic Properties and Behavior

The property's value is the same as the negative value of the global Infinity property, following IEEE 754 standards for floating-point arithmetic. When divided by any positive value except POSITIVE_INFINITY, the result is NEGATIVE_INFINITY. However, dividing by either NEGATIVE_INFINITY or POSITIVE_INFINITY yields NaN (Not a Number).


### Comparison and Numerical Operations

Any positive value, including POSITIVE_INFINITY, multiplied by NEGATIVE_INFINITY results in NEGATIVE_INFINITY. Similarly, any negative value multiplied by NEGATIVE_INFINITY produces POSITIVE_INFINITY. Dividing zero by NEGATIVE_INFINITY returns -0, while dividing NEGATIVE_INFINITY by itself or POSITIVE_INFINITY results in NaN. The product of NaN and NEGATIVE_INFINITY also equals NaN, adhering to IEEE 754 rules for floating-point operations.


## Properties and Behavior

The value of Number.NEGATIVE_INFINITY is the same as the negative value of the global Infinity property, adhering to IEEE 754 standards for floating-point arithmetic. This property behaves uniquely in comparison to mathematical infinity, with specific rules governing its interactions in arithmetic operations.

When divided by any positive value except POSITIVE_INFINITY, NEGATIVE_INFINITY maintains its value. Dividing it by itself or POSITIVE_INFINITY results in NaN (Not a Number), while division by any negative value (other than NEGATIVE_INFINITY) yields positive infinity. Similar to positive infinity, multiplying NEGATIVE_INFINITY by NaN also produces NaN, and multiplying zero by NEGATIVE_INFINITY generates NaN.

Arithmetic operations involving NEGATIVE_INFINITY produce specific outcomes based on the signs of the operands. Any positive value multiplied by NEGATIVE_INFINITY results in NEGATIVE_INFINITY, while any negative value produces POSITIVE_INFINITY. For instance, NEGATIVE_INFINITY divided by 123 results in negative infinity, and dividing negative infinity by -123 produces positive infinity. The product of 0 and NEGATIVE_INFINITY equals NaN, and multiplying NaN by NEGATIVE_INFINITY also yields NaN. This property further demonstrates its distinct behavior from traditional mathematical concepts.

The property's value is consistent across both static and instance access, though attempts to use x.NEGATIVE_INFINITY where x is a variable will return undefined. Its implementation allows for reliable detection of overflow conditions, with specific functions utilizing this property to return finite numbers in success cases where NaN would be more appropriate.


## Accessing the Property

The property is accessed using the static syntax Number.NEGATIVE_INFINITY and cannot be accessed directly from a variable using the variable.NEGATIVE_INFINITY syntax. This restriction ensures that the property can only be accessed using its defined static context.

Attempting to use the variable-syntax form (x.NEGATIVE_INFINITY where x is a variable) returns undefined, as demonstrated in the examples provided. This design choice prevents accidental misuse and ensures consistent behavior across different usage contexts.

The property's value is the same as the negative value of the global Infinity property, adhering to IEEE 754 standards for floating-point arithmetic. This consistent implementation across browsers allows reliable detection of overflow conditions, with specific functions using this property to return finite numbers in success cases where NaN would be more appropriate.


## Examples and Usage

The value of Number.NEGATIVE_INFINITY is "-?" according to the product documentation, though this is printed as "-Infinity" when calling .toString() or .valueOf(). The property represents a value lower than any other number and allows JavaScript to handle operations that would otherwise produce overflow.

Creating a number less than Number.MAX_VALUE * 2 will result in NEGATIVE_INFINITY, as demonstrated in the example where smallNumber = -Number.MAX_VALUE * 2 sets smallNumber to NEGATIVE_INFINITY before further processing. This usage pattern enables better error handling in calculations where negative infinity values are meaningful, though the official documentation notes that NaN would be more appropriate in success cases where a finite number is needed.

Dividing by zero returns infinity, as mentioned in the product documentation. This behavior aligns with mathematical expectations, and division of a positive number by positive infinity results in positive zero, while dividing a negative number by positive infinity produces negative zero. The division results can be observed directly using built-in functions: Number.NEGATIVE_INFINITY.toString() prints "-?" and Number.NEGATIVE_INFINITY.valueOf() prints "-Infinity".


## Browser Support

The Number.NEGATIVE_INFINITY property is supported in all modern browsers, including Chrome, Edge, Firefox, Safari, and Opera, according to multiple documentation sources. This cross-browser compatibility demonstrates its widespread use across JavaScript environments, with initial support dating back to ECMAScript1 (JavaScript 1997).

The property behaves as an unmodifiable constant, returned as -Infinity when accessed through Number.NEGATIVE_INFINITY. Attempts to use the variable-based syntax (x.NEGATIVE_INFINITY where x is a variable) result in undefined, maintaining a clear distinction between the static property and instance-based access.

Developers utilize this property through functions like safeDivide, which handles division by zero by returning -Infinity to signal an undefined result. In error detection, the property serves as a reliable starting point for finding maximum values, as demonstrated in the setEqualHeight function, which initializes comparisons with -Infinity. This application ensures that any encountered value will be considered larger, facilitating accurate maximum detection.

