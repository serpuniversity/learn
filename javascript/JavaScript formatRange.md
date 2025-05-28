---

title: JavaScript Intl.DateTimeFormat: formatRange and formatRangeToParts

date: 2025-05-26

---


# JavaScript Intl.DateTimeFormat: formatRange and formatRangeToParts

In today's globalized digital landscape, accurate and culture-sensitive date formatting is crucial for effective communication across time zones and languages. The JavaScript Intl.DateTimeFormat API provides powerful tools for localizing date and time display, including the formatRange method introduced in August 2021. This feature enables developers to generate human-readable date ranges that align with regional formatting preferences, from "January 10 – 20, 2007" for same-month intervals to "January 10, 2007 – February 20, 2007" when months change.

The implementation of formatRange requires developers to understand how different date components are processed, including the proper handling of Date objects, Temporal.PlainDateTime objects, and time zones. The method's behavior is influenced by locale-specific patterns defined in the Unicode CLDR TR-35 specification, making it essential to grasp the underlying mechanics for consistent results across various implementation environments.

This article explores the technical details of formatRange, from its browser support requirements to the formatting options available for controlling date and time representation. It also examines how developers can extend cross-browser compatibility through polyfills like FormatJS and demonstrates how to work with the method's output using formatRangeToParts for custom date range string construction.


## Browser Support

The formatRange() method has received full support across modern browsers since August 2021, with specific requirements for each browser version as follows:

- Google Chrome 76 and above

- Firefox 91 and above

- Opera 63 and above

- Edge 79 and above

- Safari 14.1 and above

For broader compatibility, developers can use polyfills like FormatJS to enable formatRange() support in older browsers and environments. This ensures consistent date range formatting capabilities across different devices and platforms.

The method accepts two parameters: startDate and endDate, which can be Date objects or Temporal.PlainDateTime objects. The endDate must have the same type as startDate. If a Temporal.ZonedDateTime object is provided, it will throw a TypeError, requiring developers to use Temporal.ZonedDateTime.prototype.toLocaleString() or convert it to a supported type.


## Basic Usage

The formatRange() method applies locale-specific patterns to display date ranges in a manner consistent with the user's regional settings. For example, it might represent a range of dates as "January 10 – 20, 2007" when the largest difference between dates is within the same month, versus "January 10, 2007 – February 20, 2007" when the month changes between dates.

The method requires careful handling of various date components:

- It processes both Date objects and Temporal.PlainDateTime objects for startDate and endDate parameters.

- While it supports different time zone displays through configuration options, it explicitly rejects Temporal.ZonedDateTime objects, requiring conversions to compatible types before use.

When called with valid parameters, formatRange() returns a string representing the most concise date range as determined by the locale's formatting rules. This aligns with the underlying ICU Date Interval Formatter and Unicode CLDR TR-35 specifications for date intervals.


## Formatting Options

The Intl.DateTimeFormat methods allow for precise control over date and time representation across multiple dimensions. Locale-specific formatting options enable customization of language-sensitive components, while technical parameters address regional variations in date calculation and display.

The constructor's options object determines internal slot values, including [[TimeZone]], [[Day]], [[Month]], and [[Year]] properties. These settings define default display styles for time zones, weekdays, months, and years, with fallback mechanisms in place for missing locale variants.

Key customization areas include time zone display, with multiple formats available: "long" for full time zone names, "short" for commonly recognized abbreviations, and "shortOffset" for simple UTC offsets. The calendar system also features customization options, supporting Gregorian, Chinese, Persian, and other Unicode calendar types.

For date components, developers can specify display styles through parameters like "numeric", "2-digit", and "long". The hour cycle and hour12 format options further refine time representation, with support for 11-hour and 23-hour cycles in addition to the standard 24-hour format. Fractional second digits allow precision up to three decimal places, with rounding handled according to Unicode standards.


## Polyfills and Implementation

For broader compatibility, developers can use polyfills like FormatJS to enable formatRange() support in older browsers and environments. This ensures consistent date range formatting capabilities across different devices and platforms.

The formatRange() method always throws a TypeError when provided with a Temporal.ZonedDateTime object for either the startDate or endDate parameters. To use these types, developers must either convert the object to a supported type using Temporal.ZonedDateTime.prototype.toLocaleString() or use the formatRangeToParts() method for more detailed control over the formatting process.

The formatRangeToParts() method returns an array of objects representing each part of the formatted date range string. Each object contains three properties: type, value, and source. The string concatenation of value in the order provided will result in the same string as returned by formatRange(). The type can have the same values as formatToParts(), and the source can be one of three values: startRange, endRange, or shared.

The shared token indicates that the token is used in both the start and end dates. If the start and end dates are equivalent at the output precision, the output has the same list of tokens as calling formatToParts() on the start date, with all tokens marked as source: "shared". This allows developers to build custom date range strings from locale-specific tokens while maintaining the correct order and formatting.

