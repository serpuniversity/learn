---

title: JavaScript Typed Arrays: Converting Between Hex and Binary Data

date: 2025-05-27

---


# JavaScript Typed Arrays: Converting Between Hex and Binary Data

In the world of modern web development, efficient manipulation of binary data is crucial for handling everything from cryptographic keys to network protocols. JavaScript's Typed Array family provides powerful tools for working with binary data, but mastering these tools requires a deep understanding of the underlying mechanisms. One particularly important type is Uint8Array, which represents 8-bit unsigned integers and forms the foundation for many binary data operations.

This article delves into the rich ecosystem of methods for converting between hex and binary data within Typed Arrays. We'll explore the specialized Uint8Array.fromHex() method, compare it to the more general fromBase64(), and examine how these conversions work under the hood. You'll learn about the strict validation required for hex strings, the efficient implementations of standard conversion methods, and the practical considerations for working with binary data in JavaScript. Along the way, we'll uncover some unexpected insights into browser implementation details and the performance implications of different approaches.


## Introduction to Typed Arrays

JavaScript's Uint8Array type represents 8-bit unsigned integers, providing an efficient way to store and manipulate binary data. Each element in a Uint8Array is a single byte, allowing for direct manipulation of raw binary data. As part of the typed array family, Uint8Array inherits properties and methods from its parent TypedArray class, including support for base64 and hex conversions.

The TypedArray specification defines two static methods for creating Uint8Array instances from hexadecimal strings: Uint8Array.fromHex() and Uint8Array.fromBase64(). While both methods return a new Uint8Array object, fromHex() specifically parses a hexadecimal string, while fromBase64() decodes a base64-encoded string. Both methods employ strict validation: fromHex() requires an even number of characters and only hexadecimal alphabet characters, while fromBase64() follows the standard 4/3 character ratio for base64 encoding.

Common operations for converting between binary data representations include base64 encoding and decoding. These methods offer flexible integration with TextEncoder and TextDecoder for string and binary encoding, particularly for UTF-8 data. The simdutf library provides the base64 decoding functionality, with current support limited to Latin1 strings but potential future expansion to UTF16.


## Creating Uint8Array from Hexadecimal Strings

Uint8Array.fromHex() creates a new Uint8Array object from a hexadecimal string. This method specifically parses the string into a byte array, making it distinct from other base64 or hex conversion methods. To use this method, you provide a single parameter: the hexadecimal string to convert.

Key aspects of the method include:

- The input string must have an even number of characters, as two characters encode one byte

- It only accepts characters in the hexadecimal alphabet (0-9, A-F), which are case-insensitive

- The method ignores any whitespace in the input string

- No input validation is performed beyond the basic requirements

For example, consider the following code:

```javascript

const hexString = "CAfed00d"

const bytes = Uint8Array.fromHex(hexString)

console.log(bytes) // Uint8Array [ 202, 254, 208, 13 ]

```

The method returns a new Uint8Array containing the parsed bytes. Common errors include SyntaxError for invalid characters or odd-length strings, and TypeError for non-string inputs. Understanding these constraints is crucial for correct usage in applications that require robust binary data handling.


## Converting Uint8Array to Hexadecimal Strings

The Uint8Array.prototype.toHex() method returns a hex-encoded string representing the data in the Uint8Array. This method creates strings from a byte array, providing a direct conversion mechanism for binary data representation.

The method has no parameters and returns a hex-encoded string representing the data in the Uint8Array. The implementation follows a straightforward approach, though specific details of the internal mechanism are not provided in the official documentation. Instead, alternative implementations can offer insights into the process:

A common approach uses a byte-to-hex conversion array to efficiently construct the hexadecimal string:

```javascript

let byteToHex = new Uint8Array(256);

for (let n = 0; n < 0xa; ++n) byteToHex[n] = '0' + n;

for (let n = 0xa; n < 0x10; ++n) byteToHex[n] = '0' + String.fromCharCode(n + 87);

for (let n = 0x10; n < 0x100; ++n) byteToHex[n] = n.toString(16);

function byteArrayToHex(byteArray) {

  const l = byteArray.length;

  let hex = '';

  for (let i = 0; i < l; ++i) hex += byteToHex[byteArray[i]];

  return hex;

}

const arr = new Uint8Array([4, 8, 12, 16]);

console.log(byteArrayToHex(arr)); // 04080c10

```

This method demonstrates the core functionality, though the official implementation may use more optimized techniques given the specific requirements of browser and engine implementations.

Error handling is minimal in the official specification, with no mention of specific validation beyond the general constraints of valid Uint8Array data. The implementation is designed for small data sizes (hundreds of bytes) where asynchronous operations would be inefficient, making it suitable for common use cases such as SSH key encoding.


## Binary Data Conversion Methods

The TypedArray specification introduces several methods for converting between binary data representations, including base64 encoding and decoding. The primary methods provide efficient conversion mechanisms while maintaining compatibility with existing browser implementations.

Base64 Conversion

The fromBase64() method creates a new Uint8Array from a base64-encoded string, preferred over Window.atob() due to its direct byte-array output. The method accepts an optional options object to customize behavior, including handling of the last base64 chunk through "loose", "strict", or "stop-before-partial" modes. The implementation uses the simdutf library, currently limited to Latin1 strings but potentially expandable to UTF16.

Hexadecimal Conversion

Additional methods enable direct byte-array conversion through hex representation. Two core conversion methods exist:

- fromHex(string): Converts a hexadecimal string to a Uint8Array

- toHex(): Converts a Uint8Array to a hexadecimal string representation

These methods function similarly to TextEncoder's encodeInto functionality with support for partial array views. Both synchronous and efficient in nature, the implementation is most suitable for small data sizes (hundreds of bytes) where asynchronous operations would be unnecessary.

The conversion functions draw from multiple implementation sources, including the Libauth library and direct Uint8Array operations. The uint8_to_hex and hex_to_uint8 methods demonstrate detailed conversion logic, with the former computing hexadecimal representations for each byte and the latter converting back to a Uint8Array through array indexing and value accumulation.


## Implementation and Browser Support

The Uint8Array type has reached stage 3 in the TC39 process, meaning implementations are underway and the feature is ready for practical use. The primary conversion methods - fromHex, toHex, fromBase64, and toBase64 - function through the simdutf library for base64 decoding, currently supporting Latin1 strings with potential future expansion to UTF16.

Browser and JavaScript environment implementations show consistency in core functionality. For instance, Node.js v4.5 demonstrates typical usage patterns with the Uint8Array constructor accepting a single argument representing array length. Polyfills and library implementations, such as the uint8_to_hex and hex_to_uint8 functions, provide detailed conversion logic while maintaining compatibility with existing typed array operations.

Performance benchmarks highlight the Uint8Array's efficiency for small data sizes, outperforming alternative methods in many cases. While the base64 and hex conversion methods do not use TextEncoder/TextDecoder APIs (as base64 is not a text encoding format), they demonstrate robust handling of various input scenarios, including whitespace and partial array views.

The specification allows for flexible implementation across different environments, supporting both streaming and asynchronous operations where appropriate. Current browser compatibility shows consistent support for the core conversion methods, though detailed documentation on specific engine implementations remains sparse. As the feature matures, ongoing development continues to balance performance, compatibility, and future expansion potential.

