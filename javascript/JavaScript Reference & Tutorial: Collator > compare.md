---

title: JavaScript Collator: Compare Method Overview

date: 2025-05-26

---


# JavaScript Collator: Compare Method Overview

In the ever-evolving landscape of web development, the ability to perform accurate string comparisons that respect linguistic nuances is crucial. JavaScript's Collator provides a powerful tool for locale-sensitive string comparison, allowing developers to sort and compare text based on specific collation rules. This article explores the capabilities of the Collator class, focusing on its compare method and how it enables developers to implement language-sensitive text comparison in their applications. Through detailed explanations and practical examples, we'll examine how developers can leverage the Collator's robust feature set to achieve precise string comparisons that meet their application's requirements.


## Collator Basics

The Collator class enables locale-sensitive string comparison through its compare method, which performs language-sensitive text comparison according to specific collation rules. Utilizing four comparison strengths—PRIMARY, SECONDARY, TERTIARY, and IDENTICAL—the class determines the significance of differences between characters based on the specified locale.

The comparison process considers Unicode decomposition during collation, employing FULL_DECOMPOSITION mode to handle composed characters and special format characters such as half-width and full-width ASCII/Katakana. Character differences are classified into primary, secondary, and tertiary levels, with the exact assignment varying by language. For example, Czech distinguishes between "e" and "f" at the primary level, while "e" and "ě" are considered secondary differences.

To obtain a Collator instance, developers can use the static getInstance method, specifying either the default locale or a desired locale. The class supports multiple decomposition modes: NO_DECOMPOSITION, CANONICAL_DECOMPOSITION, and FULL_DECOMPOSITION, with FULL_DECOMPOSITION used in most complete decompositions according to Unicode Normalization Forms.

The compare method evaluates the order of two strings, returning -1, 0, or 1 based on their relative position. For efficient multiple comparisons, developers should use the getCollationKey method to transform strings into CollationKey objects, which provide better performance through bitwise comparison. This approach ensures that strings are compared based on the collation rules specific to the configured locale.


## Basic Usage and Example

The compare method provides detailed insights into the ordering of strings based on their linguistic properties. According to the ECMAScript Internationalization API Specification, this method returns -1 when the first string precedes the second lexicographically, 0 when they are equivalent, and 1 when the first string follows the second. This behavior aligns with the generalized comparison logic described in the official documentation.

For precise control over comparison sensitivity, developers can configure the Collator instance with various options. The sensitivity property, for instance, determines how case distinctions affect comparisons, with "base" treating "ã" as equivalent to "a" and "level" maintaining their separateness. The example provided showcases these distinctions when comparing strings across German and Swedish locales, highlighting the method's adaptability to different linguistic requirements.

The compare method's performance characteristics are crucial for efficient string processing. The JavaScript specification emphasizes its suitability for single comparisons, while noting that CollationKey.compareTo offers superior performance for repeated string comparisons. This distinction reflects the method's intended use case and implementation efficiency considerations.


## Locale and Option Configuration

The Collator constructor allows extensive configuration of collation behavior through various options. These include:


### General Configuration

- `co`: Unicode extension key for custom collation order

- `numeric`: Enables numeric comparison

- `caseFirst`: Determines case sorting behavior

- `sensitivity`: Specifies comparison criteria

- `ignorePunctuation`: Controls punctuation handling


### Sensitivity Levels

The sensitivity property accepts the following values:

- "primary": Only primary differences (case-, accent-, variation-insensitive, base-character-sensitive)

- "base": Primary and secondary differences

- "secondary": Primary, secondary, and tertiary differences

- "accent": Primary, secondary, and tertiary differences (accent-, case-, variation-insensitive)

- "tertiary": All differences considered significant


### Script-Specific Options

- `upperFirst`: Controls capitalization for case-sensitive scripts

- `reverse`: Determines sorting order

- `scriptOrder`: Specifies script sorting order for multiple scripts

- `style`: Locale-dependent collation style

- `usage`: Specifies collator usage ("sort" or "search")


### Locale Handling

The constructor handles both locale and options validation, throwing a RangeError for invalid inputs. The _locale_ parameter supports both string and Locale object types, while other options have specific value ranges.


### Implementation Details

The class provides three decomposition modes:

- NO_DECOMPOSITION: Fastest, but only correct for languages without accents

- CANONICAL_DECOMPOSITION: Ensures correct collation of accented characters

- FULL_DECOMPOSITION: Most complete, but slowest mode, including half-width and full-width characters


## Custom Comparison and Sorting

The compare method enables developers to implement custom sorting logic by comparing strings according to specific collation rules. This customization allows for precise control over comparison criteria, including case sensitivity and numeric comparison.

For array sorting, developers can use the compare method directly or create a comparator function bound to the Collator object. The syntax for direct comparison is:

```javascript

arr.sort(collator.compare);

```

This approach is particularly effective when comparing strings once, as noted in the ECMAScript Internationalization API Specification.

When implementing custom comparators, developers have several options. For simple cases, they can chain multiple compare calls:

```javascript

arr.sort((a, b) => collator.compare(a.firstName, b.firstName) || collator.compare(a.lastName, b.lastName));

```

This technique ensures that the first comparison determines the order unless the strings are equal, triggering the second comparison.

For more complex sorting needs, developers can create custom comparator functions bound to the Collator object. This approach, supported by the Intl.Collator.prototype.getComparator method, allows for efficient sorting of arrays using the bound comparator function:

```javascript

var arr = [...unsorted];

var collator = new Intl.Collator('de-u-co-phonebk');

arr.sort(collator.getComparator());

```

The Collator class also provides methods for generating CollationKeys, which can significantly improve performance when sorting strings multiple times. This functionality is demonstrated in the following example:

```javascript

var sortKey = collator.sortKey("example string");

```

These generated sort keys maintain correct collation order when compared byte-for-byte, making them ideal for optimizing repeated string comparisons.


## Cross-Browser Compatibility

Availability and Browser Support

The Intl.Collator object and its compare method have achieved broad support across major browsers and platforms, with initial implementation beginning in September 2017. The constructor and prototype methods are consistently available in contemporary web environments, though implementation details can vary between versions and engine implementations.

Performance and Implementation

Performance considerations are critical when using the compare method across different platforms. The method's implementation varies between browsers and versions, with some engines optimizing for specific use cases. For example, the Mozilla implementation prioritizes correct collation behavior over absolute performance, while other engines may optimize for speed in certain scenarios.

The compare method's results can differ between engines, particularly when handling locale-specific behavior. Developers should test for expected outcomes, especially when relying on specific sorting behaviors. The comparison results are defined by the ECMAScript Internationalization API Specification, which requires that the method return negative values for before characters, positive values for after characters, and zero for equal characters.

Usage Considerations

The compare method's options parameter allows fine-grained control over comparison behavior. Browser implementations support various options, including caseFirst, sensitivity, and numeric, though the available options can vary between engines. For consistent results across environments, developers should test their specific usage scenarios in target platforms.

Best Practices

To achieve reliable cross-browser behavior, developers should:

- Test with multiple engines and versions

- Consider using CollationKey for performance-critical applications

- Verify behavior with locale-specific characters and sorting rules

- Use the resolvedOptions method to ensure consistent options across environments

