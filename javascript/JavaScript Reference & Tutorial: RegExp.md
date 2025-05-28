---

title: JavaScript RegExp: Regular Expression Reference & Tutorial

date: 2025-05-26

---


# JavaScript RegExp: Regular Expression Reference & Tutorial

JavaScript's regular expressions provide a powerful way to search, match, and manipulate text patterns within strings. This comprehensive guide covers the basics of regular expression syntax and pattern matching, including character classes, quantifiers, and advanced features like Unicode support and look-ahead assertions. The article also explains how to create and compile regular expressions using both literal notation and the constructor function, while demonstrating practical applications in form validation, data parsing, and URL routing. Through numerous examples, readers will learn how to wield this essential tool for text processing and pattern matching in modern web development.


## Basic Syntax and Pattern Matching

JavaScript regular expressions can be created in two primary ways: using a literal expression between forward slashes (`/pattern/`) or through the `RegExp` constructor function, which allows for dynamic pattern creation. The constructor requires both the pattern and optional flags as arguments: `new RegExp(pattern[, flags])`.

The pattern itself consists of literal characters that must match exactly, as well as special characters that enhance matching capabilities. These special characters can be grouped into character sets, using square brackets (`[abc]`) to match any of the enclosed characters. Ranges can be specified using a hyphen (`[0-9]` matches any digit).

Regular expressions also support various quantifiers to control matching frequency. The asterisk (`*`) matches zero or more occurrences of the preceding character, while the plus (`+`) matches one or more occurrences. Curly braces (`{}`) can specify an exact number of occurrences, as demonstrated by the pattern `/a{2,4}/g` which matches "aa", "aaa", "aaaa" but not "a" or "ab".

The AND and OR operators are represented by concatenation (`ab`) and alternation (`a|b`), respectively. Additional assertions test string conditions without consuming characters - input boundary assertions use `^` for start and `$` for end, while lookahead assertions check for following patterns using `(?=...)` and those not following using `(?!...)`.

For advanced matching capabilities, special flags modify the behavior of regular expressions. Common flags include case-insensitive matching (`i`), global search (`g`), and multiline mode (`m`). The Unicode flag (`u`) enables proper handling of characters represented by multiple code points, ensuring correct matching for characters like "é" when represented as `\u00e9` or `\u0065\u0301`.

To demonstrate, consider the following examples:

```javascript

// Matching any digit

const regex1 = /\d/;

console.log(regex1.test("42")); // true

// Matching words starting with 'ward'

const regex2 = /\bward/gi;

console.log(regex2.test("ward")); // true

console.log(regex2.test("fourthward")); // false

// Matching URLs using character classes

const regex3 = /[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}/;

const text = "Visit our website at example.com or contact us via support@example.org.";

const matches = text.match(regex3);

console.log(matches); // ["example.com", "example.org"]

```

These examples illustrate the fundamental capabilities of JavaScript regular expressions for pattern matching and text manipulation.


## Creating and Compiling Regular Expressions

Regular expressions in JavaScript can be created using two primary methods: literal notation and the constructor function. Both methods produce regex objects with identical methods and properties, though the constructor function offers more dynamic flexibility.


### Literal Notation

Literal notation, the most common approach, uses a pattern between forward slashes, optionally followed by flags. For example:

```javascript

const literalRegex = /ab+c/i; // Case-insensitive matching of 'ab+c'

```

This method directly incorporates the pattern into the code, making it convenient for static expressions. Patterns must appear exactly as specified, with special characters requiring backslash escaping.


### Constructor Function

The constructor function creates regular expressions through runtime compilation. It accepts either a string pattern or another RegExp object as its first argument, followed by an optional flags string:

```javascript

const constructorRegex = new RegExp("ab+c", "i"); // Case-insensitive matching of 'ab+c'

const literalConstructorRegex = new RegExp(/ab+c/, "i"); // Using a literal pattern with flags

```

This approach is particularly useful for dynamically generated patterns based on user input or other conditions.


### Compilation Process

Before use, regular expressions must be compiled. This occurs automatically during script execution when using literal notation, but requires explicit compilation when using the constructor function. Proper compilation ensures correct pattern matching and behavior.


### Constructor Flags

The constructor function allows specifying flags that modify regex behavior:

```javascript

const globalSearch = new RegExp("ab+c", "g"); // Find all occurrences of 'ab+c'

const caseInsensitive = new RegExp("ab+c", "i"); // Case-insensitive matching of 'ab+c'

```

These flags can be combined in a single expression without affecting order. The constructor function provides explicit control over regex properties, making it suitable for dynamic pattern creation and modification.


## Pattern Matching Characters and Symbols

Regular expressions in JavaScript consist of simple characters or combinations of simple and special characters, with special characters providing enhanced pattern matching capabilities. These special characters include:

- Metacharacters: Square brackets [ ] specify a set of characters to match, with ranges defined between two characters (e.g., [a-e] = [abcde]). The caret ^ at the start of a square bracket set inverts the set, matching any character not listed. The period . matches any single character except newline, while caret ^ checks if a string starts with a certain character and dollar $ checks if it ends with a certain character.

- Quantifiers: The asterisk * matches zero or more occurrences of the preceding pattern, the plus + matches one or more occurrences, and the question mark ? matches zero or one occurrence. Curly braces {} define a range of repetitions, such as exactly n occurrences (e.g., {3}) or between n and m occurrences (e.g., {2,4}).

- Set and range characters: Square brackets [ ] define character sets, with ranges specified between two characters (e.g., [0-9] matches any digit). Special character groups have built-in patterns, such as \d for any digit, \w for any word character, and \s for any whitespace character. Their negated forms are \D for any non-digit, \W for any non-word character, and \S for any non-whitespace character.

- Alternative matching: The vertical bar | represents alternation, matching either the expression before or after (e.g., a|b matches either 'a' or 'b'). Parentheses () group sub-patterns, allowing the application of quantifiers to multiple characters (e.g., (ab)* matches "a", "ab", "abb", etc.).

- Backreference: Parentheses in patterns serve as memory devices, capturing parts of the pattern that can be referenced later using backreferences. The entire capturing group can be referenced using $1, $2, etc., while individual capturing subgroups can be referenced using $1.1, $1.2, etc.

- Unicode handling: The u flag enables proper handling of characters represented by multiple code points, ensuring correct matching for characters like "é" when represented as \u00e9 or \u0065\u0301. The constructor function allows runtime compilation of patterns from dynamic input, with both literal and constructor methods producing regex objects with identical methods and properties.


## Matching Methods and Flags

JavaScript's RegExp methods enable powerful text processing capabilities, with both the `RegExp` object and string methods supporting a wide range of operations. The core methods include:

- Test: The `test()` method checks for a match between a regular expression and a string, returning `true` or `false`. When used with the `i` flag, it performs case-insensitive matching.

- Replace: The `replace()` method performs search and replace operations based on the regular expression. It can accept either a string replacement or a function to generate the replacement text. The `replaceAll()` method, introduced in ECMAScript 2021, replaces all occurrences of a string within the target string, requiring the `g` flag for global search.

- Exec: The `exec()` method searches the target string for a match and returns an array containing the results. With the `g` flag, it returns an array of matches. The method updates the `lastIndex` property, allowing for multi-pass searches or searches starting from a specific position.

- Match: The `match()` method returns an array of all matches in a string. When using the `g` flag, it returns all matches. For non-global searches, it returns the first match as an array.

The `matchAll()` method, available in ECMAScript 2020, returns an iterator that produces all matches, including capturing groups. This method is particularly useful for complex pattern matching and text extraction tasks.

To illustrate these capabilities, consider the following examples:

```javascript

// Using test() and replace()

const regex = /apple/;

const fruit = "apple banana apple cherry";

console.log(regex.test(fruit)); // true

console.log(fruit.replace(/apple/g, "orange")); // "orange banana orange cherry"

// Using match() and matchAll()

const ingredients = "2 cups flour, 1 cup sugar, 3 eggs";

const pattern = /(\d+)\s+(\w+)/g;

console.log(ingredients.match(pattern)); // ["2 cups", "1 cup", "3 eggs"]

const allMatches = [...ingredients.matchAll(pattern)];

console.log(allMatches); // Array with all matches

```

These examples demonstrate the versatility of JavaScript's regular expression methods for practical text processing tasks.


## Real-World Applications

Regular expressions in JavaScript enable powerful text processing capabilities across various applications. The language's native implementation, while not fully PCRE compatible, supports the essential features required for effective string manipulation.


### Form Validation

The `RegExp` object forms the foundation for JavaScript's regular expression functionality. As demonstrated in the Honeybadger.io guide, developers can create patterns to validate user input. For instance, the following regular expression checks if a string contains at least one digit:

```javascript

/[\d]/.test("abc123") // true

```


### Data Parsing and Search and Replace

Regular expressions excel at extracting structured data from unformatted text. The MDN Web Docs guide illustrates this capability through an example that matches URLs using a character class:

```javascript

const text = "Visit our website at example.com or contact us via support@example.org.";

const pattern = /[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}/g;

console.log(text.match(pattern)) // ["example.com", "example.org"]

```

The guide also highlights the replace method's versatility, demonstrating how to remove non-alphanumeric characters from a string.


### URL Routing

For dynamic web applications, regular expressions enable sophisticated URL matching. The Honeybadger.io guide showcases this functionality by extracting parameters from URLs using capture groups:

```javascript

const url = "/users/123";

const pattern = /^\/users\/(\d+)$/;

const match = url.match(pattern);

console.log(match) // ["users/123", "123"]

```


### Performance and Security

While the text from Regexr and Regex101 focuses on advanced usage, it's crucial to note the importance of regex performance. The guide cautions against catastrophic backtracking, offering practical tools for optimizing complex patterns.


### Unicode Support

The Honeybadger.io guide emphasizes JavaScript's Unicode capabilities through detailed examples. The following pattern correctly matches both the direct Unicode representation and the combined code points for "é":

```javascript

console.log(/\u00e9/.test("é")) // true

console.log(/\u0065\u0301/.test("é")) // true

console.log(/\u00e9/u.test("é")) // true (Unicode mode)

```


### Method Usage

The guide provides comprehensive coverage of key methods, including:

- `match()` and `matchAll()` for pattern matching

- `exec()` for multi-pass searches

- `test()` for boolean matching

- `replace()` and `replaceAll()` for text replacement

These methods enable developers to perform sophisticated text operations efficiently, as demonstrated in the example that removes comments from JavaScript code using a non-greedy match:

```javascript

const code = "console.log('Hello // world');";

const pattern = /\/\/.*|\/*[^]**\//g;

console.log(code.replace(pattern, "")) // "console.log('Hello ');"

```

By integrating these practical applications into development workflows, JavaScript developers can significantly enhance their text processing capabilities.

