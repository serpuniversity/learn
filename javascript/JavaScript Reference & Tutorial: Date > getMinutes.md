---

title: JavaScript Date getMinutes() Method

date: 2025-05-26

---


# JavaScript Date getMinutes() Method

Understanding how to work with dates and times in JavaScript is crucial for building dynamic web applications. From displaying current timestamps to implementing complex calendar features, JavaScript's Date object provides the necessary tools. This article focuses on one specific aspect of date manipulation: extracting the minutes component from a Date object using the getMinutes() method. We'll explore the method's syntax and usage, examine its return values and behavior with different date inputs, and demonstrate how it interacts with other Date object methods. Along the way, we'll see practical examples of how this method can be used in real-world JavaScript applications.


## Syntax and Usage

The getMinutes() method returns the minutes value in a Date object using local time. The required dateObj reference is a Date object, and it returns an integer between 0 and 59 equal to the minutes value stored in the Date object.

A zero is returned in two situations: when the time is less than one minute after the hour, or when the time was not stored in the Date object when the object was created. The only way to determine which situation you have is to also check the hours and seconds for zero values. If they are all zeroes, it is nearly certain that the time was not stored in the Date object.

The method returns an integer between 0 and 59. It extracts the minutes portion of the date object based on the system's local time zone. When no date is provided as an argument, it returns the minutes component of the Date object it is called on, based on local time. If the Date object is invalid, this method returns NaN as a result.

For example, if you create a Date object representing a specific time and call getMinutes(), you can retrieve the minutes component of that date. Here's an example demonstrating its functionality:

```javascript

const specificDate = new Date('2023-12-25 12:45:30');

const minutes = specificDate.getMinutes();

console.log(minutes); // Output: 45

```

The method is available across major browsers, including Chrome, Edge, Firefox, Safari, and Opera, since the release of JavaScript 1.0. It's part of the ECMAScript 2026 Language Specification and provides consistent functionality across modern JavaScript environments.

When used in conjunction with other Date object methods like getHours() and getSeconds(), getMinutes() allows developers to extract precise time information from Date objects for various applications. The method's reliability in returning zero values when time data is missing enables more accurate date and time processing in JavaScript applications.


## Return Value

The getMinutes() method consistently returns an integer value between 0 and 59, representing the minutes component of the specified date object according to local time. The value returned is directly derived from the minutes portion of the date object's timestamp, providing a straightforward way to extract time information.

The method's reliability in returning zero values when time data is missing enables accurate date and time processing in JavaScript applications. When the time is less than one minute after the hour or when no time information was stored in the Date object at creation, the method returns 0. This behavior provides developers with consistent zero values that can be used to determine if time information is missing from a Date object.

For example, creating a Date object with a time of 05:35:32 results in getMinutes() returning 35, while creating an object with a time less than one minute after the hour (e.g., 05:00:01) results in a 0 value. Similarly, when no minutes information is stored (such as when creating a Date object with the default timestamp), getMinutes() returns 0, allowing developers to determine if time information is missing from the Date object.


## Example Usage

The getMinutes() method provides consistent functionality across all major browsers, including Chrome, Edge, Firefox, Safari, and Opera. As demonstrated in the official documentation, the method has been available since the release of JavaScript 1.0 and is part of the ECMAScript 2026 Language Specification.

The method's reliability in returning zero values when time data is missing enables accurate date and time processing in JavaScript applications. When the time is less than one minute after the hour or when no time information was stored in the Date object at creation, the method consistently returns 0. This behavior provides developers with consistent zero values that can be used to determine if time information is missing from a Date object.

For example, creating a Date object with a time of 05:35:32 returns 35, while creating an object with a time less than one minute after the hour (e.g., 05:00:01) returns 0. Similarly, when no minutes information is stored (such as when creating a Date object with the default timestamp), getMinutes() returns 0, allowing developers to determine if time information is missing from the Date object.

Additional examples demonstrate the method's functionality across valid and invalid date inputs. When the date of the month exceeds 31 (October 35, 1996, 05:35:32), the method correctly returns NaN, as no date can have a month greater than 31. When no minutes are explicitly set (October 12, 1996), the method returns 0, providing a clear indication that time information is missing.


## Method Implementation

The getMinutes() method has been available across major browsers since 1996, aligning with JavaScript 1.0 release (Mozilla JavaScript 1.0 Specification). It is formally standardized in the ECMAScript 2026 Language Specification, ensuring consistent implementation across the latest JavaScript environments.


### Browser Support and Implementation

The method demonstrates strong cross-browser compatibility, supported in all major browsers including Chrome, Edge, Firefox, Safari, and Opera. Official support dates back to Firefox 1, Google Chrome 1, Internet Explorer 4, Opera 3, and Safari 1, establishing robust foundation for its implementation across the web ecosystem.


### Method Behavior and Edge Cases

For invalid date inputs, the method returns NaN, as demonstrated by attempting to create a Date object with an invalid month value (e.g., October 35, 1996, 05:35:32). It consistently returns 0 for times less than one minute past an hour or when minutes information is missing during Date object creation (e.g., October 12, 1996).


### Additional Implementation Notes

When extracting time components for display purposes, the method's direct integer output can be formatted into two-digit strings using various approaches. Common techniques include simple string concatenation (date.getMinutes() < 10 ? '0' : '') or string replacement methods (date.getMinutes().toString().replace(/^(\d)$/, '0$1')). More sophisticated implementations combine this with date parsing techniques, as shown in the following example:

```javascript

function twoDigitMinutes(date_string) {

  const date = new Date(date_string);

  let min = date.getMinutes();

  if (min < 10) {

    min = '0' + min;

  }

  return min;

}

```

This implementation ensures formatted output while maintaining proper integer handling, avoiding the limitations of direct string length checks. The method's reliability in returning 0 for missing time data enables accurate date and time processing across JavaScript applications.


## Date Object Components

JavaScript's Date object represents a specific point in time and provides methods to retrieve various components of that date. The getMinutes() method is part of this larger set of time-extraction methods, alongside getHours(), getSeconds(), and getMilliseconds().

The Date object itself can be created using either a full date and time specification (e.g., "March 13, 08 04:20") or a Unix timestamp representing the number of milliseconds since January 1, 1970. This timestamp-based approach allows JavaScript to represent dates as a single numeric value, which can be interpreted as either local time or Coordinated Universal Time (UTC) based on the host environment.

When working with date objects, developers can access multiple time components using dedicated methods:

- getFullYear() and setFullYear() retrieve and manipulate the year component

- getMonth() and setMonth() retrieve and manipulate the month component (0-11, January = 0)

- getDate() and setDate() retrieve and manipulate the day of the month (1-31)

- getDay() retrieves the day of the week as a number (0-6)

- getHours(), getMinutes(), getSeconds(), and getMilliseconds() retrieve the respective time components as integers

The getMinutes method specifically handles the minutes component, returning an integer between 0 and 59. When extracting time information, developers often use these local time methods in combination to build comprehensive date and time representations. For example, the following code snippet demonstrates how to construct a full date string:

```javascript

const date = new Date();

const year = date.getFullYear();

const month = date.getMonth() + 1; // Months are 0-indexed

const day = date.getDate();

const hours = date.getHours();

const minutes = date.getMinutes();

const seconds = date.getSeconds();

console.log(`${year}-${month}-${day} ${hours}:${minutes}:${seconds}`);

```

This combination of local time methods enables developers to extract and format date information according to their specific requirements, supporting a wide range of applications from simple time tracking to complex calendar implementations.

