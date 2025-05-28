---

title: Using nullish coalescing and optional chaining operators in JavaScript

date: 2025-05-27

---


# Using nullish coalescing and optional chaining operators in JavaScript

In JavaScript, handling null and undefined values is crucial for writing robust and maintainable code. This article explains how to use two key operators—nullish coalescing and optional chaining—to safely access object properties and provide default values. These operators help prevent errors and make your code more concise, particularly when working with complex data structures and optional function return values. You'll learn when and how to use these operators to handle missing function arguments, safely access nested properties, and prevent type errors, with examples demonstrating their proper application and behavior.


## Nullish Coalescing Operator (??)

The nullish coalescing operator works by returning the right-hand side operand when the left-hand side operand is null or undefined, and otherwise returning the left-hand side operand. This operator treats null and undefined as specific values, similar to the optional chaining operator (?.), which allows safe property access by returning undefined when accessing a non-existent property or null value.

The operator behaves as a short-circuiting operator, meaning it does not evaluate the right-hand side expression if the left-hand side proves to be neither null nor undefined. This characteristic is significant when the evaluation has side effects and allows defining default values for cases where a more specific value is not available (MDN Web Docs).

Unlike the OR operator (||), which returns any falsy value, the nullish coalescing operator specifically returns only null and undefined values. This distinction makes it particularly useful for providing defaults while preserving other falsy values, including 0 and empty strings (MDN Web Docs).

Common use cases include handling missing function arguments and setting default values in object properties. For example, in a function that logs a greeting, the operator can provide a guest name if no specific name is provided (MDN Web Docs).

When combined with the optional chaining operator (?.), nullish coalescing allows treating undefined and null values as valid inputs while providing fallbacks for missing properties (MDN Web Docs). This combination enables safer property access and more robust default value assignments without the issues associated with traditional OR operator usage (What Is It - nullish coalescing operator??).


## Optional Chaining Operator (?.)

The optional chaining operator (?.) returns undefined if the object being accessed is either null or undefined, preventing potential errors that would occur with traditional property access methods. This behavior makes it particularly useful for safely handling potentially missing object references.

When applied to function calls, the operator treats a returned value of null or undefined as the terminating condition, similar to a failed property access. This alignment with nullish values allows for concise error handling while maintaining readability.

The operator supports both dot and bracket notation for property access, enabling flexible and consistent null-safe operations across different data structures. For example, the expression `obj.first?.second` will return undefined if `obj` is null, `obj.first` is undefined, or `obj.first.second` does not exist, while allowing the rest of the property chain to evaluate when possible.

Common applications include safely accessing nested properties in complex object structures and handling optional function return values. These capabilities make the optional chaining operator a valuable addition to modern JavaScript development, particularly when working with dynamic or potentially incomplete data sources.


## Common Use Cases

The nullish coalescing operator (??) and optional chaining operator (?.) help developers safely access object properties and provide default values. When combined, these operators enable concise and efficient data handling (MDN Web Docs).


### Handling Missing Function Arguments

For function parameters, these operators allow setting default values while preserving other falsy inputs such as 0 and empty strings (MDN Web Docs). For example:

```javascript

function greet(name = {}, guest = "friend") {

  return `Hello, ${name ?? guest}!`;

}

console.log(greet({ firstName: "Alice" })); // "Hello, Alice!"

console.log(greet()); // "Hello, friend!"

```


### Nested Property Access

The optional chaining operator makes it straightforward to access deeply nested properties without risking errors (MDN Web Docs). Consider these sample properties:

```javascript

const user = {

  profile: {

    address: {

      street: "123 Main Street",

      city: "Anytown"

    }

  }

};

console.log(user.profile?.address?.city ?? "Unknown city"); // "Anytown"

console.log(user.profile?.bio ?? "No biography available"); // "No biography available"

```


### Destructuring and Assignment

When working with complex data structures, these operators simplify property extraction and assignment. For instance:

```javascript

const inventory = {

  books: [

    { name: "JavaScript Patterns", author: "Stoyan Stefanov" }

  ],

  electronics: [

    { name: "Smartphone", price: 599 }

  ]

};

const { books, electronics = [] } = inventory;

console.log(books[0]?.name ?? "No title available"); // "JavaScript Patterns"

console.log(electronics[0]?.price ?? 0); // 599

```


### Error Prevention and Default Values

These operators prevent `TypeError` exceptions when accessing properties of `null` or `undefined` objects, making them essential for robust JavaScript development (MDN Web Docs). Here's an example function that handles optional inputs safely:

```javascript

function displayInfo(user) {

  const { name, address: { street, zip } } = user || { name: "Guest", address: null };

  console.log(`${name}, ${street ?? "Unknown street"}, ${zip ?? "N/A"}`);

}

displayInfo({ name: "Alice", address: { street: "123 Main St", zip: 10001 } });

displayInfo({ name: "Bob" }); // "Bob, , N/A"

displayInfo({}); // "Guest, Unknown street, N/A"

```


## Operator Precedence and Usage

In JavaScript, the nullish coalescing operator (??) and optional chaining operator (?.) have specific precedence rules that must be understood to write correct expressions. These operators have a right-associativity property, meaning they bind more tightly to their operands than to subsequent operators. However, when combined with arithmetic, comparison, or assignment operators, they evaluate from left to right.

The short-circuit evaluation behavior of these operators means that when used in expressions, they prioritize their internal evaluation before considering higher-precedence operators. For example, in the expression `x ??= f()`, the nullish coalescing assignment operator is evaluated first, checking if `x` is null or undefined before attempting an assignment. If `x` is null or undefined, the right-hand side `f()` is evaluated and assigned to `x`.

When used with other operators, it's important to consider the evaluation process. For example, in the expression `x ?? f() + y`, the nullish coalescing operator evaluates `x` first. If `x` is null or undefined, `f()` is evaluated and added to `y`. If `x` is defined, only `y` is evaluated and added to `x`.

Understanding these rules is crucial for writing robust JavaScript code that correctly handles null and undefined values while performing complex operations. Developers should test expressions with different operand combinations to ensure the expected behavior.


## Comparison with OR Operator

The nullish coalescing operator (??) provides a more precise alternative to the OR operator (||) when dealing with falsy values. While the OR operator returns any falsy value (including 0 and empty strings) when the left-hand operand is falsy, the nullish coalescing operator specifically returns only null and undefined values, making it particularly useful for default value scenarios where these are the only valid missing values (MDN Web Docs, What Is It - nullish coalescing operator??).

When comparing the two operators, the key distinctions become apparent through their handling of different falsy values:

- The OR operator returns any falsy value (including 0, false, and empty strings) when the left-hand operand is falsy, making it less suitable for scenarios where specific values need to be preserved (MDN Web Docs).

- In contrast, the nullish coalescing operator treats null and undefined as distinct states, returning the right-hand operand only when the left-hand operand matches one of these specific nullish values (MDN Web Docs, What Is It - nullish coalescing operator??).

A practical example demonstrates these differences:

```javascript

let count = 0;

let defaultCount = 100;

console.log(count ?? defaultCount); // 0

console.log(count || defaultCount); // 100

```

In this case, the nullish coalescing operator correctly preserves the 0 value of count, while the OR operator incorrectly treats it as falsy and returns the defaultCount value (MDN Web Docs).

The nullish coalescing operator's ability to distinguish between null and undefined values enables more precise type checking and default value assignment. This capability makes it particularly valuable in scenarios where 0 or empty strings represent meaningful data, allowing developers to provide default values while preserving these distinct data points (MDN Web Docs).

