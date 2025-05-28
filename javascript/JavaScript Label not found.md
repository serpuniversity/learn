---

title: JavaScript Error: Label Not Found

date: 2025-05-26

---


# JavaScript Error: Label Not Found

In JavaScript, controlling loop flow can sometimes lead to unexpected errors, especially when working with labeled statements. This article explores the "Label Not Found" error, explaining its causes and behavior across different browsers. We'll examine how labels are used with break and continue statements, their scope restrictions, and provide best practices for implementation. You'll learn about their proper usage patterns, common pitfalls to avoid, and discover why understanding these fundamentals is crucial for writing maintainable JavaScript code.


## Understanding the Label Not Found Error

The error arises specifically when a break or continue statement attempts to reference a label that does not exist, resulting in a SyntaxError. This is distinct from other JavaScript errors and has specific behavior across different browsers: V8-based environments report "SyntaxError: Undefined label 'label'", Firefox returns "SyntaxError: label not found", and Safari indicates "SyntaxError: Cannot use the undeclared label 'label'".

Labels in JavaScript have limited utility, restricted to use with break and continue statements. They enable controlled loop flow but cannot be used as general goto statements, maintaining strict scope restrictions within the program. To illustrate proper usage, consider the following examples:

```javascript

// Correct usage

start: {

  console.log("Hello, world!");

  if (Math.random() > 0.5) {

    break start;

  }

  console.log("Maybe I'm logged");

}

```

```javascript

// Incorrect usage

start: console.log("Hello, world!");

console.log("Do it again");

break start; // This will generate the 'label not found' error

```

These examples demonstrate how labels should be used to control loop flow, exiting only the labeled block rather than terminating the entire program.


## Label Usage in JavaScript

Labels in JavaScript are limited to use with break and continue statements, and can only be jumped to from a statement contained within the labeled statement. They cannot be accessed from anywhere in the program, preventing their use as general goto statements.

The syntax for labeled statements requires identifiers that are not reserved words, followed by a statement. The break statement can be used within any labeled statement, while continue can be used within labeled looping statements. These labels function similarly to variables, available only within the scope of the labeled statement.

JavaScript supports multiple labels per statement, all of which are functionally equivalent. The labels allow for complex control flow patterns, such as selectively breaking out of nested loops or continuing execution at specific points within loops.

For example, labeled continue statements can be used to skip specific iterations in nested loops:

```javascript

loop1: for (let i = 0; i < 3; i++) {

  loop2: for (let j = 0; j < 3; j++) {

    if (i === 1 && j === 1) {

      continue loop1;

    }

    console.log(`i = ${i}, j = ${j}`);

  }

}

```

This code will output:

```

i = 0, j = 0

i = 0, j = 1

i = 0, j = 2

i = 1, j = 0

i = 2, j = 0

i = 2, j = 1

i = 2, j = 2

```

The labeled break statement allows for selective termination of loops:

```javascript

let i, j;

loop1: for (i = 0; i < 3; i++) {

  loop2: for (j = 0; j < 3; j++) {

    if (i === 1 && j === 1) {

      break loop1;

    }

    console.log(`i = ${i}, j = ${j}`);

  }

}

```

This loop will output:

```

i = 0, j = 0

i = 0, j = 1

i = 0, j = 2

i = 1, j = 0

i = 2, j = 0

i = 2, j = 1

i = 2, j = 2

```

Function declarations can be labeled in non-strict code, though this syntax is deprecated and should not be used in strict mode or with generator functions and async functions, which cannot be labeled in either strict or non-strict environments.


## Correct Label Usage Examples

Labels in JavaScript can be used with both break and continue statements, but their primary functionality is to control the flow of loops. The correct usage pattern involves using the break statement to exit the labeled block rather than the entire program.

This can be demonstrated through several valid examples, such as selectively breaking out of nested loops:

```javascript

loop1: for (let i = 0; i < 3; i++) {

  loop2: for (let j = 0; j < 3; j++) {

    if (i === 1 && j === 1) {

      continue loop1;

    }

    console.log(`i = ${i}, j = ${j}`);

  }

}

```

This loop will output:

```

i = 0, j = 0

i = 0, j = 1

i = 0, j = 2

i = 1, j = 0

i = 2, j = 0

i = 2, j = 1

i = 2, j = 2

```

Similarly, labeled break statements allow for selective termination of loops:

```javascript

let i, j;

loop1: for (i = 0; i < 3; i++) {

  loop2: for (j = 0; j < 3; j++) {

    if (i === 1 && j === 1) {

      break loop1;

    }

    console.log(`i = ${i}, j = ${j}`);

  }

}

```

This code will output:

```

i = 0, j = 0

i = 0, j = 1

i = 0, j = 2

i = 1, j = 0

i = 2, j = 0

i = 2, j = 1

i = 2, j = 2

```

Best practices for using labels in modern JavaScript development emphasize ensuring proper accessibility through screen reader support, maintaining clear label text, and using modern DOM methods for label manipulation. This includes correctly associating labels with form controls using the `for` attribute and managing label text updates based on user interactions or input validation.


## Label Handling Across Development Environments

The label handling in Salesforce Aura Components demonstrates several complexities. When using namespace for labels, Salesforce automatically removes it, keeping only 'c'. However, during package building, Salesforce inconsistently replaces 'c' with the namespace, though this behavior is not observed in the author's development process using SFDX and git with an IDE.

Label references in Aura Components behave differently based on user locale. The framework can only send labels determined at runtime, with static references evaluated at compile time and sent to the client. Using `$A.get()` with dynamically determined labels results in an empty string, while syntax like `$Label.c." + day` cannot be parsed by the framework.

To address these challenges, developers can use `$A.getReference()` to force the framework to fetch dynamic labels from the server. Example usage shows setting a variable to the reference of a dynamically determined label and then setting a component attribute from that reference. The solution effectively resolves intermittent failures with dynamic labels, though the author notes this specific approach was unnecessary in their static label scenario.


## Label Best Practices

Best practices for working with labels in JavaScript focus on ensuring proper accessibility through screen reader support, maintaining clear label text, and using modern DOM methods for label manipulation.

To ensure accessibility, developers should use the `for` attribute to associate labels with form controls. This approach helps screen readers correctly map text to input fields, enhancing usability for users with visual impairments. JavaScript can further improve accessibility by dynamically updating labels based on user interactions or input validation. Practical applications include providing immediate feedback, guiding user input, and reflecting changes in the form, such as indicating required fields or displaying error messages.

For effective label management, developers can use modern DOM methods like `querySelector` and `getElementById` to interact with form elements. The following code snippet demonstrates selecting a label using the `querySelector` method:

```javascript

let label = document.querySelector('label[for="email"]');

console.log(label.textContent);

```

These methods allow developers to dynamically access and manipulate labels, supporting improved user interaction and form functionality. The `getElementsByTagName` method can also be used to iterate over all label elements in the document:

```javascript

let labels = document.getElementsByTagName('label');

for (var i = 0; i < labels.length; i++) {

  console.log(labels[i].textContent);

}

```

To maintain consistent and clear label text, developers should provide descriptive identifiers that accurately represent the input fields they control. This best practice ensures users understand what information is required and can easily locate the appropriate form elements.

