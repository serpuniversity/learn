---

title: JavaScript DateTimeFormat: supportedLocalesOf

date: 2025-05-26

---


# JavaScript DateTimeFormat: supportedLocalesOf

The Intl.DateTimeFormat API introduces powerful localization capabilities for date and time formatting in JavaScript. However, determining which locales are truly supported can be challenging. The supportedLocalesOf method addresses this gap, allowing developers to programmatically test which language and regional settings are fully supported for date and time operations. By examining locale-specific features like calendar types and numbering systems, this method enables more robust internationalization support across modern JavaScript applications.


## supportedLocalesOf Method Overview

The supportedLocalesOf method returns an array of locale identifiers that the JavaScript implementation supports for DateTimeFormat formatting. This allows developers to determine which locales are available for date and time formatting without relying on the runtime's default locale.

The method accepts two parameters: locales (a string with a BCP 47 language tag or an array of such strings) and options (an optional object with a localeMatcher property). The locales parameter specifies the language and locale for date and time formatting, while the options parameter allows customization using various Unicode extension keys for numbering systems (nu), calendars (ca), and hour cycles (hc).

Example usage of the method demonstrates its functionality with an array of locale tags: ["ban", "id-u-co-pinyin", "de-ID"]. When the localeMatcher option is set to "lookup," the method returns an array containing the supported locale tags: ["id-u-co-pinyin", "de-ID"].

The method supports multiple locales and formatting options, including calendar types like buddhist, chinese, coptic, ethiopic, and gregory, as well as numbering systems such as arab, arabext, beng, deva, fullwide, gujr, guru, hanidec, khmr, knda, laoo, latn, limb, mlym, mong, mymr, orya, tamldec, telu, thai, and tibt.

Browser compatibility for the supportedLocalesOf method is robust, with wide availability across devices and browser versions dating back to September 2017. Modern support can be found in Chrome 24, Firefox 29, Internet Explorer 11, Opera 15, and Safari (WebKit), while Android and Safari Mobile support has been added in versions 26 and later, respectively.


## Method Parameters

The locales parameter accepts a string with a BCP 47 language tag or an array of such strings. The language tag follows the format language[-script][-region], where language is mandatory, script is optional, and region is optional but typically included for calendar-specific differences (e.g., "en-US" for US English).

The options parameter is optional and can contain a localeMatcher property with values "lookup" or "best fit". The default value is "best fit," which attempts to select the most appropriate locale based on available options. The lookup value explicitly checks for exact matches among the supported locales.

The method allows specifying multiple locale tags, as demonstrated in the example: ["ban", "id-u-co-pinyin", "de-ID"]. When using the lookup matcher with this input, the method returns ["id-u-co-pinyin", "de-ID"], indicating these locales are fully supported for relative time formatting and date/time operations.

This flexibility enables developers to test multiple locale combinations, including specific script variants (like "id-u-co-pinyin" for Indonesian with Chinese collation) and region-specific configurations (such as "de-ID" for German in Indonesia). The method's behavior demonstrates robust support across a range of language and script combinations, leveraging both the runtime's default capabilities and explicit locale matching algorithms.


## Return Value

The method returns an array of strings representing the subset of the provided locale tags that are supported in date and time formatting without falling back to the runtime's default locale. This output indicates which locales are fully supported for relative time formatting and date/time operations.

For example, when testing with locales ["ban", "id-u-co-pinyin", "de-ID"], setting localeMatcher to "lookup" results in ["id-u-co-pinyin", "de-ID"]. This demonstrates that while "ban" (Balinese) is not supported for relative time formatting, both "id-u-co-pinyin" (Indonesian with Pinyin collation) and "de-ID" (German for Indonesia) are fully supported.

The method's behavior reflects its design to enable developers to test multiple locale combinations, including:

- Specific script variants (like "id-u-co-pinyin" for Indonesian with Pinyin collation)

- Region-specific configurations (such as "de-ID" for German in Indonesia)

The exact output may vary between JavaScript engines, potentially containing non-breaking spaces or bidirectional control characters. Developers should test all user-configurable locales across multiple JavaScript engines to ensure consistent results.


## Example Usage

const exampleLocales = ["ban", "id-u-co-pinyin", "de-ID"];

const exampleOptions = { localeMatcher: "lookup" };

console.log(Intl.DateTimeFormat.supportedLocalesOf(exampleLocales, exampleOptions)); // Expected output: Array ["id-u-co-pinyin", "de-ID"]

```

This example demonstrates the supportedLocalesOf method with an array of locale tags and a locale matcher setting. The output indicates which of the specified locales are fully supported for date and time formatting.

The method also works with single locale tags:

```

const singleLocale = "es-MX";

const supported = Intl.DateTimeFormat.supportedLocalesOf([singleLocale]);

console.log(supported); // Output: ["es-MX"]

```

For fallback behavior, developers can specify multiple locales in an array:

```

const fallbackLocales = ["el-GR", "de-DE", "en-US"];

const supportedFallback = Intl.DateTimeFormat.supportedLocalesOf(fallbackLocales);

console.log(supportedFallback); // Output: ["el-GR", "de-DE"]

```

The method correctly handles locale combinations, including specific script variants and region-specific configurations:

```

const complexLocales = ["fr-CH", "de-at-u-ca-ical", "ja-u-ca-japanese"];

const supportedComplex = Intl.DateTimeFormat.supportedLocalesOf(complexLocales);

console.log(supportedComplex); // Output: ["fr-CH", "ja-u-ca-japanese"]

```

This comprehensive testing approach ensures developers can effectively configure their applications using multiple locales while leveraging the browser's supported capabilities.


## Browser Support

The supportedLocalesOf method has established browser compatibility since September 2017 across multiple devices and browser versions. The method works consistently from Chrome 24 and above, Edge 12 and above, Firefox 29 and above, and Safari 10 and above.

The method's functionality spans various JavaScript engines, including Chrome for Android 26, Firefox Mobile, Internet Explorer 11, Opera, and Safari Mobile (WebKit). However, some specific configurations may not be supported across all implementations.

For instance, the method works with both single locale tags and arrays of locale tags, returning supported locale tags in an array format. This flexibility enables developers to test multiple locale combinations while leveraging the browser's supported capabilities.

Developers should note that results may vary between JavaScript engines and may contain non-breaking spaces or bidirectional control characters. To ensure consistent results, developers should perform comprehensive testing across multiple engines and mock user preferences when necessary.

