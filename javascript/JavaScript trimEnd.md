---

title: JavaScript String trimEnd() Method

date: 2025-05-27

---


# JavaScript String trimEnd() Method

JavaScript's `trimEnd()` method, introduced in ECMAScript 2019, provides a powerful tool for string sanitization by removing whitespace characters from a string's end. This native method serves as a modern alternative to the non-standard `trimRight()`, offering developers a reliable way to preprocess text data before further processing or display. Through regular expression matching, `trimEnd()` efficiently cleans strings while preserving their original content, making it an essential utility for any JavaScript developer working with user input or external data sources.


## Overview of trimEnd() Method

The JavaScript String `trimEnd()` method removes all whitespace characters (including spaces, tabs, and line breaks) from the end of a string, returning a new string with the whitespace removed. It is available as of ECMAScript 2019 and serves as an alias for the non-standard `trimRight()` method, performing identical functionality.


### Method Syntax and Parameters

The `trimEnd()` method follows the syntax `string.trimEnd()`, accepting no parameters. It returns a new string with trailing whitespace removed while leaving the original string unchanged. This behavior mirrors the `trim()` method but operates specifically on the end portion of the string.


### Implementation Details

From a technical perspective, `trimEnd()` functions through regular expression matching of whitespace characters at the end of the string. The method processes these characters and returns a new string without modifying the original. This allows developers to sanitize string inputs effectively while maintaining source data integrity.


### Browser Compatibility

All major browsers—including Google Chrome, Firefox, Edge, Safari, and Opera—fully support the `trimEnd()` method as of January 2020. The implementation consistently removes whitespace characters plus line terminators from the end of the string, providing reliable cross-browser functionality for string sanitization tasks.


## Removing Trailing Whitespace

The trimEnd() method removes all whitespace characters from the end of a string, including space characters, tabs, carriage returns, and line breaks. This operation returns a new string while leaving the original string unchanged.

The method's behavior can be illustrated through several examples. For instance, applying trimEnd() to the string " Dev Newbs! " yields " Dev Newbs!"—the whitespace character at the end is removed. Similarly, the method processes strings containing multiple types of whitespace, such as " Hello\nWorld \t", returning " Hello\nWorld" with all trailing whitespace characters eliminated.

The implementation works by matching whitespace characters at the end of the string using regular expressions. This approach ensures consistent removal of specified whitespace characters while preserving the original string content. As with the analogous trim() method, trimEnd() returns a new string representing the original input with trailing whitespace removed, allowing developers to safely sanitize string inputs without altering the source data.


## Method Syntax and Parameters

The `trimEnd()` method functions as a string manipulation tool that specifically removes whitespace characters from the end of a string. These whitespace characters include space characters, tabs, carriage returns, new lines, form feeds, vertical tabs, and any other Unicode whitespace characters. The method operates by matching these characters at the end of the string through regular expressions and producing a new string with the whitespace removed.

The syntax for invoking `trimEnd()` is straightforward: `string.trimEnd()`, which requires no parameters. The method returns a new string with the trailing whitespace removed while preserving the original string's content. This behavior makes it particularly useful for data sanitization tasks, especially when processing user inputs or external data sources where trailing whitespace might be present unintentionally.

To demonstrate its functionality, consider the following examples:

```javascript

let str1 = " GeeksforGeeks ";

let str2 = " Hello There! ";

console.log(str1.trimEnd()); // Output: "GeeksforGeeks"

console.log(str2.trimEnd()); // Output: "Hello There!"

```

The method is designed to maintain high compatibility across modern JavaScript environments, including all major browsers (Google Chrome, Firefox, Edge, Safari, and Opera) and supporting devices as of January 2020. This widespread implementation ensures reliable functionality for developers implementing string sanitization in their applications.


## Equivalent Methods

The `trimEnd()` method serves as an alias for the non-standard `trimRight()` method, performing the identical function of removing whitespace from the end of a string. Both methods operate consistently across major JavaScript environments.


### Technical Implementation

The method employs regular expressions to match and remove whitespace characters at the end of the string. This technical approach ensures reliable functionality across different browser implementations. The method's behavior remains consistent with the `trim()` method, specifically targeting trailing whitespace while leaving the original string unchanged.


### Name Consistency

When the `trimEnd()` method was standardized, its name was chosen to align with the `padEnd()` method's naming convention. For web compatibility reasons, the `trimRight()` alias remains active, referring to the exact same function object. This dual-naming system maintains consistency while ensuring broad compatibility with existing JavaScript implementations.


## Usage Examples

The `trimEnd()` method returns a new string with whitespace removed from the end of the original string. This includes spaces, tabs, carriage returns, new lines, form feeds, vertical tabs, and any other Unicode whitespace characters.


### Basic Usage

The method can be called on any string value. If the string contains only whitespace, it returns an empty string. When applied to `null` or `undefined`, it throws a `TypeError`.


### Example Scenarios

```javascript

let str1 = " GeeksforGeeks ";

let str2 = " Hello There! ";

console.log(str1.trimEnd()); // Output: "GeeksforGeeks"

console.log(str2.trimEnd()); // Output: "Hello There!"

console.log("".trimEnd()); // Output: ""

console.log(null.trimEnd()); // Throws TypeError

console.log(undefined.trimEnd()); // Throws TypeError

```


### Integration with Other String Methods

The method works well in combination with other string manipulation methods. For example, using `trimEnd()` before `toUpperCase()` ensures that the string is properly trimmed before case conversion.

```javascript

let str = " TypeScript is great! ";

console.log(str.trimEnd().toUpperCase()); // Output: TYPESCRIPT IS GREAT!

```


### Length Comparison

When comparing the lengths of the original and trimmed strings, the trimmed version has fewer characters unless no whitespace was present at the end.

```javascript

let str = " GeeksforGeeks ";

console.log(str.length); // Output: 19

str = str.trimEnd();

console.log(str.length); // Output: 16

console.log(str); // Output: "GeeksforGeeks"

```


### Regular Expression Alternative

For advanced users, `trimEnd()` can also be implemented using regular expressions.

```javascript

let stringWithNumbers = "12345 ";

console.log(stringWithNumbers.replace(/\d+$/,'')); // Output: "12345"

```

