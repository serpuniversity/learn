---

title: JavaScript Temporal.PlainDateTime.dayOfWeek

date: 2025-05-27

---


# JavaScript Temporal.PlainDateTime.dayOfWeek

In the evolving landscape of JavaScript date and time handling, the Temporal API stands out as a promising solution to long-standing limitations of the existing Date object. Among its numerous enhancements, one particularly interesting feature is the Temporal.PlainDateTime.dayOfWeek property, which bridges the gap between technical standards and cultural practices in determining how we measure days of the week.

This property returns a positive integer representing the 1-based day index in the week of the date, following the ISO 8601 standard where Monday is typically considered the first day of the week. However, JavaScript's approach to date manipulation has always been a patchwork of workarounds to address its fundamental deficiencies in calendar and time zone support.

The Temporal API represents a significant step forward by providing a comprehensive framework for handling multiple calendar systems, time zones, and precise date operations. Through the dayOfWeek property and its related methods, developers can now work with dates in a more structured and culturally sensitive manner.

From building functions to find the next or previous occurrence of a specific day of the week to understanding how Temporal integrates with other date components like dayOfYear and weekOfYear, this article explores the practical applications and technical details of the dayOfWeek property. Along the way, we'll examine how JavaScript's new date handling capabilities expand the possibilities for accurate and culturally aware date manipulation.


## Temporal.PlainDateTime.dayOfWeek Property

The dayOfWeek property returns a positive integer representing the 1-based day index in the week of the date. The week starts at 1 and is numbered sequentially from 1 to daysInWeek, with each number mapping to its name. For ISO 8601, 1 usually represents Monday, but this can vary by locale.

Days in a week are numbered according to the calendar system in use, with ISO week 1 being the week containing the first Thursday of the year. The ISO week number system uses ISO week date format, where the week is a positive integer that increments by 1 every time, starting at 1 and resetting to 1 as the year advances.

The value of dayOfWeek is calendar-dependent and cannot be directly modified through the set accessor, which is undefined. To change the dayOfWeek value, use add() or subtract() methods with appropriate day values.

The number of days in a week is determined by the daysInWeek property, which is always 7 for the ISO 8601 calendar but may differ in other calendar systems on a weekly basis. The week concept varies across cultures and calendars, with common lengths of 7 days but also 4, 5, 6, 8, or more days, or even no fixed number of days.

The first day of the week is typically Monday in the calendar, even when locales may consider a different day as the first day of the week. The property is part of the Temporal.PlainDateTime prototype and is documented in the Temporal API for general information and examples.


## Calendar and Weekday Relationships

The concept of a week varies across cultures and calendar systems, with common lengths of 7 days but also 4, 5, 6, 8, or more days, or even no fixed number of days (MDN Web Docs, n.d.). The ISO 8601 calendar system uses a 7-day week, starting with Monday as the first day of the week (Intl.Locale.prototype.getWeekInfo, n.d.).

The week is a cultural construct that affects how days are numbered in Temporal.date objects. The dayOfWeek property returns a 1-based index representing the position of the day in the week, with the value calculated based on the calendar system in use (MDN Web Docs, n.d.). For example, in ISO 8601, the first day of the week is Monday, but this can vary based on locale-specific settings (Intl.Locale.prototype.getWeekInfo, n.d.).

The week concept influences other Temporal properties and methods, such as dayOfYear, daysInWeek, and weekOfYear. The weekOfYear property represents the ISO week number, which is a positive integer that increments by 1 every time, starting at 1 and resetting to 1 as the year advances (MDN Web Docs, n.d.). The yearOfWeek property gives the ISO "week calendar year" of the date, which is generally the same as the standard year property but may differ at the start or end of each year due to weeks crossing year boundaries (MDN Web Docs, n.d.).

The Temporal API treats the week as a fundamental unit of time organization, providing methods for working with weekly periods while recognizing the diversity of calendar systems and cultural practices (MDN Web Docs, n.d.). This approach allows developers to work with dates and times in a flexible way that respects the varied ways humans organize their calendars (MDN Web Docs, n.d.).


## Usage and Manipulation

To change the dayOfWeek value, use add() or subtract() methods with appropriate day values. The set accessor is undefined, meaning this property cannot be directly modified.

For example, to change the day of the week, you need to first calculate the difference in days to your desired day of the week, then use the add() or subtract() method to adjust the date accordingly. Here are some functions demonstrating this approach:

```javascript

// Change to the next occurrence of a specific day

function getNextDayInWeek(date, destDayOfWeek) {

  const distance = destDayOfWeek - date.dayOfWeek;

  return date.add({ days: distance < 0 ? date.daysInWeek + distance : distance });

}

// Change to the previous occurrence of a specific day

function getPreviousDayInWeek(date, destDayOfWeek) {

  const distance = destDayOfWeek - date.dayOfWeek;

  return date.add({ days: distance < 0 ? distance : date.daysInWeek + distance });

}

// Example usage

console.log(getNextDayInWeek(Temporal.PlainDate.from("2021-07-01"), 5).toString()); // 2021-07-02

console.log(getPreviousDayInWeek(Temporal.PlainDate.from("2021-07-03"), 5).toString()); // 2021-07-01

```

These functions allow precise control over date adjustments while respecting the calendar's week structure.


## Temporal API Overview

The Temporal API builds on JavaScript's existing Date object but provides significantly more robust functionality, particularly in handling calendar systems and week calculations. While the Date object lacks support for calendar systems beyond the Gregorian calendar, time zones, and the concept of "no time zone" (calendar date or wall-clock time), Temporal offers comprehensive solutions for these needs.

The API consists of multiple classes and namespaces designed to handle specific aspects of date and time, including Duration, Time point, Instant, ZonedDateTime, PlainDateTime, PlainDate, PlainTime, PlainYearMonth, and PlainMonthDay. These classes provide a structured approach to representing and manipulating dates and times across different calendar systems and time zones.


### Key Features of Temporal

1. **Calendar Support**: Temporal extends JavaScript's date functionality to support multiple calendar systems, including Gregorian, Hebrew, and Chinese calendars. This enables developers to work with dates in contexts where the standard Gregorian calendar may not be appropriate.

2. **Time Zone Handling**: The API includes robust support for time zones, allowing accurate representation of dates and times in different time zones. This is particularly important for applications that need to handle events or data from multiple regions.

3. **Date Component Access**: Temporal provides detailed access to date components through properties like day, month, year, hour, minute, second, millisecond, microsecond, and nanosecond. This level of granularity allows precise manipulation of date and time values.

4. **Date Manipulation Methods**: The API includes comprehensive methods for date manipulation, such as comparing dates (using Temporal.PlainDateTime.compare()), sorting date arrays, and combining date and time components (using Temporal.PlainDate.from() and Temporal.PlainTime.from()).

5. **Era Support**: For calendar systems that use eras (such as the Gregorian calendar with BCE/CE), Temporal provides properties for working with era information. This allows developers to handle dates in historical and modern contexts accurately.


### Implementation and Usage

To use Temporal functionality, developers need to employ a polyfill as it is not yet widely implemented in modern browsers. The API's functionality is still experimental, and some features may not be fully supported across all browsers and environments.

Browser implementation has limitations compared to standard Date object functionality. While Temporal provides powerful new capabilities, developers should test thoroughly to ensure compatibility with their target environments.


### Example Usage

The following code demonstrates creating a PlainDateTime object and accessing its properties:

```javascript

// Create a PlainDate object for May 14, 2020

let date = Temporal.PlainDate.from('2020-05-14');

// Combine with a time to create a PlainDateTime object

let dateTime = date.toPlainDateTime(Temporal.PlainTime.from({ hour: 12 }));

// Access properties

console.log(dateTime.day); // 14

console.log(dateTime.monthCode); // 'M05'

console.log(dateTime.year); // 2020

console.log(dateTime.hour); // 12

console.log(dateTime.minute); // 0

console.log(dateTime.second); // 0

console.log(dateTime.calendarId); // 'gregory'

```

This example illustrates the basic usage of Temporal.PlainDateTime, showing how to create and manipulate date-time objects while maintaining calendar-specific information.


## Browser Implementation


### Current Browser Support

As of now, the Temporal functionality is experimental and available through a polyfill in modern browsers, with limitations compared to standard Date object functionality. The polyfill can be loaded via GitHub, but implementation varies across browsers and environments (MDN Web Docs, n.d.).


### Time Zone Handling

The Temporal proposal addresses several limitations of the Date object, particularly in time zone handling. Unlike the Date object, Temporal provides robust support for time zones, allowing accurate representation of dates and times in different time zones (MDN Web Docs, n.d.).


### Compatibility with Date Object

Temporal builds on the existing Date object but provides significantly more robust functionality. While the Date object lacks support for calendar systems beyond the Gregorian calendar, time zones (with the exception of "no time zone" support), and the concept of "no time zone" (calendar date or wall-clock time), Temporal offers comprehensive solutions for these needs (MDN Web Docs, n.d.).


### Implementation Considerations

When using Temporal functionality, developers should be aware of the following limitations compared to the standard Date object:

- Time zone operations require explicit specification, as the Date object's behavior can vary between browsers and implementations

- The polyfill handles basic functionality but may not support all advanced features

- Conversion between Temporal types and legacy Date objects requires careful consideration of time zone information

