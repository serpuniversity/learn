---

title: JavaScript Reference & Tutorial: Instant > epochMilliseconds

date: 2025-05-27

---


# JavaScript Reference & Tutorial: Instant > epochMilliseconds

JavaScript's Date.now() method provides the current time as a numeric value representing milliseconds since the Unix epoch. This numeric representation enables precise time measurement and calculation in web applications. Understanding how to work with epoch milliseconds is crucial for developers needing to synchronize JavaScript time with other systems or perform time-based operations. This guide explores the most effective methods for obtaining and working with epoch milliseconds in JavaScript, including compatibility considerations for older browsers and advanced techniques from the ECMAScript Temporal API.


## Introduction to JavaScript's Epoch Time

JavaScript provides multiple methods to retrieve the current time in milliseconds since the Unix epoch. The most common approach is through the `Date.now()` method, which returns the number of milliseconds since the Unix epoch, making it the preferred way to get the current time in JavaScript.

For compatibility with older browsers, specifically Internet Explorer 8 and earlier, developers can construct a Date object and use one of the following methods: `+new Date`, `getTime()`, or `valueOf()`. These methods all return the number of milliseconds since the Unix epoch. While these approaches are supported across browsers, standard Unix epoch timestamps are typically expressed in seconds, with JavaScript's value being one-thousandth of that format.

The Text Summary notes that the `Date.now()` method has been supported across browsers since July 2015 and works reliably across many devices and browser versions. It is recommended for obtaining the current time in milliseconds. When working with date objects, developers can measure time spans by subtracting two subsequent `getTime()` calls on newly generated Date objects, as shown in the provided example code. For precise measurements requiring higher resolution than milliseconds, modern browsers support the Performance API's `Performance.now()` method, though `Date.now()` remains widely compatible.


## Using Date.now() for Current Time

The `Date.now()` method returns the number of milliseconds elapsed since the Unix epoch, defined as midnight at the beginning of January 1, 1970, UTC. This makes it the preferred method for obtaining the current time in JavaScript.

For compatibility with older browsers, specifically Internet Explorer 8 and earlier, developers can construct a Date object and use one of the following methods: `+new Date`, `getTime()`, or `valueOf()`. These methods all return the number of milliseconds since the Unix epoch.

JavaScript's `Date.now()` method has been supported across browsers since July 2015 and works reliably across many devices and browser versions. Modern browsers also support the Performance API's `Performance.now()` method for more precise measurements, though `Date.now()` remains widely compatible.

The method's precision can be reduced in Firefox through the `privacy.resistFingerprinting` setting. When enabled, this setting reduces the output to a multiple of 100 milliseconds or the specified microsecond value.

The time value returned by `Date.now()` can be converted to other time units using simple arithmetic operations. To get the current time in seconds, developers should use `Math.floor(Date.now() / 1000)` instead of `Math.round()` to ensure integer values are returned.


## Epoch Time in JavaScript and Web Browsers

The JavaScript Date object represents a single moment in time in a platform-independent format, encapsulating an integral number of milliseconds since the epoch, which is defined as midnight at the beginning of January 1, 1970, UTC. This system uniquely defines an instant in history, with the time value being in UTC and the maximum timestamp representable by a Date object being slightly smaller than Number.MAX_SAFE_INTEGER (9,007,199,254,740,991).

JavaScript provides multiple methods to retrieve the current time in milliseconds since the epoch. The most common approach is through the `Date.now()` method, which returns the number of milliseconds since the epoch and has been supported across browsers since July 2015. For compatibility with older browsers, specifically Internet Explorer 8 and earlier, developers can construct a Date object and use methods like `+new Date`, `getTime()`, or `valueOf()`, all of which return the number of milliseconds since the epoch.

Modern browsers support the Performance API's `Performance.now()` method for more precise measurements, though `Date.now()` remains widely compatible. In Firefox, the output precision of `Date.now()` can be reduced for security reasons, with the default setting being 2 milliseconds and the maximum reduction set by the `privacy.resistFingerprinting.reduceTimerPrecision.microseconds` value.

While JavaScript provides the epoch time in milliseconds, standard Unix epoch timestamps are typically expressed in seconds, with JavaScript's value being one-thousandth of that format. This relationship between JavaScript's `Date.now()` method and Unix epoch timestamps is crucial for developers working across different programming environments and standards.


## Temporal API and epochMilliseconds

The ECMAScript Temporal API introduces the epochMilliseconds property and method, which provide precise time measurement capabilities. The epochMilliseconds property returns the number of milliseconds since January 1, 1970, 00:00:00 UTC, making it a valuable addition to JavaScript's time measurement tools.

Here's how you can use the epochMilliseconds property and method:

```javascript

const instant2 = Temporal.Instant.from("1969-08-01T12:34:56.789Z");

console.log(instant2.epochMilliseconds); // -13173903211

const instant = Temporal.Instant.from("2021-08-01T12:34:56.789Z");

const instant1hourLater = instant.add({ hours: 1 });

console.log(instant1hourLater.epochMilliseconds); // 1627824896789

const instant = Temporal.Instant.from("2021-08-01T12:34:56.789Z");

const instant1hourLater = Temporal.Instant.fromEpochMilliseconds(

  instant.epochMilliseconds + 3600000

);

console.log(instant1hourLater.epochMilliseconds); // 1627824896789

```

The method's constraints include:

- The epochMilliseconds value cannot be converted to a BigInt and must remain an integer

- The value must be within the representable range: ±108 days (approximately ±273,972.6 years) from the Unix epoch

When working with the Temporal API's epochMilliseconds, keep the following in mind:

- The property is read-only and returns the number of milliseconds since the Unix epoch, truncated toward the beginning of time

- The value is suitable for interfacing with systems that use milliseconds since epoch

- The epochNanoseconds property provides higher precision (nanosecond level), while the epochMilliseconds property offers compatibility with systems expecting milliseconds


## Working with Epoch Time

The JavaScript Date object can represent a moment in time as an integral number of milliseconds since the Unix epoch, defined as midnight at the beginning of January 1, 1970, UTC. This platform-independent format uniquely defines an instant in history, with the time value representing Coordinated Universal Time (UTC). The maximum timestamp representable by a Date object is slightly smaller than Number.MAX_SAFE_INTEGER (9,007,199,254,740,991), allowing timestamps from April 20, 271821 BC to September 13, 275760 AD.

To convert between date objects and epoch timestamps, developers can use the following methods:

- `let date = new Date();` creates a Date object representing the current date and time.

- `let totalMilliseconds = date.getTime();` retrieves the number of milliseconds since the epoch.

- `let secondsSinceEpoch = Math.floor(totalMilliseconds / 1000);` converts milliseconds to seconds.

- `let daysSinceEpoch = Math.floor(secondsSinceEpoch / 86400);` converts seconds to days.

When working with different time zones, JavaScript's Date objects represent the local time zone of the device running the JavaScript. To ensure UTC calculations, developers should explicitly convert local date objects to UTC using methods like `date.getTimezoneOffset()` for time zone conversion calculations.

The `Date.now()` method returns the number of milliseconds since the epoch and is supported across browsers since July 2015. For precise measurements requiring higher resolution than milliseconds, modern browsers support the Performance API's `Performance.now()` method. When measuring time intervals, developers should use `Math.floor()` instead of `Math.round()` to ensure integer values are returned, as demonstrated in the example code: `console.log(`Elapsed time: ${String(endTime - startTime)} milliseconds`);`

JavaScript's `Date` objects behave like their timestamp values when used in number coercion, allowing for direct arithmetic operations with the underlying time value. For example, to create a new Date object with the same time value as an existing one, developers can use `const copy = new Date(originalDate.getTime());`. To measure time spans between Date objects, developers can subtract the `getTime()` values of two Date objects: `const elapsed = end.getTime() - start.getTime();`.

When working with legacy systems that use second-based epoch timestamps, JavaScript developers should note that standard Unix epoch timestamps are typically expressed in seconds, with JavaScript's value being one-thousandth of that format. To convert between these systems, remember to multiply Unix epoch seconds by 1000 before using them with JavaScript's Date methods: `const javascriptTimestamp = unixSecondTimestamp * 1000;`

