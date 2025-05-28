---

title: JavaScript Reference & Tutorial: Instant > toLocaleString

date: 2025-05-27

---


# JavaScript Reference & Tutorial: Instant > toLocaleString

JavaScript's `toLocaleString()` method revolutionizes string formatting by integrating locale-specific cultural preferences directly into your code. This comprehensive guide explores how `toLocaleString()` handles dates, numbers, and arrays across diverse languages and regions, from Arabic dates to Indian number formats. You'll learn how to customize outputs with options for notation styles, unit displays, and cultural variations, while understanding its implementation details and performance considerations for efficient internationalization.


## Method Overview

The `.toLocaleString()` method in JavaScript formats values as strings according to the specified locale, covering dates, numbers, and more. This method is part of the ECMAScript 2026 Language Specification and ECMAScript 2026 Internationalization API Specification.

For date objects, the method formats dates based on the host's locale and cultural settings, providing language-sensitive date strings. It supports various options for customization, including formatting styles, time zones, and unit displays. For example, arrays of numbers can be formatted with specific locale settings: `const nums = [1200, 3000, 4500]; console.log(nums.toLocaleString("de-DE", { style: "unit", unit: "liter", unitDisplay: "narrow" }));`.

The method also handles number formatting for various locales and options. It supports multiple locale fallbacks and detailed formatting controls through the `options` parameter. For instance, it can format numbers with specific currency styles and codes: `console.log(number.toLocaleString("de-DE", { style: "currency", currency: "EUR" }));`. It allows customization of significant digits and fractional parts: `console.log(number.toLocaleString("en-IN", { maximumSignificantDigits: 3 }));`.

The implementation uses a large database of localization strings and can be inefficient when called frequently with the same arguments. In such cases, creating an `Intl.NumberFormat` object and using its `format()` method can improve performance by caching database slices. The method supports a wide range of locales, including but not limited to "en-IN" (Indian English), "en-US" (US English), "ar-EG" (Arabic, Egypt), and various currency formats for different regions.


## Date Object Formatting

The `.toLocaleString()` method converts a `Date` object to a string representation based on locale settings. This locale-sensitive formatting considers cultural preferences for date and time presentation.

The method accepts two optional parameters: `locales`, which specifies the language and region for formatting, and `options`, which customizes the output format. `locales` can be a single language tag string or an array of tags, with additional subtags for region, variant, and script. The primary language subtag is required, while others provide context for formatting preferences.

For option customization, properties include `dateStyle` and `timeStyle`, each with options for "full," "long," "medium," and "short" formats. Additional properties allow setting specific components of the output, such as `weekday`, `year`, `month`, `day`, `hour`, `minute`, and `second`. The `timeZoneName` property controls the display of time zone information.

A practical example creates a date object and formats it using British English locale with a 24-hour clock: `const date = new Date(Date.UTC(2020, 9, 26, 7, 0, 0)); console.log(date.toLocaleString("en-GB", { timeZone: "UTC" }));` This outputs: "26/10/2020, 12:30:00".

The method supports a wide array of language specificiations, including:

- Arabic: ar-EG (Egyptian)

- Bangla: bn-BD (Bangladesh)

- Czech: cs-CZ

- Danish: da-DK

- German: de-AT (Austrian), de-CH (Swiss), de-DE (German)

- Greek: el-GR

- Spanish: es-AR (Argentine), es-ES (Spanish)

- Finnish: fi-FI

- French: fr-BE (Belgian), fr-CA (Canadian), fr-CH (Swiss), fr-FR (French)

- Hebrew: he-IL (Israel)

- Hindi: hi-IN

- Hungarian: hu-HU

- Indonesian: id-ID

- Italian: it-CH (Swiss), it-IT (Italian)

- Japanese: ja-JP

- Korean: ko-KR

- Dutch: nl-BE (Belgian), nl-NL (Dutch)

- Norwegian: no-NO

- Polish: pl-PL

- Portuguese: pt-BR (Brazilian), pt-PT (Portuguese)

- Romanian: ro-RO

- Russian: ru-RU

- Slovak: sk-SK

- Swedish: sv-SE

- Tamil: ta-IN (India)

- Thai: th-TH

- Turkish: tr-TR

- Chinese: zh-CN (China), zh-HK (Hong Kong), zh-TW (Taiwan)

- Iranian: fa-IR

- Sri Lankan Tamil: ta-LK

- Iranian Farsi: fa-IR

- South African: en-ZA (English)

- Irish: en-IE (English)

The method also supports regional variations within languages, allowing for detailed localization of date and time representation across different cultures and dialects.


## Number Object Formatting

The `toLocaleString()` method formats numbers according to locale settings, supporting multiple options for customization. The method accepts an `options` object and optionally a `locales` string to control the output format. The `options` object provides several properties for customization:

- `minimumFractionDigits`: Controls the minimum number of digits after the decimal point, with a valid range of 0 to 20. The default value is 3.

- `maximumFractionDigits`: Controls the maximum number of digits after the decimal point, with a valid range of 0 to 20. The default value is 3.

- `maximumSignificantDigits`: Controls the number of significant digits in scientific notation, with a valid range of 1 to 21. The default value is 21.

- `notation`: Controls the notation style with values "standard", "scientific", "engineering", or "compact". The default value is "standard".

- `style`: Specifies the number style with values "decimal", "currency", or "percent".

The method supports currency formatting through the `style` property set to "currency" and the `currency` property specifying the ISO 4217 currency code. For example:

```javascript

console.log((-15000).toLocaleString("en-US", { style: "currency", currency: "USD", currencySign: true }));

```

This outputs: "$-15,000.00".

The method returns consistent formatting most of the time, but output may vary between implementations within the same locale. It may use non-breaking spaces or bidirectional control characters in some cases. To check for support for locales and options parameters, you can use the following function:

```javascript

function toLocaleStringSupportsLocales() {

  return (typeof Intl === "object" && !!Intl && typeof Intl.NumberFormat === "function");

}

```

The method supports specifying multiple locales using an array, with fallback languages. For example:

```javascript

console.log(number.toLocaleString(["ban", "id"])); // 123.456,789

```

This allows for localization of number formatting across different languages and regions. The method uses the host's default language for number formatting when options are specified, providing flexibility for implementation-specific formatting behaviors.


## Array and Typed Array Support

The `toLocaleString()` method formats arrays and typed arrays according to the specified locale, combining elements with locale-specific separators. For array elements, the method delegates the formatting to each element's own `toLocaleString` method, using the provided locale and options parameters.

When formatting arrays, the method handles `undefined` elements by converting them to an empty string instead of `"null"` or `"undefined"`. It also treats sparse arrays correctly, interpreting empty slots as having the value `undefined`. The implementation uses a generic separator string that depends on the host's current locale, not the explicitly provided `locales` parameter.

The method supports multiple locales through an array parameter, with fallback languages handled according to the host's implementation. For example, passing `["ban", "id"]` would format the array using the Indonesian-Balinese language. The implementation has been available across browsers since July 2015 and works with both array and array-like object structures.

A practical example formats an array of numbers with German locale settings and unit notation: `const nums = [1200, 3000, 4500]; console.log(nums.toLocaleString("de-DE", { style: "unit", unit: "liter", unitDisplay: "narrow" }));`. This outputs the localized string: "1.200 l, 3.000 l, 4.500 l".

For efficient repeated formatting operations, the implementation suggests creating an `Intl.NumberFormat` object and using its `format()` method instead of direct `toLocaleString` calls. This approach can improve performance by caching database slices for the specific formatting requirements.


## Locale and Options Parameters

The method accepts two optional parameters: `locales` and `options`. The `locales` argument can be a language tag (string) or an array of language tags, with the primary language subtag being required. Additional subtags can include region, variant, and script tags.

The `options` argument is an object for customizing the behavior of the method. Its properties depend on the data type being formatted. For number formatting, options include:

- `minimumFractionDigits`: Controls the minimum number of digits after the decimal point, with a valid range of 0 to 20. The default value is 3.

- `maximumFractionDigits`: Controls the maximum number of digits after the decimal point, with a valid range of 0 to 20. The default value is 3.

- `maximumSignificantDigits`: Controls the number of significant digits in scientific notation, with a valid range of 1 to 21. The default value is 21.

- `notation`: Controls the notation style with values "standard", "scientific", "engineering", or "compact". The default value is "standard".

- `style`: Specifies the number style with values "decimal", "currency", or "percent".

The implementation uses the environment's default locale for formatting if parameters are not provided. For array and typed array support, the method formats elements based on their own `toLocaleString` methods, using the provided locale and options parameters.

For example, the following code formats a number with German locale settings and unit notation:

```javascript

console.log(number.toLocaleString("de-DE", { style: "unit", unit: "liter", unitDisplay: "narrow" }));

```

For efficient repeated formatting operations, the implementation suggests creating an `Intl.NumberFormat` object and using its `format()` method instead of direct `toLocaleString` calls. This approach can improve performance by caching database slices for the specific formatting requirements.

