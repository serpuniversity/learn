---

title: JavaScript Date getHours() Method

date: 2025-05-26

---


# JavaScript Date getHours() Method

In JavaScript, the Date object provides powerful tools for handling dates and times, with methods like getHours() allowing developers to extract precise time information from date objects. This article explores the nuances of the getHours() method, including how it returns local time hours (0-23), handles invalid dates, and relates to universal time calculations. Through practical examples and technical explanations, we'll demonstrate how getHours() works in various scenarios and why understanding its behavior is crucial for accurate date manipulation in JavaScript applications.


## Returns Local Time Hour [0-23]

The getHours() method returns the hour of a given date according to local time, as an integer between 0 and 23. This value represents the current hour in the local time zone where the JavaScript code is executed.

When creating a new Date object and calling getHours(), it returns the current hour in the local time zone. For example:

```javascript

let today = new Date();

let currentHour = today.getHours();

console.log(currentHour); // Outputs the current hour as an integer between 0 and 23

```

Alternatively, when initializing a Date object with a specific date and time, getHours() returns the hour component of that date in the local time zone:

```javascript

let specificTime = new Date("October 15, 1996 05:35:32");

let hourValue = specificTime.getHours();

console.log(hourValue); // Outputs 5

```

The method returns 0 for unspecified hours and NaN for invalid dates. When working with dates that fall outside the valid month range (e.g., "October 35, 1996"), getHours() returns NaN:

```javascript

let invalidDate = new Date("October 35, 1996 12:35:32");

let hourNaN = invalidDate.getHours();

console.log(hourNaN === NaN); // Outputs true

```

The ECMAScript specification requires getHours() to return `NaN` for invalid date objects, ensuring consistent behavior across implementations. While early versions of the specification did not explicitly mention this behavior, modern JavaScript engines follow this convention:

```javascript

let invalidDate = new Date(123); // Invalid date format

let result = invalidDate.getHours();

console.log(!Number.isFinite(result)); // Outputs true

```

Browser compatibility for getHours() is excellent, with the method available in all modern browsers: Chrome, Firefox, Edge, Safari, and Opera. This wide compatibility ensures developers can rely on consistent behavior across different environments.


## Basic Usage Examples

The method returns 0 for unspecified hours and NaN for invalid dates. When working with dates that fall outside the valid month range (e.g., "October 35, 1996"), getHours() returns NaN:

```javascript

let invalidDate = new Date("October 35, 1996 12:35:32");

let hourNaN = invalidDate.getHours();

console.log(hourNaN === NaN); // Outputs true

```

The method works by examining the Date object's internal time value and extracting the hour component as an integer between 0 and 23. The returned value represents the current hour in the local time zone where the JavaScript code is executed.

For example, when creating a new Date object and calling getHours(), it returns the current hour in the local time zone:

```javascript

let today = new Date();

let currentHour = today.getHours();

console.log(currentHour); // Outputs the current hour as an integer between 0 and 23

```

Alternatively, when initializing a Date object with a specific date and time, getHours() returns the hour component of that date in the local time zone:

```javascript

let specificTime = new Date("October 15, 1996 05:35:32");

let hourValue = specificTime.getHours();

console.log(hourValue); // Outputs 5

```

To demonstrate this further, consider the following examples:

```javascript

let A = new Date('October 15, 1996 05:35:32');

let B = A.getHours();

console.log(B); // Output: 5

let A = new Date('October 12, 1996');

let B = A.getHours();

console.log(B); // Output: 0

let A = new Date('October 35, 1996 12:35:32');

let B = A.getHours();

console.log(B); // Output: NaN

let A = new Date();

let B = A.getHours();

console.log(B); // Output: Current hour

```

The method returns 0 for hours not specified in the Date object and NaN for months greater than 31. It returns the hour according to local time and returns an integer between 0 and 23, where 0 represents midnight and 23 represents 11 PM. The method can be used for time comparisons by comparing integer values returned by getHours(). The returned value is affected by the local time zone of the environment where the code is executed.

To convert the hour from 24-hour format to 12-hour format, simple arithmetic can be used. For instance:

```javascript

function convert24to12HourFormat(hour) {

  return (hour % 12 || 12) + " AM/PM";

}

let currentHour = new Date().getHours();

let formattedHour = convert24to12HourFormat(currentHour);

console.log(formattedHour); // Outputs the current hour in 12-hour format

```

The method has been standardized since ECMAScript 1st Edition (1997) and is available in all modern browsers, ensuring consistent behavior across different environments.


## Behavior with Invalid Dates

The method returns NaN for invalid dates, as specified in the ECMAScript 2026 Language Specification. This applies consistently across all supported environments, with the method having been standardized since ECMAScript 1st Edition (1997).

An invalid date can occur when initializing a Date object with an unparsable string or improperly formatted date components. For example, creating a Date object with "October 35, 1996 12:35:32" results in NaN when calling getHours(), as the month value of 35 is outside the valid range of 1-12:

```javascript

let invalidDate = new Date("October 35, 1996 12:35:32");

let hourNaN = invalidDate.getHours();

console.log(hourNaN === NaN); // Outputs true

```

The same applies when attempting to reference hours in an uninitialized Date object:

```javascript

let unspecifiedHours = new Date();

let unspecifiedResult = unspecifiedHours.getHours();

console.log(!Number.isFinite(unspecifiedResult)); // Outputs true

```

In practice, this behavior allows developers to check for valid dates by examining the return value of getHours(). If the method returns NaN, the date is invalid and cannot be reliably used to extract time information.

The method's implementation across browsers consistently follows these specifications, with support dating back to July 2015 and compatibility extending to all modern browsers including Chrome, Firefox, Edge, Safari, and Opera. This ensures developers can rely on consistent behavior across different environments.


## Relation to Universal Time

The getUTCHours() method returns hours according to universal time, specifically Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). This value corresponds to the hours component of the given date according to UTC, which is the same as GMT and represents the same time zone. Like getHours(), getUTCHours() returns an integer between 0 and 23, where 0 represents midnight and 23 represents 11 PM.

JavaScript's Date object represents dates and times as local time, and the getTime() method returns the number of milliseconds since January 1, 1970, which is the Unix epoch time. When working with universal time, the UTC equivalents of the corresponding local methods are provided:

- getUTCDate() returns the same as getDate()

- getUTCFullYear() returns the same as getFullYear()

- getUTCMonth() returns the same as getMonth()

- getUTCDay() returns the same as getDay()

- getUTCHours() returns the same as getHours()

- getUTCMinutes() returns the same as getMinutes()

- getUTCSeconds() returns the same as getSeconds()

- getUTCMilliseconds() returns the same as getMilliseconds()

The difference between local time and UTC time can be up to 24 hours, representing the full range of time zones. Each time zone difference is recorded as a difference in hours, with some places adjusting their time by changing the hour value when observing daylight savings time.

When creating a Date object with specific UTC time, both getHours() and getUTCHours() return the same value if the Date object is initialized with UTC time. However, their outputs differ when dealing with time zone offsets:

```javascript

var date = new Date("2017-11-15T04:00:00Z");

console.log(date) // Wed Nov 15 2017 04:00:00 GMT+0000 (UTC)

console.log(date.getHours() === date.getUTCHours()) // true

```

In this example, both methods return the same value because the date string "2017-11-15T04:00:00Z" includes UTC information. However, when a Date object is created with local time, getHours() returns the local hour while getUTCHours() returns the UTC hour, demonstrating the difference between local and universal time.

This distinction is crucial when working with international data or time-dependent applications that need accurate time calculations across different time zones. The getTimezoneOffset() method can be used to retrieve the difference (in minutes) between local time and UTC time, allowing developers to convert local time to UTC time if needed.


## Related Methods and Best Practices

The JavaScript Date object represents a specific moment in time in a platform-independent format, encapsulating an integral number that corresponds to the milliseconds since the epoch (midnight at the beginning of January 1, 1970, UTC). This integral value allows precise representation and manipulation of dates and times.

When working with dates and times in JavaScript, several key methods are essential for accurate date manipulation. The setHours() method, for example, allows precise time setting according to local time, while the setUTCHours() method performs the same operation according to universal time. These methods accept hour values between 0 and 23 and handle minutes, seconds, and milliseconds as optional parameters, automatically adjusting other time components as necessary.

JavaScript's Date object provides robust support for time zone manipulation through methods like setUTCMonth(), setUTCDate(), and setUTCHours(). These methods ensure that date objects maintain proper time zone information when manipulating date parts. For instance, when setting the month using setUTCMonth(), the method correctly interprets month values from 0-11, where 0 corresponds to January. This ensures consistent date calculations across different time zones.


### Date String Formats and Conversion

JavaScript's Date object can parse and generate date strings in various formats. The Date constructor and Date.parse() method accept date-time strings in a specific format that includes date-only and date-time components, along with time zone offsets. For generating standard date-time strings, thetoISOString() method returns the simplified ISO 8601 format, while the toJSON() method calls toISOString() and returns the result. The toString(), toDateString(), and toTimeString() methods provide human-readable date-time representations, with toString() returning the date and time as "Thu Jan 01 1970 00:00:00 GMT+0000 (Coordinated Universal Time)".

Developers should be aware that the Date object treats two-digit year values with legacy behavior, interpreting them as offsets from 1900 or 2000. To avoid this behavior, the setFullYear() and getFullYear() methods should be used for years in the range 0-99. This ensures consistent year handling across different date inputs.

