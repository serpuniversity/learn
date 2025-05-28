---

title: ArrayBuffer and Symbol.species in JavaScript

date: 2025-05-26

---


# ArrayBuffer and Symbol.species in JavaScript

The dynamic nature of JavaScript inheritance often requires developers to customize how objects are created and manipulated. The Symbol.species property plays a crucial role in this process, allowing subclasses to control constructor behavior for built-in objects like Array and ArrayBuffer. This feature enables more flexible inheritance patterns while maintaining compatibility with existing code. However, its implementation introduces performance considerations and security vulnerabilities, particularly in array buffer methods. Understanding Symbol.species is essential for effective JavaScript development, especially when managing object creation patterns and implementing custom constructors.


## Symbol.species Property

The Symbol.species property serves as a special identifier for specifying custom constructors in JavaScript subclasses, particularly for built-in objects. This feature enables developers to customize how instances of these subclasses are created, especially when dealing with methods that return default constructors.

When a class extends a built-in object like Array, the subclass can use Symbol.species to control how its instances are instantiated. As demonstrated in the documentation, this allows subclasses to override the default constructor behavior. For example, when implementing a MyArray class that extends Array, the subclass can return either Array or a subclass of Array when called with the instanceof operator:

```javascript

class MyArray extends Array {

  static get [Symbol.species]() { return Array; }

}

console.log(MyArray instanceof Array); // true

```

In practice, this feature enables more flexible inheritance and method overriding while maintaining compatibility with existing code that relies on specific constructor behaviors. As noted in the documentation, the advantage of using Symbol.species is performance and simplicity in implementing more flexible inheritance patterns without additional wrapping code.

The implementation of Symbol.species in JavaScript engines has led to security considerations due to its potential for arbitrary code execution. Engine implementers are currently investigating whether to remove the feature, particularly in the context of array buffer methods where it creates security vulnerabilities. Modern array methods typically do not use Symbol.species and instead always return a new Array base class instance.

Developers implementing Symbol.species should be aware of performance implications and edge cases, particularly when managing non-standard object references and extending property lookup times through the prototype chain. Understanding this feature's behavior, especially in class hierarchies and with mixins, is crucial for effective JavaScript development.


## ArrayBuffer[Symbol.species]

ArrayBuffer[Symbol.species] plays a crucial role in determining the constructor used to create return values from array buffer methods, allowing for custom behavior in derived classes. When calling methods that create new array buffer instances (like slice()), the object's constructor[Symbol.species] is accessed, with the returned constructor used to construct the return value. This feature is widely available across devices and browser versions, having been implemented since December 2021 for SharedArrayBuffer[Symbol.species].

The property's default implementation returns the constructor function, meaning derived subclasses will return the constructor itself by default. When creating a subclass, such as MyArrayBuffer, the species is the MyArrayBuffer constructor by default. However, this can be overridden to return parent ArrayBuffer objects in derived class methods, demonstrating the flexibility of this feature.

The implementation process involves several key steps. First, the method checks that the this value (O) has an internal slot [[ArrayBufferData]]. It then throws TypeError exceptions if O is a shared array buffer or detached buffer. The method calculates the new length (newLen) based on the start and end parameters, ensuring it's non-negative. It determines the constructor (ctor) to use for the new ArrayBuffer based on Symbol.species, creating a new ArrayBuffer instance (new) with the calculated length. Additional checks are performed on the new ArrayBuffer, throwing exceptions if it's a shared array buffer, detached buffer, or has a smaller byte length than the calculated new length.

This process ensures that neither the creation of the new ArrayBuffer instance nor the copying from the old block are observable to other code. The new ArrayBuffer's [[ArrayBufferData]] and [[ArrayBufferByteLength]] properties are set based on the old ArrayBuffer's values and the calculated new length. The implementation notes that this method can be optimized for in-place growth or shrinkage, providing flexibility in how the buffer resizing operations are performed.


## Implementation and Behavior

ArrayBuffer's implementation of Symbol.species demonstrates its role in object instantiation across class hierarchies. When subclassing ArrayBuffer, methods like map() return instances of the subclass rather than arrays, overriding the default constructor behavior.

This functionality relies on the subclass implementing Symbol.species to return the desired constructor function. For example, consider a custom ArrayBuffer subclass:

```javascript

class MyArrayBuffer extends ArrayBuffer {

  static get [Symbol.species]() { return ArrayBuffer; }

}

const myBuffer = new MyArrayBuffer();

const mappedBuffer = myBuffer.map(x => x);

console.log(mappedBuffer instanceof MyArrayBuffer); // false

console.log(mappedBuffer instanceof ArrayBuffer); // true

```

In this case, MyArrayBuffer extends ArrayBuffer and implements Symbol.species to return ArrayBuffer. When calling map() on an instance of MyArrayBuffer, the returned object is an instance of ArrayBuffer rather than MyArrayBuffer, demonstrating the constructor override behavior.

The implementation of this feature allows for more flexible inheritance patterns while maintaining compatibility with existing code that relies on specific constructor behaviors. This balance between performance and functionality is crucial for modern JavaScript development, particularly in scenarios where custom object creation patterns are required.


## Security Considerations

ArrayBuffer and its subclasses have historically been a rich source of security vulnerabilities in JavaScript engines, primarily due to complexities in their implementation and the dynamic nature of JavaScript itself. Notable vulnerabilities include Chrome's CVE-2017-5030, where referencing the new array combined with other callbacks caused a bug, and Safari's CVE-2016-4734, which involved buffer detachment during critical operations like copyWithin and sort.

Research into these vulnerabilities has revealed that array index interceptors, a key feature enabled by Symbol.species, are particularly prone to exploitation. In Safari, this vulnerability affected both the main JavaScript engine and the WebKit implementation, with Chakra experiencing similar issues during their array sort operations. These vulnerabilities demonstrate the complex interactions between dynamic prototype manipulation and core language features.

The implementation process for ArrayBuffer[Symbol.species] demonstrates the inherent complexities of JavaScript's prototype system. When a method creates a new ArrayBuffer, it must perform several safety checks:

1. Validate the this value's [[ArrayBufferData]] slot

2. Prevent operation on shared or detached buffers

3. Calculate the new length based on provided parameters

4. Determine the appropriate constructor using Symbol.species

5. Create and configure the new ArrayBuffer object with proper byte length and data

Engine implementers face significant challenges in balancing performance and security when implementing this feature. Modern engines employ sophisticated optimization techniques, such as "fast path" and "slow path" execution, to handle array operations efficiently while maintaining robust security. These optimizations must account for the wide range of valid and invalid array states, from simple numeric arrays to complex typed arrays with multiple memory layouts.


## Development Best Practices

Implementing Symbol.species requires careful consideration of performance implications and edge cases to ensure proper object creation patterns. While the feature enables more flexible subclass behavior, developers should be aware that the MDN documentation may contain contradictory information about method return behaviors. Specifically, the implementation causes inherited methods like map() to return the parent Array object rather than derived class instances, which contradicts the expected object-oriented behavior of returning the same type in derived classes.

The species symbol allows developers to specify a custom constructor for derived classes, overriding the default behavior of returning the parent class's constructor. This functionality is particularly useful for maintaining compatibility with existing code that relies on specific constructor behaviors. For example, when creating a CustomArray subclass, developers can ensure that operations like map() return standard Array instances rather than CustomArray objects:

```javascript

class CustomArray extends Array {

  static get [Symbol.species]() {

    return Array;

  }

}

const customArray = new CustomArray(1, 2, 3);

const mappedArray = customArray.map(x => x * 2);

console.log(mappedArray instanceof Array); // true

console.log(mappedArray instanceof CustomArray); // false

```

Developers can implement a similar pattern for custom Map subclasses:

```javascript

class CustomMap extends Map {

  static get [Symbol.species]() {

    return Map;

  }

  clearAndClone() {

    const clonedMap = new this.constructor();

    for (let [key, value] of this) {

      clonedMap.set(key, value);

    }

  }

}

```

This implementation ensures that the clearAndClone method creates instances of the derived CustomMap class:

```javascript

const customMap = new CustomMap({ a: 1, b: 2, c: 3 });

customMap.clearAndClone().set('d', 4);

console.log(customMap.get('d')); // undefined

console.log(customMap.constructor); // CustomMap

```

While the underlying implementation details can vary across JavaScript engines, developers should consistently use console.dir and breakpoints to verify Symbol.species behavior in their specific environment. The property's attributes (writable: no, enumerable: no, configurable: no) indicate that it should be used as a static data property for constructor functions.

In practice, developers should implement Symbol.species in class hierarchies by defining the accessor property in their constructor functions. For mix-in patterns, this property can provide additional functionality to existing classes while maintaining proper object creation behavior:

```javascript

class MyMixin {

  static get [Symbol.species]() {

    return Array;

  }

}

class CustomArray extends Array {

  static get [Symbol.species]() {

    return Array;

  }

}

const mixedArray = new MyMixin(1, 2, 3);

console.log(mixedArray instanceof MyMixin); // true

console.log(mixedArray instanceof Array); // true

const customMixedArray = new CustomArray(1, 2, 3).concat(new MyMixin(4, 5, 6));

console.log(customMixedArray instanceof CustomArray); // false

console.log(customMixedArray instanceof Array); // true

```

By understanding the nuances of Symbol.species implementation across JavaScript engines and maintaining consistent development patterns, developers can leverage this feature to create more flexible and maintainable object creation patterns in their applications.

