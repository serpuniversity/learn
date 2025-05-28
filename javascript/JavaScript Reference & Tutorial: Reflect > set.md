---

title: JavaScript Reflect > set

date: 2025-05-26

---


# JavaScript Reflect > set

JavaScript's Reflect API offers developers precise control over language features through its reflection methods. One of these methods, Reflect.set, extends native property assignment capabilities with advanced functionality for object manipulation. This introduction will explore the behavior, applications, and implications of Reflect.set, highlighting its role in modern JavaScript development.


## Method Definition

Reflect.set takes three or four parameters: target, propertyKey, value, and optionally receiver. These parameters function as follows:

- target: The object on which to set the property. This is the primary object that contains or will contain the property.

- propertyKey: The property name to be set. This can be a string or a Symbol. When only one argument is provided, both propertyKey and value are undefined.

- value: The value to set for the property. This can be any JavaScript value.

- receiver (optional): The value of this for the target call if a setter is encountered. When not provided, it defaults to the target.

The method works similarly to direct property assignment. When target and receiver are the same object, it behaves exactly like obj[propertyKey] = value. The key difference arises when target and receiver differ - in this case, Reflect.set uses the property descriptor from the target object to determine if the property is writable and to find the setter function.

If no setter is present on the target object, Reflect.set still attempts to set the property on the receiver. It returns true if successful and false if an error occurs. This allows for more flexible property assignment, particularly in scenarios where objects may be wrapped or proxied.


### Example Usage

```javascript

const obj = {};

Reflect.set(obj, "prop", "value"); // true

console.log(obj.prop); // "value"

const arr = ["duck"];

Reflect.set(arr, 2, "goose"); // true

console.log(arr[2]); // "goose"

// Truncates array

Reflect.set(arr, "length", 1); // true

console.log(arr); // ["duck"]

// Sets property without setter

const anotherObj = {};

Reflect.set(anotherObj); // true

console.log(anotherObj); // {}

```


## Parameter Handling

When only one argument is provided to Reflect.set, both propertyKey and value are undefined. This is particularly useful for checking if a property exists on an object, similar to using the in operator:

```javascript

Reflect.has(obj, 'property') // true if property exists, false otherwise

```

The method works with various JavaScript data types:

- For objects, it sets the property value:

  ```javascript

  const obj = {};

  Reflect.set(obj, 'prop', 'value'); // true

  console.log(obj.prop); // value

  ```

- For arrays, it allows setting individual elements or truncating the array by setting the length property:

  ```javascript

  const arr = ['duck'];

  Reflect.set(arr, 2, 'goose'); // true

  console.log(arr[2]); // goose

  Reflect.set(arr, 'length', 1); // true

  console.log(arr); // ['duck']

  ```

- When the receiver differs from the target, it uses the property descriptor from the target object to determine if the property is writable and to find the setter function. If no setter is present, it sets the property on the receiver instead:

  ```javascript

  const obj = {};

  console.log(Reflect.set(obj)); // true

  console.log(Reflect.getOwnPropertyDescriptor(obj, 'undefined')); // { value: undefined, writable: true, enumerable: true, configurable: true }

  ```

The method returns true if the property is successfully set and false if an error occurs. When setting array elements, it behaves like the assignment operator, allowing values to be assigned beyond the current length of the array:

```javascript

const arr = ['geek1', 'geek2', 'geeks'];

Reflect.set(arr, 2, 'geek4'); // true

console.log(arr[2]); // geek4

```


## Property Assignment

The property assignment behavior of Reflect.set closely mirrors direct property assignment syntax. When target and receiver are the same object, it operates identically to obj[propertyKey] = value. However, when they differ, Reflect.set utilizes the property descriptor from the target object to determine if the property is writable and to locate the setter function.

A notable difference arises when no setter is present on the target object: Reflect.set will still attempt to set the property on the receiver, returning true on success and false if an error occurs. This behavior enables more flexible property assignment, particularly in scenarios involving wrapped or proxied objects.

The method demonstrates several key behaviors through its implementation:

- Direct assignment: When target and receiver match, it functions exactly like obj[propertyKey] = value.

- Property descriptor usage: It leverages the property descriptor from the target object to determine writeability and locate setters.

- Success check: Returns true if the property is successfully set and false if an error occurs, maintaining consistency with direct property assignment.

- Compatibility: Mimics the behavior of the in operator as a function, returning true if the target has the property, either as an own or inherited property.

This implementation allows for robust property manipulation while maintaining compatibility with existing JavaScript syntax and behavior.


## Special Behavior

When no setter is present on the target object, Reflect.set will still attempt to set the property on the receiver. It returns true if successful and false if an error occurs. This behavior enables more flexible property assignment, particularly in scenarios involving wrapped or proxied objects.

The method works similarly to the in operator as a function, checking whether the target has the property, either as an own or inherited property. It operates with this behavior when called with a single argument, where both propertyKey and value are undefined.

The method's behavior aligns with the ECMAScript 2015 specification, allowing it to function correctly even when the target object does not possess a setter for the specified property. This ensures consistent property assignment across various object and property configurations, maintaining compatibility with existing JavaScript syntax and behavior.


## Browser Compatibility

The Reflect.set method is part of the ECMAScript language specification and has been stable since 2016. It is available in modern browsers and environments like Node.js through core-js polyfills.


### Browser Support and Polyfills

The Reflect object provides powerful functionality for extending JavaScript language features, offering methods like `apply`, `construct`, `defineProperty`, `deleteProperty`, `get`, and more. These methods allow developers to perform operations that would otherwise require complex workarounds or direct access to the object's internal structure.

For instance, the `setPrototypeOf` method allows changing an object's [[Prototype]] to null, returning true in such cases and indicating whether the target is extensible. It returns false if a prototype chain cycle is created. This functionality is baseline and available across many devices and browser versions since September 2016.


### Implementation Details

Reflect.set operates similarly to direct property assignment syntax. When target and receiver match, it functions exactly like obj[propertyKey] = value. However, when they differ, it leverages the property descriptor from the target object to determine writeability and locate setters. In cases where no setter is present on the target object, Reflect.set attempts to set the property on the receiver, returning true on success and false if an error occurs.

This behavior enables more flexible property assignment, particularly in scenarios involving wrapped or proxied objects. For example, when using the Proxy object to wrap an object, you might want any self-references within accessors to be re-routed to your wrapper. The Reflect.set method facilitates this by allowing you to intercept and control property assignments through a handler object.


### Practical Applications

Modern browsers and environments like Node.js through core-js polyfills support Reflect.set, making it a reliable choice for developers working with advanced JavaScript features. Its consistent behavior across implementations ensures that properties can be set in a manner consistent with existing JavaScript syntax and operations, while still providing powerful reflection capabilities.

