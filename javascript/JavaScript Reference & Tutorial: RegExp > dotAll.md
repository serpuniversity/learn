---

title: JavaScript RegExp: dotAll

date: 2025-05-26

---


# JavaScript RegExp: dotAll

In JavaScript, regular expressions offer a powerful way to process and extract information from text. While the basic dot (.) character matches most characters, including newlines in some cases, the dotAll property takes control over this behavior through the 's' flag. This introduction explores how dotAll works across different JavaScript environments, its impact on pattern matching, and best practices for effective text processing. Understanding this feature is crucial for developers working with multiline strings, log files, or HTML content, where precise character matching can significantly affect the outcome of regular expressions.


## dotAll Property Overview

The dotAll property in JavaScript regular expressions manages the behavior of the dot (.) character, determining whether it matches all characters including line terminators. This property is crucial for developers working with text that includes newlines or other Unicode characters.

When dotAll is enabled through the 's' flag, the dot (.) character matches any Unicode character, including line terminators such as \n (line feed), \r (carriage return), and U+2028 and U+2029 (line separator and paragraph separator respectively). This behavior makes regular expressions more intuitive for processing multiline data and simplifies pattern matching across multiple lines.

The dotAll property is particularly useful in scenarios like matching log entries, extracting content from HTML, or processing any text that includes potential line breaks. For example, enabling dotAll allows patterns like "Start.*End" to match across multiple lines correctly.

Several engines have implemented support for the dotAll functionality, including V8 (Chrome 62), JavaScriptCore (Safari Technology Preview 39a), XS (Moddable), and others. The feature was first introduced in ECMA2018 and has since been adopted across multiple JavaScript environments, though full browser support may vary.


## Behavior with dot and s Flag

The dotAll property is a read-only Boolean that indicates whether the s flag is present in a given regular expression. It reflects the state of the s flag and cannot be changed directly. When the s flag is set, the dot (.) character matches all characters, including line terminators like \n, \r, and other Unicode line terminators. By default, dotAll is false unless explicitly enabled with the s flag.

The property provides important information about the matching behavior of regular expressions. For example, a regex object created with new RegExp("example", "s").dotAll would return true, indicating that the dot matches all characters, including line terminators. In contrast, new RegExp("example").dotAll would return false, showing the default behavior where the dot matches all characters except line terminators.


### Matching Examples

The dotAll property enables more intuitive pattern matching, particularly for multiline strings and content extraction. Consider the following examples:

- **Multiline String Matching**: `let s = "Hello\nWorld!"; let regex = /Hello.World/s; console.log(regex.test(s));` returns true, demonstrating correct multiline matching.

- **Text Extraction Across Lines**: `let s = `Start Middle End`; let regex = /Start.*End/s; console.log(regex.test(s));` returns true, while `console.log(s.match(regex)[0]);` correctly returns "Start Middle End".

- **Simple Multiline Pattern**: `let s = "abc\ndef"; let regex = /a.c/s; console.log(regex.test(s));` returns true, matching the pattern across lines.

- **HTML Tag Extraction**: `let html = "<div>\n Content\n</div>"; let regex = /<div>.*<\/div>/s; console.log(html.match(regex)[0]);` correctly extracts "<div> Content </div>", showcasing line terminator matching.


### Historical Implementation

The introduction of the dotAll flag in ECMAScript 2018 brought improved regular expression functionality. Several engines have implemented support:

- V8 (Chrome 62)

- JavaScriptCore (Safari Technology Preview 39a)

- XS (Moddable)

- regexpu (transpiler with { dotAllFlag: true } option)

- online demo

- Babel plugin

- Compat-transpiler of RegExp Tree

- Babel plugin

The flag's implementation resolves longstanding limitations in regular expression behavior, particularly with newline characters and multibyte Unicode characters. It enables more intuitive and powerful text processing capabilities in JavaScript.


## Matching Behavior Examples

The dotAll property enables more intuitive pattern matching for multiline strings and content extraction. Several key examples demonstrate its functionality:

- Matching Multiline Strings: `let s = "Hello\nWorld!"; let regex = /Hello.World/s; console.log(regex.test(s));` returns true, showing correct multiline matching.

- Extracting Text Across Lines: `let s = `Start Middle End`; let regex = /Start.*End/s; console.log(regex.test(s));` returns true, while `console.log(s.match(regex)[0]);` correctly extracts "Start Middle End".

- Simple Multiline Match: `let s = "abc\ndef"; let regex = /a.c/s; console.log(regex.test(s));` returns true, demonstrating matching across lines.

- HTML Tag Extraction: `let html = "<div>\n Content\n</div>"; let regex = /<div>.*<\/div>/s; console.log(html.match(regex)[0]);` correctly extracts "<div> Content </div>", highlighting line terminator matching.

The dotAll property also allows more efficient processing of log entries and multi-line text blocks. For example:

- Matching Entire Multiline Blocks: `let log = "Error: Something went wrong. Details: Line: 42 File: app.js"; let regex = /Error:.*?app\.js/s; console.log(regex.test(log));` returns true, correctly identifying relevant log information.

This property works seamlessly with existing regular expression features. For instance, combining dotAll with the global flag enables efficient pattern extraction:

- Global and dotAll Matching: `let s = "line1\nline2"; let regex = /.*line2/s; console.log(regex.test(s));` returns true, demonstrating successful multiline matching with global flag.

The dotAll property's straightforward implementation makes it a valuable tool for JavaScript developers working with complex text patterns. Through these examples, it becomes clear why the feature was introduced in ECMA2018 to enhance regular expression functionality.


## Historical Context and Browser Support

The origin of the dotAll functionality traces back to the 2018 ECMAScript specification, which introduced the feature as part of its evolution. The implementation initially rolled out across multiple engines, with browser support following shortly thereafter.

While the specific compatibility timeline varied across different platforms, several JavaScript environments began implementing dotAll support in 2018. This included V8 (Chrome 62), JavaScriptCore (Safari Technology Preview 39a), and the XS engine from Moddable. More recent developments have seen additional support from tools like Babel and its plugins, demonstrating the increasing importance of the feature in modern JavaScript development.

The flag's implementation resolves long-standing limitations in regular expression behavior, particularly with newline characters and multibyte Unicode characters. Current documentation shows that the dotAll property is read-only and reflects the presence of the s flag, enabling developers to write more concise and intuitive code for multiline text processing.

The feature's integration with existing regular expression capabilities makes it a valuable tool for developers working with complex text patterns. As browser support continues to evolve, the dotAll property stands to become an increasingly important part of JavaScript's text processing toolkit.


## Best Practices and Considerations

The dotAll property plays a crucial role in JavaScript's regular expression functionality, particularly when combined with other flags like global (`g`) and multiline (`m`). Understanding how to use these properties effectively can significantly enhance text processing capabilities.


### Combining dotAll with Other Flags

The dotAll property works seamlessly with the global flag (`g`) for comprehensive pattern extraction. This combination enables developers to search through multiline strings while matching all characters, including line terminators. For example, the pattern `/a.c/s` matches "a.c" across multiple lines, making it ideal for processing log entries or any text containing potential line breaks.

When working with multiline text blocks, the dotAll flag should be used in conjunction with the multiline flag (`m`). This combination allows patterns to match across multiple lines while maintaining anchor positions correctly. For instance, the pattern `/^Start.*End$/sm` matches the string "Start\nMiddle\nEnd" while ensuring that both the start and end anchors work as intended.


### Implementation Considerations

Developers should be aware of the potential impact of combining multiple flags. For example, when using both dotAll and sticky mode (`y`), developers should test thoroughly to ensure expected behavior. The sticky mode flag (`y`) affects pattern matching at the current position, which can interact unpredictably with other flags in certain edge cases.


### Best Practices

To effectively use the dotAll property, developers should:

- Always enable the dotAll flag when processing multiline text or HTML content.

- Combine dotAll with the global flag (`g`) for efficient pattern extraction across multiple lines.

- Use the multiline flag (`m`) when working with anchors that need to match across lines.

- Test thoroughly when combining dotAll with other flags like sticky mode (`y`).

By following these guidelines, developers can write more robust and maintainable regular expressions for complex text processing tasks.

