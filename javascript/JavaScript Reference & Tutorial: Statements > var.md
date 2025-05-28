---

title: JavaScript Variables: Understanding the `var` Keyword

date: 2025-05-27

---


# JavaScript Variables: Understanding the `var` Keyword

JavaScript has evolved dramatically since its 1995 introduction, yet one aspect remains largely unchanged: the `var` keyword for variable declaration. While modern development favors `let` and `const`, understanding `var` is crucial for working with legacy code and comprehending JavaScript's variable scoping rules. This article explores `var`'s fundamental behavior, from basic declarations to its quirks and limitations. You'll learn how to use `var` effectively while recognizing when its older characteristics become potential pitfalls. Most importantly, you'll discover why modern JavaScript development has moved beyond `var` in favor of more controlled scope and better variable management practices.


## Variable Declaration with `var`

The `var` keyword in JavaScript declares variables that allow both assignment and reassignment of values. Basic variable declaration follows the syntax:

```javascript

var variableName = initialValue;

```

Variables declared with `var` can store any JavaScript data type, with undefined as the default initial value if nothing is assigned:

```javascript

var x;

console.log(x); // Output: undefined

x = 10;

console.log(x); // Output: 10

```

Multiple variables can be declared in a single statement using commas:

```javascript

var a = 1, b = 2, c = 3;

```

The `var` keyword also enables concise assignment and reassignment:

```javascript

let dog = "snickers";

dog = "hugo"; // Valid reassignment

```


## Variable Initialization and Assignment

The `var` keyword in JavaScript allows for multiple variable declarations in a single statement, using commas to separate individual variable names. For example:

```javascript

var a, b; a = 70; b = 80;

```

This results in:

```javascript

The value of a is: 70

The value of b is: 80

```

The assignment operator (=) is used to assign values to variables declared with `var`. This operator assigns the value of an expression to a variable, overwriting any previous value. For instance:

```javascript

var name = "Madison";

name = "Ben"; // Reassigns the variable

```

If a variable is declared but not immediately assigned a value, it defaults to `undefined`. This can be explicitly demonstrated as follows:

```javascript

var year;

console.log(year); // Output: undefined

year = 2020;

console.log(year); // Output: 2020

```

The `var` keyword enables both arithmetic operations and string concatenation using the `+` operator. When adding numbers, it performs mathematical addition. When adding strings, it concatenates them. Numbers in quotes are treated as strings, resulting in concatenation:

```javascript

let x = "5" + 2 + 3;

console.log(x); // Output: "523"

```

In JavaScript, the dollar sign ($) and underscore (_) are valid characters in variable names. While their use is less common, the dollar sign is sometimes employed as an alias for the main function in JavaScript libraries, and underscores are a valid character in variable names:

```javascript

var $credit;

var _name;

```

While a variable declared with `var` can be used before its actual initialization, as demonstrated in the examples, modern best practices recommend against this usage. The `let` and `const` keywords offer more controlled scope and immutability features that make the code more maintainable and predictable.


## Variable Reuse and Scope

In JavaScript, variables declared with `var` can be used before their actual declaration, a feature known as hoisting. This behavior allows for more flexible code structure but can also lead to unexpected results if not understood properly. When a `var`-declared variable is accessed before its actual declaration, it defaults to `undefined`, as demonstrated in these examples:

```javascript

console.log(myVariable); // Output: undefined

var myVariable = 10;

```

This characteristic of `var` differs from modern JavaScript approaches, where variable references before declaration would typically result in an error. The use of `var` for variable declaration extends back to the language's early days, from 1995 to 2015, when it was the only keyword available for variable declaration.

The global scope of `var`-declared variables means they can be accessed anywhere in the program, though this practice is generally discouraged in favor of block-scoped variables declared with `let` or `const`. When using `var` in functions, the variable's scope is function-scoped rather than block-scoped, meaning it remains accessible throughout the function's execution and can be referenced both inside and outside the function's block structure. This can lead to different behaviors compared to block-scoped variables, which are only accessible within their specific block.


## Best Practices and Recommendations

Modern JavaScript development strongly advises against using the `var` keyword in favor of `let` and `const`, offering several advantages that promote more maintainable and predictable code. While `var` has been the only keyword available for variable declaration since JavaScript's inception in 1995, it has several limitations that make it less suitable for contemporary development practices:


### Better Scope Control with `let` and `const`

The `let` keyword introduces what's known as block scope, limiting variable accessibility to where they are declared. This differs from `var`, which has function scope, meaning variables remain accessible throughout the function's execution and can be referenced both inside and outside the function's block structure. This can lead to different behaviors compared to block-scoped variables, which are only accessible within their specific block.


### Immutable Values with `const`

`const` creates immutable variables, ideal for values that should not change, such as private keys, colors, or fonts. While `const` variables cannot be reassigned, this actually makes them more useful for setting constants, as demonstrated in the examples where constant arrays can be mutated through their properties while constant arrays can be modified through their methods.


### Error Prevention through Strict Mode

JavaScript's strict mode, introduced to address issues with undeclared variables, requires all variables to be declared with `var`, `let`, or `const`. In strict mode, attempting to use an undeclared variable results in an error, preventing the "automatic variable creation" behavior that existed in older browsers. This change addresses the security risks and maintainability issues associated with implicit variable declaration.


### Enhanced Code Organization

Modern JavaScript development guidelines recommend declaring variables using `const` for new variables, assuming they won't need updating, and converting to `let` only when needing to change a variable's value. This approach helps prevent accidental overwriting and promotes more structured, predictable code.


### Best Practices

The recommended approach today is to use `const` for values that should remain constant and `let` for variables that need to change. This aligns with JavaScript's trend toward more explicit variable declarations and better scope control, ensuring that variables are properly scoped to their intended usage while preventing common pitfalls like accidental global variable creation.

