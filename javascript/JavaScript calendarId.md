---

title: JavaScript Date & Time: ZonedDateTime and Calendar Systems

date: 2025-05-27

---


# JavaScript Date & Time: ZonedDateTime and Calendar Systems

JavaScript's Temporal library introduces sophisticated date and time handling capabilities through ZonedDateTime objects. These objects combine precise time representation with calendar system awareness, overcoming limitations of traditional Date objects. This guide explores how ZonedDateTime manages temporal data across different calendar systems, including creation methods, core properties, and manipulation functions.


## ZonedDateTime Overview


### ZonedDateTime Overview

ZonedDateTime in JavaScript represents a date and time with calendar systems and eras, bridging the gap between an exact time and wall-clock time. It combines an instant, time zone, and calendar system to create a time-aware object that differs significantly from basic Date objects. Each ZonedDateTime instance includes properties like epoch milliseconds, epoch nanoseconds, calendar system identifier, era, year, and month, with behavior varying based on the specific calendar system in use.


### Instant and Calendar Conversion

The class functions through JavaScript's concept of a temporal instant, representing time in UTC with continuous, uniform increments. Local time conversion occurs via the time zone, calculated as UTC offset + time zone definition table mapping specific offsets. This system allows for accurate representation of date and time while accounting for daylight saving transitions and political changes affecting time zones.


### Calendar System Support

JavaScript's ZonedDateTime supports multiple calendar systems through the calendarId property, which returns calendar system identifiers like 'gregory' or 'islamic-umalqura'. The eraYear and daysInYear properties provide insights into each calendar's unique properties, with eraYear starting from 1 or 0 and daysInYear varying by calendar system. The toCalendarDateTime function facilitates conversion between calendar systems, demonstrating the object's flexibility in handling diverse temporal representations.


## calendarId Property

The `calendarId` property of `Temporal.ZonedDateTime` instances returns a string representing the calendar used to interpret the internal ISO 8601 date. This property is read-only and does not allow direct modification; instead, users should use the `withCalendar()` method to create a new `Temporal.ZonedDateTime` object with the desired calendar system.

The `calendarId` property follows these key behaviors and limitations:

- It is defined on `Temporal.ZonedDateTime.prototype` and shared by all `Temporal.ZonedDateTime` instances.

- The property value is determined during object creation and cannot be changed afterward.

- To switch calendar systems, use the `withCalendar()` method, which validates the new calendar ID and returns a modified `Temporal.ZonedDateTime` instance.

The property's value depends on the calendar system used to create the `Temporal.ZonedDateTime` object. For example, creating a ZonedDateTime with the default Gregorian calendar results in a `calendarId` of "gregory". Supported calendar IDs include "gregory", "islamic-umalqura", and others, with the specific set of supported calendars varying between browser implementations.

Developers should be aware of the following important considerations:

- The property is experimental technology and may not work consistently across all browsers.

- Calendar system behavior varies, with some systems using eraYear indexing starting from 1 and others from 0.

- Day numbering can vary between calendar systems, requiring careful handling when converting between systems.


## Creating ZonedDateTime Objects

The `Temporal.ZonedDateTime` constructor allows creation from various inputs:

From Date object: `Temporal.ZonedDateTime.fromDate(date, time_zone)`

From epoch time: `Temporal.ZonedDateTime.fromAbsolute(epoch_time, time_zone)`

From current time: `Temporal.ZonedDateTime.now(time_zone)` returns local time

`Temporal.ZonedDateTime.getLocalTimeZone()` retrieves user's current time zone

Properties include:

- `calendar`: Calendar system (e.g., Gregorian)

- `era`: Calendar era (e.g., "BC" or "AD")

- `year`: Year within era

- `month`: Month number within year (variable for some calendars like Hebrew)

- `day`: Day number

Conversion methods:

- `toString()`: Converts to ISO 8601 string

- `toNativeDate()`: Converts to native JavaScript `Date` object

- `toCalendarDateTime()`: Converts to calendar-specific object

- `toTimeZone()`: Converts to target time zone

- `toLocalTimeZone()`: Converts to user's local time zone

Equality and comparison methods:

- `isSameYear()`: Compares years in calendar system

- `isSameMonth()`: Compares months in calendar system

- `isSameDay()`: Compares dates regardless of calendar system

- `isToday()`: Compares to current date in time zone

- `compare()`: Returns -1, 0, or 1 for before, equal, or after

The constructor accepts three parameters:

1. item (convertible to `Temporal.ZonedDateTime`)

2. options (optional configuration object)

3. returns: New `Temporal.ZonedDateTime` object

The options object provides configuration for:

- overflow: 'constrain' (default) or 'reject' out-of-range values

- disambiguation: 'compatible' (default), 'earlier', 'later', or 'reject' ambiguous values

- offset: 'use', 'ignore', 'prefer', or 'reject' time zone offsets

The class supports multiple calendar systems, including:

- Gregorian

- Hebrew

- Indian

- Islamic

- Buddhist

- Ethiopic

The `month` property uses positive integers for the day of the month, unlike legacy JavaScript Date where months are zero-based indices. The `day` property represents the day number within the month. Era information is provided through `era` and `eraYear`, with support for both modern and pre-modern eras in some calendar systems.


## ZonedDateTime Methods

The ZonedDateTime class offers several methods for both formatting and manipulating date-time values while maintaining precision and accuracy through calendar-aware calculations.


### Formatting

The toString method provides a standardized ISO 8601 representation of the ZonedDateTime, including UTC offset and time zone identifier. For example, a ZonedDateTime in Los Angeles will display as '2022-02-03T12:24:45-08:00[America/Los_Angeles]'. The toAbsoluteString method converts the date to Coordinated Universal Time (UTC), producing strings like '2022-02-03T20:24:45.000Z'. The toNativeDate method returns a legacy JavaScript Date object, while toCalendarDate and toTime functions extract date-only and time-only representations respectively.


### Conversion

ZonedDateTime objects support conversion to and from various representations:

- Conversion to CalendarDateTime using the toCalendarDateTime function allows operations across different calendar systems while maintaining the same underlying instant.

- Time zone conversion functions include toTimeZone for specifying a target time zone and toLocalTimeZone for the user's current time zone.


### Manipulation

Date manipulation methods allow precise adjustments to the ZonedDateTime while preserving the original object:

- The add and subtract methods operate on DateTimeDuration objects, which support year, month, hour, minute, and second increments. For example, zdt.withPlainTime({ hour: 10 }) creates a new ZonedDateTime with the hour set to 10 while preserving the original date and time zone.

The withCalendar, withPlainTime, and withTimeZone methods provide flexible state changes:

- withPlainTime allows setting the hour while maintaining the original date and time zone.

- withTimeZone projects the ZonedDateTime into a different time zone.

- withCalendar projects the ZonedDateTime into a different calendar system while preserving the underlying date and timeinstant.

Comparison methods offer comprehensive date-time evaluation:

- The compare method determines the chronological order, while isSameYear, isSameMonth, and isSameDay check for equality based on the specific calendar system.

- The isToday method evaluates against the current local time in the specified time zone.

The epochMilliseconds property returns the integer milliseconds since the Unix epoch, while epochNanoseconds provides the nanosecond precision as a bigint value. These properties enable precise conversion to legacy Date objects while maintaining time zone independence.


## Calendar System Support

The Temporal API supports multiple calendar systems through the `calendarId` property, which returns the calendar system identifier as a string. Supported calendar systems include "gregory", "hebrew", "indian", "islamic-umalqura", and others, though the specific set of supported calendars may vary between browser implementations.

Each calendar system has distinct properties, particularly in how it handles era and day numbering:

- Era: Many calendar systems use eras to represent time periods, such as BC and AD in the Gregorian calendar. The `era` property returns the era as a lowercase string, while `eraYear` returns a non-negative integer representing the year within the era. For example, in the Gregorian calendar, `era` returns "gregory" or "gregory-inverse", and `eraYear` returns the year number.

- Day numbering: The `daysInWeek` property always returns 7 for ISO 8601 calendars, while `daysInMonth` and `daysInYear` vary based on the specific calendar system. For instance, a ZonedDateTime object representing a date in the Hebrew calendar will have different values for these properties compared to a Gregorian date.

The API provides comprehensive support for calendar conversion through the `toCalendar` function, allowing dates to be represented in different calendar systems while maintaining the same underlying instant. This functionality enables operations across multiple calendar systems while preserving the accuracy of temporal relationships.

