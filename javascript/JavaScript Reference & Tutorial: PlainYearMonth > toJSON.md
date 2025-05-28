---

title: Temporal.PlainYearMonth.prototype.toJSON - JavaScript Reference & Tutorial

date: 2025-05-27

---


# Temporal.PlainYearMonth.prototype.toJSON - JavaScript Reference & Tutorial

In JavaScript, representing date and time information requires careful handling to maintain both accuracy and compatibility across different platforms and applications. The `Temporal` API introduced in modern JavaScript offers robust support for working with dates and time, including the capability to represent and manipulate year-month values independently of days and hours. This article focuses on the `toJSON()` method of `Temporal.PlainYearMonth` instances, which provides a standardized way to serialize these year-month values for storage or transmission. Understanding how this method works and how it interacts with JSON serialization is crucial for developers working with date data in JavaScript applications.


## Method Overview

The `toJSON()` method of `Temporal.PlainYearMonth` instances returns a string representation of the year-month in RFC 9557 format, equivalent to calling `toString()`. This method automatically serializes `Temporal.PlainYearMonth` objects during JSON serialization, allowing them to be stored or transmitted as strings.


### Implementation Details

The method returns a string with the calendar annotation included if it is not "iso8601". For example, `Temporal.PlainYearMonth.from({ year: 2022, month: 10 })` would return "2022-10", while `Temporal.PlainYearMonth.from({ year: 2022, month: 10, calendar: "japanese" })` would return "2022-10 u-ca=japanese".


### Calendar Handling

When called automatically by `JSON.stringify()`, `toJSON()` handles both ISO 8601 and non-ISO 8601 calendars. It includes the calendar identifier in the output string unless explicitly set to "iso8601". This behavior ensures that serialized data can be unambiguously interpreted when deserialized using `Temporal.PlainYearMonth.from()`.


### Usage Example

```

const month = Temporal.PlainYearMonth.from({ year: 2022, month: 10 });

const jsonStr = JSON.stringify({ currentMonth: month }); // '{"currentMonth":"2022-10"}'

```


## Method Implementation

The `toJSON()` method of `Temporal.PlainYearMonth` instances returns a string representing the year-month in RFC 9557 format, identical to the output of calling `toString()`. This native serialization capability is particularly useful for automatically converting `Temporal.PlainYearMonth` objects into JSON-compatible strings when using `JSON.stringify()`.


### Implementation Details

When serializing, `toJSON()` follows the same calendar handling rules as `toString()`, including the optional calendar identifier. For example, a plain year-month object representing October 2022 would serialize as "2022-10", whereas an object with a Japanese calendar would serialize as "2022-10 u-ca=japanese". This consistent behavior ensures that serialized date representations remain unambiguous upon deserialization with `Temporal.PlainYearMonth.from()`.


### Compatibility and Browser Support

While browsers universally support `toString()`, support for `toJSON()` remains experimental as of this writing. Always validate server-side when deserializing JSON to handle potential missing methods. For full compatibility, consider wrapping `Temporal.PlainYearMonth` instances in a custom object before serialization.


## Method Usage

The `toJSON` method of `Temporal.PlainYearMonth` instances returns a string representation of the year-month in RFC 9557 format, equivalent to calling `toString()`. This method is automatically called by `JSON.stringify()` when serializing `Temporal.PlainYearMonth` objects, making it a convenient way to convert year-month values into JSON-compatible strings.

When stringifying `Temporal.PlainYearMonth` objects, the method follows the same calendar handling rules as `toString()`. This includes the inclusion of the calendar identifier unless explicitly set to "iso8601". For example, a plain year-month object representing October 2022 would serialize as "2022-10", while an object with a Japanese calendar would serialize as "2022-10 u-ca=japanese".


### Automatic Serialization Behavior

The automatic serialization behavior of `toJSON()` can be customized through various options. These options, passed as part of the serialization context, influence how the year-month value is represented in the serialized string. The primary configurable aspect is the calendar annotation, which can be controlled using the `calendar` property in the serialization options.

For consistent deserialization, it's recommended to use the `Temporal.PlainYearMonth.from()` method as the reviver function with `JSON.parse()`. This ensures that the JSON string representing a year-month can be reliably converted back into a `Temporal.PlainYearMonth` object.


### Browser Support and Considerations

While `toJSON()` is designed for seamless JSON serialization, its experimental status means compatibility can vary across browsers. Always validate server-side when deserializing JSON, as `toJSON()` might not be available in all environments. For maximum compatibility, consider wrapping `Temporal.PlainYearMonth` instances in a custom object before serialization, or implementing a fallback mechanism.


### Practical Usage Example

```javascript

const month = Temporal.PlainYearMonth.from({ year: 2022, month: 10 });

const jsonStr = JSON.stringify({ currentMonth: month }); // '{"currentMonth":"2022-10"}'

```

This example demonstrates the automatic serialization of a `Temporal.PlainYearMonth` object into a JSON string, with the `toJSON()` method handling both the conversion and the inclusion of calendar annotations as needed.


## Serialization and Deserialization

To deserialize JSON strings containing `Temporal.PlainYearMonth` objects, you must use the `Temporal.PlainYearMonth.from()` method as the reviver function with `JSON.parse()`. This custom reviver function should recognize keys ending with "YearMonth" and convert them back into `Temporal.PlainYearMonth` objects using `from()`.

The `from()` method accepts a variety of input types, including strings in RFC 9557 format, objects with year and month properties, and existing `Temporal.PlainYearMonth` objects. When creating a new year-month instance via `from()`, you can specify additional options to control calendar handling and overflow behavior.

For example, the following code demonstrates proper deserialization and conversion using the reviver function:

```javascript

const jsonStr = '{"currentMonth": "2022-10 u-ca=japanese"}';

const obj = JSON.parse(jsonStr, (key, value) => {

  if (key.endsWith('YearMonth')) {

    return Temporal.PlainYearMonth.from(value);

  }

  return value;

});

console.log(obj.currentMonth.toString()); // "2022-10 u-ca=japanese"

```

This example shows how to handle the calendar annotation during deserialization. The reviver function checks if the key ends with "YearMonth" and then converts the corresponding value using `Temporal.PlainYearMonth.from()`.

Note that the browser compatibility status for `toJSON()` and related methods is experimental. Always validate server-side when deserializing JSON to handle potential missing methods. For maximum compatibility, consider wrapping `Temporal.PlainYearMonth` instances in a custom object before serialization or implementing a fallback mechanism for environments that lack native support for these methods.

