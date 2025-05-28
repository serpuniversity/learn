---

title: JavaScript Date setUTCHours Method

date: 2025-05-26

---


# JavaScript Date setUTCHours Method

JavaScript's `Date` object provides various methods to manipulate and retrieve date and time information. While methods like `getUTCHours` and `getUTCMilliseconds` allow reading specific components of a date, their counterparts `setUTCHours`, `setUTCMilliseconds`, and others enable modifying these values with precise control. This article explores the `setUTCHours` method, examining its functionality, parameter requirements, and the behavior when working with out-of-range values. Through detailed examples, we illustrate how to correctly set UTC hours while understanding the implications for other time components and the returned timestamp value.


## Setting and Understanding UTC Hours

The setUTCHours method sets the hour value of a Date object according to Coordinated Universal Time (UTC), with values ranging from 0 to 23. This method returns the updated Date object, as demonstrated in the following example:

```javascript

const eventHour = new Date('2023-06-25T00:00:00');

eventHour.setUTCHours(14);

console.log(eventHour); // Output: 2023-06-25T14:00:00.000Z

console.log(eventHour.getUTCHours()); // Output: 14

```


### Supported Date Component Setting Order

When setting minutes, seconds, or milliseconds, the corresponding previous time unit must be defined. This means that to set the milliseconds value, both the minute and second values must be specified, as illustrated in this example:

```javascript

let dateobj = new Date('October 13, 1996 05:35:32 GMT-3:00');

dateobj.setUTCHours(11, 30, 0, 450);

let B = dateobj.getUTCHours();

let M = dateobj.getUTCMinutes();

let S = dateobj.getUTCSeconds();

let milli = dateobj.getUTCMilliseconds();

console.log(B, M, S, milli); // Output: 11 30 0 450

```


### Overflow and Underflow Behavior

The method handles values outside the standard ranges through wrap-around behavior. Providing a value greater than 23 will subtract 24 hours from the date. Similarly, a value of -1 represents the last hour of the previous day, as shown in these examples:

```javascript

let dateobj = new Date();

dateobj.setUTCHours(26); // 26 - 24 = 2

console.log(dateobj); // Output: 2023-06-28T06:00:00.000Z

let dateobj2 = new Date();

dateobj2.setUTCHours(-1);

console.log(dateobj2); // Output: 2023-06-25T23:00:00.000Z

```


### Date Object Interpretation

JavaScript's Date objects represent dates as timestamps, with 0 representing midnight on January 1, 1970, UTC. This timestamp is interpreted differently based on whether it's considered local time or UTC. For local time interpretation, a timestamp of 0 represents 19:00:00 on December 31, 1969, in New York (UTC-5), demonstrating the importance of timezone considerations in date operations.


## Method Syntax and Parameter Options

The setUTCHours method can be called with four parameters: hours, minutes, seconds, and milliseconds. When setting these components, earlier time units must be defined, meaning you must specify minutes and seconds to set milliseconds.


### Parameter Requirements

The method requires an integer value between 0 and 23 for the hours parameter. Optional parameters for minutes, seconds, and milliseconds must follow specific ordering rules: minutes without seconds, seconds without milliseconds, or milliseconds without both preceding units will use default values from `getUTCMinutes()`, `getUTCSeconds()`, and `getUTCMilliseconds()` respectively.


### Behavior with Out-of-Range Values

Values outside the standard ranges are handled through overflow and underflow behavior:

- Providing -1 for hours sets the last hour of the previous day

- A value of 24 sets the first hour of the next day

- -1 for minutes or seconds sets the last minute or second of the previous hour

- 60 for minutes or seconds sets the first minute or second of the next hour

- -1 for milliseconds sets the last millisecond of the previous second

- 1000 for milliseconds sets the first millisecond of the next second


### Example Usage

The method returns the number of milliseconds since January 1, 1970, 00:00:00 UTC, which can be obtained using the getTime() method. Here's an example of setting hours and minutes:

```javascript

const currentDate = new Date("December 25, 2023, 10:15:00");

currentDate.setUTCHours(12);

console.log(currentDate.getUTCHours()); // Output: 12

console.log(currentDate.getTime()); // Output: 1703668800000

```


##  hour Value Behavior

When setting hours using the setUTCHours method, providing a value greater than 23 subtracts 24 hours from the date. For example, setting an hour of 26 would result in the hour being set to 2 (26 - 24 = 2). Similarly, supplying -1 for the hours parameter sets the hour to the last hour of the previous day.

The method uses wrap-around behavior for values outside the standard range. Setting -1 for minutes or seconds sets the last minute or second of the previous hour, while 60 for minutes or seconds sets the first minute or second of the next hour. For milliseconds, -1 sets the last millisecond of the previous second, and 1000 sets the first millisecond of the next second.

This behavior is consistent across major browsers, including Google Chrome, Internet Explorer, Mozilla Firefox, Opera, and Safari. The method does not return a value and instead modifies the Date object in place, returning its timestamp as a result of calling the getTime() method.


## Time Component Dependencies

When setting minutes, seconds, or milliseconds using the setUTCHours method, JavaScript requires the previous time unit to be defined. For example, to set milliseconds, both minute and second values must be specified, as shown in this example:

```javascript

let dateobj = new Date('October 13, 1996 05:35:32 GMT-3:00');

dateobj.setUTCHours(11, 30, 0, 450);

let B = dateobj.getUTCHours();

let M = dateobj.getUTCMinutes();

let S = dateobj.getUTCSeconds();

let milli = dateobj.getUTCMilliseconds();

console.log(B, M, S, milli); // Output: 11 30 0 450

```

The method will use the values returned from getUTCMinutes(), getUTCSeconds(), and getUTCMilliseconds() methods if the minute, second, or millisecond parameters are not specified. If a specified parameter is outside the expected range, the method attempts to update the date information accordingly. For instance, setting 100 for seconds increments the minutes by 1 and uses 40 for seconds, as demonstrated in this example:

```javascript

const eventHour = new Date('2023-06-25T00:00:00');

eventHour.setUTCHours(14, 100, 40);

console.log(eventHour.getUTCMinutes()); // Output: 1

console.log(eventHour.getUTCSeconds()); // Output: 40

```


### Handling Out-of-Range Values

If the specified minute, second, or millisecond values are outside the expected range, the method attempts to update the date information in the Date object. For example, specifying 60 for seconds increments the minutes by 1 and uses 0 for seconds:

```javascript

let dateobj = new Date('October 13, 1996 05:35:59 GMT-3:00');

dateobj.setUTCHours(11, 60, 0);

console.log(dateobj.getUTCMinutes()); // Output: 12

console.log(dateobj.getUTCSeconds()); // Output: 0

```

Similarly, if 60 is used for milliseconds, it sets the first millisecond of the next second:

```javascript

let dateobj = new Date('October 13, 1996 05:35:59.999 GMT-3:00');

dateobj.setUTCHours(11, 0, 0, 60);

console.log(dateobj.getUTCSeconds()); // Output: 0

console.log(dateobj.getUTCMilliseconds()); // Output: 1000

```


## Method Return Value

The method returns the timestamp of the updated Date object, representing the number of milliseconds since January 1, 1970, 00:00:00 UTC. This timestamp value can be accessed through the `getTime()` method, as demonstrated in this example:

```javascript

const updatedDate = new Date('2023-06-25T00:00:00');

updatedDate.setUTCHours(14);

console.log(updatedDate.getTime()); // Output: 1687806400000

```

The timestamp returned by the method has a range of ±8,640,000,000,000,000 milliseconds, or ±100,000,000 days, relative to the epoch. This corresponds to a span from April 20, 271821 BC to September 13, 275760 AD (slightly smaller than `Number.MAX_SAFE_INTEGER`). Any attempt to represent a time outside this range results in a timestamp value of `NaN`.

The returned timestamp is timezone-agnostic and represents the date and time according to Coordinated Universal Time (UTC). For local time interpretation, JavaScript's Date objects use the timezone offset determined by the host environment. This offset can change due to daylight saving time and historical changes, as explained in the Date reference documentation.

