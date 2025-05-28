---

title: JavaScript Date getYear() Method

date: 2025-05-26

---


# JavaScript Date getYear() Method

The JavaScript Date getYear() method returns the year according to universal time, but its behavior varies significantly across different JavaScript versions and implementations, particularly in Internet Explorer. While once useful for retrieving years, this method is now deprecated in favor of getFullYear(), which provides more accurate and consistent year values. Understanding the intricacies of getYear() is crucial for developers working with JavaScript dates, especially when dealing with code that needs to be compatible with older browsers.


## getYear() Method Overview

The getYear() method returns the year in the specified date according to universal time. This method subtracts 1900 from the current year to determine the returned value. For example, in the year 2026, the method would return 2026.

The method has different behaviors based on the JavaScript version and implementation:

- In Internet Explorer 3.0 and earlier, the stored year is subtracted by 1900.

- In Internet Explorer 4.0 through 8 standards mode, the method returns either a 2-digit or 4-digit year based on the stored year.

- In Internet Explorer 9 standards mode, the stored year is subtracted by 1900.

The getYear() method returns 100 or greater for years 2000 and above, between 0 and 99 for years 1900-1999, and less than 0 for years below 1900. For instance, 1995 returns 95, 2000 returns 100, and 1800 returns -100.

The method can be used to set and get years between 1900 and 1999. For example, `xmas.setYear(95);` sets the year to 1995, and `const year = xmas.getYear();` returns 95.

The getYear() method is deprecated and may be removed from web standards, with the getFullYear() method providing the full year without requiring subtraction from 1900.


## getYear() Method Behavior

The getYear() method returns the year based on local time in an abbreviated format, using 1900 as the base year. For example, in the year 2026, the method would return 2026. This method subtracts 1900 from the current year to determine the returned value.

Developers must add 1900 to the result to obtain the correct year value, as this method is deprecated and should be replaced with getFullYear for new code development. The method's return value is an integer representing the year; JavaScript versions 1.2 and earlier return either a 2-digit or 4-digit year. For instance, 2026 returns 2026, 1976 returns 76, and 1800 returns -100.

Internet Explorer versions display different behaviors: versions 3.0 and earlier return stored year minus 1900, versions 4.0 through 8 standards mode return either a 2-digit or 4-digit year based on the stored year, and version 9 standards mode returns stored year minus 1900. The method effectively returns getFullYear minus 1900 and should not be used for new development due to its removal from web standards.


## Common Usage Example

The getYear() method can be used to retrieve the year from a JavaScript Date object. For example:

let date = new Date();

let year = date.getYear();

console.log(year);

For the current date, this would output 119. To obtain the full year, developers should add 1900 to the result.

The method's behavior varies for different years:

- For years 2000 and above, the method returns 100 or greater. For example, 2026 returns 126.

- For years between 1900 and 1999, the method returns a value between 0 and 99. For example, 1976 returns 76.

- For years below 1900, the method returns a value less than 0. For example, 1800 returns -100.

JavaScript versions 1.2 and earlier return either a 2-digit or 4-digit year. For instance:

let date = new Date("1995-12-25");

let year = date.getYear(); // returns 95

let date = new Date("2000-12-25");

let year = date.getYear(); // returns 100

let date = new Date("1800-12-25");

let year = date.getYear(); // returns -100

To set the year of a date object, you can use the setYear method:

let date = new Date();

date.setYear(95); // Sets the year to 1995

let year = date.getYear(); // Returns 95

The getYear() method has different behaviors across Internet Explorer versions:

- In Internet Explorer 3.0 and earlier, the stored year is subtracted by 1900.

- In Internet Explorer 4.0 through 8 standards mode, the method returns either a 2-digit or 4-digit year based on the stored year.

- In Internet Explorer 9 standards mode, the stored year is subtracted by 1900.


## Browser Support and Compatibility

The getYear() method's behavior varies across different Internet Explorer versions. Internet Explorer 3.0 and earlier versions return the stored year minus 1900. For versions 4.0 through 8, the method returns either a 2-digit or 4-digit year based on the stored year. In Internet Explorer 9 standards mode, the stored year is subtracted by 1900.

The method returns 100 or greater for years 2000 and above, between 0 and 99 for years 1900-1999, and less than 0 for years below 1900. For example, 2026 returns 126, 1976 returns 76, and 1800 returns -100. The return value is an integer representing the year; JavaScript versions 1.2 and earlier return either a 2-digit or 4-digit year.

Developers must add 1900 to the result to obtain the correct year value, as this method is deprecated and should be replaced with getFullYear for new code development. The method's return value is an integer representing the year, and JavaScript versions 1.2 and earlier return either a 2-digit or 4-digit year. For instance, if the year is 2026, the value returned by getYear() is 2026.


## Replacement Method: getFullYear()

The getFullYear() method provides a comprehensive solution for obtaining the full year without the need to subtract 1900. Unlike the deprecated getYear() method, getFullYear() consistently returns a four-digit number representing the year for dates between 1000 and 9999.


### Key Differences and Improvements

The getFullYear() method addresses several limitations of getYear():

- It provides a four-digit year format, eliminating the need for developers to add 1900.

- It returns accurate values for all years between 1000 and 9999.

- It maintains consistent behavior across all supported browsers, with widespread support dating back to July 2015.


### Usage Example

Here's how to use getFullYear() in JavaScript:

```javascript

let currentYear = new Date().getFullYear();

console.log(currentYear); // Outputs the current full year

```

This example demonstrates obtaining the current year using getFullYear(), providing a clear and reliable alternative to the deprecated getYear() method.

