---

title: JavaScript Atomics exchange() Method

date: 2025-05-26

---


# JavaScript Atomics exchange() Method

JavaScript's Atomics API provides a powerful set of tools for performing atomic operations on shared memory. These operations enable developers to implement efficient multithreading and concurrent programming techniques directly within the language. This article explores the Atomics.exchange() method, a fundamental atomic operation that performs a value replacement in a typed array while returning the previous value. Through detailed examples and technical explanations, we'll examine how this method works, its implementation across different browsers, and its role in building safe, concurrent JavaScript applications.


## How Atomics.exchange() Works

Atomics.exchange() operates by atomically replacing the value at a specified position in a typed array with a new value while simultaneously returning the previous value at that position. This operation is performed using a shared integer typed array such as Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, BigInt64Array, or BigUint64Array.

The method takes three parameters: the typed array, the index at which to perform the exchange, and the new value. It returns the old value that was present at the specified position before the exchange occurred.

The operation ensures that no other writes can occur between reading the old value and writing the new value, providing atomicity that prevents race conditions and data corruption in concurrent environments.


### Example Usage

Creating a SharedArrayBuffer with 16 bytes:

```javascript

let sab = new SharedArrayBuffer(16);

let ta = new Uint8Array(sab);

```

Setting an initial value:

```javascript

ta[0] = 40;

```

Exchanging and retrieving the old value:

```javascript

console.log(Atomics.exchange(ta, 0, 20)); // Outputs: 40

console.log(Atomics.load(ta, 0)); // Outputs: 20

```


### Technical Details

The operation is available across multiple devices and browser versions since December 2021. Supported browsers include Google Chrome, Microsoft Edge, Firefox, Opera, and Safari.


### Implementation Notes

As of 2018, SharedArrayBuffer support was disabled in Chrome to reduce speculative side-channel attacks. Firefox disabled support by default for similar reasons, with preferences controlling feature availability. The Atomics object itself is not a constructor and cannot be used with the new operator or invoked as a function.


## Supported Data Types and Methods

The Atomics.exchange() method operates on any of the following integer typed arrays: Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, BigInt64Array, and BigUint64Array. Each of these types must be used in a shared context, specifically a SharedArrayBuffer. The method takes three parameters: the typed array, an index within the array bounds, and the new value to be exchanged.

The operation does not require the new value to match the existing value at the specified index. Instead, it performs an unconditional exchange of values at the given position. This atomic operation ensures that no other write operations can interrupt the process between reading the old value and writing the new value, preventing race conditions and data corruption in concurrent environments.

Compared to Atomics.compareExchange(), which requires the new value to match the current value before performing the exchange, Atomics.exchange() always performs the write operation and returns the original value at the specified position. Both methods provide atomicity through similar mechanisms, but Atomics.compareExchange() offers the additional functionality of conditional updates.

Common error conditions include TypeError when the typed array type does not match the allowed integer types, TypeError when the typed array is not shared, and RangeError when the index exceeds the array bounds. These error conditions help ensure that operations are performed safely and correctly in a multi-threaded environment.


## Example Usage

The Atomics.exchange() method performs an atomic exchange of values at a specified position in an integer typed array, returning the old value at that position. This operation ensures no writes occur between reading the old value and writing the new value, providing atomicity for concurrent programming scenarios.

A practical usage example demonstrates the method's functionality:

```javascript

let sharedBuffer = new SharedArrayBuffer(32);

let int32Array = new Int32Array(sharedBuffer);

Atomics.store(int32Array, 0, 42);

const value = Atomics.load(int32Array, 0);

console.log(value); // Outputs: 42

const oldValue = Atomics.add(int32Array, 0, 10);

console.log(oldValue); // Outputs: 42

console.log(int32Array[0]); // Outputs: 52

```

This example creates a shared buffer and view, initializes an element, performs a load operation, adds a value, and demonstrates the method's atomic nature through sequence consistency.

The method demonstrates consistent behavior across supported browsers, with compatibility available since December 2021 across Chrome, Edge, Firefox, Opera, and Safari. As of 2022, the feature has been widely adopted with robust support across major browser implementations.


## Common Use Cases

Atomic operations like exchange provide the foundation for safe multithreading and shared memory access. They enable developers to perform complex concurrent operations while maintaining data consistency and avoiding race conditions.


### Basic Operations and Use Cases

The Atomics object provides a set of fundamental atomic operations, including exchange, compare and exchange, wait, and notify. These operations enable basic inter-thread communication, such as setting stop flags and status indicators. The exchange operation, in particular, serves as a building block for more complex operations, allowing developers to implement custom atomic behaviors.


### Advanced Features and Applications

The compare and exchange operations demonstrate the flexibility and generality of atomic primitives. These operations can be used to implement advanced synchronization constructs, such as mutual exclusion locking and condition variables. For example, a simple mutex implementation can be constructed using compare and exchange operations to manage access to shared resources.


### Performance Considerations

The efficiency of atomic operations varies across different platforms and use cases. While atomic operations provide strong guarantees about data consistency, they often come with additional overhead compared to non-atomic operations. Modern JavaScript engines optimize atomic operations for common cases, but developers should consider profiling to identify potential bottlenecks.


### Best Practices

The Atomics object enables efficient thread coordination without requiring manual implementation of complex synchronization primitives. However, developers should be aware of platform limitations and choose appropriate atomic operations based on their specific requirements. For simple cases, basic operations like add and exchange often provide sufficient functionality, while more complex use cases may require specialized implementations.


## Browser Support

The Atomics.exchange() method is supported across multiple browsers and environments, with varying levels of availability and implementation details. Here's a breakdown of its compatibility:


### Desktop Browsers

- **Chrome**: Full support since version 68. However, shared memory support was disabled on January 5, 2018, to mitigate speculative side-channel attacks. Users need to enable the `javascript.options.shared_memory` preference for versions 57 and above.

- **Edge**: Full support since version 79 with similar restrictions to Chrome. Shared memory support was disabled on January 5, 2018, requiring the same preference setting for versions 57 and above.

- **Firefox**: Full support since version 78 with the same disabling mechanism as Chrome and Edge. Shared memory support was disabled from January 5, 2018, requiring the `javascript.options.shared_memory` preference for versions 57 and above.

- **Internet Explorer**: No support

- **Opera**: No support

- **Safari**: Full support since version 10.1, though implementation details are limited compared to other engines. Shared memory support was disabled to mitigate speculative execution side-channel attacks, requiring the same preference setting for versions 57 and above.


### Mobile Browsers

- **Android WebView**: No support from version 60 to 63, with the same restrictions as desktop browsers. Shared memory support was disabled on January 5, 2018, requiring the `javascript.options.shared_memory` preference for versions 57 and above.

- **Android Chrome**: Similar restrictions to Android WebView with no support from version 60 to 63.

- **Android Firefox**: Full support since version 57 with the same restrictions as desktop Firefox. Shared memory support was disabled from version 46 to 55, requiring the `javascript.options.shared_memory` preference for versions 57 and above.

- **Android Opera**: No support

- **Android Safari**: No support from version 10.3 to 11.3

- **Samsung Internet Android**: No support


### Other Environments

- **Node.js**: Full support since version 8.10.0

- **iOS Safari**: No support from version 10.3 to 11.3


### Shared Memory Considerations

The implementation of Atomics.exchange() relies heavily on SharedArrayBuffer support, which has faced significant browser restrictions. Chrome, Edge, and Firefox all disabled shared memory support starting January 5, 2018, to mitigate speculative side-channel attacks. To enable these features, users must set the `javascript.options.shared_memory` preference to `true` for versions 57 and above across these engines.

Developers should be aware that even with these settings, compatibility issues may arise across different versions and platforms. Performance considerations also vary, with modern JavaScript engines optimizing atomic operations for common cases but potentially introducing overhead for developers implementing complex multithreading scenarios.

