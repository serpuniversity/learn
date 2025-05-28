---

title: Supported Locales in JavaScript Internationalization

date: 2025-05-27

---


# Supported Locales in JavaScript Internationalization

JavaScript's Internationalization API offers powerful tools for handling multilingual applications, but developers need to know which locales are truly supported. The Intl.*.supportedLocalesOf() methods provide this vital information, allowing developers to determine which language tags will work reliably in various contexts. This guide explores these essential methods for list formatting, display names, number formatting, and collation, showing how they filter supported locales to prevent runtime errors and ensure accurate internationalization in modern JavaScript applications.


## Intl.ListFormat Supported Locales

The Intl.ListFormat.supportedLocalesOf() method returns an array of strings representing the subset of given locale tags that are supported in list formatting. It accepts two parameters: locales (a string with BCP 47 language tag or an array of such strings) and options (an optional object with localeMatcher property, which has values "lookup" and "best fit"). The method returns an array of supported locales.

Browser compatibility begins with Chrome 72 and above, Edge 79 and above, Firefox 78 and above, Opera 60 and above, and Safari 14.1 and above. The method has been available since April 2021 with full compatibility across modern browsers.

When called with the locales ['ban', 'id-u-co-pinyin', 'de-ID'], the method returns ['id-u-co-pinyin', 'de-ID'] because Indonesian is considered an adequate match for Balinese, and most Balinese speakers also understand Indonesian. The method follows the ECMAScript Internationalization API (ECMA-402) specification and uses the "lookup" algorithm by default, which may decide that Indonesian is an adequate match for Balinese while excluding the Balinese language tag due to lack of support.


## Intl.DisplayNames Supported Locales

Intl.DisplayNames's supportedLocalesOf() method returns an array of locale tags that are supported in display names without falling back to the runtime's default locale. It follows the same parameters and algorithmic behavior as other Intl.*.supportedLocalesOf() methods, using the localeMatcher option to determine supported locales between "lookup" and "best fit".

The method demonstrated in the documentation returns "id-u-co-pinyin" and "de-ID" for a runtime environment that supports Indonesian and German but not Balinese in display name formats. This behavior demonstrates how specific locale requirements can be filtered from broader language tag support, even when related language variations are understood or used within the same region.

Browser compatibility began with Chrome 72 and above, Edge 79 and above, Firefox 78 and above, Opera 60 and above, and Safari 14.1 and above, released in April 2021 with full compatibility across modern browsers. This matches the timeline for the method's implementation across other Intl.*.supportedLocalesOf() features, indicating consistent development and release patterns for JavaScript internationalization APIs.


## Intl.NumberFormat Supported Locales

The Intl.NumberFormat.supportedLocalesOf() method returns an array of locale tags that are supported in number formatting, without falling back to the runtime's default locale. It accepts two parameters: locales (a string with a BCP 47 language tag or an array of such strings) and options (optional, with a localeMatcher property that defaults to "best fit").

The method returns an array of strings representing a subset of the given locale tags. These tags are those for which the runtime supports a locale in number formatting that the locale matching algorithm considers a match. The algorithm can be specified using the localeMatcher option, with possible values of "lookup" and "best fit."

For example, if a runtime supports Indonesian and German but not Balinese in number formatting, the method will return the Indonesian and German language tags unchanged, as demonstrated in the documentation examples. This specific behavior ensures that language tags irrelevant to number formatting, such as "ban" (Balinese), "de-ID" (German for Indonesia), and "id-u-co-pinyin" (Indonesian with Pinyin collation), are correctly filtered.

Browser compatibility began with Chrome 24 and above, Edge 12 and above, Firefox 29 and above, Opera 15 and above, and Safari 10 and above, with full support across modern browsers since the method's initial implementation in September 2017. The method is part of the ECMAScript Internationalization API (ECMA-402) specification, with well-established support across devices and browser versions.


## Intl.Collator Supported Locales

The Intl.Collator.supportedLocalesOf() method returns an array containing locale tags that are supported in collation without falling back to the runtime's default locale. It takes two parameters: locales (a string with a BCP 47 language tag or an array of such strings), and options (optional, an object with a localeMatcher property that defaults to "best fit" and can be set to "lookup").

The method returns an array of strings representing a subset of the provided locale tags that are supported in collation without fallback. When called with the locales ['ban', 'id-u-co-pinyin', 'de-ID'], the method returns ['id-u-co-pinyin', 'de-ID'], demonstrating how Indonesian and German language tags are returned unchanged, while Balinese is excluded due to lack of support. This behavior is consistent with the method's design to filter out language tags that are irrelevant to collation, such as Indonesian's pinyin collation, which is not used in this context.

The method's implementation follows ECMAScript Internationalization API (ECMA-402) specifications and has been supported across browsers since September 2017. The method's parameters and behavior mirror those of other Intl.*.supportedLocalesOf() features, indicating consistent development and release patterns for JavaScript internationalization APIs. Compatibility spans modern browsers and versions, similar to support for number formatting and date/time formatting methods within the same API framework.


## Browser Support and Compatibility

Browser support for the Intl.*.supportedLocalesOf() methods varies depending on the specific feature and browser implementation:

- **Chrome and Edge**: Both browsers fully support the methods since version 72. Edge version 79 and above specifically support the methods as of the April 2021 release. The methods are available without fallback to the runtime's default locale.

- **Firefox**: Version 78 and above includes full support for the methods. As with other browsers, they operate without fallback to the default locale.

- **Opera**: Version 60 and above supports the methods, matching the release timeline established across modern browsers. Like other implementations, the methods avoid locale fallbacks.

- **Safari**: Release version 14.1 and above fully implements the methods. The implementation follows the same pattern of locale-specific matching without runtime fallbacks.

Compatibility data indicates that prior to Node.js version 13.0.0, only basic English ('en-US') locale data was available by default. For earlier Node.js versions requiring comprehensive ICU data support, users must build Node.js with the '--with-intl' option and provide necessary data files.

The methods use sophisticated locale matching algorithms:

- The default "best fit" matcher determines adequate language tag matches, such as considering Indonesian an acceptable match for Balinese due to shared linguistic understanding.

- The "lookup" algorithm provides a more precise match based on available data, as demonstrated in the Indonesian vs. Balinese example.

All methods consistently follow ECMAScript Internationalization API (ECMA-402) specifications and demonstrate robust support across major browsers and devices since their respective release dates. The compatibility implementation patterns align across number formatting, date/time formatting, list formatting, and other related Intl.* methods, ensuring a cohesive internationalization API framework for JavaScript applications.

