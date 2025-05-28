---

title: PluralRules in JavaScript

date: 2025-05-26

---


# PluralRules in JavaScript

Pluralization, the process of determining the correct form of a word based on quantity, is a fundamental aspect of natural language that presents significant challenges for software development. While English and some other languages have straightforward rules for singular and plural forms, many languages, including Arabic and Chinese, require complex classification systems with multiple categories. The JavaScript Intl API addresses this linguistic complexity through the PluralRules class, providing developers with a powerful toolset for locale-aware pluralization across modern browsers and devices. This article explores the capabilities of the PluralRules class, comparing its functionality to third-party libraries and providing examples of its implementation across different languages and use cases.


## Overview of PluralRules

The PluralRules class enables locale-aware pluralization in JavaScript through its constructor and static methods. The constructor can accept a single locale string or an array of locale strings, with an optional options parameter for additional configuration.

The static method supportedLocalesOf returns an array of supported locales without falling back to the runtime's default locale. This method accepts either a single locale string or an array of locale strings, with an optional options parameter to specify the locale matcher algorithm.

The select method determines the appropriate plural form based on a given number, while selectRange works with value ranges to return the correct pluralization category. These methods provide comprehensive support for both cardinal and ordinal number pluralization across multiple languages.

Differences in implementation between languages demonstrate the complexity of pluralization rules. For example, while English has five forms for cardinal numbers (zero, one, two, few, many), Arabic has distinct categories for zero, one, two, and larger numbers.

Third-party libraries like Pluralize and Numerous offer advanced capabilities for managing pluralization across multiple locales. The Numerous library requires additional locale files to be loaded before use, while Pluralize provides a simpler implementation for English-based applications.

These tools help developers effectively handle string pluralization, reducing the overhead associated with managing multiple language versions manually. The underlying Intl API provides consistent support across modern browsers and devices, with robust performance compared to alternative libraries.


## PluralRules Constructor and Static Methods

The PluralRules constructor accepts either a single locale string or an array of locale strings, with an optional options parameter that can include localeMatcher and type properties. The constructor requires locales, which can be BCP 47 language tags or Intl.Locale instances.

The static supportedLocalesOf method returns an array of supported locales without falling back to the runtime's default locale. It accepts either a single locale string or an array of locale strings, with an optional options parameter for localeMatcher.

For example, Intl.PluralRules.supportedLocalesOf(["ban", "id-u-co-pinyin", "de-ID"], { localeMatcher: "lookup" }) returns ["id-u-co-pinyin", "de-ID"], demonstrating the method's ability to handle specific locale matching algorithms.

The constructor's localeMatcher property supports two values: "lookup" and "best fit" (default). This option affects how the engine resolves matching locales when multiple options are available. The type property can be set to either "cardinal" (default) or "ordinal" based on the desired pluralization type, with additional support for Intl.NumberFormat digit options.


## Pluralization Methods

The selectRange method accepts two parameters: startRange and endRange, both of which are numbers. It returns a string indicating the plural rule to use for the specified range, following the LDML Language Plural Rules format. According to MDN Web Docs, the available plural categories are "zero", "one", "two", "few", "many", or "other". For instance, calling selectRange(102, 201) with a Slovenian rules object returns "few", while a Portuguese rules object results in "other" when given 102 as both start and end range values (MDN Web Docs).

The select method returns a string based on the specified locale and options, indicating the plural rule for a given number. English requires singular and plural forms only ("other" for zero or any other number), while Chinese and Arabic have more complex requirements - Arabic specifically has six forms (ICU 77.1 documentation). The method's behavior varies by language, with Arabic having five forms for cardinal numbers (zero, one, two, few, many) and different rules for ordinal numbers (e.g., 0 → "cathod", 1 → "gath", 2 → "gath", few → "cath", many → "chath", other → "cath") (Intl.PluralRules documentation).

The select method works with both cardinal and ordinal numbers. For English cardinal numbers, it returns "other" for 0, 2, and other non-one values, while 1 receives "one" (Intl.PluralRules documentation). The selectRange method returns "one" for the singular case and "other" for all other cardinal numbers (Intl.PluralRules documentation).

The select function's behavior depends on the language's specific requirements. English has a straightforward two-form system - singular and general plural - while Chinese and Arabic have more complex rulesets with multiple forms defined for different number ranges (ICU 77.1 documentation). The returned plural form can dictate different sentence structures - "1 dog is happy; do you want to play with it?" versus "10 dogs are happy; do you want to play with them?" - demonstrating the importance of correct pluralization in language-specific contexts (Intl.PluralRules documentation and MDN Web Docs).


## Locale-Specific Plural Rules

English follows a two-form system for cardinal numbers - singular ("1 hour, 1 dog, 1 fish") and general ("other" for zero or any other number). The select method returns "other" for 0, 2, and other non-one values, while 1 receives the "one" category (MDN Web Docs). For ordinal numbers, it has four forms: "th" for numbers above 20, "st" for one, "nd" for two, and "rd" for three. The select function categorizes 0 as "other" (0th), 1 as "one" (1st), 2 as "two" (2nd), and 3 as "few" (3rd).

Arabic requires six forms: "zero", "one", "two", "few", "many", and "other". The framework returns the appropriate category based on the number: 0 receives "zero", 1 gets "one", 2 falls into "two", 6 categorizes as "few", and 18 results in "many" (Intl.PluralRules documentation). For ordinal numbers, Arabic has distinct categories for 0 ("cathod"), 1 ("gath"), 2 ("gath"), few ("cath"), many ("chath"), and other ("cath").

The framework supports multiple locales through its constructor, allowing developers to specify language and fallback languages (MDN Web Docs). The selectRange method works with cardinal numbers, returning "one" for singular cases and "other" for all other cardinal numbers, with 18 specifically falling into the "other" category (Intl.PluralRules documentation). The resolvedOptions method returns an object containing initialization options, including locale, collation options, and significant digit settings, which affect the selection process (Intl.PluralRules documentation).


## Pluralization Libraries

The available third-party libraries for JavaScript pluralization offer various levels of functionality beyond the built-in Intl API. Key options include:

_Pluralize_

This library provides basic pluralization capabilities primarily for English applications. It requires minimal setup and works with the following simple function signature:

```javascript

const pluralize = (count, noun, suffix = 's') => `${count} ${noun}${count !== 1 ? suffix : ''}`;

```

For more complex applications requiring support for multiple locales, the Numerous library offers comprehensive pluralization capabilities across 67 languages. However, it requires downloading and importing multiple locale files into the project directory.

_Project Implementation_

The library has been successfully integrated into projects through several approaches:

- Simple English functionality: Directly using the provided `pluralize` function

- Multiple locale support: Downloading and importing numerous.js, along with locale-specific files (en.js, ru.js, etc.)

- Basic localization: Creating a "numerous_pluralization.js" file to register and manage locales programmatically

