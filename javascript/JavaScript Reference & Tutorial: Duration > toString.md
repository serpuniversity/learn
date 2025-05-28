---

title: JavaScript Time Duration Formatting

date: 2025-05-27

---


# JavaScript Time Duration Formatting

Date and time handling in JavaScript has evolved significantly with the introduction of the Temporal API and existing libraries like moment.js and Date-FNS. These tools offer powerful capabilities for duration parsing, manipulation, and formatting. The `Temporal.Duration.prototype.toString()` method represents a key part of this evolution, providing a standardized way to represent durations in ISO 8601 format while offering options for customizing the output. This article explores the intricacies of duration formatting in JavaScript, from the native capabilities of the Temporal API to popular library implementations and browser support.


## Temporal.Duration.prototype.toString()

The `toString()` method of `Temporal.Duration` instances returns a string representing the duration in ISO 8601 format. This method is experimental and not supported in all widely-used browsers.

According to the Temporal specification, the `toString()` method accepts an optional `options` object with the following properties:

- `fractionalSecondDigits`: An integer from 0 to 9, or the string "auto". If "auto", trailing zeros are removed from the fractional seconds. Otherwise, the fractional part contains this many digits, padded with zeros or rounded as necessary.

- `roundingMode`: A string specifying how to round fractional second digits beyond `fractionalSecondDigits`. Defaults to "trunc".

- `smallestUnit`: A string specifying the smallest unit to include in the output. Possible values are "second", "millisecond", "microsecond", and "nanosecond. If specified, `fractionalSecondDigits` is ignored.

Examples of usage demonstrate that the method returns null if called on a null object and follows the ISO 8601 format for representing durations, including:

- 20.345 seconds: "PT20.345S"

- 15 minutes: "PT15M"

- 10 hours: "PT10H"

- 2 days: "PT48H"

When formatting options are provided, the method can include specific units and control the precision of fractional seconds:

```javascript

const duration = Temporal.Duration.from({ days: 2, hours: 3, minutes: 4, seconds: 
5.1234 });

console.log(duration.toString({ fractionalSecondDigits: 6, roundingMode: "round", smallestUnit: "millisecond" }));

// Output: PT2D3H4M5.123400S

```

The method throws a `RangeError` if any of the options is invalid, ensuring robust handling of edge cases.


## Duration Formatting Libraries and Functions

Three popular approaches to formatting time durations in JavaScript include custom implementations, library functions, and standards-based methods.

Custom Implementations

The documentation presents two effective approaches for converting durations to human-readable formats:

1. Using browser-supported formatting capabilities with i18n support:

This method combines a `divMod` helper function, a `createDurationFormatter` function, and `Intl.ListFormat` for locale-specific formatting. It works correctly up to days and provides both long and short format options for English and Spanish locales.

2. An anonymous time conversion function:

This approach demonstrates basic duration formatting without additional libraries. It uses simple math operations to calculate hours, minutes, and seconds from the input duration, demonstrating a straightforward implementation.

Library Functions

The provided documentation includes implementations using popular JavaScript libraries:

1. Moment.js

The library's `moment.duration().toISOString()` method returns ISO 8601-formatted strings for durations. This method uses the native Date API for improved performance when available.

2. Date-FNS

While not explicitly documented here, the library has been mentioned in related contexts for its time duration formatting capabilities.

Browser-native Methods

Several simple, built-in approaches are presented for formatting durations:

1. Custom string manipulation functions

These functions demonstrate basic techniques for converting seconds to HH:MM:SS format using integer division and modulo operations.

2. Date object methods

The provided documentation includes examples of using the Date object to format durations, with additional context on its implementation details and compatibility considerations.

These examples represent a comprehensive overview of JavaScript's capabilities for formatting time durations, from simple built-in methods to sophisticated library-based solutions.


## Duration Parsing and Manipulation

JavaScript's `Temporal.Duration` class provides comprehensive support for time duration parsing and manipulation, though implementation details differ between browsers and libraries. The class supports ISO-8601 duration format parsing and offers multiple methods for duration handling:


### Parsing and Validation

Temporal.Duration instances accept ISO-8601 formatted strings, including full and partial duration specifications:

- "PT20.345S" parses as "20.345 seconds"

- "PT15M" parses as "15 minutes" (900 seconds)

- "PT10H" parses as "10 hours" (36,000 seconds)

- "P2D" parses as "2 days" (172,800 seconds)

- "P2DT3H4M" parses as "2 days, 3 hours, and 4 minutes"

- "-P6H3M" parses as "-6 hours and -3 minutes"

- "-P-6H+3M" parses as "+6 hours and -3 minutes"

The class uses the `DateTimeParseException` for handling parsing errors, providing clear feedback when input is invalid.


### Duration Manipulation

The `Temporal.Duration` class includes several powerful manipulation methods:

- `abs()`: Returns a duration with a positive length, effectively removing negative total length

- `addTo(temporal)`: Adds the duration to a specified temporal object, returning an adjusted temporal object of the same type

- `compareTo(otherDuration)`: Compares the current duration to another, returning a comparator value

- `dividedBy(divisor)`: Divides the duration by a specified value, using floating point arithmetic

These methods enable precise control over duration calculations while maintaining compatibility with existing date and time APIs. For example:

```javascript

const d1 = Temporal.Duration.from("PT1H");

const d2 = Temporal.Duration.from("PT30M");

console.log(d1.add(d2)); // PT1H30M

```

Additional methods allow for rounding and total calculation:

```javascript

Temporal.Duration.from("PT75H").round("day"); // P3D

const d = Temporal.Duration.from("P4DT12H30M5S");

console.log(d.milliseconds); // 0

console.log(d.total("millisecond")); // 390605000

```


### Browser and Library Support

While native support varies between browsers, several libraries provide robust duration handling:

- **moment.js**: Offers `moment.duration().toISOString()` for ISO 8601 parsing

- **Date-FNS**: Provides flexible time conversion capabilities

- **tinyduration**: A smaller library handling ISO 8601 durations with simple installation via npm/Yarn

- **Temporal Proposal**: A TC39 initiative defining standardized duration handling, with polyfill support in Chrome DevTools

These tools offer a range of options for developers, from simple built-in methods to sophisticated library-based solutions, ensuring comprehensive coverage of time duration formatting and manipulation needs.


## Browser Compatibility and Implementation Details


### Built-in Date Methods

All modern browsers implement the `Date.prototype.toString()` method, which returns a date as a string in the local timezone. This method combines the string representations of the date and time from `toDateString()` and `toTimeString()`, respectively, with a space in between. The resulting string format is "Thu Jan 01 1970 00:00:00 GMT+0000 (Coordinated Universal Time)".

For example:

```javascript

const date = new Date();

console.log(date.toString()); // Output varies based on local time

```


### ISO 8601 Parsing and Duration Handling

While JavaScript's built-in Date API lacks native support for durations, several libraries and proposals address this gap. The Temporal API, currently in development by TC39, introduces standardized duration handling. The `Temporal.Duration.from()` method creates new duration objects from various sources:

- Another `Temporal.Duration` object

- An object with duration properties

- An ISO 8601 string

The duration object provides properties for accessing elements or calculating totals:

```javascript

const d = Temporal.Duration.from("P4DT12H30M5S");

console.log(d.milliseconds); // 0

console.log(d.total("millisecond")); // 390605000

```

Additional functionality includes:

- Duration addition

- Rounding to the nearest unit of time

- Total calculation with a relative date

```javascript

const d1 = Temporal.Duration.from("PT1H");

const d2 = Temporal.Duration.from("PT30M");

console.log(d1.add(d2)); // PT1H30M

Temporal.Duration.from("PT75H").round("day"); // "P3D"

```


### Library Support

Several libraries offer robust duration handling capabilities:

- **moment.js**: Provides `moment.duration().toISOString()` for ISO 8601 parsing

- **Date-FNS**: Offers flexible time conversion functionality

- **tinyduration**: A lightweight library handling ISO 8601 durations through npm/Yarn installation

For developers needing immediate duration functionality, these tools provide comprehensive solutions while awaiting full browser support.

