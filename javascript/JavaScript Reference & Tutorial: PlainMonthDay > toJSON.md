---

title: Temporal.PlainMonthDay.prototype.toJSON()

date: 2025-05-27

---


# Temporal.PlainMonthDay.prototype.toJSON()

When working with date and time in JavaScript, the Temporal library provides powerful abstractions for handling various calendar systems and date representations. This article focuses on the Temporal.PlainMonthDay.toJSONObject() method, which converts month-day date objects into a standardized string format suitable for JSON serialization. We'll explore how this method handles different calendar systems, year formats, and validation rules, while also discussing how to properly serialize and deserialize these date objects using custom JSON handling functions.


## Return Value and Format

The Temporal.PlainMonthDay.prototype.toJSON() method returns a string representation of the month-day in RFC 9557 format, which is equivalent to the format produced by the monthDay.toString() method. This string format can take one of several forms based on the input options and the calendar system used:

The format can include the year, separated from the month-day by an optional hyphen. The year can either be a four-digit number or a six-digit number with a + or - sign, though the sign is only required for non-ISO calendars. The year is necessary for specifying dates in non-ISO calendar systems, while it is optional for ISO calendars.

The method supports various calendar annotations in square brackets to indicate the calendar system used. These annotations can be controlled through options parameters passed to the method, which can be set to "auto", "always", "never", or "critical". The "auto" option uses the calendar name from the input options if available, otherwise defaulting to "iso8601". The "always" option ensures the calendar name appears in square brackets, while "never" removes the calendar annotation entirely. The "critical" option adds an exclamation point before the calendar name in the annotation.

The returned string format can vary based on whether the month-day combination forms a valid date in the calendar system. If a valid date cannot be formed using the input properties, RangeError is thrown. For example, attempting to create a date with February 30 would result in an error. Similarly, out-of-range values for year, month, or day will also trigger RangeError, as the method enforces strict date validation.


## Automated JSON Conversion

The Temporal.PlainMonthDay.prototype.toJSON() method is automatically called by JSON.stringify() when a Temporal.PlainMonthDay object is stringified, providing a direct way to serialize date objects for JSON representation. This built-in functionality makes it simple to include month-day information in JSON data structures.

During serialization, the method produces a string in the same format as calling monthDay.toString(). This string includes the year and calendar annotation based on the input options, unless the calendar is "iso8601", in which case these are omitted. The format matches the output of the RFC 9557 date specification, making it consistent with other Temporal date representations.

For example, the following JavaScript code demonstrates serializing a Temporal.PlainMonthDay object:

```javascript

const md = Temporal.PlainMonthDay.from({ month: 8, day: 1 });

const jsonStr = JSON.stringify({ birthday: md });

// '{"birthday":"08-01"}'

```

To properly parse JSON data that includes month-day information, developers must use a custom reviver function with JSON.parse(). This function should specifically handle keys that represent month-day values, converting them into Temporal.PlainMonthDay objects using the appropriate constructor or static method. Without this custom reviver, JSON.parse() would not recognize the serialized month-day format and would treat it as a regular string.


## Calendar Annotations

The calendar annotation in square brackets is controlled through options parameters passed to the method. The annotation can take one of several forms based on the calendar system used:

- If the calendar is "iso8601", the output includes the calendar name in square brackets.

- The "auto" option uses the calendar name from the input options if available, otherwise defaulting to "iso8601".

- The "always" option always includes the calendar name in square brackets.

- The "never" option omits the calendar name from the output entirely.

- The "critical" option includes the calendar name only if it differs from "iso8601", and prefixes it with an exclamation point (!u-ca=calendar_id).

The calendar annotation behaves differently based on the calendar system:

- For ISO 8601 calendars, the output includes the calendar name in square brackets if requested, otherwise it omits the annotation.

- For non-ISO 8601 calendars, the behavior depends on the calendar type:

  - "era" includes fields for era, era-year, and year

  - "era-year" includes fields for era, era-year, and year

  - "year" includes fields for era, era-year, and year

  - "month" includes fields for month and month-code

  - "month-code" includes fields for month and month-code

  - "day" includes only the day field

  - "year, month, day" includes all fields: era, era-year, year, month, month-code, and day

When the calendar annotation is enabled, it provides additional context for interoperability between different calendar systems. The critical flag adds an exclamation point before the calendar name to emphasize its importance in contexts where calendar differences might affect date interpretation.


## Custom Parsing

To parse the string back into a Temporal.PlainMonthDay object, a custom 'reviver' function is required when using JSON.parse(). This function should specifically handle keys that represent month-day values, converting them into Temporal.PlainMonthDay objects using the appropriate constructor or static method.

The provided documentation demonstrates an example of how to implement this custom reviver function:

```javascript

const obj = JSON.parse(jsonStr, (key, value) => {

  if (key === "birthday") {

    return Temporal.PlainMonthDay.from(value);

  }

  return value;

});

```

This reviver function checks if the key matches the target (in this case, "birthday") and uses Temporal.PlainMonthDay.from() to convert the string value back into a PlainMonthDay object. Without this custom reviver, JSON.parse() would treat the serialized month-day format as a regular string rather than attempting to reify it into a Temporal object.

The process of creating a PlainMonthDay object can also be achieved through alternative methods. As mentioned in the documentation, the from() static method allows creation from an object representation:

```javascript

const daveObj = Temporal.PlainMonthDay.from({ month: 8, day: 26 });

```

Additionally, the class includes a constructor that accepts year, month, and day as parameters:

```javascript

const daveDoB = new Temporal.PlainMonthDay(8, 26);

```

Both approaches demonstrate the flexibility in creating PlainMonthDay objects from different data representations, with the JSON parsing specifically requiring the reviver function to maintain the correct object structure. This approach aligns with the Temporal API's design principles for managing complex date and time values during JSON serialization and deserialization.


## Implementation Details

The implementation of the toJSON method follows the same algorithm as toString, ensuring consistency in date representation while meeting the specific requirements of JSON serialization. Under the hood, both methods perform similar steps to generate the output string, including handling reference ISODay and calendar options.

Key implementation details include:

1. The method first validates the input options through checks for valid calendar names and configuration settings.

2. It then constructs the date string using the PadISOYear and ToZeroPaddedDecimalString functions to format the year and day components according to ISO 8601 standards.

3. For non-ISO calendars, the method checks the calendar annotation requirements to determine if the calendar name should be included in the output string.

4. The year component appears only when necessary, either for disambiguation in non-ISO calendars or for the critical flag specification.

5. The method follows strict validation to prevent invalid date representations, matching the behavior of other Temporal date methods that enforce valid month-day combinations.

These internal steps ensure that the toJSON method produces a consistent, interoperable date representation while supporting the calendar annotations and options required for accurate JSON serialization of month-day dates.

