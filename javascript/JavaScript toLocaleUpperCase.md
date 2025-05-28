---

title: JavaScript String toLocaleUpperCase() Method

date: 2025-05-27

---


# JavaScript String toLocaleUpperCase() Method

In JavaScript, converting strings to uppercase is a common operation – but what if you need to handle language-specific rules for capitalization? That's where the toLocaleUpperCase() method comes in. This powerful tool lets you convert strings to uppercase based on the host's current locale, taking into account special cases like Turkish 'ı'. In this article, we'll explore how toLocaleUpperCase() works, how it differs from the regular toUpperCase() method, and how to use it effectively in your JavaScript applications.


## Introduction to toLocaleUpperCase

The toLocaleUpperCase() method in JavaScript converts a string to uppercase based on the host's current locale, providing locale-specific case mappings. This locale is determined by the browser's language settings.

The method syntax is _string_.toLocaleUpperCase([locale]), where the optional locale parameter accepts BCP 47 language tags or an array of tags. If no locale is provided, it defaults to the host environment's current locale.

For most cases, the method behaves similarly to toUpperCase(), producing the same result. However, in locales where Unicode case mappings conflict with language-specific rules (such as Turkish), the method provides distinct behavior. This is illustrated in the example below, where the Turkish letter 'ı' is converted differently based on the specified locale.

```javascript

var totn_string = 'cafe';

console.log(totn_string.toLocaleUpperCase('en-US')); // CAFÉ

```

When using multiple locale options, the best available locale from the provided array is selected. The method returns a new string containing the uppercase version, leaving the original string unchanged. This behavior is consistent across browsers, with support beginning in July 2015.

The difference in behavior between toLocaleUpperCase() and toUpperCase() highlights the importance of locale awareness in string manipulation, particularly when working with languages that have complex case mappings.


## Method Syntax and Usage

The method syntax for toLocaleUpperCase() is:

string.toLocaleUpperCase([locale])

Where:

- string is the string instance to convert to uppercase

- locale (optional) is a BCP 47 language tag or array of tags specifying the locale for conversion

If no locale is provided, the method defaults to the host environment's current locale. The method returns a new string containing the uppercase version, leaving the original string unchanged.

The optional locale parameter allows specifying the locale for conversion. This can be a single locale tag (e.g., "en-US") or an array of tags, where the best available locale is selected. The method throws RangeError if an invalid locale is provided and TypeError if an array element is not of type string.

For example:

```javascript

let str = "istanbul";

console.log(str.toLocaleUpperCase('en-US')); // ISTANBUL

console.log(str.toLocaleUpperCase()); // ISTANBUL

console.log(str.toLocaleUpperCase('tr')); // İSTANBUL

```

The method has been available across browsers since July 2015 and follows the ECMAScript 2026 Language Specification. While it produces the same result as toUpperCase() for most characters, it differs in locales where Unicode case mappings conflict with language-specific rules, such as Turkish.


## Locale Parameter

The locale parameter accepts BCP 47 language tags or an array of tags. This parameter controls the locale-specific case mapping used for the conversion. If no locale is provided, the method defaults to the host environment's current locale.

When using an array of locale options, the method selects the best available locale from the provided list, falling back to the default locale if necessary. This behavior is consistent with the similar method String.prototype.toLocaleLowerCase().

The method throws RangeError if a provided locale is invalid and TypeError if an array element is not of type string. These exceptions ensure that the method operates with correctly formatted locale information.

For example, the following code demonstrates a valid use of the method with a Turkish locale:

```javascript

let str = "istanbul";

console.log(str.toLocaleUpperCase('tr')); // İSTANBUL

```

The method supports a wide range of locales, including lt-LT, lt-LIETVA, and lt-x-lietuva, though functionality may vary between different browser implementations. To access full ICU (locale) data for earlier versions of Node.js, users should refer to the official documentation on the --with-intl option and provide the necessary data.


## Comparison with toUpperCase

The toLocaleUpperCase() method and toUpperCase() method produce the same result for most characters. However, in locales where Unicode case mappings conflict with language-specific rules (such as Turkish), the results may differ. The method uses locale-specific case mappings to convert characters to uppercase, which can result in different visual representations compared to the default case mappings in Unicode.

The key difference arises from how these methods handle certain characters. For example, the Turkish letter 'ı' behaves differently when converted to uppercase:

- Using 'en-US' locale: "ı"toLocaleUpperCase('en-US') returns "I"

- Using Turkish locale: "ı"toLocaleUpperCase('tr') returns "İ"

This difference highlights the importance of locale awareness in string manipulation, particularly when working with languages that have complex case mappings. The Turkish example demonstrates that while "ist".toLocaleUpperCase('en-US') === "IST" returns true, "istanbul".toLocaleUpperCase('tr') === "İSTANBUL" returns false, due to the visually distinct uppercase representation of the 'ı' character in Turkish.

The method's behavior demonstrates its utility in handling locale-specific text transformations, while also illustrating the potential complexities introduced by Unicode case mappings. Understanding these differences is crucial for developers working with internationalized JavaScript applications, where correct locale-aware string manipulation can significantly impact both functionality and user experience.


## Browser Compatibility and Implementation

The method follows the ECMAScript 2026 Language Specification and the ECMAScript 2026 Internationalization API Specification. Browser compatibility is consistent across desktop and mobile browsers, with support beginning in July 2015. The supported locales include:

- lt-LT

- lt-LIETVA

- lt-x-lietuva

- lt-u-co-phonebk

Before version 13.0.0, only en-US locale data was available by default. For other locales, the function falls back to en-US. To access full ICU (locale) data for earlier versions of Node.js, users should refer to the official documentation on the --with-intl option and provide the necessary data.

The method operates through the Intl.Locale object, utilizing BCP 47 language tags for locale specification. It can handle both single locale tags and arrays of tags, selecting the best available locale when multiple options are provided. This functionality is reflected in the method's specification, which details how locale strings are constructed with the -u -kf extension key for caseFirst values.

The method's implementation demonstrates flexibility in handling locale-specific case mappings. While it produces the same result as toUpperCase() for most characters, it differs in locales where Unicode case mappings conflict with language-specific rules, such as Turkish. This is particularly evident in how it handles certain characters:

- "i\u0307".toLocaleUpperCase("lt-LT") returns "I"

- "i\u0307".toLocaleUpperCase() returns "İ" using the default Turkish locale

Understanding these implementation details is crucial for developers working with internationalized JavaScript applications, as correct locale-aware string manipulation can significantly impact functionality and user experience.

