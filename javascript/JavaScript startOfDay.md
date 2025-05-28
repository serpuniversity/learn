---

title: JavaScript ZonedDateTime: startOfDay Method

date: 2025-05-27

---


# JavaScript ZonedDateTime: startOfDay Method

JavaScript's Temporal.ZonedDateTime class provides an extensive framework for representing and manipulating dates and times with time zone awareness. This class handles complex situations like Daylight Saving Time transitions, ambiguous local times, and overlapping time zones, ensuring accurate date-time operations according to IANA standards. The startOfDay method, in particular, demonstrates the class's robust capabilities by returning the first valid instant of the date in the specified time zone, automatically adjusting for DST gaps and overlaps. Through three equivalent implementation approaches, this method consistently returns a ZonedDateTime object representing the start of the day while maintaining time zone context. The detailed examination of this method highlights JavaScript's comprehensive date-time handling features and their practical applications in various time zone scenarios.


## ZonedDateTime Overview

Temporal.ZonedDateTime represents a date and time with time zone in the ISO-8601 calendar system, combining an instant, a time zone, and a calendar system. It automatically handles Daylight Saving Time (DST) adjustments using RFC 5545 rules and ensures valid results when performing time-based operations by internally representing time zones with IANA Time Zone Database strings or fixed UTC offsets.

The class stores date and time fields to a precision of nanoseconds and includes a time zone with a zone offset to handle ambiguous local date-times. It supports different time zone scenarios including normal (one valid offset), gap (zero valid offsets typically occurring during spring daylight savings change), and overlap (two valid offsets occurring during autumn daylight savings change). In overlaps, the previous offset is retained unless invalid, while in gaps, the date-time is adjusted forward to the later offset.

ZonedDateTime provides comprehensive support for calendar systems, including those that use eras (e.g., BC/AD in the Gregorian calendar). The class automatically corrects capitalization of time zone identifiers to match the IANA time zone database standards and converts offsets like +01 or +0100 to +01:00 format. It also handles edge cases, such as when UTC is used as a time zone identifier, noting that this is generally not recommended due to the absence of DST and constant zero offset, which results in identical results to Temporal.PlainDateTime or Temporal.Instant for UTC times.


## startOfDay Method

The startOfDay method returns a ZonedDateTime object representing the first instant of the date in the time zone, which is typically 00:00:00. However, in cases where the midnight transition does not exist due to offset changes, such as during a daylight saving time (DST) gap, the method returns the first time that exists in the time zone.

For example, when an hour is skipped due to a DST gap, the startOfDay method will return the time immediately following the gap, effectively moving the date forward by one hour. This behavior ensures that the start of the day always represents a valid moment in time, even during transitions where intermediate times are not valid.

The underlying implementation of startOfDay uses three primary approaches, all of which produce equivalent results:

1. Using the ZonedDateTime object directly: This approach converts the original ZonedDateTime to LocalTime MIN_VALUE, effectively truncating the time component to midnight. It then converts back to ZonedDateTime while maintaining the original time zone.

2. Truncated to ChronoUnit.DAYS: This method explicitly truncates the time component to the beginning of the day, preserving the original time zone information. In the case of DST gaps, it adjusts the local date-time forward by the length of the gap.

3. fromLocalDate.atStartOfDay(zone): This approach first converts the ZonedDateTime to LocalDate and then finds the start of the day in the specified time zone. This method produces the same result as the ChronoUnit.DAYS version.

While all three approaches produce the same result in most cases, there is one exception during the transition from summer to winter time. In overlap periods, if the local date-time falls in the middle of an overlap, the previous offset is retained. If there is no valid previous offset or it is invalid, the earlier offset (typically corresponding to "summer" time) is used.

This method works by modifying the local date-time component while maintaining the original time zone information. It only changes the local date-time if it becomes invalid in the new time zone, determined using the same approach as the ofLocal method. The original time zone remains unchanged during these modifications, ensuring that the final result maintains the correct time zone context for the specified date.


## Implementation Details

The implementation employs three main strategies to determine the start of the day in the specified time zone:

1. **Direct ZonedDateTime Conversion (zonedDateTime.startOfDay())**

   This approach retrieves the local time of MIN_VALUE, effectively truncating to midnight, and then converts back to ZonedDateTime while maintaining the original time zone. This produces consistent results across most time zone scenarios.

2. **Truncate to ChronoUnit.DAYS**

   This method explicitly truncates the time component to the beginning of the day while preserving the original time zone information. It correctly handles DST transition scenarios by moving the local date-time forward by the length of the gap when summer time begins at midnight.

3. **fromLocalDate.atStartOfDay(zone)**

   This strategy first converts the ZonedDateTime to LocalDate and then finds the start of the day in the specified time zone. It behaves identically to the ChronoUnit.DAYS approach in standard cases but preserves the correct local date-time when summer time begins at midnight.

The startOfDay method's implementation preserves the original time zone context throughout modifications, converting the local date-time component only when necessary to produce valid results. In overlap periods, the method retains the previous offset if available; otherwise, it uses the earlier "summer" time offset. This approach ensures consistent date-time handling across different time zone scenarios while maintaining alignment with IANA time zone database standards.


## Examples and Use Cases

The startOfDay method consistently returns a ZonedDateTime object representing the start of the day while preserving the original time zone. In standard cases, it produces identical results across all three implementation strategies: direct ZonedDateTime conversion, truncation to ChronoUnit.DAYS, and fromLocalDate.atStartOfDay(zone).

Code examples demonstrate its usage in various time zones and transition scenarios. For instance, in the United States, where DST transitions occur at 2 AM, the method correctly handles the 2 AM hour gap:

```javascript

const dt = Temporal.ZonedDateTime.from("2024-03-10T12:00:00-04:00[America/New_York]");

console.log(dt.startOfDay().toString()); // 2024-03-10T00:00:00-05:00[America/New_York]

```

In Brazil, where DST transitions previously occurred at midnight, the method correctly handles the missing midnight transition:

```javascript

const dt2 = Temporal.ZonedDateTime.from("2015-10-18T12:00-02:00[America/Sao_Paulo]");

console.log(dt2.startOfDay().toString()); // 2015-10-18T01:00:00-02:00[America/Sao_Paulo]

```

The method's implementation preserves the original time zone context throughout modifications, converting the local date-time component only when necessary. This ensures correct date-time handling across different time zone scenarios while maintaining alignment with IANA time zone database standards.


## Related Methods and Concepts

The `ZonedDateTime` class in JavaScript provides comprehensive functionality for date and time operations, including setting fields, handling time zone transitions, and formatting date-time values. The class itself represents a date and time with a time zone, combining an instant, a time zone, and a calendar system.


### Field Manipulation and Resolution

Setting fields adjusts the date while maintaining time zone awareness, with daylight saving transitions causing corresponding UTC offset adjustments. Ambiguous times during transitions require explicit resolution through options like 'earlier', 'later', 'compatible', or 'reject'. Each option handles the ambiguity differently: 'earlier' and 'later' choose between valid times, 'compatible' applies default behavior, and 'reject' throws an error if ambiguous.


### Time Zone Transitions and Hour Cycling

The `cycle` method allows field incrementing or decrementing while remaining time zone aware. For hour operations, "spring forward" transitions skip the 2 AM hour, while "fall back" transitions repeat the 1 AM hour. Under the hood, UTC offset changes drive these modifications. Invalid hours during transitions behave predictably: "spring forward" transitions skip the 2 AM hour, and changing dates around these transitions may shift the hour as necessary.


### Parsing and Formatting

Parsing ZonedDateTime objects uses the `parseZonedDateTime` function, accepting ISO 8601 duration strings and supporting decimal values with comma or period notation. Negative values require a minus sign prefix. Setting fields in immutable objects demands use of the `set` method, which returns new ZonedDateTime objects with updated values while preserving constraints on field ranges.


### Offset and Conversion

The `offset` property returns the time zone offset as an ISO 8601-formatted string, changing after DST transitions or political time zone changes. The class includes methods like `with` for creating new objects with options to handle conflicts between input values and existing properties. The `startOfDay` method returns the first instant of the date in the time zone, typically 00:00:00 but adjusting for cases where midnight does not exist due to offset changes.

