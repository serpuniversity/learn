---

title: TypedArray.prototype.toSorted() Method

date: 2025-05-27

---


# TypedArray.prototype.toSorted() Method

This article delves into the toSorted() method of JavaScript's TypedArray prototype, showcasing its role in non-mutating array sorting. By examining how this method creates new sorted arrays while preserving the original data, we uncover an essential tool for functional programming and state management in modern JavaScript development. The technical exploration includes detailed sorting mechanisms, performance comparisons with traditional sorting methods, and practical examples across numerical and string data types.


## Non-Mutating Sorting in JavaScript

The toSorted() method provides a non-destructive way to sort arrays, returning a new sorted array while leaving the original array unchanged. This approach is particularly valuable in functional programming scenarios where operations should not modify state directly, as it explicitly signals the creation of a new sorted array.

By default, toSorted() sorts array elements as strings, which can lead to incorrect results when working with numerical values. To achieve proper numerical sorting, developers must provide a comparison function that returns a negative, zero, or positive value to determine the sort order: negative if the first argument comes before the second, positive if it comes after, and zero if they are equal. For example:

```javascript

const numbers = [3, 1, 4, 1, 5, 9];

const sortedNumbers = numbers.toSorted((a, b) => a - b);

```

The implementation of toSorted() for TypedArray instances mirrors that of Array.prototype.toSorted(), with the key difference being default numerical sorting for TypedArray elements. This distinction makes it particularly useful for data structures that require both array-like operations and numerical precision.

While the toSorted() implementation typically performs array copying, benchmark data indicates that it executes slightly faster than traditional array sorting methods in certain scenarios. However, developers should consider compatibility requirements, especially when targeting older JavaScript environments where the method might not be available.


## Default and Custom Sorting Behavior

By default, the toSorted() method sorts values as strings using Unicode code point values. For numerical values, a compare function must be provided to specify the desired order. The difference between toSorted() and traditional array sorting methods like sort() is that toSorted() creates a new sorted array while leaving the original array unchanged.

The compare function determines the sort order and should return a negative, zero, or positive value:

- Negative: if the first argument should come before the second

- Zero: if no change to sort order is needed

- Positive: if the first argument should come after the second

The syntax for using the compare function is:

```javascript

_array_.toSorted((a, b) => a - b)

```

This example demonstrates numerical sorting for a TypedArray:

```javascript

const numbers = new Int16Array([5, 1, 8, 3, 2]);

const sortedNumbers = numbers.toSorted((a, b) => a - b);

console.log(sortedNumbers); // Output: Int16Array(5) [1, 2, 3, 5, 8]

```

For string sorting, you can provide a custom compare function:

```javascript

const fruits = new Uint8Array([79, 97, 100, 101, 82, 99]);

function stringCompare(a, b) {

  return String.fromCharCode(a).localeCompare(String.fromCharCode(b));

}

const sortedFruits = fruits.toSorted(stringCompare);

console.log(String.fromCharCode.apply(null, sortedFruits)); // Output: acdeOR

```

Key points about toSorted() behavior:

- Creates a new array without modifying the original

- Sorts elements as strings by default

- Requires a compare function for numerical sorting

- Works with TypedArray instances and arrays

- Supports both ascending and descending sorting


## TypedArray Specifics

The TypedArray implementation of toSorted() shares the same algorithm as Array.prototype.toSorted() but applies default numerical sorting for TypedArray elements. This feature makes it particularly suitable for data structures that require both array-like operations and numerical precision.


### Default Sorting Behavior

By default, toSorted() sorts TypedArray elements numerically, providing direct support for common data manipulation tasks. This default behavior simplifies usage for developers working with numerical data, as it eliminates the need to explicitly specify the compare function for basic sorting operations.


### Comparison with Array.prototype.toSorted()

The toSorted() method for TypedArrays preserves key characteristics of Array.prototype.toSorted(), including the creation of a new sorted array and the requirement for a compare function when sorting non-numeric values. The primary distinction lies in the default sorting behavior: TypedArray toSorted() sorts elements numerically by default, while Array toSorted() sorts elements as strings unless a compare function is provided.


### Implementation Details

The method follows the specifications outlined in the ECMAScript 2026 Language Specification, specifically Section sec-%typedarray%.prototype.tosorted (42.2.2.6). It expects the TypedArray to have a length property and integer-keyed properties, with empty slots in sparse arrays being handled as if they contain the value undefined.


### Browser Compatibility and Performance

The TypedArray implementation of toSorted() demonstrates similar performance characteristics to Array.prototype.toSorted(), with both methods favoring the creation of a new array over modifying the original. While benchmark data indicates that toSorted() can execute slightly faster in certain scenarios, developers should consider the potential overhead of array copying, especially for large datasets.


### Additional Considerations

The TypedArray version of toSorted() provides several advantages for modern JavaScript development:

- Preserves the original array, which is particularly valuable for functional programming and immutable state management

- Integrates seamlessly with existing TypedArray operations and methods

- Aligns with the growing trend towards safe, non-mutating array operations in JavaScript


## Performance Considerations

Benchmark data consistently shows that toSorted() executes slightly faster than [array].sort() while maintaining the same basic functionality. The performance improvement is most significant when creating a new sorted array, as the traditional approach requires an extra array copy operation.

The method demonstrates similar execution characteristics to Array.prototype.toSorted(), with both approaches favoring the creation of a new array over modifying the original. The primary performance advantage of toSorted() relates to its non-mutating nature - by preserving the original array, it eliminates the overhead of array copying while maintaining efficient execution speeds.

While the performance gap is relatively small, the difference becomes more pronounced with larger data sets. For developers working with extensive data collections or performance-critical applications, the slight speed improvement of toSorted() may justify its use over traditional sorting methods while maintaining array immutability.


## Cross-Browser Compatibility

The implementation of toSorted() in modern browsers and Node.js 20+ aligns with the broader trend towards immutable array operations in JavaScript. While the method shares the same algorithm as Array.prototype.toSorted(), its primary advantage lies in its direct support for TypedArray operations and numerical sorting.


### Browser Support

The method is supported across major browsers including Chrome, Edge, Firefox, Opera, and Safari, with performance metrics showing approximately 939.67 executions per second compared to 916.91 for traditional array sorting methods. This makes it a practical choice for web development, though developers should consider the specific requirements of their target environments.


### Alternative Implementations

For developers using older versions of TypeScript (prior to 5.2), a common workaround is to use the spread syntax to create a reversed copy of the array: `const reversedArray = [...array].reverse()`. For those targeting Node.js environments, updating to version 20+ is necessary to utilize toSorted() functionality.

