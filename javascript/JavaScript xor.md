---

title: JavaScript Atomics: xor Operation

date: 2025-05-26

---


# JavaScript Atomics: xor Operation

In JavaScript's evolving landscape of concurrency and shared memory, bitwise operations play a crucial role in managing simultaneous access to critical resources. Among these operations, the bitwise XOR stands out for its simple yet powerful functionality in manipulating binary data. This article delves into the Atomics.xor() method, examining its implementation, behavior, and importance in maintaining data integrity across multiple threads. Through detailed explanations and practical examples, we'll explore how this atomic operation ensures consistent results in shared memory environments, making your multi-threaded JavaScript applications more reliable and efficient.


## xor Method Overview

The Atomics.xor() method performs a bitwise XOR operation on elements of a SharedArrayBuffer. This atomic operation ensures that no other write occurs until the modified value is written back.

The method requires three parameters:

- `typedArray`: The shared integer typed array to modify

- `index`: The position in the typedArray

- `value`: The number to compute the bitwise XOR with

For example:

```javascript

let buf = new SharedArrayBuffer(16);

let arr = new Uint8Array(buf);

arr[0] = 7;

console.log(Atomics.xor(arr, 0, 2)); // returns 5

console.log(Atomics.load(arr, 0));   // 5

```

The bitwise XOR operation returns 1 if the two operands are different, following this truth table:

```

a | b | a ^ b

---|---|------

0 | 0 | 0

0 | 1 | 1

1 | 0 | 1

1 | 1 | 0

```

As shown in the example, a bitwise XOR of 7 (0111 binary) and 2 (0010 binary) results in 5 (0101 binary).

The method throws exceptions when:

- `typedArray` is not one of the allowed integer types

- `typedArray` is not a shared typed array type

- `index` is out of bounds in the `typedArray`

The browser compatibility for the method is as follows:

- Chrome 60+

- Firefox 57+

- Edge No support

- Safari No support

- Opera No support


## Method Syntax and Parameters

The Atomics.xor() method operates on SharedArrayBuffer objects, which must be of integer type (Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, BigInt64Array, BigUint64Array). The method signature is Atomics.xor(arr, index, value), where arr is the typed array, index is the position within the array, and value is the number to compute the XOR with.

The method returns the old value at the specified position in the array, providing atomic operation semantics that prevent other writes from occurring until the modified value is written back. For example, performing a bitwise XOR with 2 on an array element initially set to 7 yields 5, while an operation with 5 on an element initially set to 3 results in 7.

The method throws exceptions for invalid inputs: a TypeError if the typedArray is not an integer type or not a shared typed array, and a RangeError if the index is out of bounds in the typedArray. The bitwise XOR operation follows this truth table: a ^ b, producing 1 if a and b are different. This operation is particularly useful for managing shared memory in multi-threaded environments, ensuring accurate read and write operations.


## Operation Behavior and Return Value

The operation yields 1 if the two operands are different, as shown in the truth table:

a | b | a ^ b

---|---|------

0 | 0 | 0

0 | 1 | 1

1 | 0 | 1

1 | 1 | 0

The method ensures atomicity through its operation semantics, preventing other write operations from occurring until the modified value is written back. This property is similar to other Atomics methods, ensuring consistent and reliable shared memory operations.

The method operates on SharedArrayBuffer objects containing Uint8Array, Uint16Array, or Uint32Array, returning the old value at the specified position. The returned value is the original contents of the array element before the operation, while the modified value is written back to the array.

The atomic operation nature of Atomics.xor() makes it suitable for multi-threaded environments where shared memory access must maintain consistency. The operation's outcome can be observed in the provided example, where a bitwise XOR of 12 with 1010 yields the original value of 12, demonstrating the method's ability to return the pre-operation state of the array element.


## Supported Data Types and Browser Compatibility

Atomics.xor() operates on SharedArrayBuffer objects containing Uint8Array, Uint16Array, or Uint32Array. The method requires that the provided typed array be of an integer type and shared, throwing a TypeError if these conditions are not met.

The method signature is Atomics.xor(arr, index, value), where arr is the typed array, index is the position within the array, and value is the number to compute the bitwise XOR with. It returns the old value at the specified index in the array. The operation is atomic, ensuring that no other write operations can occur until the modified value is written back.

The bitwise XOR operation follows this truth table: a ^ b, producing 1 if a and b are different. This operation is particularly useful for managing shared memory in multi-threaded environments, ensuring accurate read and write operations. For example, performing a bitwise XOR with 2 on an array element initially set to 7 yields 5, while an operation with 5 on an element initially set to 3 results in 7.

The method's implementation ensures that predicted values are written and read accurately, maintaining consistency in shared memory access. This atomic nature is demonstrated in the provided examples, where the method correctly returns the previous value before performing the operation, as seen in the code snippets where 7 XOR with 2 results in 5, and 3 XOR with 5 results in 7.


## Error Handling and Usage Considerations

The Atomics.xor() method requires specific parameters to function correctly:

- The typedArray must be one of the allowed integer types, including Uint8Array, Uint16Array, or Uint32Array

- The typedArray must be a shared typed array

- The index must be within the bounds of the typedArray

The method throws exceptions for invalid inputs:

- TypeError if the typedArray is not an integer type or not a shared typed array type

- RangeError if the index is out of bounds in the typedArray

The method's implementation ensures that predicted values are written and read accurately, maintaining consistency in shared memory access. This atomic nature is demonstrated in code examples where the method correctly returns the previous value before performing the operation. For instance, performing a bitwise XOR with 2 on an array element initially set to 7 yields 5, while an operation with 5 on an element initially set to 3 results in 7.

The method's browser compatibility spans Chrome 60+, Firefox 57+, Edge, Safari, and Opera, with notable exceptions for Edge, Safari, and Opera. Implementation details note that Chrome disabled SharedArrayBuffer on January 5, 2018, as a temporary measure to reduce speculative side-channel attacks.

