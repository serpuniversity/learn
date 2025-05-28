---

title: Regex Invalid Range in Character Class

date: 2025-05-26

---


# Regex Invalid Range in Character Class

Regular expressions provide a powerful way to match patterns in text, but their complexity can lead to errors if not understood correctly. One common issue developers encounter is the "invalid range in character class" error. This occurs when attempting to define a character class range where the start value is greater than the end value, or when special characters are improperly escaped. The error highlights the importance of proper syntax and understanding of Unicode character properties in regular expressions. This article examines the root causes of this error, provides examples of common scenarios where it occurs, and offers best practices to prevent similar issues in your regular expressions.


## Error Description and Common Causes

The 'invalid range in character class' error occurs when a character class in a regular expression uses a range with incorrect boundaries or improperly escaped characters. This exception appears in various JavaScript engines, including V8-based environments (Chrome, Node.js), Firefox, and Safari.


### Character Class Syntax and Ranges

Character classes allow joining two characters with a hyphen `-` to represent an inclusive interval of characters based on their Unicode code points. For example, `[a-z]` matches any lowercase letter. When creating character class ranges, the start value must be less than or equal to the end value. Attempting to create a range where the first character's value is greater than the second character's value results in the 'invalid range in character class' error. For instance, the pattern `[9-1]` will generate this exception because 9 is greater than 1.


### Escaping Special Characters

Special characters in regular expressions, including hyphens and square brackets, must be escaped using a backslash unless they are part of a predefined character class escape sequence. Proper escaping is crucial when using these characters within character class ranges. For example, the pattern `[_-]` matches the underscore and hyphen characters. The character class could also be written as `[-_]` with the hyphen moved to the end to avoid interpretation as a range. When using the RegExp object, two backslashes are needed for escaping, as seen in the example `/[\d\-]/`.


### Common Error Scenarios

The error frequently occurs when character class escapes are used within ranges, such as `/[\w-+]/u`. In Unicode-unaware mode, the hyphen character becomes literal if it is between character class boundaries, causing an error. To avoid this, the character class should be written as `/[\w\-+]/u`, placing the hyphen at the end of the character class. Another common issue arises when attempting to create ranges using Unicode characters, as character code values may not align in sequence. For example, the pattern `[A-z]` includes six non-letter characters between 'A' and 'z' due to Unicode character properties.

The error also appears when character class boundaries contain other character class escapes. For instance, `/[s-9]/u` results in a SyntaxError because 's' and '9' are both character class escapes in Unicode mode. The pattern can be corrected by escaping the hyphen: `/[s\-9]/u`.


### Workarounds and Best Practices

To avoid the 'invalid range in character class' error, developers should ensure character class boundaries represent single characters and maintain proper escaping techniques. When creating ranges for non-sequential Unicode characters, consider alternative approaches such as using individual character matches or adjusting the pattern structure. Understanding the differences between V8 and Mozilla regex implementations helps in identifying and resolving these errors consistently across environments.


## Character Class Syntax and Ranges

Character classes define ranges of characters using a hyphen `-` between two characters, representing an inclusive interval based on their Unicode code points. The syntax allows matching any character within the specified set, using single characters or escape sequences. For example, `[A-Z]` matches any uppercase letter, and `\d` represents any digit.

The character class syntax requires the two boundaries to represent single characters. When creating ranges, the first character's value must be less than or equal to the second character's value. For instance, `[9-1]` generates a syntax error because 9 is greater than 1. Attempting to use character class escapes within ranges, such as `[\w-+]`, causes issues in Unicode-aware mode. To avoid these errors, developers should place the hyphen at the end of the character class: `[\w-+]`.

The JavaScript engine treats characters as Unicode code points in non-v-mode, while v-mode considers surrogate pairs representing two characters. In Unicode-unaware mode, the hyphen becomes literal instead of causing an error. This deprecated syntax should not be relied upon, as it can lead to unexpected behavior in newer engines.

Character classes can also create complement sets using the caret `^` prefix, which matches any character not in the specified set. For example, `[^ae]` matches any character except 'a' or 'e'. The behavior of negated character classes includes case-folding, where the negated set includes all non-lowercase characters and matches using caseless comparisons.

To create more complex set operations, JavaScript's regex engine supports v-mode character classes with set notation using intersection (`&&`), subtraction (`--`), and union. For example, `[\w&&[A-z]--_]` creates a union of the intersection of word characters and uppercase letters with the subtraction of underscore. However, operators cannot be mixed on the same level: `[\w&&[A-z]--_]` is invalid, while `[\w&&[[A-z]--_]]` or `[[\w&&[A-z]]--_]` correctly express the same set.


## Escaping Special Characters

Special characters in regular expressions, including hyphens and square brackets, must be escaped using a backslash unless they are part of a predefined character class escape sequence. For example, to search for "a" followed by "*" followed by "b", use /a*b/. To match a literal slash, use backslashes before each slash: /\/example\/[a-z]+/. To match a literal backslash, escape it: /[A-Z]:\\/.

When using the RegExp constructor with string literals, backslashes must be escaped at both the string and regular expression levels. The RegExp.escape() function returns a new string with all special characters escaped, allowing creation of specific regex strings like new RegExp(RegExp.escape("a*b")).

The character class syntax requires special characters to be escaped properly. For instance, in the pattern `[_-]`, the hyphen and underscore each need to be escaped as backslashes: `\\[_\\-]`. Alternatively, the character class can be written as `[-_]`, placing the hyphen at the end of the class to avoid interpretation as a range.

In non-v-mode character classes, only character class escapes are allowed. However, in v-mode character classes, certain syntax characters are forbidden from appearing literally: `(){}[]{}/|-|`. When these characters need to be matched literally, they must be escaped with a backslash. For example, to match a literal parenthesis, use /(\())/.

When creating ranges, the character class boundaries must represent single characters. The first character's value must be less than or equal to the second character's value. For instance, the pattern `[9-1]` generates a syntax error because 9 is greater than 1. The pattern `[A-z]` includes six non-letter characters between 'A' and 'z' due to Unicode character properties. To include special characters like hyphens, underscores, or dots in character classes, they should be placed as either the first or last character in the group, such as `[-a-zA-Z0-9_.]` or `[a-zA-Z0-9_.-]`.

The JavaScript engine distinguishes between character classes in Unicode-unaware mode and v-mode. In non-ECMAScript mode, character ranges treat characters as BMP characters, while surrogate pairs represent two characters in v-mode. When one boundary of a character range is another character class, the hyphen becomes a literal character in Unicode-unaware mode. For example, /[s-9]/u results in a SyntaxError, but /[s-9]/.test("-") returns true in Unicode-unaware mode. The pattern should be corrected by escaping the hyphen: /[s\-9]/u.


## Common Error Scenarios

The error frequently occurs when character class escapes are used within ranges, such as `/[\w-+]`. In Unicode-unaware mode, the hyphen character becomes literal if it is between character class boundaries, causing an error. To avoid this, the pattern should be written as `/[\w-+]`, placing the hyphen at the end of the character class.

The error also appears when character class boundaries contain other character class escapes. For instance, /[s-9]/u results in a SyntaxError because 's' and '9' are both character class escapes in Unicode mode. The pattern can be corrected by escaping the hyphen: /[s\-9]/u.

When using the RegExp constructor with string literals, backslashes must be escaped at both the string and regular expression levels. The RegExp.escape() function returns a new string with all special characters escaped, allowing creation of specific regex strings like new RegExp(RegExp.escape("a*b")).

The error can occur in various scenarios, including attempting to create ranges with non-contiguous Unicode characters, placing character class escapes incorrectly within ranges, and using the `u` flag with specific patterns that work differently in Unicode-aware mode. For example, /[a-z]` fails if 'a' and 'z' are not contiguous in Unicode, while /[A-z]` includes multiple non-letter characters between 'A' and 'z' due to Unicode properties.

The issue arises because of the way JavaScript engines handle character ranges, particularly when dealing with Unicode character properties and non-contiguous character sets. While Microsoft's regex engine supports Unicode ranges, other implementations may behave differently, making it essential for developers to understand the specific behavior of their target environment.


## Best Practices and Workarounds

Following best practices for character class usage helps in preventing the 'invalid range in character class' error. Always verify that the character class boundaries represent single characters, with the first character's value less than or equal to the second character's value.

In Unicode-unaware mode, ensure special characters are properly escaped using double backslashes when creating string literals for regular expressions. For example, the pattern `new RegExp("^([A-Za-z0-9_\\-\\.])+@", domain + "$")` requires doubling the escaping of `-` and `_` characters to prevent the engine from interpreting them as range delimiters.

To maintain compatibility across JavaScript environments, especially when using the `u` flag for Unicode-aware mode, avoid placing character class escapes within character ranges. Instead, ensure the hyphen character is placed at the beginning or end of the character class when including special characters like `-`, `_`, or `.`, as demonstrated in valid patterns like `[-a-zA-Z0-9 _]` or `[a-zA-Z0-9 _-]`.

Developers should also be aware of limitations in specific frameworks or libraries. For instance, the intl-tel-input project experienced issues in Firefox when using the character "ÿ" within a character class pattern, highlighting the need for careful testing across different environments and versions of JavaScript engines.

