---

title: ZonedDateTime in JavaScript: Working with Years and Time Zones

date: 2025-05-27

---


# ZonedDateTime in JavaScript: Working with Years and Time Zones

In today's globalized world, accurately representing and manipulating dates and times across different time zones has become crucial. The JavaScript Temporal API addresses these needs with the introduction of ZonedDateTime, which combines precise moment representation with comprehensive time zone handling. This article explores how ZonedDateTime extends JavaScript's date-time capabilities, enabling developers to work confidently with year calculations and time zone conversions. Through detailed analysis of its creation methods, property access, and manipulation functions, we uncover the complexities of cross-time zone date arithmetic while highlighting the browser support and standardization efforts behind this powerful feature.


## Introduction to ZonedDateTime

ZonedDateTime extends the basic Date object by representing a precise moment in time that takes into account both the calendar system and the time zone. It combines elements of Temporal.Instant, Temporal.PlainDateTime, and a time zone identifier to create a comprehensive representation of wall-clock time. This extended functionality allows ZonedDateTime to handle complex time-related calculations, including daylight saving time transitions and calendar system-specific characteristics like the Hebrew calendar's variable month lengths.


### Creating ZonedDateTime Objects

ZonedDateTime instances can be created using several methods. For converting existing Date objects, the static method `fromDate` is available. To create objects based on absolute time values, `fromAbsolute` provides a straightforward approach using Unix epoch time. The `now` function captures the current time, requiring a specific time zone identifier to generate correct local time values. Additionally, `getLocalTimeZone` retrieves the time zone associated with the current JavaScript runtime.


### Working with ZonedDateTime Properties

The class exposes numerous properties for date-time manipulation. The calendar system is accessed via the `calendar` property, while the `era` property indicates whether the date falls within the BC or AD periods. The year can be directly accessed through the `year` attribute, complementing the month (`month`) and day (`day`) properties. For time-related information, the hour (`hour`), minute (`minute`), second (`second`), and millisecond (`millisecond`) properties provide exact values. The time zone is maintained through the `timeZone` property, while the UTC offset is available via the `offset` attribute.


### Managing ZonedDateTime Objects

Unlike the mutable Date object, ZonedDateTime instances are immutable. Field modification must be achieved through the `set` method, which returns a new ZonedDateTime with updated values. This method applies constraints to ensure fields remain within valid ranges, such that setting day to 100 results in the last day of February for February months. The `cycle` method offers flexible field adjustment, automatically wrapping values that exceed the field's limits. Modern browsers and Node.js environments (version 18 and above) support a comprehensive list of approximately 400 time zones, each represented by either IANA time zone identifiers or fixed UTC offsets.


## Creating ZonedDateTime Objects

The ZonedDateTime class offers several methods for creating instances, each tailored to different use cases. The static method `of8` provides a comprehensive approach, taking year, month, day, and time components along with a time zone identifier. This method handles daylight saving time changes by returning either the earlier or later valid offset when needed, though it exists primarily for testing purposes. For broader compatibility, other methods like `ofInstant` and its variants offer flexible creation from Instants or LocalDateTime objects combined with offsets.

A specialized method `ofLocal` allows creating a ZonedDateTime from a LocalDateTime while applying the preferred offset from the ZoneRules if available. In cases of overlap (clocks set back), it selects the earlier valid offset, typically corresponding to 'summer' time. Meanwhile, the `ofStrict` method validates the combination of local date-time, offset, and zone ID to ensure the offset is valid for the local date-time.

The class also handles advanced storage scenarios through `fromLocalTime`, allowing creation of ZonedDateTime instances with no checks beyond preventing null values. This method returns an instance where the offset may conflict with the zone ID, intended for situations where a zoned date-time is stored in a database or serialization-based system and later reloaded after a time-zone rule change.

All creation methods share a common approach of working with local date-time components and applying zone ID rules to determine valid offsets. This process handles complex cases like overlap and gap scenarios, ensuring accurate representation of wall-clock time across different time zones. Modern JavaScript environments implement this functionality with approximately 400 supported time zones, each represented by IANA time zone identifiers or fixed UTC offsets.


## Accessing ZonedDateTime Properties

The ZonedDateTime class holds all date and time fields to a precision of nanoseconds and includes a time-zone using a zone offset to handle ambiguous local date-times. It manages conversion between local time-line (LocalDateTime) and instant time-line (Instant) using ZoneOffset and ZoneRules.

Instance properties include:

- calendar: The IANA time zone identifier associated with this date (e.g., Asia/Tokyo, America/Los_Angeles, or UTC)

- era: The calendar era for this date (e.g., "BC" or "AD")

- year: The year of this date within the calendar era

- month: The month number within the year (note: some calendar systems like Hebrew may have variable month lengths)

- day: The day number within the month

- hour: The hour in the day, numbered from 0 to 23

- minute: The minute in the hour

- second: The second in the minute

- millisecond: The millisecond in the second

- timeZone: The IANA time zone identifier that this date and time is represented in

- offset: The UTC offset for this time, in milliseconds

The class provides several methods for working with these properties and creating new ZonedDateTime instances:

- constructor: Creates a new ZonedDateTime instance

- copy: Returns a copy of this date

- add: Returns a new ZonedDateTime with the given duration added to it

- subtract: Returns a new ZonedDateTime with the given duration subtracted from it

- set: Returns a new ZonedDateTime with the given fields set to the provided values. Other fields are constrained accordingly

- cycle: Returns a new ZonedDateTime with the given field adjusted by a specified amount. When the resulting value reaches the field's limits, it wraps around

- toDate: Converts the date to a native JavaScript Date object

- toString: Converts the date to an ISO 8601 formatted string, including the UTC offset and time zone identifier

- toAbsoluteString: Converts the date to an ISO 8601 formatted string in UTC

- compare: Compares this date with another. A negative result indicates this date is before the given one, and a positive result indicates it is after


## Manipulating ZonedDateTime

The ZonedDateTime interface offers robust capabilities for modifying date-time values while maintaining time zone awareness. The primary method for field updates is set, which returns a new ZonedDateTime instance with specified fields changed. This method applies constraints to ensure valid date-time representation, such as limiting day-of-month values within the current month's valid range.

During daylight saving time transitions, the UTC offset adjusts automatically to maintain correct wall-clock time. For example, when "spring forwarding" from 01:30 to 02:30, the 2 AM hour is skipped, and setting hours afterward may require explicitly handling AM/PM conventions depending on the local 12-hour clock cycle preference.

Field modification methods include cycle, which allows incremental adjustment while handling field limits through wrapping. The implementation treats most temporal fields as independent, with hours special-casing daylight saving transitions. For instance, setting the hour field one second before a DST transition would result in the same wall-clock time as setting it after the transition, demonstrating the underlying adjustment approach.

The class's behavior during ambiguous times demonstrates its careful handling of overlapping offsets. When the preferred offset cannot be determined, the system's default behavior of choosing the later valid offset applies, typically corresponding to "summer" time transitions. This approach balances between standard behavior and specific use cases requiring explicit time resolution.


## ZonedDateTime API and Browser Support

The Temporal.ZonedDateTime class offers experimental methods for date-time manipulation while maintaining time zone awareness. Several key properties and methods include:


### Constructor and Instance Properties

The constructor creates a new ZonedDateTime object by supplying underlying data, with the initial value being the Temporal.ZonedDateTime constructor itself. Instance properties like calendarId return a string representing the calendar used to interpret the internal ISO 8601 date, while properties such as day, dayOfWeek, and daysInWeek provide access to date components in a calendar-dependent manner.


### Comparison and Equality

The compare method returns a number (-1, 0, or 1) indicating the relationship between two date-times, equivalent to comparing their epochNanoseconds values. The equals method performs a more thorough comparison, considering date/time fields, offset, time zone ID, and calendar ID. This method returns true for strongly equal objects (including calendar and time zone comparison) and false otherwise.


### Time Zone Transitions

The getTimeZoneTransition method returns a Temporal.ZonedDateTime object representing the next or previous UTC offset transition in the specified direction, returning null if no further transitions are available. This method is particularly useful for handling daylight saving time changes, ensuring accurate wall-clock time representation.


### Calendar and Time Zone Equivalence

The time zone equivalence algorithm compares identifiers in the IANA Time Zone Database, considering identifiers equivalent if they resolve to the same Zone name (case-insensitive) or if numeric offset time zone identifiers represent the same offset. This approach ensures proper handling of time zone changes and transitions.


### Year Manipulation

The withYear method changes the year of the local date-time while converting back to ZonedDateTime using the zone ID to obtain the offset. This process handles daylight savings overlaps and gaps by retaining the offset if possible or using the earlier offset in gaps. The method throws DateTimeException if the year value is invalid and UnsupportedTemporalTypeException if the field is not supported.

