---

title: JavaScript String localeCompare() Method

date: 2025-05-26

---


# JavaScript String localeCompare() Method

JavaScript's `localeCompare()` method provides a powerful way to compare strings based on locale-specific rules, but its intricacies can be challenging to master. This article reveals its inner workings, from its fundamental mechanics to its advanced features like numeric sorting and sensitivity options. You'll learn how it returns comparison values that might surprise you (like -2 or 2), and how to use its powerful options to get the exact comparison behavior your multilingual app needs.


## Method Overview

The JavaScript `localeCompare()` method returns -1, +1, or 0 based on the comparison. The method returns -1 if the reference string comes before the compare string, +1 if the reference string comes after the compare string, and 0 if they are equivalent. The method returns numbers that may vary from 1 to any other number but maintains the same sign convention: negative for negative comparison and positive for positive comparison across browsers.

The method has three parameters: compareString (required), options (optional for customizing behavior), and locale (optional for determining language formatting convention). The `compareString` is the string being compared, while the `options` parameter allows specifying language formatting conventions. The `locale` parameter is an array of BCP 47 language tags defining the language's primary code and extension.


## Basic Usage

The method returns -1 if the reference string occurs before the compare string, 0 if the two strings are equivalent, and 1 if the reference string occurs after the compare string. The return value varies between browsers and versions, with some returning -2 or 2, or even other negative or positive values. The method works by comparing strings character by character, with uppercase letters coming before lowercase letters. The comparison stops as soon as it finds a character that differs between the two strings.

The method returns a negative number if the reference string comes before the compare string, a positive number if it comes after, and 0 if they are equivalent. The return value maintains the same sign convention across browsers but varies in magnitude. In modern browsers with Intl.Collator support, the method returns the same result as `new Intl.Collator(locales, options).compare(referenceStr, compareString)`.

The method's behavior can be customized through the options parameter, which allows specifying language formatting conventions. The method supports various properties such as sensitivity, numeric sorting, and case handling. For example, setting the sensitivity option to "base" performs a case-insensitive comparison using the specified locale. The method can handle numeric comparison, returning -1 for some locales like "en-u-kn-true".


## Parameters

The method requires the compareString parameter, which is the string to compare against the reference string. This parameter is mandatory, and the method will throw a TypeError if it is missing (as demonstrated in the MDN Web Docs example).

The locale parameter is optional and specifies the language whose formatting conventions should be used. It accepts a BCP 47 language tag or an array of such tags, where a BCP 47 language tag defines a language that may contain a primary language code as well as an extension. If not provided, the method uses the host environment's current locale (as noted in the JavaScript: String localeCompare() method documentation).

The options parameter is also optional and allows customization of the function's behavior. It can be an object containing various properties to adjust how the comparison works. The supported options include:

- sensitivity: Determines how "case" will be handled when sorting. It can be set to:

  - "upper": uppercase letters will be sorted first

  - "lower": lowercase letters will be sorted first

  - false (default): use the locale's default sorting

- ignorePunctuation: Determines whether punctuation will be ignored during sorting. It can be set to:

  - true: punctuation will be ignored

  - false (default): punctuation will not be ignored

- localeMatcher: Determines the locale matching algorithm to use. It can be set to:

  - "lookup"

  - "best fit" (default)

- numeric: Determines whether numeric collation will be used. It can be set to:

  - true: numeric collation will be used when sorting

  - false (default): numeric collation will not be used

These options provide fine-grained control over the comparison behavior, allowing developers to tailor the localeCompare() method to their specific needs. For instance, setting sensitivity to "base" performs a German-style comparison where "a" and "ä" are considered the same base letter (as demonstrated with 'Ã¤'.localeCompare('a', 'de', { sensitivity: 'base' }) returning 0).

The method requires knowledge of Unicode and locale-specific sorting rules to function correctly, making it particularly useful for applications that need to handle multilingual text data in a culturally sensitive manner.


## Advanced Options

The options parameter offers several attributes to adjust comparison behavior. Setting the sensitivity option to "base" performs a case-insensitive comparison using the specified locale, as demonstrated with 'Ã¤'.localeCompare('a', 'de', { sensitivity: 'base' }) returning 0. The method can handle numeric comparison through the numeric option, returning -1 for some locales like "en-u-kn-true".

The sensitivity property determines how letters are compared and has several options:

- "base" - compares letters without considering diacritics or case

- "accent" - ignores case but treats letters with diacritics as distinct

- "case" - treats uppercase and lowercase letters as distinct

- "variant" (default) - treats uppercase and lowercase letters as distinct and ignores diacritics

The default sensitivity setting is "variant," which provides the most detailed comparison. The method also supports additional attributes for customization:

- numeric: specifies whether to compare strings as numbers (default false, but Chrome treats this as true)

- caseFirst: determines the order of uppercase and lowercase letters (values: upper, lower, false)

The options parameter allows developers to tailor the comparison to their specific needs, enabling precise control over sorting behavior based on locale and text characteristics.


## Locale Handling

The localeCompare() method allows developers to specify the language whose sorting conventions should be used. This is particularly important for applications dealing with multilingual text data, as it ensures consistent and culturally appropriate sorting behavior across different locales.

The method provides several options for customizing sorting behavior through the `options` parameter. For instance, the `sensitivity` attribute determines how letter comparison works and can be set to:

- "base" - for German-style comparison where "a" and "ä" are considered the same base letter

- "accent" - to ignore case but treat letters with diacritics as distinct

- "case" - to treat uppercase and lowercase letters as distinct

- "variant" - the default setting, which treats uppercase and lowercase letters as distinct while ignoring diacritics

The method also supports additional attributes for advanced customization:

- `numeric`: to enable numeric collation when sorting

- `caseFirst`: to determine the order of uppercase and lowercase letters

- `ignorePunctuation`: to enable or disable punctuation ignoring during sorting

Locale handling in the method works through the `locales` parameter, which accepts BCP 47 language tags or arrays of such tags. For example, specifying "en-US" will use US English sorting rules. If no locale is provided, the method defaults to the host environment's current locale.

The method's behavior varies between implementations, with some handling different positive or negative return values (such as -2 or 2) while others maintain consistent sign conventions across browsers. To check for implementation support, developers can use the `"i"` argument and catch `RangeError` exceptions.

