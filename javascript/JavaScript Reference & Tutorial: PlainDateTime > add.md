---

title: Temporal.PlainDateTime.prototype.add() in JavaScript

date: 2025-05-27

---


# Temporal.PlainDateTime.prototype.add() in JavaScript

JavaScript's Temporal API introduces sophisticated date and time capabilities, including the `PlainDateTime` object and its `add()` method. While `PlainDateTime` represents precise calendar and wall-clock data, `add()` enables flexible and powerful time manipulation according to precise temporal rules. This guide explores how to use the `add()` method to extend JavaScript's date arithmetic beyond basic operations, handling complex cases like calendar-specific intervals and overflow constraints.


## Temporal Date and Time Fundamentals

Temporal API introduces two fundamental date and time data types: PlainDateTime and Instant. While both represent specific points in time, they serve distinct purposes and have specific characteristics.

PlainDateTime represents a calendar date and wall-clock time with nanosecond precision, but crucially, it contains no timezone information. This makes it ideal for scenarios where timezone data is stored separately or when dealing with legacy systems. It supports a wide range of date and time parameters, including year, month, day, hour, minute, second, millisecond, microsecond, and nanosecond, with default values set to zero if not specified. The API provides both a constructor and a convenient from() method for creating PlainDateTime objects, with the constructor requiring that the provided date parameters (year, month, day) form a valid ISO 8601 date.

Instant, by contrast, represents a single point in time with nanosecond precision and does not contain any date or timezone information itself. Under the hood, it relies on the ISO-8601 calendar and UTC time zone, but these aspects can be overridden using a provided timezone argument. To create an Instant object, you typically need a timestamp in nanoseconds. The API offers several creation methods, including Temporal.Now.instant() and Temporal.Instant.from("2022-01-01-06:00"), demonstrating the flexibility of the Instant type in representing absolute points in time.


## Temporal.PlainDateTime.prototype.add() Method

The `Temporal.PlainDateTime.prototype.add()` method returns a new `Temporal.PlainDateTime` object representing the original date-time plus the specified duration. This method accepts a duration parameter, which can be a string, object, or `Temporal.Duration` instance. The duration is converted using the same algorithm as `Temporal.Duration.from()`.

The method also supports an optional second parameter for options, including `overflow`, which determines how to handle date component overflow. The `overflow` property can take two values: `"constrain"` (default), which clamps the date component to the valid range, and `"reject"`, which throws a `RangeError` for out-of-range values.


### Implementation Details

The method performs its calculations using the same algorithm as `Temporal.PlainDate.prototype.add()`, adding the duration to the date while maintaining the immutable object design principle. The result is a fresh `Temporal.PlainDateTime` instance representing the new date-time value.


### Error Handling

The method enforces strict boundaries for date-time values, returning a `RangeError` if the resulting date-time falls outside the representable range of ±(108 + 1) days, or approximately ±273,972.6 years, from the Unix epoch.


### Performance Considerations

The method is designed for precise date-time calculations while maintaining the performance benefits of the Temporal API through efficient, format-optimized operations. It handles conversions and calculations internally, providing a reliable foundation for applications requiring accurate date-time manipulation.


## Method Parameters and Options

The `add()` method accepts a duration as a string, object, or `Temporal.Duration` instance. When provided with a string, it must conform to a specific format that Temporal understands. For objects, the method looks for properties that represent time components like year, month, day, hour, minute, second, millisecond, microsecond, and nanosecond, with default values set to zero if not specified.

A practical example demonstrates adding 30 minutes to a given time:

```javascript

Temporal.PlainDateTime.add(dt, 30, smallestUnit: 'minute', roundingMode: 'floor' });

```

This call would adjust the time by rounding down to the nearest minute.

The duration can also include calendar-related properties like `era`, `eraYear`, and custom calendar systems. Supported calendars include 'gregory', 'prolepticGregorian', 'iso8601', and 'julian'. The calendar system defaults to 'iso8601', which is the standard Gregorian calendar.

For creating or modifying `Temporal.PlainDateTime` objects, several utility methods are available. The `with()` method allows creating a new object while overriding specific properties from a `dateTimeLike` input. This can be particularly useful for modifying just one or two components of an existing date-time value.

The `withPlainTime()` method specializes in setting or modifying the clock time of a `Temporal.PlainDateTime` object. It accepts `Temporal.PlainTime` objects, plain objects with time properties, strings, or existing `Temporal.PlainDateTime` objects, always defaulting missing time units to zero.

These methods, combined with the primary `add()` functionality, provide robust support for date and time manipulation while maintaining the immutable object design principles of the Temporal API.


## Date Overflow and Range Handling

The `add()` method implements careful date overflow handling through its `options.overflow` parameter, which defaults to `"constrain"`, meaning it will clamp out-of-range values to the nearest valid date. For example, adding one day to "2021-12-31" with the default `"constrain"` behavior results in "2022-01-01", while setting overflow to `"reject"` would instead throw a `RangeError`.

All calendar-related fields - including year, month, and day - are subject to these overflow rules. Internally, the method handles up to 59 seconds in a minute, clamping to 59 as required by the representable range. Full-year month values are treated as 0-based, meaning January is represented as 0.

The calendar system affects the computation of month lengths and leap years. For instance, adding one year to "2021-02-28" with the default Gregorian calendar yields "2022-02-28", correctly accounting for the non-leap year. The method ensures the result remains within the Temporal API's representable range of approximately ±273,972.6 years centered on the Unix epoch, with operations failing outside this boundary.

The implementation demonstrates a careful balance between precise arithmetic and practical date handling, making it a robust tool for date-time manipulation in JavaScript applications.


## Usage Examples and Best Practices

The add() method offers several practical uses cases for common date-time manipulations. Adding time intervals in various units demonstrates its flexibility:

```javascript

// Increment a date by 30 days

Temporal.PlainDateTime.add(dt, 30, smallestUnit: 'day');

// Add 1 year, 6 months, and 2 weeks to a date

Temporal.PlainDateTime.add(dt, '1y6M2w');

// Modify the time to 10:30:45

Temporal.PlainDateTime.add(dt, { hour: 10, minute: 30, second: 45 });

```

Its functionality extends to calendar-specific operations, such as:

```javascript

// Add one Gregorian calendar month to a date

Temporal.PlainDateTime.add(dt, { month: 1 }, { calendar: 'gregory' });

// Switch to Julian calendar and add one month

Temporal.PlainDateTime.add(dt, { month: 1 }, { calendar: 'julian' });

```

Business applications can leverage the method for scheduling and time calculations:

```javascript

// Calculate next business hour

Temporal.PlainDateTime.add(NOW, { minute: 30 }, { calendar: businessSchedule });

```

Handling date overflow and range constraints safely protects application logic:

```javascript

// Correctly handle leap year transitions

Temporal.PlainDateTime.add(dt, 1, { unit: 'year' });

// Ensure value stays within valid range

Temporal.PlainDateTime.add(dt, 108.1, { unit: 'day' });

```

For advanced operations, the method integrates with other Temporal API features:

```javascript

// Compute exact event time

Temporal.PlainDateTime.add(eventStartDate, event_duration);

// Determine timezone-aware arrival time

Temporal.ZonedDateTime.add(arrivalDateTime, flight_duration);

```

