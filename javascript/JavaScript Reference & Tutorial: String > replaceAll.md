---

title: JavaScript replaceAll() Method

date: 2025-05-27

---


# JavaScript replaceAll() Method

The JavaScript `replaceAll()` method represents a significant advancement in string manipulation capabilities, offering developers a powerful tool for comprehensive text transformation. Unlike its predecessor, the `replace()` method, which only targets the first occurrence of a pattern, `replaceAll()` delivers on its promise of complete substitution through native browser support in modern environments like Chrome 85+, Firefox 77+, and Safari 13.1+. This introduction will explore the method's syntax, functionality, and implementation across both simple string patterns and complex regular expressions, highlighting its role in JavaScript's evolving string manipulation standards.


## Introduction to replaceAll()

The JavaScript `replaceAll()` method enables developers to substitute all instances of a specified substring or pattern within a string, returning a modified copy of the original string. This functionality represents an evolution from the `replace()` method, which only substitutes the first occurrence of a pattern, making `replaceAll()` particularly valuable for situations requiring comprehensive string transformation.

The method's implementation introduced with ECMAScript 2021 allows developers to employ either simple strings or regular expressions as search patterns, with the latter requiring the inclusion of the global flag (`g`) to ensure all matches are targeted. When using regular expressions, developers have the flexibility to incorporate sophisticated matching criteria while maintaining the method's primary goal of complete string replacement.


### Syntax and Parameter Usage

The `replaceAll()` method adheres to the syntax `string.replaceAll(pattern, replacement)`, where `pattern` represents the substring or regular expression to be replaced, and `replacement` defines the new content to substitute these patterns. The method's return value is a newly created string containing all matches of `pattern` replaced by `replacement`, leaving the original string unaltered.

Developers can implement this functionality using native browser support in modern environments, including Chrome 85+, Firefox 77+, and Safari 13.1+, or through polyfills for earlier browser versions, ensuring compatibility with diverse development contexts.


## Syntax and Parameter Explanation

The `replaceAll()` method operates on a syntax paradigm similar to other string manipulation functions, accepting a pattern and a replacement value to construct a new string. The pattern parameter may be either a simple string or a regular expression, while the replacement can accommodate either a standard string or a function that generates the replacement content.

When utilizing simple strings as patterns, `replaceAll()` functions in a manner analogous to its counterpart `replace()`, but operates globally across the entire string rather than targeting only the initial occurrence. This fundamental functionality enables developers to construct strings with consistent replacements, particularly when implementing transformations or data normalization processes.

For more complex pattern matching, developers may employ regular expressions, though these require the inclusion of the global flag (`g`) to facilitate multi-occurrence searches. The method processes these patterns through a similar evaluation chain as standard replace() operations, transforming matched elements according to the specified replacement logic. The result is a return value representing the modified string, while the original remains unaltered.

The method's implementation across different environments demonstrates its growing standardization, with native support emerging in major browser versions since 2021. For developers working in earlier JavaScript contexts, polyfill options are available to enable compatibility with `replaceAll()` functionality, though careful consideration of performance implications may be necessary when employing these solutions.


## Using replaceAll() with Simple Strings


### Syntax and Usage

The `replaceAll()` method operates on a syntax paradigm similar to the standard replace() method, accepting a pattern and a replacement value to construct a new string. While both methods support simple string patterns, `replaceAll()` provides global replacement functionality through regular expressions, requiring the inclusion of the global flag (`g`) for comprehensive searches.


### Basic Examples

The method enables straightforward string transformations, as demonstrated by replacing simple substrings with new values. For instance, the code snippet `myString.replaceAll("hello", "world")` would convert all instances of "hello" to "world" within myString. This functionality mirrors the behavior of the standard replace() method when both parameters are strings.


### Regular Expression Support

For more complex pattern matching, developers can utilize regular expressions through the same basic syntax: `myString.replaceAll(pattern, replacement)`. The method processes these patterns in a manner similar to the standard replace() operation, transforming matched elements based on the specified replacement logic. The global flag remains crucial for targeting all occurrences within a string.


### Behavior with Special Characters

The method handles special characters appropriately through standard JavaScript conventions. For example, the pattern "\." requires escaping to match a literal dot, as demonstrated by `myString.replaceAll("\\.", "-")`. This behavior aligns with JavaScript's regular expression standards, ensuring consistent pattern matching across various use cases.


## Using replaceAll() with Regular Expressions

The `replaceAll()` method requires a global regular expression when using a regular expression search value, as demonstrated by the example: `"aabbcc".replaceAll(/b/, ".")` throws a TypeError, while `"aabbcc".replaceAll(/b/g, ".")` returns the expected result of `"aa..cc"`. This behavior aligns with JavaScript's regular expression standards, ensuring consistent pattern matching across various use cases.

When working with regular expressions, developers have the flexibility to incorporate sophisticated matching criteria while maintaining the method's primary goal of complete string replacement. The method processes these patterns in a manner similar to the standard replace() operation, transforming matched elements based on the specified replacement logic.

For more complex replacements, especially case-insensitive ones, developers can use regular expressions with the global flag (`g`) and the case-insensitive flag (`i`). As shown in the documentation example: `my_string.replaceAll(/dogs/gi, "cats")`, this approach enables comprehensive string transformation while maintaining the method's core functionality.

The method's implementation across different environments demonstrates its growing standardization, with native support emerging in major browser versions since 2021. For developers working in earlier JavaScript contexts, polyfill options are available to enable compatibility with `replaceAll()` functionality, though careful consideration of performance implications may be necessary when employing these solutions.


## Compatibility and Browser Support

Supported in modern browsers and ES2021, the `replaceAll` method replaces all occurrences of a search value with a replace value in a string. For string patterns, it replaces all specified substrings, while for regular expressions, it requires the global flag (`g`) for multi-occurrence searches. This functionality mirrors the behavior of splitting by search value and joining with replace value, aligning with JavaScript's convention for comprehensive string transformation.

The method works similarly to the standard `replace` method but provides additional compatibility and functionality. While `replace` replaces only the first occurrence or matches a non-global regular expression once, `replaceAll` performs complete replacements as demonstrated in the native browser implementation examples. For older browsers or environments, the method is available in polyfills, with the core-js library providing reliable polyfill support since around 2012.

Implementing the method requires careful consideration of performance implications, particularly in cases involving recursive functions or complex string manipulations, where native implementations may offer superior performance to alternative methods like `split().join()` or traditional `replace()` approaches. The browser compatibility landscape includes support in Chrome 85+, Firefox 77+, and Safari 13.1+, with additional support available through polyfills and native implementations in modern JavaScript environments.

