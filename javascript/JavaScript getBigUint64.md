---

title: JavaScript DataView getBigUint64 Method

date: 2025-05-26

---


# JavaScript DataView getBigUint64 Method

JavaScript's DataView provides powerful methods for working with binary data, including the getBigUint64 method for reading 64-bit unsigned integers. This article explores the capabilities of getBigUint64, comparing it to related methods and demonstrating its use across big- and little-endian data formats.


## Overview of DataView and BigUint64

The DataView interface in JavaScript provides methods for working with ArrayBuffer data, offering a low-level approach to interact with binary data. A fundamental aspect of this interface is its ability to read and write different number types, including 64-bit unsigned integers.

Each 64-bit unsigned integer occupies 8 bytes in memory, with the DataView class providing specific methods to interact with this data type. The getBigUint64 method, in particular, retrieves an unsigned 64-bit integer (unsigned long long) from the specified byte offset within a DataView object. This method accepts two parameters: the byteOffset, which indicates the position from which to read the data, and a second parameter (littleEndian) that determines whether the 64-bit integer is stored in little- or big-endian format. The method returns a BigInt value, allowing JavaScript developers to work with numbers that exceed the native double-precision floating point format limit of 2^53 - 1.

Browser Support and Implementation

The getBigUint64 method has comprehensive support across modern browsers including Chrome, Firefox, Safari, and Edge. Additionally, it functions in environments like Node.js, making it a versatile tool for JavaScript developers working with binary data in various contexts.


## Functionality and Parameters

The getBigUint64 method retrieves an 8-byte unsigned integer from the specified byte offset within a DataView object. It accepts two parameters: byteOffset, which indicates the position from which to read the data, and littleEndian, an optional parameter that determines the byte order of the 64-bit integer. When littleEndian is not specified or is false/undefined, the method reads in big-endian format.

The method returns a BigInt value, allowing JavaScript developers to work with numbers that exceed the native double-precision floating point format limit. This functionality relies on JavaScript's support for the BigInt API, which handles numbers beyond the 2^53 - 1 limit of Number.

Implementation details show that browsers implement this method using either the native DataView prototype or fallback logic based on available typed array methods. For example, when the native method is not available, browsers may read two 32-bit unsigned values and combine them into a 64-bit unsigned integer through bitwise operations.

The method performs no alignment constraints, allowing multi-byte values to be fetched from any offset within the ArrayBuffer. To demonstrate basic usage, consider the following example:

```javascript

const { buffer } = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

const dataview = new DataView(buffer);

console.log(dataview.getBigUint64(1)); // 72623859790382856n

```

This example fetches an 8-byte unsigned integer starting at byte offset 1, demonstrating the method's capability to handle both big- and little-endian data formats as indicated by the second parameter's presence or value.


## Browser Support and Implementation

The getBigUint64 method has full support in modern browsers including Chrome, Firefox, Safari, and Edge, as well as in environments like Node.js. This functionality has been available across browsers since September 2021 and is part of the JavaScript typed arrays system.

The method operates by reading eight consecutive bytes from the DataView starting at the specified byte offset. If the littleEndian parameter is not provided or is false, it reads in big-endian format, which is the default behavior. When little-endian data is requested, the method reads the lower 32 bits first and then the upper 32 bits, combining them into a 64-bit unsigned integer.

For environments where the native method is not available, browsers implement this functionality using either the native DataView prototype or fallback logic based on available typed array methods. In cases where two 32-bit unsigned values need to be combined into a 64-bit unsigned integer, bitwise operations are used. This approach is demonstrated in the following example:

```javascript

const left = view.getUint32(0, true);

const right = view.getUint32(4, true);

const combined = left + 2**32*right;

```

This implementation handles both big-endian and little-endian byte orders, ensuring compatibility with a wide range of data formats. The method performs no alignment constraints, allowing for the retrieval of 64-bit values from any offset within the ArrayBuffer. This flexibility makes it particularly useful for working with binary data structures that store numerical values in fixed-width, multi-byte formats.


## Use Case: Reading Uint64 Data


### Reading Uint64 Data

The getBigUint64 method enables precise retrieval of unsigned 64-bit integers from binary data, supporting both big-endian and little-endian formats through its optional second parameter. The method returns a BigInt value, allowing accurate representation of numbers beyond JavaScript's standard 53-bit floating-point precision.

To demonstrate its functionality, consider the following examples:

```javascript

const { buffer } = new Uint8Array([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff]);

const dataview = new DataView(buffer);

console.log(dataview.getBigUint64(0)); // 255n

const buffer2 = new Uint8Array([0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]);

const dataview2 = new DataView(buffer2);

console.log(dataview2.getBigUint64(0, true)); // 255n

```

The first example retrieves a big-endian 64-bit unsigned integer from the specified buffer, while the second demonstrates little-endian data retrieval through the second parameter. These examples highlight the method's capability to handle different byte orders and extract precise numerical values from binary data.


### Implementation Details

The getBigUint64 method's implementation supports both native and polyfill scenarios. When the native DataView prototype includes this method, it is used directly. Otherwise, browsers employ fallback logic that reads two 32-bit unsigned values and combines them into a 64-bit unsigned integer using bitwise operations. This approach ensures compatibility across different JavaScript environments while maintaining efficient data processing.


## Comparison with Related Methods

The getBigUint64 method operates similarly to the getBigInt64 method but focuses on unsigned values. While getBigUint64 returns a BigInt representing an 8-byte unsigned integer, getBigInt64 returns a BigInt representing an 8-byte signed integer.

When the DataView prototype has the getBigUint64 method, it's used directly. Otherwise, browsers implement it by reading two 32-bit unsigned values and combining them into a 64-bit unsigned integer through bitwise operations. This fallback implementation ensures compatibility across different JavaScript environments while maintaining efficient data processing.

The method handles both big-endian and little-endian byte orders. For environments where the native method is not available, the implementation reads two 32-bit unsigned values and combines them using bitwise operations. The following example demonstrates this implementation approach:

```javascript

const left = view.getUint32(0, true);

const right = view.getUint32(4, true);

const combined = left + 2**32 * right;

```

This approach demonstrates how the method handles different byte orders and combines values to produce the final 64-bit unsigned integer.

The getBigInt64 method works similarly but reads eight 8-bit unsigned values and combines them into a 64-bit signed value using bitwise operations. This method includes additional logic to determine if the value is negative based on the most significant bit of the first byte. 

In terms of browser support, the getBigUint64 method has been available across modern browsers and environments since September 2021. The getBigInt64 method works similarly, returning BigInt values in the range of -2^63 to 2^63-1. Both methods are integral parts of the JavaScript typed arrays system and provide comprehensive support for working with 64-bit integers in a variety of byte orders.

