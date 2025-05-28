---

title: JavaScript String Methods: substring() vs substr()

date: 2025-05-27

---


# JavaScript String Methods: substring() vs substr()

Developing robust web applications requires a deep understanding of JavaScript's string manipulation methods. Two commonly used methods, substr() and substring(), offer similar functionality but have distinct behaviors that impact their reliability and maintainability. In this article, we'll explore the technical details of each method, comparing their syntax, parameter handling, and environmental compatibility. We'll also examine practical examples demonstrating their strengths and limitations, helping developers choose the most appropriate method for their projects.


## substr() Method

The substr() method functions by accepting a starting index and a length parameter to extract a portion of the string. It allows for negative starting indices, which count from the end of the string—a feature that makes its behavior somewhat inconsistent across different environments.

The method's syntax is `str.substr(start, length)`, where `start` indicates the position to begin extraction and `length` specifies the number of characters to include. If the length parameter is omitted, substr() extracts characters from the start index to the end of the string. Negative values for `start` count backwards from the end of the string, with the substring beginning at `max(start + str.length, 0)`.

However, despite its functionality, substr() has several significant drawbacks. It is not part of the core ECMAScript standard, meaning its behavior can vary between environments. Additionally, both slice() and substring() provide similar or superior functionality, making substr() redundant in modern applications.

Developers should avoid using substr() in new code due to its deprecated status and inconsistent behavior. While the method remains supported in all modern browsers, including Chrome, Edge, Firefox, Safari, and Opera, as well as Internet Explorer, its non-standard implementation makes it unsuitable for reliable cross-environment development. For existing legacy code using substr(), implementing a polyfill may be necessary to ensure compatibility with modern standards.


## substring() Method

The substring() method requires two parameters: startIndex and endIndex. The extracted substring remains part of the original string, while the source string remains unchanged. This syntax allows for flexible extraction based on character positions, as demonstrated in common examples that extract specific ranges of characters.

When both startIndex and endIndex are provided, the method returns characters from startIndex up to, but not including, endIndex. If endIndex is omitted, substring() extracts characters from startIndex to the end of the string. The method handles negative values for startIndex and endIndex: negative startIndex values are treated as 0, while negative endIndex values wrap to the tail of the string and work only when startIndex is less than endIndex.

The method's behavior differs when startIndex is greater than endIndex. In this case, substring() swaps the parameters to produce the substring, while slice() returns an empty string. This difference in handling reversed indices demonstrates substring()'s more intuitive approach to range specification.

Negative indices present additional behavior: when startIndex is negative, it sets the value to 0; when endIndex is negative, it wraps to the tail and works only when startIndex is less than endIndex. These rules for negative indices help simplify common string manipulation tasks, as explained in the documentation: "The method handles negative values for start and end indices, treating them as 0 and wrapping to the tail, respectively, when the other index is negative."

Developers can use substring() for various string manipulation tasks, including extracting specific substrings, removing prefixes or suffixes, and processing user input. The method's intuitive behavior with negative indices makes it particularly useful for tailoring string content based on dynamic index values, as demonstrated in examples that extract the final N characters of a string using negative indices.


## Sub Methods in Practice

Both methods demonstrate their practical applications through specific examples that highlight their respective behaviors. To extract the substring "World" from "Hello, World!", you can use either substr() with `str.substr(7)` or substring() with `str.substring(7, 12)`, demonstrating their ability to handle single-parameter extraction, where substring() extends to the end of the string when the second parameter is omitted.

The methods' handling of index parameters presents key differences that affect their practical use cases. For instance, consider extracting the last 3 characters of "01234". Using substr() with `aString.substr(-3)` correctly returns "lla", while substring() requires more complex syntax `aString.substring(aString.length - 3)`. This example illustrates substring()'s advantage in managing negative indices for flexible string manipulation.

Developers frequently need to work with dynamic index values, particularly when processing user input or parsing URLs. In such cases, substring() handles reversed indices more intuitively, automatically swapping startIndex and endIndex when startIndex > endIndex while slice() returns an empty string. This behavior is demonstrated when extracting a substring of "Mozilla" using `aString.substr(1, -1)`, which correctly returns "", compared to the more complex logic required with slice() when using negative indices.

The distinction between these methods becomes crucial when modifying source strings, as demonstrated by the method's treatment of parameter omission. When extracting "Mozilla" from aString, using substring() with either `aString.substring(0, 1)` or `aString.substring(1)` correctly returns "M" and "ozilla" respectively, while substr() returns "M" and "" when used without endIndex. These examples highlight substring()'s consistent behavior with parameter omission compared to substr()'s unpredictable outcomes.


## deprecated features

The ECMAScript standard explicitly states that the substr() method features are not considered part of the core ECMAScript language. While some implementations may still provide this functionality, developers should not rely on it for new code. The primary reasons for its deprecation include its non-standard status and redundant functionality provided by the more versatile substring() method.

The method's lack of standardization leads to inconsistent behavior across different environments. For instance, the second parameter's handling of negative values differs between substr() and substring(): while substring() treats both startIndex and endIndex as 0 when negative, substr() only treats endIndex negatively. This divergence in behavior can cause unexpected results when code needs to be ported between environments.

Developers should avoid using substr() in new code due to these limitations. When modifying source strings or working with dynamic index values, the more reliable substring() method automatically swaps indices when start > end, while substr() returns an empty string. This behavior difference becomes particularly problematic when implementing features that need to work consistently across various JavaScript environments.

