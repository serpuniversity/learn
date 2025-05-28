---

title: Temporal.PlainTime: Comparison Methods

date: 2025-05-27

---


# Temporal.PlainTime: Comparison Methods

JavaScript's Temporal API introduces powerful new methods for working with time, including specialized comparison functions for time-only values. This article explores the compare() and equals() methods of Temporal.PlainTime, detailing their implementation and usage. We'll see how these methods provide flexible, calendar-aware time comparisons across different input formats, making them essential tools for reliable time-based data processing.


## Overview of PlainTime Comparison

The PlainTime class provides specialized methods for comparing times without dates, using the compare() method and relational operators. The compare() method returns -1, 0, or 1 based on whether the first time comes before, is the same as, or comes after the second time, respectively.

The compare() method works by converting times to PlainTime objects using the same algorithm as Temporal.PlainTime.from(). This allows for consistent comparisons between different representations of time. For example, it can compare a string, object, or Temporal.PlainTime instance, converting them to PlainTime objects as needed.

The equals() method checks if two PlainTime objects are equal based on their time value and calendar. It effectively serves as a shorthand for Temporal.PlainTime.compare(this, other) === 0, returning true if the times are equivalent and false otherwise. When creating PlainTime objects, it's important to note that the valueOf() method throws an exception, as it's not possible to compare PlainTime objects using relational operators. Instead, the compare() method should be used for comparison.

While the documentation mentions browser compatibility through a dedicated implementation script, specific version requirements are not detailed in the provided resources. This script enables direct testing of PlainTime functionality in browser developer tools.


## compare() Method

The compare() method functions by converting both times to PlainTime objects using the same algorithm as Temporal.PlainTime.from(). It supports three parameter formats: strings, objects, and Temporal.PlainTime instances, making it flexible for various input types.

The comparison logic evaluates each time component (hour, minute, second, millisecond, microsecond, nanosecond) in sequence until a difference is found. For example, when comparing "12:34:56" and "12:34:57", the method recognizes the second difference and returns -1, indicating that "12:34:56" comes before "12:34:57". This same algorithm also handles comparisons between times in different calendars, ensuring consistent behavior regardless of the underlying date system.

As a practical example, consider the following code snippet:

```javascript

const time1 = Temporal.PlainTime.from("12:34:56");

const time2 = Temporal.PlainTime.from("12:34:57");

console.log(Temporal.PlainTime.compare(time1, time2)); // Output: -1

```

This implementation makes compare() suitable for array sorting operations, as demonstrated here:

```javascript

const times = ["12:34:56", "11:34:56", "12:34:57"];

times.sort(Temporal.PlainTime.compare);

console.log(times); // Output: ["11:34:56", "12:34:56", "12:34:57"]

```

This approach ensures accurate time comparisons while maintaining compatibility across different calendar systems.


## equals() Method

The equals() method checks if two PlainTime objects are equal based on their time value and calendar. It effectively serves as a shorthand for Temporal.PlainTime.compare(this, other) === 0, returning true if the times are equivalent and false otherwise.

The method works by converting both times to PlainTime objects using the same algorithm as Temporal.PlainTime.from(), ensuring consistent comparison behavior across different calendar systems. This conversion allows the method to accurately determine equality between times represented in various formats, such as strings, objects, or existing PlainTime instances. 

For example, consider the following usage scenarios:

- Valid equals case:

```javascript

const time1 = Temporal.PlainTime.from("12:34:56");

const time2 = Temporal.PlainTime.from({ hour: 12, minute: 34, second: 56 });

console.log(time1.equals(time2)); // true

```

- Invalid equals case:

```javascript

const time3 = Temporal.PlainTime.from("00:34:56");

console.log(time1.equals(time3)); // false

```

The equals() method provides a robust solution for comparing time values within the PlainTime class, adhering to the same underlying comparison algorithm used by compare(). This consistency ensures reliable time comparisons while accounting for the complexities of different calendar systems.


## Comparison Implementation

The compare() method converts both input times to Temporal.PlainTime objects using the same algorithm as Temporal.PlainTime.from(). This conversion process handles various input formats, including strings, objects, and existing PlainTime instances, ensuring consistent comparison across different representations.

The comparison algorithm examines each time component - hour, minute, second, millisecond, microsecond, and nanosecond - in sequence. When differences are found, the method immediately returns a result: -1 if the first time precedes the second, 0 if they are identical, and 1 if the first time succeeds the second.

For implementation details, the method performs the following steps:

1. Convert both input parameters to Temporal.PlainTime objects using Temporal.PlainTime.from().

2. Compare each time component: hour, minute, second, millisecond, microsecond, nanosecond.

3. Return -1, 0, or 1 based on the comparison outcome.

This approach ensures accurate time comparisons while maintaining consistency across different calendar systems. The comparison result can be directly used for array sorting operations, making it a versatile tool for time-based data organization.


## Browser Compatibility

The browser implementation of the PlainTime class follows the specification closely, providing consistent behavior across different calendar systems. Browser support enables direct testing of PlainTime functionality using the implementation script included with the API.

The class extends ISO 8601/RFC 3339 format with a detailed structure: HH:mm:ss.sssssssss, where HH represents hours (00-23), mm minutes (00-59), and ss.sssssssss seconds with fractional precision. This format allows for precise time representation while maintaining compatibility with existing standards.

Implementation details show that the PlainTime class handles input in multiple formats, converting strings, objects, and existing PlainTime instances to a consistent internal representation using the from() method. This ensures accurate comparisons and operations across different input types.

The class provides robust methods for time manipulation, including adding and subtracting durations, as well as formatting and parsing capabilities. These features enable sophisticated time calculations while maintaining semantic accuracy through properties like hour, minute, and second.

Browser compatibility is achieved through a dedicated implementation script, though specific version requirements are not detailed in the available documentation. This script allows developers to test PlainTime functionality directly in their browser's developer tools, facilitating rapid development and testing of time-related applications.

