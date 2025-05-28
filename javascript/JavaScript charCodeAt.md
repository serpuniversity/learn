---

title: JavaScript charCodeAt() Method

date: 2025-05-26

---


# JavaScript charCodeAt() Method

Developed specifically for working with character data, JavaScript's charCodeAt() method provides access to the Unicode values of individual characters within a string. This fundamental string manipulation tool plays a crucial role in various applications, from basic character validation to complex text processing tasks that require precise control over character encoding. Understanding how charCodeAt() functions, including its limitations with surrogate pairs and handling of out-of-range indices, is essential for developers working with internationalized text in JavaScript applications.


## Basic Usage

The method accepts a single parameter: the index of the character. If no index is provided, it defaults to 0, returning the Unicode value of the first character in the string. The index refers to the position of the character in the string, with the first character having an index of 0, the second character at index 1, and so on. The index of the last character is string length - 1.

The method returns a number representing the UTF-16 code unit value of the character at the specified index. The return value is always less than 65,536, as higher code points are represented by pairs of 16-bit surrogate pseudo-characters. For example, the string "Hello, World!" would return the Unicode value 72 for 'H', 101 for 'e', and so on.

When the index provided is out of range (less than 0 or greater than or equal to the string length), the method returns NaN. It also returns NaN for non-integer index values, as demonstrated in the sample code: `greeting.charCodeAt(5.2)` and `greeting.charCodeAt(-9)` both return NaN. The method correctly handles negative indexing by treating it as 0, as shown in the example: `greeting.charCodeAt(-1)` would return the same value as `greeting.charCodeAt(0)` for a non-empty string.


## Unicode Code Units

The method works with 16-bit UTF-16 code units, returning values between 0 and 65,535. It's important to note that while higher Unicode code points exist (up to 1,114,111), charCodeAt() represents them using pairs of 16-bit surrogate pseudo-characters [1]. This limitation means that for characters requiring more than one code unit, only the first code unit's value is returned [2].

In practical terms, this method always returns a value less than 65,536. To obtain the complete Unicode code point for characters requiring multiple code units, developers should use the String.prototype.codePointAt() method instead, which is specifically designed to return full Unicode code points [3].

The method correctly identifies and handles edge cases where the index is out of range, returning NaN for indices less than 0 or greater than or equal to the string length [4]. Additionally, it correctly processes non-integer index values by converting them to integers, demonstrating its robustness in handling various input types [5].


## Character Code Retrieval

The method returns a number between 0 and 65,535 representing the Unicode value of the character at the specified index. The returned value corresponds to the UTF-16 code unit of the character, which is a 16-bit representation used in Unicode encoding [1].

If no index is provided, the method defaults to 0, returning the Unicode value of the first character in the string [2]. The string indices start from 0, similar to array indexing in JavaScript [3].

The return value represents the character at the specified position. For example, given the string "Hello, World!", `greeting.charCodeAt(0)` returns 72, which is the Unicode value for 'H' [4]. The method continues to return values for subsequent characters: 101 for 'e', 108 for 'l', and so on [5].

The method handles edge cases by returning NaN for invalid indices, non-integer values, or empty strings [6]. This ensures that the method behaves consistently across different input types and string states [7].

For practical applications, developers can use charCodeAt() to extract individual characters for processing. The provided example demonstrates this functionality with the string "A sample sentence for demoing how the method works" [8]. The method proves particularly useful for character-based operations such as sorting strings alphabetically, transforming case (lower to upper or vice versa), or working with character codes in events (keyCode) [9].


## Edge Cases

The method returns NaN for index values that are out of range (less than 0 or greater than or equal to the string length), as demonstrated in the sample code: `greeting.charCodeAt(18)` and `greeting.charCodeAt(-9)` both return NaN [1].

When no index is provided, the method defaults to 0, returning the Unicode value of the first character in the string [2]. This behavior ensures consistent handling of empty strings and missing parameters, always returning a valid Unicode value or NaN as appropriate [3].

The method treats non-integer index values as if they were converted to integers. This means that index values with decimal portions are rounded down to the nearest integer before processing [4]. For example, `greeting.charCodeAt(5.2)` returns 109, the same value as `greeting.charCodeAt(5)` [5]. This design choice maintains compatibility with array-like indexing while ensuring predictable numerical results [6].

A key limitation of the method is its handling of characters requiring multiple code units. While higher Unicode code points exist (up to 1,114,111), charCodeAt() represents them using pairs of 16-bit surrogate pseudo-characters [7]. This limitation means that for characters requiring more than one code unit, only the first code unit's value is returned [8]. To obtain the complete Unicode code point for characters of value 65536 and above, developers must retrieve both `charCodeAt(i)` and `charCodeAt(i+1)` [9].

In practice, developers should be aware that while the method correctly identifies and handles edge cases, it may not provide the full Unicode code point for characters represented by multiple code units [10]. For scenarios requiring complete code point information, alternative methods like String.prototype.codePointAt() should be used [11].


## Practical Applications

The method plays a crucial role in string validation, particularly in validating input to ensure it contains characters from specific Unicode ranges. For example, the provided function `isAlphaNumeric(input)` uses `charCodeAt()` to check if a string contains only numeric characters (0-9), uppercase letters (A-Z), and lowercase letters (a-z) [1].

In practical applications, developers also use the method to perform case transformation and character encoding tasks. The built-in JavaScript `String.fromCharCode()` method demonstrates how `charCodeAt()` values can be used to construct strings from their Unicode representations [2]. While `String.fromCharCode()` is deprecated and recommended to be replaced with the more modern `String.fromCodePoint()` method, it provides valuable insight into how Unicode values generated by `charCodeAt()` can be manipulated to create new strings [3].

The method's ability to return Unicode values for characters beyond the basic multilingual plane is particularly useful in character encoding tasks. For instance, it can be used to convert text to its corresponding Unicode code points for transmission or storage [4]. The method's compatibility with surrogate pairs for characters above 65,535 makes it valuable for handling Unicode compatibility characters and other specialized symbols [5].

While the method's primary use case is character retrieval, its return values enable a wide range of text processing operations. Code point analysis using `charCodeAt()` can help identify surrogate pairs in text, which is crucial for correct handling of Unicode characters [6]. This functionality enables developers to write robust text processing code that correctly handles the full range of Unicode characters [7].

