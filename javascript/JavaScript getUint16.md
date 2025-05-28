---

title: DataView getUint16 Method

date: 2025-05-26

---


# DataView getUint16 Method

The getUint16 method in DataView allows developers to read 16-bit unsigned integers from a specified position within a binary data buffer. This introduction will explore the method's syntax, parameters, and behavior, including its handling of byte offsets and endianness. You'll learn how to use getUint16 to retrieve values from different positions in a binary buffer and understand its compatibility across various modern browsers and platforms.


## Method Syntax and Parameters

The getUint16 method retrieves a 16-bit unsigned integer from a specified position within a DataView object. It requires one required parameter: byteOffset, which determines the starting position in the DataView buffer, with a minimum increment of 2 bytes for 16-bit values.

The method supports an optional second parameter, littleEndian, which specifies the byte order of the 16-bit integer. If omitted or set to false, the method defaults to big-endian format, retrieving values with the most significant byte first. The method throws a RangeError if the byteOffset would cause reading beyond the view's end.

The method operates without alignment constraints, allowing multi-byte values to be fetched from any offset within the view's bounds. For example, it can retrieve a 16-bit value starting at byte position 2 in a DataView object, even though the previous 16-bit value ended at byte position 0.

The method has been implemented in various browsers since July 2015 and works with various devices and browser versions. It is part of the Typed Array specification, which was superseded by ECMAScript 2015, with the current specification found in the ECMAScript 2015 (6th Edition, ECMA-262) Language Specification.


## Byte Offset Requirements

The byteOffset parameter determines the starting position in the DataView buffer, with a minimum increment of 2 bytes for 16-bit values. A RangeError is thrown if the byteOffset would cause reading beyond the view's end. Multi-byte values can be retrieved from any offset within the view's bounds.

The buffer's byte offset is fixed at construction time and represents the starting position in the ArrayBuffer for the new view. The byteLength property represents the length of the view in bytes, also fixed at construction. All DataView instances inherit from DataView.prototype, which provides properties for the ArrayBuffer reference and the view's byte length.

The getUint16 method operates without alignment constraints, allowing 16-bit values to be fetched from any valid offset. The method supports both little-endian and big-endian formats, with the big-endian format being the default (used when the littleEndian parameter is false or omitted). The method returns a 16-bit unsigned integer between 0 and 65535.

Examples demonstrate proper usage, including setting and retrieving values. For instance, setting the value at byte position 1 to 65535 using view.setUint16(1, 65535) and subsequently retrieving it with view.getUint16(1) returns the expected value of 65535. Similarly, setting values at byte positions 2 and 4 works as expected, showing the method's flexibility with different offsets.


## Little-Endian vs. Big-Endian

The little-endian vs. big-endian parameter determines how the 16-bit value is interpreted. By default, if the littleEndian parameter is false or omitted, the method reads the most significant byte first (big-endian format). This is the primary difference between the two endianness options:

- Big-endian (default): Reads most significant byte first

- Little-endian: Reads least significant byte first (default if littleEndian is true)

For example, given the byte sequence [0x01, 0x02], the method returns 258 when using the default big-endian format (0x0201), but returns 513 when using little-endian format (0x0102).

The Document Object Model (DOM) Level 2 specifies that the byte offset is in bytes, and the method has no alignment constraints. This means multi-byte values can be fetched from any offset within the view's bounds, not just aligned positions.

Most use cases require little-endian format (true). The system endianness affects only ArrayBuffer creation, not reading operations. When reading from a Uint16Array's .buffer using a DataView, the system endianness is used. However, for reading from a binary file, the endianness must be determined from the file format specification (as noted in the DataView documentation).

The method's existence allows explicit control over endianness, which is particularly important for WebAssembly memory, which is always little-endian. This control enables developers to work consistently across different platforms, where the default behavior is often little-endian but not always.


## Example Usage

A code snippet demonstrates retrieving the first Uint16 value from an ArrayBuffer using DataView. The example creates a Uint16Array with values [7, 12, 100] and then creates a DataView object using the array's buffer. The getUint16 method is called on the DataView object with two arguments: the index of the element to access and the byte offset within the buffer. The console.log statement outputs the results of calling getUint16 on the first two elements of the array.

The method is also illustrated in an XMLHttpRequest example, where an ArrayBuffer is retrieved from a binary file. The getUint16 method reads the first two bytes of the ArrayBuffer and returns the corresponding Uint16 value, demonstrating its use with raw binary data.

The method's behavior is further explained through various examples and specifications. For instance, a Uint8Array with values [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] creates a DataView, and getUint16(1) returns 258, illustrating the method's ability to handle different byte offsets and retrieve correct values based on the specified parameters.


## Browser Compatibility

The getUint16 method has been implemented in various browsers since July 2015 and works across multiple devices and browser versions. It operates on ArrayBuffer views, with each uint16 number occupying two bytes and the byte offset for the next number incrementing by 2 (unless otherwise specified through the byteOffset parameter).

The method returns an unsigned 16-bit integer value between 0 and 65535. When reading from a typed array's .buffer using a DataView, the system endianness is used unless explicitly specified through the littleEndian parameter. For WebAssembly memory, which is always little-endian, developers can use this parameter to maintain consistent endianness across different platforms.

The implemented browsers include:

- Chrome 9 and above

- Edge 12 and above

- Firefox 15 and above

- Internet Explorer 10 and above

- Opera 12.1 and above

- Safari 5.1 and above

- Android webview 4 and above

- Chrome for Android (version not specified)

- Edge Mobile (version not specified)

- Firefox for Android 15 and above

- Opera for Android 12 and above

- iOS Safari 4.2 and above

- Samsung Internet (version not specified)

The method is part of the Typed Array specification, which was superseded by ECMAScript 2015. Its current implementation follows the ECMAScript 2015 (6th Edition, ECMA-262) Language Specification with the latest draft version. The method provides two parameters: byteOffset, which specifies the location in the buffer, and littleEndian, which determines the byte order of the 16-bit integer (defaulting to big-endian if not specified).

