---

title: Working with BigInt in JavaScript: Serialization and Workarounds

date: 2025-05-26

---


# Working with BigInt in JavaScript: Serialization and Workarounds

Working with JavaScript's BigInt functionality presents unique challenges, particularly when handling serialization and cross-browser compatibility. While BigInts expand JavaScript's numerical capabilities, their implementation requires careful consideration of type coercion rules and JSON serialization limitations. Understanding these nuances is crucial for developers working with large integer values in JavaScript applications.


## BigInt Overview

BigInt values represent integer values that are too large or too small to be represented by the standard number primitive. They are created using two methods: a string literal with a trailing "n" (e.g., "5n") or the BigInt constructor with a string argument (e.g., BigInt("5")). These values behave like other JavaScript numbers for basic arithmetic operations but require special handling when mixed with Number values or when performing bitwise operations.

The implementation of BigInts in JavaScript follows specific coercion rules noted in the MDN Web Docs:

- BigInts are returned as-is

- undefined and null throw TypeError

- true becomes 1n; false becomes 0n

- Strings are converted by parsing as integer literals

- Numbers throw TypeError to prevent precision loss

- Symbols throw TypeError

- Objects are converted to primitives:

  - First by calling [Symbol.toPrimitive]() with "number" hint

  - Then by valueOf()

  - Finally by toString()

When working with JSON serialization, these values must be converted to strings using the toString() method since JSON.stringify() does not support BigInt natively. The serialization process involves converting the BigInt to a string representation before passing it to JSON.stringify(). For example, given a small BigInt (5n) and a larger one (5555555555555555555555555500003n), the following code properly serializes the values:

```javascript

var small = BigInt(5n);

var big = BigInt(5555555555555555555555555500003n);

JSON.stringify([big.toString(), small.toString()]);

```

This results in a JSON string containing the serialized values: ["5555555555555555555555555500003", "5"]

The text from Oracle's JSON-B solution provides additional context on the challenges of JSON serialization with BigInt values. In their implementation, small values are serialized as Numbers and large values as Strings, rather than attempting to determine a unified serialization format based on the underlying data type. This approach is described as "pretty broken" due to its lack of flexibility and the issues it introduces when mixing numeric types.


## JSON Serialization Issues

JSON.stringify() throws a TypeError when attempting to serialize BigInt values, stating "Do not know how to serialize a BigInt." This error occurs across multiple JavaScript engines, with Chrome's V8 engine returning "Do not know how to serialize a BigInt," Firefox returning "BigInt value can't be serialized in JSON," and Safari reporting "JSON.stringify cannot serialize BigInt."

The core issue stems from JSON's data type limitations, which only support strings, numbers, objects, arrays, booleans, and null. BigInt values, created through both "5n" literals and the BigInt() function, fall outside these supported types. As a result, JSON.stringify() cannot handle these values directly.

Small BigInt values can be serialized as numbers, while large values require string representation. For instance, the value 5n can be serialized as 5, while 5555555555555555555555555500003n must be serialized as "5555555555555555555555555500003". Attempting to serialize these values directly results in the TypeError.

Developers have implemented various workarounds, including using the toJSON method on BigInt prototypes and modifying the JSON.stringify process to handle these values. However, these solutions introduce their own complexities, such as the need for reviver functions during deserialization to maintain the correct value types. The current implementation's handling of numeric lengths adds further complications, particularly when working with values that require arbitrary precision.


## Workaround Solutions

To address the serialization challenge, developers have implemented several workarounds. The most common approach involves overriding the `BigInt.prototype.toJSON` method to provide custom string conversion functionality. This method returns the `toString` representation of the BigInt instance, ensuring proper serialization without complaints from the JSON.stringify method.

For example, a developer might implement this solution as follows:

```javascript

BigInt.prototype.toJSON = function() {

  return this.toString();

};

```

With this implementation, the following code correctly serializes the values:

```javascript

var small = BigInt(5n);

var big = BigInt(5555555555555555555555555500003n);

JSON.stringify([big, small]);

```

This generates the expected output: ["5555555555555555555555555500003", "5"]

However, this approach still requires careful handling of deserialization, as the original BigInt type information is lost in the process. To maintain type integrity, developers may need to implement a custom reviver function when parsing JSON:

```javascript

JSON.parse(jsonString, (key, value) => {

  if (typeof value === "string" && value.startsWith("/BigInt(")) {

    return BigInt(value.slice(8, -1));

  }

  return value;

});

```

This alternative approach mirrors the behavior of Date serialization in JavaScript, where the toJSON method formats the value as a string with consistent syntax. The corresponding fromJSON method can then parse and validate the string representation, creating a similar interface to Date JSON handling.


## Chrome/V8 Implementation

Chrome's V8 engine and other JavaScript engines handle BigInt serialization differently, which presents challenges for cross-browser compatibility. The core issue stems from JSON's data type limitations, which only support strings, numbers, objects, arrays, booleans, and null. As a result, engines like V8 throw a TypeError with the message "Do not know how to serialize a BigInt" when attempting to serialize these values.

This behavior differs from other engines, which produce distinct error messages: Firefox returns "BigInt value can't be serialized in JSON," while Safari reports "JSON.stringify cannot serialize BigInt." These differences complicate development, particularly when working with multiple browser environments.

Chrome's implementation highlights the broader issue of JSON's numeric type handling. The text from Oracle's JSON-B solution offers valuable context, noting that the current JSON type system is a "relic from JavaScript" that proves useful within its scope but has limited impact outside of the language. This legacy system causes confusion when extending numeric types beyond standard JavaScript number limits.

The Oracle JSON-B approach offers an instructive alternative, serializing small BigInt values as Numbers and large values as Strings. While this method fully conforms to JSON specification requirements, it introduces its own complexities. Developers must carefully manage these differences when working across various JavaScript engines and environments, particularly when dealing with numeric data serialization.


## Future Considerations

The current JSON type system proves useful within the JavaScript scope but becomes less relevant when extending numeric types beyond standard JavaScript number limits. This legacy system causes confusion when working with non-core types, particularly with the recent addition of BigInt support.

JSON serialization has reached a new level of complexity, with engines like V8 throwing TypeError exceptions when attempting to serialize BigInt values. While the current implementation maintains backward compatibility by copying the JSON behavior of Date objects, this approach remains insufficient for general-purpose information interchange.

The text from GitHub issues related to this proposal suggests two main approaches for implementing BigInt support:

1. Conservative scheme: This approach works out of the box and maintains compatibility with existing applications. It aligns with the current behavior of JavaScript's JSON object, providing a familiar serialization pattern for users accustomed to Date serialization.

2. RFC8259 support: This option would require changes to the ES6 JSON object, potentially offering more flexibility but introducing compatibility risks.

The discussion highlights that the current JSON type scheme is already "pretty deficient" for general-purpose information interchange. State-of-the-art applications typically verify input data anyway, making explicit type information redundant. Oracle's JSON-B solution offers an instructive alternative, serializing small BigInt values as Numbers and large values as Strings, though this approach is described as "broken" according to the author's perspective.

To address these limitations, the text suggests several improvements:

- Making quotes optional for JSON keys, as this feature is already supported in JavaScript

- Adding support for JSON comments, which could enhance data interoperability

- Proposing a conservative scheme that maintains backward compatibility with many existing ES and non-ES JSON-based applications

- Exploring alternatives like DataURL syntax with mime types, which could achieve similar results while maintaining compatibility with existing JSON formats

