---

title: JavaScript PlainDate Month Property

date: 2025-05-27

---


# JavaScript PlainDate Month Property

JavaScript's PlainDate object offers a sophisticated alternative to the traditional Date API by providing immutable, calendar-agnostic date representation. While the standard Date object struggles with time zones and ambiguous date formats, PlainDate excels in handling date arithmetic and comparison through its robust property system and method set. This introduction explores the month property in particular, examining its 1-based indexing system, calendar-specific behavior, and integration with other date manipulation methods. Understanding these principles is crucial for developers working with cross-calendar date operations in JavaScript.


## PlainDate Overview

The PlainDate object in JavaScript represents a date without associated time or timezone information, addressing limitations in the traditional Date API. This object provides methods for manipulating dates, including comparison and arithmetic operations, while maintaining immutability and clarity in date representation.

PlainDate objects can be created using the Temporal.Now.plainDateISO() function, which returns the current date in ISO 8601 format, or through the from method with year, month, and day parameters. The month parameter uses 1-based indexing (1-12) instead of the traditional 0-based indexing (0-11) of the Date object.

The PlainDate class includes several key properties:

- year: Represents the year relative to a calendar-specific epoch

- month: Represents the month ordinal in the current year (1-12)

- monthCode: Provides a calendar-specific string identifying the month

- day: Represents the day of the month

Instances can be created from strings representing dates, with support for multiple calendar systems through the calendar parameter. For example, Temporal.PlainDate.from("2021-07-01[u-ca=japanese]") creates a date in the Japanese calendar system.

The class supports overflow options for invalid date inputs:

- 'constrain': Truncates to the nearest valid date (e.g., 2001-12-01 from { year: 2001, month: 1, day: 32 })

- 'reject': Throws a RangeError for invalid dates

The PlainDate object provides methods for date manipulation and formatting:

- with() method: Allows modification of date properties while constraining the day to valid values

- toString(): Returns the date in ISO format

- toLocaleString(): Returns a formatted string in locale-specific format

Comparison methods include:

- compare(one, two): Returns -1 if one comes before two, 0 if equal, 1 if after

- Converts non-PlainDate values to PlainDate using Temporal.PlainDate.from()

The PlainDate class also includes properties for calendar-specific information:

- calendarId: String identifier for the calendar

- era: String or undefined (used in some calendars)

This robust date handling mechanism simplifies date-related operations while maintaining calendar flexibility and avoiding common time zone pitfalls.


## Month Property Features

The month property allows modification through the with() method while enforcing valid day constraints. To set the month to the last value of the year, developers can use either date.with({ month: date.monthsInYear }) or date.with({ month: Number.MAX_VALUE })—both approaches achieve the same result of setting the month to the final month of the year.

For date manipulation, the add() and subtract() methods enable month-based arithmetic. These methods accept duration objects specifying months, days, or ISO 8601 strings (like P5M). Units smaller than months are interpreted as month additions/subtractions, respectively.


### Month Value Range and Constraints

The month property follows a 1-based indexing system, unlike the traditional 0-based indexing of JavaScript's Date object. This means January begins at month 1, while December is represented by the value 12. The month property always operates within the bounds of the current calendar system, with ISO 8601 calendars maintaining a consistent 12-month structure.


### Year Transition Handling

When transitioning between years, particularly in calendar systems that extend beyond the Gregorian (like the Chinese calendar), month values may shift discontinuously. For example, the month immediately following December 31st in a non-leap year will reset to 1 for January 1st of the next year. Leap months, where they exist, can cause the same-named month to have different month values across consecutive years. This behavior is calendar-specific and developers must account for these variations when performing calculations that span multiple years.


### Implementation Details

The month property itself is read-only and can only be modified indirectly through the with() method, which returns a new Temporal.PlainDate object with the updated value. Attempting to directly assign a new month value will result in an error, enforcing the immutability of existing date instances. The internal calculations for month transitions ensure proper handling of leap years and other calendar-specific anomalies, maintaining the integrity of the date representation throughout these changes.


## Date Manipulation Methods

The PlainDate class provides two primary methods for month-based date arithmetic: add() and subtract(). These methods accept duration objects specifying months, days, or ISO 8601 strings (such as P5M), with smaller units interpreted as month additions or subtractions. Both methods throw RangeError for out-of-range results, with overflow handling options 'constrain' (default) or 'reject'.

For implementation, attempting to directly modify the month property will result in an error. Instead, developers should use the with() method, which returns a new Temporal.PlainDate object with the updated value while constraining the day to valid calendar dates. The month property itself is read-only and represents the month ordinal in the current year, using 1-based indexing (1-12) rather than the traditional 0-based system of JavaScript's Date object. This structure ensures that January begins at month 1, with December represented by the value 12.

Leap months present particular challenges for month value handling, particularly across consecutive years in calendar systems that include them. For example, the same-named month may have different month values when transitioning from one leap month year to the next. Developers must account for these variations when performing multi-year calculations. The month property also interacts with other date properties; for instance, the monthsInYear property indicates the total number of months in the current calendar system, which is consistently 12 for ISO 8601 calendars regardless of leap year status. The year property provides the signed integer representing years relative to the calendar-specific epoch, while the monthCode property returns a calendar-specific string identifying the month, with leap months following the previous month's code and appending an 'L' suffix.


## Month-related Properties

The month-related properties of the PlainDate object support rich date manipulation while maintaining calendar flexibility. Development should follow these key practices:

- The month property, set through with(), returns constraints via read-only access

- For month codes, ISO 8601 returns "M07" for July 1, 2021, while Chinese dates show "M03" for March (2021) and "M02L" for February 2023 (leap month)

- All month operations require working with Temporal.PlainDate objects, as underlying properties are immutable and cannot be directly modified

- The monthsInYear property reliably returns 12 for ISO 8601, but varies in other calendars: 12 for common Chinese years, 13 in leap years

- When working with month codes, always use the recommended .toLocaleString() method with "long" option for user-friendly month names


## Calendar Support

The PlainDate class requires a '_calendar_' parameter to specify the calendar type, with "iso8601" as the default value. This parameter allows for precise date representation across different calendar systems, including those that extend beyond the Gregorian calendar. For example, the Chinese calendar system requires this parameter to correctly interpret month values.

Date creation supports multiple convenient input methods, including strings in RFC 9557 format (the official extension to ISO 8601/RFC 3339) and objects with date properties. The resulting PlainDate instances maintain an internal representation as ISO 8601 dates while preserving the specified calendar system information. This system enables accurate date handling across various cultural and historical contexts, from the Gregorian calendar to specialized systems like the Japanese calendar.

The calendar system selection affects several aspects of date representation:

- Year calculation: Chinese calendar years differ from ISO 8601 years due to their lunisolar nature, with months calculated based on lunar cycles

- Month values: Leap months cause month codes to change between consecutive years, requiring careful handling when performing multi-year calculations

- Day resolution: The PlainDate object maintains consistent day resolution regardless of calendar system, ensuring accurate date comparisons and arithmetic operations

