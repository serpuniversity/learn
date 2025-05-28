---

title: JavaScript Temporal.Duration: Working with Time Durations

date: 2025-05-27

---


# JavaScript Temporal.Duration: Working with Time Durations

JavaScript's Temporal.Duration provides a powerful way to work with time intervals, offering precise control over days, hours, minutes, and seconds. This comprehensive guide walks you through creating, manipulating, and understanding these duration objects, from basic construction to advanced operations like calendar-aware arithmetic and formatting for different locales. You'll learn how to work with both calendar and non-calendar durations, handle units overflow, and perform precise time calculations that account for everything from leap years to sub-second precision.


## Duration Fundamentals

A JavaScript `Temporal.Duration` object represents the difference between two time points, supporting precise calculations across days, hours, minutes, and seconds. The duration can be constructed using the `Temporal.Duration` constructor with properties for days, hours, minutes, and seconds. For example:

```javascript

new Temporal.Duration({ days: 3, hours: 6, minutes: 50 })

```

The object's internal representation preserves input values as much as possible, with days directly influencing months and weeks only when explicitly requested. Excess values overflow into larger components: hours range 0-23, minutes 0-59, etc. The `round()` method always balances to the "top-heavy" form, while the `add()` and `subtract()` methods ensure input units remain consistent.

For comparison, durations use the `compare` method, returning -1, 0, or 1 based on the relative length of two durations. Output is formatted as an ISO 8601 duration string, such as "PT79H10M P3DT6H50M P3DT7H630S". Supported options include `relativeTo` for timezone-specific calculations and custom rounding configurations.

The duration format preserves subsecond components as a single fractional number, though balanced durations may lose this precision during serialization. To maintain subsecond accuracy, durations must be manually serialized as JSON objects. The object's canonical string representation uses the ISO 8601 format, with durations serialized as "PT0S" for zero durations. Each component carries its own sign, with negative durations exhibiting all components as negative values.


## Creating and Parsing Durations

Temporal.Duration objects can be created from several sources:

1. Direct Construction:

```javascript

new Temporal.Duration({ days: 3, hours: 6, minutes: 50 })

```

2. ISO 8601 String Parsing:

```javascript

Temporal.Duration.from("P1Y2M3W4DT5H6M7.00800901S")

```

3. Object Properties:

```javascript

Temporal.Duration.from({ hours: 1, minutes: 30 })

```

The duration format preserves subsecond components as a single fractional number. For example, the duration "1 hour, 46 minutes, and 40 seconds" is represented as "90 seconds". Each component has an optimal range: hours 0-23, minutes 0-59, etc. Excess values overflow into larger components.

For timezone-specific calculations, use the `relativeTo` option when creating durations:

```javascript

Temporal.Duration.from({ hours: 1, minutes: 30 }, { relativeTo: new Temporal.PlainDateTime() })

```


### Parsing ISO 8601 Strings

Temporal.Duration supports parsing ISO 8601 duration strings, including extensions for weeks, months, and years:

```javascript

Temporal.Duration.from("P1Y2M3W4DT5H6M7.00800901S")

```

The parser handles various valid formats, such as:

- P1Y2M10D (1 year, 2 months, 10 days)

- PT1H30M (1 hour, 30 minutes)

- P3DT12H (3 days, 12 hours)

Negative durations are supported:

```javascript

Temporal.Duration.from("-P1Y1M")

```


### Duration Properties and Methods

A `Temporal.Duration` object contains the following properties:

- `days`, `hours`, `microseconds`, `milliseconds`, `minutes`, `months`, `nanoseconds`, `seconds`

- `sign` (1 for positive, -1 for negative, 0 for zero)

- `weeks`

Key methods include:

- `abs()`: Returns a new duration with the absolute value

- `add()`: Adds another duration and balances the result

- `negated()`: Returns a new duration with the negated value

- `round()`: Rounds to the specified unit and balances

- `subtract()`: Subtracts another duration and balances the result

- `toJSON()`: Returns an ISO 8601 string

- `toLocaleString()`: Returns a language-sensitive string representation

- `toString()`: Returns an ISO 8601 string

- `total()`: Returns the total duration in the specified unit

- `weeks()`: Returns the number of weeks (experimental)

- `years()`: Returns the number of years (experimental)

The `compare` method returns -1, 0, or 1 for duration comparisons, with timezone awareness through the `relativeTo` option:


## Calendar vs. Non-Calendar Durations

JavaScript's Temporal.Duration fundamentally represents intervals in time as combinations of years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. However, these durations can be categorized into two types: calendar durations and non-calendar durations, each with distinct characteristics and use cases.


### Calendar Durations

Calendar durations incorporate components for weeks, months, and years, making them essential for contexts where date-specific calculations are required. These durations are aware of calendar variations, such as different numbers of days in various months and the presence of leap years. As such, they cannot be used directly in date/time arithmetic without specifying a reference point or calendar context.

For calendar duration arithmetic, operations must be performed relative to a starting point using date arithmetic. This means that while you can add or subtract calendar durations, you need to provide a specific date as a reference for these operations to produce meaningful results. For example, adding a "1 year and 2 months" duration to a given date won't automatically account for the varying number of days between months.


### Non-Calendar Durations

Non-calendar durations represent fixed, calendar-agnostic periods of time. These durations are portable and can be used directly in arithmetic operations without external context. For instance, you can add "1 hour and 30 minutes" directly to a date object without any additional information.

Non-calendar durations adhere to fixed ranges for their components: hours 0-23, minutes 0-59, etc. When overflow occurs, values carry into larger units. For example, adding 1 hour and 60 minutes results in 2 hours.


### Operational Differences

While both types of durations share many operations (such as round(), total(), and compare()), they handle these operations differently based on their nature. Non-calendar durations can be directly manipulated and combined without requiring context. Calendar durations, however, need a reference point to perform operations that depend on specific date details.

To create or manipulate durations, developers use the Temporal.Duration.from() method, which accepts various inputs including other duration objects, property objects, or ISO 8601 strings. For direct duration creation, the Temporal.Duration constructor can be used with up to 10 time units (years, months, weeks, days, etc.).

Understanding these distinctions is crucial for effective use of Temporal.Duration in JavaScript applications, especially when working with date arithmetic and time calculations that require calendar awareness versus fixed time intervals.


## Duration Operations


### Duration Operations

The `Temporal.Duration` object offers several methods for manipulating durations. These operations include basic arithmetic and formatting options that help developers work with time intervals in JavaScript.


### Balancing and Rounding

To maintain consistent unit representation, `Temporal.Duration` objects are initially created in an unbalanced state, preserving exact input values. The `balance()` method ensures that smaller units are converted into larger ones when necessary. For example, adding 100 seconds to a duration results in 100 seconds unless explicitly balanced:

```javascript

const d = Temporal.Duration.from({ seconds: 100 });

console.log(d.seconds); // 100

d = d.round({ largestUnit: "auto" });

console.log(d); // PT81M30S

```

This behavior allows precise tracking of sub-second components until the `round()` method is called with a specified `largestUnit` option. For instance, setting `largestUnit` to "hour" balances the duration fully:

```javascript

const d = Temporal.Duration.from({ minutes: 80, seconds: 90 });

d = d.round({ largestUnit: "hour" });

console.log(d); // PT1H21M30S

```


### Date Arithmetic Requirements

When performing operations that depend on calendar-specific information, such as adding months or years, developers must provide a reference date using the `relativeTo` option. This is particularly important for calculations involving leap years and Daylight Saving Time transitions:

```javascript

const d = Temporal.Duration.from({ years: 1, months: 1 });

const referenceDate = new Temporal.PlainDate(2020, 1, 1);

const result = d.add({ relativeTo: referenceDate });

console.log(result); // PT12M

```

Without a specified reference date, operations that require calendar context will produce incorrect results due to variations in month lengths:

```javascript

const d = Temporal.Duration.from({ years: 1, months: 1 });

console.log(d); // PT12M (unbalanced)

d = d.round({ largestUnit: "month" });

console.log(d); // PT12M (still unbalanced)

```


## Advanced Features

The `Temporal.Duration` object offers several experimental features and advanced formatting options:


### Duration Exports

The duration can be exported using the Symbol.toStringTag property, which returns the string "Temporal.Duration" when used with Object.prototype.toString. This allows developers to identify duration objects through standard JavaScript means.


### Experimental Features

Two experimental methods provide additional functionality:

- `weeks()`: Returns the number of weeks in the duration

- `years()`: Returns the number of years in the duration

These methods allow developers to extract specific time components without needing to parse the duration string manually.


### Advanced Formatting

JavaScript's `Temporal.Duration` integrates with the Intl.DurationFormat API for language-sensitive duration representation. The `format()` method of `Intl.DurationFormat` instances requires a duration object with properties for years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. Each property should contain an integer value, maintaining consistent signs.

The method returns a formatted string based on the locale and styling options provided. For example, using the English language returns durations in the format "1 yr, 2 mths, 3 wks, 3 days, 4 hr, 5 min, 6 sec, 7 ms, 8 Î¼s, 9 ns". Additional options, such as style "long" or "narrow", produce different representations like "1 year, 2 months, 3 weeks, 3 days, 4 hours, 5 minutes, 6 seconds, 7 milliseconds, 8 microseconds, 9 nanoseconds" or "1y 2mo 3w 3d 4h 5m 6s 7ms 8Î¼s 9ns".

For localization, developers can use specific locale settings and style options to generate language-sensitive duration formats. This integration provides flexibility in displaying time intervals according to user preferences and regional standards.

