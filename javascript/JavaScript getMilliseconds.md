---

title: JavaScript Date: getMilliseconds() Method

date: 2025-05-26

---


# JavaScript Date: getMilliseconds() Method

JavaScript's Date object offers extensive functionality for handling dates and times. From retrieving the current system time to parsing and manipulating specific date components, these methods provide developers with powerful tools for working with dates in their applications. This article focuses on the getMilliseconds() method, examining its basic usage, handling of invalid dates, and its counterpart getUTCMilliseconds(). Through practical examples and detailed explanations, we'll explore how this method can be effectively used in JavaScript programming.


## Basic Usage

The getMilliseconds() method returns an integer between 0 and 999 representing the milliseconds component of a date according to local time. For example, creating a Date object for June 10, 2023 at 15:50:45.500 and calling getMilliseconds() would return 500.

Milliseconds are represented as follows:

- 0 represents the beginning of the second

- 999 represents the end of the second

When constructing a Date object without specifying milliseconds, the value defaults to 0. For instance, creating a Date for "October 13, 1996 05:35:32" yields 0 milliseconds.

Calling getMilliseconds() on an invalid Date object returns NaN. An example is provided using a date string "October 33, 1996 05:35:32:77", which results in NaN when getMilliseconds() is applied.

The method can also be used to retrieve the current milliseconds value from the system clock. This is demonstrated in the example HTML code snippet, which displays the current milliseconds value when the "Get Milliseconds" button is clicked.


## Example with Current Date

The getMilliseconds() method returns an integer between 0 and 999 representing the milliseconds component of a date according to local time. For a current example, creating a Date object and calling this method directly returns the current system milliseconds. The following code demonstrates this:

```javascript

let DateObj = new Date();

let millisec = DateObj.getMilliseconds();

console.log(millisec); // Outputs current system milliseconds

```

The method retrieves milliseconds accurately, with examples showing consistent results. When applied to a specific date like "October 13, 1996 05:35:32", it correctly returns 0, and for "October 33, 1996 05:35:32:77", it properly returns NaN when the date is invalid.


## Invalid Date Handling

The getMilliseconds() method returns an integer between 0 and 999 representing the milliseconds for the date according to local time. The method returns 0 if the milliseconds component is not specified in the date object. When attempting to retrieve milliseconds from an invalid Date object, the method returns NaN.

For example, creating a Date object with a specific time "October 13, 1996 05:35:32" returns 0 for the milliseconds component. Similarly, constructing a Date object with "October 15, 1996 05:35:32:77" returns 77 for the milliseconds component. Attempting to create a Date object with an invalid date string "sagtrjdh" using getUTCMilliseconds() also returns NaN, demonstrating proper error handling for invalid inputs.

The method correctly handles out-of-range values by returning 0 when the specified milliseconds exceed 999. For instance, creating a Date object with "October 13, 1996 05:35:32:1003" returns 1003, but the method caps this value at 0, ensuring valid output.


## Milliseconds vs. UTC Milliseconds

According to the documentation, the getMilliseconds() method returns the milliseconds of a date according to local time, while the getUTCMilliseconds() method returns the milliseconds of a date according to universal time.

The getUTCMilliseconds() method accepts no parameters and returns an integer between 0 and 999 representing the milliseconds for the given date according to universal time. This method is supported across many devices and browser versions, with compatibility since July 2015.

For example, creating a Date object for "July 20, 1969 00:20:18" and calling getUTCMilliseconds() returns 18. This demonstrates that the method accurately retrieves the UTC milliseconds value.

The getUTCMilliseconds() method can be used in conjunction with other UTC methods to manipulate and retrieve the components of a date object while working with universal time. For instance, setting the UTC milliseconds of a date object can be done using setUTCMilliseconds(), allowing precise control over date components when working with universal time.


## Additional Methods

Related methods provide comprehensive manipulation capabilities for JavaScript dates and times. The setMilliseconds() method allows setting the milliseconds component of a date object, while getMinutes(), getSeconds(), and getHours() provide corresponding functionality for other time components.

The getTime() method returns the number of milliseconds since January 1, 1970, providing a timestamp representation of the date object. This method is widely available across devices and browser versions, with compatibility since July 2015.

Additional details on date creation and manipulation include support for multiple constructor formats, such as strings in ISO 8601 format, individual year, month, day, hour, minute, and second parameters, and epoch timestamps. The constructor can be called as a function to return the current date and time as a string.

The Date object also provides static methods for time calculations and parsing, including Date.now() for current time in milliseconds, Date.parse() for parsing string representations, and Date.UTC() for universal time calculations with the same parameter formats as the constructor.

For date formatting, the object includes methods for string representation (toString()), date-specific formatting (toDateString()), time-specific formatting (toTimeString()), and ISO 8601 formatting (toISOString()). Locale-specific formatting options are available through toLocaleString(), toLocaleDateString(), and toLocaleTimeString() methods.

