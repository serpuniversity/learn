---

title: JavaScript Date.prototype.toLocaleString() Method

date: 2025-05-26

---


# JavaScript Date.prototype.toLocaleString() Method

JavaScript's `.toLocaleString()` method transforms date objects into strings that reflect local date and time conventions. This introduction explores how this versatile function enables language-sensitive formatting, its syntax, customization options, and technical implementation across different environments. Mastering this method enhances web applications' accessibility and usability by presenting date and time information in culturally appropriate formats.


## Language-Sensitive Date Formatting in JavaScript

The `.toLocaleString()` method formats JavaScript date objects according to the specified locale, enabling the display of date and time information in a format that respects regional and cultural preferences. This functionality is particularly important for web developers working with diverse languages and their specific formatting requirements.

The method operates based on implementation-dependent locale settings, using either system locales or specified parameters to format date and time information. It accepts two optional parameters: `locales` and `options`.

The `locales` parameter can be a string with a BCP 47 language tag or an array of such strings. In implementations without `Intl.DateTimeFormat` support, this parameter is ignored, and the host's locale is typically used for formatting. The `options` parameter is an object that adjusts the output format, corresponding to the options parameter of the `Intl.DateTimeFormat()` constructor. If all weekday, year, month, day, dayPeriod, hour, minute, second, and fractionalSecondDigit properties are undefined, then year, month, day, hour, minute, second will be set to "numeric" in the absence of Intl.DateTimeFormat support.

The method returns a string representing the given date according to language-specific conventions, equivalent to `new Intl.DateTimeFormat(locales, options).format(date)` in implementations that support Intl.DateTimeFormat. This functionality allows applications to specify the language whose formatting conventions should be used, with default values based on the runtime environment when parameters are not provided.


## Syntax and Basic Usage

The `toLocaleString()` method provides a straightforward way to format date and time information based on the host environment's locale settings. When called without any parameters, it returns a string representing the current date and time formatted according to the system's default language and conventions.

The method accepts two optional parameters: `locales` and `options`. The `locales` parameter allows specifying one or more BCP 47 language tags to determine the formatting style. If not provided, the method uses the host environment's default locale. The `options` parameter enables customization of the date and time representation through an object that mirrors the constructor options of `Intl.DateTimeFormat`.

For example, calling `new Date().toLocaleString()` in a US English environment returns a string formatted as "12/20/2012 6:50:21 PM", while the same call in a French Moroccan environment produces "jeudi 12 décembre 2012 18:50:21". This demonstrates the method's ability to adapt date and time display based on the specified locale or environment settings.


## Customizing the Format

The method accepts an `options` parameter that defines detailed formatting options. This parameter allows customization of various aspects of the date and time representation, including:

- Date style: The method supports short, medium, long, and full styles for both date and time formatting. For example, the `dateStyle` property can be set to "long" to include the day, month, and year in the output.

- Time style: Similarly, the `timeStyle` property allows specifying the time format style, with options for short, medium, long, or full representations.

- Calendar type: The method supports formatting dates in specific calendars, including the Gregorian calendar (the default) and alternative calendar systems like the Ethiopian calendar.

- Time zone: The `timeZone` property enables specifying the time zone for the formatted date, allowing accurate representation of dates across different geographical regions.

- Hour format: The `hour12` property allows controlling whether the output uses a 12-hour or 24-hour clock format.

- Numbering system: The `numberingSystem` property enables specifying alternative numbering systems, such as Arabic or Bengali, for use in the formatted output.

The method also provides options for customizing the display of specific date components, including:

- Weekday format: The `weekday` property allows specifying how the day of the week should be represented, with options for long, short, or narrow formats.

- Year format: The `year` property controls how the year should be displayed, with options for numeric representation or including era information.

- Month format: The `month` property allows specifying the format for month representation, supporting long, short, or numeric formats.

- Day format: The `day` property controls the format for day-of-month representation, supporting numeric or numeric-with-leading-zero formats.

- Hour format: The `hour` property allows specifying the format for hour representation, with options for numeric or numeric-with-leading-zero formats.

- Minute and second formats: Similar to hour format, the `minute` and `second` properties control the representation of minutes and seconds, respectively.

For time zone display, the method includes properties for controlling the format of time zone information, such as `timeZoneName` for specifying the level of detail in time zone representation.

When formatting arrays of elements, the method supports using date and time formatting options for date objects while applying number formatting options to numeric elements. This functionality allows for flexible formatting of mixed arrays containing both date and numeric values.


## Handling Multiple Locales

The `toLocaleString()` method allows specifying multiple locale identifiers through its `locales` parameter, which can be a single string or an array of BCP 47 language tags. The method uses the first supported locale in an array, with locales arranged from highest to lowest priority.

When multiple locales are specified, the method provides flexibility for applications targeting diverse language and cultural audiences. This feature is especially useful in international applications where users may prefer different language conventions for date and time display.

The method supports optional parameters for customizing the formatting output, including options for date style, time style, calendar type, time zone display, and specific date component formats. These customization options enable precise control over the localization process, allowing developers to tailor date and time representations to specific regional preferences.


## Technical Implementation

The implementation of the `toLocaleString()` method varies between environments based on support for the Internationalization API. In implementations that include this API, the method delegates to the `Intl.DateTimeFormat` constructor, providing access to more comprehensive localization features. In environments without this support, the method uses the system's locale and formats date and time information based on the runtime environment's default settings.

When creating `toLocaleString` implementations, the method performs a database search each time it is called with the same arguments. This can be inefficient for repeated calls with identical parameters, particularly when formatting large numbers of dates. For improved performance, developers are advised to create an `Intl.DateTimeFormat` object and use its `format` method, which caches localization strings and searches within a more constrained context.

The method accepts two primary parameters: `locales` and `options`. The `locales` parameter specifies the language and region for formatting, using BCP 47 language tags. If not specified, the method defaults to the system's locale. The `options` parameter allows customization of the formatting through an object that mirrors the constructor options of `Intl.DateTimeFormat`.

For detailed control over date and time representation, the method includes properties for specifying the format of weekdays, years, months, days, hour periods, and time zones. These properties cover various aspects of date and time display, including:

- Calendar type: Support for specific calendar systems, such as the Gregorian calendar or alternative systems like the Ethiopian calendar.

- Time zone display: Control over the format and detail level of time zone information.

- Numbering systems: Options for alternative numbering systems, such as Arabic or Bengali, for use in the formatted output.

The method's behavior differs between environments based on Internationalization API support. In implementations with API support, the method uses the specified locales and options parameters to format date and time information. In environments without API support, the method prioritizes system locales and uses default formatting conventions based on the runtime environment.

