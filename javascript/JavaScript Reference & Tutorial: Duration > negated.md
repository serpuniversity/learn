---

title: JavaScript Temporal.Duration: Working with Time Durations

date: 2025-05-27

---


# JavaScript Temporal.Duration: Working with Time Durations

Working with time durations in JavaScript has become significantly more precise and versatile with the introduction of the Temporal.Duration API. This modern approach to time calculations supports a rich set of features, from creating and representing durations to performing complex arithmetic operations while maintaining component-level precision. The Temporal.Duration object provides a comprehensive framework for handling time differences, including support for calendar durations and timezone-specific calculations. Through detailed methods for creation, manipulation, and comparison, this API offers developers powerful tools for working with time in JavaScript applications.


## Introduction to Temporal.Duration

Temporal.Duration objects represent the difference between two points in time, combining multiple duration components including years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. Each component stores its own sign, with positive durations having all components positive or zero, negative durations having all components negative or zero, and zero duration having all components zero.


### Duration Creation

Temporal.Duration instances can be created using several methods:

- Direct constructor: `new Temporal.Duration(days, hours, minutes, seconds)`

- Static method: `Temporal.Duration.from({ days: 3, hours: 6, minutes: 50 })`

- ISO 8601 strings: `Temporal.Duration.from("P3DT6H50M")`

These methods support both positive and negative durations, with operations preserving the input's exact structure unless explicitly balanced.


### Representations and Output

Durations can be represented in several ways:

- Internal storage: Components with individual positive/negative signs

- ISO 8601 format: "P" followed by time elements (e.g., "P1Y2M10D")

- Integer values: Days, hours, minutes, etc.

- Float values: For subsecond components (up to 9 digits after the decimal point)

The duration format may lose precision for subsecond components unless explicitly preserved as a JSON object.


### Comparison and Calculation

Durations support precise calculations through methods like `add()`, `subtract()`, and `round()`. The `compare()` method returns -1, 0, or 1 based on duration length, with support for custom options like `relativeTo` for timezone-specific calculations. All operations maintain the integrity of underlying time components and do not modify the original duration's structure unless explicitly requested.


## Creating Temporal.Durations

The Temporal.Duration.from() method offers versatile creation options, accepting other Duration objects, duration property objects, or ISO 8601 strings. It supports both positive and negative durations, with the from() method proven convenient for typical use cases compared to direct constructor usage.

The API extends ISO 8601 standards with additional functionality, including negative durations and detailed component handling. For instance, "-P1Y1M" creates a negative duration of 1 year and 1 month, while "P1Y1D" creates a positive duration of 1 year and 1 day. Support for calendar durations enables sophisticated time calculations relative to specific starting points, with non-calendar durations providing portable arithmetic across time zones.

Internal duration representation maintains component integrity using individual positive or negative signs (zero components are omitted when possible). Each component stores its own sign, with positive durations having all components positive or zero, negative durations having all components negative or zero, and zero durations having all components zero. The internal structure remains unbalanced, meaning it retains exact input structure unless explicitly simplified using the balancing process.


## Negation with negated()

The negated() method creates a new Temporal.Duration with all fields maintaining the same magnitude but with the sign reversed. All fields keep their absolute values, only changing their sign: positive fields become negative, and negative fields become positive. The method has no parameters and returns a new Temporal.Duration object with the negated values.

For example, calling negated() on a duration of "P1Y1D" produces "-P1Y1D", while "PT1H30M" becomes "-PT1H30M". This method enables precise representation of opposite durations and supports both positive and negative inputs, with the returned duration maintaining the exact structure of the original unless explicitly simplified.

The negated method operates independently of other duration manipulation features like rounding or balancing. It directly inverts the sign of each component while preserving the underlying magnitude, making it a valuable tool for time arithmetic and comparison operations. The method's behavior aligns with ISO 8601 standards for duration representation, ensuring consistent handling of positive and negative durations across various applications.


## Operation Methods: add(), subtract(), and round()


### Rounding and Balancing

The round() method balances the duration to the largest unit specified, while the add() and subtract() methods balance the result duration to the largest unit of the input durations. For example, adding durations of 1 hour and 30 minutes to 2 hours and 30 minutes results in a balanced duration of 4 hours instead of 3 hours and 60 minutes.

Rounding is particularly important for calendar durations, which contain weeks, months, and years. This rounding ensures that durations can be properly compared and sorted, even when involving years, months, or weeks. For instance, a duration of 30 days rounded to weeks becomes 4 weeks and 2 days, while a duration of 30 seconds rounded to hours becomes 0 hours. In cases where days are involved, the duration is assumed to be 24 hours unless a zoned relativeTo is provided to account for daylight saving time changes.

The Duration class includes several methods for creating duration instances, with options for between(), from(), of(), ofDays(), ofHours(), ofMillis(), ofMinutes(), and ofNanos(). The from() method is particularly flexible, accepting another Duration object, an object with time properties, or an ISO 8601-compliant string.


### Comparison and Sorting

Duration comparison uses the compare() method, which returns -1, 0, or 1 based on the duration's length. For example, to sort three durations, one could use durations.sort(Duration.compare). The comparison can be customized with options like relativeTo, which is particularly important when comparing durations containing years, months, or weeks. Negative durations are compared as negative numbers, making it straightforward to sort them alongside positive durations.

The compare() method requires careful consideration of timezone-specific durations, which must use Temporal.ZonedDateTime as the reference point. This ensures accurate comparison, especially when dealing with durations that span across different time zones or involve daylight saving time changes. For instance, a negative duration of 30 seconds compared to a positive duration of 10 seconds results in -1, demonstrating the method's handling of negative durations as negative numbers.


## Output and Comparison

Temporal.Durations can be compared using the compare() method, which returns -1, 0, or 1 indicating whether the first duration is shorter, equal to, or longer than the second duration. For example, [one, two, three].sort(Duration.compare) sorts durations while [one, two, three].sort((a, b) => Duration.compare(a, b)) illustrates the method's use with custom options like relativeTo for timezone-specific calculations.

TheDuration object represents durations with nanosecond resolution, storing values in seconds and nanoseconds-of-second. This allows precise arithmetic operations while storing a maximum duration greater than the current estimated age of the universe. The duration is measured in "seconds," although scientific precision impacts only durations near leap-seconds and rarely affects most applications.


### Output Formats

Durations are serialized and parsed using ISO 8601 duration format with some ECMAScript extensions. The format consists of:

- An optional sign character (+ or -) representing positive or negative duration

- A literal character P or p standing for "period"

- Numbers followed by literal characters representing:

  - Years (Y)

  - Months (M)

  - Weeks (W)

  - Days (D)

  - Hours (H)

  - Minutes (M)

  - Seconds (S)

- The last component may have a fractional part of 1 to 9 digits, led by a dot or comma

- Zero components may be omitted, but at least one component must be present

- A literal character T or t separating date and time parts (required if time components are present)

- The zero duration is always serialized as PT0S


### Standardization and Conversion

The Duration object facilitates conversion between different time units through its methods. The from() method accepts another Duration object, an object with duration properties, or an ISO 8601-compliant string, making it flexible for various input formats. For instance, Temporal.Duration.from("-P1Y1M") creates a negative duration of 1 year and 1 month, while Temporal.Duration.from("P1Y1D") creates a positive duration of 1 year and 1 day.

The class provides several static methods for creating Duration instances, including between(), from(), of(), ofDays(), ofHours(), ofMillis(), ofMinutes(), and ofNanos(). These methods support both positive and negative durations, with the from() method proving particularly convenient for typical use cases. The Duration object's functionality aligns with ISO 8601 standards, ensuring consistent handling of positive and negative durations across various applications.

