---

title: JavaScript PlainDate Year Property

date: 2025-05-27

---


# JavaScript PlainDate Year Property

JavaScript's PlainDate class provides a robust way to handle dates without time or time zone information, supporting multiple calendar systems. This article explores the year property in detail, explaining how it functions across different calendar systems and how to work with year-based date manipulations.


## Overview of PlainDate and Year Property

The PlainDate class in JavaScript represents a date without time or time zone information, making it ideal for scenarios where the time component is irrelevant, such as scheduling events, birthdays, or historical date calculations. It supports multiple calendar systems, including ISO 8601, Japanese, and Hebrew calendars, providing flexibility for various regional and cultural date requirements.

The PlainDate object is initialized through a constructor that accepts a calendar identifier and a month value, with the calendar identifier defaulting to "iso8601". The class also includes a static from() method that can parse dates from strings or objects containing date properties. For instance, the from() method can create a PlainDate from an RFC 9557 string, another PlainDate object, or an object with calendar, day, era, and eraYear properties.

The PlainDate object includes several read-only properties that provide information about the date, including daysInYear, monthsInYear, and inLeapYear, which behave similarly to the era/eraYear pair as a unique identifier of a year in a calendar system. The year property specifically returns an integer representing the number of years relative to the start of the calendar's epoch year. For example, in the ISO 8601 calendar, the year 2021 is represented as 2021, while in the Japanese calendar, which uses eras, 2021 has the same value as the ISO year.

The PlainDate implementation handles out-of-range values through an overflow option that can either constrain values to the valid range or reject invalid dates, throwing a RangeError. This flexibility allows developers to choose the appropriate behavior for their applications based on specific requirements. The overall design simplifies date manipulation while maintaining calendar system compatibility, though adoption across browsers remains experimental at this stage.


## Year Property Value and Calendar Dependency

The year property of the PlainDate object represents an integer that indicates the number of years since a calendar-specific epoch. The value of this property is derived from either the year component directly or the combination of era and eraYear properties, depending on the calendar system.

In the ISO 8601 calendar, which serves as the default, the year property functions similarly to the calendar year, with the year 2021 represented as 2021. For calendar systems that employ eras, such as the Japanese calendar, the year property returns the same value as the ISO year, ensuring consistency between different calendar representations.

The calculation of the year property's value takes into account the calendar system's epoch year, which may be located at different points within the year. In the case of the Hebrew calendar, which begins its epoch in 3761 BC, the year 2021 is represented as 5781, reflecting the years elapsed since the epoch year. This system ensures that the year property can represent dates throughout the full span of a calendar's history, from its beginning to the present.

The year property is calendar-dependent and cannot be modified directly through a setter; instead, changes to the year require creating a new PlainDate object using the with() method. The implementation supports two overflow options: 'constrain', which limits values to the valid range, and 'reject', which throws a RangeError for out-of-range values. This approach enables developers to specify the desired behavior for handling invalid dates based on their specific requirements.


## Working with Year Property

The year property of a Temporal.PlainDate instance returns an integer representing the number of years since a calendar-specific epoch year. This property is calendar-dependent and functions similarly to the `era`/`eraYear` pair as a unique identifier of a year in a calendar. The property's value is relative to the start of the epoch year, not the epoch date. For calendar systems where the epoch is in the middle of the year, the year before and after the start date of the era share the same value.

The year property cannot be changed directly and has no set accessor. Instead, to create a new PlainDate object with a modified year, developers should use the `with()` method. This method enables setting specific properties while preserving existing values. For example, to increment the year by 10, one could use: const nextDecade = date.with({ year: date.year + 10 });

When working with day-related properties, developers should be aware of the `daysInYear`, `daysInMonth`, and `daysInWeek` properties, which vary depending on the calendar system in use. The `dayOfYear` property provides the 1-based day index in the year, with the first day being 1 and the last day determined by the `daysInYear` property. This property is also calendar-dependent and cannot be directly modified.

To perform date comparisons, the PlainDate class includes a static `from()` method and a `compare()` instance method. The `from()` method creates new PlainDate objects from various inputs, including other PlainDate objects, plain JavaScript Date objects, or strings in RFC 9557 format. The `compare()` method returns -1, 0, or 1 based on whether one date comes before, matches, or comes after another, respectively. This comparison method ignores calendar differences and uses monthCode for calendar-independent comparison.

The PlainDate class requires careful handling of out-of-range values through its overflow options. When attempting to create a date with invalid values, the implementation can either throw a RangeError (using the 'reject' option) or constrain the values to the valid range (using the 'constrain' option). This flexibility allows developers to choose the appropriate error handling behavior for their applications based on specific requirements.


## Year Property and Calendar Systems

The `year` property of Temporal.PlainDate functions differently across various calendar systems:

- **ISO 8601 Calendar**: The year 2021 is represented as 2021, similar to the standard calendar year format.

- **Japanese Calendar**: This calendar system uses eras, so the year 2021 has the same value as the ISO year (2021).

- **Hebrew Calendar**: Using the Anno Mundi epoch starting in 3761 BC, the year 2021 is represented as 5781. This system accounts for the years elapsed since the epoch year.

The `year` property is calendar-dependent and cannot be modified directly through a setter. To create a new PlainDate object with a different year, developers should use the `with()` method. For example, to increment the year by 10, one would use: `const nextDecade = date.with({ year: date.year + 10 })`.

When working with day-related properties, developers need to consider the calendar system's specific characteristics:

- `daysInYear`, `daysInMonth`, and `daysInWeek` properties vary depending on the calendar system in use.

- `dayOfYear` provides the 1-based day index in the year, with the first day being 1 and the last day determined by `daysInYear`.

The `dayOfYear` property gives the ordinal day of the year, ranging from 1 to 365 or 366 in a leap year. For ISO 8601 dates, it can be used to determine the weekday number (1-7) with Monday=1 and Sunday=7.

Temporal.PlainDate instances can be created using the constructor with specific calendar systems, such as "chinese". When creating a PlainDate object with a particular calendar system, the date is passed as ISO 8601 while maintaining the specified calendar system.

The `from()` static method creates new PlainDate objects from various inputs, including other PlainDate objects, plain JavaScript Date objects, or strings in RFC 9557 format. This method accepts one of the following parameters:

1. A PlainDate instance, creating a copy of the instance.

2. A PlainDateTime instance, providing the calendar date in the same fashion as PlainDateTime.prototype.toPlainDate().

3. A ZonedDateTime instance, providing the calendar date in the same fashion as ZonedDateTime.prototype.toPlainDate().

4. An RFC 9557 string containing a date and optionally a calendar.

5. An object containing calendar, day, era, and eraYear properties, with calendar defaults to "iso8601".

When dealing with date comparisons, the PlainDate class utilizes the `compare()` method, which returns -1, 0, or 1 based on whether one date comes before, matches, or comes after another. This comparison method ignores calendar differences and uses monthCode for calendar-independent comparison.

