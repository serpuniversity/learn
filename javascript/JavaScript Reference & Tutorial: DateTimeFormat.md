---

title: JavaScript Date and Time: Using DateTimeFormat for Locale-Aware Date and Time Formatting

date: 2025-05-26

---


# JavaScript Date and Time: Using DateTimeFormat for Locale-Aware Date and Time Formatting

Using DateTimeFormat for Locale-Aware Date and Time Formatting in JavaScript


## DateTimeFormat Basics

DateTimeFormat provides three methods for formatting dates: format(date), formatRange(start, end), and formatToParts(date). The format method returns a string representing the formatted date based on the locale and options specified. The formatRange method formats a date range in the most concise way based on locale and options, returning an object with start and end formatted strings. The formatToParts method returns an array of objects representing date string parts for custom formatting. The formatRangeToParts method returns an array of objects representing date range parts for custom formatting.

The constructor supports specifying multiple languages (e.g., ["ban", "id"]) and provides options for weekday, year, month, day, hour, minute, second, and timeZone properties. The resolvedOptions method returns an object with locale and formatting options computed during initialization. The format method can handle different localizations, customizable formats, and alternative calendars and time zones. The formatRange method returns the most concise date range representation based on locale and options specified during instantiation. The formatToParts and formatRangeToParts methods return objects representing date string parts for custom formatting.

The constructor also handles time zone information and can use browser's default locale with undefined locale string. Custom calendar and numbering system options can be set, with examples showing Chinese calendar and Arabic numbering system support. Time zone handling includes both short and full time zone names, with hour12 option for 12-hour time display. The API supports precise hour, minute, second formatting with fractional second digits configurable, including support for UTC and various time zones like Tokyo and Berlin.


## Creating DateTimeFormat Objects

The Intl.DateTimeFormat constructor creates a new Intl.DateTimeFormat object, enabling language-sensitive date and time formatting. Instances of this object provide the fundamental functionality for date and time manipulation, including formatting, range formatting, and detailed option customization.

To create a DateTimeFormat object, you can use the constructor with either a single locale string or an array of language tags. For example, `new Intl.DateTimeFormat('en-US')` creates a formatter for US English, while `new Intl.DateTimeFormat(['en-US', 'en-GB'])` creates one supporting both US and UK English.

The constructor accepts an optional second parameter for formatting options, which can include properties for weekday, year, month, day, hour, minute, second, and timeZone. For instance, you can create a formatter with specific options like this: `new Intl.DateTimeFormat('en', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })`.

DateTimeFormat objects can be configured to support multiple calendar systems and numbering formats. For example:

- Chinese calendar: `new Intl.DateTimeFormat('zh-cn-u-ca-chinese')`

- Arabic numbering system: `new Intl.DateTimeFormat('ar', { numberingSystem: 'arab' })`

When creating a DateTimeFormat instance, you can also specify time zone information. This might include short or full time zone names, or the browser's default time zone if no specific time zone is provided. An example configuration might look like this: `new Intl.DateTimeFormat('en-US', { timeZone: 'America/Los_Angeles' })`.

The constructor enables precise control over date and time formatting, including support for 12-hour vs. 24-hour time display with the hour12 option and customization of time zone name display with full and short formats. For advanced formatting needs, developers can combine multiple options to create highly customized date and time representations.


## DateTimeFormat Properties and Methods

The `Intl.DateTimeFormat` object provides several key properties and methods for date and time formatting. The `constructor` property returns the function that created the `Intl.DateTimeFormat` instance, while `[Symbol.toStringTag]` returns "Intl.DateTimeFormat" and is used in `Object.prototype.toString()`.

The core formatting methods are accessed through the prototype object. The `format()` method returns a string representing the date formatted according to the locale and options of the instance. When called with a `Date` object, it produces a string formatted according to the specified patterns. For example, `Intl.DateTimeFormat('en-GB').format(new Date())` returns "22/08/2023".

The `formatRange()` method returns an object with formatted start and end dates, producing the most concise representation based on locale and options. It accepts two `Date` objects and formats the range based on the specified styles. For instance, `Intl.DateTimeFormat('en-GB', { year: 'numeric', month: 'short', day: 'numeric' }).formatRange(new Date(2023, 7, 1), new Date(2023, 7, 10))` returns { start: "1/08/2023", end: "10/08/2023" }.

The `resolvedOptions()` method returns an object containing the locale and formatting options computed during initialization. This allows developers to examine the effective configuration of the `Intl.DateTimeFormat` instance.

Additional features include precise control over date and time formatting. Options can specify exact hour, minute, second formatting, with fractional second digits configurable. The API supports both short and full time zone names, with support for browser's default locale when no specific time zone is provided. Custom calendar and numbering system options are also supported, demonstrating flexibility across different cultural and temporal contexts.


## Date and Time Formatting Options

The DateTimeFormat object offers extensive precision control over date and time formatting through its options. Users can specify exact hour, minute, second formatting, including fractional second digits up to 3 decimal places. Time zone handling supports both short and full time zone names, allowing developers to display timezone information according to user preference.

For example, developers can generate precise time strings like "2:00:00 pm AEDT" or configure fractions of a second with "2:00:00.200 pm AEDT". The API also handles default value representations for different date-time components, with year, month, day defaulting to "numeric" when formatting plain date objects.

The constructor's options include week, year, month, day, hour, minute, second specifications, complementing the standard date components. Hour formatting supports 12-hour vs. 24-hour display via the hour12 option. Additional flexibility comes from customizable day period formatting with "short" style options.

To demonstrate, creating a formatter with these options: `new Intl.DateTimeFormat('en-GB', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })` produces detailed date strings matching specific user preferences. This functionality extends to various calendar types and numbering systems through the constructor's calendar and numberingSystem properties.


## DateTimeFormat Usage and Examples

The `format()` method outputs localized, opaque strings, while `formatToParts()` produces the same information in discrete parts. This allows for programmatic manipulation of individual date components.

For example, the `dayPeriod` type can be formatted differently using a switch statement and template literals. This flexibility enables developers to create highly customized date strings that match specific user preferences.

Some calendars, like Chinese and Tibetan, use a 60-year sexagenary cycle for naming years. This requires disambiguation with the Gregorian calendar year, which the `relatedYear` type handles automatically.

The text also notes that while most formatting is consistent across devices and browser versions, output may vary in some cases. This flexibility allows the API to accommodate different language requirements while maintaining a degree of consistency.

The `DateTimeFormat` object can output different parts of the date-time value based on the specified formats. For example, it can produce strings like "2:00:00 pm AEDT" with precise hour, minute, second formatting, including fractional second digits up to 3 decimal places.

For time zone handling, the API supports both short and full time zone names. It can use the browser's default locale with an undefined locale string, providing a convenient way to display time zone information without explicit configuration.

The `Intl.DateTimeFormat` constructor can be called with or without `new`, returning a new instance in both cases. This behavior allows for compatibility with existing APIs while enabling developers to work with the hidden instance's options. Methods like `formatRange()` and `formatToParts()` fail with a `TypeError` when called directly on the returned object, ensuring proper method chaining and instance handling.

