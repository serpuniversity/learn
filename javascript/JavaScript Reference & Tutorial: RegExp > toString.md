---

title: JavaScript RegExp: toString Method

date: 2025-05-26

---


# JavaScript RegExp: toString Method

In JavaScript, regular expressions are a powerful tool for pattern matching in strings. The `RegExp.toString()` method provides a way to get a string representation of these regular expressions, which can be useful for debugging, logging, or reconstructing the expression. This article examines the `toString()` method's capabilities, including how it handles different regex patterns and flags, and its compatibility across modern browsers. We'll also look at how it deals with special cases like empty expressions and line terminators in the pattern.


## Overview of RegExp.toString

The `toString()` method returns a string representation of a regular expression in the form of a regular-expression literal, which includes the regex's pattern and flags. This method is available in all modern browsers: Chrome, Edge, Firefox, Safari, and Opera.

When called, this method creates RegExp literal notation that includes trailing forward slashes and optionally follows with the `flags` property: `/source/flags`. For example, creating a regular expression with the pattern "foo" and the "i" flag using `new RegExp("foo", "i").toString()` produces "/foo/i".

The method returns a string representation of the regular expression, which can be useful for debugging or logging purposes. It works by accessing the `source` property to determine the string value and ensuring that line terminators such as `\n` are properly escaped. The return value is always in the form `/source/flags`, providing a human-readable format of the regular expression's pattern and flags.

This method has no parameters and is widely available across browsers since July 2015. It returns the string representation of the regular expression, which includes both the pattern and the flags, allowing for easy inspection and manipulation of the regex object's properties.


## Syntax and Usage

The `toString()` method returns the string value of the regular expression, including both the pattern and flags. It is defined in ECMAScript 1 (JavaScript 1997) and is supported in all modern browsers.

The method works by accessing the `source` property to determine the string value and ensures that line terminators such as `\n` are properly escaped. An empty regular expression returns the string "/(?:)/", and flags are included after the source pattern, enclosed in forward slashes. This ensures that the returned value is always a valid regex literal, though in some cases, the order of flags may differ from their original specification.

The method has no parameters and returns a string containing both the regular expression's pattern and flags. This makes it particularly useful for debugging and logging purposes, as it provides a human-readable representation of the regex object's properties. For example:

```javascript

let regex = /^[A-Za-z0-9]+$/;

console.log(regex.toString()); // Output: /^[A-Za-z0-9]+$/

```

This output clearly shows the intended regex pattern and its properties, making it easier to confirm that the regex object has been correctly configured.


## Returned Value

The toString() method returns a string representation of the regular expression's value, including both its pattern and flags. For non-empty expressions, this results in a string of the form /source/flags. When applied to an empty expression, the output is the string "/(?:)/".

Key points about the returned value:

- For the pattern "a+b+c", it returns /a+b+c/

- Empty regular expressions produce /(?:)/ (object type: string)

- The method's output indicates whether the regular expression has flags, with non-empty flags appearing after the source pattern

- In cases where line terminators like \n are present in the pattern, they are escaped in the returned string representation

- The returned value always includes the forward slashes that delimit the regular expression's pattern

- The order of flags in the returned string may differ from their original specification

- The resulting string is optimized for parsing, making it suitable for reconstructing the regular expression as needed


## Examples

The `toString()` method returns the string representation of a regular expression in the form of a regular-expression literal, which includes the regex's pattern and flags. For non-empty expressions, this results in a string of the form /source/flags. When applied to an empty expression, the output is the string "/(?:)/".

The method works as follows:

1. For the pattern "a+b+c", it returns /a+b+c/

2. Empty regular expressions produce /(?:)/ (object type: string)

3. The method's output indicates whether the regular expression has flags, with non-empty flags appearing after the source pattern

4. Line terminators like \n in the pattern are properly escaped in the returned string representation

5. The returned value always includes the forward slashes that delimit the regular expression's pattern

6. The order of flags in the returned string may differ from their original specification

7. The resulting string is optimized for parsing, making it suitable for reconstructing the regular expression as needed


## Browser Compatibility

The `toString()` method of the `RegExp` object returns a string in the form `/source/flags`, where `source` represents the regular expression pattern and `flags` represent the various options and modifiers. This method is documented in the ECMAScript 2026 Language Specification, section 4.3.1.1, and is consistent in behavior with the general `Object.prototype.toString()` method, which returns `"[object RegExp]"` for regular expression objects.

As with other `toString()` implementations in JavaScript, the method accesses the `source` property to determine the string value. For an empty regular expression, it returns the string `"/(?:)/"`. The implementation ensures that line terminators such as `\n` are properly escaped in the returned string representation. This escaping guarantees that the returned value is always a valid regex literal, though in some cases the order of flags may differ from their original specification.

The browser compatibility information is consistent across modern browsers, with the feature being available in Chrome, Edge, Firefox, Safari, and Opera. Implementation details for Firefox note that starting with version 34, when a capturing group with quantifiers prevents its exercise, the matched text for that capturing group returns `undefined` instead of an empty string. However, the general behavior of `RegExp.$N` remains unchanged, continuing to return an empty string rather than `undefined`.

The broader `Object.prototype.toString()` method has been a fundamental part of JavaScript since July 2015. When called on `RegExp` objects, it consistently returns `"[object RegExp]"`, providing a standardized way to determine object class across different types of JavaScript values. This method serves multiple purposes, from debugging and logging to type checking and object introspection, making it a versatile component of JavaScript's object representation system.

