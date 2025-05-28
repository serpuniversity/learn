---

title: JavaScript Temporal API: PlainDate

date: 2025-05-27

---


# JavaScript Temporal API: PlainDate

JavaScript's handling of dates has long relied on the native Date object, which while functional for many use cases, presents several fundamental challenges, particularly when dealing with time zones, calendar systems beyond the Gregorian, and immutable date operations. The Temporal API addresses these limitations by introducing strongly typed date and time objects that prevent accidental modifications and provide clear, predictable behavior across different environments. This article explores the Temporal.PlainDate class, which represents dates outside of time zones and calendar systems, offering essential methods for date manipulation while maintaining core temporal consistency. Through detailed examination of its creation methods, properties, and functionality, we uncover how this API component enables more accurate and flexible date handling in JavaScript applications.


## PlainDate Overview

The Temporal.PlainDate object represents a date in JavaScript without time or time zone information, conforming to the ISO 8601 standard. The core functionality revolves around creating and manipulating date objects that are independent of time zones and times.


### Creation Methods and Properties

Temporal.PlainDate objects can be created using two primary methods: the constructor and the static from() method.

The constructor requires three parameters representing the year, month, and day:

```javascript

new Temporal.PlainDate(year, month, day, calendar);

```

Here, `month` and `day` use 1-based indexing (as opposed to JavaScript's 0-based indexing), and an optional `calendar` parameter specifies the calendar system (defaulting to "iso8601"). For example, `new Temporal.PlainDate(2023, 4, 15, "gregory")` creates a PlainDate in the Gregory calendar system.

The static from() method offers more versatile creation options:

- Copying another PlainDate object

- Converting from a PlainDateTime object

- Handling ZonedDateTime objects

- Interpreting ISO 8601 strings

- Parsing objects containing year, month, and day properties (with optional calendar)


### Basic Properties

The PlainDate class exposes several key properties:

- `year`: The year component

- `month`: The month component (1-12)

- `day`: The day component

- Additional properties include `monthCode`, `calendarId`, calendar-specific era information, and day calculations


### Methods and Functionality

The PlainDate class includes essential methods for date manipulation:

- `toString()`: Returns the date in ISO 8601 format

- `toZonedDateTime(timeZoneLike, options?)`: Converts to a ZonedDateTime object

- `until(otherDate)`: Computes the duration to another PlainDate

- `withCalendar(calendar)`: Projects the date into a new calendar system

- `toLocaleString(locales, options)`: Provides locale-sensitive string representation

- `toJSON()`: Returns a string in RFC 9557 format, compatible with JSON.stringify

These methods enable precise date manipulations while maintaining the core principle of calendar-date independence.


## PlainDate Instantiation


### Instantiation Methods

Temporal.PlainDate objects can be created using two primary methods: the constructor and the static from() method.


#### Constructor Method

The constructor requires three parameters representing the year, month, and day:

```javascript

new Temporal.PlainDate(year, month, day, calendar);

```

Here, `month` and `day` use 1-based indexing (unlike JavaScript's 0-based indexing). An optional `calendar` parameter specifies the calendar system (defaulting to "iso8601"). For example, `new Temporal.PlainDate(2023, 4, 15, "gregory")` creates a PlainDate in the Gregory calendar system.

The browser compatibility information is not provided in the source documents.

The constructor's valid input ranges are:

- `year`: 1-9999

- `month`: 1-12

- `day`: 1-31

- `calendar`: A valid calendar identifier (e.g., "iso8601")

The constructor throws exceptions for invalid inputs:

- `TypeError`: If `calendar` is not a string or `undefined`.

- `RangeError`: If inputs are outside valid ranges, inconsistent, or out of representable range (±(108 + 1) days, approximately ±273,972.6 years).


#### from() Static Method

The static from() method offers more flexible creation options:

- Copying another PlainDate object

- Converting from a PlainDateTime object

- Handling ZonedDateTime objects

- Interpreting ISO 8601 strings

- Parsing objects containing year, month, and day properties (with optional calendar)

The method accepts the following parameters:

- A `Temporal.PlainDate` instance, creating a copy

- A `Temporal.PlainDateTime` instance, which provides the calendar date

- A `Temporal.ZonedDateTime` instance, providing the calendar date

- An RFC 9557 string containing a date and optionally a calendar

- An object with the following properties:

  - `calendar` (optional): String representing the calendar, defaulting to "iso8601"

  - `day`: Integer representing the day

  - `era` and `eraYear`: String and integer representing the era if calendar system uses eras

The from() method throws exceptions for invalid inputs:

- `TypeError`: If input is not an object, string, or another Temporal.PlainDate/ZonedDateTime instance.

- `RangeError`: If input properties are inconsistent, out of range, or insufficient to determine a valid date.


### Input Requirements and Validation

The PlainDate constructor and static from() method enforce strict validation rules to ensure accurate date representation:

- `calendar` parameter must be a string identifier ("iso8601", "gregory", "islamic", etc.)

- `month` property values start at 1, unlike legacy Date objects which use 0-based indexing

- The method checks for consistency between provided date parts (year, month, day, era, eraYear)

- It validates against representable range constraints (±(108 + 1) days, approximately ±273,972.6 years)

The validation process ensures that only valid ISO 8601 dates can be created, with appropriate handling of calendar systems and date components.


## PlainDate Methods

The PlainDate class in JavaScript offers several methods for manipulating and formatting date objects. These methods support comparison, date manipulation, and calendar system conversion while maintaining the core principle of calendar-date independence.


### Comparison

The compare method evaluates two Temporal.PlainDate objects, returning -1 if the first date precedes the second, 0 if they match when projected into the ISO 8601 calendar, and 1 if the first date follows the second. Comparison disregards calendar differences, allowing accurate sorting of date arrays across various calendar systems.


### Date Properties

The class exposes essential properties for date representation:

- `year`: A signed integer indicating years relative to the calendar-specific epoch

- `month`: A positive integer representing the month ordinal in the current year

- `monthCode`: A calendar-specific string identifying the month

- `day`: A positive integer representing the day of the month

- `calendarId`: A string identifier for the calendar system

- `era`: A string or undefined, applicable only to calendar systems that use eras


### Calendar System Conversion

The `withCalendar(calendar)` method projects the date into a specified calendar system, returning a new PlainDate object. This functionality enables date operations across different calendar systems while maintaining temporal consistency.


### Date Formatting

The PlainDate object provides multiple methods for date formatting:

- `toString()`: Returns the date in RFC 9557 format, with options to include or exclude calendar annotations

- `toLocaleString(locales, options)`: Generates locale-sensitive date strings using Intl.DateTimeFormat parameters

- `toJSON()`: Returns a string in RFC 9557 format compatible with JSON.stringify(), requiring manual parsing with JSON.parse()

These formatting capabilities enable precise date representation while maintaining calendar independence, crucial for applications requiring consistent date handling across various calendar systems.


## Calendar Systems & Localization


### Calendar System Conversion

The withCalendar() method projects the date into a specified calendar system, returning a new PlainDate object. This functionality enables date operations across different calendar systems while maintaining temporal consistency. The method requires the calendar system identifier as a string parameter, with commonly supported types including "gregory", "islamic-umalqura", and "iso8601". For example:

```javascript

const date = Temporal.PlainDate.from("2021-07-01");

const newDate = date.withCalendar("islamic-umalqura");

console.log(newDate.toLocaleString("en-US", { calendar: "islamic-umalqura" })); // 11/21/1442 AH

```


### Localization

The toLocaleString() method generates language-sensitive date strings, similar to Intl.DateTimeFormat but specifically for PlainDate objects. It accepts two parameters: locales and options. The locales parameter specifies the language tag(s), while options adjust the output format. The calendar system must be explicitly specified if different from the locale's default calendar. For example:

```javascript

date.toLocaleString("en-US", { calendar: "islamic-umalqura" }) // Returns "11/21/1442 AH"

```

The method supports various formatting options, including:

- calendar: Required for non-default calendars, must be "iso8601" for that calendar

- dateStyle: Single argument expands to weekday, era, year, month, and day

- year, month, day: Default "numeric", can be "long", "short", or "numeric"

For example:

```javascript

date.toLocaleString("en-US", { year: "numeric", month: "long", day: "numeric" }) // Returns "August 1, 2021"

```

The method is part of the Temporal API and currently supported in major browsers, providing a robust solution for locale-sensitive date formatting while maintaining calendar independence.


## Temporal API Fundamentals

The current JavaScript date API, introduced in 1995, has several fundamental limitations that the Temporal API addresses. These include immutability issues, poor time zone handling, inconsistent date string parsing, and a lack of essential features like proper duration management and calendar support beyond the Gregorian system.

Temporal introduces strongly typed date and time objects that prevent accidental modifications, providing clear and predictable behavior across different environments. While the native Date object can still work for simple local project needs, its limitations become apparent when building for international audiences or requiring sophisticated time management.

The specification addresses these challenges through several core features:

1. Immutable Object Design: All Temporal objects are immutable, ensuring consistent behavior across different execution contexts. This contrasts with the mutable nature of the current Date object, which can lead to unexpected changes in application state.

2. Time Zone Support: The API handles multiple time zones natively, eliminating the need for external libraries. This enables more effective management of international user bases and schedule coordination across different time zones.

3. Non-Gregorian Calendar Support: Beyond the Gregorian system, Temporal includes robust support for various calendar systems, including Islamic and other historical calendars. This expansion allows JavaScript applications to represent dates accurately for diverse cultural contexts.

4. Improved Date Operations: The API introduces intuitive methods for common date manipulations like adding days, subtracting months, and converting between representations. This makes basic date arithmetic more straightforward and less error-prone.

The Temporal API operates through a global Temporal object that provides access to multiple specialized classes for handling temporal values. These include PlainDate for calendar dates, PlainTime for specific times of day, and fully zoned date/time types that include time zone information.


### Immutable Data Structures

The core design of Temporal revolves around immutable objects, which prevent accidental modifications and ensure consistent behavior across different execution contexts. When performing operations on date or time values, Temporal generates new objects rather than modifying existing ones. This immutability approach aligns with modern JavaScript best practices and makes debugging and reasoning about code simpler.


### Time Zone Management

Temporal separates plain dates, absolute timestamps, and time zone information, allowing developers to work effectively with specific times within particular time zones. The API automatically accounts for Daylight Saving Time changes and provides robust tools for time zone conversion. For example, developers can easily convert between time zones or perform operations that take local time zone rules into account.


### Date Arithmetic

Temporal provides clean, immutable methods for common date operations that were cumbersome with the native Date object. For instance, adding or subtracting days from a date, converting between different representations, or manipulating time values becomes straightforward with specialized methods that prevent accidental state changes.


### Implementation Status

As of now, browser and backend JavaScript implementations do not support Temporal functionality, but the specification is stable and future-proofed to minimize changes. A polyfill is available for early adoption, though developers should exercise caution in production environments until broader adoption occurs.

