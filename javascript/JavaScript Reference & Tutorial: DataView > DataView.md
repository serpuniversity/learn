---

title: dataview JavaScript API

date: 2025-05-26

---


# dataview JavaScript API

The dataview JavaScript API builds on core JavaScript data handling standards to provide advanced binary data manipulation features. This API consists of two primary interfaces: inline access through dv.pages() syntax and plugin access through app.plugins.plugins.dataview.api. The API enables precise control over binary data through methods for working with ArrayBuffer data, including operations for floating-point numbers, integers, and data buffer management. Understanding these capabilities is crucial for developers working with binary data structures in JavaScript applications.


## Dataview Overview

The dataview JavaScript API consists of two primary interfaces:

Inline Access: This allows dataview functionality within code blocks using dv.pages syntax. When executed, code blocks access the full dataview API through the dv variable. This interface supports a range of functions including dv.table() and dv.pages(). More detailed information on inline API usage is available in the codeblock API reference.

Plugin Access: This method enables dataview functionality through app.plugins.plugins.dataview.api. While similar to the inline API reference, it uses different argument structures due to the absence of implicit file execution. Plugin developers and advanced users will find comprehensive documentation in the Plugin API reference.

The dataview API builds on the JavaScript DataView object, providing access to advanced binary data manipulation features. The API includes methods for working with ArrayBuffer data, specifically:

- setFloat32, setFloat64, getInt32, getUint32 for data writing

- getFloat32, getFloat64, getInt32, getUint32 for data reading

- setBigInt64, setBigUint64, getBigInt64, getBigUint64 for 64-bit integer operations

- Methods like getArrayBuffer, buffer, byteLength, and byteOffset allow managing data views and buffers

The API structure mirrors the DataView object's design, maintaining compatibility with core JavaScript data handling standards while providing specialized dataview functionality. This includes support for big integer operations, floating-point data handling, and direct ArrayBuffer manipulation.


## Inline Access

Inline access to dataview functionality is achieved through the dv.pages() syntax. When executed within a code block, this approach grants full dataview API access through the dv variable. The API includes versatile functions such as dv.table() and dv.pages(). For comprehensive guidance on inline API usage, developers are directed to the codeblock API reference.

The dv variable encompasses the entire codeblock-relevant dataview API, enabling powerful data manipulation capabilities. When working with this interface, it's important to note the distinction between metadata fields - which include author, publication date, and tags - and content, as only metadata fields are indexed for querying purposes. This indexing mechanism allows dataview to efficiently process metadata while maintaining performance.


## Plugin Access

The plugin access interface for dataview functionality is enabled through app.plugins.plugins.dataview.api. This method provides an API structure similar to the codeblock reference API, though it uses different argument structures due to the absence of implicit file execution. Comprehensive documentation for this interface can be found in the Plugin API reference (../code-reference/).

The dataview API builds on the core JavaScript DataView object, providing advanced binary data manipulation features through several key methods:

- Array handling: getArrayBuffer, buffer, byteLength, byteOffset

- Integer operations: setBigInt64, setBigUint64, getBigInt64, getBigUint64

- Floating-point data handling: setFloat32, setFloat64, getInt32, getUint32

- Data writing: setFloat32, setFloat64, getInt32, getUint32

- Data reading: getFloat32, getFloat64, getInt32, getUint32

This structure maintains compatibility with core JavaScript data handling standards while offering specialized dataview functionality. The dataview API enables developers to work with ArrayBuffer data efficiently, including support for big integer operations and floating-point data handling.


## DataView Methods

The DataView object in JavaScript offers a comprehensive set of methods for reading and writing binary data, including:

**Float32 Handling:**

The setFloat32 method stores 32-bit floating-point numbers in an ArrayBuffer, while getFloat32 reads them. Both methods support little-endian and big-endian byte order, with the latter being the default. For example:

```javascript

const buffer = new ArrayBuffer(4);

const view = new DataView(buffer);

view.setFloat32(0, 123.456);

console.log(view.getFloat32(0)); // 123.456

```

**Integer Operations:**

DataView supports multiple integer formats, including 8-bit, 16-bit, and 32-bit signed and unsigned integers. For instance, to set and retrieve a 32-bit unsigned integer:

```javascript

view.setUint32(0, 4294967295);

console.log(view.getUint32(0)); // 4294967295

```

**Buffer Management:**

The DataView constructor allows creating views with specific byte offsets and lengths within an ArrayBuffer. This is crucial for managing complex data structures. Example usage:

```javascript

const buffer = new ArrayBuffer(16);

const view = new DataView(buffer, 0, 8);

view.setInt32(0, 12345678);

view.setInt32(4, 87654321);

```

These methods enable precise control over binary data manipulation, supporting both common and less common data formats used in web applications and systems integration.


## DataView Constructor

The DataView constructor creates DataView objects, taking three parameters: buffer, byteOffset, and byteLength. The buffer must be an existing ArrayBuffer or SharedArrayBuffer, with the byteOffset specifying the starting position within the buffer (defaulting to the beginning if omitted). The byteLength parameter determines the number of elements in the byte array, defaulting to the buffer's length if unspecified.

Key aspects of the constructor:

- Validating parameters: The constructor throws a RangeError if byteOffset plus byteLength exceeds the buffer's byte length.

- Buffer manipulation: The DataView constructor enables precise access to ArrayBuffer data, supporting various integer formats (8-bit, 16-bit, 32-bit signed and unsigned integers) and floating-point numbers.

- Endianness support: Both little-endian and big-endian formats are supported through the littleEndian parameter in methods like setFloat32 and getUint16, with big-endian being the default.

Example usage demonstrates the constructor's flexibility and power:

```javascript

const buffer = new ArrayBuffer(16);

const view = new DataView(buffer, 0);

view.setInt16(1, 42);

console.log(view.getInt16(1)); // 42

```

