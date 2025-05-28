---

title: JavaScript Proxy: getOwnPropertyDescriptor

date: 2025-05-26

---


# JavaScript Proxy: getOwnPropertyDescriptor

JavaScript proxies provide a powerful mechanism for intercepting and customizing object property access. This article focuses on the getOwnPropertyDescriptor trap, which allows proxies to control how target properties are represented as property descriptors. Through detailed examination of this trap's implementation and behavior, we'll explore how proxies maintain compatibility with existing ES5 code while enabling advanced property manipulation techniques.


## Method Overview

The `getOwnPropertyDescriptor` trap operates at the MOP (Memory Operations Protocol) level, computing both Property Descriptor fields and an [[Origin]] object for Proxy target properties. This method supports both data and accessor descriptors while adhering to internal invariant constraints.

For custom property descriptor handling, the trap can intercept operations like `Object.getOwnPropertyDescriptor()` and `Reflect.getOwnPropertyDescriptor()`, returning either an Object or undefined as per the specification. This interception allows proxies to censor built-in attributes while maintaining compatibility with existing ES5 code. When using `Object.freeze({})` as the proxy target, the trap ensures that reported descriptors are consistent with the target's own properties and extensibility constraints.

The method correctly implements ES6 standards by returning descriptors that adhere to the following criteria:

- Configurable properties are set to false for frozen targets

- Enumerable properties are only reported for existing own properties

- Writable properties are true only if the property exists as a writable own property of the target

- Value and getter/setter properties are correctly reported based on the target object's actual descriptor values

While the [[Origin]] field allows handlers to produce non-standard descriptors, the specification now limits descriptor objects to data and accessor formats, preventing proxies from introducing new types of property descriptors. This approach maintains compatibility with existing code while allowing proxies to extend functionality through alternative metadata mechanisms.


## Property Descriptor Fields

The getOwnPropertyDescriptor trap returns a Property Descriptor object with several key attributes:

Configurable: This attribute indicates whether the property can be deleted and whether its attributes can be changed. For non-configurable properties, this value is false.

Enumerable: This attribute determines if the property appears in for-in loops and object property enumeration. Non-enumerable properties have this value set to false.

Writable: This attribute specifies whether the property's value can be modified. Non-writable properties have this value set to false.

Value: This attribute holds the property's value. For data properties, it contains the actual value. For accessor properties, it may contain a default value or be undefined.

The trap correctly implements ES6 standards by adhering to several invariants:

- A property cannot be reported as configurable if it does not exist as an own property of the target object or if it exists as a non-configurable own property of the target object.

- A property cannot be reported as writable if it does not exist as an own property of the target object or if it exists as a non-writable own property of the target object.

- A property cannot be reported as enumerable if it does not exist as an own property of the target object or if it exists as a non-enumerable own property of the target object.

These invariants allow descriptors to support user-invented descriptor properties while maintaining the integrity of the target object's properties. For example, when using Object.defineProperty(), default values for writable, enumerable, and configurable attributes are false unless explicitly set.

The trap's behavior aligns with language standards, though it differs in some cases from direct property access. For instance, Symbol properties always return false for writable and enumerable attributes, while non-object arguments throw TypeError in ES5 rather than being coerced to objects as in ES2015.


## Origin Object

The [[Origin]] object serves a crucial role in the Proxy mechanism by allowing handlers to produce non-standard descriptors while the language itself only uses Property Descriptor fields. This capability enables Proxies to define their own property descriptor formats that they expose to and accept from user code, including the ability to store property metadata in forms other than complete descriptor objects.

The [[Origin]] field is particularly important because the getOwnPropertyDescriptor trap returns an internal record rather than a standard object, which means that Object.getOwnPropertyDescriptor will return an object missing most of the properties callers expect to receive. The Proxy mechanism supports both data and accessor descriptors, allowing for complex scenarios such as creating a typed array-like structure without indexed property attributes, where zero-valued properties might return only {value: 0} as the descriptor.

Despite the flexibility this provides, the specification makes several critical decisions to maintain compatibility and integrity. First, it restricts proxies from changing certain ES6-defined fields, meaning that while Proxy objects can add other fields to property descriptor objects, they cannot alter the behavior of value, writable, set, get, enumerable, and configurable attributes. Second, it requires that any descriptor returned from the handler must only use data properties for attributes, particularly for non-configurable properties which must exist on the target.

Firefox, the browser implementing this functionality, initially faced challenges with the [[Origin]] object. However, the specification team, including Allen and Mark, has worked to address these issues, ensuring that the resulting design maintains essential language invariants while providing the flexibility needed for advanced Proxy use cases. This work has involved careful consideration of how to balance extension capabilities with compatibility requirements, leading to a more refined understanding of Proxy's role in JavaScript's memory operations protocol.


## ES vs. Script Behavior

The Proxy mechanism operates at a fundamental level of JavaScript's memory operations protocol, where it computes Property Descriptor fields and an [[Origin]] object for target properties. This detailed approach allows proxies to operate flexibly while maintaining compatibility with existing ES5 code.

In practice, the ES language uses only the Property Descriptor fields for its operations. However, JavaScript scripting environments can access the [[Origin]] object, which enables proxies to produce non-standard descriptors while the language itself adheres to standard Property Descriptor fields. This distinction is particularly relevant when considering the differences between ES6 and ES5 implementations.

Implementation details reveal that the [[Origin]] field allows handlers to create custom descriptors that they can expose to and accept from user code. This capability is especially useful for scenarios where proxies need to define their own property descriptor formats, such as creating typed array-like structures without indexed property attributes. For example, a proxy could return only {value: 0} as the descriptor for zero-valued properties, maintaining flexibility while adhering to JavaScript's fundamental design principles.

The specification team, including Allen and Mark, has addressed several implementation challenges in Firefox through careful design decisions. While the [[Origin]] object was initially problematic, the current approach ensures that proxies remain compatible with existing ES5 behavior. The specification limits proxies' ability to modify certain ES6-defined fields, requiring that any descriptor returned from the handler must only use data properties for attributes. This restriction particularly applies to non-configurable properties, which must exist on the target object.

Despite these complexities, the current implementation maintains crucial language invariants while providing the necessary flexibility for advanced Proxy use cases. The decision to remove [[Origin]] from descriptor objects and revert to fresh, normalized descriptor creation ensures complete backward compatibility with ES5 behavior, preventing proxies from manipulating descriptor objects in ways that could break existing client code.


## Performance Considerations

The creation process is efficient, but handler traps can introduce 5-20% performance overhead compared to direct property access. This overhead is particularly noticeable when proxied objects are used as function parameters or return values, as the proxy mechanism introduces additional function calls.

The performance impact of traps varies based on the specific operations being intercepted. The set trap, for example, experiences higher overhead due to its need to handle dynamic property assignments. In contrast, traps that only check for property existence (like the has trap) experience minimal performance impact.

While the current implementation maintains compatibility with existing ES5 code, developers should be aware that proxies can significantly impact performance in certain scenarios. This is particularly relevant when proxies are used on frequently accessed objects or when working with performance-critical applications.

To minimize performance impact while maintaining functionality, developers are encouraged to carefully consider which traps are necessary for their implementation. The recommended approach is to use proxies sparingly in production applications, reserving their use for specific scenarios where custom property behavior is required.

