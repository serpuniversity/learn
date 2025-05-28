---

title: Deprecated Octal Escape Sequences in JavaScript

date: 2025-05-26

---


# Deprecated Octal Escape Sequences in JavaScript

JavaScript's octal escape sequences and literal notation once provided a convenient way to represent character codes in the language. However, with the evolution of JavaScript standards, these features have been deprecated, particularly in strict mode. Understanding why these changes were made and how to transition your code is crucial for maintaining compatibility and adhering to best practices in modern JavaScript development. This guide walks you through the deprecation of octal escape sequences, the proper syntax for modern JavaScript, and provides practical examples of how to update your code to avoid future errors.


## Introduction to Octal Escape Sequences

The "0"-prefixed notation for octal literals and escape sequences has been deprecated in JavaScript, particularly when executing in strict mode. These sequences, which use octal notation to represent character codes, are no longer supported in modern JavaScript environments. While the deprecated syntax continues to function in non-strict mode, developers are advised to avoid using it in new code.

In strict mode, developers should use the 0o prefix for octal literals. For example, instead of writing 03, they should write 0o3. Similarly, when using escape sequences in string literals and template literals, developers should replace \251 with \u00A9 to correctly represent the copyright symbol.

The deprecation of these features affects both string literals and template literals, with strict mode specifically prohibiting the use of octal escape sequences. Attempting to use these sequences in strict mode results in a SyntaxError. For instance, the following code will throw an error:

```javascript

"use strict";

let a = "\251"; // SyntaxError: Octal escape sequences not allowed in strict mode

```

To avoid these errors, developers should transition to using hexadecimal or Unicode escape sequences. For example, instead of \251, they should use \u00A9. For template literals, String.raw can be used to avoid interpreting escape sequences:

```javascript

String.raw`\251`; // Produces a string containing the characters '\251'

```

Best practices recommend avoiding the use of octal escape sequences and octal literals whenever possible, as they are deprecated and may cause compatibility issues in future JavaScript implementations. The modern approach to character representation in JavaScript encourages the use of hexadecimal (\x) and Unicode (\u) escape sequences for maximum compatibility and maintainability.


## Octal Literals in Strict Mode

In strict mode, octal literals that are prefixed with the number 0 are now deprecated and will generate a SyntaxError when used. To write valid octal literals in strict mode, developers should use the 0o prefix instead. For example, an octal value of 3 can now be correctly represented as 0o3.

The deprecation of this syntax aligns with broader changes in JavaScript's strict mode, which was introduced to enforce stricter parsing rules and error handling. Octal literals and escape sequences are specifically mentioned as deprecated features in the ECMAScript 5 specification, and their use in strict mode will no longer be permitted.

When transitioning existing code, developers should replace all instances of 0-prefixed octal literals with the 0o prefix. This change affects both standalone octal literals and their use in string literals and template literals. For example, the following code will generate a SyntaxError when run with strict mode:

```javascript

use strict;

03; // SyntaxError: "0"-prefixed octal literals and escape sequences are deprecated

```

To maintain compatibility with modern JavaScript standards, developers are encouraged to use hexadecimal or Unicode escape sequences as alternatives. For instance, the octal value 251 can be represented using a Unicode escape sequence:

```javascript

0o251; // Valid octal literal

'\u00A9'; // Equivalent Unicode escape sequence

```


## Octal Escape Sequences in Strict Mode

In string literals and template literals, the use of octal escape sequences is specifically deprecated in strict mode, with valid alternatives being hexadecimal or Unicode escape sequences. This change impacts both standalone octal literals and their use within string literals and template literals.

The deprecation affects both untagged template literals and tagged template literals, though the latter can still contain octal escape sequences that produce undefined values in the template array passed to the tag function. The restriction applies most strictly to Firefox and V8-based environments, where attempting to use deprecated octal sequences in untagged template literals or strict mode code will result in the error "Octal escape sequences can't be used in untagged template literals or in strict mode code."

For example, the following code will produce a SyntaxError in strict mode:

```javascript

use strict;

\251; // SyntaxError: octal escape sequences are not allowed in strict mode

```

Valid alternatives include using hexadecimal escape sequences, as in "\xA9" for the copyright symbol, or the String.raw method to preserve the literal string "\251" without interpreting the escape sequence:

```javascript

String.raw`\251`; // Produces a string containing the characters '\251'

```

The deprecation aligns with broader changes in JavaScript's strict mode, which was introduced to enforce stricter parsing rules and error handling. Similar to other deprecated features, the change aims to improve code maintainability and alignment with international standards for character representation.


## Legacy Support and Best Practices

In non-strict mode, the deprecated "0"-prefixed octal literals and escape sequences remain functional. However, they should not be used in new code due to potential compatibility issues with future JavaScript implementations. For strict mode, developers should use the 0o prefix for octal literals and hexadecimal or Unicode escape sequences for character representation.

The current specification requires strict mode to enforce these changes, though legacy support exists for backward compatibility. The deprecation began in ECMAScript 2015 and applies to all subsequent versions. Developers transitioning code should carefully review their use of octal literals and escape sequences, replacing them with modern alternatives when possible.

The strict mode restriction affects both standalone octal literals and their use within string literals and template literals. Developers should avoid the use of octal escape sequences in template literals to prevent SyntaxErrors. For example, the following code will produce an error:

```javascript

use strict;

\251; // SyntaxError: octal escape sequences can't be used in untagged template literals or in strict mode code

```

To maintain compatibility and adhere to best practices, developers are encouraged to replace octal escape sequences with equivalent hexadecimal or Unicode escape sequences. This transition not only ensures compatibility with modern JavaScript standards but also improves code maintainability and alignment with international character representation standards.


## Syntax Errors and Error Messages

JavaScript strictly enforces deprecation of "0"-prefixed octal literals and escape sequences through its strict mode parser. These features, while functional in non-strict mode, generate SyntaxErrors when used in environments with strict mode enabled.


### Error Handling and Alternatives

To address these deprecation warnings, developers should replace "0"-prefixed octal literals with the "0o" or "0O" prefix. For example, an octal value of 3 should be written as 0o3. Similarly, octal escape sequences in string literals and template literals require alternative representation methods.


### Common Error Messages

The primary error messages developers encounter when using deprecated octal features include:

- "SyntaxError: "0"-prefixed octal literals and escape sequences are deprecated" when attempting to use octal notation in strict mode.

- "SyntaxError: octal escape sequences can't be used in untagged template literals or in strict mode code" specifically when using octal escape sequences in template literals.

Developers can resolve these errors by replacing octal escape sequences with hexadecimal (\x) or Unicode (\u) escape sequences. For instance, the octal escape sequence \251 should be replaced with the Unicode sequence \u00A9 to represent the copyright symbol correctly.


### Legacy Support

While strict mode enforces these changes, legacy support exists for "0"-prefixed octal literals in non-strict mode environments. However, developers are advised to avoid using these deprecated features in new code to ensure compatibility with future JavaScript implementations. The transition to modern escape sequence representations maintains code maintainability and alignment with international character representation standards.

