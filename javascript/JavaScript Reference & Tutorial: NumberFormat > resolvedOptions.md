---

title: Intl.NumberFormat.resolvedOptions Method

date: 2025-05-26

---


# Intl.NumberFormat.resolvedOptions Method

Web developers working with internationalized numbers face a complex landscape of formatting requirements and regional variations. The Intl.NumberFormat API streamlines this process through its locale-aware number formatting capabilities, but mastering its intricacies requires a deep dive into its inner workings. This article explores the resolvedOptions method, which reveals the detailed configuration of a NumberFormat instance. From locale selection to rounding behavior, we'll uncover the precise mechanics that determine how numbers are displayed across different cultures and applications. Whether you're building global financial tools or localizing user interfaces, understanding these fundamental mechanisms will help you deliver accurate and culturally appropriate number formatting across devices and platforms.


## Method Overview

The resolvedOptions method returns an object containing the locale and formatting options computed during the initialization of an Intl.NumberFormat object. The object includes several key properties:

locale: The BCP 47 language tag for the locale actually used, with Unicode extension values included if requested and supported.

numberingSystem: The value requested using the Unicode extension key "nu" or filled in as a default.

style: Contains useGrouping properties, which are the values provided in the options argument or filled in as defaults.

currency: Contains currencyDisplay properties, which are the values provided in the options argument or filled in as defaults. These properties are only present if style is "currency".

minimumIntegerDigits, minimumFractionDigits, maximumFractionDigits: These properties are present only if neither minimumSignificantDigits nor maximumSignificantDigits was provided in the options argument. Their values are the ones provided in the options argument or filled in as defaults.

minimumSignificantDigits, maximumSignificantDigits: These properties are present only if at least one of them was provided in the options argument. Their values are the ones provided in the options argument or filled in as defaults.

Additional properties include:

- numberingSystem: "latn" (default for "de-DE" locale)

- locale: "de-DE" (locale of the NumberFormat instance)

- compactDisplay: undefined (not set)

- signDisplay: "auto" (default)

- roundingIncrement: 1 (default)

- roundingMode: "halfExpand" (default)

- roundingPriority: "auto" (default)

- trailingZeroDisplay: "auto" (default)

This method provides comprehensive details about the number formatting options in use, allowing developers to understand and programmatically access the configuration applied to their number formatting objects.


## Resolved Options Properties

The resolvedOptions method returns an object with properties reflecting the locale and number formatting options computed during the initialization of an Intl.NumberFormat object. The object includes several key properties such as locale, numberingSystem, style, currency, and formatting digits.

The locale property represents the BCP 47 language tag for the locale actually used, with Unicode extension values included if requested and supported. The numberingSystem property indicates the value requested using the Unicode extension key "nu" or filled in as a default. The style property contains useGrouping properties, which are the values provided in the options argument or filled in as defaults.

The currency property is present only if the style is "currency" and contains currencyDisplay properties, which are the values provided in the options argument or filled in as defaults. The minimumIntegerDigits, minimumFractionDigits, and maximumFractionDigits properties are present only if neither minimumSignificantDigits nor maximumSignificantDigits was provided in the options argument. Their values are the ones provided in the options argument or filled in as defaults. MinimumSignificantDigits and maximumSignificantDigits properties are present only if at least one of them was provided in the options argument, with their values being the ones provided in the options argument or filled in as defaults.

Additional properties include:

- numberingSystem: "latn" (default for "de-DE" locale)

- locale: "de-DE" (locale of the NumberFormat instance)

- compactDisplay: undefined (not set)

- signDisplay: "auto" (default)

- roundingIncrement: 1 (default)

- roundingMode: "halfExpand" (default)

- roundingPriority: "auto" (default)

- trailingZeroDisplay: "auto" (default)

The method returns comprehensive details about the number formatting options in use, allowing developers to understand and programmatically access the configuration applied to their number formatting objects. The resolvedOptions method is supported in Chrome 24, Edge 12, Firefox 29 (29), Internet Explorer 11, Opera 15, and Safari 10, making it widely available across modern browsers.


## Rounding and Significant Digits

Rounding and significant digits in JavaScript's NumberFormat follow specific rules to handle fractional and significant values. The rounding priority determines how conflicts between minimumFractionDigits and minimumSignificantDigits are resolved. The available rounding priority modes include auto, morePrecision, and lessPrecision, with auto defaulting to significant digits when both are set.

The roundingIncrement property allows rounding to specific increments, with constraints requiring values between 1 and 5000 that evenly divide 10, 100, 1000, or 10000 into tenths, fifths, quarters, or halves. For example, setting maximumFractionDigits to 2 and roundingIncrement to 5 results in rounding to the nearest 0.05, while setting it to 10 enables dime rounding.

Rounding modes determine how values are formatted with options including ceil, floor, expand, trunc, halfCeil, halfFloor, halfExpand, halfTrunc, and halfEven. These modes behave differently based on the magnitude of the number: "halfEven" behaves like "halfTrunc" when numbers are between 2.2 and 2.3, while for values between -2.3 and -2.4, it behaves like "halfExpand". This behavior ensures more intuitive rounding outcomes by avoiding consistent over- or under-estimation of half-increments.

The significant digits properties interact closely with round types. When using significant digits rounding, the number of fraction digits must match, and rounding increment cannot be combined with significant digit settings. The rounding type is automatically set based on priority or significant digit presence, with minimum and maximum fraction digits constrained to 0-20 and minimum and maximum significant digits to 1-21, respectively.

The trailingZeroDisplay property controls whether trailing zeros are removed when formatting numbers as integers, with options set to auto by default and stripIfInteger available for explicit control. Together, these features enable flexible and precise number formatting based on specific application requirements.


## Browser Support and Implementation

The resolvedOptions method of the Intl.NumberFormat object returns an object containing the computed options for number formatting, with properties specific to locale and formatting rules. The properties represent the configuration applied during the initialization of the NumberFormat object, reflecting the actual locale used and the formatting options set.


### Implementation Across Browsers

Browser support for the resolvedOptions method has evolved over time, with significant improvements in recent years. Initially, support was limited, particularly in Internet Explorer, which provided no support. The method began to see widespread implementation in major browsers starting in September 2017.

As of the latest specifications, the method is supported across all modern browsers:

- Chrome: Full support since version 24

- Edge: Full support since version 12

- Firefox: Full support since version 29

- Opera: Full support since version 15

- Safari: Full support since version 10

- WebView Android: Full support since version 4.4

- Chrome Android: Full support since version 25

- Firefox Android: Full support since version 56

- Opera Android: Full support since version 14

- Safari iOS: Full support since version 10

- Samsung Internet Android: Full support since version 1.5


### Default Behavior and Configuration

The method returns an object with default values for properties not explicitly configured when creating the NumberFormat instance. These defaults vary based on the specified locale and the properties provided in the options argument. For example, the default numbering system for the "de-DE" locale is "latn", while the default minimum and maximum fraction digits are 0 and 100, respectively.

The method consistently returns the locale as "de-DE" for the NumberFormat instance, with additional properties including:

- numberingSystem: "latn"

- compactDisplay: undefined

- currency: "USD"

- currencyDisplay: "symbol"

- currencySign: "standard"

- minimumIntegerDigits: 1

- minimumFractionDigits: 2

- maximumFractionDigits: 2

- roundingIncrement: 5

- roundingMode: "halfCeil"

- roundingPriority: "auto"

- signDisplay: "auto"

- style: "currency"

- trailingZeroDisplay: "auto"

This stable implementation across browsers allows developers to reliably access detailed formatting options through the resolvedOptions method, supporting precise number formatting requirements.


## Customization Options and Defaults

The resolvedOptions method returns detailed configuration information about the number formatting options in use, including properties for locale, numbering system, style, currency, and formatting digits. Beyond these basic properties, the method also exposes advanced formatting controls through properties like significant digits, minimum and maximum fraction digits, and rounding behavior.

The method supports multiple notation styles for number formatting, including standard, scientific, engineering, and compact notations. The compact notation can be used with display options that vary the level of detail based on the number's magnitude. For currency formatting, the method includes options for displaying the currency symbol, code, or name and supports accounting display modes that use parentheses or standard minus signs for negative values.

Additional properties control rounding behavior through settings for significant digits, fraction digits, and rounding modes. The rounding modes include options for ceiling, flooring, expanding, truncating, and various half-rounding methods that determine how numbers are formatted to the nearest significant digit or fraction value. This comprehensive rounding control allows precise tailoring of number display based on specific application requirements.

The method also manages the display of fractional digits through properties that define minimum and maximum values. These properties interact with significant digits settings to ensure consistent formatting across different numerical scales. The maximumDigits property constraints are enforced to prevent overly complex number representations, with valid values ranging from 1 to 20 for minimum digits and 1 to 21 for significant digits.

The formatting options include detailed controls for integer and fraction digit display, with minimum and maximum properties that define the number of digits to be shown. These properties work together with significant digits settings to ensure that numbers are displayed in a readable and logical manner. The resolvedOptions method consistently returns these properties with default values that vary based on the specified locale and formatting options, providing a reliable foundation for understanding and controlling number formatting behavior.

