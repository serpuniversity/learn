---

title: BigInt64Array in JavaScript

date: 2025-05-26

---


# BigInt64Array in JavaScript

JavaScript's `BigInt64Array` provides a robust way to work with 64-bit integers in the browser and Node.js environments. This article explains how to create and manipulate `BigInt64Array` instances, covering its constructor options, array methods, and performance considerations. You'll learn about its compatibility across browsers and Node.js, from the latest stable versions to older support levels. Whether you're developing for desktop or mobile, understanding `BigInt64Array` is crucial for handling large integer values efficiently in JavaScript.


## Constructor and Initialization

The BigInt64Array constructor creates instances of the BigInt64Array object, with initial values determined by the constructor itself. It offers several creation options including specification of length, initialization from typed arrays or objects, and direct ArrayBuffer manipulation.


### Constructor Parameters and Behavior

The constructor accepts several parameters:

- `new BigInt64Array()` creates an array of default length 0.

- `new BigInt64Array(length)` initializes an array with the specified length.

- `new BigInt64Array(typedArray)` creates a new array from an existing array-like structure.

- `new BigInt64Array(object)` initializes from an iterable object.

- `new BigInt64Array(buffer)` creates with an ArrayBuffer for storage.

- `new BigInt64Array(buffer, byteOffset)` creates with specified buffer offset.

- `new BigInt64Array(buffer, byteOffset, length)` creates with specific offset and length.


### Static Properties and Methods

The constructor has static properties:

- `BYTES_PER_ELEMENT` returns 8, indicating the element size.

- `name` returns "BigInt64Array" as the constructor function name.


### Browser Compatibility

The constructor has wide browser support, with full implementation in Chrome 67, Firefox 68, Edge 79, Safari 15, and Opera 54. It is available in other environments including Node.js 10.4.0 and mobile browsers starting from Android WebView 67 and Safari iOS 15.


## Array Operations and Methods

The BigInt64Array object provides several standard array methods for manipulating and processing 64-bit signed integers:


### Mapping and Transformation

The map() method applies a callback function to each element in the array, producing a new array containing the results. The callback function receives the current element, its index, and the array itself as arguments.

```js

const result = myBigUintArray.map((value, index, array) => {

  // Transformation logic

});

```


### Aggregation

The reduce() and reduceRight() methods iterate over the array elements, applying a reducing function to accumulate a single value. Both methods accept an accumulator value and return the final result.

```js

const initialValue = 0n;

const result = myBigUintArray.reduce((accumulator, currentValue, index, array) => {

  // Reduction logic

}, initialValue);

```


### Array Manipulation

The reverse() method reverses the order of the array elements, while the set() method copies values from another array into the current array, converting them to 64-bit integers.

```js

myBigUintArray.reverse();

myBigUintArray.set(otherArray);

```


### Subarray Operations

The subarray() method returns a new BigInt64Array containing a portion of the original array. This method is particularly useful for accessing or manipulating subsets of the array.

```js

const subarray = myBigUintArray.subarray(startIndex, endIndex);

```


### Sorting and Searching

The sort() method sorts the array elements in place, while the lastIndexOf() method returns the last index of a specified value. Both methods allow specifying a custom comparison function for advanced sorting logic.

```js

myBigUintArray.sort((a, b) => {

  // Comparison logic

});

const lastIndex = myBigUintArray.lastIndexOf(searchValue);

```


## Data Access and Manipulation

The `BigInt64Array` constructor creates instances of the 64-bit signed integer array object, with initial values determined by the constructor itself. The constructor supports several creation options:


### Array Creation Options

- **From a length**: `new BigInt64Array(2)` creates an array of length 2 with all items initialized to 0.

- **From an array**: `new BigInt64Array([21n, 31n])` creates a new array from the provided values.

- **From another TypedArray**: `const y = new BigInt64Array(x)` creates a view on the source TypedArray.

- **From an ArrayBuffer**: `const buffer = new ArrayBuffer(64); const z = new BigInt64Array(buffer, 8, 4)` creates a view with specified buffer offset and length.

- **From an iterable**: `(function* () { yield* [1n, 2n, 3n]; })(); const bigint64FromIterable = new BigInt64Array(iterable)` creates a new array from the iterable's values.


### Array Properties

The `BigInt64Array` instance has several properties for accessing its underlying data:

- `buffer`: Returns the underlying ArrayBuffer.

- `byteLength`: Returns the total length of the array in bytes.

- `byteOffset`: Returns the offset in bytes from the beginning of the ArrayBuffer.

- `length`: Returns the number of elements in the array (1 greater than the index of the last item).


### Array Methods

The `BigInt64Array` instance provides several methods for manipulating its contents:

- `copyWithin()`: Copies a sequence of array elements within the array.

- `entries()`: Returns an iterator for the array's elements.

- `every()`: Tests whether all elements pass a provided test function.

- `fill()`: Fills all elements of the array with a static value.

- `filter()`: Creates a new array with elements that pass a provided filtering function.

- `find()`: Returns the found value in the array if an element satisfies the provided testing function, or `undefined` if not found.

- `findIndex()`: Returns the found index in the array if an element satisfies the provided testing function, or -1 if not found.

- `forEach()`: Calls a function for each element in the array.

- `includes()`: Determines whether the array includes a certain element, returning `true` or `false`.

- `indexOf()`: Returns the first (least) index of an element within the array equal to the specified value, or -1 if none is found.

- `join()`: Joins all elements of the array into a string.

- `keys()`: Returns a new Array Iterator containing keys for each index in the array.

- `lastIndexOf()`: Returns the last index of an element within the array equal to the specified value, or -1 if none is found.


## Browser Compatibility and Support

The `BigInt64Array` constructor has achieved significant browser compatibility, with full implementation in modern versions of Chrome, Firefox, Edge, Safari, Opera, and Node.js environments. As of the latest data, 92% of global browsers support the constructor, making it a safe choice for development.

The current implementation status across major browser engines is as follows:

- Chrome: 26% support as of version 67, with 36% of Chrome Android users running supported versions

- Safari: 5% native support as of version 15, with 15% support on iOS as of version 15

- Firefox: 2% support as of version 68, with 2% on Android as of version 68

- Edge: 5% support as of version 79

- Safari on iOS: 15% native support as of version 15, with 93% native support as of version 15+

- Samsung Internet: 2% support as of version 9, with 93% support as of version 9+

- WebView Android: 100% support as of version 67

The constructor returns a new `BigInt64Array` object that represents the underlying value, inheriting instance methods from its parent `TypedArray` object. The available creation options include specifying length, initializing from typed arrays or objects, and direct `ArrayBuffer` manipulation. The constructor also provides static properties including `BYTES_PER_ELEMENT` (8) and `name` ("BigInt64Array"), with the former accessible even from object instances while the latter requires accessing the constructor directly via `arr.constructor.name`.


### Technical Implementation

From a technical standpoint, the constructor utilizes JavaScript's internal 64-bit representation while working with `BigInt` values to maintain precision. This implementation builds upon the existing 32-bit integer capabilities of `Int32Array` and `Uint32Array` by extending the data type to 64 bits. As explained in the documentation, this approach enables developers to handle large integer values safely within the constraints of JavaScript's floating-point arithmetic.

Given the browser landscape, developers can rely on the following support levels:

- Full support in Chrome 67+, Firefox 68+, Edge 79+, Safari 15+, Opera 54+, Node.js 10.4+, and WebView Android 67+

- Partial or experimental support in older versions, though specific compatibility data is not detailed in the sources


## Performance Considerations

Performance optimization is crucial when working with `BigInt64Array`, particularly given the fixed size of 8 bytes per element. The underlying representation uses JavaScript's internal 64-bit integer format, ensuring efficient memory usage but limiting each element to 8 bytes.


### Memory Management and Usage

Implementation details indicate that `BigInt64Array` provides direct access to memory through its parent `TypedArray` object, which can be both an advantage and limitation. The array stores values using `BigInt` types internally, allowing precise integer representation. However, this design leads to overhead compared to traditional integers when performing arithmetic operations due to the additional handling required for `BigInt` conversions.

The `BYTES_PER_ELEMENT` property consistently returns 8, reflecting the fixed size of each element. This uniformity makes it easier to manage memory buffers but restricts flexibility compared to dynamically sized types.


### High-Level Performance Considerations

While `BigInt64Array` enables efficient storage of large integers, performance-critical applications may face limitations. Arithmetic operations on `BigInt` values generally perform worse than operations on native integers, making simple numerical processing potentially slower. For applications requiring high throughput, developers should consider fallbacks or alternative data structures based on browser support and usage patterns. 


### Optimization Techniques

In scenarios where full precision is not required, using regular 64-bit integers through `Int64Array` or `Uint64Array` may offer better performance. Developers should measure specific use cases to determine the optimal approach. For large datasets or computational tasks, implementing custom memory management or leveraging WebAssembly for intensive operations can provide significant speed improvements.


### Browser-Specific Performance

Performance varies between browser implementations. Edge and Chrome show the highest native support, while Safari and Firefox have lower native implementation rates. Developers should test performance across target environments, particularly when optimizing for older browsers or mobile devices where JavaScript execution speed can vary significantly.

