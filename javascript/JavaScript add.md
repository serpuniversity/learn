---

title: Atomics.add() in JavaScript

date: 2025-05-26

---


# Atomics.add() in JavaScript

JavaScript's Atomics object introduces atomic operations for shared memory manipulation, enabling high-performance concurrent programming. These operations provide a well-defined execution order across parallel CPU threads, crucial for developing robust multi-agent programs. This article focuses on the add() method, which performs atomic addition on shared memory arrays. We'll explore its implementation details, usage examples, and performance considerations, demonstrating how to leverage this powerful concurrency primitive while managing associated challenges.


## Atomics Object Overview

The Atomics object in JavaScript introduces a new memory model that enables multi-agent programs to communicate using atomic operations. These operations ensure a well-defined execution order even on parallel CPUs, making them essential for developing high-performance, concurrent programs. The object provides static methods that operate directly on SharedArrayBuffer objects, facilitating direct access to shared memory from multiple threads simultaneously.

The Atomics interface includes several fundamental operations:

- Atomic addition (add)

- Subtraction (sub)

- Bitwise operations (and, or, xor)

- Value loading and storing

- Compare-and-swap operations

- Synchronization primitives (wait, notify)

Each operation is designed to perform its task as an indivisible unit, preventing other threads from observing intermediate states. This atomicity is crucial for maintaining memory consistency across multiple threads and preventing common concurrency issues such as data corruption and deadlocks.

Developers can use Atomics to implement complex concurrent data structures and algorithms. For example, the add() method atomically increments a value in a shared memory array, making it suitable for scenarios where multiple threads need to increment a counter or perform cumulative operations. The method's atomic nature ensures that the increment operation completes fully before any other thread can read or modify the value, preventing race conditions and ensuring data integrity.


## add() Method Details

The Atomics.add() method performs an atomic addition operation on a given value at a specified position in an array, returning the original value at that position before the modification. This operation ensures that no other write operation can occur until the modified value is written back, maintaining memory consistency across multiple threads.

The method's syntax is Atomics.add(typedArray, index, value), where:

- typedArray must be one of the following integer types: Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, BigInt64Array, or BigUint64Array

- index represents the position in the typedArray where the value will be added

- value is the number to add to the position

The method returns the old value at the given position (typedArray[index]). It throws TypeError exceptions if the typedArray is not one of the allowed integer types or if the typedArray is not a shared typed array type. It throws RangeError exceptions if the index is out of bounds in the typedArray.

For example, the following code demonstrates the correct usage of the Atomics.add() method:

```javascript

const sab = new SharedArrayBuffer(1024);

const ta = new Uint8Array(sab);

console.log(Atomics.add(ta, 0, 12)); // Returns 0, the old value

console.log(Atomics.load(ta, 0)); // 12

```

The method's atomic nature ensures that the addition operation completes fully before any other thread can read or modify the value, preventing race conditions and maintaining data integrity. This characteristic makes it particularly useful for implementing concurrent data structures and algorithms that require precise memory management.


## Usage Examples

The add() method performs atomic addition on shared integer typed arrays, returning the original value before the modification. This operation ensures that no other write occurs until the modified value is written back, maintaining memory consistency across threads.

To demonstrate its usage, let's examine two examples:

Example 1:

```javascript

let buf = new SharedArrayBuffer(25);

let arr = new Uint8Array(buf);

arr[0] = 9;

console.log(Atomics.add(arr, 0, 3)); // Returns 9

console.log(Atomics.load(arr, 0));   // 12

```

In this example, we first set the value at index 0 to 9. The add() method then adds 3 to this position, returning the original value of 9 before the modification. When we subsequently load the value at index 0, we see that it has been correctly updated to 12.

Example 2:

```javascript

let buf = new SharedArrayBuffer(25);

let arr = new Uint8Array(buf);

arr[0] = 3;

console.log(Atomics.add(arr, 0, 2)); // Returns 3

console.log(Atomics.load(arr, 0));   // 5

```

Here, we initialize the array at index 0 with the value 3. Adding 2 to this position via Atomics.add() returns the original value of 3, and the subsequent load operation confirms that the array value has been correctly incremented to 5.

These examples demonstrate the method's consistent behavior across different initial values and addition amounts, while highlighting its atomic nature through the consistent return and final values.


## Error Handling

The Atomics.add() method throws two types of exceptions when encountering invalid inputs: TypeError and RangeError. These exceptions help developers catch and handle errors during runtime, ensuring that their applications can respond appropriately to incorrect usage patterns.

TypeErrors occur when the typedArray parameter is not one of the allowed integer types (Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, BigInt64Array, BigUint64Array) or when typedArray is not a shared typed array type. This means that any attempt to pass a non-integer typed array will result in a TypeError.

RangeErrors are thrown when the index parameter is out of bounds in the typedArray. This occurs when the index value falls outside the valid range of indices for the array, indicating that the specified position does not exist within the array's bounds.

Here's an example of error handling in JavaScript:

```javascript

try {

  const sab = new SharedArrayBuffer(25);

  const arr = new Float32Array(sab); // Invalid type, should be integer typed array

  console.log(Atomics.add(arr, 0, 3));

} catch (e) {

  if (e instanceof TypeError) {

    console.error("TypeError: Invalid typedArray type");

  }

}

try {

  const sab = new SharedArrayBuffer(25);

  const arr = new Uint8Array(sab);

  console.log(Atomics.add(arr, 25, 3)); // Out of bounds index

} catch (e) {

  if (e instanceof RangeError) {

    console.error("RangeError: Index out of bounds");

  }

}

```

These error-handling examples demonstrate how to catch and identify the specific type of exception thrown by the Atomics.add() method. The first try-catch block handles a TypeError, while the second handles a RangeError, allowing developers to write robust concurrent applications that can gracefully handle invalid input scenarios.


## Performance Considerations

The atomic nature of Atomics operations prevents race conditions and maintains memory consistency across multiple threads, but these operations also introduce performance considerations that developers must understand. Each atomic operation acts as a blocking method, meaning the current thread waits until the operation completes before proceeding. While this ensures data integrity, it can lead to idle CPU cycles if not managed carefully, particularly in scenarios with high thread contention.

Memory ordering enforced by Atomics operations introduces overhead compared to non-atomic alternatives, making careful design crucial for performance-critical applications. Modern multi-core processors require this level of synchronization to prevent data corruption, but developers should weigh the benefits against potential performance impacts. To optimize performance, best practices include minimizing shared data, designing lock-free algorithms where possible, and batching multiple operations into single atomic steps to reduce synchronization overhead.

The module's capabilities extend beyond basic arithmetic operations, providing synchronization primitives that enable developers to coordinate thread actions effectively. However, this power comes with responsibilities, particularly in security. Developers must implement proper synchronization strategies to prevent shared data corruption and ensure thread safety. The Atomics object stands as a powerful tool for managing concurrent JavaScript applications, especially those leveraging modern multi-core processors and shared memory architectures.

