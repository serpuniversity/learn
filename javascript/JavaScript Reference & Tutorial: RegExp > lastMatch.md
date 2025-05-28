---

title: JavaScript lastMatch Property

date: 2025-05-26

---


# JavaScript lastMatch Property

The lastMatch property in JavaScript's RegExp object plays a crucial role in modern string manipulation and pattern matching, serving as the contemporary alternative to the legacy $& property. This powerful feature allows developers to access the last matched substring directly, making it essential for implementing stateful matching behavior across multiple operations. In this article, we'll explore the nuances of lastMatch, its behavior with different regular expression flags, and practical applications in string manipulation and pattern matching. Understanding this property enables developers to write more robust and efficient JavaScript code for parsing and processing text data.


## lastMatch Property Basics

The lastMatch property of the RegExp object in JavaScript returns the last matched characters in a string, serving as the modern equivalent to the legacy $& property for accessing the last matched substring. This property is particularly useful in scenarios requiring iterative or position-based matching, where the stateful behavior of regular expressions can be leveraged to maintain search position across multiple operations.

When working with regular expressions, developers should be aware that the underlying lastIndex property can affect matching behavior, especially when using global or sticky flags. To avoid issues with non-zero lastIndex values between operations, developers can reset lastIndex to 0 before each search using `regexp.lastIndex = 0`. Alternatively, string methods like `str.match` can be used to avoid lastIndex altogether.

The lastMatch property behaves consistently across modern JavaScript implementations, allowing developers to rely on its presence for accessing the last matched substring in their applications.


## lastMatch vs. Legacy $& Property

The lastMatch property functions as the modern equivalent to the legacy $& property for accessing the last matched substring. The property returns the matched substring, updating whenever a RegExp instance successfully matches. If no matches have been made, lastMatch returns an empty string. This behavior is consistent across modern JavaScript implementations, though developers should note that the underlying lastIndex property can affect matching behavior when using global, ignoreCase, or multiline flags. To maintain search position across operations, developers can reset lastIndex to 0 before each search using `regexp.lastIndex = 0`. Alternatively, string methods like `str.match` can be used to avoid lastIndex altogether.

The lastMatch property facilitates usage in scenarios requiring iterative or position-based matching, maintaining the stateful behavior of regular expressions for subsequent operations. For developers working with regular expressions in JavaScript, understanding both the lastMatch and legacy $& properties enables more effective string manipulation and pattern matching.


## lastMatch with match() Method


### lastMatch with match() Method

The match() method with global flag returns an array of all matches, while the replacement string can reference groups using $&. This property behaves consistently across modern JavaScript implementations, though developers should note that the underlying lastIndex property affects matching behavior when using global, ignoreCase, or multiline flags. To maintain search position across operations, developers can reset lastIndex to 0 before each search using regexp.lastIndex = 0. Alternatively, string methods like str.match can be used to avoid lastIndex altogether.

When working with regular expressions in JavaScript, developers can use lastMatch in the replacement string of String.prototype.replace(), but this functionality is independent of the RegExp["$&"] legacy property. The lastMatch property is essential for maintaining stateful matching behavior across multiple operations, particularly when iterating through matches in a string.

As demonstrated in the MDN Web Docs, the lastMatch property returns the last overall match in the match() method with global flag. For example, when using a global flag with the regular expression /hi/, the lastMatch property will contain the last occurrence of "hi" in the matched string.

The property maintains compatibility with legacy functionality, as noted in the provided documentation. This includes support for named capturing groups in browsers that implement this feature, as shown in the example usage:

```javascript

const re = /hi/g;

re.test("hi there!");

RegExp.lastMatch; // "hi"

RegExp["$&"]; // "hi"

```

Understanding the interaction between lastMatch and global flag is crucial for effective regular expression usage in JavaScript. The property enables developers to maintain stateful matching behavior while iterating through multiple matches in a string, providing a powerful tool for string manipulation and pattern matching applications.


## lastMatch and Regular Expression Flags

The behavior of the lastMatch property depends on the specific flags used with the regular expression. When using the global flag (g), lastMatch returns the last match found in the string. The property's value updates based on the match results, providing an accurate representation of the most recent match.

For regular expressions with the global flag enabled, the lastMatch property behaves consistently across modern JavaScript implementations. This consistency enables developers to maintain stateful matching behavior across multiple operations, particularly when iterating through matches in a string.

When working with regular expressions in JavaScript, understanding the interaction between lastMatch and the global flag is crucial for effective string manipulation and pattern matching. The property returns the last overall match in the match() method with global flag, as demonstrated in the MDN Web Docs example:

```javascript

const re = /hi/g;

re.test("hi there!");

RegExp.lastMatch; // "hi"

```

The lastMatch property also interacts with other flags to determine its behavior. When using the ignoreCase (i) or multiline (m) flags, the property continues to return the last matched substring as expected. These flags affect matching behavior by enabling case-insensitive matching or multi-line pattern recognition, respectively, without altering the fundamental functionality of lastMatch.

Developers should note that the underlying lastIndex property can impact matching behavior, particularly when using global, ignoreCase, or multiline flags. To maintain search position across operations, developers can reset lastIndex to 0 before each search using `regexp.lastIndex = 0`. Alternatively, string methods like `str.match` can be used to avoid lastIndex altogether.

When working with regular expressions in JavaScript, understanding the behavior of lastMatch with different flag combinations enables developers to maintain precise control over their matching operations. This knowledge is particularly valuable when implementing complex string manipulation or pattern matching functionality in JavaScript applications.


## lastMatch in Practice

The lastMatch property enables developers to maintain stateful matching behavior while iterating through matches in a string. This functionality is particularly useful when implementing complex string manipulation or pattern matching functionality in JavaScript applications.


### Iterating through Matches in a String

The provided documentation demonstrates how to use RegExp.lastIndex and RegExp.exec() in JavaScript for iterating through matches. When working with regular expressions in JavaScript, developers can use the following approach to maintain precise control over their matching operations:

```javascript

const str = 'a a a';

const re = /a/g;

while (match = re.exec(str)) {

  console.log(match, ' found at : ', match.index);

}

```

This code uses a while loop to find all matches of the pattern /a/g in the string str. The match variable holds the current match, and match.index shows the index where the match was found.

Here's another example demonstrating using RegExp.lastIndex to keep track of the last match position:

```javascript

let text = `How much wood would a woodchuck chuck if a woodchuck could chuck wood?`;

let re = /wood/g;

let lastMatch;

while (lastMatch = re.exec(text)) {

  console.log(lastMatch);

  console.log(re.lastIndex);

  // Avoid infinite loop if(!re.global) break;

}

```

In this code, RegExp.lastIndex is used to track the position for the next match. The lastMatch variable holds the current match, and re.lastIndex shows the current position to start searching for the next match. The loop continues until re.global is false, preventing an infinite loop.


### Extracting the Last Match

The lastMatch property can be effectively used to extract the last match from a string. The documentation provides two JavaScript solutions for this purpose:

1. The first solution uses the original regex `/@(\w+)/ig` and modifies the code to:

```javascript

matches.pop();  // get the last match

// Optionally keep the original matches array

matches[matches.length - 1];

// Update the #result element with the last match

document.getElementById('result').textContent = matches.pop();

// Run on keyup events

```

2. The second solution uses a modified regex `/@(\w+)$/ig` and provides an alternative approach:

```javascript

const split = str.split(/(@[^ ]*)/);

split.length > 1 ? split[split.length - 2] : '';

```

The second solution works only if the @word is the last word of the phrase, while the first solution handles cases where @word appears multiple times.

