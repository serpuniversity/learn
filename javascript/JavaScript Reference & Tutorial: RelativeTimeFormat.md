---

title: Using JavaScript's Intl.RelativeTimeFormat for Human-readable Time Display

date: 2025-05-26

---


# Using JavaScript's Intl.RelativeTimeFormat for Human-readable Time Display

JavaScript's Intl.RelativeTimeFormat introduces language-sensitive relative time formatting, allowing developers to display time differences in human-readable formats. This article explores the API's capabilities, including its unit selection process, browser support, and implementation best practices, while demonstrating how to create effective relative time displays in various application contexts.


## Relative Time Format Basics

The Intl.RelativeTimeFormat() constructor creates language-sensitive relative time formatters for JavaScript applications. It requires two parameters: the locale (here set to 'en') and the numeric format option (defaulting to 'auto' to display "yesterday" or "tomorrow" for negative values).

The constructor supports various browsers including Chrome, Edge, Firefox, Opera, and Safari, with implementation in V8 version 7.1.179 (Chrome 71) and shipping in Firefox 65. Polyfills are available from the FormatJS project for broader compatibility.

The constructor returns an Intl.RelativeTimeFormat object with properties including `constructor`, `[Symbol.toStringTag]`, and instance methods for formatting and resolving options. The resolvedOptions() method returns an object reflecting the locale and formatting options computed during initialization.

The format() method formats a given value and unit according to the specified locale and options. For example, `new Intl.RelativeTimeFormat("en", { numeric: "always" }).format(-2, "year")` outputs "2 yr. ago", while `new Intl.RelativeTimeFormat("es-ES", { numeric: "auto" }).format(1, "day")` outputs "mañana".

The formatToParts() method returns an array of objects representing the formatted relative time string in parts. For instance, `new Intl.RelativeTimeFormat("en", { numeric: "auto" }).formatToParts(-1, "day")` produces an array containing the part representing "yesterday".

The object supports units for years, quarters, months, weeks, days, hours, minutes, and seconds, with automatic unit selection based on time deltas. This automatic selection works across different units, providing concise representations like "1 day ago" or "in 10 minutes" while maintaining flexibility for more complex time expressions.


## Cutoff Values and Time Unit Selection

The time unit selection process leverages an array of cutoff values to determine the most appropriate unit of measurement based on the difference between two dates. For differences of up to 60 seconds, the unit is seconds; between 60 and 3600 seconds, it's minutes; between 3600 and 86400 seconds (1 day), it's hours; between 86400 and 86400 * 7 seconds (1 week), it's days; between 86400 * 7 and 86400 * 30 seconds (1 month), it's weeks; between 86400 * 30 and 86400 * 365 seconds (1 year), it's months; and for differences greater than 86400 * 365 seconds, it's years.

For example, if the difference between two dates is exactly 2 hours and 22 minutes, the format() method would first calculate the time difference in seconds (8220 seconds). Using this value, it would then determine that the appropriate unit is hours, converting 8220 seconds to 2.25 hours and formatting it as "in 2 hours".

The API automatically handles various edge cases, such as rounding and sign direction. For instance, a difference of -100 seconds would be formatted as "100 seconds ago", while a difference of 86401 seconds would be formatted as "1 day". The implementation includes detailed logic to manage these scenarios, using Math.floor() and Math.sign() functions to ensure accurate representation across all possible time deltas.


## Locales and Language Support

The `Intl.RelativeTimeFormat.supportedLocalesOf()` static method returns an array of locale tags that are supported in relative time formatting without falling back to the runtime's default locale. This array reflects which locales can be used with the `Intl.RelativeTimeFormat` constructor. The method provides flexibility through its optional `options` parameter, including the ability to specify the `localeMatcher` property, which determines the matching algorithm to use for locale resolution.

The constructor itself leverages robust locale data resolution, likely incorporating caching mechanisms to improve performance. The implementation draws upon established standards including the ICU Relative Date Time Formatter and Unicode CLDR Calendar Fields, ensuring compatibility with existing internationalization frameworks.

The API supports a wide array of languages through its implementation across multiple browsers and devices. As of the latest specifications, the constructor requires locale data resolution and caching, indicating a sophisticated approach to handling localization. The method's design closely mirrors those of `Intl.NumberFormat` and `Intl.DateTimeFormat`, sharing a similar form for creating an `Intl.RelativeTimeFormat` instance.

The supported locales span a diverse range of language tags, from major world languages like English and Spanish to regional variants and less commonly used languages. This comprehensive support demonstrates the API's capabilities across various linguistic contexts, though specific implementation details may vary between different browser versions and device platforms.


## Formatting Examples and Best Practices

To illustrate practical implementation, let's examine a detailed usage example. Consider a scenario where you're developing a social media platform that needs to display how long ago a post was created. You could create a utility function that encapsulates the relative time formatting logic:

```javascript

function formatRelativeTime(date) {

  const now = new Date().getTime();

  const difference = (now - date.getTime()) / 1000; // Convert to seconds

  const rtf = new Intl.RelativeTimeFormat(navigator.language, { numeric: 'auto' });

  const cutoffs = [60, 3600, 86400, 86400 * 7, 86400 * 30, 86400 * 365, Infinity];

  const unitIndex = cutoffs.findIndex(cutoff => difference >= cutoff);

  const unit = unitIndex === -1 ? 'second' : unitIndex === 0 ? 'second' : `s ${

    Intl.RelativeTimeFormat/unitIndex}`;

  return rtf.format(-difference, unit);

}

const postDate = new Date(); // Simulate a post date

console.log(formatRelativeTime(postDate)); // Output: "posted just now"

```

This function correctly handles different time deltas by checking against the cutoff array and applying the appropriate time unit. It demonstrates handling both past and future dates, as well as edge cases like exact minutes or hours.

In another context, consider implementing relative time formatting for event scheduling in a calendar application. You might use a similar approach, but adjust the cutoff logic to prioritize shorter units for immediately upcoming events:

```javascript

function formatUpcomingEvent(date) {

  const difference = (date.getTime() - new Date().getTime()) / 1000;

  const rtf = new Intl.RelativeTimeFormat(navigator.language, { numeric: 'always' });

  const cutoffs = [60, 3600, 86400 * 7, 86400 * 365, Infinity];

  const unitIndex = cutoffs.findIndex(cutoff => difference >= cutoff);

  return rtf.format(difference, `day ${unitIndex === -1 ? 'minute' : ''}`);

}

```

This implementation uses a specific cutoff array optimized for upcoming events, providing more granularity for near-term dates while maintaining simple representations for longer-term events. The approach handles both positive and negative differences, making it suitable for scheduling and reminder applications.


## Browser Support and Polyfills

The Intl.RelativeTimeFormat API is widely implemented across modern browsers, with support reaching back to September 2020. As of the latest specifications, the constructor requires locale data resolution and caching, indicating a sophisticated approach to handling localization. The implementation closely mirrors those of Intl.NumberFormat and Intl.DateTimeFormat, sharing a similar form for creating an Intl.RelativeTimeFormat instance.

The constructor creates a new Intl.RelativeTimeFormat object with properties including `constructor` and `[Symbol.toStringTag]`. The `resolvedOptions()` method returns an object reflecting the locale and formatting options computed during initialization. The `format(value, unit)` method formats a given value and unit according to the specified locale and options, while the `formatToParts(value, unit)` method returns an array of objects representing the formatted relative time string in parts.

The constructor supports multiple units including years, quarters, months, weeks, days, hours, minutes, and seconds, with automatic unit selection based on time deltas. For example, a difference of 86401 seconds would be formatted as "1 day", while -100 seconds would be formatted as "100 seconds ago". The implementation includes detailed logic to handle these scenarios using Math.floor() and Math.sign() functions for accurate representation across all possible time deltas.

Browser compatibility stands at Stage 4 implementation, with support in V8 version 7.1.179 (Chrome 71) and shipping in Firefox 65. The API's performance is enhanced through caching mechanisms, as demonstrated by the constructor's reliance on cached locale data. The proposal draws from established standards including the ICU Relative Date Time Formatter and Unicode CLDR Calendar Fields, maintaining compatibility with existing internationalization frameworks.

For broader compatibility, polyfills are available with support from three JavaScript libraries. The format.js polyfill implementation passes the official ECMAScript conformance test, while two other libraries also meet this standard. These polyfills provide robust browser compatibility, with core bundle sizes ranging from 2.7 to 3.2 kilobytes (gzipped). Implementation details may vary between different browser versions and device platforms, particularly for less commonly used language tags.

