---

title: NumberFormat.formatRange(): Modern JavaScript Ranged Number Formatting

date: 2025-05-26

---


# NumberFormat.formatRange(): Modern JavaScript Ranged Number Formatting

The formatRange() method of Intl.NumberFormat adds powerful locale-aware range formatting capabilities to JavaScript, allowing developers to create consistently formatted number ranges across different languages and regions. This introduction explores the method's features, implementation details, and how it handles various input scenarios while building on existing number formatting capabilities.


## Introduction to NumberFormat.prototype.formatRange

The formatRange() method of Intl.NumberFormat instances formats a range of numbers according to the instance's locale and options. This functionality allows developers to create locale-aware number ranges with consistent formatting across different languages and regions.


### Basic Usage

The method requires two parameters: startRange and endRange, which can be numeric values or strings. Strings are parsed using number conversion rules, preserving the exact value to maintain precision. The method returns a string representing the formatted range according to the locale and options of the Intl.NumberFormat object.


### Validation and Error Handling

(formatRange() throws a RangeError for NaN or inconvertible string inputs and a TypeError for undefined inputs. These exceptions ensure that developers handle invalid input scenarios gracefully.


### Implementation Details

(formatRange() operates through the Intl.MathematicalValue conversion process before calling FormatNumericRange(). The method is available in the ECMA-262 specification, having reached Stage 3 proposal status as of July 2021.


### Range Formatting Behavior

The method effectively handles infinite values and NaN inputs, though specific examples are not provided in the documents. Developers can rely on its robust handling of edge cases to create reliable range formatting functionality.


## Method Signature and Parameters

The method accepts two parameters representing the start and end of the range. These parameters can be numeric values (Number or BigInt) or strings, with strings being parsed using number conversion rules. Notably, strings are treated with higher precision, preserving their exact value rather than converting them to numbers through implicit parsing.

The method returns a string representation of the formatted range, utilizing the locale and formatting options of the calling Intl.NumberFormat object. Specifically, it utilizes the same formatting rules as the base format() method, including decimal and thousands separators appropriate for the specified locale.


### Implementation Details

The formatRange mechanism operates through the Intl.MathematicalValue conversion process before invoking the FormatNumericRange() function. This ensures that the implementation leverages consistent numeric handling across different operations while providing the specific range formatting required by developers.


### Error Handling

Invalid inputs trigger specific exceptions to help developers handle errors gracefully. If either startRange or endRange is NaN, an inconvertible string, or undefined, formatRange() throws the appropriate exception: RangeError for NaN or inconvertible strings, and TypeError for undefined values. This robust error handling allows developers to implement effective input validation for their applications.


## Formatting Behavior and Edge Cases

The method robustly handles various edge cases, including NaN, undefined inputs, and ranges extending to infinite values. When either startRange or endRange is NaN, formatRange() throws a RangeError, while undefined inputs result in a TypeError. This ensures that developers can implement effective input validation for their applications.

For infinite values, the method formats them appropriately according to the locale and options of the calling Intl.NumberFormat object. This consistent handling across different input types allows developers to create reliable range formatting functionality that works correctly in all specified scenarios.


## Rounding and Precision Options

The formatRange method's rounding behavior and precision options provide extensive control over number formatting. The method allows developers to specify rounding to a particular precision using minimumFractionDigits and maximumFractionDigits properties, with significant digit rules taking precedence when both are set.

MinimumFractionDigits and MaximumFractionDigits Settings

Rounding follows specific rules when both minimumFractionDigits and maximumFractionDigits are defined. The implementation provides three roundingPriority strategies:

- Auto: Significant digits always win

- MorePrecision: More precise results take precedence

- LessPrecision: Less precise results take precedence

The method's behavior demonstrates its atomic approach to rounding conflicts:

- For 4.321 with { maximumFractionDigits: 2, maximumSignificantDigits: 2 }, rounding produces 4.32 and 4.3 respectively.

- For 1 with { minimumFractionDigits: 2, maximumFractionDigits: 2, minimumSignificantDigits: 2, maximumSignificantDigits: 6 }, both minimum and maximum significant digits rounds to 1.00, demonstrating the priority resolution.

The roundingIncrement property offers flexible rounding modes, including nickel (5 cent) and dime (10 cent) increments. This feature enables precise control over rounding behavior for specific use cases, such as currency formatting.

Rounding modes provide extensive control over how values are rounded when they exceed specified precision limits. The available modes include:

- ceil: Always rounds up

- floor: Always rounds down

- expand: Rounds away from zero at the half-increment (default behavior)

- trunc: Rounds toward zero

- halfCeil: Rounds away from zero if the fractional part is 0.5 or greater

- halfFloor: Rounds toward zero if the fractional part is 0.5 or greater

- halfExpand: Rounds away from zero if the fractional part is 0.5 or greater (default behavior)

- halfTrunc: Rounds toward zero if the fractional part is 0.5 or greater

- halfEven: Rounds to the nearest even number, with specific behavior based on number magnitude

Developers can use these options to fine-tune the rounding process for their applications, ensuring consistent and accurate number formatting across various use cases.


## Polyfills and Browser Support

Availability and Implementation Status

The formatRange() method became available in August 2023 and is implemented across latest devices and browser versions. According to the specification, it's currently supported by Safari (starting with version 15.4), Chrome (since version 106), and Firefox (from version 93). Implementations follow the latest spec available in the V8 prototype repository, accessible through the --harmony_intl_number_format_v3 flag.

API Documentation and Usage

The method returns a string representing the formatted range according to the locale and formatting options of the calling Intl.NumberFormat object. It accepts two parameters: startRange and endRange, which can be Number, BigInt, or string values. Unlike format(), strings are parsed using number conversion rules while preserving their exact value to maintain precision.

Implementation Constraints and Locale Data Requirements

The NumberFormat API design acknowledges implementation dependencies due to internationalization requirements. This includes support for approximately 6000 human languages with regional variations, drawn from collections like the Common Locale Data Repository. The exact form of localizations varies based on conventions and implementation details, with character limitations defined by Unicode standards.

Additional Implementation Details

The API specification requires implementations to support a set of locales with adequate localizations. Internal property constraints dictate that [[availableLocales]] must conform to defined limitations, while [[localeData]] requires patterns for all locale values with specific structure requirements. Implementation choices are allowed to limit functionality while ensuring compliance with these broader linguistic and technical constraints.

