---

title: JavaScript Working with Time Durations and Dates

date: 2025-05-27

---


# JavaScript Working with Time Durations and Dates

JavaScript's built-in Date object and libraries like Day.js offer powerful tools for working with time durations and dates. This article explores how to manipulate time using these JavaScript features, from converting days to milliseconds to working with human-readable time formats. We'll also examine the nuances of JavaScript's Date object methods for time arithmetic, helping you handle dates and durations effectively in your applications.


## Using Day.js for Duration Operations

Day.js provides two methods for working with durations. The `dayjs.duration(milliseconds).milliseconds()` method returns the milliseconds component, with a maximum value of 999. For example, `dayjs.duration(500).milliseconds()` returns 500, while `dayjs.duration(15000).milliseconds()` returns 500. The `dayjs.duration().asMilliseconds()` method returns the full duration in milliseconds directly, making it suitable for operations that require the entire duration value. For instance, `dayjs.duration(500).asMilliseconds()` returns 500, and `dayjs.duration(15000).asMilliseconds()` returns 15000.


## Converting Days to Milliseconds

The conversion of days to milliseconds in JavaScript follows a straightforward sequence of multiplications:

1. Multiply the input days by 24 to convert to hours

2. Multiply the result by 60 to convert to minutes

3. Multiply by 60 again to convert to seconds

4. Finally, multiply by 1000 to convert to milliseconds

For example, 2 days are converted as follows:

2 * 24 * 60 * 60 * 1000 = 17,280,000 milliseconds

The JavaScript program demonstrates this conversion through user interaction, prompting the user to enter days and performing the precise sequence of multiplications to display the result in milliseconds.


## Human-Readable Time Duration Formatting

JavaScript offers multiple approaches for converting time durations into human-readable formats. The formatDuration function utilizes Moment.js for precise conversions. It processes durations in milliseconds and returns strings formatted as "days hours:minutes:seconds.milliseconds", supporting customizable format strings.

The msToDaysHoursMinutes function presents an alternative approach using basic arithmetic. It accepts timestamps in milliseconds and returns formatted strings representing days, hours, minutes, and seconds. The functionality includes automatic padding for single-digit hours and minutes to maintain consistent two-digit formatting.

Both implementations demonstrate sophisticated handling of multiple time units, from milliseconds to years. The functions accommodate various conversion requirements, supporting display options for different time scales and custom formatting preferences. This flexibility enables developers to present elapsed time in the most appropriate units for their applications.


## JavaScript Date Object Methods

The `Date` object in JavaScript provides several methods for working with milliseconds. For instance, the `getMilliseconds()` method returns the milliseconds part of the date, while the `setMilliseconds(milliseconds_value)` method allows setting the milliseconds component of a date object created with the `Date()` constructor.

The `getTime()` method returns the number of milliseconds between midnight of January 1, 1970, and the specified date. It returns a number representing the timestamp in milliseconds and returns NaN if the date is invalid. This method is functionally equivalent to the `valueOf()` method and can be used to retrieve the timestamp of a date object, assign a date and time to another Date object, or measure the execution time of operations. In browsers supporting the Performance API's high-resolution time feature, `Performance.now()` can provide more reliable and precise measurements of elapsed time than `Date.now()`.

To convert milliseconds to a date, developers can use the following approach: declare a variable to store the current date's milliseconds using `new Date().getTime()`, then convert these milliseconds to a Date object and store it in a new variable. For example:

```javascript

let time = new Date().getTime();

let date = new Date(time);

console.log("Milliseconds = " + date.toString());

```

This will output the current date and time in a standard format. The `Date` object also includes methods for working with time in different time zones and for converting between different date representations.

The `Date` object's methods for manipulating time extend beyond milliseconds to include:

```javascript

getMinutes() // Returns the minutes (0 to 59) of the provided date and time

getHours() // Returns the hour (0 to 23) of the provided date and time

getSeconds() // Returns the seconds (0 to 59) of the provided date and time

getDate() // Returns the day of the month (1 to 31) for the defined date

setMilliseconds(milliseconds_value) // Sets the milliseconds of a date object

```

These methods offer comprehensive functionality for time manipulation, from retrieving individual time components to setting values and performing arithmetic operations on date objects.


## Date Arithmetic with Time Durations

JavaScript's Date object provides several methods for performing date arithmetic with time durations. To add days to a date, developers can use the `setDate()` method or manipulate the date's timestamp directly. The example provided demonstrates adding 3 days to the current date using both approaches:

```javascript

// Using setDate()

var dateObj = new Date();

var val = dateObj.getTime();

var days = 3 * 24 * 60 * 60 * 1000; // 3 days in milliseconds

dateObj.setDate(dateObj.getDate() + 3);

val = dateObj.getMonth() + 1 + "/" + dateObj.getDate() + "/" + dateObj.getFullYear();

alert(val);

// Using setTime()

dateObj.setTime(dateObj.getTime() + 3 * 24 * 60 * 60 * 1000);

```

Both methods correctly update the date object to represent the new date. The first approach modifies the date properties directly, while the second updates the timestamp and recalculates the date components.

The Date object's methods for manipulating time components include:

```javascript

getMinutes() // Returns the current minutes (0-59)

getHours() // Returns the current hour (0-23)

getSeconds() // Returns the current seconds (0-59)

getDate() // Returns the day of the month (1-31)

setMilliseconds(milliseconds_value) // Sets the milliseconds for the date object

```

These methods enable comprehensive manipulation of date and time values in JavaScript, supporting both simple timestamp operations and complex date calculations. The combination of these methods allows developers to perform precise date arithmetic and time manipulation in their JavaScript applications.

