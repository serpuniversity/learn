---

title: JavaScript Property Access: Dot Notation vs. Bracket Notation

date: 2025-05-27

---


# JavaScript Property Access: Dot Notation vs. Bracket Notation

In JavaScript, property access is a fundamental operation that enables developers to retrieve and manipulate data stored within objects. While the language provides multiple ways to achieve this, two primary approaches - dot notation and bracket notation - offer distinct advantages and syntaxes. Understanding these differences is crucial for writing efficient, flexible, and maintainable JavaScript code, particularly when working with complex data structures or implementing object-oriented patterns. This article explores the properties and use cases of both dot and bracket notation, highlighting their strengths and appropriate usage scenarios in modern JavaScript development.


## Basic Property Access

In JavaScript, the most common method for accessing object properties is dot notation, which requires the part after the dot to be a valid variable name, directly naming the property. For example, in the object `var obj = { "abc" : "hello" };`, using dot notation allows you to access properties like `obj.abc`. However, this notation has limitations when dealing with property names containing special characters or spaces.

Bracket notation offers more flexibility by allowing access to properties with numbers as names and working when property names are assigned to variables. This method's syntax requires specifying the object followed by square brackets and the property name inside quotes. For instance, for an object `var obj = { "abc" : "hello" };`, you can successfully use bracket notation to access properties with `obj["abc"]`.

An important distinction between the two methods is their handling of dynamic property names. When you need to access properties whose names are determined at runtime or stored in variables, bracket notation becomes essential. The text provides examples demonstrating these capabilities, such as using a variable to access properties dynamically: `const propertyName = "name"; console.log(person[propertyName]); // Output: John`.

The MDN Web Docs note that both syntaxes treat the key as a string, with numbers being coerced to strings automatically. This means you can use either notation to access properties like `recordCollection[2548].artist`, while also noting that both dot and bracket notations require the property to exist in the object.

Both methods share similarities in their basic function of accessing properties, but bracket notation significantly expands JavaScript's flexibility in handling diverse property names and dynamic naming scenarios.


## Property Access Syntax

Dot notation allows direct property access using the object name followed by the property name. This approach requires the property name to be a literal string and allows properties to contain valid identifiers, including reserved words like `$1`. However, dot notation has limitations, as demonstrated with the following example:

```javascript

const obj = {

  123: 'digit',

  123name: 'start with digit',

  name123: 'does not start with digit',

  $name: '$ sign',

  name-123: 'hyphen',

  NAME: 'upper case',

  name: 'lower case'

};

// Success with valid identifiers

console.log(obj.$name); // '$ sign'

console.log(obj['123name']); // 'start with digit'

console.log(obj['name123']); // 'does not start with digit'

console.log(obj['NAME']); // 'upper case'

console.log(obj['name']); // 'lower case'

// Failures with special character properties

console.log(obj.123); // SyntaxError

console.log(obj['name-123']); // TypeError

```

While dot notation excels when property names are known and valid identifiers, bracket notation offers flexibility with dynamic property names and special character support. The following code demonstrates accessing properties using bracket notation:

```javascript

const propertyName = "name-123";

obj[propertyName]; // 'hyphen'

obj["$name"]; // '$ sign'

obj['123name']; // 'start with digit'

obj[123]; // 'digit'

```

The bracket notation syntax requires the expression inside the square brackets to evaluate to a string or Symbol representing the property's name. This allows for accessing properties with numbers as names and working when property names are assigned to variables, as shown in this example:

```javascript

const obj = { "abc" : "hello" };

const x = "abc";

obj[x]; // 'hello'

```


## Dynamic Property Names

While dot notation provides a clean and concise syntax for accessing object properties, it has limitations when dealing with dynamic property names or properties containing special characters. The key difference lies in how property names are evaluated: dot notation requires the property name to be a literal string, while bracket notation allows for more flexible evaluation.

The specification clearly states that the "expression" in bracket notation "should evaluate to a string or Symbol representing the property's name." This flexibility allows developers to use variables, string literals, or expressions that evaluate to valid property names. For example:

```javascript

const propertyName = "name-123";

obj[propertyName]; // 'hyphen'

obj["$name"]; // '$ sign'

obj['123name']; // 'start with digit'

obj[123]; // 'digit'

```

Dynamic property name access is particularly powerful when combined with variable assignment. The text demonstrates this capability through examples like:

```javascript

let propertyName = "make";

myCar[propertyName] = "Ford";

propertyName = "model";

myCar[propertyName] = "Mustang";

console.log(myCar); // { make: 'Ford', model: 'Mustang' }

```

However, this flexibility comes with important caveats. Browser support for bracket notation is consistently modern, with full support since July 2015. Nonetheless, developers must ensure that the evaluated property name produces a valid string or Symbol, as any other value will be coerced to a string during access.

The text emphasizes that while both notations perform the same basic function of accessing properties, they excel in different scenarios. Dot notation remains the preferred choice for its readability and performance, as it directly names properties using valid JavaScript identifiers. Bracket notation, while slightly slower due to the additional processing required to evaluate property names, offers essential capabilities for dynamic name access and special character handling.

Modern JavaScript development increasingly favors bracket notation for property access when dynamic or special character names are involved, while continuing to use dot notation for its clarity and performance in static, alphanumeric naming scenarios.


## Special Considerations

JavaScript's property accessors offer developers two primary methods for accessing object properties: dot notation and bracket notation. Each method has distinct limitations and capabilities, particularly regarding property names and their validity.

Dot notation requires the property name to be a valid JavaScript identifier, including reserved words like `$1`. This notation fails when encountering properties containing special characters or spaces, as demonstrated in this example:

```javascript

const obj = {

  123: 'digit',

  123name: 'start with digit',

  name123: 'does not start with digit',

  $name: '$ sign',

  name-123: 'hyphen',

  NAME: 'upper case',

  name: 'lower case'

};

obj.123; // SyntaxError

obj.123name; // SyntaxError

obj.name-123; // SyntaxError

obj['name-123']; // 'hyphen'

```

Bracket notation operates differently, allowing access to properties containing special characters and spaces. It requires the expression inside the square brackets to evaluate to a string or Symbol representing the property's name. Examples of successful bracket notation usage include:

```javascript

obj['123']; // 'digit'

obj['123name']; // 'start with digit'

obj['name123']; // 'does not start with digit'

obj['$name']; // '$ sign'

obj['name-123']; // 'hyphen'

obj['NAME']; // 'upper case'

obj['name']; // 'lower case'

```

This flexibility comes with specific requirements: property names using bracket notation must be valid strings or Symbols. When accessing array elements, bracket notation correctly interprets numeric indices, while dot notation does not:

```javascript

const array = [10, 20, 30];

console.log(array.0); // SyntaxError

console.log(array[0]); // 10

```

Both property access methods perform the same basic function, with dot notation generally preferred for its readability and performance when dealing with standard property names. Bracket notation remains essential for accessing properties with special characters, spaces, or dynamically determined names. The language specification ensures consistent behavior across modern JavaScript implementations.


## Accessor Methods

Property accessors in JavaScript enable custom behavior when accessing or modifying object property values through getter and setter methods. This feature allows developers to encapsulate property access logic while maintaining a clean, readable interface for external code.

The primary mechanism for implementing accessors is via the `get` and `set` keywords within object literals or using the `Object.defineProperty` method. These methods enable developers to control how properties are accessed and modified, providing several key benefits including data validation, encapsulation, and computed properties.


### Getter Implementation

Getter methods allow for establishing custom behavior when accessing object property values. For example, consider a `User` class that encapsulates email information:

```javascript

class User {

  constructor(name, email) {

    this._name = name;

    this._email = email;

  }

  get userEmail() {

    return this._email;

  }

}

```

In this implementation, the `userEmail` getter method returns the protected `_email` property, demonstrating how accessors can control property access logic.


### Setter Implementation

Setter methods enable modifying property values while executing custom behavior. For instance, consider implementing a `fullName` property that combines first and last names:

```javascript

let person = {

  firstName: "John",

  lastName: "Doe",

  get fullName() {

    return `${this.firstName} ${this.lastName}`;

  },

  set fullName(name) {

    let parts = name.split(' ');

    this.firstName = parts[0];

    this.lastName = parts[1];

  }

};

```

This implementation demonstrates how setter methods can process and assign values, while maintaining encapsulation of internal property values.


### Accessor Metadata

Accessor properties differ from data properties in their descriptor structure. While data properties have `value` and `writable` attributes, accessor properties define `get` and `set` functions. This distinction affects how properties are handled in operations such as `Object.defineProperty`:

```javascript

let obj = {

  get propName() {

    // getter implementation

  },

  set propName(value) {

    // setter implementation

  }

};

```

The metadata attributes for accessor properties include `enumerable`, `configurable`, and in the case of getters and setters, no `value` or `writable` properties. Understanding these differences allows developers to effectively manipulate property attributes using methods like `Object.defineProperty`.


### Cross-Browser Compatibility

While modern JavaScript implementations fully support property accessors, developers should note compatibility with older browsers. The feature has consistently worked across devices and browser versions since July 2015, with Internet Explorer 8 being the primary exception due to lack of support. This compatibility information helps developers balance feature implementation with broader cross-browser support considerations.

