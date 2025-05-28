---

title: JavaScript Proxy: handler.preventExtensions

date: 2025-05-26

---


# JavaScript Proxy: handler.preventExtensions

In JavaScript, controlling an object's mutability is crucial for maintaining data integrity and ensuring predictable behavior. While traditional methods like `Object.seal()` and `Object.freeze()` provide basic protection, modern JavaScript engines offer more sophisticated tools through Proxy objects. The `handler.preventExtensions` trap, specifically, allows developers to intercept and customize operations that affect an object's extensibility.

This article explores how `handler.preventExtensions` works, its relationship with the `Object.preventExtensions` and `Reflect.preventExtensions` methods, and its implementation details. We'll examine how this trap interacts with other sealing and freezing operations, discuss best practices for its implementation, and demonstrate its behavior across different JavaScript engines. Through practical examples and browser compatibility information, you'll learn how to leverage this powerful feature to maintain control over your objects' mutable state.


## Overview of Proxy.handler.preventExtensions

The `Object.preventExtensions(target)` method prevents further properties from being added to an object. This method is intercepted by the `handler.preventExtensions` trap in JavaScript Proxies. When `handler.preventExtensions` is defined, it acts as a custom behavior handler for both `Object.preventExtensions` and `Reflect.preventExtensions`.

The `handler.preventExtensions` trap must return a boolean value indicating whether the operation was successful. If the target object's extensibility changes to non-extensible after calling `handler.preventExtensions`, then the trap must also return `true`. Violation of this invariant results in a TypeError.

This feature is supported across multiple ECMAScript versions, with specific implementations available since ES2015 (ECMA-262) and detailed specifications in ECMAScript 2026 Language Specification (section 2.14.14.1 "Proxy Object Internal Methods and Internal Slots - preventExtensions"). Modern JavaScript engines include detailed support through browser compatibility features available since September 2016.

A common implementation involves returning `true` only if `Reflect.isExtensible()` on the target object returns `false` after the handler call. This ensures proper behavior while maintaining consistency with object extensibility status. Alternative approaches include synchronizing the target's extensibility state by modifying both the target and proxy objects accordingly.


## Method Definition and Return Value

The `handler.preventExtensions` trap must return a Boolean value, with 'true' indicating the operation's success. The trap intercepts four specific operations: `Object.preventExtensions()`, `Reflect.preventExtensions()`, `Object.seal()`, and `Object.freeze()`. Modern JavaScript engines support this feature since September 2016.

The method is defined in multiple ECMAScript specifications. In ES2015 and ES2017, the return value is a boolean indicating whether the operation was successful. The specification explicitly states that `Object.preventExtensions(proxy)` should only return true if `Object.isExtensible(proxy)` returns false. Violations of this invariant result in a TypeError.

Implementations must adhere to specific requirements. The trap must return true only if Reflect.isExtensible() on the target object returns false after the handler call. This ensures proper behavior while maintaining consistency with object extensibility status. Alternative approaches include synchronizing the target's extensibility state by modifying both the target and proxy objects accordingly.


## Implementation Examples and Best Practices

const p = new Proxy({}, { preventExtensions: function(target) {

    console.log('preventExtensions()');

    console.log(Object.preventExtensions(target));

    return true;

} });

console.log(Object.preventExtensions(p));

let x = { first: false };

let y = { preventExtensions(target) {

    target.canEvolve = false;

    Object.preventExtensions(target);

    return true;

} };

let proxy = new Proxy(x, y);

console.log(x.first);

Object.preventExtensions(proxy);

console.log(x.first);

The supported browsers are:

- Google Chrome 49 and above

- Edge 12 and above

- Firefox 22 and above

- Opera 36 and above

- Safari 10 and above


## Compatibility and Browser Support

The `handler.preventExtensions` trap began its implementation in ECMAScript 2015 and has since been supported across major browser versions, with official support beginning in September 2016. Modern JavaScript engines, including Google Chrome, Edge, Firefox, Opera, and Safari, all provide complete implementation from their respective version 49, 12, 22, 36, and 10 milestones.

The trap operates as a fundamental mechanism for intercepting operations that affect an object's extensibility, including `Object.preventExtensions`, `Reflect.preventExtensions`, and the equivalent operations from sealing and freezing objects. This ensures developers can maintain control over an object's mutable state while providing a consistent interface for managing object properties.

Browser compatibility details are documented in the ECMAScript specifications for both ES2015 and ES2017, with additional support noted in the implementation notes for later versions. The feature's widespread adoption across modern JavaScript engines demonstrates its importance in managing object state and preventing unintended modifications.

