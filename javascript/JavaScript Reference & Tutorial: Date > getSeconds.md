---

title: JavaScript Date.getSecond() Method

date: 2025-05-26

---


# JavaScript Date.getSecond() Method

JavaScript's Date object provides numerous methods for working with dates and times, from creating new date objects to manipulating and formatting existing ones. One such method is getSeconds(), which retrieves the seconds component of a specified date. This introduction will explore the getSeconds() method's functionality, demonstrating how it works with valid and invalid dates, highlighting key aspects like time zone considerations and common usage pitfalls. Through practical examples and insights into the method's implementation, developers will gain a solid understanding of how to effectively use getSeconds() in their JavaScript applications.


## getSeconds() Method Overview

The getSeconds() method returns the seconds component of a date according to local time, providing an integer between 0 and 59. For example, `new Date('July 20, 1969 00:20:18').getSeconds()` correctly returns 18.

The method is called on a Date object and returns the seconds component of the date according to local time. If the date is invalid, getSeconds() returns NaN. This behavior is consistent across all supported browsers, including Chrome, Edge, Firefox, Safari, Opera, and Internet Explorer since JavaScript 1.0.

The method works by extracting the seconds component from the Date object's internal time value, which represents milliseconds since January 1, 1970. It then returns this value as an integer between 0 and 59, representing the seconds of the specified date.

When creating a Date object for a specific date, getSeconds() retrieves the seconds component of that date. For instance, `new Date('October 15, 1996 05:35:32').getSeconds()` returns 32. Similarly, `new Date('December 25, 2023 10:30:45').getSeconds()` returns 45.

However, using getSeconds() to capture the current time every 600ms may not work as intended due to how JavaScript schedules microtasks. While the code runs once every second, the time might not be correctly captured during this interval.

To get the current date or time in seconds, developers can use `Math.floor(new Date().getTime() / 1000)`. This method provides an integer representing the number of seconds since midnight, January 1, 1970 (the Unix epoch).


## Basic Usage and Return Value

The getSeconds() method returns the seconds component of a specified date and time based on the local time zone. The method returns an integer between 0 and 59, representing the seconds of a date. If the provided Date object is invalid, the method returns NaN.

Syntax: getSeconds();

Return Value: Returns an integer representing the seconds component of the time portion of the Date object.

Example 1:

```html

<html>

<body>

<script>

  const currentDate = new Date();

  const seconds = currentDate.getSeconds();

  console.log(seconds);

</script>

</body>

</html>

```

Example 2: Extracting seconds from a specific date

```javascript

let specificDate = new Date('October 15, 1996 05:35:32');

let seconds = specificDate.getSeconds();

console.log(seconds); // Output: 32

```

Example 3: Handling invalid dates

```javascript

let invalidDate = new Date('October 33, 1996 05:35:32');

let result = invalidDate.getSeconds();

console.log(result); // Output: NaN

```

Example 4: Date without seconds

```javascript

let dateWithoutSeconds = new Date('October 13, 1996 05:35');

let seconds = dateWithoutSeconds.getSeconds();

console.log(seconds); // Output: 0

```

Example 5: Out-of-range value

```javascript

let outOfRangeValue = new Date('October 13, 1996 05:35:88');

let seconds = outOfRangeValue.getSeconds();

console.log(seconds); // Output: 0

```

Example 6: Current second

```javascript

let currentSecond = new Date().getSeconds();

console.log(currentSecond);

```


## Timezone Considerations

The getSeconds() method returns the seconds based on the local time zone of the environment where the code is executed, rather than using UTC or any other time zone. This means that if you run the method on a Date object representing a specific date and time, it will return the correct seconds value according to the time zone settings of the device or server running the code.

For example, consider the following code:

```javascript

let specificDate = new Date('December 25, 2023 10:30:45');

let seconds = specificDate.getSeconds();

console.log(seconds); // Outputs: 45

```

This code creates a Date object for December 25, 2023, at 10:30:45 and retrieves the seconds component using getSeconds(). The output will be 45, which is correct for that specific date and time in the local time zone.

The method accounts for time zones by interpreting the date and time according to the local time zone of the environment where the code is executed. This behavior ensures that the seconds value returned is consistent with the local time settings, rather than a fixed time zone like UTC.


## Common Pitfalls and Usage Notes

When running the getSeconds() method at 600ms intervals, developers may encounter issues with incorrect time capture. The code executes once every second, but the time might not be correctly captured during this interval. To avoid this pitfall, developers should use `Math.floor(Date.now() / 1000)` to obtain the current second, which provides an integer representing the number of seconds since midnight, January 1, 1970 (the Unix epoch).

The getSeconds() method consistently returns an integer value between 0 and 59, representing the seconds component of the specified date according to local time. The method works correctly with valid Date objects, returning 0 for dates without seconds and NaN for invalid dates. When creating a Date object, getSeconds() retrieves the seconds component accurately based on the provided date and time.

For developers working with Date objects, understanding the method's behavior with missing or out-of-range values is crucial. The method returns 0 when the time is less than one second into the current minute and 0 for dates with missing seconds. When dealing with invalid dates, the method correctly returns NaN, allowing developers to easily identify and handle such cases.

