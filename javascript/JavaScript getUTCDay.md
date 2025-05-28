---

title: JavaScript Date getUTCDay() Method

date: 2025-05-26

---


# JavaScript Date getUTCDay() Method

The JavaScript Date getUTCDay() method serves as a crucial tool for date manipulation, particularly when dealing with time zone conversions and international date standards. By returning the day of the week as an integer according to Universal Coordinated Time (UTC), this method enables developers to create applications that accurately interpret and display dates across different time zones. This article provides an in-depth exploration of the getUTCDay() method, examining its syntax, parameters, return values, and compatibility across major browsers. Additionally, we'll examine common usage patterns and potential challenges when working with date-related operations in JavaScript.


## Date.getUTCDay() Method Overview

The getUTCDay() method returns the day of the week for a given date according to Universal Coordinated Time (UTC), where 0 represents Sunday. For example, if today is Sunday, January 1, 2023, at midnight UTC, getUTCDay() would return 0. The method takes no parameters and returns an integer value between 0 and 6, representing Sunday through Saturday, respectively.

The method utilizes UTC time by default, meaning that date-only forms of ISO 8601 format (such as "YYYY-MM-DD") are interpreted as UTC, while date-time forms (including time components) are treated as local time. This behavior can lead to discrepancies between local and UTC time zones, as demonstrated by the difference in returned values for the same date in Quebec City (GMT-0500), where February 18, 2019, is represented as Monday (1) in getUTCDay() and Sunday (0) in getDay().

JavaScript's Date object uses the ECMAScript specification for its implementations, with specific details outlined in "sec-date.prototype.getutcday". The method has been available across major browsers since July 2015 and consistently returns values between 0 and 6, with 0 representing Sunday and 6 representing Saturday. All major browsers including Chrome, Edge, Firefox, Internet Explorer, Opera, and Safari support the method, with compatibility extending back to version 1 for many browsers.


## Syntax and Parameters

The getUTCDay() method can be called as a property of a Date object or as a static method of the Date object itself. When called as a property, it returns the day of the week for the specified date according to Universal Coordinated Time (UTC), with 0 representing Sunday. When called as a static method, it requires a date value in UTC.

The method accepts the same format arguments as the Date constructor, allowing for the creation of Date objects from various date representations. Supported formats include:

- Year (YYYY)

- Year-Month (YYYY-MM)

- Year-Month-Day (YYYY-MM-DD)

- Date-Time (date-only form followed by T, then HH:mm, HH:mm:ss, or HH:mm:ss.sss, with optional time zone offset)

When a date-only form is provided, the method interprets the input as UTC time. For date-time forms, it treats the input as local time. This behavior aligns with JavaScript's interpretation of ISO 8601 calendar date extended format (YYYY-MM-DDTHH:mm:ss.sssZ), where date-only forms are interpreted as UTC.

The method supports construction using the Date constructor with one to seven arguments, representing year, month, day, hour, minute, second, and millisecond respectively. For date-time formats, the month argument is interpreted as UTC, while for date-only formats, the day argument is also interpreted as UTC.

The method handles date component overflow and underflow as follows:

- Months overflow to the next year: December becomes January

- Days underflow to the previous month: 0 becomes the last day of the previous month

- Unspecified components default to midnight of the current day: For example, calling getUTCDay() with just a year argument returns the day of the week for January 1 of that year.


## Return Value and Range

The getUTCDay() method consistently returns an integer value between 0 and 6, corresponding to Sunday through Saturday respectively. This behavior is documented across multiple sources, including the ECMA-262 specification and MDN Web Docs.

The method's return value directly maps to the days of the week as follows:

0 = Sunday

1 = Monday

2 = Tuesday

3 = Wednesday

4 = Thursday

5 = Friday

6 = Saturday

This consistent behavior has been available across major browsers since July 2015 and continues to function as described in all modern implementations. The method's return value is based on the local time provided to the Date object, with the day of the week calculation performed using UTC time internally.


## Examples and Usage

The getUTCDay() method returns the day of the week in the specified date according to universal time, as an integer value from 0 - 6, where 0 represents Sunday. For example, calling this method on a date object representing January 1, 2023, would return 0.

Here's a common usage pattern:

```javascript

const date = new Date();

console.log(date.getUTCDay()); // Returns the day of the week as an integer (0-6)

```

To convert the integer representation to a more human-readable format, you can use a switch statement:

```javascript

const day = date.getUTCDay();

switch(day) {

  case 0: console.log("Sunday"); break;

  case 1: console.log("Monday"); break;

  case 2: console.log("Tuesday"); break;

  case 3: console.log("Wednesday"); break;

  case 4: console.log("Thursday"); break;

  case 5: console.log("Friday"); break;

  case 6: console.log("Saturday"); break;

}

```

JavaScript's Date object handles date component overflow and underflow as follows:

- Months overflow to the next year: December becomes January

- Days underflow to the previous month: 0 becomes the last day of the previous month

- Unspecified components default to midnight of the current day: For example, calling getUTCDay() with just a year argument returns the day of the week for January 1 of that year


## Browser Support

The getUTCDay() method returns the same value across all major browsers, including Chrome, Edge, Firefox, Internet Explorer, Opera, and Safari, with support available since version 1 for many browsers. The method's return value is consistent across implementations, consistently returning an integer value between 0 and 6, where 0 represents Sunday and 6 represents Saturday.

While JavaScript's Date object methods generally return a timestamp in the local time zone, the getUTCDay() method specifically returns values based on Universal Coordinated Time (UTC). This means that date-only forms of ISO 8601 format are interpreted as UTC time, while date-time forms are treated as local time. However, this behavior can lead to discrepancies between local and UTC time zones as demonstrated by the difference in returned values for the same date in Quebec City (GMT-0500), where February 18, 2019, is represented as Monday (1) in getUTCDay() and Sunday (0) in getDay().

The method's reliability extends to handling date component overflow and underflow, with months overflowing to the next year and days underflowing to the previous month. Unspecified components default to midnight of the current day, as demonstrated by the method returning the day of the week for January 1 of a given year when only the year argument is provided.

