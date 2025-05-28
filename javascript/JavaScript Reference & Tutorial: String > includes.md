---

title: JavaScript String includes() Method

date: 2025-05-27

---


# JavaScript String includes() Method

Checking for substring presence is a common operation in JavaScript, and the includes() method provides a straightforward way to perform these checks. This article explores the basics of includes(), including its parameters and behavior, while also discussing important considerations such as case sensitivity, nested array search, and browser support. You'll learn how to use includes() effectively, understand its limitations, and discover how it fits into the broader landscape of JavaScript string manipulation tools.


## Basic Usage and Parameters

The includes() method is a built-in function that checks if a specific substring is present within a given string. It performs this check with case sensitivity, meaning that it distinguishes between uppercase and lowercase characters.

Basic Usage:

The method is invoked using the syntax string.includes(substring, startPosition). Here, substring represents the value you're searching for within the string, and startPosition (optional) indicates where to begin the search within the string.

Key Parameters:

- substring: The value to search for within the string. This can be any valid JavaScript value, including other strings, which will be coerced to strings if needed.

- startPosition: An integer indicating the index position to start searching from. If omitted, the search begins at the start of the string. Negative indices count from the end of the string, with -1 representing the last character.

The method returns true if the substring is found anywhere within the string, including when the substring is an empty string. If the substring is not found, the method returns false.

Examples:

Check if a word exists in a sentence:

const sentence = "Welcome to freeCodeCamp!";

const word = "freeCodeCamp";

console.log(sentence.includes(word)); // Output: true

Search with a starting position:

const sentence = "Welcome to freeCodeCamp!";

console.log(sentence.includes("freeCodeCamp", 1)); // Output: false


## Case Sensitivity

The includes() method is case-sensitive, treating uppercase and lowercase characters as distinct values. This means that 'LOVE' and 'love' are considered different strings.

To perform case-insensitive searches, you can convert both the main string and the substring to the same case using the toLowerCase() or toUpperCase() methods. For example, when checking if 'love' is in 'I love freeCodeCamp', the comparison would fail due to case sensitivity. However, by converting both strings to lowercase:

```javascript

const sentence = "I love freeCodeCamp";

const word = "love";

console.log(sentence.toLowerCase().includes(word.toLowerCase())); // Output: true

```

The includes() method's case sensitivity can affect results when dealing with multiple occurrences of the same string in different cases. For instance, searching for 'To be' in 'To be, or not to be, that is the question.' returns false due to case sensitivity, while converting both to lowercase resolves this:

```javascript

const str = "To be, or not to be, that is the question.";

console.log(str.toLowerCase().includes("to be")); // Output: true

```


## Nested Arrays

The includes() method cannot search nested arrays directly. For nested arrays, you can use nested loops or combine includes() with Array.prototype.some() to achieve the desired functionality.


### Nested Loops Example

```javascript

const nestedArray = [["alpha", "beta"], ["gamma", "delta"], ["epsilon"]];

const target = "beta";

for (let i = 0; i < nestedArray.length; i++) {

  const innerArray = nestedArray[i];

  for (let j = 0; j < innerArray.length; j++) {

    if (innerArray[j].includes(target)) {

      console.log(`Found "${target}" at index [${i}][${j}]`);

    }

  }

}

```


### Array.prototype.some() Example

```javascript

const nestedArray = [["alpha", "beta"], ["gamma", "delta"], ["epsilon"]];

const target = "beta";

const found = nestedArray.some(innerArray => innerArray.some(word => word.includes(target)));

console.log(`Nested Array includes "${target}": ${found}`);

```

These solutions demonstrate practical approaches for searching within nested arrays while leveraging JavaScript's built-in array methods.


## Browser Support

The includes() method is an ECMAScript6 (ES6) feature with robust browser support across modern browsers since June 2017. Current compatibility stands at:

- Google Chrome 51

- Microsoft Edge 15

- Mozilla Firefox 54

- Apple Safari 10

- Opera 38

These specifications ensure compatibility with all major modern browser environments, while older browsers receive support through alternative methods like the indexOf() implementation.

For developer convenience, including backwards compatibility, the method employs a fallback behavior in environments where native support is lacking. This design choice enables consistent string search functionality across both modern and legacy browser versions.


## Related Methods

The includes() method is part of a larger ecosystem of JavaScript string methods designed to facilitate various aspects of text manipulation. These methods include tools for matching patterns (`match()` and `matchAll()`), normalizing Unicode text (`normalize()`), padding strings (`padEnd()` and `padStart()`), repeating strings (`repeat()`), and replacing substrings (`replace()` and `replaceAll()`).

For developers working with strings, combining these methods allows for sophisticated text processing capabilities. For instance, to check if a string contains any of multiple values, developers can use the `.some()` method in combination with includes():

```javascript

const fruitsArray = ["apple", "pear", "orange"];

const fruit = "grape";

fruitsArray.some(fruit => input.includes(fruit))

```

Alternately, regular expressions provide another powerful approach to pattern matching:

```javascript

const input = "Apple pie with fresh pears";

if (/Apple|pear/.test(input)) {

  console.log("Match found");

}

```

Developers should be aware that some methods listed in the documentation, such as `toWellFormed()` and the deprecated `.substr()` function, create non-standard or potentially insecure markup. Modern JavaScript developers are encouraged to use `.slice()` for string extraction and regular methods for handling Unicode characters.

The includes() method's flexible parameters, case sensitivity, and cross-browser compatibility make it a valuable tool for developers building robust JavaScript applications. Whether working on simple string comparisons or complex text processing tasks, understanding these related methods and their proper usage is essential for JavaScript development.

