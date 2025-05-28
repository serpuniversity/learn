---

title: JavaScript Internationalization: supportedValuesOf

date: 2025-05-26

---


# JavaScript Internationalization: supportedValuesOf

Developing applications that support multiple languages and regions requires understanding the various date, time, and number formatting options available in different locales. JavaScript's Internationalization API provides developers with powerful tools to create locale-aware applications, including the Intl.supportedValuesOf method. This method allows developers to discover which calendar systems, collation settings, currencies, numbering schemes, time zones, and units are supported in their environment. By examining the supported values for each category, developers can build applications that display dates, times, and numbers in the most appropriate formats for their users. This article explores the supportedValuesOf method's capabilities, its usage patterns, and the differences between the values it returns compared to those from Locale objects, helping developers create more flexible and globally compatible applications.


## supportedValuesOf Method Overview

The Intl.supportedValuesOf method provides developers with a means to determine which calendar, collation, currency, numbering system, time zone, and unit values are supported in their JavaScript environment. This functionality helps with both feature detection and building locale-aware user interfaces.

The method returns an array of unique values, sorted in ascending lexicographical order, for each supported category. For instance, when querying the supported calendars, the response might include "buddhist", "chinese", "coptic", and "dangi". Similar arrays are generated for time zones, such as "Africa/Abidjan", "Africa/Accra", and "Africa/Addis_Ababa", and for units like "acre", "bit", and "byte".

Developers can use this information to build locale-sensitive applications. For example, when creating a date picker, the method can help determine which time zones and calendar systems are available to display. However, it's important to note that supportedValuesOf is locale-unaware. To get the preferred values for a specific locale, developers should use the corresponding Locale object methods, such as Intl.Locale.prototype.getCalendars().

To use this functionality effectively, developers need to be aware of browser compatibility. As of the current implementation, the method requires Typescript 5.1 or later to function correctly. Browser support varies, with global usage at 93.48% as of the latest data. Edge versions 99-13 support the method, while Internet Explorer versions 6-10 and 11 do not implement it.

The method throws a RangeError when an unsupported key is provided as an argument, providing clear feedback when a developer attempts to query an unsupported category. This helps prevent runtime errors and ensures that applications can handle unsupported configurations gracefully.


## Method Syntax and Usage

The method accepts a single parameter: `key`, which is a string indicating the category of values to be returned. The valid keys are "calendar", "collation", "currency", "numberingSystem", "timeZone", and "unit". The method returns a sorted array of unique string values indicating the values supported by the implementation for the given key.

The returned values are sorted in ascending lexicographical order, using `Array.prototype.sort()` with an undefined compare function. This ensures consistency across different JavaScript environments while maintaining readability.

Developers can use this information for feature detection, allowing them to determine which locale features are available in their environment. For example, they can check for specific time zones or calendar systems to decide which features to enable in their applications.

The method throws a RangeError if an invalid key is provided, providing clear feedback when a developer attempts to query an unsupported category. This helps prevent runtime errors and ensures applications can handle unsupported configurations gracefully. Developers should note that this method is locale-unaware, meaning certain identifiers may only be supported or preferred in specific locales. To determine the preferred values for a particular locale, developers should use the corresponding Locale object methods, such as `Intl.Locale.prototype.getCalendars()`.


## Supported Values by Category

The supportedValuesOf method provides unique values for calendars, collation, currency, numbering systems, time zone, and units. Supported categories include calendar types like buddhist, chinese, coptic, and dangi; collation types such as compat, dict, and emoji; currency identifiers like ADP, AED, AFA, and AFN; numbering system types including adlm, ahom, arab, and arabext; time zone identifiers such as Africa/Abidjan, Africa/Accra, and Africa/Addis_Ababa; and unit identifiers covering acre, bit, byte, celsius, centimeter, and many others.

The method accepts a single parameter indicating the category of values to be returned, with valid keys including "calendar", "collation", "currency", "numberingSystem", "timeZone", and "unit". For example, to retrieve supported time zones, developers can query Intl.supportedValuesOf("timeZone"). The returned values are sorted in ascending lexicographical order using Array.prototype.sort() with an undefined compare function, ensuring consistency across JavaScript environments while maintaining readability.

Note that certain identifiers may only be supported or preferred in specific locales. To determine preferred values for a particular locale, developers should use the corresponding Locale object methods, such as Intl.Locale.prototype.getCalendars(). The method throws a RangeError when an unsupported key is provided, providing clear feedback when developers attempt to query an unsupported category.


## Browser Compatibility

The `Intl.supportedValuesOf` method's support status across browsers varies significantly. As of the latest data, global usage stands at 93.48%. However, support is inconsistent across different browsers and versions:

- **Internet Explorer**: No support in versions 6-10 and 11

- **Edge**: Supported from version 99-139

- **Firefox**: Supported from version 93-141

- **Chrome**: Supported from version 99-139

- **Safari**: Supported from version 15.4-18.5, including TP (Technology Preview)

- **Opera**: Supported from version 85-117

- **Android Browser**: Supported from version 136

- **Chrome for Android**: Supported

- **Firefox for Android**: Supported

- **UC Browser for Android**: Support status unknown

- **Samsung Internet**: Supported from version 18.0-26, including 27

- **QQ Browser**: Support status unknown

- **Baidu Browser**: Support status unknown

- **KaiOS Browser**: Support status unknown

For older versions, developers need to implement a custom polyfill. A recommended approach is to create a file named `Intl.d.ts` and add the following declaration:

```typescript

declare namespace Intl {

  type Key = "calendar" | "collation" | "currency" | "numberingSystem" | "timeZone" | "unit";

  function supportedValuesOf(input: Key): any[];

}

```

This solution requires TypeScript 5.1 or later to function correctly.

The method's usage extends beyond the browser environment. It can be utilized in background scripts, browser action or page action popups, sidebars, options pages, or new tab pages for web extensions. Content scripts can access these APIs through the content script guide, though more powerful APIs require specific permission requests in the manifest.json file.

Developers can use this functionality for feature detection, allowing them to determine which locale features are available in their environment. For example, they can check for specific time zones or calendar systems to decide which features to enable in their applications. This information is crucial for building locale-sensitive applications that need to accommodate various international date and time formats.


## Error Handling and Best Practices

The method throws a RangeError when an unsupported key is provided, providing clear feedback when developers attempt to query an unsupported category. This helps prevent runtime errors and ensures applications can handle unsupported configurations gracefully.

The following keys are supported:

- Calendar: "buddhist", "chinese", "coptic", "dangi", etc.

- Collation: "compat", "dict", "emoji", etc.

- Currency: "ADP", "AED", "AFA", "AFN", "ALK", "ALL", "AMD", etc.

- Numbering System: "adlm", "ahom", "arab", "arabext", "bali", etc.

- TimeZone: "Africa/Abidjan", "Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers", etc.

- Unit: "acre", "bit", "byte", "celsius", "centimeter", etc.

The method's usage extends beyond the browser environment. It can be utilized in background scripts, browser action or page action popups, sidebars, options pages, or new tab pages for web extensions. Content scripts can access these APIs through the content script guide, though more powerful APIs require specific permission requests in the manifest.json file.

For older browser versions, developers need to implement a custom polyfill. A recommended approach is to create a file named `Intl.d.ts` and add the following declaration:

```typescript

declare namespace Intl {

  type Key = "calendar" | "collation" | "currency" | "numberingSystem" | "timeZone" | "unit";

  function supportedValuesOf(input: Key): any[];

}

```

This solution requires TypeScript 5.1 or later to function correctly. The method's support status across browsers varies. As of the latest data, global usage stands at 93.48%. Support is inconsistent across different browsers and versions, with Internet Explorer versions 6-10 and 11 not implementing the method at all. Edge versions 99-139, Firefox versions 93-141, Chrome versions 99-139, Safari versions 15.4-18.5 (including TP), Opera versions 85-117, and Android Browser version 136 are documented as supporting the method.

To determine preferred values for a specific locale, developers should use the corresponding Locale object methods, such as `Intl.Locale.prototype.getCalendars()`. The method's behavior is locale-unaware, meaning certain identifiers may only be supported or preferred in specific locales.

