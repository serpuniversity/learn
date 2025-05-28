---

title: JavaScript Conditional Statements: if...else

date: 2025-05-27

---


# JavaScript Conditional Statements: if...else

JavaScript's conditional statements offer powerful tools for making decisions within your code. Whether you're validating user input, controlling the flow of an application, or performing complex logical operations, these statements enable precise control over what actions your program takes. This guide walks you through the basic and extended uses of if statements, showing how to evaluate conditions, handle multiple cases, and create flexible, responsive JavaScript applications.


## Basic if Statement

The basic if statement in JavaScript provides conditional execution based on a specified condition. When the condition evaluates to true, the associated code block is executed. The syntax follows the simple format:

```javascript

if (expression) {

  // statement(s) to be executed if expression is true

}

```

Note that if multiple statements are needed within the code block, they must be enclosed in curly braces `{}`. For example:

```javascript

let temperature = 23;

if (temperature >= 20) {

  console.log("The weather is pleasant.");

}

```

In this case, the message "The weather is pleasant." will be logged to the console because the condition `temperature >= 20` evaluates to true.

The if statement automatically converts the expression result to a boolean value, meaning that any non-zero, non-empty, and non-null value is treated as true. This includes numbers, strings, and non-null objects. Conversely, 0, "", null, undefined, and NaN are considered false.


## if...else Statement

The if...else statement in JavaScript provides a mechanism for executing alternative blocks of code based on whether a specified condition evaluates to true or false. The basic syntax extends the if statement with an additional else block:

```javascript

if (expression) {

  // statement(s) to be executed if expression is true

} else {

  // statement(s) to be executed if expression is false

}

```

The expression within parentheses is evaluated to produce a boolean value. If true, the code block following the if statement is executed. If false, the code block following the else statement is executed, if present. This structure allows for direct comparison between the outcomes of multiple conditions.

For example, the if...else statement can be used to determine user access based on password verification:

```javascript

let password = "securePass123";

let inputPassword = "securePass123";

if (inputPassword === password) {

  console.log("Access granted.");

} else {

  console.log("Access denied.");

}

```

The code checks if the input password matches the stored password. If there's a match, access is granted; otherwise, access is denied.


### Nested and Multiple Conditions

JavaScript supports extended conditional logic through nested if statements and multiple else if blocks. This allows evaluation of multiple conditions in sequence:

```javascript

let score = 85;

if (score >= 90) {

  console.log("Excellent!");

} else if (score >= 70) {

  console.log("Good job!");

} else if (score >= 60) {

  console.log("Passed.");

} else {

  console.log("Failed.");

}

```

In this example, the code first checks if the score is 90 or above. If not, it proceeds to check if the score is 70 or above, and so on, until a condition is met or all conditions are exhausted. This structure ensures that only one block of code is executed based on the score value.


## Nested and Multiple Conditions

Using nested if statements enables evaluation of multiple conditions within a single logical structure:

```javascript

let num = 10;

if (num > 0) {

  console.log('The number is positive.');

  if (num % 2 === 0) {

    console.log('The number is even.');

  } else {

    console.log('The number is odd.');

  }

} else {

  console.log('The number is not positive.');

}

```

Here, the outer if statement checks if the number is positive. If true, it proceeds to an inner if statement that determines whether the number is even or odd. This nested structure allows for more complex condition evaluation while maintaining clear logical flow.

Multiple else if statements enable sequential testing of conditions:

```javascript

let rating = 3;

switch (rating) {

  case 2:

    console.log('Not very good.');

    break;

  case 3:

    console.log('Average.');

    break;

  case 4:

    console.log('Good.');

    break;

  case 5:

    console.log('Excellent.');

    break;

  default:

    console.log('Unknown rating.');

}

```

This example demonstrates how a series of else if statements can evaluate different rating levels, with the appropriate message displayed based on the input value.

The syntax ensures that the first matching condition is executed:

```javascript

let time = 15;

if (time < 10) {

  console.log('Good morning');

} else if (time < 20) {

  console.log('Good day');

} else {

  console.log('Good evening');

}

```

In this sequence, the time is first checked against 10. If false, it proceeds to the next condition at 20, printing "Good day" since the current time of 15 falls within this range. The final else block would only execute if all preceding conditions were false.

