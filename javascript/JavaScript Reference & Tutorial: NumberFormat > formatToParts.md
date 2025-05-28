---

title: JavaScript Number Format: formatToParts

date: 2025-05-26

---


# JavaScript Number Format: formatToParts

The JavaScript Number format API offers powerful tools for handling numerical data across diverse locales and formatting requirements. One of its most versatile features is the formatToParts method, which decomposes numbers into their constituent parts while preserving locale-specific formatting details. This capability enables developers to customize number presentations in ways that maintain accuracy and cultural relevance. From displaying currency values to rendering scientific notation, formatToParts delivers granular control over how numerical data appears in applications worldwide.


## formatToParts Method Overview

The formatToParts method returns a list of FormatPart objects containing locale-specific tokens that can be used to build custom strings while preserving locale-specific parts. This enables developers to access individual components of the formatted number, such as currency symbols, grouping separators, and decimal points, which can be manipulated or displayed in custom ways.

Each object in the returned array represents a component of the formatted number, with possible types including 'integer', 'group', 'decimal', 'fraction', and 'currency'. Together, these parts form the complete, locale-aware representation of the number, allowing for precise control over how it is displayed.

The method supports multiple formatting options through its parameters:

- `style`: Specifies the type of formatting (e.g., "currency", "unit")

- `currency`: Specifies the currency code for currency formatting

- `maximumSignificantDigits`: Limits the number of significant digits in the formatted number

- `unit`: Specifies the unit type for unit formatting

- `unitDisplay`: Specifies the display format for units (e.g., "long", "short")

This flexibility enables the handling of special cases across various languages and number systems, including Arabic, Indian numbering conventions, and non-standard languages with fallback support. The method returns its results in an array of objects, providing developers with complete control over the presentation of formatted numbers while maintaining compatibility with different localization requirements.


## Method Parameters and Return Type

The method requires a single parameter: value, which is a Number, BigInt, or string representing the number to be formatted. The return type is an array of objects, each containing two properties: type and value. These objects provide detailed information about each component of the formatted number string.

The type property indicates the type of the number part, which can be one of several categories:

- Literal: Represents any string that's part of the format pattern

- Integer: The integral part of the number, or a segment of it when using grouping

- Group: The group separator string, such as "," when using grouping

- Decimal: The decimal separator string, such as "." when a fraction is present

- Fraction: The fractional part of the number

- Compact: The compact exponent, such as "M" or "thousands" when using compact notation

- ExponentSeparator: The exponent separator, such as "E" when using scientific or engineering notation

- ExponentMinusSign: The exponent minus sign string, such as "-" when using scientific notation

This detailed breakdown enables developers to manipulate individual parts of the formatted number string while maintaining locale-specific formatting. The method supports various number formats and styles through its options parameter, allowing for flexible customization of number presentation. For example, developers can specify currency styles, unit types, or display options like "long" or "short" for units. This comprehensive approach ensures that numbers are represented in a format that's both accurate and meaningful to the target audience.


## Formatting Number Parts

The formatToParts method processes the number according to the specified locale and formatting options, breaking it down into discrete parts that can be manipulated independently. Each part includes a type property indicating its role in the formatted number and a value property containing the specific string representation.

The method supports a wide range of number types, including integers, decimal fractions, currency symbols, and grouping separators. It also handles special cases such as scientific notation, compact representation, and unit-based formatting, providing detailed control over the presentation of numerical data.

The returned objects contain the following possible types:

- Literal: Represents any string that's part of the format pattern

- Integer: The integral part of the number, or a segment of it when using grouping

- Group: The group separator string, such as "," when using grouping

- Decimal: The decimal separator string, such as "." when a fraction is present

- Fraction: The fractional part of the number

- Compact: The compact exponent, such as "M" or "thousands" when using compact notation

- ExponentSeparator: The exponent separator, such as "E" when using scientific or engineering notation

- ExponentMinusSign: The exponent minus sign string, such as "-" when using scientific notation

This breakdown enables developers to customize the display of numbers while maintaining locale-specific formatting rules. For example, they can use the "currency" type to display currency symbols and values in bold, as shown in the following code snippet:

```javascript

const numberString = formatter

  .formatToParts(number)

  .map(({ type, value }) => {

    switch (type) {

      case "currency": return `<strong>${value}</strong>`;

      default: return value;

    }

  })

  .reduce((string, part) => string + part);

```

This functionality is particularly valuable for applications requiring precise control over number presentation, such as financial software, localization tools, or any system where numerical data needs to be displayed according to specific linguistic and cultural rules. The method's flexibility makes it suitable for a wide range of applications, from basic number formatting to complex localization scenarios.


## Locale-Specific Formatting

The method preserves locale-specific formatting options, such as grouping separators and decimal symbols, allowing for accurate localization. This functionality is ensured through the `Intl.NumberFormat` object, which supports multiple locales and handles special cases like Arabic, Indian numbering systems, and non-standard languages with fallback support.

The flexibility of locale support enables precise control over number presentation across different languages and cultural contexts. For example, when formatting numbers in Hindi (en-IN), the formatter correctly applies the Indian numbering system, where the group separator is "," rather than the Western "," or "." used in languages like French or English.

The method also handles complex cases such as scientific notation and compact representation. When using compact notation, it correctly formats numbers like 1,234,567,890 as "1.234M" in languages that use this convention, while ensuring that other languages display the number in standard format.


### Supported Locales and Runtime Requirements

The method requires specific runtime flags in older versions of Chrome and Node.js, with full support available in modern browsers and Node.js 10.0.0 and above. For detailed compatibility information, developers can use `Intl.NumberFormat.supportedLocalesOf(locales)` to query which locales are supported by NumberFormat from the given locale(s).

This comprehensive approach to locale handling ensures that developers can create highly localized number formatting solutions while maintaining compatibility across different language and cultural requirements.


## Browser and Node.js Support

The formatToParts method requires specific runtime flags for compatibility in older versions of Chrome and Node.js. For Chrome versions below 63, developers need to enable the `harmony-number-format-to-parts` runtime flag on the command line.

In modern browsers and Node.js 10.0.0 and above, the method is fully supported. The feature was added to Chrome in version 64 and Edge in version 12. However, as of April 9, 2019, Edge 18's update had not been pushed to all users through Windows Update, despite support being present in the version information (Edge 42.17134.1.0 EdgeHTML 17.134).

The method works across multiple devices and browser versions, with wide availability since September 2020. Desktop support includes Chrome, Edge, Firefox, Internet Explorer, Opera, Safari, Android webview, and Chrome Android. Node.js supports the feature in version 10.0.0 and above.

For developers working with older versions or specific environments, checking the availability of locale data for en-US is essential. The resolvedOptions method of NumberFormat returns NumberFormatOptions, which contains the formatting options used by the formatToParts method. This data ensures compatibility across different runtime environments while providing the flexibility needed for locale-aware number formatting.

