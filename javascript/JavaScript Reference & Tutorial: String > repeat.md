---

title: JavaScript String repeat() Method

date: 2025-05-27

---


# JavaScript String repeat() Method

The JavaScript string repeat() method, introduced in ECMAScript 6, provides an efficient way to concatenate a string multiple times. While the native implementation offers broad compatibility and performance advantages in modern browsers, developers must account for cross-browser differences and potential limitations. Understanding the method's behavior, performance characteristics, and available implementations is crucial for effective string manipulation in JavaScript applications.


## Introduction to String Repeat

The `repeat()` method is a native JavaScript feature introduced in ECMAScript 6 (ES6), also known as JavaScript 2015. This method returns a new string comprised of the original string repeated a specified number of times. For example, `"abc".repeat(3)` results in `"abcabcabc"`.

Key aspects of the native implementation include support across modern browsers (Edge, Firefox, Chrome, Safari) since June 2017, with Internet Explorer being the notable exception. The method accepts an integer parameter `_count_`, which determines how many times the string should be repeated. Zero results in an empty string, while non-integer values are automatically rounded to the nearest integer. Negative counts or values exceeding the maximum string length constraints (2^30 characters in Chrome and Firefox) result in a RangeError.

When using the native implementation, developers must consider cross-browser compatibility. While the method is well-supported in modern browsers, projects targeting older versions of Internet Explorer or specific mobile devices may need to implement alternative solutions. The provided polyfill demonstrates one approach, utilizing `Array.prototype.join()` to achieve string repetition across all browsers:

```javascript

String.prototype.repeat = String.prototype.repeat || function(n) {

  if (n < 0) throw new RangeError("invalid count value");

  if (n == 0) return "";

  return new Array(n + 1).join(this.toString());

};

```

This implementation handles basic functionality but requires exception handling for invalid count values, as noted in the MDN documentation. For more complex use cases involving fractional counts or very long strings, developers may need to implement additional logic to maintain optimal performance across different browser versions.


## Native String.repeat Method

As of June 2017, the native `String.prototype.repeat` method has achieved widespread browser compatibility across modern platforms, including Chrome 51, Edge 15, Firefox 54, Opera 38, and Safari 10. The method's syntax, _string_.repeat(_count_), accepts a single integer parameter to determine the number of string copies returned.

The native implementation handles several edge cases:

- A count of 0 returns an empty string

- Non-integer counts are automatically rounded to the nearest integer

- Negative counts or values exceeding browser-specific length limits (2^30 characters in Chrome and Firefox) result in a RangeError

The method's performance varies across browsers. Benchmarks demonstrate that modern browser implementations, particularly in Chrome and Safari, outperform alternative approaches using loops and array methods. For developers targeting Internet Explorer or older browsers, the native implementation is not available and alternative polyfills must be used. Current recommendations from MDN and web development standards suggest developers leverage the native implementation where possible, given its efficient performance and cross-browser compatibility.


## Alternative Implementations

The text presents multiple approaches to string repetition in JavaScript, ranging from simple implementations to optimized solutions. For modern browsers supporting the native `repeat()` method, the basic implementation works as follows:

```javascript

String.prototype.repeat = String.prototype.repeat || function(n) {

  if (n < 0) throw new RangeError("invalid count value");

  if (n == 0) return "";

  return new Array(n + 1).join(this.toString());

};

```

This approach creates an array of the specified length and joins its elements into a string. While effective for modern browsers, this method's performance varies across implementations. Chrome and Safari demonstrate superior performance compared to Firefox when using concatenation loops:

```javascript

for (let i = 0; i < 10; i++) {

  result += "a";

}

```

However, this loop-based approach becomes less efficient as the number of repetitions increases. Modern optimizations, such as the bitwise approach:

```javascript

String.prototype.repeat = function(count) {

  if (count < 1) return '';

  var result = '', pattern = this.valueOf();

  while (count > 1) {

    if (count & 1) result += pattern;

    count >>= 1, pattern += pattern;

  }

  return result + pattern;

}

```

Show significant improvements, particularly for larger values of count. This optimized implementation reduces the number of iterations and demonstrates performance gains when compared to simpler approaches:

```javascript

function repeat(s, n){

    var a = [];

    while(a.length < n){

        a.push(s);

    }

    return a.join('');

}

```

The performance-optimized version shows approximately twice the performance of the original implementation in Firefox, and nearly four times the performance in Chrome. These benchmarks highlight the importance of efficient string manipulation techniques when working with large data sets or performance-critical applications.


## Best Practices and Performance

Developers targeting modern browsers can leverage the native `repeat()` method for efficient string repetition. For applications requiring performance optimization across different browser versions, several alternative implementations are available. The bitwise-optimized approach demonstrates significant performance benefits, particularly for large values of count:

```javascript

function repeat(s, n) {

    var result = '';

    while (n > 0) {

        if (n & 1) result += s;

        n >>= 1;

        s += s;

    }

    return result;

}

```

This implementation consistently outperforms simpler approaches, demonstrating approximately twice the performance in Firefox and nearly four times the performance in Chrome compared to basic concatenation loops.

For developers working with older browser versions, the array-based approach remains effective while maintaining good performance. The optimized version combining bitwise operations and array joining demonstrates the best balance of efficiency and readability:

```javascript

function repeat(s, n) {

    var result = '', pattern = s;

    while (n > 1) {

        if (n & 1) result += pattern;

        n >>= 1;

        pattern += pattern;

    }

    return result + pattern;

}

```

While modern browsers achieve near-constant performance for string repetition, developers must account for browser-specific limitations. Chrome and Firefox enforce a maximum string length of approximately 2^30 characters, while IE versions prior to Edge support are not compatible with any JavaScript string manipulation technique. Future developments in ECMAScript standards may introduce additional optimizations, but current best practices prioritize modern browser compatibility and efficient implementation strategies.


## Handling Edge Cases

The native `String.prototype.repeat` method handles several edge cases gracefully. It returns an empty string when a count of 0 is provided and automatically converts non-integer count values to the nearest integer. Negative count values trigger a RangeError, ensuring developers receive explicit feedback when attempting invalid operations.

For developers working with older browser versions, the polyfill implementation maintains consistent behavior across different environments. The function-based approach provides a robust alternative:

```javascript

function repeat(str, count) {

  if (count < 0) throw new RangeError("invalid count value");

  if (count == 0) return "";

  var result = '';

  var pattern = str;

  while (count > 1) {

    if (count & 1) result += pattern;

    count >>= 1;

    pattern += pattern;

  }

  return result + pattern;

}

```

This custom implementation addresses key performance considerations, demonstrating improved efficiency over basic concatenation approaches while maintaining compatibility with Internet Explorer and other legacy browsers.

String length limitations vary across browsers. Current implementations approach a maximum of approximately 2^30 characters (1 billion characters) in Chrome and Firefox, while older versions or specific environments may enforce lower limits. Developers can determine the maximum string length for their environment using the provided script:

```javascript

for (var startPow2 = 1; startPow2 < 9007199254740992; startPow2 *= 2) {

  try {

    " ".repeat(startPow2);

  } catch(e) {

    break;

  }

}

var floor = Math.floor, mask = floor(startPow2 / 2);

while (startPow2 = floor(startPow2 / 2)) {

  try {

    " ".repeat(mask + startPow2);

    mask += startPow2;

  } catch(e) {}

}

console.log("The max string length for this browser is " + mask);

```

This script determines the maximum available length, allowing developers to implement appropriate safeguards against potential overflow errors. The browser compatibility list maintained by MDN Web Docs provides detailed support information, highlighting the method's availability across major browser versions since September 2015.

