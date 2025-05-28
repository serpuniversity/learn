---

title: JavaScript Intl API: A Comprehensive Guide

date: 2025-05-26

---


# JavaScript Intl API: A Comprehensive Guide

Developing software that works seamlessly across different languages and regions requires careful consideration of internationalization and localization. The JavaScript Intl API provides robust tools for handling these complexities, from date and number formatting to string comparison and pluralization. This guide explores the key features of the Intl API, demonstrating how developers can create more inclusive applications that adapt to user preferences and locale requirements. Through practical examples, we'll see how to use the API for tasks like language-sensitive sorting, accurate number formatting, and handling plural and ordinal forms across multiple languages.


## Overview of the JavaScript Intl Object

The JavaScript Intl object offers a powerful set of tools for internationalization and localization, supporting applications that need to accommodate diverse global audiences. It provides four primary constructors: Intl.DateTimeFormat, Intl.NumberFormat, Intl.Collator, and Intl.ListFormat, each designed to handle specific formatting and comparison tasks.


### Locale Handling and Normalization

The `Intl` object manages locale data through the `Locale` constructor, which can be instantiated using language tags or options. The `Locale` object's properties include:

- `calendar`, which groups days into years, months, and weeks and assigns names (example: "2022-01-01" becomes "28 Tevet 5782" in Hebrew)

- `hourCycle`, which determines 12-hour/24-hour format and smallest hour number (0 or 1)

- `numberingSystem`, which transforms numbers into locale-specific notation (default is `latn` for Latin)

- `caseFirst`, which determines sorting order (uppercase, lowercase, or ignore)

- `numeric`, which determines sorting method (numbers or strings)

- `collation`, which defines the generic collation algorithm (e.g., German `phonebk` treats "Ã¤" as "ae")

Locale normalization is handled by the `Intl.getLocale()` method, which returns the normalized locale or null if no known locale was found. It normalizes the locale string to ensure consistent interpretation across implementations.


### Locale Change Management

The `Intl.onLocaleChange` function allows developers to register callback functions that receive notifications whenever the locale changes. This is particularly useful in applications where content or behavior needs to adapt based on the user's locale preference. The method returns a handler with a `remove()` method to stop listening for locale changes.


### Message Bundle Support

For localization, the Intl API includes a message bundle loader system. The `Intl.registerMessageBundleLoader` method allows developers to provide custom loaders or use the convenience method `createJSONLoader` to fetch translation files. These loaders enable applications to dynamically load language-specific resources based on the selected locale.

The text also mentions the `Intl.resolvedOptions` method, which computes the final locale and formatting options during the initialization of objects like `Intl.Collator` and `Intl.DateTimeFormat`. Additionally, the `Intl.supportedLocalesOf` method helps determine which locales are supported for specific formatting operations.


### Implementation and Browser Support

The Intl API is built into modern browsers and Node.js environments, providing a consistent foundation for internationalization tasks. While the API handles most common formatting requirements, developers should be aware of its current limitations and consider third-party libraries for more specialized use cases. The API's growing maturity indicates its evolving role in JavaScript development, particularly for applications targeting global audiences.


## Number Formatting with the Intl.NumberFormat Constructor

The Intl.NumberFormat constructor enables language-sensitive number formatting, supporting multiple formatting options and locale-specific conventions. It handles various number formats, including currencies, percentages, and scientific notation, with options for minimum and maximum fraction digits, digit grouping, and significant digits.

Common formatting options include:

- Numbering system: affects digit characters (e.g., Chinese, Arabic, Roman)

- Locale-specific conventions: decimal symbol, digit grouping, exponential notation

- Currency formatting: applies specific currency symbols and rounding rules

- Unit formatting: applies translated unit names

- Style options: "decimal", "percent", "currency", "unit"

The constructor accepts inputs as numbers, strings, or BigInt values, handling large or small numbers that exceed JavaScript's number precision. It supports multiple formatting notations, including scientific, engineering, and compact forms with short and long display options.

The API provides extensive configuration options for number formatting:

- `minimumIntegerDigits`: minimum number of integer digits

- `minimumFractionDigits`: minimum number of fractional digits

- `maximumFractionDigits`: maximum number of fractional digits

- `minimumSignificantDigits`: minimum number of significant digits

- `notation`: "scientific", "engineering", "compact"

For example, the following code demonstrates formatting with different options:

```javascript

const results = [];

for (const options of [

  { style: "decimal" },

  { style: "percent" },

  { style: "currency", currency: "USD" },

  { style: "unit", unit: "meter" }

]) {

  const nf = new Intl.NumberFormat("en-US", options);

  results.push({ style: options.style, output: nf.format(1234567.89) });

}

console.table(results);

```

This yields the following formatted outputs:

- 'decimal': '1,234,567.89'

- 'percent': '123,456,789%'

- 'currency': '$1,234,567.89'

- 'unit': '1234567.89 m'

The API also supports compact notation with short and long display options:

```javascript

for (const options of [

  { notation: "scientific" },

  { notation: "engineering" },

  { notation: "compact", compactDisplay: "short" },

  { notation: "compact", compactDisplay: "long" }

]) {

  const nf = new Intl.NumberFormat("en-US", options);

  results.push({ notation: options.compactDisplay ? `${options.notation}-${options.compactDisplay}` : options.notation, output: nf.format(12000) });

}

console.table(results);

```

This produces the following formatted outputs:

- 'scientific' | '1.2E4'

- 'engineering' | '12E3'

- 'compact-short' | '12K'

- 'compact-long' | '12 thousand'

The Intl.NumberFormat constructor supports multiple language and format requirements based on user location. The provided code snippet demonstrates formatting for different locales:

```javascript

function dateFormatter(locale) {

  const numberFormatter = new Intl.NumberFormat(locale)

  const dateFormatter = new Intl.DateTimeFormat(locale)

  const today = new Date()

  const value = 1234.39

  const date = dateFormatter.format(today)

  const number = numberFormatter.format(value)

  console.log(locale, date, number)

}

```

This function demonstrates formatting:

- Number: "1,234.39" (US locale)

- Date: "9/7/2022" (US locale)

- Number: "1.234,39" (ES locale)

- Date: "7/9/2022" (ES locale)


## Date and Time Formatting with Intl.DateTimeFormat

The Intl.DateTimeFormat constructor enables language-sensitive date and time formatting, supporting a wide range of styles and options. It handles various date and time formats with options for minimum and maximum formatting widths, including:

- Date styles: long, medium, short, and numeric

- Time styles: long, medium, short, and abbreviated

- Hour cycle: 12-hour and 24-hour formats

- Time zone: localized time zone names and UTC/GMT offsets

The constructor can format dates and times in multiple languages and styles based on user location. For example:

```javascript

const today = new Date();

const dateFormatter = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' });

const timeFormatter = new Intl.DateTimeFormat('en-US', { timeStyle: 'long' });

console.log("Medium Date:", today.toDateString());

console.log("Long Time:", today.toTimeString());

```

This produces:

- "Medium Date: 9/7/2022"

- "Long Time: 6:14:23 PM"

The API supports detailed formatting options for both dates and times:

- `year`: full year, 2-digit year, or "y" for the last two digits

- `month`: full month name, abbreviated month name, or "M" for numeric value

- `day`: full day name, abbreviated day name, or "d" for numeric value

- `hour`: 24-hour format with leading zero, 12-hour format with AM/PM

- `minute`: leading zero included

- `second`: leading zero included

The constructor also handles different time zone representations:

- Local time

- UTC/GMT offsets

- Named time zones

- Unix timestamps in milliseconds

For custom date/time formats, developers can use the `formatToParts()` method to construct output strings with specific formatting requirements. This allows for complex date/time patterns that go beyond basic style options.


## Plural and Ordinal Formatting

Plural and Ordinal Formatting in JavaScript's Intl API

The Intl API includes powerful plural and ordinal formatting capabilities through the Intl.PluralRules constructor. This object handles complex plural rules across multiple languages, automatically selecting the appropriate grammatical form based on the specified quantity. The constructor requires locale and options parameters, with options including localeMatcher ("lookup" or "best fit", default "best fit") and type ("cardinal" or "ordinal").

Basic usage without specifying a locale returns the default plural form, while locale usage demonstrates language-specific plural rules. For example, the following code illustrates cardinal plural rules in English:

```javascript

const pluralRules = new Intl.PluralRules();

console.log(pluralRules.select(1)); // Output: "one"

console.log(pluralRules.select(2)); // Output: "other"

```

Options usage allows customization of plural results with ordinal indicators. The example below demonstrates selecting the correct ordinal form based on the quantity:

```javascript

const pluralRules = new Intl.PluralRules({ type: "ordinal" });

console.log(pluralRules.select(1)); // Output: "1st"

console.log(pluralRules.select(2)); // Output: "2nd"

```

The constructor supports selecting plural forms based on quantity while handling different languages with specific plural rules. The text emphasizes that while this functionality is less widely applicable than some other Intl methods, it remains valuable for developers working with international applications.

The API also provides comprehensive support for managing ordinals, including the correct use of ordinal indicators in various languages. The following code snippet demonstrates formatting an array of strings according to Swedish language rules:

```javascript

const characters = ["a", "z", "Z", "a"];

const collator = new Intl.Collator("sv");

const sortedCharacters = characters.sort(collator.compare);

console.log(sortedCharacters); // Output: ['a', 'z', 'Z', 'a']

```

The implementation handles complex cases, such as the English language where plural rules are particularly intricate. While the API may not cover every edge case, it provides a solid foundation for developers working with international applications that require accurate plural and ordinal formatting.


## String Comparison and Sorting with Intl.Collator

The Intl.Collator object enables language-sensitive string comparison and sorting, supporting a wide range of languages and sorting rules. It automatically handles complexities such as diacritics and local sorting conventions, ensuring accurate results for applications that need to sort or compare textual data.

For example, the following code demonstrates sorting an array of strings according to Swedish language rules:

```javascript

const characters = ["a", "z", "Z", "a"];

const collator = new Intl.Collator("sv");

const sortedCharacters = characters.sort(collator.compare);

console.log(sortedCharacters); // Output: ['a', 'z', 'Z', 'a']

```

This capability is particularly valuable when working with data from different cultures or languages, where standard sorting algorithms may produce incorrect results due to specific sorting rules. For instance, German has distinct phonebook and dictionary sorting rules, with the phonebook order emphasizing sound while the dictionary order ignores umlauts except for differing words.

The API also supports detailed configuration options for sorting behavior. Developers can customize sorting through options such as sensitivity to case and treatment of undefined values. For example:

```javascript

const options = { sensitivity: 'base', caseFirst: 'upper' };

const collator = new Intl.Collator('en', options);

const words = ['apple', 'banana', 'Apple'];

words.sort(collator.compare);

console.log(words); // Output: ['Apple', 'apple', 'banana']

```

This configuration demonstrates case-insensitive comparison while prioritizing uppercase letters.

The Intl API's sort functionality extends beyond simple string comparison to support complex data structures and use cases. For instance, it can be used to sort arrays of objects based on specific properties:

```javascript

const items = [

  { name: "banana", quantity: 2 },

  { name: "apple", quantity: 1 },

  { name: "banana", quantity: 1 }

];

items.sort((a, b) => a.name.localeCompare(b.name));

console.log(items); // Output: [{ name: "apple", quantity: 1 }, { name: "banana", quantity: 1 }, { name: "banana", quantity: 2 }]

```

This demonstrates sorting based on object properties, showcasing the API's versatility in handling structured data.

The Intl.Collator object is part of a larger set of language-sensitive tools provided by the JavaScript Intl API. Together, these tools enable developers to create applications that provide accurate and culturally sensitive sorting and comparison capabilities, simplifying the process of internationalization and localization.

