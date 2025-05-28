---

title: JavaScript String endsWith() Method

date: 2025-05-26

---


# JavaScript String endsWith() Method

In modern web development, string manipulation is a fundamental skill that developers use daily. One common task is determining whether a string ends with a specific character or substring. While this seems straightforward, implementing such functionality requires considerations for both performance and browser compatibility.

The endsWith() method, introduced in ECMAScript 2015, simplifies this task by returning true if a string ends with a specified substring. However, its widespread adoption occurred relatively recently, with full browser support beginning in June 2017. For developers working with older browsers or environments that lack native endsWith() support, implementing this functionality requires careful consideration of performance implications.

This article explores the implementation and usage of the endsWith() method, examining its behavior with various input types and lengths. We'll also examine performance considerations when implementing this functionality in browsers that lack native support, comparing different approaches to ensure efficient string manipulation across all development environments.


## Method Overview

The endsWith() method returns true if a string ends with a specified character or string, and false otherwise. The method follows the syntax string.endsWith(searchValue, length), where searchValue is required and length is optional (defaulting to the string's full length).

The method performs a case-sensitive search and does not change the value of the original string. When using the length parameter, the method tests only the first specified number of characters from the end. For example, with the string "TechOnTheNet" and a length parameter of 6, it checks "TechOn" (the first 6 characters).

The endsWith() method has been implemented in modern browsers since June 2017:

- Chrome 51 and above

- Edge 15 and above

- Firefox 54 and above

- Safari 10 and above

- Opera 38 and above

For browsers that do not support endsWith(), you can implement the functionality using either of these two approaches:

1. Using regex and match:

```javascript

function endsWith(str, suffix) {

  var regex = new RegExp(suffix + '$');

  return str.match(regex) != null;

}

```

2. Using substr and length comparison:

```javascript

function endsWith(str, suffix) {

  return (str.length >= suffix.length) && (str.substr(str.length - suffix.length) === suffix);

}

```

Both implementations check if the string ends with the specified suffix. The regex approach uses the `$` symbol to ensure the suffix is at the end of the string, while the substr approach compares the substring from the end of the string with the suffix.


## Syntax and Parameters

The endsWith() method requires two parameters: searchString (the string to search for) and length (optional, determines the length of the given string value). It returns a boolean value (true if the string ends with the specified substring, false otherwise).

The method performs a case-sensitive search and works correctly for strings of length 1 or greater. For strings shorter than the search length, it returns false. When using the length parameter, the method tests only the first specified number of characters from the end. For example, with the string "TechOnTheNet" and a length parameter of 6, the method checks "TechOn" (the first 6 characters).

The method returns true if the given characters are found at the end of the string, including when searchString is an empty string. If the original string length is one less than the search string length and the search string is not found, lastIndexOf returns -1, causing potential errors in the original implementation. The alternative fix is to use this.length >= str.length && this.lastIndexOf(str) + str.length == this.length.

The method has been implemented in modern browsers since June 2017, with support in Mozilla Firefox (17.0 and above), Microsoft Edge (12.0 and above), Google Chrome (41 and above), Safari (9.0 and above), and Opera (28.0 and above). Internet Explorer does not support this functionality natively. For compatibility with older browsers, developers can use polyfills such as the one available at http://mths.be/endswith.


## Usage Examples

The endsWith() method can handle various scenarios for string comparison. For single characters, it can be used as:

```javascript

let name = "TechOnTheNet";

console.log(name.endsWith('N')); // true

console.log(name.endsWith('n')); // false

```

For multiple characters, the method checks if the string ends with the specified value:

```javascript

console.log(name.endsWith('Net')); // true

console.log(name.endsWith('Net', 5)); // true

console.log(name.endsWith('Net', 6)); // false

```

The method also works with multiple words:

```javascript

console.log("JavaScript ES6 methods".endsWith("ES6 methods")); // true

console.log("JavaScript ES6 methods".endsWith("ES6 method")); // false

```

When checking with a length parameter, the method tests only the first specified number of characters:

```javascript

console.log("TechOnTheNet".endsWith("on", 6)); // true

console.log("TechOnTheNet".endsWith("TechOnTheNet", 12)); // true

console.log("TechOnTheNet".endsWith("on", 3)); // false

```

The method can handle edge cases, returning true for empty string searches and false for shorter search strings:

```javascript

console.log("TechOnTheNet".endsWith("")); // true

console.log("TechOnTheNet".endsWith("TechOnTheNet", 17)); // false

```

For regular expressions, the method threw a TypeError in older implementations but is now supported in modern browsers:

```javascript

let str = "mystring#";

if (str.length > 0 && str[str.length - 1] === '#') {

    console.log("The string ends with '#'"); // true

}

```

When implementing the functionality in older browsers, developers can use native methods or polyfills. Modern implementations avoid unnecessary substring creation and provide efficient performance across different string lengths and browsers.


## Browser Support

The endsWith() method finds support across all modern browsers: Edge 12+, Firefox 17+, Chrome 41+, Safari 9+, and Opera 28+. This includes Safari on iOS 9+, Android Browser 136+, Chrome for Android 136+, and Firefox for Android 137+.

For older browsers, developers can implement the functionality using native methods or polyfills. The simplest approach is a standalone function that checks if the suffix is found at the end of the string using indexOf:

```javascript

function endsWith(str, suffix) {

    return str.indexOf(suffix, str.length - suffix.length) !== -1;

}

```

This works efficiently in modern browsers without creating unnecessary substrings. Current benchmarks show it performs similarly to the native implementation in Chrome, matches IE11's performance, and is only 4% slower in Firefox.

While native support has improved significantly since 2017, some older browsers still lack this functionality. Notably, Internet Explorer versions 6-10 and 11 do not support endsWith. Additionally, specific mobile browsers including Opera Mini, versions of Android Browser before 136, and older KaiOS browsers lack this feature.


## Polyfill Implementation

The endsWith() method has become available in all modern browsers since June 2017, with support in Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. However, for those still working with older browsers, several polyfill implementations are available to add this functionality.

The simplest standalone solution uses native JavaScript methods, checking if the suffix is found at the end of the string using indexOf:

```javascript

function endsWith(str, suffix) {

    return str.indexOf(suffix, str.length - suffix.length) !== -1;

}

```

This approach works efficiently in modern browsers without creating unnecessary substrings, performing similarly to the native implementation in Chrome and matching IE11's performance.

For developers who prefer a more comprehensive approach, a native method implementation can be added to the String prototype:

```javascript

String.prototype.endsWith = function (str) {

    return (this.length >= str.length) && (this.substr(this.length - str.length) === str);

}

```

Modern browsers handle this implementation well, and benchmarks show that while creating substrings isn't necessary, it doesn't significantly impact performance compared to the native method.

The polyfill can be tested for performance across different implementation approaches:

- `this.substr(-str.length) === str` (fastest on Chrome)

- `indexOf` (same performance on IE11)

- 4% slower than `indexOf` on Firefox

The chosen implementation should balance between efficiency and compatibility across all targeted browsers, with the native method providing optimal performance in modern environments.

