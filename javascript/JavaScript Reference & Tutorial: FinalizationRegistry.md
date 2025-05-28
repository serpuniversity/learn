---

title: JavaScript FinalizationRegistry: Memory Management and Cleanup

date: 2025-05-26

---


# JavaScript FinalizationRegistry: Memory Management and Cleanup

JavaScript's memory management system is designed to automatically clean up memory when objects are no longer in use, but developers often need more control over the cleanup process. The FinalizationRegistry API provides a powerful solution for managing object cleanup when objects are garbage collected. This article explores the core functionality of FinalizationRegistry, including how to create and use registries, how objects are registered and unregistered, and the mechanism for invoking cleanup callbacks. We'll also examine the technical details of the API, its behavior in different runtime environments, and best practices for implementation.


## FinalizationRegistry Constructor

The FinalizationRegistry constructor creates a registry object that manages cleanup callbacks for objects that may be garbage collected. This constructor requires a callback function as its primary parameter and supports an optional unregister token.

The constructor follows these key behaviors:

- It can only be instantiated using the 'new' keyword; calling it without 'new' will result in a TypeError.

- The constructor function that creates the instance is stored as a property of the object.

- The Symbol.toStringTag property is set to "FinalizationRegistry" to provide consistent behavior across different JavaScript engines.

When creating a registry instance, developers provide a callback function that specifies what action should be taken when a registered object is garbage collected. This callback will be invoked with the held value as an argument, allowing for targeted cleanup operations.

The held value can be any type (primitive, object, or undefined) and serves as a reference identifier for the registered object. This value is crucial for identifying which object's cleanup callback should be executed when the object is garbage collected.

The unregister token, which can be the same as the registered object or a different value, allows for targeted removal of objects from the registry. When an unregister token is provided, the registry maintains a weak reference to it, ensuring that the object can still be garbage collected while allowing for controlled removal from the registry via the unregister method.


## Registering and Unregistering Objects

The register method adds objects to the registry using the following syntax:

```javascript

registry.register(target, heldValue[, unregisterToken]);

```

The method returns the registry object itself, allowing for method chaining. When called, it performs these primary actions:

- Registers the target object for garbage collection tracking

- Stores the heldValue associated with the target

- Maintains a weak reference to the unregisterToken, allowing for targeted removal

To unregister an object, developers call the registry's unregister method with the unregisterToken:

```javascript

registry.unregister(unregisterToken);

```

The unregister method removes the target value from the registry if it matches the registered object or provided unregisterToken. This method operates as follows:

- Takes the unregisterToken as its sole argument

- Removes the target value if a matching entry exists

- Uses weak references for all stored values, ensuring that objects can still be garbage collected

- Does not affect the registry's ability to call cleanup callbacks for other registered objects

- Returns the registry object itself, allowing for method chaining


## Callback Mechanism

When an object is garbage collected, its callback function is invoked with the held value as an argument. The callback function receives the held value passed during registration, allowing for precise cleanup operations specific to each object.

The cleanup callback mechanism operates as follows:

- Callbacks are not called synchronously, meaning the object may be reclaimed before the callback executes

- Callbacks may be called during the current JavaScript job or after it completes

- While callbacks are best used for non-critical operations, they help reduce memory usage by performing necessary cleanup tasks before an object is deleted

- The callback may be called for different objects simultaneously, making it suitable for managing multiple cleanup operations

- Certain scenarios prevent callback execution, including program shutdown, registry instance unreachability, or specific runtime conditions

Developers should implement fallback mechanisms for critical paths due to the non-deterministic nature of callback execution. For instance, the weakRefCache example demonstrates using FinalizationRegistry to manage image caching and cleanup efficiently while handling potential cleanup callback limitations.


## Timing and Considerations

The timing of cleanup callbacks is not guaranteed and may vary based on the JavaScript engine's implementation and runtime conditions. While the callback may be called immediately after the object becomes unreachable, it is equally likely to be delayed until after the current JavaScript job completes. This behavior ensures that the callback runs only after the object has been successfully removed from memory, but developers should not rely on this timing for critical operations.

In certain scenarios, cleanup callbacks may not be called at all. These cases include:

- When the JavaScript program fully terminates

- When the FinalizationRegistry instance itself becomes unreachable

- When the object that created the registry goes out of scope or is deleted

The garbage collection process is managed entirely by the JavaScript engine and cannot be directly controlled by developers. This fundamental aspect of JavaScript's memory management model means that objects may be reclaimed at any time and that cleanup callbacks follow a best-effort execution pattern.

To demonstrate the timing variability, consider the following example code:

```javascript

const registry = new FinalizationRegistry(value => {

  console.log(value);

});

function performGarbageCollectionTest() {

  const testObject = {};

  registry.register(testObject, "Garbage collected");

  

  // Force garbage collection

  global.gc(); // Note: Requires running Node.js with --expose-gc flag

}

// The output may show the counter value smaller than 5000, demonstrating

// that the callback can execute before all allocations have occurred

```

Developers should implement fallback mechanisms for critical operations due to the non-deterministic nature of callback execution. For instance, the weakRefCache example demonstrates using FinalizationRegistry to manage image caching and cleanup efficiently while handling potential cleanup callback limitations.


## Browser Support and Implementation

FinalizationRegistry is implemented in major browsers since April 2021, with varying levels of support across different environments. The feature is available in Chrome 84, Edge 84, Firefox 79, and Android versions 84 and above, though support may vary in specific runtime conditions.

The constructor function allows creating a FinalizationRegistry instance with the specified callback, requiring the callback to be a function. Both the constructor and its methods are part of the WeakRefs proposal and are defined in the ECMAScript 2026 Language Specification.

The FinalizationRegistry constructor requires the `--harmony-weak-refs` runtime flag in Node.js version 13.0.0 and above. The feature is not natively supported in Internet Explorer, Opera, Safari, or Samsung Internet.

Browser compatibility includes support for key properties and methods such as constructor property, Symbol.toStringTag property, and standard JavaScript methods and properties. However, some non-standard and deprecated features are present in instances, including `__defineGetter__`, `__defineSetter__`, `__lookupGetter__`, `__lookupSetter__`, and `arguments` property.

To utilize FinalizationRegistry effectively, developers can employ techniques such as registering objects using the IIFE pattern to ensure they become eligible for garbage collection. For manual GC invocation, developers can use the Memory tab in Developer Tools, though direct API access to the garbage collector is restricted for security reasons.

