---

title: JavaScript String and Number Conversion

date: 2025-05-26

---


# JavaScript String and Number Conversion

The JavaScript toString() method offers versatile functionality for converting objects to strings, with unique behaviors for numbers, strings, arrays, and custom objects. This article explores the method's capabilities, from basic object conversion to complex number formatting and specialized object type detection, providing developers with powerful tools for string representation in JavaScript applications.


## toString() Method Overview

The toString() method returns a string representation of a JavaScript object. For built-in objects like String and Array, this method returns the object's literal text content. For custom objects, the method returns a [object Type] string unless an overridden toString() method provides a custom representation (Example 2: Custom toString() method for objects with key-value pairs).

By default, toString() operates without parameters and returns a string value representing the object (Examples 1-6: String and Array conversion, Object prototype behavior). However, the method supports additional functionality when applied to numeric values. When called on numbers, toString() returns the string representation of the number as a string primitive (Examples 4-5: Number conversion with and without base).

The method also handles specific edge cases: both 0 and -0 produce "0" as their string representation (Example 9: Number conversion), and the result of toString() for NaN values is "NaN" (Example 10: Number conversion result). For numbers with non-integer values, the decimal point separates integer and fractional components (Example 11: Number conversion with fractional value).

When working with arrays, the toString() method returns the elements separated by commas (Example 7: Array conversion). For objects that override the toString() method, the custom implementation determines the returned string representation (Example 3: Custom toString() method for user-defined objects). The method also supports base conversion for numeric values when an integer between 2 and 36 is specified as the radix parameter (Example 8: Number conversion with specified base).

To detect object class types, developers can call Function.prototype.call() and pass the object to inspect (Example 6: Using toString() to detect object class). The returned string always represents the object's type, using "[object Type]" format (Example 1: Custom toString() method implementation). This behavior can be customized by overriding the toString() method in custom objects (Example 2: Custom object behavior with overridden toString()).

The method's behavior varies slightly between primitives and wrapper objects: String primitives (Examples 7-8: Array and number conversion) and wrapper objects (Examples 1-3: Basic usage) produce consistent results, while attempting to call toString() on non-string values throws a TypeError (Example 12: toString() called on non-string value). For non-numeric values, the method produces the same result whether called on the primitive value directly or through its wrapper object (Example 13: toString() called on primitive and wrapper object).


## Using toString() with Numbers

The toString() method can convert numbers to strings with an optional radix parameter for specifying the base (between 2 and 36). The method returns a string representation of the number, using a decimal point to separate integer and fractional components. For example, 1234.toString() returns "1234", and 1234.toString(16) returns "4d2".

The radix parameter must be between 2 and 36; when outside this range, a RangeError is thrown. For instance, attempting to convert using a radix of 1 results in an error. The method handles special cases like 0 and -0, returning "0" for both, and returns "NaN" for NaN values. When converting numbers with decimal places, the method uses the least number of significant figures necessary to distinguish the output from adjacent number values.

The returned string representation uses the specified base for values between 2 and 36, with letters representing values greater than 9. For example, 10.toString(16) returns "a". Negative numbers retain their sign, with the positive binary representation preceded by a - sign rather than using two's complement notation. Large numbers use scientific notation (base-10) when their magnitude is greater than or equal to 10^21 or less than 10^-6, with the sign of the exponent specified in this case.


## toString() with Strings and Arrays

The toString() method returns a string representing the specified object. For String objects, it returns a string representation of the object, matching the behavior of the valueOf() method. The String object overrides the method of the same name from the Object object, meaning the original toString() method from the Object object is not inherited and the String version of the method is used instead.

The method's default behavior for objects that do not override toString() is to return "[object type]", where type is the object type. For String objects, the toString() method returns the string that the object wraps. The method requires its this value to be a String primitive or wrapper object, throwing a TypeError for other this values without attempting to coerce them to string values.

The toString() method works automatically when a String object is used in a context expecting a string, such as in a template literal. It operates by receiving an argument and returning the object's text representation as a string value. The returned string value depends on the type of argument being converted to string. For objects with key-value pairs, the method defaults to returning "[object Object]". To customize this behavior, developers can override the toString() method, which can generate strings containing object properties in key:value format.

When converting numeric values to strings, the method returns the number's string representation by default. If a base value between 2 and 36 is specified, the numeric value is converted according to that base. Arrays can be converted to string representations, with the resulting string containing comma-separated values. The method can also be used to detect object classes by calling Function.prototype.call() and passing the object to inspect. The returned string always represents the object's type, using "[object Type]" format, with this behavior available since ECMAScript1 (JavaScript 1997).


## toLocaleString() for Numbers

The toLocaleString() method provides a flexible way to format numbers according to the conventions of different locales. It accepts two parameters: a locales string or array specifying the language and region, and an options object that allows fine-tuning of the output format.

The method supports a wide range of language tags (BCP 47 format) for the locales parameter. When this parameter is not provided, the system's default locale is used. For optimal performance, developers are encouraged to create an Intl.NumberFormat object and use its format() method, which caches arguments and performs searches in a more constrained context.

Basic usage of the method simply returns a string representation of the number according to the host's default language. However, when called with specific locale information, it produces output tailored to that language's conventions. For example, the same number might be formatted as "30,000.65" in English, "30.000,65" in German, or "30 000,65" in French.

The method supports several key options for customization:

- minimumFractionDigits and maximumFractionDigits control the number of decimal places

- maximumSignificantDigits limits the overall precision of the output

- style can be set to "currency" for number formatting as currency

- currency and currencyDisplay properties enable currency-specific formatting

Developers can chain multiple formatting options to achieve complex output. For instance, the following code formats a number as currency with 2 decimal places:

number.toLocaleString("en-US", { style: "currency", currency: "USD", currencyDisplay: "symbol", minimumFractionDigits: 2, maximumFractionDigits: 2 })

Browser compatibility is generally good, though older Safari versions have limited support for the locale and option functionality. To ensure cross-browser compatibility, developers should consider polyfilling the method or handling it manually where necessary.


## toString() for Object References

The Object.prototype.toString() method provides a standardized way to determine an object's type through its return value. For most objects, including user-defined classes, it returns a "[object Type]" string, where Type is the object's class name. However, for null and undefined values, it returns "[object Null]" and "[object Undefined]" respectively. The method achieves this by returning "[object Date]" for Date objects, "[object String]" for String objects, and "[object Function]" for Function objects (Examples 6-7: Object.prototype.toString() usage).

For custom objects, the method can be overridden to return more specific type information. This is particularly useful when working with complex object structures or when custom object classes need clear identification (Example 2: Custom toString() method for objects with key-value pairs). To detect the class of an object, developers can call Function.prototype.call() and pass the object to inspect. The returned string always represents the object's type and has been available since ECMAScript1 (JavaScript 1997) (Example 6: Using toString() to detect object class).

The method's behavior extends beyond basic types to include special cases like the arguments object, which returns "[object Arguments]" (Example 8: Special cases). When objects have a Symbol.toStringTag property, its value is used as the Type in the output string. For objects without this property, a special tag may be used instead, as demonstrated with array objects (Example 5: toString() with arrays).

Developers can further customize object representation by setting the Symbol.toStringTag property. For instance, setting myDate[Symbol.toStringTag] to "myDate" changes the object's toString() result to "myDate". Similarly, modifying Date.prototype[Symbol.toStringTag] to "prototype polluted" changes the result of new Date() to "prototype polluted" (Example 9: Customizing toString output).

The method's flexibility extends to built-in objects, where it maintains compatibility and consistency across different JavaScript implementations. This includes support for the arguments object and adherence to ECMAScript specifications (Examples 6-9: Special cases and customizations). The method's wide compatibility across browsers and JavaScript versions ensures reliable type identification across development environments (Example 10: Browser compatibility).

