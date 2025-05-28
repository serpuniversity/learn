---

title: JavaScript String replace Method

date: 2025-05-27

---


# JavaScript String replace Method

JavaScript's `replace()` method stands as a versatile workhorse for string manipulation tasks, offering developers a powerful way to transform text data with precision and efficiency. Whether you're updating log entries, sanitizing user input, or dynamically modifying HTML content, this method provides the flexibility needed to handle a wide range of text processing challenges. From basic substring replacements to sophisticated regular expression operations, `replace()` delivers a robust solution for cleaning, transforming, and updating text-based data across modern web applications.


## Basic Usage of replace()

The `replace()` method in JavaScript addresses basic substring replacement scenarios effectively. It requires two parameters: the value or regular expression to search for (`pattern`), and the new value to replace it with (`replacement`).

By default, the method replaces only the first occurrence of the pattern specified. For example:

```javascript

let original = "Hello World";

let modified = original.replace("World", "Universe");

console.log(modified); // Output: "Hello Universe"

```

For global replacements across all occurrences of the pattern, the global flag (`g`) must be used within the regular expression:

```javascript

let text = "Repeat, repeat, and repeat again";

let newPhrase = text.replace(/repeat/gi, "do");

console.log(newPhrase); // Output: "Do, do, and do again"

```

The replacement value can be a simple string or a function. When a function is provided, it is called for each match, allowing for dynamic replacement logic based on the matched content:

```javascript

let phrase = "The quick brown fox jumps over the lazy dog";

let result = phrase.replace(/(\b\w{3}\b)/g, match => match.toUpperCase());

console.log(result); // Output: "The QUICk brown fox jumps over the LAZY dog"

```

This function-based replacement demonstrates the method's flexibility in handling both simple and complex string modifications.


## Advanced Pattern Matching

The `replace()` method supports sophisticated pattern matching through regular expressions, enabling developers to perform precise text substitutions. For global replacements across all matching instances, the method requires the global flag (`g`) in the regular expression. This flag is essential for operations that need to affect multiple occurrences, as demonstrated in the following example:

```javascript

let phrase = "Repeat, repeat, and repeat again";

let newPhrase = phrase.replace(/repeat/gi, "do");

console.log(newPhrase); // Output: "Do, do, and do again"

```

Case-insensitive matching can be achieved using the `i` flag, as shown in the example where "world" is replaced with "JavaScript" in both uppercase and lowercase occurrences:

```javascript

let text = "hello WORLD";

let updatedText = text.replace(/world/i, "JavaScript");

console.log(updatedText); // Output: "hello JavaScript"

```

When working with regular expressions, the method employs special match references within replacement functions. Capture groups are denoted using `$1`, `$2`, etc., while `$&` reinserts the entire matched text. This functionality allows for complex transformations based on the matched content.

The method's capability to accept regular expressions enables sophisticated pattern matching, as illustrated in the removal of non-digit characters from a string:

```javascript

const reg = /\D/g

const str = "Java323Scr995ip4894545t"

const newStr = str.replace(reg, "")

console.log(newStr) // Output: "Java323Scr995ip4894545t"

```

In this case, all non-digit characters are removed from the original string, leaving only the numeric values intact. The method's flexibility in handling both simple and complex patterns makes it a valuable tool for various text manipulation tasks.


## Function-based Replacements

The replace() method's functionality extends significantly when combined with functions as the replacement parameter. A function can be provided that takes three arguments: the matched string, the offset of the match, and the original string. This allows for dynamic replacement logic based on the matched content.

A notable example demonstrating this capability is the conversion of camelCase to dash-separated format. The regular expression /[A-Z]/g is used to match uppercase letters, with a function that converts these to lowercase and inserts a hyphen before the match location: `function styleHyphenFormat(propertyName) { function upperToHyphenLower(match, offset, string) { return (offset > 0 ? "-" : "") + match.toLowerCase(); } return propertyName.replace(/[A-Z]/g, upperToHyphenLower); }`.

The method's support for capturing groups further enhances its functionality. For instance, the expression `(\w+)\s(\w+)` uses capturing groups to construct the replacement string, as demonstrated in the transformation of "Maria Cruz" to "Cruz, Maria": `const str = "Maria Cruz"; const newStr = str.replace(/(\w+)\s(\w+)/, "$2, $1");`.

The method's flexibility extends to unit conversion, such as transforming Fahrenheit degrees to Celsius. The regular expression /F$/ checks for any number ending with "F", with the function receiving the number as the second parameter (p1). It calculates the Celsius equivalent based on the Fahrenheit value: `if input is "212F", the function returns "100C", and if the input is "0F", it returns "-17.77777777777778C"`.

To handle global replacements effectively, developers can leverage the method's support for regular expressions with the global flag (g) and case-insensitive flag (i). For instance, the pattern "Geeks" is replaced with "GFG" in a case-insensitive manner across the entire string: `let stringReplace = "Geeks for Geeks is a great platform to learn Javascript"; let result = stringReplace.replace(/Geeks/gi, "GFG");`.

Modern JavaScript versions have introduced additional capabilities. ES12 introduced the replaceAll() method, which provides a simpler way to replace all occurrences of a substring without the need for regular expressions. This method works efficiently for small to medium-sized strings, but for extensive text processing, developers are encouraged to consider alternative approaches for better performance.


## Special Match References

The replace() function supports several special $ references to achieve complex replacement patterns. The $& token inserts the entire matched substring, offering a straightforward way to incorporate the matched text into replacements:

```javascript

text.replace(regex, function(m){ return ''+m+'';});

```

The MDN documentation emphasizes that $& is particularly valuable under two circumstances:

1. When the regex pattern is static and cannot be modified

2. When capturing groups are unnecessary in the regular expression

The text also highlights that both $$ and $& enable capturing group functionality, but with different uses. While $$ inserts a literal "$" character, $& offers more flexibility by reinserting the full matched substring:

```javascript

text.replace(regex, function(m) { return '$&'; });

```

Special $ references enable dynamic replacements based on match positions. For instance, the function:

```javascript

function styleHyphenFormat(propertyName) {

  function upperToHyphenLower(match, offset, string) {

    return (offset > 0 ? "-" : "") + match.toLowerCase();

  }

  return propertyName.replace(/[A-Z]/g, upperToHyphenLower);

}

```

demonstrates capturing group usage effectively. This approach ensures proper matching and replacement logic:

```javascript

const newString = propertyName.replace(/[A-Z]/g, function(match, offset, str) {

  return (offset > 0 ? "-" : "") + match.toLowerCase();

});

```

The $1, $2, etc., notation captures individual groups, allowing for precise substring manipulations. For example:

```javascript

const str = "foo(bar)baz";

const newStr = str.replace(/\(([^)]+)\)/, "$1");

```

In this case, the $1 reference captures the group inside the parentheses, effectively extracting "bar" from "foo(bar)baz".

For scenarios where both capturing groups and full matches are needed, the $& token proves particularly useful. Consider the task of converting Fahrenheit temperatures to Celsius:

```javascript

const str = "212F";

const newStr = str.replace(/F$/, function(temp) {

  return (5/9) * (temp - 32) + "C";

});

```

Here, $& ensures the full temperature string (e.g., "212") is correctly passed to the replacement function for accurate conversion calculations.

The functionality's versatility extends to complex text transformations. For instance, the pattern `/(\w+)\s(\w+)/` uses capturing groups to construct the replacement string, successfully switching "Maria Cruz" to "Cruz, Maria":

```javascript

const str = "Maria Cruz";

const newStr = str.replace(/(\w+)\s(\w+)/, "$2, $1");

```

This approach demonstrates the $ references' power in managing sophisticated string manipulations while maintaining the flexibility required for dynamic replacement logic.


## Common Use Cases

The replace() method finds extensive application across various string manipulation tasks, particularly in scenarios requiring dynamic content modification and data sanitization.

Common use cases include:

- Updating specific entries in logs: By targeting specific user identifiers or event codes, developers can efficiently modify log entries. For example, updating user IDs in a server log: `let updatedLog = log.replace("user123", "user");`

- Modifying HTML content: The method streamlines the process of updating or replacing elements within HTML snippets. This simplifies content management and ensures consistency across templates: `let updatedSnippet = htmlSnippet.replace("Old Text", "New Text");`

- Dynamically updating inline CSS: Content management systems and dynamic styling solutions can leverage replace() to update color schemes or font styles based on user preferences or theme changes: `let updatedStyles = styles.replace("red", "blue");`

Data sanitization represents another critical application area, where the method helps protect against security vulnerabilities by removing potentially dangerous input:

- Sanitizing user input: By removing script tags and their contents, developers prevent cross-site scripting (XSS) attacks while maintaining the integrity of user-submitted data: `let sanitizedInput = userInput.replace("<script>", "").replace("</script>", "");`

- Updating text in files: Content management systems often require updating large documents across multiple files. replace() enables efficient local modification without overwriting original files: `let updatedDocument = document.replace("<http://oldsite.com>", "<http://newsite.com>");`

The method's flexibility extends to complex transformations, supporting everything from simple string replacements to advanced regular expression operations. This versatility makes it a fundamental tool for developers working with text-based data across various applications and platforms.

