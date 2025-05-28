---

title: Symbol.matchAll: JavaScript's Iterable Regular Expression Matching

date: 2025-05-27

---


# Symbol.matchAll: JavaScript's Iterable Regular Expression Matching

JavaScript's String.prototype.matchAll method revolutionizes regular expression processing by returning an iterator of all matches, including capturing groups. This powerful feature enables sophisticated text analysis and manipulation, particularly when handling complex patterns and multiple occurrences. We'll explore how to use matchAll effectively, its behavior when working with different regex flags, and how custom matchers can extend its capabilities through Symbol.matchAll.


## Introduction to matchAll

matchAll enables detailed string processing through regular expressions by returning an iterator of all matches, including capturing groups. This functionality supports sophisticated text analysis and manipulation, particularly when handling complex patterns and multiple occurrences.

The method requires a regular expression object with the /g flag for global searching, otherwise a TypeError is thrown. Each iterator item contains the matched text, index position, and input string, with capturing groups represented as an object of named groups or indices.

matchAll demonstrates the flexibility of JavaScript's string matching capabilities by allowing custom implementation through Symbol.matchAll. While the Symbol.matchAll property exists on the RegExp prototype, custom matchers must be implemented within objects, as direct use of RegExp.matchAll() results in a TypeError.

The method excels in complex pattern matching and text processing tasks, as shown in examples where it successfully extracts structured data from strings containing multiple elements separated by varied delimiters. It supports both simple and sophisticated patterns, including those with multiple capturing groups and varied elements.


## matchAll Syntax and Usage

matchAll requires a regular expression object with the /g flag for global searching. Without this flag, a TypeError is thrown. The method returns an iterator containing match objects that include capturing groups and match indices.

Each match object in the iterator follows this structure:

- match[0]: The matched text

- match.index: The index position where the match was found

- match.input: A copy of the search string

- match.groups: An object containing named capturing groups with their respective matches

The method supports multiple return values, allowing developers to process all matches in a single operation. For example:

```javascript

const sentence = "The quick brown fox jumps over the lazy dog";

const regex = /\b\w{4}\b/g;

const matches = [...sentence.matchAll(regex)];

console.log(matches);

// Output: [

//   Array ["quick", index: 4, input: "The quick brown fox jumps over the lazy dog", groups: undefined],

//   Array ["brown", index: 10, input: "The quick brown fox jumps over the lazy dog", groups: undefined],

//   Array ["lazy", index: 39, input: "The quick brown fox jumps over the lazy dog", groups: undefined]

// ]

```

The method also handles complex patterns effectively. For instance, when dealing with text containing both commas and semicolons as delimiters:

```javascript

const bio = "His name is Albert and albert likes to code.";

const regex = /albert/gi;

const result = bio.matchAll(regex);

console.log(Array.from(result));

// Output: [

//   Array ["Albert", index: 13, input: "His name is Albert and albert likes to code.", groups: undefined],

//   Array ["albert", index: 24, input: "His name is Albert and albert likes to code.", groups: undefined]

// ]

```

The matchAll method can process both case-sensitive and case-insensitive patterns efficiently. The /i flag enables case-insensitive matching, as demonstrated in this example:

```javascript

const sentence = "I am learning JavaScript not Java.";

const regex = /Java[a-z]*/gi;

const result = sentence.matchAll(regex);

console.log(Array.from(result));

// Output: [

//   Array ["JavaScript", index: 14, input: "I am learning JavaScript not Java.", groups: undefined],

//   Array ["Java", index: 29, input: "I am learning JavaScript not Java.", groups: undefined]

// ]

```


## matchAll Features and Behavior

The matchAll method returns an iterator of all matches, including capturing groups, for a given regular expression. This functionality is particularly useful for complex pattern matching requirements in text processing. Each match is represented as an array with the matched text, index position, input string, and capturing groups.

The method handles multiple return values efficiently, allowing developers to process all matches in a single operation. For example, when matching words of exactly four characters, the method successfully extracts them from the input string and returns their positions:

```javascript

const sentence = "The quick brown fox jumps over the lazy dog";

const regex = /\b\w{4}\b/g;

const matches = [...sentence.matchAll(regex)];

console.log(matches);

```

This results in an array of match objects, each containing the matched text, index position, input string, and capturing groups:

```javascript

[

  Array ["quick", index: 4, input: "The quick brown fox jumps over the lazy dog", groups: undefined],

  Array ["brown", index: 10, input: "The quick brown fox jumps over the lazy dog", groups: undefined],

  Array ["lazy", index: 39, input: "The quick brown fox jumps over the lazy dog", groups: undefined]

]

```

When dealing with complex patterns, matchAll demonstrates its effectiveness. For instance, it successfully extracts structured data from strings containing multiple elements separated by various delimiters:

```javascript

const bio = "His name is Albert and albert likes to code.";

const regex = /albert/gi;

const result = bio.matchAll(regex);

console.log(Array.from(result));

```

The output shows both case-sensitive and case-insensitive matching capabilities:

```javascript

[

  Array ["Albert", index: 13, input: "His name is Albert and albert likes to code.", groups: undefined],

  Array ["albert", index: 24, input: "His name is Albert and albert likes to code.", groups: undefined]

]

```

The method also handles capturing groups effectively. When used with a pattern that includes multiple capturing groups and varied elements:

```javascript

const sentence = "I am learning JavaScript not Java.";

const regex = /Java[a-z]*/gi;

const result = sentence.matchAll(regex);

console.log(Array.from(result));

```

The output demonstrates the detailed information provided for each match:

```javascript

[

  Array ["JavaScript", index: 14, input: "I am learning JavaScript not Java.", groups: undefined],

  Array ["Java", index: 29, input: "I am learning JavaScript not Java.", groups: undefined]

]

```

The matchAll method supports both simple and sophisticated patterns, including those with multiple capturing groups and varied elements. This functionality is particularly useful for complex text processing tasks, as demonstrated by its ability to handle intricate patterns effectively.


## matchAll and Symbol.matchAll

matchAll relies on the Symbol.matchAll property to define its behavior. This property represents the well-known symbol @@matchAll, which is used by String.prototype.matchAll to look up the appropriate method for matching against a string.

The Symbol.matchAll static data property has the following attributes:

- Writable: false

- Enumerable: false

- Configurable: false

This implementation pattern allows for customizing string matching behavior through subclasses. For example:

```javascript

const integers = {

  *[Symbol.matchAll](str) {

    for (const m of str.matchAll(/\d+/g)) {

      yield parseInt(m[0], 10);

    }

  }

};

console.log(Array.from("42ab17, 2x".matchAll(integers)))

```

The Symbol.matchAll method operates similarly to String.prototype.matchAll, with some key differences:

1. It uses [Symbol.species] to construct a new regex, avoiding mutation of the original.

2. lastIndex starts with the original regex's value.

3. It validates global regexes in String.prototype.matchAll, while the method itself does not validate input regexes.

4. For non-global regexes, it yields the exec result once and returns undefined.

5. For global regexes, each next call calls exec and yields the result.

6. Sticky behavior applies only to global regexes, matching only beyond lastIndex.

7. Empty string matches advance lastIndex by one Unicode code point (one UTF-16 code point for Unicode flags).

As of January 2020, the method is widely implemented across browsers and devices. The following code demonstrates its usage and behavior:

```javascript

const re = /\d+/g;

const str = "2016-01-02|2019-03-07";

const result = re[Symbol.matchAll](str);

console.log(Array.from(result, (x) => x[0])); // ["2016", "01", "02", "2019", "03", "07"]

```

The implementation has been stable enough to be referenced in the ECMAScript 2026 Language Specification, with documented behavior across multiple web browsers and JavaScript environments.


## matchAll Best Practices

The matchAll method requires regular expressions with the /g flag for global searching; otherwise, it throws a TypeError. This flag enables efficient processing of multiple occurrences within a string. The method returns an iterator containing matches including capturing groups, with each item possessing the additional properties groups, index, and input.

To work effectively with matchAll, developers should:

- Always include the /g flag when performing global searches

- Use the iterator returned by matchAll with for...of loops, array spreading, or Array.from() constructs for efficient processing

- Handle potential TypeError exceptions when using non-global regular expressions

Developers can implement custom matchers through Symbol.matchAll on RegExp prototypes, allowing for specific behavior customization while maintaining compatibility across JavaScript environments. This approach enables robust text processing capabilities while providing clear feedback on matching failures.

