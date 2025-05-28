---

title: JavaScript FinalizationRegistry: register Method in Depth

date: 2025-05-26

---


# JavaScript FinalizationRegistry: register Method in Depth

JavaScript's FinalizationRegistry provides a mechanism for performing automatic cleanup tasks when objects are garbage collected. The register method is central to this functionality, allowing developers to schedule cleanup operations for specific targets. This article examines the details of the register method, including its fundamental behavior, implementation requirements, and practical applications, while highlighting the variability in its behavior across different JavaScript engines and versions.


## Register Method Fundamentals

The register method of JavaScript's FinalizationRegistry allows developers to schedule cleanup tasks for objects during garbage collection. This core functionality works by creating a registry object with a callback function, which receives a held value associated with each registered target object.

The method takes two required parameters: the target value and the held value. The target value is the object to be registered for cleanup, while the held value is passed to the cleanup callback when the target is reclaimed. Developers can optionally provide a unregisterToken, which must be an object and serves as a key for later removal of the registered target.

Garbage collection behavior varies across JavaScript engines and versions, as the proposal notes that collectors are complex with varying object collection times and heuristics. While cleanup callbacks help reduce memory usage, developers should not rely on them for essential program logic due to implementation differences across engines and versions.


## Method Syntax and Parameters

The register method requires a target object and a held value, with optional unregistration token. The method's syntax is `registry.register(target, heldValue [, unregisterToken])`, where target is the object to register, heldValue is passed to the cleanup callback when the target is reclaimed, and unregisterToken is an optional object used to unregister the target later.


### Parameters and Requirements

- The target parameter must be an object or a non-registered symbol, and must not be the same reference as the heldValue (`target !== heldValue`).

- The heldValue can be any value, including an object, function, or primitive type.

- The unregisterToken must be provided as an object if used, and serves as a reference for later removal of the target value.


### Validation and Behavior

The method performs several checks before successfully registering the target:

- Validates that the target is an object or a non-registered symbol.

- Ensures the target is not the same reference as the heldValue to prevent circular references.

- Validates that unregisterToken (if provided) is an object to maintain consistency with registration requirements.


### Method Return and Exceptions

The method returns `undefined`, adhering to its specified return value. It throws exceptions under specific conditions:

- Throws a TypeError if the target is not an object or is the same as the heldValue.

- Throws a TypeError if unregisterToken is not provided and is required for unregistration.

This method implementation requires careful handling of object references and token validity to prevent memory management issues while providing flexible cleanup capabilities.


## Behavior and Implementation Notes

The behavior of the `register` method and its associated cleanup callbacks varies significantly depending on JavaScript engine implementation and garbage collection strategies, as noted in the proposal for `FinalizationRegistry`. Garbage collectors are complex systems with varying collection timings and implementation details, making the behavior of `register` and its callbacks highly dependent on both engine-specific algorithms and runtime conditions.

Key aspects of this implementation variability include:

1. Object collection timing: Garbage collection techniques such as generational collection, incremental collection, and concurrent operations introduce significant unpredictability. Engine runtime heuristics balance memory management with application responsiveness, while closures and inline caches maintain references to objects in ways that can affect garbage collection timing.

2. Cleanup callback invocation: Callbacks are not guaranteed to run immediately after object deletion, and their execution can be delayed until after the current JavaScript event loop completes. The registry does not prevent the cleanup callback from running multiple times, particularly for objects in different registries, though developers should expect the possibility of delayed or absent callbacks under certain conditions.

3. Program termination considerations: Cleanup callbacks may not be called when the JavaScript program fully terminates or when the `FinalizationRegistry` instance becomes unreachable. This behavior differs between implementations and should not be relied upon for essential program logic.

Development patterns that leverage these implementation details include managing temporary data structures and lazy initialization, where automatic cleanup of unused objects can significantly reduce memory overhead. However, developers must account for the unpredictable nature of `FinalizationRegistry` behavior across engines and versions to avoid critical application dependencies on cleanup callbacks.


## Use Cases and Best Practices

FinalizationRegistry targets specific application patterns where automatic cleanup of unused objects can significantly reduce memory overhead. Primary use cases include external resource management, debugging, and complex lifecycle scenarios requiring automated object cleanup.


### External Resource Cleanup

Developers frequently use FinalizationRegistry to manage resources that should be closed or released when no longer needed, such as file handles, network connections, or database connections. For example, a file management system might register each opened file with a FinalizationRegistry instance, allowing the system to automatically close the file when it's no longer referenced by the application.


### Debugging

The registry provides a powerful debugging tool for tracking object lifetimes. By associating a cleanup callback with each object, developers can log or trace when objects are removed from memory. This feature helps identify memory leaks or unexpectedly long-lived objects in complex applications.


### Complex Lifecycle Management

The registry excels in scenarios where objects have complex lifecycles requiring multiple cleanup operations. For instance, a UI framework might use FinalizationRegistry to manage event listeners and UI state. When an element is removed from the DOM, the associated registry entries ensure all related listeners and state data are properly cleaned up.


### Implementation Considerations

While FinalizationRegistry offers significant benefits, developers must carefully consider its implementation details and limitations. The cleanup callback mechanism is not suitable for essential program logic due to implementation differences across engines and versions. Garbage collection behavior varies significantly between engines and versions, with callbacks potentially delayed or omitted under certain conditions.


### Best Practices

To effectively use FinalizationRegistry, developers should:

- Use sparingly, limiting implementation to specific use cases

- Prefer WeakRef for caching and lazy initialization

- Regularly review and test cleanup behavior across different JavaScript environments

- Avoid critical program logic dependencies on cleanup callbacks

- Monitor application performance to prevent potential overhead


## Browser Compatibility and Runtime Flags

The `register` method requires specific runtime flags for activation across different JavaScript environments, including browsers and Node.js with version dependencies.

Browser compatibility varies significantly:

- Full support: Firefox 79, Chrome 84, Edge 84

- Partial support: Safari 84, Android webview 84, Chrome Android 84, Firefox Android, Opera Android, Safari iOS, Samsung Internet Android

- No support: Internet Explorer, Opera, Safari on iOS, Samsung Internet Android

To enable the feature in browsers:

- Firefox: Use the `--harmony-weak-refs` runtime flag

- Node.js: Use the `--harmony-weak-refs` flag, available from version 13.0.0 and above

The method signature is:

```javascript

FinalizationRegistry.prototype.register(target, heldValue)

FinalizationRegistry.prototype.register(target, heldValue, unregisterToken)

```

Parameters:

- `target`: The target value to register. Must be an object or a non-registered symbol (not primitives or functions)

- `heldValue`: The value to pass to the finalizer for this target. Cannot be the target itself but can be anything else, including functions and primitives

- `unregisterToken`: Optional. A token that may be used with the unregister method later to unregister the target. Must be an object or a non-registered symbol. If not provided, the target cannot be unregistered

The method returns `undefined`, adhering to its specified return value. It throws exceptions under specific conditions:

- Throws a TypeError if the target is not an object or is the same as the held value (`target === heldValue`)

- Throws a TypeError if unregisterToken is not provided and is required for unregistration

