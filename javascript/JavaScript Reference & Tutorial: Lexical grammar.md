---

title: JavaScript Reference & Tutorial: Lexical Grammar

date: 2025-05-27

---


# JavaScript Reference & Tutorial: Lexical Grammar

JavaScript's lexical structure forms the foundation of the language, dictating how source code is converted into executable instructions. This comprehensive guide explores the technical details of JavaScript's lexical grammar, from basic character rules to advanced syntax features. We'll examine how the Unicode character set shapes tokenization, how comments influence parsing behavior, and the precise rules governing identifiers and expressions. Whether you're a seasoned developer or just beginning to explore JavaScript, understanding these fundamental concepts will deepen your comprehension of the language's inner workings.


## Basic Concepts

JavaScript's lexical structure consists of simple rules that define how characters are combined into tokens. The language processes source text from left to right, converting it into individual atomic elements through a process called lexical analysis. This analysis removes insignificant elements such as white space and comments before further syntax analysis can occur.

The Unicode character set forms the basis for character combination rules. Each character must adhere to Unicode standards, with whitespace characters being particularly noteworthy. Common white space characters include spaces, tabs, and newline characters. The Unicode standard affects how characters like U+180E MONGOLIAN VOWEL SEPARATOR are interpreted. ES2016 updated the Unicode standard from 5.1 to 8.0.0, changing the category of this character from Space_Separator to Format (Cf), which affected its behavior in string manipulation functions like `trim()`.

The language distinguishes between different types of whitespace characters. Format control characters, including Zero Width Non-Joiner (U+200C) and Zero Width Joiner (U+200D), do not display visually but influence text interpretation. The Byte Order Mark (U+FEFF) indicates Unicode script and helps detect encoding and byte order. These characters affect how JavaScript processes source text, particularly in string handling and regular expressions.

Comments in JavaScript come in three forms: single-line (//), multi-line (/* */), and hashbang comments (!#). Single-line comments apply to the following line only, while multi-line comments span multiple lines and cannot be nested. Hashbang comments specify the path of the JavaScript interpreter to be used for executing the entire script. The interpretation of comments guides automatic semicolon insertion (ASI) rules, especially when line terminators are involved.

Identifiers must start with a letter, underscore (_), or dollar sign ($), followed by letters, digits, or Unicode characters. The language is case-sensitive, treating car, Car, CAR, and cAr as distinct identifiers. The naming rules align with Unicode Standard Annex #31, with some minor modifications noted in the lexical grammar specifications. This case sensitivity extends to keywords like while, which must be typed exactly as "while" and cannot be written as "While" or "WHILE".


## Tokenization

The lexical structure consists of simple rules that define how characters in the language are combined into tokens. JavaScript uses the Unicode character set, which forms the basis for character combination rules. Each character must adhere to Unicode standards, particularly whitespace characters, which influence text interpretation.

JavaScript's parser employs a two-step process: lexical analysis scans the text from left to right, converting it into individual input elements, while further syntax analysis interprets these elements. The initial conversion produces tokens, which are the smallest individual units of a program. These tokens can include keywords, identifiers, operators, and literals.

JavaScript comments are syntactically insignificant but guide automatic semicolon insertion. Single-line comments start with `//` and continue until the end of the line, while multi-line comments begin with `/*` and end with `*/`. The language also supports hashbang comments, which specify the path of the JavaScript interpreter to be used for executing the entire script.

The parser uses several production rules to determine tokenization. The `InputElementDiv` production consists of whitespace followed by a line terminator and optional comment, followed by the division operator (`/`) and other punctuators. The `InputElementRegExp` production behaves similarly but places a RegularExpressionLiteral after the division operator.

String literals follow specific rules for character interpretation. The base string value is the empty string when enclosing characters are empty. Double string characters match SourceCharacter unless they represent special line or paragraph separator characters (LINE SEPARATOR and PARAGRAPH SEPARATOR). Single string characters behave similarly, returning the UTF-16 encoded code point or special separator characters.

The identifier code point determination follows a piecewise structure over IdentifierStart and IdentifierPart, with UnicodeEscapeSequence returning the appropriate code point based on Hex4Digits or CodePoint value. Identifier categories allow Math, window, toString, and underscore as always-allowed identifiers, with specific restrictions on reserved word usage in strict mode except for await and yield.


## Expressions and Statements

Expressions in JavaScript combine values, variables, and operators to compute results. Basic expressions include arithmetic operations like (5 + 6) * 10 and variable assignments such as x = 5; y = 6;. The language supports string concatenation with expressions like "John" + " " + "Doe".

The language includes keywords for variable declaration, with let creating block-scoped variables and var creating function-scoped variables (deprecated). Variable values are assigned using the equal sign (=), and the language supports arithmetic operations with operators +, -, *, /.

Statement structure in JavaScript requires careful attention to punctuation, particularly when using automatic semicolon insertion (ASI). This feature inserts semicolons in specific cases to maintain correct program syntax. For example, a sequence like { 1 2 } 3 becomes { 1 ;2 ;} 3; after ASI. Other cases include a = b ++c (transformed to a = b; ++c;) and return a + b (transformed to return; a + b;).

The language distinguishes between identifiers (variable names) and numbers, with rules for legal names: identifiers must start with a letter, dollar sign ($), or underscore (_), followed by letters, digits, underscores, or dollar signs. Numbers cannot be the first character in an identifier. JavaScript is case-sensitive, meaning lastName and lastname are considered distinct identifiers. 

Reserved words in JavaScript have specific meanings and cannot be used as identifiers. These include var, if, else, for, while, function, return, true, false, null, undefined, this, new, delete, in, instanceof, typeof, void, with, break, continue, switch, case, among others. The language's case sensitivity affects how these reserved words are recognized and used in programming.


## Case Sensitivity and White Space

JavaScript's case sensitivity applies to all language elements, including keywords, variables, function names, and other identifiers. For example, while, While, and WALRUS represent three distinct identifiers, while var, if, else, for, function, return, true, false, null, undefined, this, new, delete, in, instanceof, typeof, void, with, break, continue, switch, and case must be typed exactly as shown to function correctly.

The language's whitespace handling allows developers to format code with indentation, line breaks, tabs, and spaces without affecting functionality. Standard white space characters include spaces, tabs, and newline characters, but JavaScript also recognizes several less common Unicode space characters. These include the zero-width non-joiner (U+200C), zero-width joiner (U+200D), and byte order mark (U+FEFF), which do not display visually but influence text interpretation.

Line terminators, beyond traditional whitespace characters, improve source text readability while affecting JavaScript code execution. They include U+000A (Line Feed), U+000D (Carriage Return), U+2028 (Line Separator), and U+2029 (Paragraph Separator). These characters serve multiple purposes: improving source text readability, influencing automatic semicolon insertion, and acting as comment terminators for block comments containing line terminators. Developers should be aware that while minification tools often remove whitespace for data transfer optimization, preserved whitespace can affect code readability and maintainability.


## Special Syntax Features

The grammar includes several unique syntax elements that enhance JavaScript's flexibility and expressiveness. These features include hashbang comments, template literals, and specific handling for `let` declarations within blocks.

Hashbang comments begin with "!#" and are distinct from regular single-line comments, which start with "//". Unlike standard comments, hashbangs are intended to specify the path of the JavaScript interpreter to be used for executing the entire script, overriding the default interpreter of the JavaScript engine. This feature allows developers to write cross-engine compatible code by explicitly defining the required interpreter at the beginning of their script.

Template literals offer a powerful way to construct and manipulate strings through multi-line support and embedded expressions. These literals are enclosed by backticks (`) and allow seamless integration of expressions through the ${} syntax. The grammar treats template literals as a sequence of three tokens: head (``xxx${`), middle (`}xxx${`), and tail (`}xxx``). This structure enables sophisticated string interpolation while maintaining clear parsing rules.

The `let` keyword presents unique challenges in the grammar due to its dual role in variable declaration and its interaction with lexical scopes. Unlike `var`, which creates function-scoped variables, `let` introduces block-scoped variables. This distinction affects how the parser handles declarations, particularly within block statements. The grammar allows `let` in function declarations but requires careful placement to avoid syntax errors. For instance, while the following code snippet demonstrates proper usage:

```javascript

function foo() {

  if (true) {

    let bar;

    function bar() {} // Valid block-scoped declaration

  }

}

```

Incorrect placement can lead to syntax errors:

```javascript

function foo() {

  let bar;

  function bar() {} // Syntax error: Identifier 'bar' has already been declared

}

```

Understanding these nuances is crucial for developers working with modern JavaScript features, particularly those transitioning from older versions or using environments with strict mode enabled. The grammar's sophisticated handling of `let` demonstrates the language's commitment to both flexibility and semantic correctness.

