---

title: JavaScript Date Object Reference & Tutorial

date: 2025-05-26

---


# JavaScript Date Object Reference & Tutorial

Working with dates in JavaScript involves mastering the powerful but complex Date object and its numerous methods. This article reveals the secrets of date creation, manipulation, and formatting, helping you master this essential aspect of web development. From crafting dates from timestamps and strings to formatting output and performing time calculations, we'll explore every tool in JavaScript's date toolkit. Along the way, we'll compare the built-in Date object to modern alternatives like Luxon and date-fns, showing you how to handle dates with confidence and precision. Whether you're building a simple event calendar or a full-fledged time-tracking application, this comprehensive guide will empower you to manage dates and times effectively in your JavaScript projects.


## Basic Date Operations

The Date object in JavaScript offers multiple methods for creation and manipulation. Without arguments, new Date() returns the current date and time in the local timezone. It can also create a Date object from:

- A timestamp: new Date(milliseconds), representing the number of milliseconds since January 1, 1970 at 00:00:00 UTC (the Unix Epoch).

- A string: new Date(datestring), which parses input strings to create a Date object. Supported formats include "Month Day, Year Hour:Minute:Second" and "YYYY-MM-DDTHH:MM:SS".

- Individual date components: new Date(year, month, date, hours, minutes, seconds, ms) accepts from 1 to 7 arguments, with 1 being the current date if not specified.

Dates before January 1, 1970 have negative timestamps. The object's getTime() method converts a Date object to its corresponding timestamp, while the constructor can create Date objects from both positive and negative timestamps.

The Date object handles date creation with a combination of methods:

- new Date() creates the current date and time

- new Date("December 17, 1995 03:24:00") creates a Date from a formatted string

- new Date(1995, 11, 17) creates a Date from year, month (0-indexed), and day values

- new Date(1995, 11, 17, 3, 24, 0) creates a Date from full date and time components

- new Date(628021800000) creates a Date from an epoch timestamp

JavaScript's Date methods return values that need formatting for output:

- getDate() returns the day of the month

- getDay() returns the day of the week (0 to 6)

- getFullYear() returns the year

- getHours() returns the hour

- getMilliseconds() returns the milliseconds

For extended functionality, developers can use third-party libraries like Luxon, which builds on built-in Intl functionality for locales and time zones. Modern alternatives to outdated libraries like Datejs recommend using Luxon for date manipulation tasks.


## Date Creation Methods

The constructor function `Date()` creates Date objects representing various points in time through multiple method signatures. The signature with no arguments returns the current date and time, while passing a timestamp creates a Date object corresponding to the specified number of milliseconds since January 1, 1970 UTC+0. To create a Date object from a string, the constructor accepts various ISO 8601 formats including "Month Day, Year Hour:Minute:Second" and "YYYY-MM-DDTHH:MM:SS". Additionally, it supports creation from individual date and time components: year, month, date, hours, minutes, seconds, and milliseconds.

The constructor can handle non-Date values, coercing them to their primitive representations: undefined becomes NaN, null becomes 0, and arrays are joined with commas. String coercion follows the Array.prototype.toString() method, requiring valid ISO 8601 date strings for reliable parsing. For numerical values, the constructor interprets dates before January 1, 1970 correctly with negative timestamps, making it flexible for both past and present date creation.

The Date object also provides several static methods for time manipulation, including `now()` which returns the current timestamp, `parse()` for converting date strings to timestamps, and `UTC()` for calculating timestamps based on universal time. The object's internal representation stores dates as the number of milliseconds since the Unix Epoch, allowing for precise time calculations across various creation methods.


## Date Property Access

The JavaScript Date object provides a rich set of methods for accessing date components, including the year, month, date, hours, minutes, seconds, and milliseconds. These methods allow developers to retrieve or set individual components of a date, either relative to the local time zone or universal time (UTC).


### Accessing Date Components

To retrieve date components, developers can use methods with similar names to those used for setting values. For example, `getYear()` returns the year, while `getFullYear()` returns the four-digit year. The month is represented as a zero-based index (0-11), not the month name directly, which differs from some other date-handling libraries.

Here are some key access methods:

- `getMinutes()`, `setMinutes()`: Retrieve and set the minutes

- `getUTCMinutes()`, `setUTCMinutes()`: Retrieve and set the UTC minutes

- `getSeconds()`, `setSeconds()`: Retrieve and set the seconds

- `getUTCMilliseconds()`: Retrieve the UTC milliseconds

- `getDay()`, `getUTCDay()`: Retrieve the day of the week (0-6)


### Constructor and UTC Methods

The `Date()` constructor creates Date objects in several ways. It can accept two or more arguments: year, month, day, hour, minute, second, and millisecond, representing local time. Alternatively, it can use `Date.UTC()` for UTC time, accepting a single year argument and interpreting other components as UTC.

For instance, the following code creates a Date object representing January 1, 2023:

```javascript

var d = new Date(2023, 0, 1); // Note: month is 0-based (0 for January)

```

The constructor handles missing arguments by defaulting to the current date and time. For example, passing only year and month results in the start of the month on the current day:

```javascript

var d = new Date(2023, 0); // This creates midnight January 1, 2023

```


### Property Behavior

When manipulating date components, developers should be aware of how changes affect other properties. For example, changing the day of the month can roll over to the previous month. Similarly, changing the month advances to the next year when necessary. The property ranges are as follows:

- Months: 0-11 (January is 0, December is 11)

- Day: 1-31

- Hour: 0-23

- Minute: 0-59

- Second: 0-59

- Millisecond: 0-999

Understanding these nuances is crucial for accurately working with JavaScript date and time data.


## Date Formatting Techniques

JavaScript offers multiple approaches to date formatting, with the built-in Intl.DateTimeFormat providing robust localization capabilities. This method allows specifying locale formats such as "Dienstag, 17. Oktober 2023" for German or "2013. 10. 17." for Korean. When an unsupported locale is provided, it gracefully falls back to the default formatting.

For more basic needs, developers can use the Date object's built-in .toLocaleDateString method, though this requires modern browser support and specifying both locale and format options. A practical custom formatting function iterates over date properties with leading zero padding, though it requires Object.keys() support which may need polyfilling for older browsers.

Modern JavaScript development recommends several powerful libraries:

- date-fns: A modern, immutable library that builds on ECMAScript standards

- Luxon: A comprehensive toolkit focusing on parsing, formatting, and manipulation with built-in internationalization

- Day.js: A minimalist alternative for lightweight date handling

Developers can perform advanced date operations using these libraries, including precise time calculations and comprehensive date string support. The Temporal API represents a future direction for JavaScript date handling, offering improved functionality over the existing Date object.


## Date Manipulation

The Date object in JavaScript offers extensive functionality for manipulating date components, including direct setting of hour, minute, second, and millisecond values through the `setHours()`, `setMinutes()`, `setSeconds()`, and `setMilliseconds()` methods. These methods allow setting individual time components while preserving other properties of the Date object. For example, calling `setHours(14)` on a Date object without specifying minutes, seconds, or milliseconds will adjust only the hour while maintaining the original day, month, and year values.

For more complex time adjustments, developers can utilize the `setTime()` method, which accepts a timestamp representing the number of milliseconds since January 1, 1970, 00:00:00 UTC. This method provides a flexible way to manipulate Date objects by directly setting their internal representation. Additionally, JavaScript offers the `setUTC` variants (`setUTCHours()`, `setUTCMinutes()`, `setUTCMilliseconds()`) for performing these operations in universal time, allowing precise control over time zone differences.

To illustrate these capabilities, consider the following example where we adjust a Date object representing a specific time to a new hour:

```javascript

let eventDate = new Date("2023-10-05T15:30:00Z");

eventDate.setHours(18); // Change event time to 18:00

console.log(eventDate.toISOString()); // Output: 2023-10-05T18:00:00.000Z

```

Developers can also subtract Date objects to calculate time differences in milliseconds, as demonstrated in the provided documentation example:

```javascript

function diffSubtract(date1, date2) {

    return date2 - date1;

}

// Example usage

let start = new Date("2023-01-01T00:00:00Z");

let end = new Date("2023-01-02T23:59:59Z");

console.log(diffSubtract(end, start)); // Output: 86399000

```

This subtraction method returns the exact difference between two dates, measured in milliseconds, providing a precise basis for time calculations in JavaScript applications.

