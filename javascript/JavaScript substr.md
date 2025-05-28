---

title: JavaScript String.substr Method

date: 2025-05-27

---


# JavaScript String.substr Method

JavaScript's substr method provides a straightforward way to extract substrings based on start positions and optional lengths. While similar to modern alternatives like substring and slice, substr offers unique behavior particularly with negative indices. Understanding its quirks and limitations helps developers implement reliable string manipulation logic.


## substr Method Overview

substr is a string method in JavaScript that extracts a substring based on a start position and an optional length. The return value is a new string, and the original string is not modified. When only the start position is provided, the method extracts from that position to the end of the string.

The start position parameter uses 0-based indexing, where the first character is at index 0. Negative values count from the end of the string, with negative 1 referring to the last character. If the length parameter is omitted, all characters from the start position to the end of the string are included.

When the length parameter is specified, the method returns up to that many characters from the start position. If the length exceeds the string's remaining characters, the method returns the rest of the string. Both the start position and length parameters accept numbers, where decimal values are rounded down to the nearest integer.

The method also handles edge cases where start positions or lengths are non-numeric. In these cases, it treats the value as zero, except for negative start positions which wrap around from the end of the string. If both start and length are negative, the method returns an empty string.

The substr method is considered a legacy function and is less flexible than its alternatives, substring and slice. These modern methods provide similar functionality while handling edge cases and negative indices more consistently across environments.


## Method Syntax and Parameters

The substr() method syntax requires two parameters: start and length (optional). When only the start position is provided, the method extracts all characters from that position to the end of the string.

The start position uses 0-based indexing, meaning the first character is at index 0. Negative values count from the end of the string, with -1 referring to the last character. If the length parameter is omitted, the method extracts characters from the start position to the end of the string.

The length parameter determines the number of characters to extract from the start position. If the length exceeds the string's remaining characters, the method returns the rest of the string. Both start and length accept numbers, with decimal values rounding down to the nearest integer. Non-numeric values are treated as zero, except for negative start positions which wrap around from the end of the string. If both start and length are negative, the method returns an empty string.


## Positive and Negative Indexing

The substr method treats positive and negative start positions distinctly. When a positive index is provided, substr begins extraction at that position and continues to the end of the string if no length is specified. Here, the first character is at index 0, and the length parameter determines how many characters to extract.

Negative start positions work differently, counting backwards from the end of the string. For example, substr(-3) extracts the last three characters of the string. If both start and length are negative, the method returns an empty string.

The method handles edge cases where start positions or lengths are non-numeric. In these cases, it treats the value as zero, except for negative start positions, which wrap around from the end of the string. This behavior differs from the substring method, which always treats negative indices as 0.

When the length parameter is greater than the string's remaining characters, substr returns all remaining characters from the start position. Decimal or non-numeric length values are rounded down to the nearest integer, and non-numeric values are treated as zero.

The method's behavior with positive and negative indices is consistent across environments, making it a reliable choice for extracting substrings based on position. However, its handling of length parameters and negative values distinguishes it from the newer substring and slice methods, which provide more consistent behavior across different JavaScript implementations.


## Comparison with Other Methods

The substring and slice methods provide similar functionality to substr but with more consistent behavior across JavaScript environments. Substring requires two parameters: startIndex and endIndex (optional), where startIndex determines the beginning of the extraction and endIndex indicates where to stop. If endIndex is omitted, the method extracts from startIndex to the end of the string.

When only startIndex is provided, substring returns a tail of characters from that index to the end of the string. Both methods allow negative startIndex values, which count backwards from the end of the string. However, substring treats negative values as zero, while slice supports negative indices counting from the end.

A key difference between the methods is how they handle arguments: if startIndex is greater than endIndex, substring swaps them, while slice does not. This affects the method's return value, with substring returning an empty string in such cases. The length parameter also behaves differently between the methods - substring uses both parameters to determine the end index, while slice treats length as the number of characters to extract.

For developers, the preferred modern methods are substring and slice, as they provide better consistency and support for negative indices. Both are more widely supported across JavaScript environments and align with the ECMAScript standard. While substr remains functional for existing codebases, new development should use substring or slice for more reliable and maintainable string manipulation.


## Common Use Cases and Examples


### Extracting Specific Portions of Strings

The substr method enables developers to extract specific portions of strings using straightforward syntax. For example, substr(7, 5) extracts a substring from index 7 to 11 in the string "Hello, World!", returning "World".

Developers can use substr with a single parameter to extract from a specified index to the end of the string. The method handles negative indices by counting from the end of the string, making it flexible for various use cases.


### Example Usage: String Manipulation

A practical application of substr appears in the replaceString function, which demonstrates how to replace substrings within a string. Using substring with only a startIndex parameter, developers can efficiently replace portions of a string without modifying the original:

```javascript

function replaceString(text, oldS, newS) {

  return text.substring(text.indexOf(oldS), text.indexOf(oldS) + oldS.length).replace(oldS, newS);

}

```


### Negative Indices and Edge Cases

The substr method handles negative indices effectively, counting from the end of the string. For instance, substr(-3) extracts the last three characters from any string, making it simple to access specific portions of text data.

Developers should be aware that substr's behavior with negative lengths is different from substring: substr treats negative lengths as zero, while substring swaps the indices. This distinction highlights the importance of understanding the specific method requirements for reliable string manipulation.

