---

title: JavaScript String matchAll() - Match All Occurrences

date: 2025-05-26

---


# JavaScript String matchAll() - Match All Occurrences

JavaScript's String methods offer powerful tools for text processing, and one of the most versatile is the matchAll() function. While similar to the match() method, matchAll() provides unique capabilities for working with regular expressions, particularly when dealing with multiple occurrences and capturing groups. In this article, we'll explore the fundamentals of matchAll(), examining how it processes strings, handles capturing groups, and returns match results. We'll also look at common use cases and best practices for using this powerful text-matching tool.


## matchAll() Function Basics

matchAll() requires the regular expression to have the global flag "g" and returns an iterator that cannot be restarted. The method returns an iterator object containing all matches of the regular expression in the string.

The iterator's value property consists of an array for each match, which contains the matched text as the first value, followed by captured groups (if any), and an object with additional properties including index (match position), input (original string), and input property (string used for matching).

Each match array follows the pattern:

[matched string, capture group 1, capture group 2, ..., {index: match position, input: original string, length: match length}]

The method works with both capturing and non-capturing groups. When capturing groups are present, the match array includes the captured groups in addition to the matched string. The iterator can be converted to an array using methods such as `Array.from()`, for...of loops, or the spread operator.

Some key characteristics of matchAll():

- The method creates a new iterator on each call

- It doesn't modify the lastIndex property of the RegExp

- Case-insensitive matching can be performed with the "i" flag

- The method works with both global and non-global regular expressions

- It supports extended regular expression syntax (e.g., capturing groups, flags)


## matchAll() Parameters and Behavior

matchAll() requires a regular expression with the global flag 'g' and returns an iterator that can be converted to an array of match results. The method works differently from match() in several key ways: it returns an iterator object instead of an array, requires the global flag for functionality, and performs better with capturing groups.

When called with a global flag, matchAll() returns an iterator object containing all matches, while without the global flag, it matches only the first occurrence and returns an array containing the match result. The method works with both string literals and variables. Each match array contains the matched string, capturing group patterns if present, the index position where the match began, the input string, and named capturing group values if specified.

The returned iterator object contains several properties for each match: the matched pattern, the index position where the match began, information about the input string, and a groups property that contains a collection of named capturing groups or undefined if no named groups are present. This property provides better access to capturing groups compared to the match() method when using the global flag.

The method supports patterns containing one, two, three capturing groups, and named capturing groups. The returned iterator can be used to match patterns with or without capturing groups, including those with two, three capturing groups, and two named capturing groups. The method requires the use of the g flag with its RegExp argument to prevent TypeError exceptions and internally creates a clone of the RegExp object to prevent lastIndex property changes during string scanning.


## Working with Match Results

Each match result from matchAll() consists of an array containing the matched text as the first value, followed by capturing group patterns (if present), and an object with additional properties including index, input, and groups. This structure allows for detailed access to matching text and captured groups throughout a string.

The matched patterns are returned as arrays, rather than plain strings, and the method supports both named and unnamed capturing groups. When used with named capturing groups, the returned match objects contain a groups property with collections of these named groups. If no named groups are present, this property returns undefined.

The method supports various patterns, including those with one, two, three capturing groups, and named capturing groups. For example, when matching the pattern "rain in Spain" across multiple occurrences in a text, the method returns an array of matches, each containing the captured group "ain" and the index position where the match began.

When iterating over matches using for...of loops or the spread operator, developers can access all match properties, including the matched pattern, index position, input string, and groups object. This structure provides a comprehensive way to handle complex pattern matching tasks while maintaining compatibility with both named and unnamed capturing groups.


## Common Use Cases

matchAll() is a robust tool for text analysis and manipulation, particularly when working with complex patterns and multiple occurrences in a string. The method returns an iterable object that can be converted to an array using various methods, including spread syntax, for...of loops, or Array.from(), providing flexibility in how matches are processed.

The function's syntax is str.matchAll(regexp), where str is the string being searched and regexp is a regular expression object requiring the global flag 'g' for proper functionality. The method works with both string literals and variables, offering efficient text searching operations compared to alternative methods.

matchAll() returns an iterator object containing the following properties for each match:

- Day: The matched pattern

- index: The 0-based index position where the matched pattern began

- input: Indicates the string on which matchAll() was invoked

- groups: Contains a collection of named capturing groups specified in the RegExp argument, or undefined if the regular expression does not contain any named capturing groups

This rich output structure provides detailed information about each match while maintaining compatibility with both named and unnamed capturing groups. For example, when matching the pattern "rain in Spain" across multiple occurrences in a text, matchAll() returns an array of matches, each containing the captured group "ain" and the index position where the match began.

Developers can use matchAll() in three primary ways: assigning to a variable, converting to an array with spread syntax, or executing multiple times. This flexibility enables efficient text searching operations and powerful string manipulation capabilities, making matchAll() an indispensable tool for JavaScript developers working with regular expressions.

