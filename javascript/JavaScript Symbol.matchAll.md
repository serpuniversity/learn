---

title: JavaScript matchAll: The Full Guide

date: 2025-05-26

---


# JavaScript matchAll: The Full Guide

JavaScript's matchAll method revolutionizes string pattern matching with its powerful iterator-based approach. Unlike traditional match methods, matchAll returns an iterator of all regex matches, offering unprecedented control over pattern recognition. This comprehensive guide explores matchAll's fundamentals, including its syntax, capabilities, and behavior with capturing groups. We'll also compare it to the standard match method, highlighting key differences in iterator stability, error handling, and performance. Whether you're extracting data from complex strings or implementing custom matching logic, this guide provides the insights you need to master JavaScript's most versatile string matching tool.


## matchAll Fundamentals

The matchAll() method returns an iterator of all matches found by applying a regular expression to a string. The method requires the global flag to be specified, either as part of the regular expression literal or via the `RegExp` constructor.

The syntax for using matchAll() with a string is `str.matchAll(/your-regex/g)`. When using matchAll() with a RegExp object, you can choose to convert the iterator to an array using methods such as Array.from(), a for...of loop, or the spread operator.

For example, calling `matchAll('p5*js is easier than abc123', '[a-z][0-9]')` would return `[['p5'], ['c1']]`. If no matches are found, an empty array is returned (`[]`).

The method works with regular expressions containing no capturing groups, as well as patterns with one, two, or three capturing groups. It also handles named capturing groups and supports the following flags:

- `g`: Enables searching for all matches

- `i`: Enables case-insensitive matching

- `m`: Enables multiline mode

- `s`: Enables dotall mode (allows `.` to match newline characters)

- `u`: Enables full Unicode matching

- `y`: Enables "sticky" mode, starting matches from the current position in the target string

When used with RegExp objects, matchAll() returns an iterator that can be converted to an array using the same methods. In Node.js, Deno, or Firefox environments, you can use `const matchAll = require('string.prototype.matchall')` to access the matchAll functionality.

The method syntax is matchAll(str, regexp), and it returns matches found as a String[]. It's important to note that matchAll() uses the global flag, even when using the g flag, to prevent TypeError exceptions.


## matchAll Behavior with Regular Expressions

matchAll() creates a stable iterator that allows multiple passes over the match results and maintains the original regex's lastIndex property. This iterator contains the following properties for each match:

- day: the matched pattern

- index: the index position where the matched pattern began

- input: the string on which matchAll() was invoked

- groups: a collection of named capturing groups specified in the RegExp argument, or undefined if no named capturing groups are present

When matching patterns with capturing groups, the iterator returns arrays where the first element is the matched pattern, followed by capture group values. For example:

```javascript

const string = "Tuesday";

const regExp = /day/g;

let result = string.matchAll(regExp);

console.log(result.next().value); // ['day']

console.log(result.next().value); // undefined

```

The iterator can be converted to an array using Array.from(), a for...of loop, or the spread operator. Here's an example demonstrating conversion to an array:

```javascript

const string = "SunDay, Tuesday, and Friday are good DAYS";

const regExp = /(\w+)d(a)y/g;

const result = [...string.matchAll(regExp)];

console.log(result);

// Output: [

//   ['SunDay', 'Sun', 'a', index: 0, input: 'SunDay, Tuesday, and Friday are good DAYS', groups: undefined],

//   ['Tuesday', 'Tues', 'a', index: 8, input: 'SunDay, Tuesday, and Friday are good DAYS', groups: undefined],

//   ['Friday', 'Fri', 'a', index: 21, input: 'SunDay, Tuesday, and Friday are good DAYS', groups: undefined]

// ]

```

Implementations create a clone of the regular expression to prevent lastIndex changes during scanning, ensuring the original regex's properties remain unchanged. This stability allows developers to iterate over matches multiple times without modifying the original pattern's state.


## matchAll in Practice

The matchAll method enables developers to extract data from strings based on regular expressions effectively. For instance, to extract all weekday names from a string containing days of the week, you can use `matchAll("SunDay, Tuesday, and Friday are good DAYS", /(\w+)d(a)y/g)`. This results in an iterator that yields multiple matches: `[['Tuesday', 'Tues', 'a', index: 8, input: 'SunDay, Tuesday, and Friday are good DAYS', groups: undefined], ['Friday', 'Fri', 'a', index: 21, input: 'SunDay, Tuesday, and Friday are good DAYS', groups: undefined]]`.

For handling complex patterns with multiple occurrences, matchAll demonstrates its utility. The example `matchAll('p5*js is easier than abc123', '[a-z][0-9]')` showcases its ability to match multiple patterns efficiently, returning `[['p5'], ['c1']]`.

When working with capturing groups, matchAll maintains stability across iterations through the iterator's clone mechanism. This robust approach allows developers to process matches multiple times without affecting the original regular expression's state. For example, the pattern `matchAll(/day/g)` correctly returns `[['day']]`, demonstrating its consistent behavior with the global flag.


## matchAll vs match

The matchAll() method presents several key differences when compared to the standard match() method, particularly in how they handle iterators, capturing groups, and iterator stability.

While match() returns an array containing all matches, including capturing groups, matchAll() returns an iterator of results. However, both methods support regular expressions with the global flag (g), allowing for searching all occurrences in the string.


### Capturing Group Support

The most significant differentiation between match() and matchAll() is their handling of capturing groups. As noted in the MDN Web Docs, matchAll() provides better access to capture groups than String.prototype.match(). This enhanced capability allows developers to extract both the matched pattern and its constituent parts in a single operation.

For example, when matching patterns with capturing groups, matchAll() returns arrays where the first element is the matched pattern, followed by capture group values. In contrast, match() would return only the matched pattern without capturing group information.


### Iterator Behavior

Another critical distinction is their approach to iterator behavior. As documented in the Symbols Are Your Friend series, matchAll() creates a stable iterator that maintains the original regex's lastIndex property across iterations. This stability is crucial for developers who need to process matches multiple times without affecting the original pattern's state.

In comparison, match() methods can alter the lastIndex property during matching operations, which may impact subsequent calls to match() on the same string. This difference makes matchAll() more suitable for scenarios requiring repeated pattern matching operations on the same string.


### Implementation Details

Both methods utilize different strategies for handling complex patterns. matchAll() creates a clone of the regular expression to prevent lastIndex changes during scanning, while match() directly modifies the original regex object. This distinction affects how developers can reuse regular expressions in multiple matching operations.


### Error Handling

A notable difference appears in their error handling behavior. When using matchAll() with a RegExp object lacking the g flag, a TypeError is thrown. In contrast, match() can be called without the g flag and may succeed depending on the pattern and string content.

In summary, while match() remains valuable for basic pattern matching operations, matchAll() offers distinct advantages in handling complex patterns, capturing groups, iterator stability, and error handling. This makes matchAll() particularly well-suited for advanced text processing tasks requiring detailed pattern matching capabilities.


## Custom matchAll Implementations

The matchAll method's flexibility extends beyond its standard implementation through custom Symbol.matchAll methods. This approach enables developers to define tailored matching behavior for their regular expressions, providing maximum control over pattern matching operations.


### Customizable Matcher Implementation

Developers can implement custom matchers by defining a Symbol.matchAll method on their regular expression objects. This method acts as a hook for matching behavior, allowing arbitrary objects to serve as matchers for strings. For example:

```javascript

const integers = {

  [Symbol.matchAll](str) {

    // Custom matching logic here

  }

}

```

This mechanism follows a protocol similar to JavaScript's iterable and thenable protocols, enabling flexible integration with string matching operations.


### Regex Subclass Customization

Regular expression subclasses can override the Symbol.matchAll method to modify their behavior. For instance, a custom subclass might return an array instead of an iterator, providing a different interface for match results. Implementations maintain the original regex's properties through cloning mechanisms, ensuring stability across multiple matching operations.


### Advanced Matching Control

Custom implementations can extend beyond simple pattern matching, offering sophisticated control over matching behavior. Developers can implement logic to track match locations, limit match frequency, or apply conditional matching criteria. This level of customization allows for precise text analysis and manipulation, particularly in applications requiring complex pattern recognition.


### Iterator Stability and Performance

Developers must consider iterator stability when implementing custom matchAll methods. The standard implementation creates a clone of the regular expression to prevent lastIndex changes during scanning. Custom implementations should maintain similar stability to ensure consistent results across multiple iterations.


### Example Implementation

To demonstrate a custom implementation, consider a scenario where you want to limit matches to specific character positions. You can implement custom behavior like this:

```javascript

class PositionalMatcher extends RegExp {

  [Symbol.matchAll](str) {

    const matches = super.exec(str);

    if (matches && matches.index % 2 === 0) {

      yield matches;

    }

  }

}

```

This example demonstrates how custom implementations can filter matches based on additional criteria, extending the basic matchAll functionality.

In conclusion, custom matchAll implementations provide developers with powerful tools for extending regular expression matching capabilities. By leveraging Symbol.matchAll and implementing tailored matching logic, developers can create highly specialized text processing solutions.

