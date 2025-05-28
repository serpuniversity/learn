---

title: JavaScript String.prototype.repeat() Method

date: 2025-05-26

---


# JavaScript String.prototype.repeat() Method

JavaScript's String.prototype.repeat() method provides an elegant way to concatenate string literals multiple times. However, its implementation includes important restrictions that developers must understand to avoid runtime errors. This article explores the method's behavior when passed non-positive integer values, highlighting the RangeError thrown by V8-based engines (Chrome, Node.js), Firefox, and Safari. Through detailed examples and cross-browser comparisons, we'll examine how to catch and handle these errors effectively.


## Method Overview

The repeat() method creates a new string by repeating a specified string a given number of times. The count parameter, which determines how many times the string is repeated, must be an integer between 0 and less than positive infinity. Non-integer values are converted to integers before processing.

The method throws a RangeError when the count argument is negative, indicating that the repeat count must be non-negative. This error applies to V8-based environments (Chrome, Node.js), Firefox, and Safari. The specific error message varies between browsers: Firefox reports "argument out of range" or "repeat count must be non-negative," while Chrome states "Invalid count value."

When the count is zero, the method returns an empty string. For positive integers, it simply repeats the string the specified number of times. If a non-integer value is provided, it is converted to an integer using the Math.floor() method before repetition occurs. This means that 3.9 will result in the same output as 3, while -1 will trigger the RangeError.


## Negative Count Error

The method throws a RangeError when the count argument is negative, indicating that the repeat count must be non-negative. This specific error type is documented in the JavaScript Error Handling series as occurring when using the repeat() method of a String object with a negative count parameter.

The error message varies between browsers: Firefox reports "argument out of range" or "repeat count must be non-negative," while Chrome states "Invalid count value." The error applies to V8-based environments (Chrome, Node.js), Firefox, and Safari.

When attempting to use the method with a negative count, the behavior across browsers is consistent - a RangeError is thrown. This can be demonstrated through basic examples where 'abc'.repeat(-1) throws a RangeError, while 'abc'.repeat(0) returns an empty string, and 'abc'.repeat(1) returns 'abc' as expected.


## Error Handling

Developers can catch and handle the RangeError using try-catch blocks, with specific error handling for negative count values. The error type is a RangeError object, which is inherited from the Error object. The error message varies between browsers: Firefox reports "argument out of range" or "repeat count must be non-negative," while Chrome states "Invalid count value."

For example, the following code demonstrates catching and handling this error using a printError function to format the error output:

```javascript

try {

  var count = -5;

  var name = 'Bob';

  name.repeat(count);

} catch (e) {

  if (e instanceof RangeError) {

    printError(e, true);

  } else {

    printError(e, false);

  }

}

```

In this example, attempting to repeat the string with a negative count will trigger the RangeError, which is caught by the catch block and formatted for output using the printError function.

The error message provides clear guidance that the repeat count must be non-negative. This information can be used in the catch block to prompt the developer to check the count value before calling the repeat method. The error is consistent across browsers and applies to V8-based environments (Chrome, Node.js), Firefox, and Safari, ensuring that developers can rely on similar error handling behavior regardless of the execution environment.


## Technical Details

The count parameter must be an integer between 0 and less than positive Infinity. The method converts non-integer values to integers before processing. This means that 3.9 will result in the same output as 3, while -1 will trigger the RangeError. The method handles other object types by converting them to integers before processing, so both negative integers and string representations of negative numbers will be caught by the error. For example, -5 and '-99' will both result in a RangeError.

The method's behavior is consistent across V8-based environments (Chrome, Node.js), Firefox, and Safari. It returns an empty string when the count is zero and repeats the string the specified number of times for positive integers. When attempting to use the method with a negative count, a RangeError is thrown with specific error messages varying between browsers: Firefox reports "argument out of range" or "repeat count must be non-negative," while Chrome states "Invalid count value."


## Browser Support

The negative count error applies to V8-based environments (Chrome, Node.js), Firefox, and Safari. The error manifests with specific messages across browsers: Firefox reports "argument out of range" or "repeat count must be non-negative," while Chrome states "Invalid count value."

The method handles count values through integer conversion before processing, meaning that both negative integers and string representations of negative numbers will trigger the RangeError. For example, attempting to repeat a string with either -5 or '-99' will result in a RangeError, as demonstrated in the provided documentation.

The error applies to a comprehensive range of invalid count values. Both negative integers and string representations of negative numbers will trigger the RangeError, ensuring consistent behavior across supported environments.

