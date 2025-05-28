---

title: JavaScript ZonedDateTime: Working with Date and Time in JavaScript

date: 2025-05-27

---


# JavaScript ZonedDateTime: Working with Date and Time in JavaScript

Working with dates and times in JavaScript has traditionally been fraught with challenges, particularly when dealing with time zones and calendar systems. The introduction of the ZonedDateTime class addresses these pain points by combining the functionality of JavaScript's Date object with robust time zone and calendar support. This article explores the capabilities of ZonedDateTime, from its basic construction and manipulation methods to its advanced features for handling time zone transitions and calendar systems. Whether you're working on a project that requires precise date-time calculations or just need to display time in the user's local time zone, this guide will help you master JavaScript's powerful new date handling API.


## Introduction to ZonedDateTime

ZonedDateTime combines the capabilities of JavaScript's Date object with support for time zones and calendar systems. The class supports multiple calendar systems, including the Japanese calendar which uses eras for each Emperor's reign.


### Constructor and Basic Methods

The constructor takes two parameters: a JavaScript Date object and IANA time zone data. It supports fields for month number, day number, hour, minute, second, millisecond, timeZone (IANA identifier), and offset (in milliseconds). ZonedDateTime objects can be created using methods like `from`, `set`, and `clone`.


### Date and Time Manipulation

ZonedDateTime includes methods for adding and subtracting durations, with operations that respect time zone transitions. For example, adding or subtracting hours accounts for daylight saving time changes, potentially causing the hour to wrap around (e.g., 2 AM to 3 AM during "spring forward" transitions). The class handles these operations through a "balancing" mechanism that ensures time values remain valid within their constraints.


### Time Zone and Calendar Support

Time zones are represented by IANA identifiers like 'America/Los_Angeles' or 'UTC'. The class supports multiple calendar systems, including Gregorian, Hebrew, Indian, and Islamic calendars. For instance, ZonedDateTime can represent dates in the Buddhist calendar system, equivalent to April 30th, 2020 at 9:15 AM in the Gregorian calendar.


### String Representation and Parsing

ZonedDateTime objects can be converted to strings using the `toString` method, which returns a format like '2022-02-03T12:24:45-08:00[America/Los_Angeles]'. The class also supports parsing ISO 8601 strings and provides methods like `toCalendar` for converting between calendar systems.


## Date and Time Manipulation

ZonedDateTime provides multiple methods for adding and subtracting durations, including support for weeks, months, years, hours, and minutes. When performing these operations, the class automatically handles daylight saving time transitions, potentially causing hour values to wrap around during "spring forward" transitions or remain unchanged during "fall back" transitions.

The class uses a "balancing" mechanism to maintain valid date-time values. For example, when adding one hour to a time near a "spring forward" transition (2 AM to 3 AM), the resulting hour value is adjusted to 3 AM instead of creating an invalid 2:60 AM. Conversely, when adding one hour to a time near a "fall back" transition (1 AM to 2 AM), the result is 2 AM, as the original 1 AM hour repeats.


### Zone ID and Offset Handling

When manipulating date-time values, ZonedDateTime always maintains consistency with the underlying ZoneId rules. This means that adding or subtracting durations adjusts both the local time and UTC offset as appropriate for the specified time zone. For instance, a daylight savings transition from 2 AM to 3 AM results in the UTC offset changing instead of the local time.


### Ambiguous and Invalid Times

Special handling is required for times that become ambiguous or invalid during daylight saving transitions. ZonedDateTime resolves these ambiguities using default strategies that can be customized through specific options:

- Default behavior: selects the later time during "spring forward" transitions and the earlier time during "fall back" transitions.

- Custom options: includes 'earlier', 'later', 'compatible', and 'reject' strategies for handling ambiguous times.

- 'earlier' and 'later' options explicitly choose the earlier or later of two possible times.

- 'compatible' strategy aligns with the default behavior, selecting the later time during spring transitions and the earlier time during fall transitions.

- 'reject' strategy throws an error when encountering ambiguous times, preventing invalid state changes.


### Conversion and Representation

ZonedDateTime offers comprehensive conversion capabilities between different representations:

- Converting to and from ISO 8601 strings preserves all time zone and offset information.

- The toString method formats the date-time as 'YYYY-MM-DDTHH:mm:ss[.SSS][Z|[+-]HH:mm]' with the time zone and offset clearly displayed.

- The toAbsoluteString method provides the same information but formatted in UTC time, removing the local time zone context.

These capabilities enable precise date-time manipulation while maintaining awareness of time zone rules and daylight saving adjustments.


## Time Zone and Calendar Support

ZonedDateTime works with IANA time zone identifiers and supports multiple calendar systems, including ISO 8601 being the most common. Time zones are represented by IANA Time Zone Database identifiers (e.g., 'America/Los_Angeles', 'Asia/Tokyo'), with fixed-offset identifiers like '+05:30' discouraged. The API requires IANA time zone data for converting between Instant or PlainDateTime and ZonedDateTime.


### Calendar System Support

The class supports multiple calendar systems including Gregorian, Hebrew, Indian, and Islamic calendars. For example, it can represent dates in the Buddhist calendar system, equivalent to April 30th, 2020 at 9:15 AM in the Gregorian calendar. The constructor can accept a Calendar instance to represent dates in a specific calendar system, as demonstrated in the sample usage:

```javascript

import {ZonedDateTime} from '@internationalized/date';

let date = new ZonedDateTime(

  2022, 2, 3, // Date

  'America/Los_Angeles', -28800000, // Time zone and UTC offset

  9, 15, 0 // Time

);

```


### Conversion and Representation

The API provides comprehensive conversion capabilities between different representations. The toString method formats the date-time as 'YYYY-MM-DDTHH:mm:ss[.SSS][Z|[+-]HH:mm]' with the time zone and offset clearly displayed. The toAbsoluteString method provides the same information but formatted in UTC time, removing the local time zone context. All Temporal types have string representation for persistence and interoperability, including support for ISO 8601, RFC 3339, and RFC 9557 standards. The documentation includes a diagram showing the correspondence between types and machine-readable strings.


## String Representation and Parsing

The JavaScript ZonedDateTime class represents dates with both year and era information, using string identifiers for eras with years counting from 1 within each era. It supports multiple calendar systems including the Japanese calendar, which uses eras for each Emperor's reign.


### Conversion Methods

ZonedDateTime offers several methods for converting between calendar systems using the `toCalendar` function. For example, it can convert dates from the Gregorian calendar to the Hebrew calendar system.


### String Representations

The class provides comprehensive formatting and parsing capabilities through the `DateTimeFormatter`. Built-in formats include ISO 8601 (RFC 3339), and the API supports custom temporal adjusters, fields, and formats for greater flexibility.


### Formatting Options

The text notes that non-numeric date and time formats require specified locales, with plugins available for `@js-joda/locale` and `@js-joda/timezone`. The class supports multiple locale builds via npm, including options for de, de-de, en, en-us, es, fi, fi-fi, fr, hi, and it.


### Parsing

ZonedDateTime supports ISO 8601 format parsing with built-in validation. The API generates helpful error messages when encountering non-supported format elements, such as "Pattern using (localized) text not implemented, use @js-joda/locale plugin!"


### Conversion to Native JavaScript Date

The class includes a `toDate` method that converts ZonedDateTime to a native JavaScript Date object while allowing specification of the desired time zone. For example: `date.toDate('America/Los_Angeles')`.


### ISO 8601 Compliance

ZonedDateTime's string representations adhere to ISO 8601 standards, supporting both basic and extended formats. The class's `toString` method returns a format like 'YYYY-MM-DDTHH:mm:ss[.SSS][Z|[+-]HH:mm]', while `toAbsoluteString` provides the same information in UTC time.


### Calendar System Support

The API supports multiple calendar systems including Gregorian, Hebrew, Indian, and Islamic calendars. For instance, it can represent dates in the Buddhist calendar system, equivalent to April 30th, 2020 at 9:15 AM in the Gregorian calendar.


## Locale and Internationalization

The JavaScript ZonedDateTime API supports extensive locale and internationalization features through its integration with JavaScript's built-in Internationalization API. The core methods for working with dates and times include `toString`, which formats the date-time as 'YYYY-MM-DDTHH:mm:ss[UTC offset][time zone]', and `toAbsoluteString`, which provides the same information in UTC time.

For displaying this information to users, the API recommends using either `Intl.DateTimeFormat` with the appropriate time zone or the Globalize library. The Temporal API currently supports ISO calendars and plans to expand support in the future, particularly for emerging markets like China and India.

The API includes robust support for formatting and parsing dates and times. Built-in formats include ISO 8601 (RFC 3339), with additional support for RFC 9557 standards. The class's string representations adhere to ISO 8601 standards, supporting both basic and extended formats. For example, the `toString` method returns a format like 'YYYY-MM-DDTHH:mm:ss[.SSS][Z|[+-]HH:mm]', while `toAbsoluteString` provides the same information in UTC time.

Non-numeric date and time formats require a specified locale, with plugins available through the @js-joda/locale and @js-joda/timezone libraries. The API supports multiple locale builds via npm, including options for de, de-de, en, en-us, es, fi, fi-fi, fr, hi, and it. The parsing functionality supports ISO 8601 format with built-in validation, generating helpful error messages when encountering unsupported format elements. Full customization options include custom temporal adjusters, fields, and format rules.

When converting between JavaScript's built-in Date object and ZonedDateTime, the API provides several methods. The `clone` method creates a copy of the ZonedDateTime object, while `getTime` returns the underlying JavaScript timestamp. The `toDate` method converts ZonedDateTime to a native JavaScript Date object, with the option to specify the desired time zone. Additional conversion methods include `getDay`, `getFullYear`, `getHours`, and `getTimezoneOffset`, providing comprehensive control over date-time representation.

