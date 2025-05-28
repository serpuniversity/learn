---

title: JavaScript Public Class Fields

date: 2025-05-26

---


# JavaScript Public Class Fields

JavaScript's class syntax has evolved significantly since its introduction in ECMAScript 2015, with several features designed to make class definitions more flexible and intuitive. One of the most notable additions is the ability to define properties directly within class declarations using public class fields. This syntax provides a more concise way to initialize properties and organize class state, but it also introduces new considerations for initialization order, field visibility, and method implementation.

In this article, we'll explore the behavior of public class fields, from their basic syntax and initialization mechanics to their interaction with constructors and inheritance. We'll examine how these fields differ from regular instance properties and constructor assignments, and we'll discuss best practices for using them in both simple and complex class hierarchies. Whether you're just starting to explore modern JavaScript classes or looking to refine your existing codebase, understanding public class fields will help you write more maintainable and readable code.


## Basic Syntax and Behavior

JavaScript's class fields feature allows properties to be declared and defined directly within class declarations, similar to how properties are defined in object literals. This syntax provides several benefits, including improved code readability and separation of initialization logic from the constructor body.

A class field can be either an ordinary string value or a function. For example:

```javascript

property = 'value';

routine = function () {};

```

The class constructor remains responsible for initializing properties, registering event listeners, invoking super methods, and performing similar setup tasks. While class fields offer more concise syntax, there are implications for memory usage and inheritance that developers should consider.

Like object properties, class fields can be initialized with default values and accessed using dot notation. For instance:

```javascript

class Person {

  name = "John Doe";

  age = 30;

}

var john = new Person();

console.log(john.name); // "John Doe"

console.log(john.age);  // 30

```

This syntax creates both the field value and a getter method. However, class fields also introduce some drawbacks. They can add extra lines of code where they serve little purpose, though they become more valuable when assigning multiple properties that don't depend on constructor arguments. The implementation requires Babel for transpilation in environments where native support is lacking.

Public class fields are accessed from outside the class and overwrite any previous definitions with the same name. For example:

```javascript

class Example {

  value = 1;

  override = 2;

  duplicate = 3;

}

let instance = new Example();

console.log(instance.value); // 1

console.log(instance.override); // 2

console.log(instance.duplicate); // 3

// Overwriting duplicate field

class SubExample extends Example {

  duplicate = 4;

}

let subInstance = new SubExample();

console.log(subInstance.duplicate); // 4

```

Understanding how these fields interact with the constructor and what methods can achieve similar functionality helps developers make informed decisions about their usage.


## Initialization and Overwriting

The class field syntax allows properties to be declared and defined directly within class declarations, with a few key implications for initialization and behavior. When a class field is initialized with a value, that value is assigned to the instance property before the constructor body runs. This means that field initializers execute immediately after any superclass constructors have completed, but before the subclass constructor runs.

For instance fields (properties that are not static), the initializer expression is evaluated during instance creation, either at the start of the constructor or just before the `super()` call returns for derived classes. In contrast, static fields (both public and private) have their initializers evaluated with `this` set to the class itself, creating the property directly on the class rather than on an instance.

This behavior has important implications for field initialization order and scope. In the example provided:

```javascript

class Person {

  name;

  age;

  constructor(name, age) {

    this.name = name;

    this.age = age;

  }

}

```

The `name` and `age` fields are added to the instance before the constructor runs, allowing them to be accessed and modified within the constructor method. This differs from traditional class definitions where instance property assignment would occur within the constructor.

The implementation treats public class fields as writable, enumerable, and configurable properties. While this gives developers flexibility in how they access and modify these properties, it also means that field values can be changed after initialization. This differs from static fields, which are created on the class itself and cannot be directly modified by instance operations.

Developers should be aware that while field initializers can access properties created by the base class constructor, they cannot reference fields that will be defined later in the class body. This ensures that properties are accessed in the correct initialization order and prevents potential errors from referencing non-existent properties.

The availability of public class fields varies across JavaScript environments. Modern browsers since ES2015 support public class fields natively, while older versions require transpilation using tools like Babel. Understanding these implementation details helps developers choose the right approach for their projects, balancing modern syntax with compatibility requirements.


## Instance Access

The behavior of public class fields makes them distinct from regular instance properties. While fields are added to each class instance before the constructor runs, this process differs from using `this.field = ...` within the constructor. Fields are created using the `[[DefineOwnProperty]]` semantic, meaning they exist on every created instance of a class.

Field initializers provide an alternative to constructor property assignment, particularly for properties that don't depend on constructor arguments. For instance fields, these initializers execute immediately after `super()` but before the constructor body runs. This ensures that field values are available within the constructor, though derived class fields are defined after `super()` returns and cannot be accessed by the base class constructor.

When multiple fields with the same name are defined, the last field declaration overwrites previous ones. This behavior applies to both instance and static fields. In the example provided:

```javascript

class Example {

  value = 1;

  override = 2;

  duplicate = 3;

}

let instance = new Example();

console.log(instance.value); // 1

console.log(instance.override); // 2

console.log(instance.duplicate); // 3

// Overwriting duplicate field

class SubExample extends Example {

  duplicate = 4;

}

let subInstance = new SubExample();

console.log(subInstance.duplicate); // 4

```

Field initializers create properties on each instance, making them accessible from outside the class. The access rules for public, static, and private fields differ, with public fields available on both instances and the constructor, while static fields are accessed through the class name. Private fields require the class name prefix for access (e.g., `User.#name`).

The implementation of public class fields requires careful consideration of initialization order and scope. Field access within the constructor behaves as expected, while referencing fields below the current initializer can lead to errors. This behavior differs from direct assignment using `this.field = ...`, which would allow referencing subsequent fields.


## Class vs Method Fields

Class fields differ fundamentally from regular instance properties in their placement within the class body and interaction with the constructor. While instance properties are attached to the `this` value within constructors, class fields are defined directly within the class declaration using the `=` syntax.

These direct definitions create properties via the `[[DefineOwnProperty]]` semantic, distinct from using `this.field = ...` in the constructor. The primary implication is that field initializers execute immediately after the `super()` call but before the constructor body runs. This placement allows them to access properties created by the base class constructor while preventing the base class constructor from referencing fields defined later in the class body.

The key distinctions manifest in several behaviors:

1. Property Creation: Fields create properties directly on instances using `[[DefineOwnProperty]]`, while constructor property assignment happens through `this.field = ...`.

2. Execution Order: In base classes, fields initialize before the constructor runs, while in derived classes, they execute immediately after `super()`. This ordering ensures fields are available within the constructor but not before `super()` returns.

3. Access Scope: For instance fields, `this` refers to the current instance, while static fields access `this` as the current class. Private fields require the class name prefix for access (e.g., `User.#name`).

4. Property Attributes: By default, public fields are writable, enumerable, and configurable. This differs from constructor property assignment, which always triggers setter methods if defined.

Class fields offer both advantages and challenges. They provide quick visibility into instance properties and align with the mental model of overriding properties at the class level. However, they can introduce refactoring hazards when moving property creation from constructors to fields and change behavior when moving from base to derived classes. Understanding these differences helps developers choose the appropriate approach for their projects, balancing modern syntax with compatibility requirements.


## Browser Support and Implementation

Modern browsers have supported public class fields since ES2015, though implementation details vary. For instance, Chrome has fully implemented public fields since version 72, while Firefox 68 throws a SyntaxError when encountering these features.

Field implementations use the `[[DefineOwnProperty]]` semantic to create properties directly on instances, distinct from traditional constructor property assignment. This approach requires different handling for base and derived class fields. In base classes, fields initialize before the constructor runs, while derived class fields execute immediately after `super()`.

The implementation treats public class fields as writable, enumerable, and configurable properties. By default, these fields behave similarly to ordinary properties, though developers can override these attributes as needed. For example:

```javascript

class MyClass {

  static publicStaticField;

  publicInstanceField;

}

assert.deepEqual(Object.getOwnPropertyDescriptor(MyClass, 'publicStaticField'), {

  value: undefined,

  writable: true,

  enumerable: true,

  configurable: true

});

assert.deepEqual(Object.getOwnPropertyDescriptor(new MyClass(), 'publicInstanceField'), {

  value: undefined,

  writable: true,

  enumerable: true,

  configurable: true

});

```

The feature requires the use of Babel 7.0+ for transpilation in environments without native support. Node.js 12+ also implements public fields, though private fields require Chrome 74+. Developers should be aware that while the syntax itself is not special, the use case is what makes it valuable.

The implementation allows developers to define properties and their associated getter/setter methods in a single line of code, making class definitions more concise and easier to read. This feature enables both public and private class fields, with public fields defined directly within the class and private fields using the `= () => {}` syntax.

