---

title: JavaScript Time API: Understanding nanoseconds

date: 2025-05-27

---


# JavaScript Time API: Understanding nanoseconds

JavaScript's evolving Time API brings powerful new capabilities to date and time management, offering precision and reliability that previous solutions lacked. At the heart of this API is the concept of immutable temporal objects, which prevent the kind of subtle bugs that often plagued earlier date handling mechanisms. One of the most interesting features of these new objects is their ability to work with nanosecond precision, allowing developers to represent and manipulate time values with unprecedented accuracy.

This technical exploration delves deep into the nanosecond property of JavaScript's Temporal API, examining how it works across different time object types like PlainTime, ZonedDateTime, and PlainDateTime. We'll look at how to create and manipulate nanosecond values, including the limitations and complexities you might encounter when working with this experimental feature. For developers who need even more precision than the API provides, we'll also explore alternative solutions like the NanoTimer library and the performance.now() method, explaining when and why you might choose one approach over another.


## nanosecond Property Overview

The `nanosecond` property of Temporal objects returns an integer from 0 to 999 representing the nanosecond component of a time value. This feature is experimental and has limited availability across browsers. For instance, both `Temporal.ZonedDateTime` and `Temporal.PlanTime` include this property while `Temporal.PlainDateTime` also utilizes it (MDN Web Docs).

When creating a `Temporal.PlainTime` object, you can specify the nanosecond value directly through the constructor parameters. For example:

```javascript

let time = new Temporal.PlainTime(12, 34, 56, 0, 0, 789); // Represents 12:34:56.789

```

If you need to create a new `Temporal.PlainTime` object with a different nanosecond value, you can use the `with()` method:

```javascript

let time = Temporal.PlainTime.from("12:34:56");

let newTime = time.with({ nanosecond: 100 });

console.log(newTime.toString()); // Output: 12:34:56.0000001

```

JavaScript provides alternative timing solutions for developers who require more precise measurements than what the `Temporal` API offers. The `performance.now()` method returns a DOMHighResTimeStamp measured in milliseconds, offering sub-millisecond resolution. However, while this method provides improved accuracy over previous millisecond-based APIs, its minimum resolution is typically set to no less than 5 microseconds due to architectural and software constraints (MDN Web Docs).

For applications requiring even higher precision, developers may consider libraries like NanoTimer or process.hrtime(). These tools can offer more granular time measurements beyond what is available through the Temporal API or performance.now().


## Setting and Changing Nanoseconds

The `Temporal.PlainTime` constructor allows for precise specification of time components, including nanoseconds. When creating a new time object, you can directly set the nanosecond value through the constructor parameters:

```javascript

let time = new Temporal.PlainTime(12, 34, 56, 0, 0, 789); // Creates 12:34:56.789

```

Alternatively, you can create a `Temporal.PlainTime` object and then use the `with()` method to change the nanosecond value:

```javascript

let time = Temporal.PlainTime.from("12:34:56");

let newTime = time.with({ nanosecond: 100 });

console.log(newTime.toString()); // Output: 12:34:56.0000001

```

For `Temporal.ZonedDateTime` objects, the same principle applies. You can either create a new zoned time with the desired nanosecond value:

```javascript

let zonedDateTime = Temporal.ZonedDateTime.from("2023-02-25T12:34:56.789+08:00[Asia/Shanghai]");

console.log(zonedDateTime.toString()); // Output: 2023-02-25T12:34:56.789+08:00[Asia/Shanghai]

```

Or modify an existing zoned time using the `with()` method:

```javascript

let newZonedDateTime = zonedDateTime.with({ nanosecond: 100 });

console.log(newZonedDateTime.toString()); // Output: 2023-02-25T12:34:56.0000001+08:00[Asia/Shanghai]

```

The `Temporal.PlainTime.prototype.add` method can also be used to change the nanosecond value by adding or subtracting a duration:

```javascript

let time = Temporal.PlainTime.from("12:34:56");

let newTime = time.add({ nanoseconds: 100 });

console.log(newTime.toString()); // Output: 12:34:56.0000001

```

The `Temporal.Duration.prototype.nanoseconds` accessor property provides information about the duration in nanoseconds. While you cannot directly change this property, you can create new `Temporal.Duration` objects with modified values using the `with()` method:

```javascript

const d1 = Temporal.Duration.from({ microseconds: 1, nanoseconds: 500 });

const d2 = Temporal.Duration.from({ microseconds: -1, nanoseconds: -500 });

const d3 = Temporal.Duration.from({ microseconds: 1 });

const d4 = Temporal.Duration.from({ nanoseconds: 1000 });

console.log(d1.nanoseconds); // 500

console.log(d2.nanoseconds); // -500

console.log(d3.nanoseconds); // 0

console.log(d4.nanoseconds); // 1000

// Create balanced duration

const d4Balanced = d4.round({ largestUnit: "microseconds" });

console.log(d4Balanced.nanoseconds); // 0

console.log(d4Balanced.microseconds); // 1

```


## nanosecond Property Implementation

The `nanosecond` property is an integral component of temporal objects within JavaScript's Time API, providing access to the precise nanosecond value of a given time instance. As part of the Temporal.PlainTime prototype, this immutable accessor returns an integer between 0 and 999, representing the nanosecond component of the time.

Implementation of the `nanosecond` property follows similar patterns across various temporal objects. For example, Temporal.ZonedDateTime and Temporal.PlainDateTime both expose this property through their respective prototypes. When modifying the nanosecond value, developers must use the `with()` method to create a new temporal object instance, rather than attempting to change the existing property directly.

The browser compatibility for nanosecond access is limited, with the feature being classified as experimental and not Baseline. Compatibility details vary across different temporal object types - while Temporal.ZonedDateTime supports direct access via the `nanosecond` property, Temporal.PlainDateTime requires modifications through the `with()` method to change the value. This limitation applies across multiple browsers, though the feature works consistently in some environments.

JavaScript developers seeking higher precision timing capabilities have several alternative solutions beyond the `Temporal` API. The `performance.now()` method provides high-resolution timestamps suitable for most timing requirements, though its precision varies based on browser implementation (typically between 5 and 100 microseconds). For applications needing even greater accuracy, the NanoTimer library offers a robust solution, implementing high-resolution timers using Node.js's built-in `process.hrtime()` functionality. The latest version of NanoTimer includes enhancements for improved performance and logging capabilities, making it a viable alternative to native JavaScript timing methods.


## Alternative Timing Solutions

For applications requiring timing precision beyond what JavaScript's built-in methods provide, developers have several robust alternatives. The most widely-used library for this purpose is NanoTimer, which specifically addresses the shortcomings of standard JavaScript timing functions. This library can be installed via npm with the command `npm install nanotimer`.

NanoTimer reimplements core JavaScript timing functions using Node.js's built-in `process.hrtime()` functionality, which measures high-resolution time intervals. The library provides several key features:

- Clear interval and timeout management

- Enhanced logging capabilities for debugging

- Improved performance through optimized interval handling

- Compatibility with Node.js v0.10.13 and later versions

The library handles timing tasks through concrete timer objects that manage individual setTimeout and setInterval operations without requiring complex reference tracking. Implementation examples demonstrate both function object and function declaration methods for timing tasks.

While JavaScript's `performance.now()` method offers sub-millisecond resolution through the DOMHighResTimeStamp interface, it has limitations. This method returns the time elapsed since a known origin time, making it unsuitable for obtaining UTC timestamps. The minimum resolution provided by this API is typically 5 microseconds, with UA-specific adjustments possible due to architectural and security constraints.

For systems requiring even higher precision, developers can explore additional npm packages like timestamp-nano, which provides nanosecond timestamp functionality. However, it's important to note that native methods like `Date.now()` with simple string concatenation (`Date.now() + "000000"`) only provide millisecond-level accuracy, falling short of the required 4-digit precision (microseconds or better).

Developers implementing high-precision timing solutions should carefully consider browser compatibility and performance implications. While NanoTimer significantly improves upon standard JavaScript timing mechanisms, developers must still account for subtle variations in platform-specific implementations of high-resolution timing functions.


## Temporal API Fundamentals

The Temporal API represents a significant advancement in JavaScript's date and time management capabilities, addressing numerous limitations of the traditional Date object introduced in 1995. Unlike the mutable Date objects that can lead to subtle bugs in complex applications, Temporal introduces immutable time types that prevent accidental modification of time values.

The API resolves key issues with the Date object through several architectural improvements. For instance, it eliminates ambiguity in date parsing through strict string formats, ensuring consistent interpretation across different environments. It also extends time zone handling to be fully integrated within the API, reducing dependency on external libraries and manual adjustments.

At its core, the Temporal API provides a comprehensive set of fundamental types for date and time representation:

1. **PlainDate**: Represents calendar dates without associated times or time zones.

2. **PlainTime**: Represents specific times of day without dates or time zones.

3. **PlainDateTime**: Combines calendar dates and wall-clock times into a single object.

4. **Instant**: Represents precise points in UTC time with nanosecond resolution.

5. **ZonedDateTime**: Represents dates and times with associated time zones, enabling precise time zone calculations.

All Temporal types include string representations for persistence and interoperability, with strict correspondences between machine-readable strings and their object forms. The API supports multiple calendar systems beyond the Gregorian calendar, making it suitable for applications requiring historical or cultural date calculations.

As of 2025, the Temporal API has achieved broad browser support, though polyfills like proposal-temporal can be used in environments where native support is unavailable. The API's design balances practical usability with strict adherence to time-related standards, providing developers with powerful tools for date and time management while maintaining backward compatibility with existing JavaScript applications.

