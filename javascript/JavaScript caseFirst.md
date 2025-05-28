---

title: JavaScript Internationalization: Locale.caseFirst

date: 2025-05-26

---


# JavaScript Internationalization: Locale.caseFirst

Sorting text correctly according to local language rules can make or break an international application. That's where JavaScript's Intl.Locale comes in - it lets you customize how your app handles text based on where your users are. One lesser-known feature is the caseFirst property, which lets you choose whether uppercase or lowercase letters should come first in a locale's alphabet. Whether you're building a French app that sorts names by last name (uppercase) first or an English site that puts lowercase letters before uppercase, this little-known property can make your app more user-friendly and accurate for speakers of languages with specific sorting rules.


## caseFirst Property Basics

The `Intl.Locale.prototype.caseFirst` property in JavaScript's Intl.Locale allows specifying how case should be handled in locale-specific text processing. It enables three distinct case-first sorting orders: upper (uppercase before lowercase), lower (lowercase before uppercase), and false (no special case ordering).

This property can be configured through two primary methods:

1. Directly in the locale string:

   The required format combines the base locale identifier with the `-u` extension key and the `-kf` subtag, followed by the desired case-first value. For example:

   ```

   let caseFirstStr = new Intl.Locale("fr-Latn-FR-u-kf-upper");

   ```

2. Using a configuration object in the constructor:

   A configuration object can be passed as the second argument to the Intl.Locale constructor, with the `caseFirst` property set to the desired value. For example:

   ```

   let caseFirstObj = new Intl.Locale("en-Latn-US", {caseFirst: "lower"});

   ```

The property returns a collation key representing the locale's case-first sorting order, implementing the Unicode Collation Algorithm (UCA) for string comparison. Understanding this mechanism is crucial for developers working with locales that require specific case-sensitive sorting rules, particularly in applications supporting multiple languages with distinct text ordering requirements.


## Configuring caseFirst

The caseFirst property can be configured using two primary methods: direct specification in the locale string or through the configuration object passed to the Intl.Locale constructor.


### Locale String Configuration

In the Unicode locale string specification, the caseFirst property is represented by the `kf` extension key. To configure caseFirst in the locale string, follow these steps:

1. Start with the base locale identifier (e.g., "fr-Latn-FR")

2. Add the `-u` extension key

3. Append the `-kf` subtag

4. Include the desired caseFirst value (upper, lower, or false)

For example, to create a French locale with case-first set to upper:

```javascript

const caseFirstStr = new Intl.Locale("fr-Latn-FR-u-kf-upper");

console.log(caseFirstStr.caseFirst); // prints "upper"

```


### Constructor Configuration

The configuration object passed to the Intl.Locale constructor allows setting the caseFirst property directly. The property should be included as part of the configuration object, with the desired value as its property:

```javascript

const caseFirstObj = new Intl.Locale("en-Latn-US", { caseFirst: "lower" });

console.log(caseFirstObj.caseFirst); // prints "lower"

```

This configuration method provides flexibility, allowing developers to set multiple locale properties simultaneously.


## Locale String Configuration

The caseFirst value is specified using the `-u` extension key followed by the `-kf` subtag, indicating a locale string extension subtag. This subtag adds additional data about the locale to the identifier string using the `-u` extension key, with the `caseFirst` value added using the `-kf` extension key.

This feature enables precise control over case ordering in locale-specific text processing, with three possible values:

- `upper`: Sorting uppercase characters before lowercase characters

- `lower`: Sorting lowercase characters before uppercase characters

- `false`: No special case ordering

The `-kf` subtag is particularly useful for implementing language-specific sorting rules, such as the French convention where spaces precede punctuation and both uppercase and lowercase punctuation characters are treated as lowercase for sorting purposes. This allows developers to tailor string comparisons to regional standards and user expectations, ensuring that applications correctly reflect the intended order of displayed text.


## Constructor Configuration

The configuration of the caseFirst property can also be achieved through the constructor's configuration object, which provides additional flexibility for setting multiple locale properties simultaneously. The configuration object should include the caseFirst property with the desired value (upper, lower, or false). For example:

```javascript

const caseFirstObj = new Intl.Locale("en-Latn-US", { caseFirst: "lower" });

console.log(caseFirstObj.caseFirst); // prints "lower"

```

This method allows developers to specify multiple configuration options in a single constructor call, streamlining locale initialization.

The caseFirst property affects how strings are ordered in the locale, with certain locales using character case (uppercase or lowercase) in the collation process. The property can have three values:

- upper: Indicates that uppercase characters should be sorted before lowercase characters

- lower: Indicates that lowercase characters should be sorted before uppercase characters

- false: Indicates no special case ordering

Browser support for the caseFirst property has improved since its initial implementation. While full support was not present across all browsers before version 74, the latest versions of Chrome and Android webview now fully support the feature (Chrome 74, Edge 79, Firefox 75, Opera 62, Safari 14). Node.js also supports the property in version 12.0.0 and later, though native support varies across different JavaScript environments.


## Browser Support

The caseFirst property implementation varies across browsers, with full support in Chrome, Edge, Firefox, Safari, and Android webview as of version 74. For other browsers, support is mixed: Opera and Chrome Android versions 74 and above provide support, while Safari iOS 14 and Samsung Internet 11.0 also fully support the feature.

Before these versions, browser support was limited:

- Chrome and Edge support began in version 74

- Firefox added support in version 75

- Opera supported the property from version 62

- Safari implemented support in version 14

- Android webview achieved full support in version 74, matching Chrome on mobile devices

While Node.js supports the property in version 12.0.0 and later, native support varies across different JavaScript environments. Developers should check browser compatibility before relying on caseFirst functionality, especially when targeting older or less common browser versions. For applications requiring consistent case sensitivity across multiple locales, the constructor configuration method provides a flexible way to set the property alongside other locale options.

