---

title: JavaScript Date getMonth Method

date: 2025-05-26

---


# JavaScript Date getMonth Method

JavaScript's Date object provides a powerful set of tools for working with dates and times, including the getMonth() method. This method offers developers a simple way to retrieve the month from a date object, making it a fundamental building block for date-related applications. Whether you're building a calendar, implementing a time-tracking system, or simply need to display the current month, understanding how getMonth() works can significantly enhance your web development projects. This article explores the details of getMonth(), including its syntax, return value, and practical usage scenarios, equipping you with the knowledge to effectively work with dates in JavaScript.


## Method Overview

The getMonth() method returns the month in the specified date according to local time. The value returned by getMonth is an integer between 0 and 11, where 0 represents January and 11 represents December.

The method returns 0 for January and 11 for December, as demonstrated in the examples provided. When applied to an invalid date or an error value, getMonth returns NaN (Not a Number).

To convert the 0-based month index to a 1-based month number, add 1 to the result. For instance, if getMonth() returns 8, this corresponds to September.

Here's an example of retrieving the current month as a zero-based index:

```javascript

let currentDate = new Date();

let currentMonth = currentDate.getMonth();

console.log("Current Month (zero-based index):", currentMonth);

```

For applications requiring month names, an array can be used to map the numeric index to month names:

```javascript

const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

let currentMonthName = months[currentDate.getMonth()];

console.log("Current Month Name:", currentMonthName)

```

Using the toLocaleString() method allows formatting the date based on the user's locale, providing a flexible alternative to hardcoded month names.


## Syntax and Return Value

The getMonth() method is a built-in function in JavaScript's Date object that retrieves the month component of a specified date object, representing the month within the year. The return value is an integer between 0 to 11, where 0 indicates the first month of the year and 11 indicates the last month. If the provided Date object is an invalid date, this method returns Not a Number (NaN) as the result. The method does not accept any parameters and always returns an integer representing the month of the specified date object.

The syntax for the method is straightforward: getMonth().

For example:

```javascript

const currentDate = new Date();

const currentMonth = currentDate.getMonth();

console.log(currentMonth);

```

This will output the current month as a zero-based index. To convert this to a 1-based month number, simply add 1 to the result. For instance, a return value of 8 would correspond to September.

The method returns 0 for January and 11 for December. Here's a practical example:

```javascript

const december = new Date('December 15, 1996 05:35:32');

const currentMonth = december.getMonth();

console.log(currentMonth); // Output: 11

```

Alternatively, you can use the toLocaleString() method for formatting based on the user's locale:

```javascript

const december = new Date('December 15, 1996 05:35:32');

const formattedDate = december.toLocaleString("default", { month: "long" });

console.log(formattedDate); // Output: "December"

```


## Example Usage

The getMonth() method returns the month of the date as an integer between 0 and 11, where 0 represents January and 11 represents December, as documented in the MDN Web Docs.

When creating a new Date object without specifying a date and time, it defaults to the current date and time based on the user's system settings. Calling getMonth() on this object retrieves the current month as a zero-based index, where 8 represents September.

To obtain a more user-friendly month name, you can map the numeric index to an array of month names or use the toLocaleString() method with appropriate options. For example:

```javascript

let currentDate = new Date();

let currentMonthName = currentDate.toLocaleString("default", { month: "long" });

console.log("Current Month Name:", currentMonthName);

```

This approach allows for localization and flexible date formatting based on the user's locale setting.

The method returns NaN for invalid dates or extreme timestamps, making it useful for validating date objects before extracting other components. For instance, attempting to convert the invalid date "December 33, 1996" results in a NaN value:

```javascript

let december = new Date('December 33, 1996 05:35:32');

let month = december.getMonth();

console.log(month); // Output: NaN

```

Understanding the zero-based index simplifies date manipulation and array-based operations, as demonstrated in the following example:

```javascript

const currentDate = new Date();

const month = currentDate.getMonth();

const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

console.log(monthNames[month]); // Output: The name of the current month

```

The method's return value of 0 for January ensures compatibility with array indexing, making it a practical choice for date-related calculations and data manipulation tasks.


## Browser Support

The getMonth() method is supported across all major browsers, including Chrome, Edge, Firefox, Safari, Opera, and Internet Explorer. This compatibility ensures that developers can rely on the method's functionality regardless of the user's chosen browser.

The method's behavior with different types of input demonstrates its robustness:

- When given a valid date (e.g., "October 15, 1996 05:35:32"), it returns the correct month as an integer (0-11).

- For invalid dates or extreme timestamps (like "October 33, 1996"), it returns NaN, allowing developers to check for valid date objects before extraction.

- In cases where no specific date is provided (i.e., using `new Date()`), it returns the current month based on the user's system settings, making it practical for many applications.

The method's implementation across browsers maintains consistency in handling date creation and coercion. For instance, passing arrays to the Date constructor, while discouraged, works consistently across implementations, returning an invalid date (NaN) for improper input and local time dates for valid arguments.


## Related Methods

The getMonth() method belongs to the broader family of JavaScript Date methods designed to extract specific components from date objects. These related methods include getFullYear(), which returns the year as a four-digit number, getDate(), which provides the day of the month as a number between 1 and 31, and getHours(), which returns the hour of the day in 24-hour format.

The Date object constructor creates date instances with various options, including the ability to create a new date from the current time, a string representation, an epoch timestamp, or individual date and time components. When creating a date, the month is represented as a zero-based index, where 0 corresponds to January and 11 to December.

Basic Date manipulation methods include getSeconds() for retrieving seconds (0-59), getMilliseconds() for milliseconds (0-999), and getTime() for returning the date as the number of milliseconds since January 1, 1970, at 00:00:00 UTC. The getTimezoneOffset() method provides the difference in minutes between local time and UTC time.

For applications requiring internationalization, the Date object includes several localization methods. These methods return localized strings when called with appropriate locale options, such as toLocaleDateString() and toLocaleTimeString(). The toUTCString() method returns the date in generalized RFC 7231 format, while toISOString() provides an ISO 8601 format string.

Additional methods allow retrieval of UTC (Coordinated Universal Time) equivalents for all date components, using suffixes like getUTCDay() for the weekday and getUTCFullYear() for the year. These methods return values relative to UTC time, which can differ from local time by up to 24 hours.

