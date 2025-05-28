---

title: Float16Array: JavaScript's 16-bit Floating-Point Array

date: 2025-05-27

---


# Float16Array: JavaScript's 16-bit Floating-Point Array

JavaScript's Float16Array represents a crucial advancement in web development, offering developers a powerful tool for optimizing memory usage in floating-point calculations. By utilizing the IEEE 754 binary16 format, these 16-bit floating-point arrays consume just 2 bytes per element—half the memory of standard 32-bit floats—making them particularly valuable for mobile devices and GPU-accelerated applications. While sacrificing some precision compared to their 32-bit and 64-bit counterparts, Float16Array strikes an optimal balance for scenarios where basic floating-point operations suffice. The array's implementation closely mirrors other JavaScript typed arrays, yet introduces unique methods for precise data manipulation and memory optimization. Understanding this specialized data structure is essential for developers working at the intersection of web technologies and high-performance computing.


## Introduction to Float16Array

As the second smallest IEEE floating point format, the 16-bit half-precision float represents numbers using 1 sign bit, 5 exponent bits, and 10 significand bits. This format consumes just 2 bytes per element, compared to 4 bytes for 32-bit floats (Float32Array) and 8 bytes for 64-bit floats (Float64Array), making it particularly valuable for memory-constrained environments where only basic floating-point precision is needed.

The Float16Array specification closely follows the IEEE 754-2008 binary16 format, providing robust support for GPU applications through its alignment with OpenGL and WebGL specifications. The array operates similarly to other JavaScript TypedArray types like Uint8Array and Float32Array, providing methods for standard operations such as mapping, filtering, and slicing.

Developed specifically for interoperation with GPU memory, the Float16Array offers advantages in both data transfer and processing. Modern GPU architectures, including those for both desktop and mobile platforms, natively support half-float textures and vertex data through extensions like ARB_half_float_pixel, OES_texture_float, and WebGL's OES_texture_half_float. While some early implementations faced challenges with rounding accuracy and required complex conversion routines, current browsers support the format through specialized hardware acceleration.


## Technical Specifications and Browser Support

The Float16Array constructor creates new Float16Array objects using several parameters. It can initialize with:

- `new Float16Array()`: Creates an empty array

- `new Float16Array(length)`: Creates an array of specified length

- `new Float16Array(typedArray)`: Copies values from an existing typed array

- `new Float16Array(object)`: Transfers data from another object

- `new Float16Array(buffer)`: Creates array from ArrayBuffer

- `new Float16Array(buffer, byteOffset)`: Creates array from specific ArrayBuffer region

- `new Float16Array(buffer, byteOffset, length)`: Creates array with specific region and length

The constructor supports multiple data types, including Arrays, DOMStrings, and ArrayBufferViews. It operates on the ArrayBuffer and provides standard TypedArray methods like map, filter, and slice, while adhering to the IEEE 754-half-precision format constraints. The constructor functions effectively with the latest device and browser versions since implementation in April 2025.


## Memory and Precision Comparison

Each element in a Float16Array occupies 2 bytes, significantly reducing memory consumption compared to the 4 bytes required for Float32Array or the 8 bytes needed for Float64Array. This reduced memory footprint makes Float16Array particularly suitable for applications with strict memory constraints, such as mobile devices and GPU-accelerated computations.

The precision of Float16Array is limited to approximately 3 decimal digits, with a range of ±65,504. While this limits the maximum representable value compared to Float32Array and Float64Array, it often provides sufficient precision for applications where higher precision is not necessary. This balance of reduced memory usage with adequate precision makes Float16Array an ideal choice for scenarios where standard floating-point operations can be performed using the smaller format.


## API Implementation and Methods

The Float16Array constructor creates typed arrays of 16-bit floating-point numbers, requiring an ArrayBuffer and optionally a start index and length. This constructor enables efficient memory management and specialized data handling while maintaining compatibility with existing JavaScript typed array operations.

Each Float16Array instance can be created using multiple methods, including:

- From an ArrayBuffer: `const buffer = new ArrayBuffer(32); const z = new Float16Array(buffer, 4, 4); console.log(z.byteOffset); // 4`

- From an iterable: `const iterable = (function* () { yield* [1, 2, 3]; })(); const float16FromIterable = new Float16Array(iterable); console.log(float16FromIterable); // Float16Array [1, 2, 3]`

The constructor returns a valid Float16Array object, with the `BYTES_PER_ELEMENT` property consistently returning 2, regardless of the underlying data type. This attribute distinguishes Float16Array from other typed array classes, which return false when checked with `TypedArray.isTypedArray`.

The Float16Array implementation includes several utility methods for precise data manipulation:

- `getFloat16(index)`: Retrieves a 16-bit floating-point value from the specified index

- `setFloat16(index, value)`: Sets a 16-bit floating-point value at the specified index

- `f16round(value)`: Returns the nearest 16-bit float representation of a number, similar to `Math.fround`

For data interaction with other JavaScript elements, Float16Array requires special considerations:

- `ArrayBuffer.isView` returns false for Float16Array instances

- `structuredClone` cannot clone Proxy objects like Float16Array instances

- WebGL requires Uint16Array for buffer or texture data of type `gl.HALF_FLOAT` (WebGL 2) or `ext.HALF_FLOAT_OES` (WebGL 1 extension), and cannot use Float16Array directly with `gl.bufferData` or `gl.texImage2D`

The Float16Array constructor operates across the latest devices and browser versions since implementation in April 2025, providing efficient memory management and specialized data handling for modern GPU-accelerated computing.

