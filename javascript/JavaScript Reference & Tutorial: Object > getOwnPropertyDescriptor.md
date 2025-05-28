---

title: Object.getOwnPropertyDescriptor: JavaScript Property Management

date: 2025-05-26

---


# Object.getOwnPropertyDescriptor: JavaScript Property Management

In JavaScript, managing object properties goes beyond simple value assignment. The Object.getOwnPropertyDescriptor method offers developers precise control over property configurations, from read-only data properties to dynamically accessible values. This article explores the fundamentals of property descriptors, demonstrates how to access and manipulate these configurations, and shows how this powerful tool can enhance your JavaScript development toolkit.


## Property Descriptor Basics

The Object.getOwnPropertyDescriptor method allows developers to examine the precise configuration of an object's properties through its descriptor object. Each property descriptor consists of several key attributes:

Value: Represents the current value of the property.

Writable: A boolean indicating whether the property's value can be changed.

Enumerable: A boolean determining whether the property appears in for...in loops and Object.keys() results.

Configurable: A boolean controlling whether the property can be deleted or its descriptor modified.

As of July 2013, this feature has full browser support across modern browsers including Chrome 23, IE/Edge 11, Firefox 21, Safari 6, and Opera 15.

The method's response structure includes both data descriptors (properties with a value) and accessor descriptors (properties with getter and/or setter functions). For example, considering an object with a simple value property and a getter method:

```javascript

let person = { name: 'John', age: 25 };

let descriptor = Object.getOwnPropertyDescriptor(person, 'name');

console.log(descriptor); // {value: "John", writable: true, enumerable: true, configurable: true}

descriptor = Object.getOwnPropertyDescriptor(person, 'getFullName');

console.log(descriptor); // {get: [Function: getFullName], set: undefined, enumerable: true, configurable: true}

```

In this example, the 'name' property returns a data descriptor with writable, enumerable, and configurable attributes. The 'getFullName' property demonstrates an accessor descriptor with a getter function and the respective enumerable and configurable attributes.

Developers utilize Object.getOwnPropertyDescriptor for various purposes, including property cloning and deep object property inspection. This method serves as a fundamental tool for advanced JavaScript development, enabling precise control over object property configurations.


## Accessing Property Descriptors

The Object.getOwnPropertyDescriptor method retrieves detailed property descriptors for specified object properties. This includes information about the property's value, mutability, and visibility.

To access a property descriptor, you use the method's syntax: Object.getOwnPropertyDescriptor(obj, prop), where obj is the target object and prop is the property name or Symbol.

For example:

```javascript

let person = { name: 'John', age: 30 };

let descriptor = Object.getOwnPropertyDescriptor(person, 'name');

console.log(descriptor); // { value: "John", writable: true, enumerable: true, configurable: true }

```

This example demonstrates fetching the descriptor for the 'name' property, revealing its configuration. The method returns undefined if the specified property does not exist on the object.

For comprehensive property inspection, developers can use for...in loops in conjunction with this method. For example:

```javascript

let person = { name: 'John', age: 30 };

for (let prop in person) {

    if (Object.getOwnPropertyDescriptor(person, prop)) {

        console.log(prop);

    }

}

```

This loop iterates over all enumerable properties of the person object, checking each with Object.getOwnPropertyDescriptor.

Developers can also retrieve descriptors for multiple properties simultaneously using Object.getOwnPropertyDescriptors(obj), which returns an object containing descriptors for all object properties.

For instance:

```javascript

let person = { name: 'John', age: 30 };

let descriptors = Object.getOwnPropertyDescriptors(person);

console.log(descriptors);

```

This returns:

{

    name: { value: 'John', writable: true, enumerable: true, configurable: true },

    age: { value: 30, writable: true, enumerable: true, configurable: true }

}

The getOwnPropertyDescriptor method operates on the object's direct properties, excluding inherited properties from the prototype chain.

In practice, developers use these methods for precise property inspection and manipulation, such as object cloning with retained property configurations.


## Property Descriptor Attributes

Property descriptors provide a mechanism for precise control over object properties through attribute settings. These attributes include value, writable, enumerable, and configurable.

The value attribute holds the property's current value. The writable attribute determines whether the property's value can be changed. The enumerable attribute controls whether the property appears in for...in loops and Object.keys results. The configurable attribute determines if the property can be deleted and its attributes modified.

A property descriptor may also include a get function as its [[Get]] attribute and a set function as its [[Set]] attribute, making it an accessor descriptor. The [[Value]] attribute holds the property's value, while [[Writable]] indicates if the value can be changed. The [[Enumerable]] attribute controls enumeration visibility, and the [[Configurable]] attribute determines if attribute modification is allowed.

The configurable attribute, when set to false, prevents changes to the property type (data property vs. accessor property) and deletion. Writable properties allow value modification, while non-writable properties throw errors in strict mode when attempting assignment. Enumerable properties appear in Object.keys() and for...in loops, while non-enumerable properties remain hidden. Configurable properties permit deletion and attribute modification, while non-configurable properties resist these changes.

Developers can create custom getters and setters using the descriptor's getter and setter functions, providing fine-grained control over property access and modification. For example, an Archiver object might use Object.defineProperty to implement a temperature property with a custom setter that logs the value to an archive array: `Object.defineProperty(archiver, 'temperature', { set: function(val) { this.archive.push(val); } })`.

Implementing robust property management requires careful consideration of these attributes. For instance, setting writable: false creates a read-only property, while setting configurable: false prevents deletion and attribute modification, creating a more rigid property configuration. Understanding these attributes enables developers to implement constants (writable: false), hide internal properties during enumeration (enumerable: false), and protect object structure (configurable: false).


## Cloning Objects with Property Descriptors

To clone an object while preserving its property configurations, developers use the combination of Object.getOwnPropertyDescriptors and Object.defineProperties methods. This approach provides a "flags-aware" clone that maintains the original object's property metadata.

The process begins by retrieving all property descriptors using Object.getOwnPropertyDescriptors(obj), which returns an object containing descriptors for all own properties. This method captures symbolic and non-enumerable properties, providing a complete snapshot of the object's configuration.

Next, Object.defineProperties(target, descriptors) creates a new object with identical property configurations. This method takes two parameters: the target object and an object containing property descriptors. By passing the descriptors obtained from the previous step, the method creates a new object with matching property configurations.

Here is an example demonstrating this cloning process:

```javascript

const original = {

  name: "John",

  age: 25,

  get fullName() { return `${this.name} Doe`; }

};

const descriptors = Object.getOwnPropertyDescriptors(original);

const clone = Object.defineProperties({}, descriptors);

console.log(clone.name); // John

console.log(clone.age); // 25

console.log(clone.fullName()); // John Doe

```

In this example, the original object includes a data property (name) and an accessor property (fullName). The clone created using the descriptors maintains these properties and their configurations, including the getter function for fullName.

While these methods provide robust property cloning, developers should be aware that they may encounter limitations in certain scenarios. For instance, properties with non-configurable attributes may prevent deletion or modification. Additionally, the methods are subject to browser support considerations, with full compatibility available since April 2017.


## Browser Support and Methodology

Object.getOwnPropertyDescriptor has been an essential part of JavaScript since its ECMAScript 5 implementation. Introduced in July 2013 across modern browsers including Chrome 23, IE/Edge 11, Firefox 21, Safari 6, and Opera 15, this feature provides robust property inspection capabilities.


### Method Compatibility and Usage

The method returns an object containing descriptors for all own properties of a given object, capturing both symbolic and non-enumerable properties. For example:

```javascript

const person = { name: "John", age: 25, getFullName() {} };

const descriptor = Object.getOwnPropertyDescriptor(person, 'name');

console.log(descriptor); // { value: "John", writable: true, enumerable: true, configurable: true }

```

This demonstrates the retrieval of detailed information about the 'name' property. The method also supports bulk property inspection through Object.getOwnPropertyDescriptors(obj), capturing configuration details for multiple properties:

```javascript

const person = { name: "John", age: 25, getFullName() {} };

const descriptors = Object.getOwnPropertyDescriptors(person);

console.log(descriptors);

```


### Related Methods and Features

The method operates alongside other object property management tools:

- `Object.defineProperty()` adds or changes one property

- `Object.defineProperties()` adds or changes multiple properties

- `Object.getOwnPropertyNames()` returns the property names of an object

- `Object.getOwnPropertyDescriptor()` returns the descriptor of a specific property

- `Object.getOwnPropertyDescriptors()` returns all descriptors for an object

Together, these methods provide a comprehensive toolkit for JavaScript object manipulation, enabling developers to inspect, modify, and clone property configurations accurately.


### Browser Support and Evolution

As of April 2017, all modern browsers fully support the method. The original functionality has remained consistent since its July 2013 release, with no reported changes in major browser versions:

- Chrome 23

- IE/Edge 11

- Firefox 21

- Safari 6

- Opera 15 (September 2012)

This stable implementation across major browsers has established Object.getOwnPropertyDescriptor as a reliable foundation for JavaScript property management patterns.

