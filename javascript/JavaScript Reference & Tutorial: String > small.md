---

title: JavaScript String Small Method and Other String Manipulation Techniques

date: 2025-05-27

---


# JavaScript String Small Method and Other String Manipulation Techniques

JavaScript strings are powerful tools for handling text data, and mastering their methods can significantly enhance your web development capabilities. From extracting substrings to transforming and comparing strings, these built-in functions provide versatile options for text manipulation. While some legacy methods like small() have been deprecated, understanding both the modern and older approaches will help you write more efficient, maintainable code. This article explores essential string manipulation techniques, comparing modern and legacy methods to help you choose the right tools for your projects.


## String Small Method

The small() method creates a string wrapped in a <small> element. It began as part of the ECMAScript standard primarily for compatibility reasons, though it's no longer recommended for use. The method generates a string structure starting with <small>, containing the original text, and ending with </small>. While it's documented in the latest ECMAScript specifications, its use is deprecated, and modern web development recommends alternative DOM API approaches for creating HTML elements.


## String Methods Overview

JavaScript strings possess numerous methods for handling and manipulating text. These methods enable developers to perform operations such as substring extraction, character access, and numeric conversion, among others.

The `slice()` and `substring()` methods enable developers to extract portions of strings. While similar in functionality, they accept different parameters: `slice()` requires both a start and end index, with an optional end parameter that defaults to the end of the string, while `substring()` requires only start and end indices.

For character access, developers have several options: `charAt()`, `charCodeAt()`, and the recently introduced `at()` method. The `charAt()` method returns the character at a specified index, while `charCodeAt()` returns the Unicode value of the character at that index. The `at()` method, available in modern browsers since March 2023, provides an alternative way to access characters and supports negative indexing.

When working with string lengths, developers can utilize the built-in `length` property or employ methods like `localeCompare()`, `startsWith()`, and `endsWith()`, which also interact with string properties and methods. These methods offer developers versatile options for manipulating and comparing strings while maintaining the integrity of their original data.


## String Manipulation Techniques


### String Manipulation Techniques


#### Substring Extraction

JavaScript's substring extraction methods offer versatile ways to manipulate string content. The `slice()` method extracts portions of a string based on start and end indices, with an optional second parameter that defaults to the end of the string. Alternatively, `substring()` requires both start and end indices, providing similar functionality with slightly different parameter requirements.

To extract station codes and names from a list of identifiers, developers can use these methods in combination with other techniques. For example, the code selects the output list element using `document.querySelector('.output ul')`, then iterates through an array of station identifiers. It extracts the first three characters using `station.slice(0,3)` and finds the semicolon position using `station.indexOf(';')`. The station name is then extracted from the substring following the semicolon using `station.slice(semiColon + 1)`.


#### String Transformation

Developers can transform strings using methods like `toUpperCase()` and `toLowerCase()`. The `toUpperCase()` method converts all characters in a string to uppercase, while `toLowerCase()` performs the opposite transformation. These methods return new strings rather than modifying the original data.

The `trim()` method removes white spaces from both ends of a string, while `trimStart()` and `trimEnd()` specifically address leading and trailing spaces, respectively. The `padStart()` method adds padding characters to the left end of a string until it reaches the specified length. Together, these methods enable precise control over string formatting and padding.


#### String Searching and Comparison

For substring searches, developers can use methods like `indexOf()`, `includes()`, and `startsWith()`. The `indexOf()` method returns the index of the first occurrence of a specified value in a string, while `includes()` checks if a string contains a specific substring and returns a boolean result. The `startsWith()` method determines if a string begins with a specified value.

Developers can also compare strings using the equality (`==`) and inequality (`!=`) operators. However, these operators compare strings based on their character codes by default. For language-specific comparisons, the `localeCompare()` method is recommended, returning a negative number if the first string is less than the second, a positive number if greater, and 0 if they are equivalent. This method takes into account the host machine's current locale, providing more accurate comparison results.


## Legacy vs Modern String Handling

The evolution of JavaScript's string handling reflects broader changes in web development best practices, with modern methods offering both enhanced functionality and improved performance. Developers today have access to powerful string manipulation tools while facing the challenge of maintaining compatibility with older browsers.


### String Length and Basic Properties

JavaScript strings maintain several useful properties and methods. The `length` property returns the number of characters in a string, while square bracket notation allows direct character access. The `includes()` method checks for substring presence, and `indexOf()` finds the position of a substring, returning -1 if not found.


### Modern String Manipulation Methods

Several modern string methods offer significant improvements over legacy approaches. The `trim()` method removes leading and trailing white space, with `trimStart()` and `trimEnd()` providing more granular control for different scenarios. The `repeat()` method creates a new string containing multiple copies of the original, while `split()` efficiently converts strings into arrays based on specified separators.


### Legacy String Handling Methods

The `small()` method and other HTML wrapper functions represent legacy approaches now deprecated in favor of DOM APIs. These methods create strings wrapped in HTML elements like <small>str</small>, highlighting the shifting responsibility for HTML structure from JavaScript to the Document Object Model.


### Best Practices

Developers should prioritize modern string methods for their enhanced functionality and better performance. While the transition from legacy methods like `small()` may require updating existing code, the resulting improvements in maintainability and compliance with web standards make the effort worthwhile. Modern JavaScript versions offer robust alternatives that align with current web development best practices.

