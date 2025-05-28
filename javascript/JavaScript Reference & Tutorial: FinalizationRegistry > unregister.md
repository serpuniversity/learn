---

title: JavaScript FinalizationRegistry: unregister Method

date: 2025-05-26

---


# JavaScript FinalizationRegistry: unregister Method

In JavaScript, managing memory and ensuring proper cleanup of resources is crucial for maintaining efficient and reliable applications. The FinalizationRegistry provides a powerful mechanism for finalization, allowing developers to notify when objects are no longer referenced. This built-in object enables registration of objects for cleanup during garbage collection, but requires careful management of unregistration tokens to prevent premature garbage collection or missed cleanups. This article explores the unregister method in detail, examining its parameters, behavior, and implementation to help developers master memory management with FinalizationRegistry.


## Overview of FinalizationRegistry

The FinalizationRegistry object in JavaScript offers a mechanism for finalization, allowing objects to notify when they're no longer referenced. This built-in object enables developers to register objects for cleanup when they're garbage collected, managing memory usage without preventing the garbage collector from reclaiming unreachable objects.

To use the FinalizationRegistry, developers create an instance by passing a callback function to the constructor. The register method then associates objects with these callbacks, taking two parameters: the target object and a held value that will be passed to the cleanup callback. This held value can be any JavaScript value, including primitives, objects, or undefined. For unregistering registered values, the unregister method requires a third parameter: the unregistration token, which should match the target value or be a different registered token. This token mechanism enables developers to selectively unregister objects while maintaining weak references to prevent premature garbage collection.

The registry itself maintains only weak references to registered objects, ensuring they can be reclaimed by the garbage collector. When an object is garbage collected, the registry's callback may be invoked with the held value. While the cleanup callback mechanism helps reduce memory usage throughout program execution, developers should not rely on these callbacks for essential logic due to unpredictable timings and implementation differences across JavaScript engines.


## Register Method

The register method takes three parameters: the target object, the held value, and an optional unregister token. The target must be an object or a non-registered symbol, while the held value can be any JavaScript value, including primitives, objects, or undefined. Notably, the held value cannot be the same as the target object.

The method registers the target object with the registry, maintaining a strong reference to the held value if it is an object. This strong reference ensures that the held value remains accessible to the cleanup callback when the target object is garbage collected. However, the registry itself maintains only weak references to the target objects, allowing them to be reclaimed by the garbage collector.

When used with itself as the unregister token, the register method works by storing both the target object and its label in the registry. This allows later calls to the unregister method to remove the associated target value. Alternatively, the method can register a target object with a different object as the unregister token, enabling more flexible management of registered values.


## Unregister Method

The unregister method removes an object from the finalization registry, accepting a single parameter: the unregisterToken. This token must be an object or a non-registered symbol, matching the target value used during registration.

The method returns a boolean value: true if at least one cell was unregistered and false if no cells were unregistered. It throws a TypeError if the unregisterToken is not valid, maintaining type safety for registry operations.

Multiple cells registered with the same unregisterToken are unregistered together. The registry automatically unregisters target values when they're reclaimed, so cleanup callbacks are only needed if the target value hasn't already received one.

In practice, two main scenarios apply:

1. When a target object is registered using itself as the unregister token, unregistering with the same object maintains consistency.

2. When a target object is registered using a different object as the unregister token, unregistering with that object enables flexible management of registered values.

This method implements core functionality for finalization registry maintenance, ensuring that registered objects can be selectively removed while maintaining weak references to prevent premature garbage collection.


## Parameter Requirements

The unregister method requires a single parameter: the unregistration token. This token must be either an object or a non-registered symbol and must match the token used during registration.

If the unregistration token is an object, it must uniquely identify the target value. The registry maintains weak references to these tokens, allowing multiple cells registered with the same token to be unregistered together. This token mechanism enables developers to selectively unregister objects while maintaining weak references to prevent premature garbage collection.

The method returns a boolean value: true if at least one cell was unregistered and false if no cells were unregistered. It throws a TypeError if the unregistration token is not valid, maintaining type safety for registry operations. The registry automatically unregisters target values when they're reclaimed, so cleanup callbacks are only needed if the target value hasn't already received one.

The behavior of the unregister method is consistent across the registry's implementation, with both MDN and @fastly/js-compute documentation reporting identical requirements and functionality. The method operates independently of the target object's type or held value, focusing solely on the registration token provided during the initial registration process.


## Method Behavior

The method returns true if at least one cell was unregistered and false if no cells were unregistered. This boolean feedback enables developers to verify the success of the unregistration operation, facilitating robust memory management practices. The method's return value of false indicates that the specific unregisterToken did not match any registered entries, while true confirms successful removal of one or more cells.

The implementation consistently returns a boolean value to provide clear feedback on the operation's success:

- When unregistering with the same object used during registration, the method returns true if the object was successfully unregistered.

- When using a different object as the unregister token, the method also returns true if the associated target value is removed from the registry.

The method's behavior has been validated across multiple sources, including the @fastly/js-compute documentation and the MDN JavaScript guide, which report identical functionality for determining successful unregistration operations.

