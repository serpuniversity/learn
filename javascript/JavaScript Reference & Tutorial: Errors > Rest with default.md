---

title: JavaScript Reference & Tutorial: Errors > Rest with Default

date: 2025-05-26

---


# JavaScript Reference & Tutorial: Errors > Rest with Default

In JavaScript, the combination of rest parameters and default parameter values appears straightforward: both features allow functions to handle variable numbers of arguments. However, these seemingly compatible tools intersect in a fundamental way that causes SyntaxErrors in the language. This article explores why a rest parameter cannot have a default value, examining the technical implementation details and their implications for JavaScript development. Through examples and analysis of browser implementation, we'll understand the limitations of combining these features and learn how to write more robust, maintainable JavaScript functions.


## Understanding Rest Parameters

A rest parameter always creates an array, making it incompatible with default values. This fundamental incompatibility causes a SyntaxError when attempting to assign a default value to a rest parameter.

Rest parameters work by collecting all remaining arguments into an array-like object. This means that a rest parameter always has an array as its value, regardless of how many arguments are passed to the function. As the MDN Web Docs explain, "When you use a rest parameter, the argument corresponding to that parameter becomes an array containing all the remaining arguments passed to the function."

Default parameters, on the other hand, allow setting a fallback value for a function parameter if no argument is provided or if the provided argument is undefined. The syntax for default parameters is `parameterName = defaultValue`.

The combination of these two features leads to the SyntaxError described in the documentation: "rest parameter may not have a default". As the MDN Web Docs note, "A rest parameter collects all remaining arguments and always creates an array. Having a default value for a rest parameter doesn't make sense, as rest parameters inherently create arrays."

This incompatibility is demonstrated in the example provided, where attempting to set a default value for a rest parameter results in a SyntaxError:

```javascript

const describePerson = (name, ...traits = ['a nondescript individual']) => `Hi, ${name}! You are ${traits.join(', ')}`;

```

In this case, Edge browser specifically throws a SyntaxError, while Chrome provides a more descriptive error message. The underlying issue is that the rest parameter `...traits` always creates an array, making the default value assignment incompatible with the language syntax.


## Syntax Error Explanation

In JavaScript, rest parameters and default parameter features serve distinct purposes but cannot be combined due to fundamental language design. A rest parameter collects all remaining arguments into an array-like object, making it incompatible with the intended use of default values.

The core issue arises from how these features are implemented in JavaScript's language design. According to the MDN Web Docs, "A rest parameter collects all remaining arguments and always creates an array. Having a default value for a rest parameter doesn't make sense, as rest parameters inherently create arrays."

This leads to specific error behaviors across different browsers. While modern browsers generally throw a SyntaxError when attempting to assign a default value to a rest parameter, the exact message and behavior can vary. As noted by developers testing this feature, Edge browser specifically throws a SyntaxError, while Chrome provides more detailed error messages.

The inconsistency in error handling across browsers highlights the fundamental incompatibility between these features. Attempting to use a default value with a rest parameter results in a clear violation of JavaScript's syntax rules, as the rest parameter will always create an array regardless of any default value specified.

Given this fundamental compatibility issue, developers seeking to provide default values in functions with variable argument counts should use regular parameters instead of rest parameters. Modern JavaScript development practices strongly recommend using default parameter values to improve code readability and maintainability while avoiding the limitations of rest parameter usage.


## Incorrect Implementation Example

As demonstrated in the code snippet, attempting to assign a default value to a rest parameter results in a SyntaxError across browsers. The function `sayHi` illustrates this issue effectively:

```javascript

const sayHi = (greeting = 'Hi, ', ...names) => {

  names.forEach(name => console.log(greeting + name));

};

sayHi('Good morning, ', 'Alice', 'Bob');

sayHi('How are you, ', 'Charlie');

sayHi(); // This line would throw an error in Edge, while Chrome provides a more descriptive message

```

The function `sayHi` accepts an optional greeting parameter and an arbitrary number of names using a rest parameter. Attempting to call `sayHi()` without arguments results in a SyntaxError, as seen in Edge browser. While Chrome provides a more detailed error message, both browsers enforce the rule that rest parameters cannot have default values due to their inherent array creation.

The technical implementation details explain why this error occurs. The rest parameter `...names` always creates an array, making it incompatible with default values. This fundamental incompatibility is why developers must treat rest parameters and default parameters as distinct features with separate use cases. Modern JavaScript development strategies recommend using default parameter values for named parameters and rest parameters for handling variable argument counts.


## Browser Compatibility

Edge browser specifically implements this behavior by throwing a SyntaxError when attempting to assign a default value to a rest parameter. This differs from other browsers, which may provide more descriptive error messages.

According to the documentation, "rest parameter may not have a default" is a well-defined syntax error that affects all modern browsers. While Chrome provides detailed error messages, other browsers implement this as a strict syntax check, matching Edge's approach of throwing a SyntaxError.

This implementation detail is consistent with the underlying JavaScript language design, where rest parameters inherently create arrays. The error behavior serves as a clear indication that combining rest parameters with default values conflicts with JavaScript's syntax rules and language semantics.


## Best Practices

To avoid SyntaxErrors, developers should follow these best practices:

- Use default values for named parameters: This allows setting fallback values for function parameters that may not receive an argument. The syntax is simple and effective, as demonstrated in the example provided by MDN Web Docs:

```javascript

function multiply(a, b) {

  return a * b;

}

// Using default values

multiply(5, 2); // 10

multiply(5); // NaN

// Providing custom values

multiply(5, 2); // 10

multiply(5); // 10

```

- Avoid setting default values for rest parameters: As noted by the developers in their console testing, attempting to assign a default value to a rest parameter results in a SyntaxError across browsers. The correct approach is to use named parameters for default values and rest parameters for handling variable argument counts:

```javascript

const describePerson = (name, ...traits) => `Hi, ${name}! You are ${traits.join(', ')}`;

describePerson('John Doe', 'the prototypical placeholder person'); // => "Hi, John Doe! You are the prototypical placeholder person"

describePerson('Alice', 'a friend', 'an explorer'); // => "Hi, Alice! You are a friend, an explorer"

describePerson('Bob'); // => "Hi, Bob! You are undefined"

```

- Implement careful parameter referencing: When using default parameter initializers, ensure that earlier parameters can be referenced in later initializers. However, avoid referencing functions or variables declared in the function body, as this can lead to run-time ReferenceErrors:

```javascript

function processMarks([val1, val2, val3 = val1 + val2]) {

  console.log(val1, val2, val3);

}

processMarks([10, 20, 30]); // 10 20 30

processMarks([10, 20]); // 10 20 30

```

- Use destructuring for advanced argument handling: For functions that work with a variable number of arguments, combine rest parameters with array destructuring for enhanced functionality and readability. This approach demonstrates the flexibility of modern JavaScript function parameters while avoiding common pitfalls:

```javascript

function calculateAverage(...marks) {

  const [firstScore, secondScore, thirdScore] = marks;

  return (firstScore + secondScore + thirdScore) / 3;

}

console.log(calculateAverage(90, 85, 95)); // 90

console.log(calculateAverage(90, 85)); // NaN

```

