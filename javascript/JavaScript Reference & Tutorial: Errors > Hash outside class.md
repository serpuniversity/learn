---

title: Understanding JavaScript Hash Characters in Class Context

date: 2025-05-26

---


# Understanding JavaScript Hash Characters in Class Context

In JavaScript, the humble hash character (#) takes on a uniquely powerful role when used within class definitions. Unlike its common uses elsewhere in programming, this syntax creates private fields that encapsulate data and behavior in a way traditional class properties cannot. By examining both the technical implementation and common usage scenarios, we'll uncover how this seemingly simple syntax revolutionizes JavaScript class design while preventing the very issues it solves.


## Hash Characters in JavaScript

The hash (`#`) character in JavaScript serves a unique purpose when used within class definitions, allowing developers to create private fields that encapsulate data and behavior. Unlike regular class properties, which can be accessed, modified, or deleted by external code, private fields created with the hash syntax maintain their encapsulation directly within the class.

When a class includes a property with the `#` prefix, such as `#privateField`, it creates a private field that cannot be accessed from outside the class body. This differs from traditional private properties, which would require additional setup and could recreate functions for each instance. Modern JavaScript's private field implementation maintains true privacy by storing these properties in a hidden internal space that is inaccessible to external scripts.


### Common Usage Scenarios


#### Class Definitions and Private Fields

```javascript

class SecureBox {

  #content;

  constructor(value) {

    this.#content = value;

  }

  getContent() {

    return this.#content;

  }

}

```

In this example, the `#content` field is encapsulated within the SecureBox class. Attempting to access or modify `this.#content` from outside the class will result in a syntax error, demonstrating the private field's isolation from external code.


#### Private Fields vs Public Fields

```javascript

class Box {

  constructor(content) {

    this.content = content; // public field

  }

}

const box = new Box('hello');

console.log(box.content); // "hello"

box.content = 'changed'; // modifying public field

console.log(box.content); // "changed"

delete box.content; // deleting public field

console.log(box.content); // undefined

```

In contrast, a private field within the same class structure would prevent direct modification or deletion, illustrating the privacy benefits of the hash syntax.


### Error Handling and Best Practices

Attempting to use a hash character outside of a class context will result in a "SyntaxError: Unexpected '#' used outside of class body". To avoid this error, ensure that all hash characters are properly placed within class definitions or as part of private field declarations. Following these guidelines will help maintain clean, maintainable code while leveraging JavaScript's private field capabilities effectively.


## SyntaxError: Unexpected '#' used outside of class body

The "SyntaxError: Unexpected '#' used outside of class body" error occurs specifically when a hash symbol (#) is encountered in JavaScript code that is not within a class declaration. This error message indicates that the hash character has been used in an unexpected context, where it is not valid according to JavaScript syntax rules.


### Common Causes and Solutions


#### Code Moving or Repositioning

One frequent cause of this error is the relocation of code that originally belonged within a class declaration. For example, if private field declarations were moved out of a class, they would no longer be in the correct context to use the hash syntax. Correcting this requires moving the private field declarations back into the class body.


#### Hashbang Comments

The hash character can be used correctly in JavaScript as a hashbang comment at the beginning of a file. However, this usage is specific to the first line of a file and not valid anywhere else. If a hashbang comment appears on any line other than the first, it will cause this syntax error.


#### DOM Identifier Strings

When used in DOM selection methods like `document.querySelector`, hash characters require proper string delimiters (quotation marks). For instance, incorrectly written `document.querySelector(#some-element)` will trigger this error. The correct usage is `document.querySelector("#some-element")`.


### Moving Private Fields

Private fields created with the hash syntax must remain within the class body to maintain their encapsulation. Moving a private field from within a class to an external location will result in this error. To fix this, all hash character usage must remain within class definitions.


### Best Practices

To avoid encountering this error, developers should ensure that:

1. All hash characters are used within class declarations.

2. Private field declarations remain within their respective class bodies.

3. Hashbang comments (if used) appear only on the first line of the file.

4. DOM identifier strings always include proper string delimiters.

The error message points to a fundamental aspect of JavaScript's syntax design, where certain characters have specific semantic meanings (like the hash in class declarations). Understanding these rules and common pitfalls helps prevent runtime errors and maintains clean, maintainable code.


## Common Scenarios for the Error

Common scenarios leading to the "Unexpected '#' used outside of class body" error involve improper placement of hash characters and mismanagement of private fields. The primary context where hashes are valid is within class declarations for defining private fields. When encountered outside these contexts, the error indicates a syntax violation.

The error can occur in several common situations:


### Missing Quotation Marks

Incorrect usage can arise when string delimiters are forgotten, such as in DOM selection statements:

```javascript

document.querySelector(#some-element) // Incorrect

```

The proper usage requires enclosing the selector in quotation marks:

```javascript

document.querySelector("#some-element") // Correct

```


### Code Relocation

Moving class-related code can disrupt proper syntax. For example, private field declarations must remain within class bodies:

```javascript

class ClassWithPrivateField { #privateField; constructor() {} }

this.#privateField = 42; // Error: Unexpected '#' used outside of class body

```

To correct this, the field initialization must stay within the class definition:

```javascript

class ClassWithPrivateField { #privateField; constructor() { this.#privateField = 42; } }

```


### Incorrect Comment Usage

A less common but relevant scenario involves hashbang comments. While valid as the first line of a script, hashes on subsequent lines cause syntax errors:

```javascript


# This is a valid hashbang comment

console.log("Hello, world!"); // Error: Unexpected '#' used outside of class body

```

Maintaining proper syntax requires consistent use of quotation marks and correct placement within class declarations. Understanding these patterns helps developers avoid runtime errors and maintain clean, maintainable code.


## Private Fields and Class Design

Private class fields in JavaScript enable a form of encapsulation that traditional public fields do not support. Unlike regular class properties, which reside directly on the object instance and can be accessed, modified, or deleted by external code, private fields prefixed with the hash (#) symbol maintain their encapsulation within the class body.

The privacy of these fields is enforced by JavaScript itself, with access restricted to methods defined within the class. This is distinct from private properties in closure scopes, which require manual setup and can recreate functions for each instance. Modern JavaScript's implementation of private fields maintains true encapsulation by storing these properties in a hidden internal space that is inaccessible to external scripts.

When a class declares a property using the `#` symbol, it creates a private field that cannot be accessed directly from outside the class. These fields are managed through the class body, and attempting to reference them from outside results in a SyntaxError. The privacy mechanism works by storing properties in a way that prevents inspection, copying, or scanning through regular object enumeration.


### Implementation Details

Private fields in JavaScript are designed to work seamlessly with class syntax. When a class declares a property using the `#` symbol, it creates a private field that is accessible only through methods defined within the class body. This includes initializers that run before the constructor, allowing for controlled property assignment.

Each class manages its own private fields independently. While two classes may declare fields with the same name, they maintain separate, non-interfering sets of private data. This unique identifier system prevents clashes between static and instance properties, with the exception of getter-setter pairs.


### Method Access and Encapsulation

The class body serves as the scope for private field access. Methods within the class can read and write to these fields, while external code encounters a SyntaxError attempting to access them directly. For example, a class might include a method like `this.#value` to access its private field.

The MDN documentation notes that while JavaScript engines perform static analysis to detect all private field usages before evaluation, the Chrome console temporarily relaxes this restriction, allowing access to private properties outside the class. However, this behavior is specifically for development tools and should not be relied upon in production code.


### Class Method Interactions

Class methods maintain consistent access to private fields regardless of implementation changes. For instance, a Color class might implement its methods using either RGB or HSL values internally, with private fields ensuring that external access remains abstracted from the underlying implementation. This abstraction allows for safer refactoring and prevents client code from breaking when internal representations change.


## Best Practices for Class Development

Private fields in JavaScript provide a way to define properties that are only accessible within the class body. Unlike private properties in closures, which require manual setup and can recreate functions for each instance, private fields maintain their privacy without additional complexity.

When a class declares a property using the `#` symbol, it creates a private field that cannot be accessed directly from outside the class. These fields are stored in a hidden internal space and can only be accessed through methods defined within the class body. This approach differs from the symbol-based approach, which, while ensuring uniqueness, still allows properties to be inspected, copied, or scanned using `Object.getOwnPropertySymbols()`.

The privacy encapsulation is enforced by JavaScript itself, with access restricted to methods defined within the class. While JavaScript is dynamically typed, compile-time checks enforce these restrictions, preventing accidental access or modification of private fields from outside the class body. The only way to access private fields is through the class body where they are defined, providing a more secure implementation of privacy features within JavaScript classes.


### Implementation and Access

Each class manages its own private fields independently. Even if two classes declare fields with the same name, they maintain separate, non-interfering sets of private data. This unique identifier system prevents clashes between static and instance properties, with the exception of getter-setter pairs. Within the class body, private fields behave consistently regardless of implementation changes. For example, a Color class might implement its methods using either RGB or HSL values internally, while maintaining a consistent interface for external access.


### Best Practices

While JavaScript engines perform static analysis to detect all private field usages before evaluation, the Chrome console temporarily relaxes this restriction. This allows access to private properties for development purposes but should not be relied upon in production code. Public fields or methods should be used for iterating over an object's properties, as private fields are explicitly excluded from such iterations to maintain their encapsulation.

