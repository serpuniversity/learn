---

title: BigUint64Array in JavaScript

date: 2025-05-26

---


# BigUint64Array in JavaScript

The JavaScript BigUint64Array represents fixed-size arrays of 64-bit unsigned integers, providing precise arithmetic operations for large numeric values. This data type efficiently handles the limitations of JavaScript's standard number precision while offering comprehensive array manipulation capabilities. Through its constructor and methods, BigUint64Array enables developers to work with arbitrary-precision integers, ensuring both performance and accuracy in numeric computations.


## Data Type Overview

The BigUint64Array in JavaScript represents fixed-size arrays of 64-bit unsigned integers, providing an efficient way to work with large numeric values that exceed the standard JavaScript number precision. This data type operates on 8-byte elements and is particularly useful for applications requiring arbitrary-precision integer arithmetic.

To create a BigUint64Array, you can use its constructor with various parameters. For example:

```javascript

const buffer = new ArrayBuffer(32);

const array = new BigUint64Array(buffer, 8, 4);

```

This initializes an array with a specified ArrayBuffer, starting offset, and element count. You can also create an array from an iterable object:

```javascript

const iterable = [150n, 210n, 400n];

const bigUint64Array = new BigUint64Array(iterable);

```

The resulting array can be manipulated using standard array methods. For instance, you can access and modify elements as follows:

```javascript

const bigArray = new BigUint64Array([200n, 300n, 200n, 400n, 700n]);

const subArray = bigArray.subarray(1, 3);

console.log(subArray);

const bigArray = new BigUint64Array([20n, 30n, 30n]);

bigArray[2] = 50n;

console.log(bigArray);

```

The array maintains its length, byte length, and byte offset properties, providing a comprehensive interface for typed array operations. These properties can be accessed through methods like `byte_length()`, `byte_offset()`, and the standard `length` property.


## Implementation and Browser Support

The BigUint64Array constructor creates a new typed array of 64-bit unsigned integers (BigInts), allowing efficient handling and manipulation of large unsigned 64-bit integers. The constructor supports several parameter variations:

```javascript

new BigUint64Array(length) // Creates an array with the specified length

new BigUint64Array(typedArray) // Based on an existing typedArray

new BigUint64Array(object) // From an iterable object containing numeric values

new BigUint64Array(buffer) // Using an ArrayBuffer for underlying storage

new BigUint64Array(buffer, byteOffset) // With a specific byte offset

new BigUint64Array(buffer, byteOffset, length) // Creating a view over a subset of the buffer

```

The constructor returns a new BigUint64Array object with either an explicit length or elements copied from provided typedArray or object. For example:

```javascript

const lengthArray = new BigUint64Array(2); // Array of length 2

const typedArray = new BigUint64Array(lengthArray); // Based on existing lengthArray

const objectArray = new BigUint64Array([21n, 31n]); // From iterable object

const bufferArray = new BigUint64Array(new ArrayBuffer(64), 8, 4); // With specific buffer, offset, and length

```


### Browser Support

The BigUint64Array constructor is supported in major browsers, with initial implementations in:

- Google Chrome 67

- Mozilla Firefox 68

- Microsoft Edge 79

- Safari 15

- Opera 54

While the implementation details are not specified in the documentation, the constructor follows the syntax and behavior of other TypedArray constructors, with parameters matching the expected length, typedArray, object, and buffer specifications. The constructor throws a TypeError when called without the 'new' keyword, consistent with JavaScript constructor syntax.


## Methods and Operations

This constructor supports several parameter variants:

- `new BigUint64Array(length)`: Creates an array with the specified length, all elements initialized to 0n.

- `new BigUint64Array(typedArray)`: Creates a view based on an existing typedArray.

- `new BigUint64Array(object)`: Creates an array from an iterable object containing numeric values.

- `new BigUint64Array(buffer)`: Creates an array using an ArrayBuffer for underlying storage.

- `new BigUint64Array(buffer, byteOffset)`: Creates an array with a specific byte offset.

- `new BigUint64Array(buffer, byteOffset, length)`: Creates a view over a subset of the buffer.

The array maintains its length, byte length, and byte offset properties using properties like `length`, `byteLength`, and `byteOffset`.


### Data Operations

The array supports standard array methods for element access and modification:

```javascript

const bigArray = new BigUint64Array([20n, 30n, 30n]);

bigArray[2] = 50n;

console.log(bigArray);

```


### Element Setting and Getting

The array's elements can be set and retrieved using standard array indexing:

```javascript

const bigArray = new BigUint64Array([200n, 300n, 200n, 400n, 700n]);

bigArray[1] = 350n; // Set second element

const secondElement = bigArray[1]; // Retrieve second element

```


### Subarray Creation

You can create views of subsets of the array using the `subarray` method:

```javascript

const bigArray = new BigUint64Array([200n, 300n, 200n, 400n, 700n]);

const subArray = bigArray.subarray(1, 3);

console.log(subArray);

```


## Interoperability and Conversion

The BigUint64Array data type can be created from various sources including ArrayBuffers, existing typed arrays, iterable objects, and by specifying length, buffer, and offset parameters. Conversion examples include creating arrays from BigInt arrays, object literals, and ArrayBuffer views.

The constructor supports several parameter variations:

- new BigUint64Array(length): Creates an array with the specified length, all elements initialized to 0n

- new BigUint64Array(typedArray): Creates a view based on an existing typedArray

- new BigUint64Array(object): Creates an array from an iterable object containing numeric values

- new BigUint64Array(buffer): Creates an array using an ArrayBuffer for underlying storage

- new BigUint64Array(buffer, byteOffset): Creates an array with a specific byte offset

- new BigUint64Array(buffer, byteOffset, length): Creates a view over a subset of the buffer

The array maintains its length, byte length, and byte offset properties using standard typed array methods. The constructor returns a new BigUint64Array object with the specified length or elements copied from provided typedArray or object.

The API allows interoperable operations with other JavaScript structures. For example, the fill method can be used to set all elements to a specific value, while the buffer accessor property represents the underlying ArrayBuffer. The subarray method returns a new TypedArray on the same ArrayBuffer store with the same element types as the original typedArray object.


## Iteration and Enumeration

The BigUint64Array interface supports iteration through its elements using methods like forEach, as well as following standard iterator protocols. The iteration process involves several key components: the object-to-iterate, callback function, and index management.


### Iteration Process

The iteration starts by converting the BigUint64Array object to an object value using ToObject. The following security checks are performed if the object is a platform object. The process then creates a Function object from the callback function and accesses the list of value pairs to iterate over. For each iteration, the process extracts the current pair's value and key, invoking the callback function with the pair's value, key, and the BigUint64Array object itself. The list of value pairs is updated, and the index is incremented accordingly.


### Iterator Implementation

The BigUint64Array interface implements its iterators using built-in function objects with specific attributes. The keys and values methods return map iterators with kind "key" and "value", respectively, each implemented as a built-in function object with attributes { [[Writable]], [[Enumerable]], [[Configurable]] }. Both methods return 0 for length. The forEach method is implemented similarly, taking three arguments: callbackFn, thisArg, and map. It throws a TypeError if callbackFn is not callable, iterates over map's key-value pairs, converts keys and values to JavaScript values, and calls callbackFn with the specified arguments.


### Interaction with Other JavaScript Structures

The BigUint64Array interface follows standard JavaScript array iteration protocols. For instance, the value iterators use Array.prototype.forEach-like behavior, while pair iterators use Map.prototype.forEach-like behavior. Note that interfaces with indexed properties return actual array iterator objects, and these interfaces must not have attributes, constants, or regular operations named "entries", "forEach", "keys", or "values". The iterator prototype object serves as the prototype for default iterator objects for the BigUint64Array interface.

