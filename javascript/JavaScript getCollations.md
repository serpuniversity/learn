---

title: JavaScript Locale > getCollations

date: 2025-05-26

---


# JavaScript Locale > getCollations

JavaScript's built-in locale system represents a significant advancement in web development, enabling developers to create applications that adapt seamlessly to global audiences. From managing complex plural forms in languages like Arabic to handling intricate sorting rules for German and Chinese characters, this system addresses the diverse needs of international users. This article explores the core components of JavaScript localization, focusing on the `getCollations` method and its implementation across major browsers. Through detailed examples and technical specifications, we'll uncover how developers can harness this powerful feature to create truly localized applications.


## JavaScript Locale Overview

The JavaScript locale system manages three key aspects: collations, plural rules, and segmenters. Collations handle string sorting and searching, with options for different sorting methods - such as German's phonebook and dictionary orders - and only compare string equality. Segmenters enable text segmentation at grapheme level, allowing precise text manipulation and measurement.

Locale detection occurs through the browser's `navigator.language` and `navigator.languages` properties. The built-in support across browsers shows minor variations: Chrome 130.0.6723.59 lists 7547 locales, Firefox 131.0.3 adds 5 unique ones (abq, dgl, kzh, oui, rna), while Safari 18.0.1 offers 7548 with 1 unique locale (ber). The `Intl.Locale` object facilitates this process with its `maximize` method and region property, generating all possible language codes.

The system provides robust plural handling through `Intl.PluralRules`, supporting multiple forms in languages like Arabic (zero, one, two, few, many, other). The `Intl.NumberFormat` object manages number formatting across locales, ensuring correct display based on user preferences. Together, these features enable comprehensive JavaScript localization, though developers must account for browser variations and fully qualified locale usage.


## getCollations Method

The `getCollations()` method returns an array of collation types commonly used for a given locale, sorted alphabetically. The returned array contains strings representing these collation types, excluding the standard and search values.

For example, calling `getCollations()` with `new Intl.Locale("zh")` returns the collation types ["pinyin", "stroke", "zhuyin", "emoji", "eor"]. Each entry in the array represents a distinct sorting method for Chinese characters.

The collation type is determined at the time the `Intl.Locale` object is constructed. You can specify a collation type through the `co` key of the locale identifier or by passing a configuration object to the `Intl.Locale()` constructor. However, once set, you cannot directly modify the collation type using the `collation` property, which only allows read access to the constructed value.


## Locale Implementation Across Browsers

As of October 21, 2024, browser implementation of JavaScript localization shows minor differences in supported locales:

- Chrome 130.0.6723.59 supports 7547 locales with no unique additions.

- Firefox 131.0.3 adds 5 unique locales (abq, dgl, kzh, oui, rna), bringing its total to 7550.

- Safari 18.0.1 supports 7548 locales, adding 1 unique locale (ber).

The language identifier formats used by browsers conform to Unicode standards, using ISO 639-1 and ISO 639-2 codes where applicable. For unsupported locales, developers should refer to the Unicode Language Identifier Best Practices (<https://www.unicode.org/reports/tr35/tr35.html#BCP_47_Conformance>). Locales are typically derived from the browser's `navigator.language` and `navigator.languages` properties, which provide a dynamic view of the user's preferred languages. When implementing language switching functionality, developers should consider using i18next's `i18next-browser-languageDetector` plugin to handle language selection based on browser settings.


## Collation Variations and Sorting

Collation processing in JavaScript follows specific rules based on the locale settings. For German, small differences exist between sorting options: "ä" sorts before "z" in Swedish but after in German. By default, "ä" sorts within lowercase characters, as demonstrated by the comparison methods returned -1 and 1 respectively.

The `Intl.Collator` constructor handles these variations through Unicode locale extensions. While the method was implemented as an accessor called `collations` in older browser versions, it later changed to a method to prevent false equality (`locale1.collations === locale2.collations` returning false instead of true).

Collation modes include "upper" (uppercase sorts before lowercase), "lower" (default), and "off" (with specific differences). Key comparison options are numeric ordering (false by default), alternate comparison (with non-ignorable whitespace and punctuation options), and backwards sorting (default false).

For locale implementation, supported operations include collection creation methods, aggregation, and distinct queries. String comparison with collation requires exact match between string and index collation, with only contiguous non-negative integer substrings of digits considered. This system treats up to 254 character sequences as single numbers, with Unicode code points in the Number or Decimal Digit category.


## Plural Rules and Locale Settings

The JavaScript localization system handles plural forms through the `Intl.PluralRules` object, which determines the correct form of words based on number. For example, English has two plural forms ("one" and "other"), while Arabic requires six forms ("zero", "one", "two", "few", "many", "other"). The system applies these rules to message keys ending with "-plural", requiring a `count` integer to select the appropriate form.

Plural handling uses specific conventions for different libraries. Polyglot handles plurals with four-pipe syntax `||||`, requiring developers to explicitly load translations for each locale. The `loadAndTranslate` function demonstrates this approach, setting the locale and replacing translations as needed. Modern frameworks like React, Angular, and Vue.js support localization, though specific implementation details vary between libraries.

The language subtag is crucial for accurate formatting, requiring developers to specify both region and script in locale definitions. While most scripts use a single numbering system, exceptions exist for languages like Serbian (using both Latin and Cyrillic scripts) and Chinese (using both Simplified and Traditional script variants). The Intl.DateTimeFormat and Intl.NumberFormat methods demonstrate that while both can create Hebrew calendar formatters, Intl.NumberFormat requires additional options to change behavior when using "en-US".

The system supports comprehensive date and number formatting across multiple locales. The ArcGIS Maps SDK for JavaScript, for example, offers translation support for 42 different languages, including Arabic, Bosnian, Bulgarian, and Chinese (Taiwan). The SDK also handles right-to-left support through the `dir` attribute, allowing developers to specify "rtl" for Arabic and other RTL languages. For formatting, the system uses the ICU plural syntax, where a `count` variable determines the chosen form, with the `#` symbol replaced during rendering.

