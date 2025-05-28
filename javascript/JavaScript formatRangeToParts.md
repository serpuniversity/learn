---

title: JavaScript NumberFormat: Rounding and Formatting

date: 2025-05-26

---


# JavaScript NumberFormat: Rounding and Formatting

JavaScript's NumberFormat API offers extensive control over numeric formatting, including rounding, notation options, and sign display. This article explores the subtle behaviors of the rounding algorithm, the detailed mechanics of range formatting, and the customizable display options available. Understanding these features is essential for developers working with numerical data in international applications, financial systems, and scientific computations.


## Rounding Algorithms

The rounding modes in JavaScript's NumberFormat behave counterintuitively when minimum values are specified without maximum values, particularly with respect to rounding priority and significant digit calculations. When both minimum and maximum significant digits are unspecified, the algorithm evaluates rounding based on maximum significant and fractional digits alone, leading to unexpected behavior.

Understanding the rounding algorithm requires examining several key properties: roundingPriority, roundingIncrement, minimumFractionDigits, and maximumFractionDigits. By default, rounding priority determines whether the system favors more or less precision. For example, when rounding priority is "morePrecision," the system prioritizes maximum significant digits. However, if notation is "compact" and no FractionDigits or SignificantDigits options are set, rounding mode normalizes to "morePrecision."

The rounding increment allows precise control over rounding intervals, though it cannot be combined with significant-digits rounding or non-auto rounding priorities. The system uses this increment to find the nearest valid value while preserving the specified number of significant or fractional digits. For instance, when rounding to the nearest 5, the system will select the closest multiple of 5, adjusting the number of significant digits as needed.

These mechanisms work together to determine the final formatted value, with the algorithm performing several key steps:

1. Calculating the rounding magnitude based on the specified increment

2. Applying the rounding mode to determine the closest valid value (using ceil, floor, expand, or trunc based on the selected mode)

3. Adjusting the formatted value to ensure it meets both significant and fractional digit constraints

Understanding these internal processes helps developers manage number formatting in JavaScript, particularly when working with financial or scientific applications that require precise control over numerical representation.


## Range Formatting Methods

The `formatRange()` and `formatRangeToParts()` methods of `Intl.NumberFormat` provide detailed control over how number ranges are represented in specific locales. These methods enable precise formatting of numeric ranges according to locale-specific rules and options.


### Basic Usage and Parameters

The methods accept two parameters: `startRange` and `endRange`, which can be numbers, big integers, or strings. Strings are parsed using locale-specific number conversion rules, preserving their exact value without loss of precision during conversion.


### Return Values and Structure

- `formatRangeToParts()` returns an array of objects containing detailed parts of the formatted range. Each object has three properties: `type`, `value`, and `source`.

- The `type` property indicates the part's nature (e.g., "integer", "group", "decimal"), while `value` provides the numeric value of the part.

- The `source` property indicates whether the part belongs to "startRange", "endRange", or is "shared" between both.


### Key Configuration Options

The rounding modes available include:

- ceil: Rounding toward positive infinity

- floor: Rounding toward negative infinity

- expand: Rounding away from zero

- trunc: Rounding toward zero

- halfCeil, halfFloor, halfExpand, halfTrunc: Various tie-breaking rules

- halfEven: Rounding to nearest even integer

The rounding increment parameter determines the intervals for rounding, with valid values including 1, 2, 5, 10, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, 5000. This parameter cannot be used simultaneously with significant-digits rounding or specific rounding priorities.


### Notable Features

When start and end numbers are identical, the output mirrors the result of calling `formatToParts()` on the single number, with all tokens marked as "source: "shared"". The method throws errors for invalid inputs, including `NaN` or non-convertible strings.

The `format()` method serves as the foundation for range formatting, offering extensive customization through various options. This includes control over number notation, currency formatting, unit display, and precision settings.


## Notation Options

Notation options in JavaScript's NumberFormat API provide flexible control over number display styles, including engineering, compact, and scientific notations. These options enable precise formatting tailored to the data's intended use and the user's locale preferences.


### Engineering Notation

Engineering notation displays exponents as multiples of three, making it particularly useful for scientific and technical applications. The notation automatically adjusts the exponent to present numbers in a human-readable format. For example, 987654321 is formatted as 987,654E6, clearly showing the magnitude of the number while maintaining readability.


### Compact Notation

Compact notation simplifies large numbers by using shorter exponent representations. This style is ideal for displaying values in a space-constrained environment or when precise numerical information is less critical than visual clarity. For instance, the number 987654321 is formatted as 9.999999999999999, with the compact exponent "M" indicating millions.


### Scientific Notation

Scientific notation presents numbers using a base ten exponent, suitable for both large and small values. It provides a precise representation of numerical data, making it valuable for scientific calculations and measurements. The notation uses the exponent separator "E" to indicate the power of ten, as demonstrated in 987654321 formatted as 9.87654321E8.


### Display Options

The API offers several options for controlling how numbers are displayed, including:

- **Sign Display**: Options for controlling how positive, negative, and zero values are represented. By default, positive numbers are displayed without a sign, while negative numbers use parentheses. This behavior can be customized through explicit options.

- **Fractional Digits**: Control over the number of digits displayed after the decimal point. The system defaults to 3 for plain numbers and 2 for currency values, allowing developers to adjust precision as needed.

- **Grouping Separators**: Control over the use of grouping separators (commas, periods, etc.) between digits. This property can be enabled or disabled based on the locale requirements.

- **Numbering System**: Support for multiple numbering systems, including Arabic, Bengali, Devanagari, and others, allowing for localization across different cultural contexts.

These options work together to provide comprehensive control over number formatting, enabling developers to create locale-aware applications with precise numerical representation. The API's detailed configuration allows for both simple and complex formatting requirements, from basic number display to specialized scientific notation.


## Sign and Zero Display

NumberFormat objects control sign and zero display through several key properties:


### Sign Display

The `signDisplay` property determines when to display signs for positive, negative, and zero values. Options include:

- auto: Displays signs except for positive values

- always: Always displays signs

- never: Never displays signs

- exceptZero: Displays signs except for zero

- negative: Always displays negative sign


### Zero Display

For zero values, NumberFormat uses the `trailingZeroDisplay` property:

- auto: Keeps trailing zeros based on minimumFractionDigits and minimumSignificantDigits

- stripIfInteger: Removes fraction digits if all are zero (same as "auto" if any fraction digit is non-zero)


### Custom Sign Control

The `formatter.formatToParts()` method can be used to manually control sign display in complex cases. This method returns detailed parts of the formatted number, allowing developers to inspect and potentially customize the output.


### Example Scenarios

The following scenarios demonstrate sign and zero display behavior:

- `formatter.format(0.99999)` should result in '0.9999'

- `formatter.format(0.006393555)` should result in '0.006393'

- `formatter.format(0.9972620384752073)` should result in '0.9972'

- `formatter.format(12345.67)` should result in '12,345.67'

- `formatter.format(200001)` should result in '200,001'

For more precise control, developers can combine `formatToParts()` with custom formatting logic, as recommended in specific use cases.


## Fraction and Significant Digits

The NumberFormat API manages fractional and significant digits through several key properties:


### Rounding Priority and Increment

The rounding priority determines whether the value favors more or less precision. By default, the system uses significant digits unless notation is "compact" and no specific rounding options are set. The rounding increment controls the rounding interval, accepting values 1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, or 5000. This value cannot be combined with significant-digits rounding or specific rounding priorities.


### Rounding Modes

The algorithm supports several rounding modes:

- Default: halfExpand, rounding away from zero at the half-increment

- Options: ceil, floor, expand, trunc, and various half modes (halfCeil, halfFloor, etc.)


### Precision Control

The system calculates minimum and maximum significant digits based on the rounding priority:

- If rounding priority is "auto", minimum significant digits default to 1

- Maximum significant digits and fractional digits default to 21 and 0, respectively

- For "morePrecision" rounding, minimum significant digits default to 1, and maximum remains 21

- For "lessPrecision" rounding, rounding type becomes lessPrecision


### Implementation Details

The process involves multiple conditional checks:

1. Setting default values for minimum integer digits and rounding increment

2. Adjusting minimum and maximum significant digits based on rounding priority

3. Validating rounding increment and determining rounding type


### Notable Behavior

When minimum significant or fractional digits are unspecified, the algorithm evaluates rounding based on both significant and fractional digit constraints. This can lead to unintuitive behavior when only minimum values are specified without maximums. The working group proposes a modification to evaluate both minimum and maximum values independently, selecting more fractional digits for "morePrecision" and fewer for "lessPrecision".

