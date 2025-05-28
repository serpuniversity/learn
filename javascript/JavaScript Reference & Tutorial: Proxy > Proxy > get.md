---

title: JavaScript Proxy: The get Trap

date: 2025-05-26

---


# JavaScript Proxy: The get Trap

JavaScript's Proxy object allows developers to create custom behavior around fundamental operations on objects. By wrapping another object and defining specific behavior patterns, Proxies enable powerful features like property interception and method decoration. This guide focuses on the get trap, which controls property access through a Proxy. You'll learn how to implement custom property behavior, enforce constraints, and work with private properties while maintaining proper object interactions.


## Understanding JavaScript Proxy and the get Trap

A JavaScript Proxy intercepts fundamental operations on objects, and the get trap specifically defines behavior when accessing properties of a Proxy object. When using a JavaScript Proxy, you wrap another object (the target) to intercept its operations. These operations include property lookup, assignment, enumeration, and function invocations.

The Proxy constructor function allows you to create a new proxy object with the syntax `let proxy = new Proxy(target, handler)`, where the target is the object you want to intercept, and the handler is the object containing methods to control the behaviors of the target. These methods are called traps, and the most common traps include get, set, has, and deleteProperty.

The get trap is particularly important because it's called whenever a property of the target object is accessed through the proxy. Its basic functionality allows you to control how properties are accessed while maintaining proper object interactions. For example, when you use a JavaScript Proxy to log property accesses, you can intercept reads to perform custom actions before returning the property value.

Implementing a custom get trap involves defining behavior when a property is accessed. The trap receives three main arguments: the target object (`this`), the property name (`property`), and the receiver (usually the proxy itself or an object inheriting from the proxy). The trap can then return any value, which represents the property value. This return value becomes the result of the property access operation.

JavaScript Proxies offer several advantages. They allow developers to modify object properties and methods, add validation, enforce constraints, and provide custom logic when accessing properties. For instance, you can create computed properties using the get trap to generate values based on other properties. Additionally, Proxies can handle function calls through their apply trap, allowing you to control how functions are invoked.

To retrieve the original target object within a Proxy structure, JavaScript provides several approaches. One method is to implement a conditional getter trap that returns the target when a specific flag is set. Another approach involves using instance variables within class constructors, where the class returns a Proxy with an `__target__` property holding the original target object.


## Creating and Using a Proxy with the get Trap

A JavaScript Proxy wraps another object (the target) and intercepts its fundamental operations through a set of methods known as traps. To create a proxy, you use the Proxy constructor with the syntax `let proxy = new Proxy(target, handler)`, where `target` is the object to wrap, and `handler` contains methods to control the behaviors of the target.

For example, consider a simple array that needs dynamic getter functionality. You can use a Proxy to create this behavior:

```javascript

const target = [0, 1, 2];

const handler = {

  get: (target, prop) => {

    // If the property is undefined, return a new Proxy for chaining

    if (typeof prop === 'undefined') {

      return new Proxy(target, handler);

    }

    // Otherwise, return the target property as-is

    return target[prop];

  }

};

const proxy = new Proxy(target, handler);

```

This implementation allows properties to be accessed as functions, returning the property value unchanged if called without arguments or setting the property value and returning a new proxy for chaining.


### Property Access and Return Values

The get trap receives three main arguments: the target object (`this`), the property name (`prop`), and the receiver (usually the proxy itself). The trap returns any value, which becomes the result of the property access operation. This can be used to provide default values for missing properties, validate input, or perform custom logic before returning the property value.

For instance, you can wrap an array in a proxy that returns 0 for non-existent properties:

```javascript

let numbers = [0, 1, 2];

numbers = new Proxy(numbers, {

  get(target, prop) {

    if (prop in target) {

      return target[prop];

    } else {

      return 0; // default value

    }

  }

});

alert(numbers[1]); // 1

alert(numbers[123]); // 0 (no such item)

```


### Enforcing Constraints and Custom Logic

The get trap can also enforce specific constraints. For example, you can wrap an array in a proxy that only allows number values:

```javascript

let numbers = [];

numbers = new Proxy(numbers, {

  set(target, prop, val) {

    if (typeof val === 'number') {

      target[prop] = val;

      return true;

    } else {

      return false;

    }

  }

});

numbers.push(1); // added successfully

numbers.push(2); // added successfully

alert("Length is: " + numbers.length); // 2

numbers.push("test"); // TypeError ('set' on proxy returned false)

```

This example maintains the built-in functionality of arrays while adding custom validation. The proxy handler returns true on successful writes and false on invalid inputs, ensuring that only number values are accepted.


### Handling Private Properties and Method Context

When working with private properties, the get trap requires special handling. For instance, consider a user object with a password:

```javascript

let user = {

  _password: 'securepassword'

};

user = new Proxy(user, {

  get: (target, prop) => {

    if (prop === 'checkPassword') {

      return function(userInput) {

        return userInput === target._password;

      };

    }

    return target[prop];

  }

});

alert(user.checkPassword('correctpassword')); // true

alert(user.checkPassword('incorrectpassword')); // false

```

In this case, the get trap intercepts reads to `checkPassword`, returning a function that compares the input with the stored password. This maintains proper object functionality while providing controlled access to the private property.


## get Trap Parameters and Return Values

The get trap's implementation requires careful handling of its parameters to maintain correct object interactions. When a property is accessed through the proxy, the trap receives three main arguments: the target object (`this`), the property name (`prop`), and the receiver (usually the proxy object itself).

The return value of the get trap becomes the result of the property access operation. This allows developers to provide default values for missing properties, validate input, or perform custom logic before returning the property value. For example, you can wrap an array in a proxy that returns 0 for non-existent properties:

```javascript

let numbers = [0, 1, 2];

numbers = new Proxy(numbers, {

  get(target, prop) {

    if (prop in target) {

      return target[prop];

    } else {

      return 0; // default value

    }

  }

});

alert(numbers[1]); // 1

alert(numbers[123]); // 0 (no such item)

```

The trap's return value must adhere to specific invariants defined by the JavaScript specification. For non-writable, non-configurable own data properties, the trap must return the same value as the target's property descriptor's value attribute. For non-configurable own accessor properties with undefined getters, the trap must return undefined.

In cases where private properties are involved, the get trap requires special handling to maintain proper object functionality. For instance, consider a user object with a password:

```javascript

let user = {

  _password: 'securepassword'

};

user = new Proxy(user, {

  get: (target, prop) => {

    if (prop === 'checkPassword') {

      return function(userInput) {

        return userInput === target._password;

      };

    }

    return target[prop];

  }

});

alert(user.checkPassword('correctpassword')); // true

alert(user.checkPassword('incorrectpassword')); // false

```

In this case, the get trap intercepts reads to `checkPassword`, returning a function that compares the input with the stored password. This maintains proper object functionality while providing controlled access to the private property.

When working with object methods that access private properties, the get trap must bind the context to the original object. For example:

```javascript

let user = {

  _name: 'John',

  get name() {

    return this._name;

  }

};

user = new Proxy(user, {

  get: (target, prop, receiver) => {

    if (prop === 'name') {

      return Reflect.get(target, prop, receiver);

    }

    return Reflect.get(target, prop);

  }

});

alert(user.name()); // John

```

Here, the get trap uses Reflect.get to maintain the correct this context for the getter method. This ensures that methods like `user.name()` function correctly even when accessed through a proxy.

To handle built-in objects and maintain proper functioning, the proxy implementation should use Reflect.get instead of directly assigning the target property. This approach ensures that internal slots and built-in methods continue to operate correctly:

```javascript

let builtIn = new Date();

builtIn = new Proxy(builtIn, {

  get: (target, prop) => {

    return Reflect.get(target, prop);

  }

});

alert(builtIn instanceof Date); // true

alert(builtIn.toString()); // correct date string

```

This implementation maintains compatibility with built-in object behavior while providing the necessary property access control through the proxy.


## Common Issues and Limitations with get Trap

Understanding these built-in limitations is crucial for effective Proxy implementation. Built-in objects and private class fields have "internal slots" that cannot be proxied directly. Accessing these requires special handling, which often involves using the Reflect API to forward calls correctly.

Property inheritance and object equality testing present additional challenges. While Proxies can trap and control property access patterns, they have inherent limitations with deep property structures. For instance, attempting to override built-in property descriptors results in "TypeError" exceptions, as demonstrated in the document example:

```javascript

const obj = {};

Object.defineProperty(obj, "a", { configurable: false, enumerable: false, value: 10, writable: false });

const p = new Proxy(obj, { get(target, property) {

  return 20;

}});

p.a; // TypeError is thrown

```

Developers must be aware that while Proxies excel at dynamic property handling and method decoration, they cannot modify built-in object behavior or intercept === equality tests. These limitations affect how Proxies interact with language fundamentals and external libraries.

Performance considerations further complicate Proxy usage. Basic property access through a Proxy can be 2-3 times slower than direct object access, though this impact is most noticeable only in performance-critical code. This overhead arises from the additional function call and trap evaluation required for each property operation.

To mitigate these issues, developers should carefully consider where to apply Proxies. While useful for controlling property access and method behavior, they may not be necessary (or advisable) for simple data access patterns. For complex object structures or performance-sensitive applications, traditional object pattern wrapping may offer better trade-offs between functionality and efficiency.


## Best Practices for Using the get Trap

The get trap implements custom behavior for property access through the proxy, while set, deleteProperty, and other traps handle corresponding operations. The handler object defines these traps, and each trap receives specific parameters (target, property, receiver, etc.) based on its functionality.

For dynamic property access, the get trap can return functions to enable method chaining. The handler function checks if the argument is undefined. If not, it sets the target property and returns a new Proxy of the target object. If the argument is undefined, it returns the target property as-is. This allows properties to be accessed as functions, with two behaviors: returning the property value unchanged if called without arguments, or setting the property value and returning a new proxy for chaining.

Developers should consider implementing the set trap to enforce constraints. For example, wrapping an array in a proxy that only allows number values:

```javascript

let numbers = [];

numbers = new Proxy(numbers, {

  set(target, prop, val) {

    if (typeof val === 'number') {

      target[prop] = val;

      return true;

    } else {

      return false;

    }

  }

});

numbers.push(1); // added successfully

numbers.push(2); // added successfully

alert("Length is: " + numbers.length); // 2

numbers.push("test"); // TypeError ('set' on proxy returned false)

```

The proxy maintains the built-in functionality of arrays while adding custom validation. For handling missing keys, you can create a dictionary proxy that returns the untranslated phrase for non-existent keys:

```javascript

let dictionary = { 'Hello': 'Hola', 'Bye': 'Adiós' };

dictionary = new Proxy(dictionary, {

  get(target, phrase) {

    if (phrase in target) {

      return target[phrase];

    } else {

      return phrase;

    }

  }

});

alert(dictionary['Hello']); // Hola

alert(dictionary['Welcome to Proxy']); // Welcome to Proxy (no translation)

```

Developers must also consider the limitations of Proxy usage. Built-in objects have internal slots that cannot be proxied directly, requiring special handling. Accessing these requires using the Reflect API to forward calls correctly. For private class fields, implemented using slots, proxied method calls must have the target object as this to access them.

Proxies have inherent limitations with deep property structures and === equality testing. While useful for dynamic property handling and method decoration, they may not be suitable for built-in object behavior modification or performance-critical code. Developers should carefully evaluate where to apply Proxies, considering alternatives like traditional object pattern wrapping for simpler data access patterns.

