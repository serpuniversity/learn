---

title: JavaScript Locale > getTextInfo

date: 2025-05-26

---


# JavaScript Locale > getTextInfo

Text direction information is crucial for proper rendering of text in applications that support multiple languages and writing systems. The getTextInfo() method of the Intl.Locale object returns essential information about the text direction for a given locale, allowing developers to ensure correct text ordering and layout. This article explores the implementation and usage of the getTextInfo() method, its consistent behavior across different locales, and its role in modern web development's internationalization capabilities.


## getTextInfo Method Overview

The getTextInfo() method returns an object indicating text direction as either 'ltr' (left-to-right) or 'rtl' (right-to-left) for the specified locale. This method plays a crucial role in determining how text should be rendered based on the language and script associated with a particular locale.

The method returns an object with a single property:

- `direction`: A string that specifies the text direction. It can be either `"ltr"` for left-to-right or `"rtl"` for right-to-left. This information is particularly important for applications that need to ensure proper rendering of text, especially when dealing with languages that have different writing systems (such as Arabic and Hebrew, which are written from right to left).

For example:

```javascript

const ar = new Intl.Locale("ar");

console.log(ar.getTextInfo()); // { direction: "rtl" }

const es = new Intl.Locale("es");

console.log(es.getTextInfo()); // { direction: "ltr" }

```

The implementation of this method was initially as an accessor property called `textInfo`, but it was later changed to a method to prevent false equality comparisons of the form `locale.textInfo === locale.textInfo`, which would evaluate to `false`. This change ensures more accurate comparison of locale objects based on their text direction information.


## Method Implementation and Browser Support

The getTextInfo() method was initially implemented as an accessor property called textInfo in certain browser versions. However, to address inconsistencies in equality comparisons, the implementation was later changed to a method. This modification prevents situations where `locale.textInfo === locale.textInfo` would incorrectly return false.

According to the specification, the method returns an object with a single property: `direction`, which specifies the text direction as either "ltr" (left-to-right) or "rtl" (right-to-left). The method's browser compatibility across major browsers is excellent, with full support in Chrome, Edge, and Firefox across both desktop and mobile environments.

The text direction information returned by the method is consistent with the writing systems of the specified locales. For example, Arabic locales consistently return "rtl" direction, while Spanish locales return "ltr". This functionality is particularly important for applications that need to ensure proper rendering of text, especially when dealing with languages that have different writing systems.


## Locale and Text Direction

This difference in text direction is particularly important for applications that need to render text correctly across multiple languages. For example, Arabic locales consistently return "rtl" direction, while Spanish locales return "ltr". This functionality is crucial for proper rendering of text, especially when dealing with languages that have different writing systems.

The method's detailed implementation ensures correct text ordering through the `direction` property, which can be either "ltr" (left-to-right) or "rtl" (right-to-left). When called on an Arabic locale (`ar`), it returns `{ direction: "rtl" }`. Similarly, when called on a Spanish locale (`es`), it returns `{ direction: "ltr" }`.

This capability is aligned with the broader functionality of the `Intl.Locale` object, which provides essential data for localization and internationalization. The object includes properties for week information, text information, calendar data, collation data, and numbering system data, each tailored to specific language and script requirements.


## Method Usage and Examples

The method returns this information through an object with a single property: `direction`. This property can take one of two values: "ltr" for left-to-right text direction, or "rtl" for right-to-left text direction. This information is essential for rendering text correctly, particularly when dealing with languages that have distinct writing systems.

To demonstrate its usage, consider the following examples:

```javascript

const ar = new Intl.Locale("ar");

console.log(ar.getTextInfo()); // { direction: "rtl" }

const es = new Intl.Locale("es");

console.log(es.getTextInfo()); // { direction: "ltr" }

```

These examples create new `Intl.Locale` instances for Arabic ("ar") and Spanish ("es"), then call `getTextInfo()` to retrieve text direction information for each locale. The method returns different values for these locales, demonstrating its functionality across multiple language scripts.

The text direction information is consistent with the writing systems of the specified locales. For instance, when called on an Arabic locale (`ar`), the method returns `{ direction: "rtl" }`, while for a Spanish locale (`es`), it returns `{ direction: "ltr" }`.

This capability is aligned with the broader functionality of the `Intl.Locale` object, which provides essential data for localization and internationalization. The object includes properties for week information, text information, calendar data, collation data, and numbering system data, each tailored to specific language and script requirements.


## Additional Resources

The specification for the getTextInfo method can be found at https://tc39.es/proposal-intl-locale-info/#sec-Intl.Locale.prototype.getTextInfo, where it is described as returning an object representing text typesetting information associated with the Locale data specified in UTS 35's Layouts Elements.

The method returns an object containing the following properties:

- direction: A string indicating the direction of text for the locale, which can be either "ltr" (left-to-right) or "rtl" (right-to-left).

Browser compatibility information is as follows:

| Desktop | Mobile | Server |

|---------|--------|--------|

| Chrome  | Edge   | Firefox |

All major browsers support the method across both desktop and mobile environments, with full compatibility in Chrome, Edge, and Firefox.

