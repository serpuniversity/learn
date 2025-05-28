---

title: JavaScript Date Reference: now() Method

date: 2025-05-26

---


# JavaScript Date Reference: now() Method

JavaScript's Date object provides essential functionality for working with dates and times in web applications. This reference guide focuses on the now() method, which returns the current timestamp in milliseconds since the Unix epoch. While seemingly simple, now() offers several important considerations, including its implementation details, precision control for privacy, and efficient time measurement capabilities compared to alternative methods like the Date constructor. Through detailed examples and practical applications, we'll explore how to effectively use now() for generating unique identifiers, measuring performance, and understanding JavaScript's date and time utilities.


## now() Method Overview

The now() method returns the current timestamp in milliseconds since January 1, 1970, 00:00:00 UTC, as defined by the ECMAScript standard. Each call to Date.now() results in a difference of half a second or more between calls due to the rapid passage of milliseconds. This method is particularly efficient for capturing the current time, as demonstrated in examples where it's used to measure performance and create unique identifiers.

The method's precision can be reduced to protect against timing attacks and fingerprinting, with Firefox implementing a default setting of 2 milliseconds of reduced precision when the privacy.resistFingerprinting preference is enabled. When this preference is active, the precision is further limited to either 100 milliseconds or the value of privacy.resistFingerprinting.reduceTimerPrecision.microseconds, whichever is larger.

The output of Date.now() is always a multiple of 2 milliseconds in Firefox 60, and a multiple of 100 milliseconds or the specified microsecond value when privacy.resistFingerprinting is enabled. This makes it suitable for scenarios requiring reduced precision while maintaining compatibility with older implementations. For precise time measurements, developers are encouraged to use the Performance.now() method from the JavaScript performance API, which offers higher resolution timing capabilities.


## Generating Timestamps

The Date.now() method returns the current timestamp in milliseconds since January 1, 1970, making it an ideal choice for generating unique identifiers and measuring performance. A practical use case demonstrates capturing the current timestamp to log event times: let currentTimestamp = Date.now(); console.log("The current time in milliseconds is: " + currentTimestamp);

Developers can measure elapsed time between two points in code using the following approach: const startTime = Date.now(); executeTask(); const endTime = Date.now(); console.log(`Task execution took ${endTime - startTime} milliseconds.`);

The method's efficiency is further illustrated in a performance benchmark comparing it to creating a new Date object: let start = Date.now(); // measure start time for a loop or task let end = Date.now(); // measure end time console.log(`The operation took ${end - start} milliseconds.`);

For applications requiring precise elapsed seconds, developers should utilize Math.floor(Date.now() / 1000) to ensure only actual elapsed seconds are returned, as per the ECMAScript 2026 Language Specification.

The method's compatibility across browsers demonstrates its reliability for cross-platform development, with initial support dating back to July 2015. Firefox implements reduced precision by default with a setting of 2 milliseconds, while enabling privacy.resistFingerprinting limits the precision to either 100 milliseconds or the value of privacy.resistFingerprinting.reduceTimerPrecision.microseconds, whichever is larger. This precision reduction helps protect against timing attacks and fingerprinting while maintaining practical usability for most applications.


## Comparing Date Constructors

The Date.now() method returns the current timestamp in milliseconds since January 1, 1970, while the new Date() constructor returns a Date object representing the current date and time. Each call to Date.now() results in a difference of half a second or more between calls due to the rapid passage of milliseconds. In contrast, the new Date() constructor returns a Date object that can be manipulated using various methods to retrieve or set date components.

A practical example demonstrates the difference between the two methods: let startTime = Date.now(); let dateObject = new Date(); console.log(`The current timestamp is: ${startTime}`); console.log(`The current date object is: ${dateObject}`); This code first captures the current timestamp, then creates a Date object representing the current date and time.

The Date.now() method provides a static method of the Date object without creating a new date instance, making it particularly efficient for capturing the current time or measuring performance. It returns a number representing milliseconds since the Unix epoch, as demonstrated in this usage example: const timestamp = Date.now(); console.log(`The current time in milliseconds is ${timestamp}`); The console output represents the number of milliseconds elapsed since the epoch.

The new Date() constructor can be called with no arguments to return the current date and time as a Date object, with methods available for various date components. This constructor offers powerful functionality for date and time manipulation, including methods to retrieve year, month, day, hour, minute, second, and millisecond information. While Date.now() provides a simple method for capturing current time, new Date() offers comprehensive functionality for date and time management in JavaScript applications.


## Date Manipulation with now()

The Date.now() method provides a foundation for precise time measurements in JavaScript, offering developers a direct way to access the current timestamp. By comparing it with the new Date() constructor, we can see how these two methods serve different purposes in date and time manipulation.

For instance, while the new Date() constructor generates a Date object representing the current date and time, it requires additional processing to extract specific components or calculate differences. This can be demonstrated with the following code snippet:

JavaScript

```javascript

let startTime = new Date().getTime();

// execute task

let endTime = new Date().getTime();

console.log(`Task execution took ${endTime - startTime} milliseconds.`);

```

In contrast, the Date.now() method achieves the same result with greater efficiency:

JavaScript

```javascript

let startTime = Date.now();

// execute task

let endTime = Date.now();

console.log(`Task execution took ${endTime - startTime} milliseconds.`);

```

The performance difference becomes more apparent in scenarios requiring frequent time measurements, as the Date.now() method avoids the overhead of constructing a full Date object.

To illustrate more complex time calculations, let's examine how to measure elapsed time using both methods:

```javascript

function printElapsedTime(testFn) {

  const startTime = Date.now();

  const result = testFn();

  const endTime = Date.now();

  console.log(`Elapsed time: ${String(endTime - startTime)} milliseconds`);

  return result;

}

```

This function demonstrates the practical application of Date.now() for performance measurement, providing developers with a clear example of how to implement precise time tracking in their code.

The compatibility and support for Date.now() across browsers also make it a reliable choice for cross-platform development. As noted in the documentation, the method has been supported since July 2015, with implementations ensuring consistent returns of milliseconds since the Unix Epoch. The precision of these returns can be adjusted based on privacy settings, further enhancing its versatility for different application requirements.


## Understanding Timestamps

The JavaScript Date object represents a single moment in time in a platform-independent format, storing an integral number of milliseconds since the midnight at the beginning of January 1, 1970, UTC (the epoch). This epoch is timezone-agnostic and uniquely defines an instant in history. The object supports timestamps up to ±8,640,000,000,000,000 milliseconds, which covers from April 20, 271821 BC to September 13, 275760 AD. Any attempt to represent a time outside this range results in the Date object holding a timestamp value of NaN, which is an "Invalid Date."

The object stores its timestamp in UTC but provides methods to work with local time zones and offsets. Basic date and time methods return information in the local time zone. For example, getFullYear() returns the full year (4 digits), getMonth() returns the month as a number (0-11), and getDate() returns the day as a number (1-31). There are corresponding UTC methods (getUTCFullYear(), getUTCMonth(), getUTCDate()) that return values for the UTC+0 time zone.

To create a new Date object, you can use the `new` keyword with `new Date()`, which returns the current date and time in the local timezone. You can also pass individual date and time components as arguments to the constructor, in the order: Year (2023), Month (8 - representing August), Day (10), Hour (23), Minute (15), Second (34), and Millisecond (0). The constructor behaves differently based on the number of arguments provided, allowing for various date and time specifications.

The Date object provides several methods for interacting with the timestamp:

- `getTime()` returns the timestamp in milliseconds since the epoch

- `setTime(milliseconds)` directly manipulates the timestamp value

- `valueOf()` and `[Symbol.toPrimitive]()` (when passed "number") return the timestamp, allowing `Date` objects to behave like their timestamps when used in number coercion

JavaScript's Date object serves as a standard for computing date and time in applications ranging from financial to office and social applications. While libraries like Moment.js offer extensive functionality including timezone handling and formatting options, the native Date object remains fundamental for basic date and time operations in JavaScript.

