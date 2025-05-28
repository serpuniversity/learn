---

title: JavaScript Errors > Invalid for-of initializer

date: 2025-05-26

---


# JavaScript Errors > Invalid for-of initializer

JavaScript's for-of loop provides a convenient way to iterate over iterable objects. However, developers often encounter a "SyntaxError: invalid for-of initializer" when attempting to initialize the loop variable within the declaration. This article explains the underlying restrictions, common error scenarios, and provides solutions for correctly implementing for-of loops in JavaScript.


## Understanding the Invalid for-of Initializer Error

The 'invalid for-of initializer' error occurs due to specific restrictions on the syntax of for-of loop declarations. Unlike for-in loops, which silently ignore initializer expressions in non-strict mode, for-of loops strictly enforce correct syntax.


### Loop Declaration Syntax

A valid for-of loop declaration must conform to the following structure:

```javascript

for (let variable of iterable) {

  // loop body

}

```

The key restriction is that the declaration (e.g., `let variable`) cannot include an initializer expression (e.g., `variable = 0`). This is enforced to prevent syntax ambiguities and maintain clear semantics for iterable operations.


### Error Context and Examples

The error typically occurs when attempting to initialize the loop variable in the declaration. For example, the following code will produce a SyntaxError:

```javascript

const iterable = [10, 20, 30];

for (let val = 10 of iterable) {

  console.log(val);

}

```

The correct approach is to use a simple variable declaration without an initializer:

```javascript

const iterable = [10, 20, 30];

for (let val of iterable) {

  console.log(val);

}

```

This valid example correctly logs each value from the iterable, demonstrating proper for-of loop syntax.


## Common Error Scenarios

The 'invalid for-of initializer' error occurs when the loop variable declaration in a for-of loop contains an initializer expression. This behavior differs from for-in loops, which allow initializer expressions in non-strict mode but silently ignore them. For-of loops, however, strictly enforce correct syntax to prevent ambiguities in iterable operations.

Common error scenarios include attempting to initialize the loop variable with a value before iterating over the iterable. For example:

```javascript

const iterable = [10, 20, 30];

for (let val = 10 of iterable) {

  console.log(val);

}

```

This code will produce a SyntaxError because the `let val = 10` initializer is not allowed in for-of loop declarations. The correct approach is to use a simple variable declaration without an initializer:

```javascript

const iterable = [10, 20, 30];

for (let val of iterable) {

  console.log(val);

}

```

This valid example correctly logs each value from the iterable, demonstrating proper for-of loop syntax. The error message can vary between different JavaScript engines. V8-based systems typically report "SyntaxError: for-of loop variable declaration may not have an initializer," while Firefox reports "SyntaxError: a declaration in the head of a for-of loop can't have an initializer."

The error type is SyntaxError and occurs when the loop contains an initialization that is invalid inside for-of loops. This includes lexical declarations with initializers like `for (const i = 0 in obj)`, which are not allowed outside strict mode and will always produce a SyntaxError. The recommended approach for Array iteration is to use a traditional for loop instead of for-in loops:

```javascript

const arr = ["a", "b", "c"];

for (let i = 0; i < arr.length; i++) {

  console.log(arr[i]); // "a", "b", "c"

}

```

This structure correctly iterates over the array without causing syntax errors.


## Troubleshooting and Solutions

If you encounter a SyntaxError related to for-of loop initializers, the key issue usually lies in how you've declared your loop variable. The error occurs when you attempt to initialize the loop variable directly within the declaration, as shown in these common mistake examples:

```javascript

// Incorrect: initializer in for-of loop declaration

for (let item = {} of myArray) {

  console.log(item); // Throws SyntaxError

}

// Correct: simple variable declaration

for (let item of myArray) {

  console.log(item);

}

```

The error message can vary between JavaScript engines. V8-based systems will report "SyntaxError: for-of loop variable declaration may not have an initializer," while Firefox more clearly states "SyntaxError: a declaration in the head of a for-of loop can't have an initializer."

To troubleshoot these errors, start by reviewing your for-of loop declarations for any initializers or lexical declarations with initializers, such as `for (const i = 0 of iterable)`. These patterns will always produce a SyntaxError.

For cases where you need to track an index or perform additional operations before iteration, consider using a traditional for loop instead:

```javascript

// Incorrect: tracking index in for-of loop

for (let i = 0, i < myArray.length; i++) {

  console.log(myArray[i]);

}

// Correct: traditional for loop

for (let i = 0; i < myArray.length; i++) {

  console.log(myArray[i]);

}

```

If you specifically need to check a condition before iteration (e.g., ensuring an iterable is not empty), perform that check separately before entering the loop:

```javascript

if (!Array.isArray(myIterable)) return;

for (let elem of myIterable) {

  console.log(elem);

}

```

