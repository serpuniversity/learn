---

title: JavaScript String fontsize() Method

date: 2025-05-26

---


# JavaScript String fontsize() Method

The `fontsize()` method in JavaScript offers a straightforward way to apply different font sizes to text strings by returning a string wrapped in a `<font>` tag. Although this functionality has been part of JavaScript since version 1.0, its reliance on the `<font>` tag, which was removed from HTML5, makes it increasingly irrelevant for modern web development. This article examines the method's definition, usage, and technical specifications while emphasizing the importance of adopting CSS for font styling in contemporary web standards.


## Definition and Usage

The `fontsize()` method in JavaScript returns a string embedded in a `<font>` tag with the specified size. It takes a single parameter, `size`, which must be an integer between 1 and 7, or a string representing a signed integer between 1 and 7. For example:

```javascript

let str = "Hello, World!";

console.log(str.fontsize(3)); // Output: <font size="3">Hello, World!</font>

```

The method creates an HTML `<font>` element with the specified size attribute. This functionality is intended to allow strings to be displayed with different sizes, similar to using the `<font size="size">` tag directly in HTML. However, due to its reliance on the `<font>` tag, which has been removed from HTML5, this method is no longer recommended for new development.

The method works by concatenating the `<font size="size">` tag with the input string and returning the resulting string. Here's a more detailed example demonstrating its usage:

```javascript

let str1 = "This is a test string.";

let str2 = "Another string with a larger font size.";

console.log(str1.fontsize(2)); // Output: <font size="2">This is a test string.</font>

console.log(str2.fontsize(5)); // Output: <font size="5">Another string with a larger font size.</font>

```

The `fontsize()` method has been part of JavaScript since version 1.0 and continues to function in current implementations. However, its use is discouraged due to the `<font>` tag's removal from HTML5. For modern web development, CSS properties should be used instead for font styling.


## Syntax and Parameters

The `fontsize()` method is called on a string instance using the syntax `string.fontsize(size)`. The `size` parameter can be either a numeric value between 1 and 7, or a string representing a signed integer within the same range.

When invoked with a numeric parameter, the method generates an HTML `<font>` element with the specified size attribute. For example:

```javascript

var str = "Hello, World!";

console.log(str.fontsize(4)); // Output: <font size="4">Hello, World!</font>

```

The method supports relative font sizes as well, using the '+' and '-' notation. For instance:

```javascript

var str = "TechOnTheNet";

console.log(str.fontsize('+1')); // Output: <font size="+1">TechOnTheNet</font>

console.log(str.fontsize('-2')); // Output: <font size="-2">TechOnTheNet</font>

```

The method returns a string containing the `<font>` element, effectively embedding the original string with the specified size. It's important to note that while this method has been standardized for compatibility purposes, its use is strongly discouraged due to the removal of the `<font>` element from the HTML5 specification. Modern web development should rely on CSS properties for font styling.


## Size Range and Values

The size parameter accepts integers between 1 and 7, or strings representing signed integers within the same range. When an integer is provided, it directly sets the font size to one of the seven predefined levels. Positive integers increase the font size, with 7 being the largest and 1 the smallest, while 3 represents the default size.

For example, when passing 4 as the size parameter, the resulting HTML will have a <font size="4"> tag applied to the string. Similarly, passing -2 will adjust the font size relative to the default size of 3, effectively making the text 1 point smaller.

The method also supports relative font sizes using the '+' notation. For instance, providing '+1' as the size will increase the font size by one level, while '-2' will decrease it by two levels. This allows for flexible adjustments based on the existing font size context.


## Deprecated Status and Future

The `fontsize()` method is deprecated and may no longer function in future browsers. As of 2026, ECMAScript language specifications include `sec-string.prototype.fontsize` but warn that the method only maintains this standardization for compatibility purposes. Developers are explicitly instructed to use CSS properties instead of relying on this deprecated functionality.

This deprecation applies to all valid uses of the method, including both numeric values (1-7) and relative values ('+1', '-2'). The method's removal from the HTML5 specification means that relying on `<font size="...">` elements for text styling is no longer supported in modern web development.

The method's status as deprecated impacts its reliability across different browsers and versions. While currently supported in JavaScript versions 1.0 and later, developers should expect potential removal or non-functional behavior in future releases. This limitation affects both new development and existing codebases that continue to use the method, making CSS a more reliable choice for implementing font size changes.

