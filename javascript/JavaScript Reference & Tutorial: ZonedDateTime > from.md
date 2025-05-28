---

title: ZonedDateTime in JavaScript

date: 2025-05-27

---


# ZonedDateTime in JavaScript

Working with dates and times across different time zones can be complex, especially when you need to account for daylight saving time changes and multiple calendar systems. In JavaScript, built-in date types don't handle time zones very well, but the ZonedDateTime library fills this gap by providing robust date and time manipulation capabilities while maintaining time zone awareness. This article explores the features of ZonedDateTime, from its basic usage to advanced functionality like calendar system conversion and time zone handling.


## ZonedDateTime Overview

ZonedDateTime is a JavaScript implementation that brings IANA timezone support to the language. It's available through the npm package zoned-date-time, which includes the necessary IANA timezone data through the iana-tz-data package. This implementation packs a lot of functionality into just 0.6KB, making it an efficient choice for date and time handling in JavaScript applications.


### Constructor and Basic Usage

Creating a ZonedDateTime instance can be done in several ways:

- From a Date object and IANA timezone data

- From an absolute Unix timestamp (milliseconds) and IANA timezone data

- By parsing an ISO 8601 string with a time zone identifier

- Retrieving the current date and time in a specific time zone

Here's how you might create a ZonedDateTime object representing the current date and time in the Los Angeles time zone:

```javascript

import {ZonedDateTime} from '@internationalized/date';

let now = ZonedDateTime.now('America/Los_Angeles');

```


### Time Zone and Calendar Handling

The class maintains full time zone awareness and supports multiple calendar systems including Gregorian, Hebrew, Indian, Islamic, Buddhist, and Ethiopic. It stores both the time zone identifier and the UTC offset, with the offset determined from the time zone data when creating the instance.

When performing calculations, special handling is required for daylight saving transitions:

- During a "spring forward" transition (2 AM to 3 AM), adding one hour skips the 2 AM hour.

- During a "fall back" transition (1 AM to 2 AM), adding one hour repeats the 1 AM hour.


### Conversion and Representation

Conversion between different representations is handled through several methods:

- To ISO 8601 string representation (with UTC offset and time zone identifier)

- Conversion to native JavaScript Date object

- Conversion to CalendarDateTime using the '@internationalized/date' library

The class also allows for detailed date manipulation, including adding and subtracting durations while maintaining time zone awareness. Calendar system conversion functions are available for bridging between different calendar representations, such as converting between the Gregorian and Jewish calendars.


## creation and parsing

The ZonedDateTime class provides several methods for creating instances, each with specific use cases:

- `parseZonedDateTime`: This static method creates a ZonedDateTime from a string in ISO 8601 format, allowing for explicit time zone and UTC offset specification. It supports both "2021-11-07T00:45[America/Los_Angeles]" and "2021-11-07T00:45-07:00[America/Los_Angeles]" formats, preserving the maximum amount of information about the original local time and time zone selection.

- `fromDate`: Creates a ZonedDateTime from a Date object, requiring a time zone identifier to determine the appropriate time zone and offset.

- `fromAbsolute`: Creates a ZonedDateTime from a Unix epoch timestamp (milliseconds), requiring a time zone identifier to establish the correct time zone and offset.

- `now`: Retrieves the current time in a specified time zone, providing a convenient way to get the current date and time in a particular time zone without manual configuration.

- `getLocalTimeZone`: Returns the user's current time zone, which can be useful for obtaining the local time zone in applications that need to display time in the user's local time zone.


### Technical Implementation

The class maintains the following internal state:

- LocalDateTime: Represents the local date and time components

- ZoneId: The time zone identifier, which determines the zone rules

- ZoneOffset: The UTC offset, represented in milliseconds

Key methods for creating instances include:

- `of(year, month, dayOfMonth, hour, minute, second, nanoOfSecond, zone)`: Constructs a ZonedDateTime from year, month, day, hour, minute, second, nanosecond, and time-zone information, resolving the local date-time to a single instant on the time-line using ZoneRules of the zone ID.

- `ofLocal(localDateTime, zone)`: Obtains an instance from a local date-time using the preferred offset if possible, with the offset found based on the ZoneRules of the zone ID. This method typically has only one valid offset, but handles overlaps where clocks set back, using the earlier valid offset (usually corresponding to 'summer') and adjusting the local date-time by one hour later in case of clock jumps (gaps).

Validation during construction is strict, ensuring that the provided offset is valid according to the zone's rules. If invalid, an exception is thrown, preventing the creation of a ZonedDateTime instance with an inconsistent time zone configuration.


## Date and Time Manipulation

The ZonedDateTime class in JavaScript supports advanced date and time manipulation through its comprehensive method set. For instance, the `withHour(hour: number)` method allows setting the hour component while automatically handling daylight saving transitions. This method throws a DateTimeException for invalid hour values, ensuring robust date integrity.

Daylight saving time transitions present unique challenges, and ZonedDateTime provides specialized methods to address them. In cases of overlapping local time lines (such as the autumn daylight savings change), the `withLaterOffsetAtOverlap()` method returns a ZonedDateTime with the later of two valid offsets. Conversely, for spring "gap" transitions, the local date-time is adjusted to skip the invalid hour, maintaining time zone consistency.

The class handles date conversion and field manipulation through its core temporal adjustment API. This includes methods for adding and subtracting durations (`add()`, `subtract()`), setting fields while constraining others (`set()`), and cycling through field values (`cycle()`). These operations maintain time zone awareness, adjusting the UTC offset as necessary to preserve global time-line consistency.


### Zone Handling and Conversion

ZonedDateTime instances retain their original time zone data through methods like `withFixedOffsetZone()`, which updates the zone ID while preserving the local date-time and offset. For time zone conversion, the `toTimeZone()` function allows precise date translation between zones, while `toLocalTimeZone()` provides convenient local time zone conversion.

The class's flexible instantiation methods (`of()`, `fromDate()`, `fromAbsolute()`) support sophisticated use cases, including government time zone changes and legacy date-time combinations. Validation during construction is strict, employing both lenient and strict creation modes to balance flexibility and data integrity.

These features make ZonedDateTime a powerful tool for JavaScript developers working with global time zone data, offering robust support for complex date-time operations while maintaining consistent time-line integrity across daylight saving changes.


## Time Zone and Calendar Handling

ZonedDateTime supports multiple calendar systems including Gregorian, Hebrew, Indian, Islamic, Buddhist, and Ethiopic. The class can accept a Calendar instance to represent dates in a specific calendar system. For example, it demonstrates creating a date in the Buddhist calendar system equivalent to April 30th, 2020 at 9:15 AM in the Gregorian calendar.


### Conversion and Representation

The class provides comprehensive methods for conversion between different representations. It can convert to native JavaScript Date objects using the `toDate` method, or to ISO 8601 strings using the `toString` and `toAbsoluteString` methods. The latter includes UTC offset and time zone identifier information.


### Calendar System Conversion

Conversion between calendar systems is handled through the `toCalendarDateTime` function, which uses the `@internationalized/date` library. This function takes a ZonedDateTime object and returns a CalendarDateTime object representing the same date and time.


### Time Zone Handling

Time zone conversion is managed through the `toTimeZone` and `toLocalTimeZone` functions. Both methods take a time zone identifier as an argument to perform the conversion. The conversion logic handles various time zone scenarios:

- For time zone gaps (zero valid offsets, typically due to spring daylight savings changes): Local date-time in the middle results in a shifted forward date-time in the later offset (typically 'summer' time).

- For time zone overlaps (two valid offsets, typically due to autumn daylight savings changes): Previous offset retained unless invalid, then earlier offset (typically 'summer' time).


### Field Manipulation

The class handles field cycling and adjustment through its core temporal API, including methods for adding and subtracting durations (`add`, `subtract`), setting fields while constraining others (`set`), and cycling through field values (`cycle`). These operations maintain time zone awareness, adjusting the UTC offset as necessary to preserve global time-line consistency.


### Comparison Methods

Comparison methods are available for ZonedDateTime objects, including `compare`, `isSameYear`, `isSameMonth`, `isSameDay`, and `isToday`. The `compare` method returns a number indicating whether the first date is before, equal to, or after the second date.

The library supports partial comparisons between dates in different calendar systems, converting the second date to the calendar system of the first date before comparison. This ensures accurate cross-calendar comparisons while maintaining time zone awareness.


## Conversion and Representation

ZonedDateTime offers several representation methods, including:

- Conversion to ISO 8601 strings using the `toString` and `toAbsoluteString` methods

- Conversion to native JavaScript Date objects using the `toDate` method

- Conversion to CalendarDateTime objects using the `toCalendarDateTime` method

The class also includes a `toJSON` method that automatically serializes ZonedDateTime instances into a JSON-friendly format, suitable for storage or transmission. This method returns a string in the RFC 9557 format, including the calendar annotation and offset information, ensuring complete representation of the original date-time.


### Calendar System Conversion

ZonedDateTime supports conversion between different calendar systems, including Gregorian, Hebrew, Indian, Islamic, Buddhist, and Ethiopic. For example, it can convert a date in the Gregorian calendar to its equivalent in the Buddhist calendar system, as demonstrated in the documentation:

```javascript

import {ZonedDateTime, GregorianCalendar, BuddhistCalendar} from '@internationalized/date';

let date = new ZonedDateTime(

  2022, 2, 3, // Gregorian calendar

  'America/Los_Angeles',

  9, 15, 0

);

let buddhistDate = date.toCalendarDateTime().convertTo(new BuddhistCalendar());

```


### Date and Time Extraction

The class provides several methods for extracting specific components of the date-time:

- `getMonth()`: Returns the month number

- `getDay()`: Returns the day number

- `getHour()`, `getMinute()`, `getSecond()`, `getMillisecond()`: Return the corresponding time component

- `getTimezoneOffset()`: Returns the UTC offset in minutes

- `getTimezoneId()`: Returns the IANA time zone identifier

These methods allow programmatic access to the components of a ZonedDateTime object, facilitating both direct manipulation and formatting for display. The class also supports setting and updating these fields through its `set` method, ensuring consistent calendar and time zone handling.

