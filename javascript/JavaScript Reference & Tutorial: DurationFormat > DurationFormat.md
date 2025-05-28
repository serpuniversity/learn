---

title: Temporal.Duration in JavaScript: Properties, Methods, and Formatting

date: 2025-05-26

---


# Temporal.Duration in JavaScript: Properties, Methods, and Formatting

Working with dates and times in JavaScript can be complex, especially when you need to perform precise calculations involving durations. The Temporal.Duration object provides a powerful solution for representing and manipulating time differences, combining multiple units from nanoseconds to centuries. This article explores the capabilities of Temporal.Duration, from its basic properties to advanced formatting options and arithmetic operations. You'll learn how to create and manipulate duration objects, format them according to different styles and locales, and perform precise time calculations using the modern JavaScript API.


## Introduction toTemporal.Duration

The Temporal.Duration object represents differences between time points, enabling precise date and time arithmetic in JavaScript. This object combines multiple time units including years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds, allowing for representing durations from nanoseconds to centuries.

The format() method, part of the Intl.DurationFormat API, provides flexible duration formatting based on locale and style preferences. Available locales include English, French, and others, with formatting rules derived from Unicode Technical Standard 35. The API supports three style options: long (fully spelled out), short (abbreviated), and narrow (most compact), defaulting to digital formatting.

Each Temporal.Duration instance contains properties representing its constituent time units. The days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds properties provide direct access to these components. The sign property indicates whether the duration is positive (1), negative (-1), or zero (0), while the [Symbol.toStringTag] property always returns "Temporal.Duration".

Durations can be manipulated through several methods. The abs() method returns the duration's absolute value, while negated() returns a duration with the opposite sign. The add() and subtract() methods perform arithmetic operations, combining or separating durations as needed. The round() method balances durations to the nearest unit specified by the largestUnit option, ensuring optimal representation of calendar units like days and months. The toJSON() method serializes durations in ISO 8601 format, while toLocaleString() generates language-sensitive string representations based on the current locale settings.


## duration Object Properties

The Temporal.Duration object represents durations using a combination of years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. According to the JavaScript specification, these durations are fundamentally represented as a combination of these components, though the implementation allows some flexibility beyond the basic structure.

The duration is constructed using a standardized ISO 8601 format that can represent periods from nanoseconds to centuries. The string structure begins with an optional sign character, followed by a 'P' or 'p' representing the period, followed by the component values in descending order: years, months, weeks, days, hours, minutes, seconds. The time components may include fractions of a second, with up to nine digits after the decimal point. While weeks cannot contain other units, the implementation allows combining weeks with other time components.

Each duration is represented as a JavaScript object with properties corresponding to the time units. The days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds properties provide direct access to these components. The months property represents the number of calendar months, while the sign property indicates whether the duration is positive, negative, or zero. The [Symbol.toStringTag] property consistently returns "Temporal.Duration".


## format() Method and Options

The format() method of Intl.DurationFormat instances processes duration objects according to the locale and formatting options of the DurationFormat object. The method requires a duration object as a parameter, which should include some or all of the following: years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. Each property's value should be an integer, and their signs should be consistent.

The format() method supports three primary styles: 'long' (fully spelled out), 'short' (abbreviated), and 'narrow' (most compact). These styles produce progressively more concise representations of the duration. For instance, a duration might be formatted as "1 yr, 2 mths, 3 wks, 3 days, 4 hr, 5 min, 6 sec, 7 ms, 8 Î¼s, 9 ns" in basic format, "1 year, 2 months, 3 weeks, 3 days, 4 hours, 5 minutes, 6 seconds, 7 milliseconds, 8 microseconds, 9 nanoseconds" in long format, or "1y 2mo 3w 3d 4h 5m 6s 7ms 8Î¼s 9ns" in narrow format.

The method's output varies based on the specified locale. The examples provided include English ("1 hour, 46 minutes and 40 seconds"), French ("1 heure, 46 minutes et 40 secondes"), Portuguese ("1h 46min 40s"), and Italian ("1 ora, 46 minuti e 40 secondi"). The formatting may also include non-breaking spaces or bidirectional control characters, though these are not dependent on the format style.

The method works across modern browsers and devices, with full support beginning in March 2025. Implementation examples demonstrate usage with different locale styles: "1 hr, 46 min and 40 sec" for short English format, "1h 46min 40s" for narrow Portuguese format, and "1 hour, 46:40" for digital English format with long hours styling.


## Comparison and Arithmetic Methods

The compare() method allows direct comparison of duration objects, returning -1, 0, or 1 to indicate which duration is shorter, equal to, or longer than the other. This method is particularly useful for determining the relative size of time periods without converting them to a common unit.

The add() and subtract() methods combine or separate durations, respectively. These operations follow specific rules based on the component units: weeks are carried into months only if explicitly requested, and calendar units like days are directly carried into months. When working with calendar durations that include years, months, or weeks, a relative date must be specified to account for varying month and day lengths across calendars.

The round() method balances durations to the nearest unit specified by the largestUnit option, ensuring optimal representation. For example, rounding "PT75H" to days results in "P3D" rather than "P3.125D". This method always returns a "top-heavy" form, up to the specified largest unit.

The abs() method returns a new duration with the absolute value, while the negated() method returns a duration with the opposite sign. These operations maintain the underlying duration structure while allowing for signed values to represent events in the past or future. The sign property indicates whether the duration is positive, negative, or zero, providing clear metadata about the duration's direction.


## Locale and Numbering System Support

The Temporal.Duration object supports formatting in multiple locales and numbering systems, allowing precise control over how time durations are presented. The formatting process begins with the Intl.DurationFormat constructor, which requires an optional locales parameter and options object. The locales parameter determines the language and regional conventions used in formatting, while the options object allows customization of the output style and other formatting options.

The DurationFormat object supports three primary styles: 'long' (fully spelled out), 'short' (abbreviated), and 'narrow' (most compact). Each style generates progressively more concise representations of the duration, with the default style being digital. The format method requires a duration object as input, which should include properties for years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds. Each property's value should be an integer, and their signs must be consistent.

The formatting process works across modern browsers and devices, with full support beginning in March 2025. The implementation draws from Unicode Technical Standard 35 for its formatting rules, ensuring compatibility with a wide range of languages and numbering systems. The API works similarly to the Intl.RelativeTimeFormat object, allowing for flexible localization while maintaining consistent output across implementations.

The numbering system is determined by the Unicode Locale Identifier type, with the CLDR serving as the recommended source for locale data. The formatToParts method returns an array of objects representing the formatted duration in parts, allowing for fine-grained control over the presentation of individual components. The resolvedOptions method returns an object containing the locale and options computed during the DurationFormat's initialization, providing transparency into the formatting process.

