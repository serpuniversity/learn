---

title: JavaScript Date and Time Formatting with toLocaleString

date: 2025-05-27

---


# JavaScript Date and Time Formatting with toLocaleString

JavaScript's date and time formatting capabilities have evolved significantly over the years, with the introduction of the `toLocaleString` method providing language-sensitive formatting options for numbers, dates, and times. This method, which works with both standalone values and Temporal objects, allows developers to generate string representations that adhere to specific locale conventions while offering extensive customization through its parameters.

The `toLocaleString` method represents a crucial aspect of JavaScript's internationalization toolkit, bridging the gap between raw date/time data and human-readable formats. By supporting multiple locale options and detailed formatting controls, it enables developers to create applications that deliver a more engaging and culturally relevant user experience across different regions and languages.

This article examines the capabilities and implementation details of JavaScript's `toLocaleString` method, focusing on its behavior with both general numeric values and Temporal objects. Through analysis of the method's parameters and output options, we'll explore how developers can effectively leverage this feature to provide language-sensitive date and time formatting in their JavaScript applications.


## toLocaleString Method Overview

JavaScript's `toLocaleString` method provides language-sensitive formatting for various data types including dates, numbers, and times. It works by converting a number, date, or time value into a string representation that is appropriate for the specified locale.

The method accepts two optional parameters: `locales` and `options`. The `locales` argument can be a language tag or an array of language tags, with the primary language subtag being required. Additional subtags can include region, variant, and script tags. The method uses the first supported locale in an array of locales, arranged from highest to lowest priority.

For example, the method can format numbers using the specified locale and options. Using the default English locale, it formats 30,000.65 as "30,000.65" in English, "30.000,65" in German, and "30 000,65" in French.

When formatting dates and times, the method can include various components such as weekday, year, month, and day, and can use 12 or 24-hour time formats. For instance, it can display a date as "Thursday, December 20, 2012" or "12/19/2012, 19:00:00" based on the specified options.

The `options` parameter allows extensive customization of the output format. It includes properties for controlling fraction digits (`minimumFractionDigits`, `maximumFractionDigits`), style formatting (`style` property with values "currency", "decimal" or "percent"), and whether to use grouping separators (`useGrouping`). Additionally, it supports currency formatting by requiring a `style` property set to "currency" along with a specified ISO 4217 currency code.

The method also provides flexibility for time formatting through the `Temporal.PlainTime` prototype implementation. It allows customization of output through options such as `timeStyle` to return only the hour and minute, or controlling the hour component format with options like "2-digit" to display "12 PM" instead of "12:00 PM".


## PlainTime.prototype.toLocaleString

The toLocaleString method for Temporal.PlainTime instances produces a language-sensitive string representation of the time value, closely following the behavior of the Intl.DateTimeFormat API when supported. Each call to toLocaleString requires a search through localization string databases, which can be inefficient for multiple calls with identical arguments. In these cases, it is more efficient to create an Intl.DateTimeFormat object and use its format method, which can cache localization strings within a more constrained context.

The method accepts two parameters: locales (a string or array of BCP 47 language tags) and options (an object adjusting the output format). Similar to Intl.DateTimeFormat, the locales parameter determines the language formatting conventions to use, while the options parameter allows detailed control over the output format.

When no options are provided, the default formatting style is "numeric" for hour, minute, and second. The options parameter supports the timeStyle property, which can be set to "short" to return only the hour and minute components. Additionally, the hour option controls the formatting of the hour component, with "2-digit" returning "12 PM" instead of "12:00 PM". The method follows these formatting rules:

- If only timeStyle is provided, it expands to include dayPeriod, hour, minute, second, and fractionalSecondDigits formats.

- Only specified time components are included in the output.

The method generates strings equivalent to new Intl.DateTimeFormat(locales, options).format(time), with the option for normalized formatting properties as described in the specification. Implementation details allow for variation in output between different implementations while maintaining consistency within the same locale. Users should avoid comparing results to hardcoded constants due to these implementation considerations.


## Formatting Options

The method accepts two arguments: locales and options. The locales argument can be a language tag or an array of language tags, with the primary language subtag being required. Additional subtags can include region, variant, and script tags. The method uses the first supported locale in an array of locales, arranged from highest to lowest priority.

The options parameter allows customization of the output format. For numbers, this includes properties for controlling fraction digits (minimumFractionDigits, maximumFractionDigits), style formatting (style property with values "currency", "decimal" or "percent"), and whether to use grouping separators (useGrouping).

For time values, additional options control the precision and rounding of the output:

- fractionalSecondDigits: Controls the number of fractional digits in the output (default 'auto')

- smallestUnit: Specifies the smallest unit of time to include in the output (default 'auto')

- roundingMode: Determines how to handle remainders (default 'trunc')

The output format follows the specifications for RFC 9557, ISO 8601, and RFC 3339. Implementations may vary within the same locale, adhering to specific design considerations rather than producing consistent results across implementations.


## Locale Support and Performance

The implementation of toLocaleString is optimized for repeated calls with the same arguments through caching mechanisms. When called multiple times with identical parameters, it is more efficient to create an Intl.DateTimeFormat object and use its format method. This approach allows caching of localization strings within a more restricted scope, improving performance for subsequent calls with the same arguments.

The method supports several key options for customizing the output format. These include control over date and time components such as weekday, year, month, and day. For time-related options, it allows customization through properties like timeStyle, which can return only the hour and minute components. Additionally, it supports hour format options including "2-digit" to display "12 PM" instead of "12:00 PM".

The method consistently follows the specifications for RFC 9557, ISO 8601, and RFC 3339, with implementation details allowing for variations in output between different implementations while maintaining consistency within the same locale. Users should avoid comparing results to hardcoded constants due to these implementation considerations.


## Browser Compatibility and Implementation

The toLocaleString method has reached Stage 3 of the TC39 process and is not yet ready for production use. Current implementation details show that it provides a unified date formatting API similar to Intl.DateTimeFormat, maintaining familiarity while simplifying the API. It offers explicit time zone handling through ZonedDateTime with time zone specifications, avoiding ambiguity about UTC, local, or other time zones.

The method supports the ECMAScript 2026 Language Specification and the ECMAScript 2026 Internationalization API Specification. While native browser support is not yet available, several JavaScript libraries can serve as recommended alternatives until Temporal reaches Stage 4 and has widespread browser support:

1. Day.js: Lightweight, good browser support, TypeScript support, extensible with plugins, large community, active development

2. date-fns: Functional programming approach, tree-shakeable, good TypeScript support

3. Luxon: Similar features to Temporal, immutable by default, native time zone and Intl support

Browser compatibility information indicates that the method is supported in all modern browsers, with the ECMAScript3 (JavaScript 1999) feature available in all browsers. The (locales, options) syntax is supported across modern browsers, offering flexibility in language-sensitive formatting through the use of BCP 47 language tags and options objects for customizing output format.

