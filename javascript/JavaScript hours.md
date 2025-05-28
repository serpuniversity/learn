---

title: JavaScript Duration: Working with Hours and Other Units

date: 2025-05-27

---


# JavaScript Duration: Working with Hours and Other Units

Working with time durations in JavaScript can be complex due to limited built-in support and varying requirements across applications. The Temporal.Duration API offers a modern solution, providing robust methods for duration calculations with support for years, months, and sub-second precision. This guide explores how to create, manipulate, and format durations using the Temporal API while highlighting best practices for accurate time measurements in JavaScript.


## JavaScript Duration Overview

The Temporal.Duration object represents time differences using days, hours, minutes, and seconds, following ISO 8601 standards with some ECMAScript extensions. Each component (days, hours, microseconds, milliseconds, minutes, months, nanoseconds, seconds) can have positive, negative, or zero values, and mixed sign components are invalid.


### Duration Representation and Construction

Temporal.Duration instances can be created using the `from()` method in several ways:

- From another Temporal.Duration object

- From an object with time properties

- From an ISO 8601-compliant string

For example, `Temporal.Duration.from({ days: 3, hours: 6, minutes: 50 })` creates a duration of 3 days, 6 hours, and 50 minutes. The API also supports negative durations and includes extensions to the ISO 8601 standard.


### Duration Components and Balancing

The duration object retains input values as much as possible, with components having optimal ranges: hours 0-23, minutes 0-59, etc. Excess values overflow into larger components, and the object balances durations into "top-heavy" form, up to a specified largest unit. The `round()` method manages this process, while `add()` and `subtract()` methods also balance results to input units.


### Subsecond Handling and Serialization

Durations can represent periods ranging from years to nanoseconds and handle complex real-world time variations such as leap years and time zone differences. The serialized format uses the ISO 8601 duration format, which represents subsecond components as a single fraction number. To preserve subsecond precision, developers must serialize durations as JSON objects rather than using the default ISO 8601 format.


## Creating and Manipulating Durations

Temporal-duration instances can be created using several methods, the most common being `Temporal.Duration.from()`, which accepts various inputs including another Temporal-duration object, an object with time properties, or an ISO 8601-compliant string. For example, `Temporal.Duration.from({ days: 3, hours: 6, minutes: 50 })` creates a duration of 3 days, 6 hours, and 50 minutes.

The API also includes methods for specific units of time:

- `Temporal.Duration.ofDays(days: Number)` creates a duration from standard 24-hour days, with seconds calculated based on 86400 seconds per day. This method throws an ArithmeticException if the input exceeds Duration capacity.

- `Temporal.Duration.ofHours(hours: Number)` creates a duration from standard hours, with seconds calculated based on 3600 seconds per hour. Similarly, this method throws an ArithmeticException for inputs exceeding Duration capacity.

- `Temporal.Duration.ofMillis(millis: Number)` creates a duration from milliseconds, extracting seconds and nanoseconds from the specified amount. This method returns a duration instance.

- `Temporal.ofMinutes(minutes: Number)` creates a duration from standard minutes, calculating seconds based on 60 seconds per minute. This method throws an ArithmeticException for inputs exceeding Duration capacity.

Developers can manipulate these durations using methods like `add()` and `subtract()`, which return new duration objects rather than modifying the original. Balancing units can be managed with the `round()` method, allowing specification of the largest unit in the final result.

For real-time applications, developers often measure durations using `console.time()` and `console.timeEnd()`, or by tracking `Date.getTime()` values before and after the event. For precise duration calculations, `Temporal.Duration.from()` remains the recommended approach, providing consistent results across both calendar and non-calendar durations.


## Duration Formatting and Comparison

The Temporal API provides two primary methods for duration formatting: the `Temporal.Duration.prototype.toString()` method and the `Intl.DurationFormat` API.

The `toString()` method returns duration values in ISO 8601 format, while `Intl.DurationFormat` offers more flexible localization options. For example, the duration "3 days, 6 hours, and 50 minutes" would be formatted as "P3DT6H50M" using `toString()`, but could be localized to "3 d, 6 h, 50 m" using `Intl.DurationFormat`.

Developer Tool Support: While the modern developer tools and browsers support these features, developers should consider providing fallbacks for older environments. The MDN documentation mentions compatibility across "the latest devices and browser versions," but developers should validate compatibility across their target environments.

When using `Intl.DurationFormat`, developers can specify various options such as style, unit display, and relative-to values. The `style` property can take values like "long," "narrow," or "short" to control the format's verbosity. The `unitDisplay` property chooses between showing full units (like "day" vs. "d") and can be set to "narrow" for space-saving applications.

For timezone-specific calculations, developers can use the `relativeTo` option in both `Temporal.Duration.compare()` and `Intl.DurationFormat`. This ensures that durations are correctly adjusted for time zone differences, particularly important when comparing durations across different time zones or when working with daylight saving time transitions.

When sorting durations, developers should use the `Temporal.Duration.compare()` method with the appropriate `relativeTo` value for years, months, or weeks. The method returns -1, 0, or 1 for shorter, equal, or longer durations, respectively. This approach ensures correct sorting even when dealing with complex time period calculations, including those affected by daylight saving time changes.


## Balancing and Rounding Durations

The `round()` method is central to managing the balanced representation of durations. When creating a duration with 100 seconds using `Temporal.Duration.from({ seconds: 100 })`, the duration remains unbalanced until explicitly balanced using `round`. This occurs with `d = d.round({ largestUnit: "auto" });`, converting 100 seconds to "81M30S" (81 minutes and 30 seconds) - the method balances seconds into minutes but leaves minutes unbalanced.

To fully balance the duration, you'd then call `d = d.round({ largestUnit: "hour" });`, resulting in "1H21M30S" (1 hour, 21 minutes, and 30 seconds). This process demonstrates how the `round()` method allows specifying the largest unit in the final result, while smaller units are adjusted appropriately.


### Balancing Mechanism

The underlying mechanism preserves input values as much as possible. Days are carried directly into months, while weeks require explicit request due to their dependency on calendar systems. Determining how many units fit into another introduces complexity, particularly for calendar-related components like months and years.


### Calendar Considerations

For calendar durations, the `relativeTo` option becomes crucial for operations. This parameter requires either a `Temporal.ZonedDateTime` for timezone-specific calculations or a `Temporal.PlainDate` for timezone-neutral data. This ensures accurate handling of variations like leap years and daylight saving time transitions.


### Subsecond Handling

During serialization, the default ISO 8601 format loses subsecond precision. To maintain this information, durations must be serialized as JSON objects rather than using the standard ISO 8601 format, which represents subsecond components as single fraction numbers.


## Best Practices for Duration Calculations

When measuring time durations in JavaScript, developers have multiple options, each with its own strengths and trade-offs. Built-in methods like `Date.now()` and `Date.getTime()` provide straightforward ways to measure durations, but they have limitations in precision and compatibility. For precise measurements, developers can use `console.time()` and `console.timeEnd()`, though this method is limited to modern browsers.

The recommended approach for consistent cross-browsers compatibility is the `Temporal.Duration` API. This modern JavaScript standard provides robust capabilities for duration calculations, including precise sub-second measurements and support for calendar durations. The API's methods like `add()`, `subtract()`, and `round()` enable complex time arithmetic while maintaining consistent results across different systems.

In practice, developers should use `Temporal.Duration` for time measurements where precision and portability are essential. For simpler cases, the built-in methods can be sufficient, but developers should be aware of their limitations. The MDN Web Docs provide comprehensive guidance on using `Temporal.Duration`, including compatibility information and advanced usage scenarios.

