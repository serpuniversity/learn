---

title: JavaScript String Methods: search, find, and manipulate text

date: 2025-05-27

---


# JavaScript String Methods: search, find, and manipulate text

JavaScript's powerful string manipulation capabilities enable developers to efficiently process textual data in their applications. This article explores essential string methods for searching and manipulating text, including `indexOf()`, `lastIndexOf()`, and `includes()`. We'll examine how these methods work together to enable precise substring location and demonstrate practical usage scenarios. Additionally, we'll look at techniques for extracting substrings using `slice()`, `substring()`, and `substr()`, and discuss best practices for performing case-sensitive and case-insensitive searches. By mastering these fundamental string operations, developers can build more robust and efficient text processing functionality into their JavaScript applications.


## String search methods

JavaScript's string search methods include `indexOf()`, `lastIndexOf()`, and `includes()`, providing developers with flexible ways to locate substrings within strings.


### indexOf() and lastIndexOf()

The `indexOf()` method searches for a substring within a string and returns the index of its first occurrence. If the substring is not found, it returns `-1`. For example:

```javascript

const tagline = "MDN - Resources for developers, by developers";

console.log(tagline.indexOf("developers")); // 20

console.log(tagline.indexOf("x")); // -1

```

To find subsequent occurrences, you can provide a starting index as the second parameter:

```javascript

const firstOccurrence = tagline.indexOf("developers");

const secondOccurrence = tagline.indexOf("developers", firstOccurrence + 1);

console.log(firstOccurrence); // 20

console.log(secondOccurrence); // 35

```

The `lastIndexOf()` method works similarly but searches from the end of the string, returning the index of the last occurrence of the substring:

```javascript

console.log(tagline.lastIndexOf("developers")); // 35

console.log(tagline.lastIndexOf("x")); // -1

```


### includes()

The `includes()` method checks for substring presence, returning `true` if the substring is found and `false` otherwise. This method offers a concise way to perform case-sensitive substring checks:

```javascript

const sentence = "The brown fox jumps from the tree.";

console.log(sentence.includes("fox")); // true

console.log(sentence.includes("cat")); // false

```

This method also supports checking substrings at specific positions by providing an additional parameter:

```javascript

const filename = "document.pdf";

console.log(filename.endsWith(".pdf")); // true

console.log(filename.endsWith(".docx")); // false

```

These methods together provide a robust foundation for text search operations in JavaScript, supporting both simple and complex pattern matching needs.


## Finding substring positions

The `slice()` method extracts a portion of a string from a specified start index to an end index (exclusive), returning a new string. For negative indices, `slice()` allows extraction from the end of the string. For example:

```javascript

const browserType = "mozilla";

console.log(browserType.slice(1, 4)); // "ozi"

console.log(browserType.slice(2)); // "zilla"

```

The `substring()` method extracts a specified portion of a string but does not support negative indices, treating them as 0. This limitation makes it less versatile than `slice()` for certain extraction needs:

```javascript

const sentence = "The quick brown fox";

console.log(sentence.substring(10, 13)); // "brown"

```

In practice, developers often use `slice()` for its flexibility in handling both positive and negative indices:

```javascript

const browserType = "mozilla";

console.log(browserType.slice(-5)); // "zilla"

```

The `substr()` method extracts a portion of the original string from a specified index, accepting two parameters: a start index and an optional length. This method does not support negative indices, making it less suitable for end extraction compared to `slice()`:

```javascript

const browserType = "mozilla";

console.log(browserType.substr(1, 3)); // "olu"

```


## Case-sensitive searching

JavaScript's string comparison is case-sensitive by default, meaning "Apple" and "apple" would be considered different strings. To perform case-insensitive comparisons, developers often use methods like `toUpperCase()` or `toLowerCase()`, though these have limitations with certain characters outside the Latin alphabet.

For more robust case-insensitive searching, developers can use the `localeCompare()` method with specific locale settings. For example, to ignore case differences in Turkish strings, you would use `localeCompare("string", "otherString", { sensitivity: "base" })`.

When performing case-sensitive substring searches, developers must ensure that both the target string and pattern match exactly. Using methods like `includes()` directly performs case-sensitive checks, while `indexOf()` and `lastIndexOf()` require matching case. For case-insensitive searches, always consider converting both strings to the same case using `toUpperCase()` or `toLowerCase()` before comparison.


## Finding multiple occurrences

To find all occurrences of a substring within a string, developers often use a loop that continues until the `indexOf` method returns -1, indicating no more matches. Each iteration updates the search position with `pos = foundPos + 1` to ensure all instances are found, even when they overlap.

```javascript

function getAllOccurrences(str, pattern) {

  const positions = [];

  let pos = str.indexOf(pattern);

  while (pos !== -1) {

    positions.push(pos);

    pos = str.indexOf(pattern, pos + 1);

  }

  return positions;

}

const text = "banana";

const pattern = "na";

console.log(getAllOccurrences(text, pattern)); // [2, 4]

```

The `lastIndexOf` method can also be used to find occurrences in reverse order:

```javascript

function getAllOccurrencesBackwards(str, pattern) {

  const positions = [];

  let pos = str.lastIndexOf(pattern);

  while (pos !== -1) {

    positions.push(pos);

    pos = str.lastIndexOf(pattern, pos - 1);

  }

  return positions;

}

console.log(getAllOccurrencesBackwards(text, pattern)); // [4, 2]

```

For performance optimization, especially in cases where substrings can overlap, developers may implement custom algorithms that track both the current position and the last match position to avoid redundant searches.

