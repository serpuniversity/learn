---

title: JavaScript RelativeTimeFormat: Formatting Relative Time with Locale Awareness

date: 2025-05-26

---


# JavaScript RelativeTimeFormat: Formatting Relative Time with Locale Awareness

Relative time formatting is crucial for creating user-friendly date and time displays that adapt to local conventions and contexts. JavaScript's Intl.RelativeTimeFormat API provides a powerful solution for language-sensitive relative time formatting, supporting multiple styles and units while handling complex edge cases. In this comprehensive exploration, we'll examine how to effectively utilize RelativeTimeFormat, from basic usage to advanced customization. We'll also examine its implementation details, browser support, and best practices for developers looking to incorporate this functionality into their applications.


## RelativeTimeFormat Overview

The RelativeTimeFormat constructor creates objects that enable language-sensitive relative time formatting. It supports three style options: "long", "short", and "narrow".

Instance methods include:

- format(value, unit): Formats a value and unit according to the locale and formatting options

- formatToParts(value, unit): Returns an array of objects representing the relative time format in parts

- resolvedOptions(): Returns information about the object's locale and formatting options

The prototype inherits properties from Intl.RelativeTimeFormat.prototype, including:

- constructor: The constructor function that created the instance object

- [Symbol.toStringTag]: The initial value of the Symbol.toStringTag property (set to "Intl.RelativeTimeFormat")

RelativeTimeFormat supports the following units:

- year

- quarter

- month

- week

- day

- hour

- minute

- second

Key behaviors for formatting include:

- "always" numeric option formats "1 day ago" or "in 1 day"

- "auto" numeric option:

  - "yesterday" for -1

  - "tomorrow" for 1

  - "now" for 0 seconds

  - "today" for 0 days

  - "this minute" for 0 minutes

The specified locales and options must be valid, or a RangeError will be thrown. Supported locales can be checked using the static method supportedLocalesOf().


## RelativeTimeFormat Implementation

The RelativeTimeFormat constructor creates new objects with specified locales and options. When creating an instance, locales and options must be valid; otherwise, a RangeError is thrown. The constructor supports three style options: "long", "short", and "narrow".

Instance methods include:

- format(value, unit): Returns a string representing the given value and unit formatted according to the locale and formatting options

- formatToParts(value, unit): Returns an array of objects representing the relative time format in parts

- resolvedOptions(): Returns an object with properties reflecting the locale and formatting options computed during initialization

The prototype inherits properties from Intl.RelativeTimeFormat.prototype, including:

- constructor: The constructor function that created the instance object

- [Symbol.toStringTag]: The initial value of the Symbol.toStringTag property (set to "Intl.RelativeTimeFormat")

The object supports the following units:

- year

- quarter

- month

- week

- day

- hour

- minute

- second


### Custom Formatting with formatToParts

The formatToParts method returns an array of objects representing the relative time format in parts. These objects have a "type" property indicating whether the part is a literal string, an integer, or a unit, and a "value" property containing the corresponding value.


### Performance Optimization

The implementation handles input validation, locale resolution, and formatting options computation during initialization. The format function processes the value and unit according to the locale and formatting options, while formatToParts provides detailed control over the output structure.


### Supported Locales and Browser Compatibility

Supported locales can be checked using the static method supportedLocalesOf(). The implementation maintains compatibility across browsers through polyfills that preserve API functionality. As of September 2020, support extends across major browsers with variations in import methods, locale loading, and ECMAScript conformance testing.


## RelativeTimeFormat Methods

The `format()` method of `Intl.RelativeTimeFormat` creates a string representing the given value and unit according to the locale and formatting options. The method accepts two parameters:

- `value`: A numeric value to use in the internationalized relative time message

- `unit`: The unit to use in the relative time internationalized message, with possible values including "year", "quarter", "month", "week", "day", "hour", "minute", and "second" (plural forms are also supported)

The return value is a string formatted according to the specified locale and options. Some specific examples of formatted output based on the documentation include:

- `rtf.format(-1, "day")` returns "yesterday"

- `rtf.format(2.15, "day")` returns "in 2.15 days"

- `rtf.format(100, "day")` returns "in 100 days"

- `rtf.format(0, "day")` returns "today"

- `rtf.format(-0, "day")` returns "today"

The `formatToParts()` method returns an array of objects representing the formatted number's constituent parts, allowing for custom locale-aware formatting. Each object in the array has two properties: `type` (indicating whether the part is a literal string, an integer, or a unit), and `value` containing the corresponding value. Unit information is included for parts that come from time formatting.

The resolved options method provides detailed information about the object's locale and formatting options after initialization. This can be useful for debugging or validating the settings of the RelativeTimeFormat instance.


## RelativeTimeFormat Browser Support

The implementation status for RelativeTimeFormat is at Stage 4, indicating readiness for formal ECMAScript standard inclusion. As of September 2020, native implementation is available in V8 v7.1.179 (Chrome 71) and Firefox 65, with other major browsers implementing the API.

The constructor creates a relative time formatter for specified locales with default values. It supports three style options: "long", "short", or "narrow". The numeric option can be set to "always" or "auto" to control output formatting. When numeric is "always", formats use "1 day ago" or "in 1 day". When numeric is "auto":

- "yesterday" for -1

- "tomorrow" for 1

- "now" for 0 seconds

- "today" for 0 days

- "this minute" for 0 minutes

The formatter supports the following units: day, second, minute, hour, month, year. The output format depends on the unit and value:

- For 0 seconds: localized "now"

- For 0 days: localized "today"

- For 0 minutes: "this minute"

- For -1: "yesterday"

- For 1: "tomorrow"

- For other values: "1 day ago" or "in 1 day" depending on numeric setting

The API specification supports units including year (31536000000 ms), month (2628000000 ms), day (86400000 ms), hour (3600000 ms), minute (60000 ms), and second (1000 ms).

The constructor accepts locales and options as parameters. The RangeError exception is thrown if locales or options contain invalid values. The static method `Intl.RelativeTimeFormat.supportedLocalesOf()` returns an array containing those of the provided locales that are supported without falling back to the runtime's default locale.


## Best Practices for Relative Time Formatting


### Best Practices for Implementation and Usage

Implementing RelativeTimeFormat effectively requires careful consideration of locale selection and formatting options. To ensure optimal performance and user experience:

- Validate input locale strings using `Intl.RelativeTimeFormat.supportedLocalesOf()` to avoid runtime errors and provide fallback options when necessary

- Use the most specific style option available ('long' for detailed formats, 'short' for simplified displays, and 'narrow' for minimalistic interfaces) to balance clarity and space usage

- Configure the numeric option ('always' for consistent syntax or 'auto' for concise representations where possible) to match your application's requirements

- Leverage `formatToParts()` for custom formatting scenarios, breaking down the output to selectively apply styling or further processing

- Implement fallback mechanisms for unsupported locales by providing default messages or falling back to browser defaults


### Styling and Display Considerations

When displaying RelativeTimeFormat outputs:

- Allow for dynamic styling of literal strings, integers, and units to accommodate different display requirements

- Support localization of time units (e.g., using locale-aware calendars for month and day names)

- Provide options for adjusting formatting according to context (e.g., 1 second ago vs. 1 second before)

- Implement accessibility features by ensuring sufficient contrast and clear reading order in rendered text


### Performance Optimization

To maintain efficient performance:

- Minimize unnecessary formatting calls by caching results where appropriate

- Use precise unit values rather than generic time periods when possible

- Opt for simpler formats ('short' or 'narrow') when processing large volumes of data

- Monitor and optimize formatting operations in high-performance environments

