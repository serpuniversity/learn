---

title: JavaScript Date Object: getUTCSeconds Method

date: 2025-05-26

---


# JavaScript Date Object: getUTCSeconds Method

JavaScript's Date object provides numerous methods for working with dates and times, including operations for UTC conversion. The getUTCSeconds() method specifically extracts the seconds component of a date in Coordinated Universal Time (UTC), offering developers a powerful tool for time-based calculations and date comparisons. This article explores the method's functionality, including its behavior with valid and invalid dates, its implementation details, and practical usage examples.


## getUTCSeconds Method Overview

The getUTCSeconds() method returns the seconds (ranging from 0 to 59) of a specific date according to Coordinated Universal Time (UTC). The method assumes the date is in local time and converts it to UTC before extracting the seconds component.

The method has been available since JavaScript 1.3 and is supported across major browsers including Chrome, Edge, Firefox, Safari, Opera, and Internet Explorer. It operates by returning an integer between 0 and 59, representing the seconds of the date in UTC. If the specified date is invalid, the method returns NaN.

To demonstrate basic usage, consider the following example:

```javascript

const moonLanding = new Date("July 20, 1969, 20:18:04 UTC");

console.log(moonLanding.getUTCSeconds()); // Output: 4

```

This code creates a date object representing the Apollo 11 moon landing and extracts the UTC seconds component, which is 4 in this case.

When working with JavaScript Date objects, it's important to note that the time is static and not a "running clock." To get the current UTC seconds, you can use the following code:

```javascript

const currentUTCSeconds = new Date().getUTCSeconds();

console.log(currentUTCSeconds);

```

This will log the current number of seconds since January 1, 1970, 00:00:00 UTC, adjusting for leap seconds.

The method can also be used in conjunction with the setInterval function to print the current UTC seconds every 2 seconds:

```javascript

function printSeconds() {

  const currentSeconds = new Date().getUTCSeconds();

  console.log(currentSeconds);

}

setInterval(printSeconds, 2000);

```

This code will continuously output the current UTC seconds, updating every 2 seconds.


## Syntax and Parameters

The getUTCSeconds() method requires a single parameter: a Date object reference. This method does not accept any additional parameters.

The method returns the number of seconds in the local time represented by the Date object, converted to Coordinated Universal Time (UTC). The value returned is an integer between 0 and 59, representing the seconds of the date in UTC.

Here's a breakdown of the method's behavior with different types of Date objects:

- For valid Date objects representing specific times, getUTCSeconds() returns the seconds component in UTC format. For example, a date set to 20:18:04 UTC on July 20, 1969, would return 4.

- If the Date object was created without specifying the time, getUTCSeconds() returns 0. For instance, a Date object created without a specific time would default to midnight, resulting in a seconds value of 0.

- When the specified date is invalid, getUTCSeconds() returns NaN. This includes cases where the date exceeds valid calendar boundaries or has incorrect time components.

Here are several practical examples demonstrating basic usage and handling of invalid dates:

```javascript

let moonLanding = new Date("July 20, 1969, 20:18:04 UTC");

console.log(moonLanding.getUTCSeconds()); // Output: 4

let invalidDate = new Date("July 33, 1969, 20:18:04 UTC");

console.log(invalidDate.getUTCSeconds()); // Output: NaN

let currentDate = new Date();

console.log(currentDate.getUTCSeconds()); // Output varies based on current time

```

Understanding this method's functionality and limitations is crucial for accurate date-time operations in JavaScript, particularly when working with time zones and historical data.


## Return Value and Valid Range

The method returns an integer between 0 and 59 representing the UTC seconds of the date (Section 1 of the provided documents).

The returned value is the number of seconds since midnight, converted to UTC time (Section 2 of the provided documents). This means that for any given Date object, the seconds will always range from 0 to 59, regardless of the time component in the original date (Section 4 of the provided documents).

When a Date object is created without specifying the time, getUTCSeconds returns 0 (Section 3 of the provided documents). This occurs because the date defaults to midnight when no specific time is provided, and 0 seconds correspond to the beginning of the first minute of that day.

The method always operates on the timestamp value stored in UTC format (Section 1 of the provided documents). This ensures consistent behavior across different time zones, as the seconds are calculated based on universal time rather than local time (Section 2 of the provided documents).

For invalid date strings, the method returns NaN (Section 1 of the provided documents). This allows developers to check for valid date inputs by verifying that the returned value is not NaN (Section 1 of the provided documents).


## Handling Invalid Dates

When a Date object is created without specifying the time, getUTCSeconds returns 0 (Section 3 of the provided documents). This occurs because the date defaults to midnight when no specific time is provided, and 0 seconds correspond to the beginning of the first minute of that day.

If the specified date is invalid, getUTCSeconds returns NaN (Section 1 of the provided documents). This includes cases where the date exceeds valid calendar boundaries or has incorrect time components. For example, attempting to create a Date object with a non-existent date like 'October 33, 1996' will result in NaN (Section 2 of the provided documents).

The method's implementation checks for valid date inputs by attempting to extract the seconds component. If the date is invalid, this extraction fails, and NaN is returned (Section 1 of the provided documents). This allows developers to check for valid date inputs by verifying that the returned value is not NaN (Section 1 of the provided documents).

The maximum timestamp representable by a Date object is slightly smaller than Number.MAX_SAFE_INTEGER, corresponding to ±100,000,000 days around the epoch (Section 2 of the provided documents). Attempting to represent a time outside this range results in the Date object holding a timestamp value of NaN, which indicates an "Invalid Date" (Section 1 of the provided documents).


## Examples

Examples of valid and invalid date inputs demonstrate the method's behavior:

```javascript

const validDate = new Date("October 15, 1996, 05:35:32 UTC");

console.log(validDate.getUTCSeconds()); // Output: 32

```

While this date is valid and returns the correct seconds value, attempting to create a date with an invalid month:

```javascript

const invalidDate = new Date("October 33, 1996, 05:35:32 UTC");

console.log(invalidDate.getUTCSeconds()); // Output: NaN

```

This invalid date results in NaN, indicating an "Invalid Date" as per the specification.

For dates without specified time, the method returns 0:

```javascript

const midnightDate = new Date("October 13, 1996");

console.log(midnightDate.getUTCSeconds()); // Output: 0

```

Setting the date to a time that requires more than 60 seconds produces NaN:

```javascript

const invalidTimeDate = new Date("October 15, 1996, 05:35:60 UTC");

console.log(invalidTimeDate.getUTCSeconds()); // Output: NaN

```

This example demonstrates the method's validation of both date components and time values, ensuring the seconds are always within the expected range of 0-59.

