---

title: Object.preventExtensions()

date: 2025-05-27

---


# Object.preventExtensions()

JavaScript objects are inherently mutable, allowing developers to freely add, modify, and delete properties. While this flexibility is invaluable for building dynamic applications, there are scenarios where maintaining a fixed object structure is crucial. This is where `Object.preventExtensions()` comes into play—a powerful method that locks an object against new property additions while preserving its existing structure. In this comprehensive exploration, we'll examine how to use `Object.preventExtensions()`, what it does and doesn't affect, and why this method is essential for maintaining object integrity in modern JavaScript development.


## Basic Usage

To create an object and make it non-extensible, you can use the `Object.preventExtensions()` method. This method effectively prevents new properties from being added to the object while allowing modifications to existing properties.

Here's a basic example to illustrate its usage:

```javascript

const car = { brand: 'Toyota', model: 'Corolla' };

Object.preventExtensions(car);

```

After applying `Object.preventExtensions(car)`, attempting to add a new property to the `car` object will fail:

```javascript

try {

  car.year = 2021;

} catch (e) {

  console.log(e.message); // Outputs: Cannot add property year, object is not extensible

}

```

To check if an object has been made non-extensible, you can use the `Object.isExtensible()` method:

```javascript

const isExtensible = Object.isExtensible(car);

console.log(isExtensible); // Outputs: false

```

The `Object.preventExtensions()` method returns the object being made non-extensible. In cases where the argument is not an object (i.e., a primitive type), the method returns the argument itself:

```javascript

const notAnObject = Object.preventExtensions(42);

console.log(notAnObject === 42); // Outputs: true

```

The method only prevents addition of own properties, allowing properties to be added to the object prototype:

```javascript

let obj = {};

Object.preventExtensions(obj);

Object.getPrototypeOf(obj).newProperty = 'value';

console.log(obj.newProperty); // Outputs: 'value'

```


## Example Usage

Let's explore how `Object.preventExtensions()` works in practice. First, consider an object that's initially extensible:

```javascript

let obj = {};

console.log(Object.isExtensible(obj)); // Outputs: true

```

After applying `Object.preventExtensions(obj)`, the object becomes non-extensible:

```javascript

Object.preventExtensions(obj);

console.log(Object.isExtensible(obj)); // Outputs: false

```

Now, let's examine what happens when we attempt to add properties to this non-extensible object:

```javascript

try {

  obj.newProperty = 'value';

} catch (e) {

  console.log(e.message); // Outputs: Cannot add property newProperty, object is not extensible

}

```

In strict mode, attempting to add a new property will indeed throw an error:

```javascript

'use strict';

try {

  obj.newProperty = 'value';

} catch (e) {

  console.log(e.message); // Outputs: Cannot add property newProperty, object is not extensible

}

```

The method only affects own properties and allows modifications to existing properties:

```javascript

Object.preventExtensions(obj);

obj.existingProperty = 'new value'; // This works

console.log(obj.existingProperty); // Outputs: 'new value'

delete obj.existingProperty; // This works

console.log(obj.existingProperty in obj); // Outputs: false

```

We can also verify that the object's prototype remains unaffected:

```javascript

let proto = Object.getPrototypeOf(obj);

proto.newProperty = 'value';

console.log(obj.newProperty); // Outputs: 'value'

```

As noted in the documentation, calling `Object.preventExtensions()` makes it impossible to add new properties to the object, including its prototype chain. Attempting to modify the `__proto__` property will result in a `TypeError`:

```javascript

obj.__proto__ = {}; // Throws TypeError: Cannot assign to __proto__ of an object which does not implement __proto__

```

Finally, we should note that once an object is made non-extensible, its extensibility cannot be changed:

```javascript

Object.preventExtensions(obj);

try {

  Object.preventExtensions(obj); // This will not raise an error, but it's redundant

} catch (e) {

  console.log(e.message);

}

try {

  Object.seal(obj); // This will raise a TypeError

} catch (e) {

  console.log(e.message); // Outputs: TypeError: Cannot seal object, it is already non-extensible

}

try {

  Object.freeze(obj); // This will raise a TypeError

} catch (e) {

  console.log(e.message); // Outputs: TypeError: Cannot freeze object, it is already non-extensible

}

```

This behavior makes `Object.preventExtensions()` particularly useful in scenarios where maintaining a fixed object structure is crucial, such as configuration objects or data models that should not change once initialized.


## Return Value and Behavior

The method returns the object being made non-extensible, with the modification taking effect immediately. As documented, this return value can be used to verify that the operation was successful. For example, attempting to define a property on a non-extensible object will either fail silently in non-strict mode or throw a TypeError in strict mode.

```javascript

const obj = { name: 'John' };

const result = Object.preventExtensions(obj);

console.log(result === obj); // Outputs: true

```

The operation only affects own properties and does not impact the object's prototype chain. Therefore, it's possible to add properties to the object's prototype while keeping the original object non-extensible:

```javascript

Object.preventExtensions(obj);

Object.getPrototypeOf(obj).newProperty = 'value';

console.log(obj.newProperty); // Outputs: 'value'

```

Calling `Object.preventExtensions()` on an already non-extensible object has no effect and will not raise an error:

```javascript

Object.preventExtensions(obj); // No error

try {

  Object.preventExtensions(obj); // This is redundant but harmless

} catch (e) {

  console.log(e); // Expected output: null

}

```

This behavior prevents unnecessary attempts to modify an object's extensibility status. It's worth noting that while the method prevents new property additions, it does not affect existing properties in any way. This makes it particularly useful for maintaining the structure of complex objects without locking down their entire property system.


### Related Method Behavior

Comparing `Object.preventExtensions()` to other object-related methods provides further context:

- `Object.seal()` prevents new properties and deletions, making existing properties non-configurable.

- `Object.freeze()` creates fully immutable objects, preventing all modifications.

- `Object.preventExtensions()` specifically targets preventing new property additions while maintaining flexibility for existing property modifications and deletions.

These methods offer increasing levels of immutability, with `preventExtensions()` serving as a stepping stone between completely extensible and fully sealed/frozen objects. Understanding their distinct behaviors enables developers to choose the appropriate level of object protection based on specific use cases.


## Compatibility and Browser Support

Object.preventExtensions() has been supported across browsers since July 2015, making it widely available for use in modern web development. This method effectively prevents new properties from being added to an object while allowing modifications to existing properties.

The method works by returning the object being made non-extensible. This return value can be used to verify that the operation was successful. The following example illustrates its usage:

```javascript

const obj = { name: 'John' };

const result = Object.preventExtensions(obj);

console.log(result === obj); // Outputs: true

```

In cases where the argument is not an object (i.e., a primitive type), the method returns the argument itself:

```javascript

const notAnObject = Object.preventExtensions(42);

console.log(notAnObject === 42); // Outputs: true

```

The method prevents new properties from being added to the object and its prototype chain:

```javascript

const obj = {};

Object.preventExtensions(obj);

try {

  obj.newProperty = 'value';

} catch (e) {

  console.log(e.message); // Outputs: Cannot add property newProperty, object is not extensible

}

try {

  obj.__proto__.newProperty = 'value';

} catch (e) {

  console.log(e.message); // Outputs: Cannot assign to __proto__ of an object which does not implement __proto__

}

```

While `Object.preventExtensions()` makes an object non-extensible, it does not affect existing properties or the object's prototype chain. This behavior allows developers to protect the structure of complex objects without freezing their entire property system.

For instance, existing properties can still be modified or deleted:

```javascript

const car = { brand: 'Toyota', model: 'Corolla' };

Object.preventExtensions(car);

car.brand = 'Honda'; // This works

delete car.brand; // This works

console.log(car.brand in car); // Outputs: false

```

The method's behavior aligns with the ECMAScript 5 specification, providing consistent support across modern browsers. Implementation details show that Chrome 23, IE/Edge 11, Firefox 21, Safari 6, and Opera 15 all fully support the feature. More recent browser versions maintain compatibility, ensuring wide-ranging applicability for developers implementing robust object management strategies.


## Related Methods

`Object.preventExtensions()` serves as a foundational method in JavaScript for controlling object immutability, specifically designed to prevent new properties from being added to an object while maintaining flexibility for existing property modifications and deletions. This method operates by returning the object being made non-extensible, allowing developers to verify the operation's success through subsequent checks.

In comparison to `Object.seal()`, while both methods prevent new properties from being added, `Object.preventExtensions()` does not alter the configuration attributes of existing properties, meaning they remain mutable and deletable. `Object.seal()`, on the other hand, enhances this restriction by making all existing properties non-configurable, thereby preventing any changes to their attributes.

When contrasted with `Object.freeze()`, which creates fully immutable objects by preventing both property addition and modification, `Object.preventExtensions()` represents an intermediate level of control. It enables developers to protect the structure of complex objects while maintaining the ability to modify or delete existing properties, offering a more nuanced approach to object management.

In practice, these methods provide developers with robust tools for implementing defensive programming strategies. By selectively controlling object mutability based on specific requirements, developers can enhance code security and reduce unintentional data changes throughout an application's lifecycle. The appropriate selection of these methods—`preventExtensions()`, `seal()`, or `freeze()`—depends on whether the primary goal is to prevent accidental property additions, maintain flexible modifications to existing properties, or achieve complete object immutability.

