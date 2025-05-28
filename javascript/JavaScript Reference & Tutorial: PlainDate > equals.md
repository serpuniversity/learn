---

title: JavaScript Temporal.PlainDate.equals(): Method and Usage

date: 2025-05-27

---


# JavaScript Temporal.PlainDate.equals(): Method and Usage

JavaScript's Temporal API introduces powerful new capabilities for working with dates and times, including support for multiple calendar systems. At its core, the Temporal.PlainDate object represents a calendar date without time or timezone information, allowing detailed control over how dates are represented and compared. This article explores the equals() method, which determines whether two PlainDate instances represent the same calendar date while considering both the date values and the calendar system used. Through practical examples and detailed explanations, we demonstrate how this method enables accurate date comparisons across different calendar systems while maintaining the core functionality needed for everyday date operations.


## Introduction to Temporal.PlainDate

The Temporal.PlainDate object represents a calendar date in JavaScript without associated time or timezone information, fundamentally as an ISO 8601 calendar date with year, month, and day fields. It can be constructed using either its constructor or the static from method, with the constructor accepting year, month, and day as parameters along with an optional calendar specification.

The object stores date values in ISO 8601 format, allowing creation through various means such as the Temporal.Now.plainDateISO() function for the current date in ISO format or Temporal.Now.plainDate("persian") for the current Persian calendar date. Additionally, Date objects can be converted to PlainDate instances using methods like toTemporalInstant() followed by conversion to Temporal.PlainDate.

The API supports multiple calendar systems through the calendar parameter, with options including "gregory", "islamic", and "iso8601". This feature allows for accurate date representation across different cultures and historical periods, ensuring that January is always represented by 1 and months range from 1-12 rather than 0-11 as in traditional JavaScript Date objects.


## The equals() Method

The equals() method determines whether two PlainDate instances represent the same calendar date, considering both the date values and the calendar system used. It takes a single parameter - other, which can be a string, an object, or another Temporal.PlainDate instance.

The method returns true if the two dates are equivalent in both their value and calendar system, and false otherwise. For example, a PlainDate from "2021-08-01" will equal another created from { year: 2021, month: 8, day: 1 }, but will not equal a date from the Japanese calendar created with the same string "2021-08-01[u-ca=japanese]".

This comparison mechanism ensures that dates from different calendar systems are treated distinctly, though two dates in different calendars but representing the same ISO date (like Gregorian August 1st and the corresponding Islamic calendar date) would be considered equal by the compare() method, which ignores calendar differences.


## Comparison with Other Date Systems

The equals() method compares PlainDate objects with other date systems through a careful consideration of both date values and calendar systems. This ensures that dates from different calendar systems are treated distinctly despite potentially representing the same ISO 8601 date.

For example, a PlainDate object created from "2021-08-01" will be considered equal to another created from the object { year: 2021, month: 8, day: 1 } because they represent the same ISO 8601 date. However, attempting to compare these with a date in a different calendar system, such as "2021-08-01[u-ca=japanese]", will result in a false comparison, as the equals() method takes the specific calendar into account.

This comparison mechanism is particularly useful when working with multi-calendar applications, where dates from different systems need to be compared while maintaining their calendar-specific properties. The method's strict calendar comparison ensures that dates are only considered equal when their ISO 8601 values and calendar systems match.

When comparing PlainDate objects with PlainDateTime objects, the comparison focuses solely on the date components, ignoring any time information. This allows for accurate comparison between date-only and date-time values while maintaining the calendar-specific comparison behavior.


## Example Usage

To demonstrate the creation and comparison of PlainDate objects, consider the following examples:

```javascript

const date1 = Temporal.PlainDate.from('2021-08-01');

const date2 = Temporal.PlainDate.from({ year: 2021, month: 8, day: 1 });

console.log(date1.equals(date2)); // true

const date3 = Temporal.PlainDate.from('2021-08-01[u-ca=japanese]');

console.log(date1.equals(date3)); // false

const date4 = Temporal.PlainDate.from('2021-08-02');

console.log(date1.equals(date4)); // false

```

In these examples, date1 is created from an ISO format string, while date2 uses the object-based constructor. Both are compared to date1 using the equals() method, demonstrating the method's ability to handle different input formats.

The comparison with date3 shows how dates across different calendar systems are treated distinctly, even when they represent the same ISO 8601 date. Finally, comparing date1 to date4 illustrates the method's strict equality check, returning false despite the dates being consecutive.

This functionality is particularly useful in applications requiring precise date comparisons across multiple calendar systems, ensuring that dates are only considered equal when their calendar systems and ISO 8601 values match.

