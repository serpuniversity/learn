---

title: JavaScript Collator: Locale-Specific String Comparison

date: 2025-05-26

---


# JavaScript Collator: Locale-Specific String Comparison

JavaScript's Intl.Collator brings locale-sensitive string comparison to web development, handling everything from German names to Japanese characters with ease. This introduction explores how to use the Collator constructor to create language-aware comparators, the methods that power precise string ordering, and the options that let you tailor comparisons to your needs. You'll learn how to sort German names correctly and handle mixed-script inputs, all while understanding the performance optimizations that make large-scale sorting efficient and reliable.


## Collator Constructor

The Intl.Collator() constructor creates a locale-aware string comparator that supports various options for customizing string comparison behavior. It provides a flexible foundation for implementing language-sensitive string operations in JavaScript.

The constructor accepts two parameters: a locales specification and an options object. The locales parameter can be a string with a BCP 47 language tag or an array of such strings, defaulting to the runtime's default locale if undefined is passed. The options object allows specifying detailed collation behavior through multiple properties:

- usage: Defines the comparison purpose as either "sort" (default) or "search"

- localeMatcher: Specifies the locale matching algorithm ("lookup" or "best fit"; default "best fit")

- sensitivity: Sets the string comparison sensitivity level (default "primary")

- numeric: Enables numeric collation behavior (default false)

The constructor performs internal locale matching to determine the appropriate collation rules, falling back to the runtime's default locale when necessary. This flexible configuration allows developers to tailor string comparison behavior to specific localization requirements while maintaining consistency across locales.

For example, a developer working with German names and Japanese characters might use the following configuration:

```javascript

new Intl.Collator('de-DE', {

  usage: 'sort',

  sensitivity: 'base',

  numeric: true

})

```

This setup ensures that numeric values are sorted correctly and that base characters take precedence in comparisons, allowing the collator to handle mixed script inputs reliably.


## Collator Methods

The Collator object provides three key methods for implementing language-specific string comparison: compare, getComparator, and sortKey.

The compare() method evaluates two strings according to the collator's rules and returns a negative number if the first string precedes the second, a positive number if it follows, or zero if they are equivalent. This core functionality enables precise control over string ordering while abstracting away complex collation rules. For example, the method correctly handles character sequences with diacritical marks and numeric strings:

Example 1: Array Sorting

```javascript

const a = ["Offenbach", "Österreich", "Odenwald"];

const collator = new Intl.Collator("de-u-co-phonebk");

a.sort(collator.compare);

console.log(a.join(", ")); // "Odenwald, Österreich, Offenbach"

```

Example 2: Array Searching

```javascript

const a = ["Congrès", "congres", "Assemblée", "poisson"];

const collator = new Intl.Collator("fr", { usage: "search", sensitivity: "base" });

const s = "congres";

const matches = a.filter((v) => collator.compare(v, s) === 0);

console.log(matches.join(", ")); // "Congrès, congres"

```

The getComparator() method returns a bound comparator function compatible with JavaScript's Array.sort() method, while maintaining the same locale-specific behavior. This function generates the same sorted order as the standalone compare() method, allowing developers to integrate locale-aware sorting into existing data structures:

Example: Custom Sorting Function

```javascript

var arr = ["ö", "oe", "ü", "o", "a", "ae", "u", "ß", "ä"];

var collator = new Collator({locale: 'de-DE', style: "dictionary"});

arr.sort(collator.getComparator());

console.log(JSON.stringify(arr)); // ["a", "ae", "ä", "o", "oe", "ö", "ß", "u", "ü"]

```

The sortKey() method generates a sort key string representing the character collation values according to the algorithm and options. This string allows direct comparison of generated keys, maintaining consistent ordering between identical collator instances while preventing inconsistencies across different collator implementations. The sort key functionality enables efficient sorting of string arrays without requiring repeated rule evaluation:

Example: JavaScript Implementation

```javascript

const collator = new Intl.Collator("example");

console.log(collator.sortKey("abc")); // "abc"

console.log(collator.sortKey("ábc")); // "ábc"

console.log(collator.sortKey("aábc")); // "áabc"

console.log(collator.sortKey("áaábc")); // "áaabc"

```

This approach ensures reliable string comparison across various scripts and collation styles while optimizing performance through precomputed key values.


## Collation Options

The Collator constructor accepts various options that govern string comparison behavior. These options allow developers to tailor the collation process to specific localization requirements while maintaining consistency across locales.


### Sensitivity Levels

The sensitivity option determines the level of character comparison sensitivity. The available values are:

- "base": Only primary distinctions significant (default for "search")

- "accent": Both primary and secondary distinctions significant

- "case": Secondary distinctions significant, plus case sensitivity

- "secondary": Both primary and secondary distinctions significant

- "tertiary": Primary, secondary, and tertiary distinctions significant

- "variant": All distinctions significant (default for "sort")


### Usage Types

The usage option specifies whether the collator will be used for searching or sorting. The supported values are:

- "sort": Default value, requires stable results (order independent of input array)

- "search": Requires matching strings differing only by case


### Additional Options

The constructor also supports several other options:

- ignorePunctuation: Boolean flag to skip punctuation characters during comparison (default false)

- numeric: Boolean flag to treat strings as starting with numbers for sorting (default false)

- caseFirst: Determines whether upper-case characters should come first in case-sensitive comparisons. The supported values are "upper", "lower", or "false" (default locale's default)

- onLoad: Callback function for loading locale data, using ilib loader callback (requires onLoad option for preassembled data)

- sync: Boolean flag controlling loading behavior (default true for native implementation)

- _loadParams: Custom parameters for loader callback

- _useNative: Boolean flag to use native Intl object if available (default true)


### Implementation Notes

While the constructor accepts a wide range of options, not all properties are required to be supported by implementations. The caseFirst and numeric properties, in particular, are noted as not being required by the specification. Browser compatibility varies, with the feature being widely available across modern devices and versions since September 2017.


## Collator Performance

Collator instances generate sort keys that maintain consistent ordering across identical options, enabling efficient large-scale sorting. This functionality ensures that while multiple collator instances may differ in behavior, those with the same options produce equivalent sort keys.

The sortKey method generates a three-number string representing primary, secondary, and tertiary character characteristics, adjusted according to the collator's strength. These byte-for-byte comparable keys allow efficient array sorting without repeated rule evaluation, though different collator implementations may produce inconsistent results.

For optimal performance with large datasets, the recommendation is to use sort keys for 10 or more items or when arrays might be resorted arbitrarily. For extensive data handling, the guidance suggests implementing server-side sorting, particularly for database query results, where cursors enable efficient on-database sorting.

The character handling approach varies based on script usage:

- Full multilingual data requires loading the full collation data, implementing the Unicode Collation Algorithm (UCA) based on the Default Unicode Collation Element Table (DUCET), which is necessary for multilingual sorting but provides multiple megabytes of data.

- For limited script sets, include specific ISO 15924 script codes, with each script having its own data file.

- Single-script text can rely on locale-specific collation data, using "!data collate" to load locale-specific data for the most common script, ensuring correct sorting for the primary script while applying default UCA rules for other scripts in the DUCET.

The collator handles characters without collation data by sorting them by pure Unicode value after processing characters with available data. This approach ensures consistency in string ordering while supporting a wide range of script handling requirements.


## Collator Browser Support

The Collator object is widely available across modern browsers and platforms, although implementation details vary between versions and engines. Full support includes Chrome 24+ and later versions, Edge 12+, Firefox 29+, Opera 15+, Safari 10+, and their mobile counterparts. The functionality is also implemented in Android Chrome 25+, Android Firefox 56+, Android Opera 14+, Samsung Internet 1.5+, and Node.js with the '--with-intl' option.

Before version 13, browser implementations limited default locale availability to 'en-US', requiring Node.js with the ICU data flag or manually loaded locale data for full support. As of version 13, browsers utilize the native Intl object if available, though this is configurable through the constructor's _useNative option.

The constructor accepts two primary parameters: a locales specification and an options object. The locales parameter follows BCP 47 language tags and supports both single and array inputs, defaulting to the runtime's default locale if undefined. The options object enables detailed customization through properties including usage, localeMatcher, sensitivity, numeric, and caseFirst, though browser support for numeric and caseFirst is not universal.

Browser compatibility varies, with some implementations requiring specific flags or versions to access full collator functionality. The recommended approach for cross-browser string comparison involves creating collator instances with explicit options rather than relying on default behavior. This ensures consistent string ordering across different environments while providing the flexibility needed for language-specific sorting requirements.

