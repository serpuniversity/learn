---

title: JavaScript Date setUTCMilliseconds() Method

date: 2025-05-26

---


# JavaScript Date setUTCMilliseconds() Method

JavaScript's Date.setUTCMilliseconds() method provides developers with precise control over millisecond values in UTC time. This introduction will explore the method's functionality, parameters, and behavior across different time ranges, helping developers effectively manipulate date objects while maintaining UTC standards.


## Overview of setUTCMilliseconds() Method

The `setUTCMilliseconds()` method modifies a Date object's millisecond value in Coordinated Universal Time (UTC), which serves as the primary time standard for global applications. According to ECMAScript specifications, this method requires a single integer parameter within the range of 0 to 999, representing the milliseconds to be set.

When called on a Date object, `setUTCMilliseconds()` updates the object's internal timestamp without altering the year, month, or day components. For example, setting milliseconds to 1006 in a Date object created with new Date('October 13, 1996 05:35:32:45 GMT-3:00') results in a millisecond value of 6, while the UTC seconds remain unchanged at 33.

The method behaves consistently across major browsers, including Chrome, Edge, Firefox, Safari, and Opera, as it has been part of JavaScript since ECMAScript1 (1997). When provided with an invalid or out-of-range value, the method adjusts the date information accordingly - for instance, specifying 1100 increments the seconds stored in the Date object by 1 while using 100 for milliseconds.

Developers should note that while `setUTCMilliseconds()` modifies the Date object in place, its return value is typically the modified timestamp rather than the updated milliseconds value, unless explicitly needed for calculations. The method is particularly useful for precise time manipulation in applications requiring UTC time standards.


## Method Syntax and Parameters

The setUTCMilliseconds() method takes a single required parameter: millisecondsValue, which must be an integer between 0 and 999 representing the milliseconds. This value determines the millisecond component of the date, with valid ranges from 0 to 999. The method adjusts the date information accordingly if a parameter is outside the expected range – for example, setting 1100 increments the seconds stored in the Date object by 1 while using 100 for milliseconds.

When called on a Date object, setUTCMilliseconds() updates the object's internal timestamp without changing the year, month, or day components. The method modifies the Date object in place and returns its new timestamp, though developers can explicitly request the updated milliseconds value. This method is particularly useful in applications requiring precise millisecond-level time manipulation while operating under the Coordinated Universal Time (UTC) standard.

The method's behavior is consistent across major browsers, having been part of JavaScript since ECMAScript1 (1997) and supported in Chrome, Edge, Firefox, Safari, and Opera. It has been available across these browsers since July 2015 and remains integral to JavaScript's Date object functionality.


## Method Behavior and Return Value

The method returns the new timestamp of the Date object upon successful execution, allowing developers to retrieve or verify the updated millisecond value if needed. However, the primary effect of the setUTCMilliseconds() method is to modify the Date object in place without requiring developers to store or use the returned value for regular operations.

For edge cases, the method employs logical adjustments when provided with invalid inputs. If the milliseconds value is NaN or coerces to NaN (such as undefined), the date is set to the Invalid Date, resulting in a return value of NaN. Similarly, if the specified milliseconds value exceeds 999, the method adjusts the date information accordingly - for example, setting 1100 increments the seconds stored in the Date object by 1 while using 100 for milliseconds. These behaviors ensure consistent date manipulation while maintaining proper time representation.


## Examples of setUTCMilliseconds() Usage

The `setUTCMilliseconds()` method allows developers to precisely manipulate the millisecond value of a Date object in Coordinated Universal Time (UTC). Here are several examples demonstrating its usage with both UTC and local time formats:

Example 1: Setting millisecond 52 in a Date object created with universal time

```javascript

const dateUTC = new Date(Date.UTC(2023, 9, 12, 17, 30, 15, 52));

console.log(dateUTC); // Output: Mon Oct 12 2023 17:30:15 GMT+0000 (Coordinated Universal Time)

```

Example 2: Setting millisecond 51 in a Date object without explicitly setting milliseconds in the constructor

```javascript

const currentDate = new Date();

const updatedDate = new Date(currentDate);

updatedDate.setUTCMilliseconds(51);

console.log(updatedDate); // Output will vary based on system time

```

Example 3: Setting millisecond 42 in a Date object without specifying month, date, or year in the constructor, while maintaining universal time values for month (October), date (12), and year (2023)

```javascript

const dateObject = new Date(Date.UTC(2023, 9 /* October */, 12, 17, 30, 15));

dateObject.setUTCMilliseconds(42);

console.log(dateObject); // Output: Mon Oct 12 2023 17:30:15 GMT+0000 (Coordinated Universal Time)

```

These examples demonstrate how `setUTCMilliseconds()` can be used to update the millisecond value of a Date object while preserving the other time components. The method consistently adjusts the date information according to the provided millisecond value, ensuring precise time manipulation in JavaScript applications.


## Relationship to Other Date Methods

When combined with getUTCMilliseconds(), setUTCMilliseconds() enables precise manipulation of date values under UTC time standards. The getUTCMilliseconds() method returns the current millisecond value according to universal time, providing the necessary context for time manipulation operations.

The Date() constructor, when used in conjunction with setUTCMilliseconds(), allows for flexible date creation and modification. For example, setting millisecond 52 in a date object created with universal time requires creating the initial Date object using the Date.UTC constructor and then applying setUTCMilliseconds() to modify the millisecond value.

The method works consistently across major browsers, including Chrome, Edge, Firefox, Safari, and Opera, as it has supported these browsers since ECMAScript1 (1997). While the method returns the updated timestamp on successful execution, developers can explicitly request the updated milliseconds value if needed. In cases where the provided value is NaN or coerces to NaN (such as undefined), the date is set to the Invalid Date, resulting in a return value of NaN. If the specified milliseconds value exceeds 999, the method adjusts the date information accordingly.

Additional methods like Date.now() and Date.getTime() provide related functionality for measuring time intervals and working with timestamps. The Date.now() method returns the number of milliseconds since the ECMAScript epoch (January 1, 1970), while Date.getTime() returns the number of milliseconds since the ECMAScript epoch for a given Date object. These methods offer developers alternative approaches for handling time measurements, with Date.now() particularly useful for high-resolution timing when the Performance API's high-resolution time feature is available.

