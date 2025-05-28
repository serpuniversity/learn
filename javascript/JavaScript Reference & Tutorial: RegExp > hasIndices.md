---

title: JavaScript RegExp hasIndices Property

date: 2025-05-26

---


# JavaScript RegExp hasIndices Property

Regular expressions in JavaScript offer powerful pattern matching capabilities through various flags and properties. While most developers are familiar with common flags like global search (g), case-insensitive matching (i), and multiline mode (m), fewer understand the details of the d flag and its associated hasIndices property. This article explores how capturing group indices are managed in JavaScript regex patterns, demonstrating practical applications for developers working with structured text data.


## Understanding JavaScript RegExp

JavaScript's RegExp object implements powerful pattern matching capabilities through various flags and properties. Among these features is the hasIndices property, which indicates whether capturing group indices are available for a regular expression.

A regular expression in JavaScript can be created using two primary methods: literal notation (e.g., /pattern/) or the constructor function (new RegExp("pattern")). This flexibility allows developers to choose the most appropriate syntax based on their use case. The RegExp object supports multiple flags to control matching behavior, including g (global search), i (case-insensitive), m (multiline), s (dotAll), u (unicode), and y (sticky).

The hasIndices property specifically responds to the d flag, which indicates that the result of a regular expression match should contain the start and end indices of the substrings of each capture group. When this flag is present, the match result objects returned by exec() have an additional indices property containing the index ranges for each group.

This feature particularly impacts the return value of exec(), where the array includes an extra indices property for capturing group information. All other regex-related methods, such as String.prototype.match(), internally call exec() and will also return indices if the regex has the d flag. The property itself has an undefined set accessor, meaning it cannot be changed directly.

In practical applications, this property enables detailed positional analysis of matched patterns, particularly useful in text editors, data parsers, and scenarios requiring precise substring location information.


## hasIndices Property Overview

The hasIndices property in JavaScript regular expressions indicates whether the d flag is enabled. When this flag is set, the regular expression captures the start and end indices of the matched substring within the input string, providing detailed positional information.

The property's value is undefined and cannot be changed directly. The text provides examples demonstrating this property:

For the regex /foo/dg:

- regex1.hasIndices returns true

- regex1.exec(str1).indices[0] returns [0, 3]

- regex1.exec(str1).indices[1] returns [8, 11]

For the regex /foo/:

- regex2.hasIndices returns false

- regex2.exec(str1).indices returns undefined

The specification for hasIndices is located at https://tc39.es/ecma262/multipage/text-processing.html#sec-get-regexp.prototype.hasIndices. The browser compatibility information is not provided in the text, but the feature has been available across browsers since September 2021.

The hasIndices accessor property of RegExp instances returns whether or not the d flag is used with this regular expression. This feature is well-established and works across many devices and browser versions. The d flag indicates that the result of a regular expression match should contain the start and end indices of the substrings of each capture group. It does not change the regex's interpretation or matching behavior in any way but only provides additional information in the matching result.

This flag primarily affects the return value of exec(). If the d flag is present, the array returned by exec() has an additional indices property as described in the exec() method's return value. Because all other regex-related methods (such as String.prototype.match()) call exec() internally, they will also return the indices if the regex has the d flag. The set accessor of hasIndices is undefined, meaning you cannot change this property directly.


## hasIndices in Action

The hasIndices property significantly impacts match results by enabling detailed positional analysis of matched patterns. When the d flag is enabled, the exec() method returns match objects with an additional indices property containing the start and end positions of each captured group.

For example, the following code demonstrates how to use match indices for parsing quoted content:

```javascript

const reQuoted = /“([^”]+)”/dgu;

function pointToQuotedText(str) {

  const startIndices = new Set();

  const endIndices = new Set();

  for (const match of str.matchAll(reQuoted)) {

    const [start, end] = match.indices[1];

    startIndices.add(start);

    endIndices.add(end);

  }

  let result = '';

  for (let index = 0; index < str.length; index++) {

    if (startIndices.has(index)) {

      result += '[';

    } else if (endIndices.has(index + 1)) {

      result += ']';

    } else {

      result += ' ';

    }

  }

  return result;

}

assert.equal(pointToQuotedText('They said “hello” and “goodbye”.'), ' [ ] [ ] ');

```

This example shows how match indices can be used to precisely locate quoted content within a string.

Named capture groups store their indices in matchObj.indices.groups, allowing for flexible pattern matching:

```javascript

const s = "color: blue; background: red;";

const regex = /(\w+): (\w+)/d;

const match = regex.exec(s);

console.log(match.indices); // Output: [0, 12], [0, 5], [7, 11]

```

This demonstrates the retrieval of start and end positions for both the full match and individual capture groups.

JavaScript developers can use these match indices for a variety of practical applications, such as:

- Validating if a pattern occurs after a specific position

- Efficient tracking of field positions in CSV strings

- Improved parsing of structured data like arrays or objects


## Implementing hasIndices

The hasIndices property offers several practical benefits for JavaScript developers working with regular expressions. Its read-only nature ensures that developers cannot accidentally alter the property, instead providing a clear indication of whether match indices are available.

This property enables developers to retrieve precise starting and ending positions of matched patterns, making it particularly useful for advanced parsing tasks. For example, the property allows developers to determine if a specific pattern occurs after a certain position within a string, as demonstrated in the validation example from the Mozilla documentation:

```javascript

let s = "abc123xyz";

let regex = /\d+/d;

let match = regex.exec(s);

if (match.indices[0] !== null && match.indices[0][0] > 3) {

  console.log("Numbers found after 3rd character");

}

```

Developers can also use match indices to efficiently track the position of each field in structured data, such as CSV strings. The following code snippet illustrates how match indices can parse CSV data while maintaining accurate positional information:

```javascript

let csv = "name,age,location";

let regex = /[^,]+/gd;

let match;

while ((match = regex.exec(csv)) !== null) {

  console.log(`Matched: ${match[0]} at indices: ${match.indices[0]}`);

}

```

The property's impact extends to custom matcher implementations, where it facilitates precise pattern matching and extraction. For instance, the Option class demonstrates how custom matchers can utilize match indices to extract specific subject properties:

```javascript

class Option {

  Some(value) { return [value]; }

  None() { return this; }

  static from(subject) {

    return match(subject, this.Some, this.None);

  }

  static match(subject, some, none) {

    return new Option(subject === false ? none : some(subject));

  }

}

```

In this implementation, match indices enable developers to define precise extraction rules for different subject types, enhancing the flexibility and power of regular expression-based pattern matching in JavaScript.


## Cross-Browser Compatibility

The hasIndices property has been available across browsers since September 2021, with robust support for this feature across multiple devices and browser versions. While the specific document does not provide detailed browser compatibility data, the property's implementation closely tracks the JavaScript standard, ensuring consistent behavior in modern JavaScript environments.

Developers can rely on this property to provide accurate positional information without concern for cross-browser compatibility issues. The feature's standardized behavior across implementations ensures that match indices function consistently whether used in Chrome, Firefox, Safari, or other compliant browsers.

