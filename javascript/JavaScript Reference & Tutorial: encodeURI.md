---

title: JavaScript encodeURI Function

date: 2025-05-26

---


# JavaScript encodeURI Function

When working with web applications, developers often need to manipulate and transmit Uniform Resource Identifiers (URIs) across different systems. This requires encoding special characters in URIs to ensure proper interpretation and compatibility across various environments. While standard string functions can handle many encoding needs, JavaScript provides specific tools like encodeURI to address the unique requirements of URI manipulation. This article examines the encodeURI function, its implementation, and its role in maintaining URI integrity while supporting essential special characters. We'll explore how encodeURI works with different character sets, reserved characters, and compare it to related functions like encodeURIComponent to understand when and how to use them effectively in web development projects.


## Introduction to encodeURI

The encodeURI function encodes a Uniform Resource Identifier (URI) using UTF-8 encoding escape sequences. It operates by replacing each instance of certain characters with escape sequences that represent their UTF-8 encoding. The function is designed to maintain the integrity of URI structure by preserving reserved characters that have special meanings within URIs.

The encoding process specifically addresses characters that fall outside the standard 128-character ASCII set, as these special characters are not permitted in URLs without proper encoding. The function employs UTF-8 code units for encoding, representing each octet in the format %XX and left-padding with 0 if necessary. However, the function encounters limitations with lone surrogates in UTF-16, as these do not represent valid Unicode characters and cause the function to throw a URIError.

The encodeURI function maintains strict adherence to URI syntax standards, escaping all characters except those that are integral to the URI structure. These reserved characters include: ; (semicolon), , (comma), / (slash), ? (question mark), : (colon), @ (at symbol), & (ampersand), = (equals sign), + (plus), and $ (dollar sign). Additionally, the function preserves unescaped characters that constitute valid URI components: A-Z, a-z, 0-9, -, _, ., !, ~, *, ' (single quote), and (parentheses). This selective encoding approach enables the function to handle complete URIs while maintaining their structural integrity and compatibility across modern browsers.


## Encoding Behavior

encodeURI encodes all characters except reserved characters (;, /, ?, : ,@, &, =, +, $) and unescaped characters (A-Z, a-z, 0-9, -, _, ., !, ~, *, ' ). This includes numerical digits (0-9), letters (A-Z, a-z), and certain special characters like punctuation marks (., -, _, !, ~, *, ' ).

The function processes each character individually, replacing it with one to four UTF-8 escape sequences based on its Unicode representation. Common escape sequences follow this format: %XX, where each X represents a hexadecimal digit. For example, the space character is encoded as %20. Special handling is required for characters composed of two "surrogate" characters, which encode to four-character sequences.

Reserved characters maintain their original form and are not altered during the encoding process. These characters have predefined meanings within URIs: ; (semicolon), , (comma), / (slash), ? (question mark), : (colon), @ (at symbol), & (ampersand), = (equals sign), + (plus), and $ (dollar sign). Additionally, the function preserves unescaped characters that constitute valid URI components: A-Z, a-z, 0-9, -, _, ., !, ~, *, ' (single quote), and (parentheses).

Certain characters outside this set, including square brackets [], are not encoded by default. To ensure RFC3986 compliance for these characters, developers may use a custom function that applies the necessary replacements after encoding. For example, the function `fixedEncodeURI` demonstrates this approach by replacing %5B and %5D with [ and ] respectively.


## Syntax and Parameters

The encodeURI function takes a URI parameter and returns a string representing the encoded URI. The syntax is straightforward: encodeURI(uri), where uri is the URI to be encoded. This function is designed to maintain the integrity of URI structure while encoding special characters using UTF-8 escape sequences.

The function processes each character individually, replacing it with UTF-8 escape sequences when necessary. These escape sequences follow the format %XX, where each X represents a hexadecimal digit. For example, the space character is encoded as %20. The function handles characters composed of two "surrogate" characters by using four-character sequences, as mandated by the ECMAScript standard.

Commonly, the function leaves certain characters unencoded to maintain their special meaning within URIs. These characters include: ; (semicolon), , (comma), / (slash), ? (question mark), : (colon), @ (at symbol), & (ampersand), = (equals sign), + (plus), and $ (dollar sign). Additionally, the function preserves unescaped characters that constitute valid URI components: A-Z, a-z, 0-9, -, _, ., !, ~, *, ' (single quote), and (parentheses).

While the function follows strict URI syntax standards, it has limitations with lone surrogates in UTF-16 encoding. These invalid Unicode characters cause the function to throw a URIError exception, preventing potential encoding issues that could arise from such characters.


## Comparison with encodeURIComponent

encodeURI and encodeURIComponent share similarities while operating with distinct purposes. Both functions encode special characters using UTF-8 escape sequences, with the primary difference lying in their encoding scope and target characters.

While encodeURI maintains the integrity of URI structure by preserving reserved characters, encodeURIComponent excludes reserved characters to ensure they remain interpretable as URI components. For example, encodeURI correctly encodes the space character as %20 while leaving reserved characters intact, while encodeURIComponent replaces spaces with %20 and further encodes reserved characters like ?, =, and &.

The functions' behavior with special characters demonstrates their specific use cases. encodeURI correctly handles the space character in "Amit Kumar" by encoding it as %20, preserving the integrity of the URI structure. In contrast, encodeURIComponent processes the same input by encoding it as "Amit%20Kumar", demonstrating its focus on encoding individual URI components rather than maintaining overall URI structure.

The functions' relationship with other encoding methods further highlights their distinct purposes. Both encodeURI and encodeURIComponent share similarities in their UTF-8 encoding approach, encoding all characters except A-Z, a-z, 0-9, -, _, ., !, ~, *, ' (single quote), and (parentheses). However, the key difference lies in their handling of reserved characters: encodeURI preserves them for URI structure integrity, while encodeURIComponent encodes them to maintain URI component compatibility.


## Browser Support and Standards

encodeURI is an ECMAScript 1 feature supported in all modern browsers including Chrome, Edge, Firefox, Safari, and Opera. The function works consistently across multiple browser versions, providing programmers with a reliable method for URI encoding.

As a built-in function in JavaScript, encodeURI simplifies URI encoding for developers while maintaining compatibility with older browser versions. Unlike some alternative encoding methods that may require significant modifications for cross-browser compatibility, encodeURI functions with minimal changes, making it a practical choice for web development projects.

The function has been standardized since ECMAScript 3rd Edition and continues to support modern web development needs through its widespread browser compatibility. This long-term support ensures that developers can rely on encodeURI functionality across diverse user environments, from older desktop browsers to the latest mobile devices.

