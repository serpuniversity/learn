---

title: JSON(rawJSON): Working with Raw JSON in JavaScript

date: 2025-05-26

---


# JSON(rawJSON): Working with Raw JSON in JavaScript

JavaScript's JSON handling capabilities have evolved significantly since its inception, particularly with the introduction of native support for features like BigInts. However, these advancements have not reached all environments equally. The JSON(rawJSON) module addresses this gap by providing reliable rawJSON objects that maintain syntactic validity across various JavaScript implementations.

These specialized JSON objects behave uniquely within the ecosystem, offering precise numeric representation through their interaction with JavaScript's JSON methods. Understanding how to work with rawJSON objects is crucial for developers working in environments where native support is lacking, as these objects bridge the gap between standard JSON handling and advanced numerical precision requirements.

This article explores the fundamentals of rawJSON objects, including their creation, behavior, and implications for JavaScript development. We'll examine how they differ from standard JSON objects, why they're important for precise numerical representation, and how to effectively integrate them into your projects.


## rawJSON Basics

The JSON(rawJSON) module introduces rawJSON objects, which are guaranteed to be syntactically valid JSON. These objects serve as a specialized form of JSON handling in JavaScript, particularly important for environments where native support for features like BigInts is lacking.

rawJSON objects behave uniquely within JavaScript's JSON ecosystem. When such an object is encountered during serialization, it is treated as a self-contained piece of JSON rather than an ordinary object. This behavior is managed through the `JSON.isRawJSON()` method, which provides a reliable way to identify rawJSON objects.

Fundamentally, rawJSON objects are created using the `JSON.rawJSON()` function, which accepts a single parameter representing valid JSON text. The resulting object is a special form of frozen object with a single public field, `rawJSON`, which stores the original JSON string. This structure ensures that rawJSON objects maintain their integrity throughout serialization and deserialization processes.

The handling of numeric values in rawJSON objects warrants particular attention. Unlike standard JavaScript numbers, which face limitations in precision representation, rawJSON objects can accurately store and retrieve BigInt values. This capability makes them particularly valuable in applications where exact numeric precision is critical, such as financial calculations or scientific data processing.

When working with rawJSON objects, developers must be aware of their behavior during serialization and deserialization. JSON.stringify() can process rawJSON objects directly, maintaining their integrity as JSON text. However, JSON.parse() requires additional considerations due to the specialized nature of rawJSON objects. To successfully handle these objects during parsing, developers may need to implement custom reviver functions that can recognize and properly process rawJSON values.

The performance benefits of rawJSON objects are notable, with reported improvements of 1.5x to 3x over simpler cases and nearly matching native implementations in environments like Chrome. These efficiency gains make rawJSON objects an attractive choice for performance-sensitive applications while maintaining their syntactic reliability.


## isRawJSON Method

The JSON.isRawJSON() method provides a reliable way to distinguish rawJSON objects from other JavaScript values. This capability is particularly important in environments where developers need to process values that may come from multiple sources, including both standard JSON objects and rawJSON objects.

The method's implementation relies on the unique structure of rawJSON objects. When a value is created using JSON.rawJSON(), it becomes a frozen object with a single public field, `rawJSON`, which stores the original JSON string (see Doc 1). This structure allows the isRawJSON method to return true for raw JSON objects while reliably returning false for other types of JavaScript values.

The method's performance characteristics are noteworthy. It operates efficiently, with minimal overhead compared to basic value checks. In environments where rawJSON functionality is available, isRawJSON provides a direct and effective means of validating rawJSON objects, ensuring that developers can implement precise JSON handling logic without unnecessary complexity (see Doc 2).

Developers should be aware of potential limitations when using isRawJSON. The method specifically tests for objects created by JSON.rawJSON(), making it incompatible with standard JSON objects and other JavaScript value types. For comprehensive JSON validation, developers may need to combine isRawJSON with additional checks that account for valid JSON structures (see Doc 3).

By providing a clear distinction between rawJSON objects and other JavaScript values, isRawJSON enables developers to implement precise JSON handling strategies that maintain data integrity while supporting advanced JSON features like BigInt precision (see Doc 4).


## rawJSON Example

The example demonstrates a custom serializer function that handles both standard JSON objects and rawJSON objects. This function illustrates several key aspects of working with rawJSON objects, particularly focusing on numeric precision and object serialization.

When processing the `userId` field, the example highlights a critical limitation of standard JavaScript numbers. For instance, the value `12345678901234567890` cannot be represented precisely due to JavaScript's floating point limitations. To demonstrate this, the code initially attempts to use a standard number representation:

```javascript

const userId = 12345678901234567890;

console.log(JSON.stringify({ userId })); // {"userId":12345678901234567000}

```

This comparison clearly shows the loss of precision:

```javascript

const userIdRaw = JSON.rawJSON("12345678901234567890");

console.log(JSON.stringify({ userId: userIdRaw })); // {"userId":"12345678901234567890"}

```

The custom serializer function effectively handles these cases by using JSON.isRawJSON to determine the proper serialization approach:

```javascript

function customSerializer(key, value) {

  if (key === "userId" && !JSON.isRawJSON(value)) {

    value = JSON.rawJSON(value.toString());

  }

  return value;

}

const data = { userId: 12345678901234567890 };

console.log(JSON.stringify(data, customSerializer));

```

This function successfully maintains the precise numeric value when the original data was provided as a standard number, demonstrating the importance of using rawJSON objects in scenarios requiring exact numeric representation.


## JSON(rawJSON) Implementation

The JSON(rawJSON) module provides comprehensive ponyfill support for rawJSON functionality, addressing key aspects of rawJSON implementation across various JavaScript environments. The package offers a modular design with clear documentation, making it suitable for both new and experienced developers.

JSON.rawJSON accepts only primitive values, including Symbols, and returns a specialized, frozen null prototyped object with a single public field, rawJSON, which stores the original JSON string. This structure enables developers to create rawJSON objects using the JSON.rawJSON method, implementing precise value representation similar to native implementation in browsers like Chrome.

Performance benchmarks demonstrate significant efficiency gains, with reported improvements of 1.5x to 3x over simpler cases and nearly matching native Chrome implementation. The ponyfill's implementation details reveal a robust foundation, capable of handling complex cases with minimal overhead while maintaining strict type constraints.

Implementing rawJSON functionality requires careful consideration of parsing behavior. JSON.parse() necessitates a reviver function to properly handle rawJSON values, as demonstrated in the official implementation example (Doc 1). The JSON.reviver helper function effectively recognizes BigInts and returns them, ensuring accurate value representation during deserialization processes.

The module's architecture includes extensive error handling mechanisms, particularly for edge cases (Doc 2). While the documentation notes potential issues with seppuku arrays or objects during parsing or value resolution, the implementation appears robust across standard use cases. The ponyfill's adherence to strict type constraints and detailed validation routines helps developers maintain reliable JSON processing workflows in modern JavaScript environments.


## JSON(rawJSON) Best Practices


### Integration with Existing Workflows

When integrating rawJSON functionality with existing JSON processing workflows, developers should focus on maintaining clear distinctions between rawJSON and standard JSON objects. This separation is crucial for proper data handling and serialization processes. Developers can leverage the JSON.isRawJSON method to identify rawJSON objects reliably, allowing them to implement precise JSON processing logic while supporting advanced features like BigInt precision.


### General Usage Guidelines

Developers should use rawJSON objects in scenarios requiring exact numeric representation, particularly with BigInt values. While rawJSON objects enhance precision, they introduce specialized handling requirements during serialization and deserialization. For optimal performance and reliability, developers should combine rawJSON usage with appropriate serialization strategies that maintain data integrity across JSON processing pipelines.


### Error Handling Best Practices

The JSON(rawJSON) module includes comprehensive error handling mechanisms to address known limitations. Developers should be aware of potential issues with seppuku arrays or objects during parsing and value resolution. To safely implement rawJSON functionality, developers should include robust error handling routines that can manage these edge cases while maintaining reliable JSON processing workflows.


### Performance Considerations

The rawJSON implementation demonstrates significant performance gains compared to standard JSON handling, with reported improvements up to 3x faster on complex cases. Developers should evaluate their specific use cases to determine where rawJSON implementation can provide the most substantial benefits. The specialized handling requirements for rawJSON objects mean that developers should balance performance gains with the complexity of implementation and error handling routines.

