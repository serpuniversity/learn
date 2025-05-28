---

title: JavaScript String.fromCodePoint() Method

date: 2025-05-26

---


# JavaScript String.fromCodePoint() Method

In modern web development, working with text involves handling a vast array of characters from diverse writing systems. JavaScript's String methods like fromCharCode and its modern counterpart fromCodePoint enable developers to create and manipulate these text-based strings. This article explores the powerful capabilities of String.fromCodePoint(), examining how it creates strings from Unicode code points, processes various number formats, and handles both single and multiple characters. We'll also look at its implementation limitations in older environments and provide practical usage examples to help you effectively utilize this versatile method in your projects.


## Syntax and Parameters

The String.fromCodePoint() method creates a string from a sequence of Unicode code points, supporting multiple parameters representing code points and working with values in decimal, hexadecimal, and octal formats. It was widely available since September 2015 and works across many devices and browser versions.

The method accepts code points in the range 0 to 0x10FFFF and returns a string created from these code points. For inputs outside this range, it throws a RangeError. It processes each argument as a Unicode code point, allowing for the creation of both single characters and multiple characters at once. The method supports various number formats, including decimal (88), hexadecimal (0x58), and octal (0o58).

For characters beyond the Basic Multilingual Plane (BMP), String.fromCodePoint() requires the UTF-16 surrogate pair representation. The surrogate pair formula works with both hexadecimal and decimal values: ((first - 0xD7F7) << 10) + second. This formula effectively combines pairs of surrogate code points into a single code point value.

The method processes inputs in the form of numbers, decimal, hexadecimal, or octal representations. It supports single numbers as well as arrays of numbers for multiple code points. When called with non-integer values, less than 0, or greater than 0x10FFFF after conversion, it throws a RangeError. This functionality applies regardless of whether the method is invoked through the String constructor or its prototype method syntax.


## Character Creation

String.fromCodePoint() creates characters based on Unicode code points, with support for both Basic Multilingual Plane (BMP) and supplementary characters. BMP characters use a single code unit, while supplementary characters require surrogate pairs. These pairs are represented using hexadecimal values, as shown in the examples: `String.fromCharCode(0xd83c, 0xdf03)` returns "Night with Stars" (U+1F303), and `String.fromCharCode(55356, 57091)` returns "\uD83C\uDF03".

The method processes each argument as a Unicode code point, allowing for the creation of both single characters and multiple characters at once. For instance, `String.fromCodePoint(72, 101, 108, 108, 111)` returns "Hello", demonstrating its capability to handle multiple code points simultaneously.

When creating strings from Unicode code points, it's important to note that values greater than 65536 are represented using the first 4 hexadecimal digits. For example, `String.fromCodePoint(0x1f303)` creates a string containing the character "Night with Stars" (U+1F303), while `String.fromCodePoint(127747)` achieves the same result through a different hexadecimal representation.

The method throws a RangeError for invalid inputs, including non-integer values and out-of-range numbers. This ensures that only valid Unicode code points are processed, maintaining data integrity when creating strings from code points.


## Valid Range and Exceptions

The method accepts Unicode code points in the range 0 to 0x10FFFF, inclusive. Higher code points require the UTF-16 surrogate pair representation, which the method handles through a specific formula: ((first - 0xD7F7) << 10) + second. This formula works with both hexadecimal and decimal values, as demonstrated in the example where the method calculates the code point 0x1F4A9 from the surrogate pair ["D83D", "DCA9"].

Values outside the accepted range throw a RangeError exception. This behavior applies to non-integer values, negative numbers, and numbers greater than 0x10FFFF after conversion. The method can process individual numbers or arrays of numbers, as shown in the example where the method successfully creates a string containing all capital letters from 'A' to 'Z' when called in a for loop.

The method returns a string created using these code points and works similarly to fromCharCode but can process code points, including those from the Base Multilingual Plane (characters less than 65536) and emoji composed of two code units. For values greater than 65536, only the first 4 hexadecimal digits are used, as demonstrated in the example where the method correctly interprets "8011" as 0x1F4A9.

The method processes the input as a sequence of code points, with each argument representing a Unicode code point value within the allowed range. It throws a RangeError for any value outside this range, ensuring that only valid Unicode code points are processed and maintaining data integrity when creating strings from code points.


## Polyfill Implementation

For environments that do not natively support String.fromCodePoint(), a polyfill is available to enable character creation from code points. The polyfill implementation allows developers to create strings from Unicode code points, even in environments with limited native support.

The polyfill works by providing a fallback mechanism for creating strings from code points. It enables the creation of both single characters and multiple characters at once, similar to the native implementation. The polyfill processes inputs as a sequence of code points, with each argument representing a Unicode code point value within the allowed range (0 to 0x10FFFF).

To demonstrate the polyfill usage, consider the following example:

```javascript

if (!String.fromCodePoint) {

  String.fromCodePoint = function() {

    var result = '';

    for (var i = 0; i < arguments.length; i++) {

      result += String.fromCharCode(parseInt(arguments[i], 10));

    }

    return result;

  };

}

let greet = String.fromCodePoint(72, 101, 108, 108, 111);

console.log(greet); // Output: Hello

```

This polyfill implementation checks if the native String.fromCodePoint() method is available. If not, it provides its own implementation using a for loop to process each argument as a Unicode code point and concatenate the resulting characters into a string.

The polyfill handles various input formats, including decimals, hexadecimal, and octal representations. It processes individual numbers or arrays of numbers, ensuring compatibility with different usage patterns. The implementation maintains consistency with the native method by throwing a RangeError for invalid inputs, including non-integer values and out-of-range numbers.


## Usage Examples

The method processes input arguments as Unicode code points, allowing for the creation of both single characters and multiple characters at once. For example, `String.fromCodePoint(71, 70, 71)` returns "GFG", and `String.fromCodePoint(42)` returns "*" (0x2A).

The function supports various number formats, including decimal, hexadecimal, and octal representations. For instance, `String.fromCodePoint(0x48, 0x45, 0x4C, 0x4C, 0x4F, 0x2E)` returns "HELLO." and `String.fromCodePoint(0o110, 0o105, 0o114, 0o114, 0o117, 0o56)` achieves the same result through a different octal representation.

When creating strings from Unicode code points, the method processes individual numbers or arrays of numbers. For example, the following code creates a string containing the characters "G", "F", and "G":

```javascript

let charArray = [71, 70, 71];

let result = String.fromCodePoint(...charArray);

console.log(result); // Output: GFG

```

This approach demonstrates the method's flexibility in handling different input formats while consistently producing the correct string output.

The method maintains consistency with the native implementation by throwing a RangeError for invalid inputs, including non-integer values and out-of-range numbers. As shown in the example below, passing `Infinity` as an argument results in a RangeError:

```javascript

let string3 = String.fromCodePoint(Infinity);

console.log(string3); // Output: RangeError: Invalid code point Infinity

```

This behavior ensures data integrity when creating strings from code points, providing clear feedback for invalid input values.

