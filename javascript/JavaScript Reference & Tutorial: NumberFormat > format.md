---

title: JavaScript Number Formatting with Intl.NumberFormat

date: 2025-05-26

---


# JavaScript Number Formatting with Intl.NumberFormat

JavaScript's Intl.NumberFormat provides powerful language-sensitive number formatting capabilities through its constructor and options object. While its basic usage returns formatted strings in the default locale, the truly impressive functionality emerges when customizing formatting through its extensive options for currency, unit, and significant digit control. This article delves into NumberFormat's intricacies, from its fundamental usage patterns to advanced features like range formatting and locale-specific customization. Whether you're displaying monetary values, scientific notation, or simple integers, this comprehensive guide covers everything you need to know about locale-aware number formatting in JavaScript.


## NumberFormat Basics

The Intl.NumberFormat object enables language-sensitive number formatting through its constructor, which accepts an optional locales parameter and options object. The locales parameter can be a BCP 47 language tag or an array of such tags, with the runtime's default locale used as a fallback if none of the specified locales are supported. The options object allows customization of formatting through properties grouped into locale options, style options, digit options, and other options.


### Basic Usage

The basic usage of NumberFormat without specifying a locale returns a formatted string in the default locale with default options. For example:

```javascript

const number = 3500;

console.log(new Intl.NumberFormat().format(number)); // '3,500'

```


### Supported Locales

The NumberFormat object determines supported locales through its supportedLocalesOf method, which returns an array of locales supported without falling back to the runtime's default locale. This method takes an array of locale identifiers and returns those that are supported.

When requesting a language not supported by the runtime, a fallback language can be included. For example, using both "ban" (Balinese) and "id" (Indonesian) as fallbacks:

```javascript

console.log(new Intl.NumberFormat(["ban", "id"]).format(number)); // 123.456,789

```

The constructor supports several usage patterns:

- `Intl.NumberFormat()`

- `Intl.NumberFormat(locales)`

- `Intl.NumberFormat(locales, options)`


### Number Formatting Options

The NumberFormat object provides properties to control formatting behavior:

- `minimumFractionDigits`: Determines the minimum number of decimal places, with a default value of 0 for percent formatting. This property is calculated as the larger of the specified value and the number of minor unit digits from the ISO 4217 currency code list (2 if not provided).

- `minimumSignificantDigits`: Specifies the minimum number of significant digits, with valid values ranging from 1 to 21 and a default of 1.

- `maximumSignificantDigits`: Sets the maximum number of significant digits, with valid values ranging from 1 to 21 and a default equal to `minimumSignificantDigits`.

These properties can be customized when creating a new NumberFormat instance, allowing for precise control over the formatted output.


## Format Method Details

The format method returns a getter function that applies number formatting according to the locale and formatting options of the NumberFormat object. This getter function can be invoked with a number to produce a formatted string, or it can be directly accessed as a property of the NumberFormat instance.


### Basic Usage

The format method can be used directly on a NumberFormat instance to convert numbers into formatted strings. For example:

```javascript

const number = 123456.789;

const formatter = new Intl.NumberFormat("de-DE");

console.log(formatter.format(number)); // Expected output: "123.456,789"

```


### Using Options

Options can be passed to the format method to customize the output. For example:

```javascript

const formatter = new Intl.NumberFormat("en-IN", { maximumSignificantDigits: 3 });

console.log(formatter.format(123456.789)); // Expected output: "1,23,000"

```


### Error Handling

If the input is not a valid number or string, or if the string cannot be parsed, the method returns an empty string. This behavior is consistent across supported browsers and devices, though the exact string returned may vary.


### Range Formatting

The format method can also handle number ranges by accepting two parameters: startRange and endRange. This functionality requires the latest browser versions, with support available since August 2023.


### Browser Support

The format method is widely supported across modern browsers and devices, with consistent behavior across implementations. For optimal results when formatting large numbers, it's recommended to create a NumberFormat instance and use the format getter function rather than calling toLocaleString directly.


## Formatting Options

NumberFormat supports comprehensive options for currency, unit, and significant digit formatting. The style parameter determines the type of formatting, with options including "currency," "percent," and "unit." When using currency formatting, the style parameter requires the currency parameter to be set to an ISO 4217 currency code, which is normalized to uppercase.

The number formatting system can be customized through several properties:

- Minimum and maximum integer digits control the number of digits displayed before the decimal point.

- Minimum and maximum fraction digits set the number of digits displayed after the decimal point.

- Minimum significant digits limit the total number of significant digits in the formatted output.

Additional formatting options include:

- Notation styles: "engineering," "compact," "long," and "short"

- Currency display formats: "code," "symbol," "narrowSymbol," and "name"

- Grouping separators for large numbers

- Rounding modes for decimal places

- Digit grouping based on locale preferences

The formatting options object can be extended with custom parameters, such as the numbering system through the Unicode extension key `nu`. This enables localization of number formatting beyond the default decimal system, supporting various script-based number representations.


## Locale-Specific Formatting

The constructor requires a locale string or an array of locale identifiers, with the runtime's default locale used as a fallback if none of the specified locales are supported. This initialization parameter determines the language-sensitive formatting behavior of the NumberFormat object.

When specifying multiple locales, the system performs implicit locale matching to find the most appropriate format settings. The algorithm balances between "lookup" (exact match) and "best fit" (closest match) strategies, depending on the options provided. For instance, the `supportedLocalesOf` method demonstrates that while Indonesian and German are directly supported, Balinese input selects the closest available match (in this case, Indonesian).

Options can be specified through the `numberingSystem` property or the options object, allowing for precise control over number representation beyond the default decimal system. This capability supports localization requirements for languages that use distinct number scripts, such as Arabic numerals or traditional Chinese number systems.


## Range Formatting

The formatRange and formatRangeToParts methods of the Intl.NumberFormat object enable advanced number formatting for ranges, with browser compatibility available since August 2023. Both methods require two parameters: startRange and endRange, which must be defined numeric values. If either parameter is undefined, a TypeError is thrown.

The formatRange method produces a localized string representing the range, while formatRangeToParts returns an array of objects representing the formatted range parts. Each object contains three properties: type (indicating the data type), value (the specific value), and source (indicating whether the value comes from startRange or endRange).

For example, to format the range from 123456.789 to 234567.890, you would use:

```javascript

const formatter = new Intl.NumberFormat("de-DE");

console.log(formatter.formatRange(123456.789, 234567.890)); // Expected output: "123.456,789 - 234.567,890"

```

The output of formatRangeToParts breaks down each element of the formatted range:

```javascript

const parts = formatter.formatRangeToParts(123456.789, 234567.890);

console.log(parts); // Array of objects with type, value, and source properties

```

This detailed formatting capability allows developers to create locale-aware number range displays while maintaining control over the composition of the final string. The system handles various edge cases, including when start and end numbers are equivalent, in which case the output behaves similarly to calling formatToParts on the start number with all tokens marked as source: "shared".

