---

title: JavaScript String codePointAt() Method: Unicode Code Point Retrieval

date: 2025-05-26

---


# JavaScript String codePointAt() Method: Unicode Code Point Retrieval

JavaScript's `codePointAt()` method provides a powerful tool for working with Unicode characters, especially when dealing with surrogate pairs and supplementary characters. While similar to Java's implementation, it handles these complex cases differently, making it essential for developers working with multilingual or emojis. This article explores the method's behavior across various scenarios, from simple ASCII characters to the most complex Unicode code points, helping developers choose the right approach for their internationalized text processing needs.


## Origins and JavaScript Implementation

The `codePointAt()` method in JavaScript implements the specification from Java but processes surrogate pairs and Unicode characters differently. This method retrieves the Unicode code point for characters at specified positions in strings, handling multi-code-point characters and surrogate pairs appropriately.

For instance, when dealing with surrogate pairs, `codePointAt(0)` returns the code point of the first character, while `codePointAt(1)` returns the second character. The method correctly handles these pairs by returning the full code point when the index corresponds to the beginning of a surrogate pair.

The behavior of `codePointAt()` extends to various character types. For common ASCII characters, it returns the standard Unicode code point value. When working with non-ASCII characters, including emojis and complex symbols, the method ensures accurate retrieval of code points by properly managing surrogate pairs and multi-code-point characters.

Developers can utilize `codePointAt()` effectively by understanding its indexing mechanism. The method defaults to index 0 when no parameter is provided, making it straightforward to access the first code point of a string. However, for optimal Unicode character handling, particularly in scenarios involving surrogate pairs, the recommended approach is to use index-based loops with the string's iterator method, which processes characters by code points rather than UTF-16 code units.


## Method Syntax and Parameters

The `codePointAt()` method returns a non-negative integer representing the Unicode code point value of the character at the specified position in a string. This method works by taking a single parameter, `pos`, which indicates the position of the character to return the code point value from.

The method behavior is as follows:

1. If the input is `null` or `undefined`, a `TypeError` is thrown.

2. The input is converted to a string, and its length is determined.

3. The position is converted to an integer. If it's not a number, it is set to 0.

4. If the position is out of bounds (less than 0 or greater than or equal to the string's length), `undefined` is returned.

5. The method retrieves the first code unit at the specified position.

6. If the first code unit is a high surrogate (between 0xD800 and 0xDBFF), it checks if there is a corresponding low surrogate (between 0xDC00 and 0xDFFF) at the next position.

7. If a low surrogate is found, the method calculates the Unicode code point using the surrogate pair formula: `(first - 0xD800) * 0x400 + second - 0xDC00 + 0x10000`.

8. If no surrogate pair is found, the method returns the first code unit as is.

Edge cases are handled appropriately:

- For indices outside the string's length range, the method returns `undefined`.

- For non-integer inputs, the method uses zero as the default index value.

- Boolean values `true` and `false` default to index 1 and 0 respectively.

This method works across various JavaScript environments, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, supporting all modern browsers since June 2017. The polyfill implementation extends native String objects to include the `codePointAt()` functionality as specified in ECMAScript 2015 for environments without native support.


## Unicode Character Retrieval

The `codePointAt()` method retrieves the Unicode code point for characters at specified positions in strings, handling multi-code-point characters and surrogate pairs appropriately. When processing single-code-point characters, it returns the standard Unicode code point value. For multi-code-point characters, including those requiring surrogate pairs, the method correctly extracts the full code point.

The method demonstrates flexibility in handling different Unicode character ranges. When dealing with characters representable in a single UTF-16 code unit (between 0 and 65535), it provides the corresponding Unicode code point. For characters outside this range (0x010000 - 0x10FFFF), the method returns the full Unicode value, effectively managing supplementary characters that cannot be represented within a single code unit.

Developers can effectively use `codePointAt()` through various indexing strategies. When no position parameter is provided, it defaults to 0, allowing retrieval of the first code point in a string. For optimal Unicode character handling, particularly in scenarios involving surrogate pairs, developers are recommended to use index-based loops with the string's iterator method. This approach processes characters by code points rather than UTF-16 code units, ensuring accurate representation of complex Unicode characters.


## Method Behavior Across Browsers

The `codePointAt()` method has full support across modern browsers, starting with version 51 of Chrome, 12 of Edge, 29 of Firefox, 10 of Safari, and 28 of Opera, as documented in the ECMAScript 2015 specification. This functionality is available in all major desktop and mobile environments, including Android WebView, Chrome Android, Firefox Android, and Safari iOS.

The method returns a non-negative integer representing the Unicode code point value, with specific behaviors for different input conditions. When the index is valid (0 to string length - 1), it returns the Unicode code point value directly. For indices outside this range, it returns `undefined`. The method handles surrogate pairs by returning the full code point value when the index corresponds to the first character of a pair, and only the trailing surrogate code unit for the second character.

Developers should avoid using index-based loops when working with surrogate pairs, as this can lead to incorrect results. Instead, the recommended approach is to use a `for...of` statement or spread the string, both of which invoke the string's `[Symbol.iterator]()` method, iterating by code points. This allows developers to access the correct code point value using `codePointAt(0)` for each element.


## Best Practices and Alternative Methods

The `codePointAt()` method stands out for its precise Unicode character handling, particularly with characters requiring surrogate pairs and supplementary plane characters. It excels when working with complex symbols and internationalized text, making it essential for developers dealing with diverse languages and symbols.

When to Use `codePointAt()` versus `charCodeAt()`

The decision to use `codePointAt()` or `charCodeAt()` depends on the character and its representation requirements:

- Use `codePointAt()` for characters that span multiple UTF-16 code units, including those outside the Basic Multilingual Plane (UTF-16 range of 0x0000 to 0xFFFF). This method correctly handles surrogate pairs and returns the full code point value.

- Use `charCodeAt()` for characters representable in a single UTF-16 code unit (0x0000 to 0xFFFF), which makes it suitable for basic ASCII characters and common punctuation marks.

Best Practices

Developers should follow these guidelines for optimal Unicode character handling:

1. For strings containing characters requiring surrogate pairs, always use `codePointAt(0)` to access the complete code point value.

2. When working with emoji characters, recognize that they often consist of multiple code units. `codePointAt()` correctly handles these pairs, while `charCodeAt()` may return only the second half of surrogate pairs.

3. To safely access code points at specific positions, use the String iterator method. This approach processes characters by code points rather than UTF-16 code units, ensuring accurate representation of complex Unicode characters.

For scenarios involving supplementary characters (code points 0x010000 - 0x10FFFF), the `String.fromCodePoint()` method provides an alternative for both inserting and validating character values. This approach ensures compatibility with the ECMAScript 2026 Language Specification and maintains proper Unicode character representation across all modern browsers.

