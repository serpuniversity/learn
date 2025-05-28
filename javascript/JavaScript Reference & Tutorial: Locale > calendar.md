---

title: JavaScript Date and Time Localization

date: 2025-05-26

---


# JavaScript Date and Time Localization

JavaScript's `Intl` API has introduced powerful new capabilities for date and time localization, allowing developers to create applications that accurately represent dates and times in users' local calendars and formats. These features are particularly important for applications serving diverse global audiences, as different regions use a wide variety of calendar systems. From the familiar Gregorian calendar to the Islamic, Persian, and Thai calendars, JavaScript now provides comprehensive support for regional date and time conventions. This article explores the latest developments in JavaScript date localization, including the `Intl.Locale` API, calendar identifier management, and implementation details for modern JavaScript development.


## Locale and Calendar Fundamentals

The `Intl.Locale` API manages calendar types through the `calendar` property and related methods. This property returns the calendar type for a given locale, with values set at construction time through locale identifiers or the `Intl.Locale` constructor options. The property's value is read-only, preventing direct modification.

Three primary methods manage calendar settings:

1. Calendar settings can be specified using Unicode extension subtags (e.g., "fr-FR-u-ca-buddhist") or configuration objects in the `Intl.Locale` constructor.

2. The `getCalendars()` method returns an array of calendar identifiers sorted by preference, representing all commonly used calendars for the locale. For example, Arabic (Egyptian) locale returns ["gregory", "coptic", "islamic", "islamic-civil", "islamic-tbla"].

3. Browser compatibility ranges from full support in Chrome 74, Edge 79, Firefox 75, Opera 62, Safari 14, and Android WebView 74 to no support in Internet Explorer.

The `Intl.Locale` object represents a Unicode locale identifier with properties like language, script, and region, while extension tags handle calendar type, clock type, and numbering system type. These extensions enable precise locale representation and manipulation through methods like `maximize()` and `minimize()`. Calendar support extends beyond the native Gregorian calendar, with regional choices including Persian, Japanese, and Islamic calendar systems.


## Calendar Identifier Management

The getCalendars() method returns an array of calendar identifiers for a given locale, sorted by preference. For example, the Arabic (Egyptian) locale returns an array of five calendar identifiers: ["gregory", "coptic", "islamic", "islamic-civil", "islamic-tbla"]. The Japanese locale returns a simpler array of two identifiers: ["gregory", "japanese"].

Locale data for the "en-US" region was limited before version 13.0.0, but full browser support for calendar identifiers is now available across major browsers, including Chrome 74, Edge 79, Firefox 75, Opera 62, Safari 14, and Android WebView 74. The method returns a new array on each access and serves as an alternative to directly accessing the calendar property.

For setting calendar preferences, developers can use string-based locale identifiers with Unicode extensions or configuration objects in the Intl.Locale constructor. For instance, a Buddhist calendar for French can be created with either "fr-FR-u-ca-buddhist" or by using the configuration object method: new Intl.Locale("fr-FR", { calendar: "buddhist" }). The calendar property is read-only and cannot be changed directly, ensuring locale integrity while allowing developers to work with preferred calendar systems through these supported methods.


## Setting Locale Calendars

Calendar settings can be specified using locale strings with Unicode extensions or through configuration objects in the `Intl.Locale` constructor. The `calendar` property's value is set at construction time, either through the `ca` key of the locale identifier or through the `calendar` option of the `Intl.Locale()` constructor, with the latter taking priority if both are present.

Setting calendar preferences occurs through two primary methods:

1. Using a locale string with Unicode extensions:

   ```javascript

   const locale = new Intl.Locale("fr-FR-u-ca-buddhist");

   console.log(locale.calendar); // Prints "buddhist"

   ```

2. Through a configuration object argument:

   ```javascript

   const locale = new Intl.Locale("fr-FR", { calendar: "buddhist" });

   console.log(locale.calendar); // "buddhist"

   ```

The property value is read-only, preventing direct modification. Browser compatibility spans from Chrome 74, Edge 79, Firefox 75, Opera 62, Safari 14, and Android WebView 74 to no support in Internet Explorer.

The `Intl.Locale` class extends Unicode locale identifier subtags to represent calendar types, with valid calendar keys including `buddhist`, `chinese`, `coptic`, `dangi`, `ethioaa`, `ethiopic`, `gregory`, `hebrew`, `indian`, `islamic`, `islamic-umalqura`, `islamic-tbla`, `islamic-civil`, `islamic-rgsa`, and `iso8601`. The `islamicc` key has been deprecated, and developers should use `islamic-civil` instead.

Additional configuration options include:

- `dayHeaderFormat`: Specifies the format of the day in header, with possible values including 'Short', 'Narrow', 'Abbreviated', and 'Wide'.

- `firstDayOfWeek`: Sets the Calendar's first day of the week, defaulting to 0 for Sunday.

- `locale`: Overrides the global culture and localization value for the component, defaulting to "en-US".

- `max`: Sets the maximum date that can be selected in the Calendar, with a default value of new Date(2099, 11, 31).

- `min`: Sets the minimum date that can be selected in the Calendar, with a default value of new Date(1900, 00, 01).


## Date Object Creation and Localization

The JavaScript Date object interprets year, month, and day inputs based on the Persian calendar, but for more precise control, developers can use the Temporal API. While the current implementation requires a polyfill, major browsers including Chrome, Firefox, Safari, and Edge are implementing Temporal support.

The native Date object can create date objects using ISO 8601 format or numerical inputs, and can output dates in various locales using methods like toLocaleString and toLocaleDateString. For example, `new Date("1401/01/01")` creates a Persian date, and `console.log(dt.toLocaleString("fa-IR"))` outputs it in Persian format. The Temporal API further enhances calendar support with methods like `Temporal.PlainDate.from({year, month, day, calendar: 'persian'})`, providing both calendar creation and formatting capabilities.

Understanding user locales and regional calendars is crucial for accurate date representation. While the Gregorian calendar follows January and February, other calendars like the Islamic, Persian, and Thai calendars have distinct month names and structures. This variation requires careful localization to ensure dates are correctly represented for each region's default calendar.


## Browser Compatibility and Polyfills

JavaScript's date localization capabilities have expanded since September 2020, with full browser support available through libraries like Moment.js and Luxon. These libraries offer robust solutions for developers working with dates and time across multiple locales and time zones.

Modern JavaScript development increasingly favors libraries such as Date-fns and Luxon, which provide comprehensive date and time utilities with localized support. While Moment.js remains widely used due to its extensive feature set and large ecosystem, it has reached a maintenance phase and is no longer receiving significant updates. The updated Moment.js library follows the ECMA-402 standard, codified as the Intl object, which allows other libraries like Luxon to reduce or eliminate their need for separate data files.

For developers prioritizing modern best practices, Luxon presents several advantages. As a more modern alternative to Moment.js, it features an immutable API and built-in internationalization and time zone support. While it has a smaller community compared to Moment.js, its growing popularity indicates its value for new projects. The library's key strengths include comprehensive date and time manipulation, robust locale support through internationalization, and built-in time zone capabilities. This makes it particularly suitable for applications requiring precise date calculations and consistent time zone handling across global users.

