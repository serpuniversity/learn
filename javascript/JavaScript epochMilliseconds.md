---

title: JavaScript's Temporal.ZonedDateTime: Working with Date and Time in JavaScript

date: 2025-05-27

---


# JavaScript's Temporal.ZonedDateTime: Working with Date and Time in JavaScript

JavaScript's Temporal.ZonedDateTime offers a sophisticated framework for managing date and time across time zones and calendar systems. This introduction will guide you through creating ZonedDateTime objects, understanding their properties, and mastering their methods for precise time zone and calendar handling.


## Creating ZonedDateTime Objects

The construction of ZonedDateTime objects in JavaScript allows for three primary approaches: conversion from existing Date objects, creation from epoch time (milliseconds), and representation of the current time with specified time zones.


### Conversion from Existing Date Objects

ZonedDateTime can be created by converting a native JavaScript Date object into the desired time zone. This process involves mapping the local date-time to the target time zone's rules for offset changes, considering scenarios such as daylight saving time transitions and calendar-specific characteristics.

```javascript

const localDate = new Date(); // Current local date and time

const targetZone = "America/New_York";

const zonedDateTime = new Temporal.ZonedDateTime(localDate, targetZone);

```


### Creation from Epoch Time (Milliseconds)

JavaScript's ZonedDateTime provides a method to construct objects based on a specific epoch time value, measured in milliseconds since the Unix epoch. This approach requires careful handling of time zone offsets and calendar system interpretations to produce accurate date-time representations.

```javascript

const epochTime = new Date().getTime(); // Current time in milliseconds

const targetZone = "Asia/Kolkata";

const zonedDateTime = new Temporal.ZonedDateTime(epochTime, targetZone);

```


### Representation of Current Time with Specified Time Zone

The simplest method for creating ZonedDateTime objects is to obtain the current time in the specified time zone. This approach automatically handles local time calculations and time zone rule applications to produce accurate date-time representations.

```javascript

const targetZone = "Europe/Paris";

const zonedDateTime = new Temporal.ZonedDateTime();

```


## Properties of ZonedDateTime Objects

ZonedDateTime objects encompass several key properties that enable precise date-time representation and manipulation. The core properties include calendar system, era, year, month, and day, each with specific characteristics:


### Calendar System and Era

The calendar system attribute defines the calendar used for date calculations, with options including Gregorian, Hebrew, Indian, Islamic, Buddhist, Ethiopic, and others. The era property represents the calendar's era, using string identifiers like "gregory" or "gregory-inverse" for the Gregorian calendar.


### Year, Month, and Day

The year property represents the year within the calendar's era, while the month property indicates the month number within the year. The day property specifies the day of the month. It's important to note that month numbers may not always correspond to the same month names in different years due to variable month lengths in some calendar systems.


### Time Components

ZonedDateTime includes detailed time components: hours, minutes, seconds, and milliseconds. The offsetNanoseconds property represents the UTC offset in nanoseconds, while the timeZone property stores the IANA time zone identifier.


### Date Manipulation

The class offers comprehensive methods for date manipulation, including adding and subtracting time durations. For example, the withDayOfMonth method changes the day-of-month of the local date-time, from 1 to 28-31, while the withHour method changes the hour-of-day, from 0 to 23. These methods operate on the local time-line and convert the modified local date-time back to a ZonedDateTime using the zone ID to obtain the offset.


### Time Zone Handling

ZonedDateTime effectively manages time zone complexities through its offset handling mechanisms. In gap scenarios (clocks jump forward), local date-time in the middle of a gap results in a shifted local date-time in the later offset. In overlap scenarios (clocks set back), the local date-time retains the offset if possible, otherwise using the earlier offset. The class strictly validates combinations of local date-time, offset, and zone ID to ensure accurate representation.


## ZonedDateTime Methods

ZonedDateTime objects provide a comprehensive suite of methods for constructing and manipulating date-time information, while maintaining strict validation of the underlying temporal data. These methods enable precise time zone handling and calendar system interpretation, particularly in cases of daylight saving time transitions and calendar-specific characteristics.


### Constructor and Factory Methods

ZonedDateTime can be created from local date-time and time-zone information through the `fromLocalDateTime` method, which resolves the input local date-time to a single instant on the time-line using the zone ID's rules. In overlap scenarios (clocks set back), the method selects the earlier valid offset typically corresponding to "summer". For gap scenarios (clocks jump forward), the local date-time is adjusted to be one hour later into the summer offset. The class also includes a static factory method `of8` for creating instances from year, month, day, hour, minute, second, and time-zone information, primarily used for test cases.


### Basic Access Methods

The class provides direct access to key temporal properties including year, month, day, hour, minute, second, and nanosecond. These methods return the corresponding values based on the calendar system, with month numbers adjusted according to calendar-specific characteristics. The offsetNanoseconds property returns the UTC offset in nanoseconds, while the timeZone property stores the IANA time zone identifier.


### Date Manipulation Methods

ZonedDateTime supports precise modification of date-time components using the `withDayOfMonth`, `withDayOfYear`, and `withHour` methods. These operations adjust the local date-time while maintaining the overall structure of the ZonedDateTime object. When converting back to ZonedDateTime after modification, the class handles time zone overlaps and gaps by retaining the offset if possible, or using the earlier offset when necessary. All methods operate immutably, returning new ZonedDateTime instances without affecting the original object.


### Time Zone Conversion Methods

The class includes methods for converting between different time zones and calendar systems. The `toTimeZone` function converts a ZonedDateTime to a different time zone, while `toLocalTimeZone` converts to the user's local time zone. These operations involve mapping the local date-time to the target time zone's rules for offset changes, considering daylight saving time transitions and calendar-specific characteristics.


### Comparison and Validation Methods

ZonedDateTime objects can be compared using the `compare` method, which determines if one date is before, after, or equal to another, returning negative, zero, or positive values respectively. The class also provides several partial comparison functions, including `isSameYear`, `isSameMonth`, `isSameDay`, and `isToday`, which operate based on the calendar system of the first date for year and month comparisons, and ignore time and calendar system for day comparisons.


### Duration Calculation Methods

The class offers methods for adding and subtracting time periods, including `plus`, `plusYears`, `minusMinutes`, `minusSeconds`, and `minusNanos`. These operations always return new ZonedDateTime instances based on the original date-time, with immutability ensured through the creation of new objects rather than modifying existing ones. The class handles complex time zone scenarios such as gaps and overlaps correctly, ensuring consistent results across different time zone rule changes.


## EpochMilliseconds Property

The epochMilliseconds property of a ZonedDateTime object represents the number of milliseconds elapsed since the Unix epoch (midnight at the beginning of January 1, 1970, UTC) to this instant. This property is read-only and cannot be changed directly.

To create a ZonedDateTime object with a specific epochMilliseconds value:

1. Convert the epochMilliseconds value to nanoseconds by multiplying by 1,000,000.

2. Create a Temporal.Instant object using `Temporal.Instant.fromEpochMilli(epochMilliseconds)` and then convert it to a Temporal.ZonedDateTime object using `Temporal.Instant.prototype.toZonedDateTimeISO()`.

3. Alternatively, use the Temporal.ZonedDateTime() constructor, converting the milliseconds to nanoseconds first: `const epochMilliseconds = 1627821296789; const epochNanoseconds = BigInt(epochMilliseconds) * 1_000_000n; const zdt = new Temporal.ZonedDateTime(epochNanoseconds, "UTC");`

Handling Time Zone and Calendar System Considerations:

When working with epochMilliseconds, keep in mind that the local time behavior can differ from day to day due to time zone rules. Days may have less than 24 hours, and entire days may be missing from the local calendar in extreme cases. The class uses the Gregorian calendar by default but supports other calendar systems including Hebrew, Indian, Islamic, Buddhist, Ethiopic, and more.

The time zone handling includes scenarios for gaps (where clocks jump forward) and overlaps (where clocks set back). In gap scenarios, the local date-time in the middle results in a shifted local date-time in the later offset. In overlap scenarios, the previous offset is retained unless invalid, in which case the earlier offset is used. The class ensures accurate representation by strictly validating the combination of local date-time, offset, and zone ID.


## Time Zone and Calendar Systems

ZonedDateTime effectively manages time zone complexities through its robust handling of offset changes, including scenarios where clocks jump forward (gaps) or set back (overlaps). In gap scenarios, local date-time in the middle of a gap results in a shifted local date-time in the later offset, typically corresponding to "summer" time. For overlap scenarios, the local date-time retains the offset if possible; otherwise, the earlier offset is used.

The class maintains consistency through careful validation of the combination of local date-time, offset, and zone ID. When working with epochMilliseconds, the local time behavior can differ from day to day due to time zone rules. Days may have less than 24 hours, and entire days may be missing from the local calendar in extreme cases. The implementation stores the time zone rules in the ZoneRules of the zone ID, allowing precise handling of daylight saving time transitions.

The ZonedDateTime class supports multiple calendar systems including Gregorian, Hebrew, Indian, Islamic, Buddhist, and Ethiopic, with the Gregorian calendar used by default. During daylight saving transitions, the UTC offset adjusts accordingly. Ambiguous times during transitions require explicit resolution, with the default behavior choosing the later time for "spring forward" transitions and the earlier time for "fall back" transitions. Custom behavior can be specified using the disambiguation parameter, which offers options for earlier, later, compatible (default), and reject behavior.

The class provides comprehensive methods for handling calendar-specific characteristics, including the month number, day number, hour, minute, second, and millisecond properties. These methods operate with strict validation of the underlying temporal data, ensuring accurate representation across different calendar systems and time zone rules. The implementation handles offset ambiguities by allowing the offset to be freely set while maintaining the controlled nature of zone rules, providing developers with powerful tools for precise date and time manipulation.

