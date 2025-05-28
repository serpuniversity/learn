---

title: JavaScript Reference & Tutorial: Reflect.ownKeys

date: 2025-05-26

---


# JavaScript Reference & Tutorial: Reflect.ownKeys

Enumerating an object's properties in JavaScript can be surprisingly complex, particularly when you need to account for non-enumerable properties and symbols. While methods like Object.keys provide a basic way to list string keys, they fall short when you need a complete picture of an object's state. In this article, we explore the Reflect.ownKeys method, which addresses these limitations by returning all of an object's own property keys, including strings and symbols, while maintaining a specific order that makes sense for how objects are typically structured. This powerful tool helps developers effectively manage object state and implement more robust property enumeration logic.


## Method Overview

Reflect.ownKeys returns an array of an object's own property keys, including both strings and symbols. This array represents all properties directly found upon the object, with the order determined by specific criteria: numeric indexes in ascending order (as strings), other string keys in insertion order, and symbol keys also in insertion order. The method's implementation follows these rules for ordering keys: numeric indexes first, then strings in their insertion order, and finally symbols in their insertion order.

The method's return value is equivalent to combining the results of Object.getOwnPropertyNames(target) and Object.getOwnPropertySymbols(target), ensuring that all own properties - both enumerable and non-enumerable, as well as string and symbol keys - are included. This is distinct from Object.keys, which only returns enumerable string keys. The behavior is consistent across most objects, with numeric indexes appearing as strings in ascending order, followed by string keys in their insertion order, and finally symbol keys in their insertion order.

The method performs this operation through the target object's internal [[OwnPropertyKeys]] method, providing a unified way to retrieve all own properties without the need for additional filtering logic. While environments generally return properties in a predictable order similar to that of Reflect.ownKeys, the method guarantees this consistent behavior across implementations.


## Implementation Details

The method follows specific rules for ordering keys, with non-negative integer indexes appearing as strings in ascending order, followed by string keys in their insertion order, and finally symbol keys in their insertion order. This order is guaranteed by the specification and is required by the internal [[OwnPropertyKeys]] method, which is invoked by Reflect.ownKeys.

For most objects, the array returned by Reflect.ownKeys will follow this order: numeric indexes as strings in increasing numeric order, other string keys in the order they were inserted onto the object, and symbol keys in the order of their creation. The method's return value is equivalent to concatenating the results of Object.getOwnPropertyNames(target) and Object.getOwnPropertySymbols(target), providing a unified way to retrieve all own properties without additional filtering logic.

The method works consistently with both objects and arrays. For objects, it returns an array containing all own property keys, while for arrays, it returns an array containing only the "length" property. The method invokes the target object's internal [[OwnPropertyKeys]] method to perform this operation, and under normal circumstances, the order of keys returned by this method matches the order specified in the implementation details.

While environments generally return properties in a consistent order similar to Reflect.ownKeys, the method ensures this predictable behavior across all implementations. The method's return value is an Array of the target object's own property keys, including strings and symbols, and it correctly handles both extensible and non-extensible objects.


## Compatibility

The method is specified in the ECMAScript 2026 Language Specification under the section for Reflect.ownKeys. It is supported in Chrome 49+, Edge 12+, Firefox 42+, Opera 36+, and Safari 10+ across desktop, while also being available in recent versions of Chrome Android 49+, Edge Android 12+, Firefox Android 18+, Opera Android 36+, Safari iOS 10+, and Android WebView 49+.

The method works with both objects and arrays. For objects, it returns an array containing all own property keys in ascending numeric order for indexes, followed by string keys in their insertion order, and finally symbol keys in their insertion order. For arrays, it returns an array containing only the "length" property. The method invokes the target object's internal [[OwnPropertyKeys]] method to perform this operation, ensuring consistent behavior across implementations.

The method's return value is equivalent to [Object.getOwnPropertyNames(target)].concat([Object.getOwnPropertySymbols(target)]), providing a unified way to retrieve all own properties without additional filtering logic. It correctly handles both extensible and non-extensible objects, returning all own properties of the target object in the specified order. The method can handle proxy objects with custom [[OwnPropertyKeys]] methods, though the order of keys may differ in such cases.


## Use Cases

Reflect.ownKeys can be particularly useful when developers need to enumerate all properties of an object, including non-enumerable and symbol properties. Unlike Object.keys, which only returns enumerable string keys, Reflect.ownKeys provides a comprehensive view of an object's properties by combining the results of Object.getOwnPropertyNames(target) and Object.getOwnPropertySymbols(target).

This method is particularly powerful when working with objects that need to maintain internal state using non-enumerable properties. For example, a class might use non-enumerable properties to store private data while exposing methods through enumerable properties. Reflect.ownKeys allows developers to inspect all aspects of an object's internal state.

The ability to retrieve symbol keys also opens up possibilities for more sophisticated object manipulation. Symbols can be used as property keys to create unique identifiers that prevent clashes with existing property names. Reflect.ownKeys provides a consistent way to discover these unique properties, which might be critical for deep object inspection or serialization processes.

Developers can use this method to implement custom property enumeration logic. For instance, they might need to traverse all properties of an object, including those that would normally be skipped by for..in loops or JSON-based serialization. By combining the results of getOwnPropertyNames and getOwnPropertySymbols, Reflect.ownKeys offers an exhaustive way to work with an object's property set.

The method's role in proxy objects demonstrates its importance in advanced JavaScript programming. When working with proxies, developers often need to intercept and control property access. Reflect.ownKeys allows them to understand the complete set of properties that might affect the proxy's behavior, including those added through traps. This understanding is crucial for implementing robust proxy handlers that maintain the correct object state.

