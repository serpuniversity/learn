---

title: JavaScript Class Inheritance: Understanding extends

date: 2025-05-26

---


# JavaScript Class Inheritance: Understanding extends

JavaScript's class inheritance model allows child classes to inherit attributes and functionality from parent classes, promoting code reuse and extension while reducing redundancy. By leveraging the extends keyword, developers can create well-organized class hierarchies that accurately represent real-world relationships. This article explores the fundamentals of JavaScript class inheritance, from basic syntax to advanced usage patterns, while highlighting best practices for maintaining optimal code organization and performance.


## JavaScript Class Inheritance Fundamentals

In JavaScript, classes provide a structured way to create and manage objects, offering several key benefits. They enable improved code organization through clear structure and enhanced maintainability (Doc3). Classes also support encapsulation by bundling data and methods into one place, improving code clarity (Doc3).

The language's class inheritance model allows a child class to inherit attributes and functionality from a parent class. This support for inheritance enables code reuse and extension while reducing redundancy (Doc1). When implementing inheritance in JavaScript, the extends keyword is used to declare or define a class, automatically turning it into a child class (Doc1).

JavaScript's class-based OOP follows several fundamental concepts. Functions serve as primary building blocks, with constructor functions creating object blueprints similar to class-based OOP in other languages (Doc5). The prototype chain enables prototype-based inheritance, where objects can inherit properties and behaviors from other objects (Doc4).

The syntax for class declaration consists of the class keyword followed by the class name, with class methods defined within curly braces (Doc4). The constructor method is a special method for creating objects from the class, allowing initialization of class properties when a JavaScript object is created (Doc4).

Classes can be used to represent objects with similar functionalities or properties. For example, the Rectangle class demonstrates this with two instances: square with dimensions 5x5 and poster with dimensions 2x3. This structure enables creating multiple instances of a type of object with similar functionalities, while encapsulation allows methods to behave differently based on the object's type (Doc4).

The language also supports private fields, which are scoped to the class body and inaccessible to outside code. This prevents access to private fields in derived classes while maintaining the overall object structure (Doc5). While JavaScript classes provide a structured approach to object-oriented programming, they must be used judiciously to balance maintainability and performance considerations (Doc1).


## Using extends to Create Child Classes

Using the extends keyword, developers create child classes that inherit methods and properties from parent classes. This allows for code reuse and efficient implementation of common functionality.


### Subclass Definition and Constructor

When declaring a child class, the extends keyword specifies the parent class. The child class's constructor must call super() with any required arguments before referencing this. This ensures proper inheritance of parent class functionality.

```javascript

class Vehicle {

  constructor(brand) {

    this.brand = brand;

  }

  displayBrand() {

    console.log(`Brand: ${this.brand}`);

  }

}

class Car extends Vehicle {

  constructor(brand, model, color) {

    super(brand);

    this.model = model;

    this.color = color;

  }

  displayDetails() {

    console.log(`Details: ${this.model} ${this.color}`);

  }

}

```


### Method and Property Inheritance

Child classes inherit properties and methods from their parent class. This allows extending core functionality while maintaining a clear separation of concerns.

```javascript

class Animal {

  constructor(name) {

    this.speed = 0;

    this.name = name;

  }

  run(speed) {

    this.speed = speed;

    console.log(`${this.name} runs with speed ${this.speed}.`);

  }

  stop() {

    this.speed = 0;

    console.log(`${this.name} stands still.`);

  }

}

class Rabbit extends Animal {

  hide() {

    console.log(`${this.name} hides!`);

  }

}

```


### Custom Constructor Behavior

The child class constructor can provide additional properties and methods while maintaining access to parent functionality. This allows implementing specific behaviors while building upon existing class structures.

```javascript

class MyClass {

  constructor(myPassedValue) {

    this.instanceProp = myPassedValue;

  }

  classMethod() {

    console.log(`The value was '${this.instanceProp}'.`);

  }

}

class ChildClass extends MyClass {

  constructor(myPassedValue) {

    super(myPassedValue);

    this.modifiedProp = myPassedValue + 50;

  }

  subclassMethod() {

    super.classMethod();

    console.log(`The value type was '${typeof this.instanceProp}'.`);

  }

}

```


### Property Accessors

Child classes can implement custom getter and setter methods for inherited properties. This allows extending functionality while maintaining controlled access to class properties.

```javascript

class MyClass {

  constructor(originalValue) {

    this.totalValue = 0;

  }

  set doubleThisValue(newValue) {

    this.totalValue = newValue * 2;

  }

  get currentValue() {

    console.log(`The current value is: ${this.totalValue}`);

  }

}

const myClassInstance = new MyClass();

myClassInstance.doubleThisValue = 20;

myClassInstance.currentValue; // The current value is: 40

```


### Method Overriding

Child classes can override parent class methods while maintaining access to parent functionality through super(). This allows implementing specific behaviors while building upon existing class structures.

```javascript

class Animal {

  makeSound() {

    console.log('Make Sound');

  }

}

class Dog extends Animal {

  makeSound() {

    super.makeSound();

    console.log('Woof! Woof!!');

  }

}

```


## Inheritance Mechanics: super and this

In JavaScript, the extends keyword establishes a relationship between classes, allowing subclasses to inherit properties and functions from parent classes. When implementing inheritance, the derived class constructor must call super() with any required arguments before referencing this. This ensures the proper initialization of the parent class constructor, equivalent to this = new ParentClass(arguments), as described in the MDN documentation.

The super() method plays a crucial role in JavaScript inheritance. Within a derived class constructor, super() is used to call the parent class constructor, initializing this - in this context, roughly equivalent to this = new ParentClass(arguments). Additionally, the super() function can call parent class static methods, as demonstrated in the ColorWithAlpha class example provided in one of the documents.

In the instance of method overriding, classes can specify their own methods to replace or extend parent class methods. When overriding, classes can use super.method(...) to call parent methods before or after implementing their own functionality, maintaining access to parent class methods while building upon existing class structures. This approach allows for enhanced functionality without completely replacing the parent class method.

The class extends relationship affects both methods and constructors. In constructors, JavaScript generates an empty constructor that calls the parent constructor with all arguments if a derived class extends another class without its own constructor, as described in the MDN documentation and demonstrated in the Mage class example. This ensures proper initialization of the derived class while maintaining access to parent class constructor functionality.

The language's handling of this and super() ensures a clear separation of concerns between parent and derived classes. Unlike arrow functions, which have no super access, traditional function bodies maintain super access from the outer function, as noted in the provided documentation. This design choice affects both method and constructor behavior, with constructors possessing a specific internal property [[ConstructorKind]]: "derived" that influences their behavior during inheritance.


## Best Practices and Considerations

The `extends` keyword enables JavaScript classes to form a clear hierarchy, representing real-world relationships and improving code organization. When creating a class hierarchy, it's important to choose the right parent class to maximize code reuse and maintainability. For example, the `Rectangle` class can be extended from the `Animal` class with a `speak` method, while the `Square` class can extend `Rectangle` to set both width and height to the same value (Doc1).

When adding or modifying behavior, use `extends` to create classes with enhanced functionality while maintaining a clear separation of concerns. The `BasicAccount` class can serve as a base for the `InterestAccount` class, which extends it with an `addInterest` method for calculating interest (Doc1).

In applications that process objects of different classes through a single interface, use inheritance to maintain consistency. The `Shape` class can have a `draw` method that is extended by the `Circle` class to add specific behavior (Doc1).

Some practical applications of `extends` include creating customized error types that inherit from the native `Error` class. The `DatabaseError` class can extend `Error` to create a specific error type with a custom name (Doc1).

While implementing inheritance, consider the following best practices:

- Use `extends` to create a clear class hierarchy that represents real-world relationships.

- Choose the right parent class to maximize code reuse and maintainability.

- Use `extends` to extend functionality while maintaining a clear separation of concerns.

- Process objects of different classes through a single interface using inheritance.

- Create customized error types by extending built-in classes like `Error`.

- Consider performance implications when extending built-in classes, as optimizations may be affected by inheritance patterns (Doc2).

- Avoid extending regular (non-constructible) objects by using composition instead.

- Be aware that JavaScript classes cannot extend `null` directly; use `extends null` only with careful consideration of `super()` behavior (Doc3).

- Understand that any expression can be used with `extends`, not just a class definition (Doc4).

