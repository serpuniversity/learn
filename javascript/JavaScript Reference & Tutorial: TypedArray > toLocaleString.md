---

title: JavaScript TypedArray toLocaleString Method

date: 2025-05-27

---


# JavaScript TypedArray toLocaleString Method

JavaScript TypedArrays provide efficient ways to handle binary data, but sometimes you need to convert that raw data into human-readable strings. The toLocaleString() method offers a powerful solution, allowing you to format typed array elements based on locale-specific conventions. Whether you're building international applications or working with numeric data, understanding this method's behavior and options will help you create more flexible and user-friendly JavaScript applications. This guide covers everything you need to know about using toLocaleString() with TypedArrays, from basic usage to advanced formatting options.


## toLocaleString() Method Overview

The toLocaleString() method of TypedArray instances returns a string representing the elements of the typed array, with elements converted to strings using their toLocaleString methods and separated by locale-specific characters. This method shares the same algorithm as Array.prototype.toLocaleString() and follows the same behavior for number elements as Number.prototype.toLocaleString().

The method accepts two optional parameters: locales and options. The locales parameter customizes the method's behavior using BCP 47 language tags, while the options parameter allows specifying additional formatting options such as style and currency. The method's implementation may ignore these parameters, in which case the locale used and the string format returned are determined by the host environment.

When called without parameters, the method converts typed array elements to strings based on the system's default locale and separator. For example, a new Uint32Array [100, 897, 123, 132, 22] returns "100, 897, 123, 132, 22" when called with no arguments.

The method supports locale-specific formatting for both number and string elements. For instance, passing the 'hi' locale and currency options formats the array elements using the Indian Rupee symbol: [4023, 6123, 30, 146].toLocaleString('hi', { style: 'currency', currency: 'HIR' }) results in "HIR 4,023.00, HIR 6,123.00, HIR 30.00, HIR 146.00".


## Method Parameters

The toLocaleString() method of TypedArray instances accepts two optional parameters: locales and options. The locales parameter customizes the method's behavior using BCP 47 language tags, allowing developers to specify the language whose formatting conventions should be used. The options parameter allows for additional formatting options, though its specific configuration properties depend on the underlying browser or JavaScript implementation.

When no parameters are provided, the method converts typed array elements to strings based on the system's default locale and separator. This behavior aligns with the host environment's settings, making it particularly useful for applications requiring locale-sensitive string representations.

The method's implementation may ignore the locale and options parameters, defaulting to the host environment's locale and formatting conventions. This flexibility allows developers to produce localized string representations while maintaining compatibility across different runtime environments.

For example, creating a new Uint32Array [100, 897, 123, 132, 22] and calling toLocaleString() with no arguments results in "100,897,123,132,22". When formatting is required, passing the 'hi' locale and currency options produces Indian Rupee symbols: [4023, 6123, 30, 146].toLocaleString('hi', { style: 'currency', currency: 'EUR' }) generates "EUR 4,023.00, EUR 6,123.00, EUR 30.00, EUR 146.00".


## locales Parameter

The locales parameter of the toLocaleString() method specifies the language and region for formatting using BCP 47 language tags. When not specified, the method defaults to the system's locale, providing flexibility in localized string representation while maintaining compatibility across different runtime environments.

The parameter accepts either a single BCP 47 language tag string or an array of such strings. For typed array elements that are numbers, the method supports a wide range of numbering systems through the "nu" extension key, with specific values including "arab" for Arabic numerals, "arabext" for extended Arabic numerals, "bali" for Balinese numerals, and "beng" for Bengali numerals. This extension allows developers to format numbers according to specific cultural representation preferences.

When formatting numeric elements, the method supports various numbering systems through the "nu" extension key. Possible values include "arab" for standard Arabic numerals, "arabext" for extended Arabic numerals, "bali" for Balinese numerals, and "beng" for Bengali numerals. This functionality enables precise control over number representation, particularly useful for applications requiring specific numeral systems.

The method's behavior when no locale is specified reflects the host environment's settings, making it particularly useful for applications requiring locale-sensitive string representations. It's important to note that the implementation may ignore the locales parameter, defaulting to the host environment's locale and formatting conventions. However, when supported, this parameter allows developers to produce localized string representations while maintaining compatibility across different runtime environments.


## options Parameter

The options parameter allows for extensive customization of the toLocaleString method's output through various formatting options. Key properties include:

- **localeMatcher**: Determines how locales are matched, with "lookup" matching directly against installed locales and "best fit" selecting the most appropriate match.

- **style**: Defines the formatting style, with options "decimal" (default), "currency", and "percent".

- **currency**: Specifies the currency code for currency formatting (e.g., "EUR", "USD").

- **currencyDisplay**: Determines how currency is displayed (as "symbol", "code", or "name").

- **useGrouping**: Controls the use of grouping separators (thousands/sigfig separators), with "true" (default) or "false".

Additional properties enable precise control over number representation:

- **minimumIntegerDigits**: Sets the minimum number of integer digits (1-21, default 1)

- **minimumFractionDigits**: Sets the minimum number of fraction digits (0-20, default varies by style)

- **maximumFractionDigits**: Sets the maximum number of fraction digits (0-20, default varies by style)

- **minimumSignificantDigits**: Sets the minimum number of significant digits (default varies by style)

For example, to format an array of numbers with German currency conventions, including thousand separators and the currency symbol:

```javascript

let numbers = [1234567.89, 897654.321, 456789.123];

let formatted = numbers.toLocaleString("de-DE", { style: "currency", currency: "EUR" });

console.log(formatted); // Output: 
1.234.567,89 €, 897.654,32 €, 456.789,12 €

```

This configuration produces strings formatted according to German conventions, including the appropriate decimal separator and currency symbol. Developers can use these options to create locale-specific string representations that match their application's requirements.


## Method Behavior

The method follows the same algorithm as `Array.prototype.toLocaleString()` for numbers and `Number.prototype.toLocaleString()` for number elements, converting the elements to strings and separating them with locale-specific characters.


### Default Behavior

When called with no arguments, the method converts the elements of the typed array to strings based on the system's default locale and separator. For example:

```javascript

let geekArray = new Uint32Array([100, 897, 123, 132, 22]);

console.log(geekArray.toLocaleString()); // Output: 100, 897, 123, 132, 22

console.log(geekArray.toLocaleString('en-US')); // Output: 100, 897, 123, 132, 22

console.log(geekArray.toLocaleString('hi', { style: 'currency', currency: 'HIR' })); // Output: HIR 100.00,HIR 897.00,HIR 123.00,HIR 132.00,HIR 22.00

```


### Locale-Specific Formatting

The method supports locale-specific formatting through both the `minimumFractionDigits`, `minimumSignificantDigits`, and `maximumSignificantDigits` options, providing precise control over number representation. For instance, the `maximumSignificantDigits` option determines the number of significant digits used in the formatted string, with a default of 21 and a range of 1-21.


### Browser Support

The method is supported in Chrome 2+ (2008), Firefox 51+ (2017), Internet Explorer 10+ (2011), Opera, Safari, and Edge across desktop, mobile, and webview platforms, with basic support available in Node.js.

