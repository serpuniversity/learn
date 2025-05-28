---

title: Uint8Array.setFromHex() Method

date: 2025-05-27

---


# Uint8Array.setFromHex() Method

JavaScript's TypedArray objects provide powerful tools for working with binary data, but converting between different representations can be challenging. This article explores the Uint8Array.setFromHex() method, which creates a new Uint8Array from a hexadecimal string while returning detailed information about the conversion process. Through rigorous input validation and efficient data processing, this method offers a robust solution for working with binary data in JavaScript.


## Method Overview

The Uint8Array.setFromHex() method creates a new Uint8Array instance from a hexadecimal string, writing the specified number of bytes to the Uint8Array and returning an object indicating how many bytes were read and written.


### Method Implementation

The method processes input data by:

1. Creating a new Uint8Array instance with the same length as the input string

2. Setting each element of the new array to the corresponding character's ASCII value

3. Returning the new Uint8Array instance


### Input Validation

The method validates the input string:

- Requires an even number of characters (two characters encode one byte)

- Only allows characters in the hexadecimal alphabet (0-9 and A-F, case-insensitive)

- Disallows whitespace (unlike the base64 implementation)


### Error Handling

The method throws exceptions for invalid input:

- SyntaxError: If the string contains characters outside the hex alphabet or has an odd length

- TypeError: If the input is not a string


### Data Processing

The method writes data to the Uint8Array:

- Always starts at the beginning of the array

- Ignores excess characters, even if they are valid

- Allows writing to specific offsets using TypedArray.prototype.subarray()


### Return Value

The method returns an object containing:

- read: The number of hex characters read from the input string (length if decoded data fits, otherwise number of complete hex characters)

- written: The number of bytes written to the Uint8Array (never exceeds the array's byteLength)


## Method Usage

The Uint8Array.setFromHex() method provides a straightforward way to convert a hexadecimal string into a Uint8Array instance. The method takes a single string argument representing the hexadecimal data and returns an object containing details about the conversion process (Figure 1).


### Method Implementation

The method creates a new Uint8Array instance with the same length as the input string, sets each element to the corresponding character's ASCII value, and returns the new Uint8Array instance.


### Example Usage

The example demonstrates converting a hexadecimal string to a Uint8Array (Figure 2):

```javascript

const uint8Array = new Uint8Array(4);

const result = uint8Array.setFromHex("cafed00d-some random stuff");

console.log(result); // { read: 8, written: 4 }

console.log(uint8Array); // Uint8Array(4) [202, 254, 208, 13]

const uint8Array = new Uint8Array(8);

const result = uint8Array.subarray(2).setFromHex("cafed00d");

console.log(result); // { read: 8, written: 4 }

console.log(uint8Array); // Uint8Array(8) [0, 0, 202, 254, 208, 13, 0, 0]

```


### Validation and Error Handling

The method requires an even number of characters in the input string, as two characters encode one byte. It only allows characters in the hexadecimal alphabet (0-9 and A-F, case-insensitive) and disallows whitespace (unlike the base64 implementation). Any invalid characters or an odd-length string will result in a SyntaxError exception (Figure 3).


### Data Processing

The method always starts writing at the beginning of the Uint8Array and ignores excess characters, even if they are valid (Figure 4). It allows writing to specific offsets using TypedArray.prototype.subarray() (Figure 2).


### Return Value

The method returns an object containing the number of hex characters read from the input string (Figure 1) and the number of bytes written to the Uint8Array (never exceeding the array's byteLength).


#### Figure 1: Method Return Value

```javascript

{

  read: 8, // Number of hex characters read from the input string

  written: 4 // Number of bytes written to the Uint8Array

}

```


#### Figure 2: Example Usage

```javascript

const uint8Array = new Uint8Array(4);

const result = uint8Array.setFromHex("cafed00d-some random stuff");

console.log(result); // { read: 8, written: 4 }

console.log(uint8Array); // Uint8Array(4) [202, 254, 208, 13]

const uint8Array = new Uint8Array(8);

const result = uint8Array.subarray(2).setFromHex("cafed00d");

console.log(result); // { read: 8, written: 4 }

console.log(uint8Array); // Uint8Array(8) [0, 0, 202, 254, 208, 13, 0, 0]

```


#### Figure 3: Error Handling

```javascript

new Uint8Array().setFromHex("deadbeefxyz") // Throws SyntaxError

new Uint8Array().setFromHex("oddlength") // Throws SyntaxError

```


#### Figure 4: Writing to Specific Offsets

```javascript

const uint8Array = new Uint8Array(8);

const result = uint8Array.subarray(2).setFromHex("cafed00d");

console.log(result); // { read: 8, written: 4 }

console.log(uint8Array); // Uint8Array(8) [0, 0, 202, 254, 208, 13, 0, 0]

```


## Validation and Error Handling

The method validates the input string according to the following rules:

- Requires an even number of characters (two characters encode one byte)

- Only allows characters in the hexadecimal alphabet (0-9 and A-F, case-insensitive)

- Disallows whitespace (unlike the base64 implementation)

Any invalid characters or an odd-length string will result in a SyntaxError exception. The method throws a TypeError if the input is not a string or if the options object is not an object or undefined, as well as when the options properties are not of the expected values or undefined.

The validation process involves checking each character in the input string:

1. The method starts at the beginning of the string and checks each character's code unit.

2. If a character is not a TAB (0x0009), LF (0x000A), FF (0x000C), CR (0x000D), or SPACE (0x0020), it returns the current index.

3. If all characters pass validation, it continues to the next step.

To handle the input data, the method performs these steps:

1. Creates a new Uint8Array instance with the same length as the input string

2. Sets each element of the new array to the corresponding character's ASCII value

3. Returns the new Uint8Array instance

The method throws exceptions for the following conditions:

- SyntaxError: If the string contains characters outside the hex alphabet or has an odd length

- TypeError: If the input is not a string, the options object is not an object or undefined, or the options properties are not of the expected values or undefined


## Data Processing

The Uint8Array.setFromHex() method processes input data through several key steps:

1. Input Validation: The method begins by validating the input string using a regular expression that matches valid ASCII characters for hexadecimal input. Specifically, it allows characters in the range 0x0009 to 0x0020 (excluding newline characters) and any ASCII letter or digit.

2. Data Conversion: For each valid character in the input string, the method converts it to its corresponding ASCII value, creating a new Uint8Array instance of the same length as the input string.

3. Error Handling: The method throws exceptions for invalid input conditions. These include:

   - SyntaxError: If the string contains characters outside the hexadecimal alphabet or has an odd length.

   - TypeError: If the input is not a string, the options object is not an object or undefined, or the options properties are not of the expected values or undefined.

4. Character Processing: The method processes characters in chunks of two, converting each pair to a byte value using parseInt with base 16. It handles odd-length strings by ignoring excess characters and ensures that only valid hexadecimal characters are processed.

5. Array Construction: The final step constructs a Uint8Array instance from the processed byte values, returning this array along with metadata about the conversion process.

This processing approach aligns with similar methods for base64 conversion, where input validation and character processing play crucial roles in ensuring data integrity. The method's strict handling of input length and character validation helps prevent common errors in hexadecimal data processing.


## Polyfills and Browser Support

The Uint8Array.setFromHex() method offers similar functionality to other conversion methods in the JavaScript standard library, including Uint8Array.fromBase64 and its related functions. Like these methods, setFromHex returns an object containing the updated Uint8Array instance and metadata about the conversion process, including the number of bytes read and written.

The method's behavior is consistent across standard operations, handling three primary scenarios:

1. Converting base64 strings into existing Uint8Array objects

2. Writing only the amount of data that fits within the array capacity

3. Writing to specific offsets using TypedArray.prototype.subarray()

For optimal performance, the method employs direct memory manipulation techniques, avoiding unnecessary data copying. When working with existing Uint8Array instances, it efficiently updates the target array while maintaining minimal memory overhead.

The method's design aligns with best practices established in the TC39 proposal for Uint8Array <-> base64/hex conversion, incorporating lessons learned from previous implementations of similar functionality. This includes careful handling of edge cases, such as ensuring proper array bounds checks and maintaining consistent error reporting across different use cases.

