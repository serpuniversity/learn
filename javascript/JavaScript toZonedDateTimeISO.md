---

title: Temporal.Instant.prototype.toZonedDateTimeISO() - JavaScript

date: 2025-05-27

---


# Temporal.Instant.prototype.toZonedDateTimeISO() - JavaScript

Working with dates and times in JavaScript can be complex, especially when dealing with time zones and different calendar systems. The Temporal library introduces powerful new APIs for handling temporal data, including the `Instant` and `ZonedDateTime` classes. This article focuses on the `Instant.prototype.toZonedDateTimeISO()` method, which provides a clear and robust way to convert an instant to a zoned date-time, handling time zone conversion while maintaining precision. Through detailed examples and explanations, we'll explore how to use this method effectively, including best practices for specifying time zones and understanding the return value.


## Method Overview

The Temporal.Instant.prototype.toZonedDateTimeISO() method returns a new Temporal.ZonedDateTime object representing the given instant in the specified time zone using the ISO 8601 calendar system. This method provides a clear and explicit way to convert an instant to a zoned date-time, handling time zone conversion while maintaining precision.


### Parameters

The method accepts a single parameter: `timeZone`, which can be either a string or a Temporal.ZonedDateTime instance. This flexibility allows for specifying the desired time zone through various identifiers, including named time zones, offset time zones, or date-time strings containing time zone information.


### Return Value

The return value is a new Temporal.ZonedDateTime object representing the instant in the specified time zone. This object encapsulates both the wall-clock time and the time zone information in the ISO 8601 calendar system.


### Exception Handling

The method includes robust error handling:

- `RangeError` is thrown if the time zone name is invalid.

- `TypeError` is thrown if the time zone parameter is of incorrect type.


### Example Usage

The method can be used to convert an instant to a zoned date-time in a specific time zone. For example:

```javascript

const instant = Temporal.Instant.from("2021-08-01T12:34:56.123456789Z");

const zonedDateTime = instant.toZonedDateTimeISO("America/New_York");

console.log(zonedDateTime.toString()); // 2021-08-01T08:34:56.123456789-04:00[America/New_York]

```

This example demonstrates converting an instant from UTC to the America/New_York time zone, providing both the local time and time zone identifier in the output.


## Parameters

The method accepts a single parameter: `timeZone`, which can be either a string or a Temporal.ZonedDateTime instance. This flexibility allows for specifying the desired time zone through various identifiers, including named time zones, offset time zones, or date-time strings containing time zone information.


### String Time Zone Identifiers

A string identifier can represent a named time zone, an offset time zone, or a date-time string containing time zone information. Named time zones use standardized identifiers based on the IANA Time Zone Database, such as "America/New_York" or "Europe/London". Offset time zones use formats like "-05:00" or "+02:00" to indicate the time difference from UTC. Date-time strings can include the time zone identifier or offset, providing precise synchronization with specific moments in time.


### Temporal.ZonedDateTime Instances

Alternatively, the method accepts a Temporal.ZonedDateTime instance directly. When provided, this instance's time zone properties are used for the conversion. This approach ensures that time zone information is consistent across multiple operations and allows for chaining time zone conversions without explicit identifier specification.


### Default Behavior

If no time zone parameter is provided, the method defaults to the user's current time zone. This default behavior simplifies common use cases where local time zone conversion is desired without explicit parameter specification.


## Return Value

The returned Temporal.ZonedDateTime object represents the instant in the specified time zone using the ISO 8601 calendar system. This object encapsulates the wall-clock time and time zone information, providing a comprehensive representation of the datetime that is both precise and compliant with international standards.


### Object Structure

The Temporal.ZonedDateTime object contains several key properties:

- **year**: The four-digit year component of the date.

- **month**: The month component, ranging from 1 to 12.

- **day**: The day component, ranging from 1 to 31.

- **hour**: The hour component, ranging from 0 to 23.

- **minute**: The minute component, ranging from 0 to 59.

- **second**: The second component, ranging from 0 to 59.

- **fractionalSecondNanoseconds**: The fractional second component, represented as nanoseconds.

- **offset**: The time zone offset from UTC, expressed as hours and minutes.

- **timeZone**: The time zone identifier, such as "America/New_York" or "Europe/London".


### Time Zone Handling

The time zone information in the returned object is determined by the time zone parameter provided to the method:

- If a string identifier is used (e.g., "America/New_York"), the object includes the corresponding time zone offset and identifier.

- If a Temporal.ZonedDateTime instance is provided, it uses the time zone information from that instance.


### Calendar System

The object represents the date and time using the ISO 8601 calendar system, which provides a standardized format for expressing dates and times:

- Year-month-day order: YYYY-MM-DD

- Time format: HH:mm:ss.ssssss

- Time zone format: [time zone identifier]

- Full format example: 2021-08-01T08:34:56.123456789-04:00[America/New_York]


### Ambiguity and Gaps Handling

The method handles ambiguous and gapless local time to UTC time transitions using the `disambiguation` option when creating Temporal.ZonedDateTime objects from PlainDateTime instances. This allows for precise time representation in time zones with complex daylight saving time rules.


### Implementation Notes

The method is part of the Temporal proposal and is implemented as a static method on the Temporal object. It returns an object that is immutable and based on the immutable nature of date objects in the Temporal API, ensuring that the returned datetime cannot be modified after creation.


## Exception Handling

The toZonedDateTimeISO() method implements strict validation for time zone parameters, throwing specific errors based on validation failures:


### RangeError: Invalid Time Zone Name

This error is thrown when the provided time zone name cannot be resolved to a valid time zone identifier. The method checks the IANA Time Zone Database to verify the existence and correctness of the specified time zone name. For example, attempting to use an invalid or non-existent time zone like "NonExistentTimeZone" will result in this exception.


### TypeError: Invalid Parameter Type

The method performs strict type checking on the time zone parameter. It requires either a string representing a time zone identifier or a Temporal.ZonedDateTime instance. Passing any other type will result in a TypeError. For example, supplying a number or object other than a string or Temporal.ZonedDateTime will trigger this exception.

Additional constraints include:

- When using a string identifier, it must conform to the IANA Time Zone Database format (e.g., "America/New_York" or "Europe/Paris").

- If using offset time zones, the string must match the ISO 8601 offset format (e.g., "-05:00" or "+02:00").

- Date-time strings containing time zone information must adhere to valid ISO 8601 formats, including proper structure and syntax for time zone components.

These rigorous validation checks ensure that the method operates with high reliability and precision, preventing common errors related to invalid time zone identifiers and incorrect parameter types.


## Example Usage

The `Instant.toZonedDateTimeISO()` method demonstrates several key aspects of working with temporal data in JavaScript. The method accepts a time zone parameter that can be either a string identifier or a `Temporal.ZonedDateTime` instance, providing flexibility in time zone specification.


### Example Conversion

```javascript

const instant = Temporal.Instant.from("2021-08-01T12:34:56.123456789Z");

const zonedDateTime = instant.toZonedDateTimeISO("America/New_York");

console.log(zonedDateTime.toString()); // 2021-08-01T08:34:56.123456789-04:00[America/New_York]

```


### Local Time Zone Conversion

```javascript

const localDateTime = instant.toZonedDateTimeISO(Temporal.Now.timeZoneId());

console.log(localDateTime.toString()); // This instant in your timezone

```


### API Usage

The method conforms to the Temporal API's design principles, which emphasize explicit time zone handling and robust error checking. Like other Temporal methods, it throws `RangeError` for invalid time zone names and `TypeError` for incorrect parameter types, ensuring reliable method usage and error-free development.

