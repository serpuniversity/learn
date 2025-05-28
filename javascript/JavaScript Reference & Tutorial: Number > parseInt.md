---

title: JavaScript parseInt() Method

date: 2025-05-26

---


# JavaScript parseInt() Method

Working with numbers in JavaScript often requires converting string representations into numerical values. The `parseInt()` method provides a way to do this, but its behavior can vary significantly based on how you use it. Understanding its basic functionality, how to use the radix parameter correctly, and the nuances of string handling is essential for reliable number parsing in JavaScript applications.


## Basic Functionality

The parseInt() function in JavaScript converts string representations of numbers into integers. It requires two parameters: the string to parse and an optional radix parameter specifying the numeral system base (between 2 and 36).

When invoked with a single argument, parseInt() parses the string and returns an integer using a default radix of 10. However, automatic radix interpretation can lead to unexpected results: strings beginning with "0x" or "0X" are interpreted as hexadecimal (base 16), while those starting with a "0" are parsed as octal (base 8) in some environments.

Omitting the radix parameter can result in inconsistent behavior across JavaScript engines. For consistent parsing, always specify the radix. Common errors include attempting to parse non-numeric characters (e.g., "123x") or specifying a radix outside the valid range (0-36), which will both return NaN.

The function processes strings by removing leading and trailing whitespace, then parsing characters until a non-numeric value is encountered. It returns the integer formed by the preceding numerals or NaN if no valid integer is found. For example, parseInt("123abc", 10) correctly returns 123, while parseInt("abc123", 10) returns NaN.


## Parsing with Radix

The radix parameter determines the numeral system for parsing, with a valid range of 2 to 36. The function automatically infers the radix for strings beginning with "0x" or "0X", treating them as hexadecimal (base 16), while strings starting with "0" are parsed as octal (base 8) in some environments.

JavaScript engines behave differently when the input string starts with "0" but assumes octal only if the radix is explicitly set to 8. For other radix values outside the range of 2-36, the function returns NaN. The integer conversion occurs as follows: the string is first converted to a number using the `ToString` method, then parsed according to the specified radix.

The function processes strings by removing leading and trailing spaces, parsing from left to right until an invalid numeral is encountered for the specified radix. It returns the integer formed by the preceding numerals or NaN if no valid integer is found. Edge cases include strings containing characters invalid in the specified radix (e.g., "17" in base 8 returns NaN), negative inputs (which are interpreted as -15 for hexadecimal inputs like "F"), and scientific notation (which is accepted and parsed correctly, as in "15e2" returning 1500).

For very large numbers, JavaScript uses scientific notation in string representation, which can lead to unexpected truncation behavior (for example, "1000000000000000" returns 1.0E15). Always specifying the radix parameter ensures consistent parsing across different environments and prevents unintended base interpretation.


## String Handling

The function begins by ignoring any leading or trailing whitespace in the input string. It then attempts to extract an integer value from the string using the following rules:

- If the string begins with "0x" or "0X", the function assumes a hexadecimal (base 16) interpretation, disregarding any subsequent characters that do not conform to this base.

- For other cases where the string starts with a "0" character, the function requires the explicit specification of a radix value of 8 to interpret the number as octal. In environments where no radix is specified, strings starting with "0" are typically parsed as octal, though this behavior can vary between JavaScript engines.

- In all other cases, the function assumes a default radix of 10 (decimal) interpretation for the number. This means that strings representing numbers in bases other than 2-36 will be returned as NaN if the radix is not explicitly specified.

The function processes the string from left to right, removing any leading sign characters (`+` or `-`) before beginning the numeric conversion. It stops parsing upon encountering the first non-numeric character that does not conform to the specified radix or any invalid numeral sequence. For example, the input "17" with a radix of 8 would produce NaN because 7 is not a valid digit in base 8. Similarly, attempting to parse "FXX123" with a radix of 16 would also result in NaN, as "XX" represents invalid hexadecimal characters.

The function correctly handles leading zeros as octal representation when the radix is explicitly set to 8, returning values such as "015" correctly as 15. For scientific notation inputs like "15e2", the function returns 1500 in base 10, demonstrating its ability to process these formats while maintaining proper numeric interpretation. However, it's important to note that integers outside the safe range may lose precision, potentially requiring the use of `BigInt()` for arbitrary-length integer parsing in cases where precise large number handling is necessary.


## Use Cases

The `parseInt()` function proves invaluable when extracting numbers from text data or handling inputs that should be integers for mathematical operations. Its basic operation is to convert a string representing a positive integer into an integer, as shown in the example where "123" becomes 123.

A powerful feature is its ability to handle strings with numbers leading characters, extracting valid integer portions and discarding non-numeric characters afterwards. For instance, "456xyz" produces 456 when parsed. Leading, embedded, or trailing spaces are also gracefully ignored according to the language specification.

When working with different numeral systems, specifying the radix parameter is crucial for correct interpretation. For standard decimal conversion, the method behaves identically to its global counterpart - the global `parseInt()` function. However, developers are advised to use `Number.parseInt()` for consistency with other Number methods and clearer code style guidelines.

The method effectively handles various edge cases. It correctly processes strings with negative numbers, scientific notation, and large numbers - though it does truncate scientific notation to the nearest valid integer, as demonstrated by "1000000000000000" returning 1.0E15.

Leading zeros are interpreted as octal representation when the radix is explicitly set to 8, such as "015" being correctly converted to 15. However, the method returns NaN for inputs containing characters invalid in the specified radix, like "17" in base 8 or "FXX123" in base 16. Always checking the result with `Number.isNaN` is recommended to handle invalid inputs effectively.


## Best Practices

Always specify the radix parameter to ensure consistent number interpretation across different JavaScript environments. By default, `parseInt()` infers the radix based on the string's content: it assumes hexadecimal for "0x" or "0X" prefixes, octal for leading zeros, and decimal for all other cases. However, relying on automatic radix detection can lead to unexpected results, especially when dealing with octal representations.

To avoid parsing errors, explicitly set the radix parameter to 10 for decimal numbers and use specific values for other numeral systems (2-36). For example, to parse a binary number, use `parseInt(binaryString, 2)`, and for hexadecimal, use `parseInt(hexString, 16)`. Always validate the result using `Number.isNaN()` to handle inputs that cannot be converted to integers, as shown in the snippet provided: `var i = parseInt("25x"); // i is not a number`.

When working with scientific notation, understand that `parseInt()` will truncate the value to the nearest integer. For parsing very large numbers or maintaining precise integer arithmetic, consider using the `BigInt` constructor when dealing with values that exceed JavaScript's safe integer range.

