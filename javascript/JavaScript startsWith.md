---

title: JavaScript String startsWith() Method

date: 2025-05-27

---


# JavaScript String startsWith() Method

JavaScript's `startsWith()` method provides a concise way to check if a string begins with a specified substring, returning true or false accordingly. This built-in functionality offers several advantages over traditional methods like `indexOf()` or custom implementations, including improved readability and performance optimizations in modern JavaScript engines. The method's basic syntax and functionality make it particularly valuable for common tasks such as form validation and consistent string handling across different parts of an application. Understanding how to effectively use `startsWith()` and its optional parameters can significantly enhance code clarity and maintainability when working with string data in JavaScript applications.


## Introduction to startsWith()

The JavaScript `startsWith()` method determines whether a string begins with a specified substring, returning `true` or `false` accordingly. This built-in method offers a straightforward and efficient way to perform prefix checks, making it particularly useful for tasks like form validation and string manipulation.


### Method Syntax and Parameters

The method follows this syntax:

```javascript

string.startsWith(searchValue, start)

```

- `searchValue`: The substring to search for at the start of the string. This parameter is required and can be a single character or a longer string.

- `start` (optional): The position within the string where the search should begin. Defaults to `0`.


### Basic Usage

```javascript

const greeting = "Hello, world!";

console.log(greeting.startsWith("Hello")); // true

console.log(greeting.startsWith("world")); // false

console.log(greeting.startsWith("H", 2)); // false

```


### Case Sensitivity

The method is case-sensitive, treating uppercase and lowercase characters as distinct:

```javascript

const caseInsensitive = "Today is sunny.";

const search = "today";

const result = caseInsensitive.toLowerCase().startsWith(search.toLowerCase());

console.log(result); // true

```


### Position Parameter

The `start` parameter allows checking for substring presence at any specified position within the string:

```javascript

const sentence = "JavaScript is versatile!";

console.log(sentence.startsWith("is", 11)); // true

```


### Browser Support

The `startsWith()` method has been available since ECMAScript6, with full browser support across modern browsers:

- Chrome 41 and later

- Firefox 17 and later

- Safari 9 and later

- Edge all versions

- Opera 28 and later

Internet Explorer does not support this method. For compatibility with older browsers, developers can use either the native method with a polyfill or alternative string manipulation methods.


### Performance Considerations

The built-in `startsWith()` method generally provides better performance and readability compared to implementing similar functionality using `indexOf()`, `slice()`, or custom implementations. Modern JavaScript engines optimize string operations, making the native method a preferred choice for prefix checks.


## Syntax and Parameters

The `startsWith()` method determines if a string begins with a specified substring, returning a boolean value accordingly. This built-in method allows for case-sensitive prefix checking and accepts two parameters: `searchValue` and `position`.

The method signature follows this structure:

```javascript

string.startsWith(searchValue, start)

```

Here, `searchValue` represents the substring to search for at the beginning of the string. This parameter is required and can be a single character or a longer string.

The optional `start` parameter specifies the position within the string where the search should begin. If not provided, the default value is `0`, meaning the search starts at the beginning of the string.


### Method Parameters

The `searchValue` parameter defines the substring to search for at the start of the string. This can be a single character or a longer string, and the method is case-sensitive, treating uppercase and lowercase characters as distinct.

The `start` parameter is an optional position within the string where the search should begin. If not specified, the default value of `0` is used, indicating the search starts at the beginning of the string.


### Implementation Details

The method internally uses the value of `searchValue` to determine if it matches the start of the string. If the search string is not found or if the search starts at a specified position, the method returns `false`.

For position-based searches, the method examines the substring starting from the specified index. If the search string is found at the beginning of this substring, the method returns `true`; otherwise, it returns `false`.


### Performance Considerations

The `startsWith()` method provides an efficient way to check string prefixes. It performs this check in a time complexity of O(min(m, n)), where `m` is the length of the search string and `n` is the length of the target string.

This performance characteristic makes it particularly useful in scenarios where prefix matching needs to be performed frequently, as it avoids unnecessary full-string searches. Modern JavaScript engines optimize this method, making it a reliable choice for string manipulation tasks.


## Basic Usage

The basic usage of the `startsWith()` method follows a straightforward pattern: it checks if the current string begins with a specified substring and returns a boolean value based on this evaluation. This built-in method provides a clean and efficient way to perform prefix checks, making it particularly useful for tasks like form validation and string manipulation.

The method adheres to case sensitivity, meaning it treats uppercase and lowercase characters as distinct. For developers familiar with older JavaScript practices, this method offers an intuitive alternative to the `indexOf()` approach, as demonstrated in this comparison:

```javascript

const caseInsensitive = "Today is sunny.";

const search = "today";

const result = caseInsensitive.toLowerCase().startsWith(search.toLowerCase());

console.log(result); // true

```

Here, the method correctly identifies the prefix despite the original case difference, while providing the flexibility to perform case-insensitive checks through additional processing.

Developers can utilize the optional `start` parameter to perform position-based searches, checking if a substring matches at any specified location within the string. This functionality enables more complex string manipulations and conditional logic based on specific string patterns.

The native implementation of the method generally provides better performance and readability compared to alternative string manipulation techniques. Modern JavaScript engines further optimize this functionality, making it a robust choice for prefix checks in various applications.


## Performance Considerations

The built-in `startsWith()` method generally provides the best combination of performance and readability for prefix checks. Modern JavaScript engines optimize this method, making it efficient in most scenarios.

For testing with older JavaScript versions or environments without native support, developers can use the `slice()` method to extract the relevant portion of the string and compare it directly to the target substring:

```javascript

let s = 'Hello World';

let prefix = 'Hello';

if (s.slice(0, prefix.length) === prefix) {

  console.log('Prefix matches');

}

```

As an alternative, the `indexOf()` method can be used, particularly when existing codebase already employs this approach. This method returns the position of the first occurrence of the specified substring. If the substring is found at the beginning of the string, `indexOf()` will return 0:

```javascript

let s = 'Hello World';

let prefix = 'Hello';

if (s.indexOf(prefix) === 0) {

  console.log('Prefix matches');

}

```


### Custom Implementation

For developers needing to support extremely old environments or implementing custom string libraries, a loop-based approach offers flexibility:

```javascript

function startsWith(s, starter) {

  if (s.length < starter.length) return false;

  for (var i = starter.length - 1; (i >= 0) && (s[i] === starter[i]); --i) continue;

  return i < 0;

}

```


### Performance Comparison

A performance test comparing different implementations shows that the built-in `startsWith()` method generally outperforms custom solutions. The optimized loop implementation in the custom version provides better performance than basic approaches but remains less efficient than the native method.


### Cross-Language Considerations

The `startsWith()` functionality exists in similar forms across languages, with slight variations in implementation. For example, in Java, the method signature is:

```java

boolean startsWith(String prefix)

```

This allows checking if a string starts with a specific prefix, maintaining consistency with JavaScript's approach while providing additional flexibility through index parameters.


## Browser Support

The `startsWith()` method is a built-in JavaScript feature introduced in ECMAScript6 (ES6), making it available in modern browsers as of June 2017 in the following versions:

- Chrome 51

- Firefox 54

- Safari 10

- Edge 15

- Opera 38


### Browser Implementation

The method checks if a string begins with a specified substring, returning `true` if the condition is met and `false` otherwise. It supports case-sensitive comparisons and accepts an optional second parameter to specify the starting position for the search.


### Polyfill Implementation

For environments lacking native support, Mozilla provides an official polyfill:

```javascript

if (!String.prototype.startsWith) {

  String.prototype.startsWith = function(searchString, position) {

    position = position || 0;

    return this.indexOf(searchString, position) === position;

  };

}

```


### Performance Considerations

Performance tests show varying results across browsers. In Chrome 75, the native method performs as follows:

- Substring: 
0.08271 average

- Slice: 
0.08615 average

- LastIndexOf: 
0.77025 average

- IndexOf: 
1.64375 average

- StartsWith: 
3.5454 average

Firefox 67 results demonstrate similar patterns:

- IndexOf: 
0.1807 average

- Substring: 
0.08213 average

- Slice: 
0.08342 average

- LastIndexOf: 
0.7831 average

- StartsWith: 
3.55448 average

Browser performance differences highlight the importance of considering target environments when implementing string manipulation logic.

