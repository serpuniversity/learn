---

title: JavaScript Array.prototype.toSorted() Method

date: 2025-05-26

---


# JavaScript Array.prototype.toSorted() Method

Sorting arrays is a fundamental operation in programming, with the native `Array.sort()` method being widely used. However, this method modifies the original array, which can be problematic in certain scenarios. The ECMAScript 2023 specification introduces the `Array.prototype.toSorted()` method, providing a safer alternative that returns a shallow copy of the array sorted in ascending order. This introduction will explore the features and implementation details of `toSorted`, comparing it to existing sorting methods and demonstrating its practical applications in both simple and complex data structures.


## The `toSorted` Method

The `toSorted` method creates a shallow copy of the original array and returns it sorted in ascending order. This ensures that the original array remains unmodified, providing a safer alternative to methods that alter the original data structure.

The method applies a stable sorting algorithm according to the ECMAScript specification, designed to handle various types of real-world data efficiently. This algorithm provides consistent sorting behavior across different data types and sizes.

When called on non-array objects with a `length` property and integer-keyed properties, `toSorted` reads these properties and collects them in the range of 0 to `length - 1`, sorting them into a new array. It specifically handles sparse arrays by treating empty slots as if they contain the value `undefined`, ensuring all elements are considered in the sorting process.

This method provides a direct copy of the sorted array, making it suitable for scenarios where maintaining the original data structure is crucial. The stable sorting algorithm ensures that equal elements retain their relative order, though JavaScript engines may implement this behavior differently across platforms.


## Sorting Algorithm

The `toSorted` method relies on the stable sorting algorithm defined by the ECMAScript specification, ensuring consistent behavior across different types of real-world data. Underlying this method is the TimSort algorithm, derived from merge sort and insertion sort, which has proven effective for a wide range of sorting scenarios.

When implementing array sorting, JavaScript engines face several challenges. The default string-based comparison produces unexpected results for numeric or mixed-type arrays, necessitating custom comparison functions. Moreover, the stability of the sort operation—where equal elements retain their original order—varies across JavaScript engines. While some engines, particularly V8, implement stable sorting, this behavior is not consistently maintained across all environments.

The sorting algorithm handles various data types with specific considerations. For numeric arrays, it performs an efficient comparison using subtraction. However, it's important to note that JavaScript's string-based comparison can lead to incorrect sorting of numbers; for example, "25" is incorrectly sorted before "100". To address this, developers must implement custom comparison functions that correctly interpret the data type of the elements being sorted.

The method's implementation also shows flexibility with different data structures. It handles sparse arrays by treating empty slots as "undefined", ensuring these elements are considered in the sorting process. For non-array objects, it reads the `length` property and collects integer-keyed properties from 0 to `length - 1`, maintaining the original order of elements when possible. This functionality makes the method particularly useful for sorting objects with numerical keys while preserving their order.


## Comparison Function

The comparison function passed to `toSorted()` determines the sorting order of the elements. It must return a negative, zero, or positive value to define the sort order, with negative values indicating that the first argument comes before the second, positive values indicating the second comes before the first, and zero indicating no change to the sort order.

For numbers, the comparison function should subtract one value from the other: `a - b` returns negative if `a < b`, positive if `a > b`, and zero if `a == b`. This differs from the default string comparison, which incorrectly sorts numbers alphabetically, placing "25" before "100" due to the lexicographical comparison of "2" and "1".

When sorting strings, the comparison function should return -1, 0, or 1 based on the Unicode code point values of the characters. A common implementation uses a ternary operator: `a === b ? 0 : a > b ? 1 : -1`, which evaluates to 0 if the strings are equal, 1 if the first string comes after the second, and -1 if the first comes before the second.

The comparison function also enables custom sorting of objects and mixed-type arrays. For example, to sort an array of book objects by title, the comparison function could use `object1.title.localeCompare(object2.title)`, which compares strings while respecting Unicode character properties and locale-specific sorting rules.

The method handles arrays of numeric values by converting them to strings and comparing their Unicode code points, which can produce unexpected results for floating-point numbers due to their string representation. For precise numeric sorting, developers should provide custom comparison functions that correctly handle the data type of the elements being sorted.


## Non-array Usage

The `toSorted()` method can be applied to objects with a `length` property and integer-keyed properties, reading these properties and collecting them in the range of 0 to `length - 1`. This allows the method to sort the properties of non-array objects into a new array.

For example, the method handles sparse arrays by treating empty slots as "undefined", ensuring all elements are considered in the sorting process. Consider an array-like object with the following structure:

```javascript

const arrayLike = {

  length: 3,

  unrelated: "foo",

  0: 5,

  2: 4,

  3: 3 // ignored by toSorted() since length is 3

};

```

When calling `Array.prototype.toSorted.call(arrayLike)`, the method produces the output `[4, 5, undefined]`, correctly handling the empty slot at index 1.

The method also demonstrates flexibility when working with non-numeric properties. For instance, consider an array of skills with some undefined values:

```javascript

const skills = ['JS', '', 'Node.js'];

const sortedSkills = skills.toSorted();

console.log(sortedSkills); // Output: ['JS', 'Node.js', undefined]

```

In this case, the sorted array maintains the original skill order while placing undefined values at the end.

To handle custom sorting scenarios, the method accepts an optional comparison function. The comparison function must return -1, 0, or 1 to define the sort order, with negative values indicating that the first argument comes before the second, positive values indicating the second comes before the first, and zero indicating no change to the sort order.

For example, when sorting an array of book objects by title, the comparison function could use `object1.title.localeCompare(object2.title)`, allowing the method to sort the objects based on their title properties while respecting Unicode character properties and locale-specific sorting rules.


## Browser Support

The `toSorted` method requires Node.js 20.0.0 or a modern browser that implements ECMAScript 2023 features. For earlier environments, polyfills are available, though the actual support can vary.

Browser compatibility aligns with the ECMAScript specification, which allows browsers to implement the `sort` method as they see fit. However, the specific implementation details can differ between engines..chrome implements `Array.prototype.sort` using the TimSort algorithm since version 70 (September 2018), while Firefox uses Merge Sort. Both engines are free to implement the function according to their own algorithms, which may differ from the standard implementation.

In practice, the method follows the TC39 proposal for immutability, returning a new sorted array while preserving the original. This behavior is consistent with the ECMAScript 2026 Language Specification, though the exact version support varies between environments. As of 2023, Node.js 14 does not support `toSorted`, despite some documentation suggesting otherwise, highlighting the importance of checking implementation details for specific version compatibility.

For developers working with older environments, polyfills are available via npm or through core-js. These polyfills provide the same functionality as the native implementation, ensuring compatibility across different JavaScript environments.

