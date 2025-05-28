---

title: JavaScript PluralRules supportedLocalesOf

date: 2025-05-27

---


# JavaScript PluralRules supportedLocalesOf

The Intl.PluralRules.supportedLocalesOf() method in JavaScript determines which requested locales have complete plural rule support, helping developers optimize localization without defaulting to the runtime's fallback locale. This article explores the method's implementation details, supported algorithms, and browser compatibility, demonstrating how it enables precise control over pluralization in multi-locale applications.


## supportedLocalesOf Method Overview

The Intl.PluralRules.supportedLocalesOf() method returns an array containing those of the provided locales that are supported without having to fall back to the runtime's default locale (MDN Web Docs). This method supports both 'best fit' and 'lookup' algorithms for determining supported locales, allowing developers to customize the matching behavior through an options object.

When called, the method processes its parameters, which include a locales array and an optional options object with a localeMatcher property (MDN Web Docs). The locales parameter should contain BCP 47 language tags that represent the desired locales for plural rule support. The options parameter, if provided, can include a localeMatcher property with values "lookup" or "best fit" (defaulting to "best fit").

The method's implementation involves several internal steps. First, it canonicalizes the input locales to ensure compatibility. Next, it coerces the options parameter into an object format. The method then creates an options record, setting the localeMatcher property based on the provided value or the default "best fit" setting. It also initializes other properties such as the type (cardinal or ordinal) and digit formatting options.

When called with specific parameters, such as locales = ["ban", "id-u-co-pinyin", "de-ID"] and options = { localeMatcher: "lookup" }, the method returns an array like ["id-u-co-pinyin", "de-ID"]. This output demonstrates how certain locales, like Indonesian with pinyin collation, may still be supported while others are excluded based on the runtime environment's capabilities.


## Method Syntax and Parameters

The method takes two parameters: locales (a string with a BCP 47 language tag or an array of such strings) and options (optional, with a localeMatcher property that defaults to "best fit" and can be set to "lookup"). When called with specific parameters, such as locales = ["ban", "id-u-co-pinyin", "de-ID"] and options = { localeMatcher: "lookup" }, the method returns an array like ["id-u-co-pinyin", "de-ID"].

The locales parameter should contain BCP 47 language tags that represent the desired locales for plural rule support. The options parameter, if provided, can include a localeMatcher property with values "lookup" or "best fit" (defaulting to "best fit").

The method's implementation processes its parameters through several internal steps. It first canonicalizes the input locales to ensure compatibility and coerces the options parameter into an object format. It then creates an options record, setting the localeMatcher property based on the provided value or the default "best fit" setting. The method initializes other properties such as type (cardinal or ordinal) and digit formatting options.

The returned array contains locale tags that are supported for plural rules without falling back to the runtime's default locale. For example, when called with locales = ["ban", "id-u-co-pinyin", "de-ID"] and options = { localeMatcher: "lookup" }, the method returns an array like ["id-u-co-pinyin", "de-ID"], demonstrating how certain locales, like Indonesian with pinyin collation, may still be supported while others are excluded based on the runtime environment's capabilities.


## Locale Matching Algorithms

The supportedLocalesOf method employs two primary algorithms for determining supported locales: 'best fit' and 'lookup'. The algorithm can be specified through the options object's localeMatcher property, with "best fit" serving as the default.


### LocaleMatcher Algorithm Selection

When the localeMatcher property is absent or set to "best fit", the method applies a multi-step process to determine supported locales (MDN Web Docs). This approach evaluates the compatibility of requested locales against available runtime capabilities, selecting the most compatible match when exact matches are not found.

The second algorithm, "lookup", performs a direct check against the available locales without the additional compatibility evaluation (MDN Web Docs). This approach returns only those locales for which the runtime explicitly supports plural rules, providing a stricter match against the requested locales.


### Implementation and Browser Compatibility

The functionality is widely available across modern browsers and device environments, having been implemented since September 2019 (MDN Web Docs). The method leverages internal slots and options records to manage locale-sensitive formatting rules, ensuring compatibility across different runtime configurations.

Browser compatibility extends to multiple versions across major desktop and mobile platforms, including Chrome 24+, Edge 12+, Firefox 29+, Internet Explorer 11+, Opera 15+, Safari 10+, Android WebView 4.4+, and Chrome Android 25+. Server-side compatibility is supported in Node.js 13.0.0+ with proper ICU data configuration (MDN Web Docs).

These algorithms enable developers to determine which locales are supported for plural rules without falling back to the runtime's default locale, providing fine-grained control over localization capabilities.


## Example Usage

The supportedLocalesOf method returns an array containing locale tags that are supported for plural rules without falling back to the runtime's default locale. For example, when called with the locales ['ban', 'id-u-co-pinyin', 'de-ID'] and options { localeMatcher: 'lookup' }, the method returns ['id-u-co-pinyin', 'de-ID'].

The method requires ICU (locale) data to function properly. Before version 13.0.0, only the locale data for 'en-US' was available by default. To enable full ICU data for earlier versions, developers can use the '--with-intl' option when building Node.js and provide the necessary data. The method is available across multiple versions of modern browsers and device environments, including Chrome 24+, Edge 12+, Firefox 29+, Internet Explorer 11+, Opera 15+, Safari 10+, Android WebView 4.4+, Chrome Android 25+, and Node.js 13.0.0+.


## Implementation Details

The implementation of supportedLocalesOf leverages internal slots and options records to manage locale-sensitive formatting rules. When the method is called with specified locales and options, it first canonicalizes the input locales to ensure compatibility. The options parameter is then coerced into an object format, and an options record is created with properties initialized based on the provided values or default settings.

The method processes localeMatcher as either "best fit" (default) or "lookup" based on the options parameter. For "best fit" matching, the method evaluates the compatibility of requested locales against available runtime capabilities, selecting the most compatible match when exact matches are not found. In contrast, "lookup" performs a direct check against the available locales without additional compatibility evaluation, returning only those explicitly supported for plural rules.

The method's implementation structure ensures that locale-sensitive formatting rules are initialized and resolved correctly across different runtime configurations. This compatibility layer allows the method to function consistently across multiple versions of modern browsers, device environments, and Node.js releases.

