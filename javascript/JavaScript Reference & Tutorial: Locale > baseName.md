---

title: JavaScript Locale: baseName Property

date: 2025-05-26

---


# JavaScript Locale: baseName Property

The JavaScript `Intl.Locale` object offers powerful tools for working with locale-specific data, including methods to manage and manipulate locale identifiers. While developers can create complex locale identifiers with detailed calendar and numbering system specifications, there's often a need to work with a simplified version of this identifier that excludes region and calendar details. This is where the `baseName` property comes into play. In this article, we'll explore how the `baseName` property processes Unicode locale identifiers to extract the core language, script, and region information, providing developers with a robust way to handle basic locale manipulation while maintaining the flexibility to manage specific locale modifications through separate property settings.


## baseName Property Basics

The `baseName` property of the `Intl.Locale` object provides a simplified view of the locale identifier, excluding region and calendar specification details. This property is particularly useful when you need to work with the core language identifier without additional locale modifiers.

Let's consider an example: `japan = new Intl.Locale("ja-JP-u-ca-gregory-hc-24")`. When we examine this locale, we see it contains specific calendar and hour cycle specifications. However, when we create the `baseName` property using `japan.baseName`, we get "ja-JP-u-ca-gregory-hc-h24". This output demonstrates that the `baseName` property strips out the hour cycle modification ("h24") while keeping the core locale identifier intact.

According to the ECMA-402 specification, the `baseName` property processes Unicode locale identifier subtags to extract the language, script, and region information. This means it operates on the BCP 47 language tag structure, which consists of:

- Language (ex: "ja" for Japanese)

- Script (optional, ex: "Latn" for Latin script)

- Region (optional, ex: "JP" for Japan)

- Extension tags (optional, ex: "u-ca-gregory" for calendar specification)

The property specifically targets the language, script, and region subtags, omitting any extension tags that might include calendar, hour cycle, or numbering system information. This structure allows developers to create locales with specific language, region, and calendar settings while maintaining the ability to extract the fundamental language identifier through the `baseName` property.


## Locale Identifier Structure

A complete locale identifier consists of several components:

- Language: This identifies the primary language, represented by 2-3 or 5-8 letter codes following the Unicode language subtag grammar. For example, "fr" for French or "ko" for Korean.

- Script: The writing system used for the language, identified by a 4-letter code following the Unicode script subtag grammar. For instance, "Latn" for Latin script or "Kore" for Korean script.

- Region: This specifies the geographic location, using either 2-letter country codes (ISO 3166-1 alpha-2) or 3-digit FIPS 10-4 region codes. "US" represents the United States, while "KR" denotes South Korea.

- Extension Tags: Optional information about calendar type, clock type, and numbering system type, represented by segments of 3-8 alphanumerals joined by hyphens.

The baseName property returns the core locale identifier, excluding extension tags. This means it provides a simplified view of the locale, containing only the language, script, and region subtags. For example, when creating a Finnish locale with options `{ script: "Fin" }` and setting the region to "FI", the baseName would be "fi-Fin-FI" - "fi" for Finnish language, "Fin" for Finnish script, and "FI" for Finland.


## Example Usage: baseName Property

The baseName property delivers a simplified locale identifier that includes only the language, script, and region subtags. Let's explore this through specific examples:

```javascript

// Create a Japanese locale with detailed calendar and hour cycle specifications

const japan = new Intl.Locale("ja-JP-u-ca-gregory-hc-24");

console.log(japan.toString()); // Output: ja-JP-u-ca-gregory-hc-24

// Extract the core locale identifier using baseName

console.log(japan.baseName); // Output: ja-JP-u-ca-gregory-hc-h24

```

In this example, the complete locale identifier includes calendar ("u-ca-gregory") and hour cycle ("u-hc-24") specifications. However, the baseName property removes these extension tags, returning "ja-JP-u-ca-gregory-hc-h24". This output demonstrates that baseName processes the Unicode locale identifier subtags to extract the language, script, and region information while omitting extension tags.

To further illustrate this concept, consider the following creation of a Dutch locale:

```javascript

const dutch = new Intl.Locale("nl-Latn-BE", { region: "NL" });

console.log(dutch.toString()); // Output: nl-Latn-BE-u-variant-nl-nl

console.log(dutch.baseName); // Output: nl-Latn-NL

```

Here, we create a Dutch locale that includes specific script and region settings. The `baseName` property returns "nl-Latn-NL", effectively stripping away the region extension tag while maintaining the core language identifier. This behavior aligns with the Unicode language tag structure, where the baseName property focuses on the language, script, and region subtags, excluding any extension tags that contain specific locale modifications.

The `baseName` property implementation operates within this structured framework, processing the Unicode locale identifier subtags to extract the language, script, and region information while ignoring extension tags that contain calendar, hour cycle, or numbering system information. This structure allows developers to work with the fundamental language identifier while providing the flexibility to manage specific locale modifications through distinct property settings.


## baseName vs. toString Method

The `baseName` property and `toString` method both process locale identifiers, but the `baseName` property returns a simplified version without extension tags. This distinction becomes particularly important when working with locales that have specific calendar, hour cycle, or numbering system settings.

For example, consider creating a Korean locale with script "Kore" and region "KR". The resulting locale would have the identifier "ko-Kore-KR". However, when we call the `baseName` property on this locale, it returns "ko-Kore-KR" - effectively stripping away any extension tags, including information about calendar type, clock type, and numbering system type.

In contrast, when we use the `toString` method on the same Korean locale, we get "ko-Kore-KR-u-kf-upper-kn". This output demonstrates that the `toString` method includes all available extension tags, providing a complete representation of the locale identifier.

The `baseName` property implementation operates within the structured framework of Unicode locale identifier subtags. It focuses on extracting the language, script, and region information while ignoring extension tags that contain specific locale modifications. This behavior aligns with the Unicode language tag structure, where the baseName property specifically targets the language, script, and region subtags, excluding any extension tags that might include calendar, hour cycle, or numbering system information.

The `toString` method, on the other hand, provides an exact string representation suitable for various contexts, including serialization in JSON or as an argument to `Intl` constructors. This full representation includes the base name of the locale, followed by optional parameters in the format `u-ca-calendar-hourCycle-hour12`. For example, when creating a `Locale` instance with the options `hourCycle: "h12", calendar: "gregory",` the `toString` method returns `"fr-Latn-FR-u-ca-gregory-hc-h12"`.

Understanding these differences is crucial for developers working with JavaScript locales. The `baseName` property allows for simplified locale manipulation, while the `toString` method provides complete locale identification information. Proper usage of these properties ensures correct handling of locale data in JavaScript applications, especially when working with complex identifier structures that include calendar, hour cycle, and numbering system information.


## baseName Property Implementation

The baseName property implementation processes Unicode locale identifier subtags to extract language, script, and region information. This extraction process occurs through several key steps defined in the Unicode Language and Locale Identifiers grammar.

When creating a locale identifier, the process begins by determining whether it contains a Unicode locale extension sequence. If present, the system extracts the extension sequence and parses its components, including attributes and keywords. These components are then subjected to option application and canonicalization procedures, with all locale extensions removed before constructing a new Unicode BCP 47 U Extension.

For locales without an extension sequence, the process initializes attributes and keywords as empty lists before parsing the tag according to the Unicode locale ID production. It extracts the Unicode script subtag (if present) and the Unicode region subtag, storing these components in the result while maintaining the canonicalized tag.

The implementation specifically handles the `language ["-" script] ["-" region] *("-" variant)` subsequence of the Unicode BCP 47 grammar. This extraction mechanism ensures that only the first occurrence of each attribute or keyword is returned, with appropriate handling for subtags that have specific length requirements or conditions.

The baseName property returns this extracted information as a substring of the complete data string, representing the core locale identifier without region or calendar specifications. For example, creating a Korean locale with script "Kore" and region "KR" results in "ko-Kore-KR" when calling the baseName property.

This implementation aligns with the ECMAScript 2026 Internationalization API Specification and provides a standardized approach to extracting core locale information while preserving script and region specifications. The resulting baseName representation serves as the foundation for locale manipulation and comparison in JavaScript applications, enabling developers to work with fundamental language identifiers while managing specific locale modifications through distinct property settings.

