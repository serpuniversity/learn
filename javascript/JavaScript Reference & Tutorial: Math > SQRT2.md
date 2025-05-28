---

title: JavaScript's Math Object: SQRT2 Property

date: 2025-05-26

---


# JavaScript's Math Object: SQRT2 Property

In JavaScript, the Math object serves as a comprehensive collection of mathematical functions and constants. These properties and methods provide developers with essential tools for performing calculations, solving mathematical problems, and implementing various algorithms. One particularly useful property within the Math object is SQRT2, which represents the square root of 2. This article explores the properties and usage of Math.SQRT2, highlighting its significance in mathematical computations and its implementation in modern JavaScript environments.


## SQRT2 Property Overview

The Math.SQRT2 property provides the square root of 2, which is approximately 1.4142135623730951. This constant value is part of the broader collection of mathematical properties found within the Math object's namespace.

This property serves as a convenient reference point for developers working on mathematical calculations. Its value is specifically optimized for precision and performance, making it a preferable choice over recalculating the square root of 2 through the Math.sqrt() function every time it's needed.

As a static property of the Math object, Math.SQRT2 can be directly accessed without creating an instance of the Math object. This design choice aligns with the ES1 specification while ensuring consistent behavior across modern JavaScript environments.

The property's value is a constant, meaning it cannot be modified once set. It's classified as not writable, not enumerable, and not configurable, providing a stable foundation for mathematical computations.


## Usage and Implementation

The Math.SQRT2 property returns the square root of 2, providing a precise constant value of approximately 1.4142135623730951. This property serves as an efficient alternative to recalculating the square root of 2 using Math.sqrt(2), as demonstrated in the following examples:

Example 1:

```javascript

console.log(Math.SQRT2); // Output: 
1.4142135623730951

```

Example 2:

```javascript

function get_Value_of_square_root() {

    return Math.SQRT2;

}

console.log(get_Value_of_square_root()); // Output: 
1.4142135623730951

```

The property's direct access and constant value make it particularly useful in mathematical calculations, as shown in this example that utilizes Math.SQRT2 to solve for the square root of 8:

Example 3:

```javascript

const number = 8;

const sqrtOfNumber = Math.sqrt(number) * Math.SQRT2;

console.log(sqrtOfNumber); // Output: 4

```

This approach maintains precision while avoiding redundant calculations, making it a valuable feature of the Math object for developers working with mathematical constants.


## Comparison with Math.sqrt()

The Math.sqrt(2) function and the Math.SQRT2 property differ in their implementation approach. While both provide the square root of 2, the property version offers improved performance through constant caching. This design choice optimizes runtime efficiency by avoiding recalculations of the same value.

The Math object maintains a collection of commonly used mathematical constants, including SQRT2, alongside its array of mathematical functions. This setup mirrors similar implementations for other constants like PI, E, LN2, LN10, LOG2E, and LOG10E, all of which are optimized for precision and performance in calculations.

Modern JavaScript engines implement these constants using internal caching mechanisms, ensuring that each constant returns its precomputed value without performing additional calculations. This approach aligns with ES1 specifications while providing developers with a reliable set of mathematical foundations.


## Browser Support

The Math.SQRT2 property returns the square root of 2, which is approximately 1.4142135623730951. This constant value serves two primary purposes: it provides a precise reference point for mathematical equations, and it offers performance benefits through efficient constant caching.

Modern JavaScript engines implement these constants using internal caching mechanisms to avoid recalculating their values. This approach aligns with ES1 specifications while providing developers with a reliable set of mathematical foundations.


### Browser Compatibility and Usage

The Math.SQRT2 property has been available in all modern browsers since July 2015. This includes support across major browser versions:

- Google Chrome 1 and above

- Internet Explorer 3 and above

- Firefox 1 and above

- Opera 3 and above

- Safari 1 and above

The property can be accessed directly as a static property of the Math object, without the need to create an instance of Math. It returns the precise value 1.4142135623730951 each time it's called, making it a consistent and efficient choice for mathematical calculations in JavaScript.


### Technical Implementation

The property is implemented as a constant, meaning it cannot be modified once set. It's designed to be not writable, not enumerable, and not configurable, ensuring its value remains stable across different runtime environments. This implementation mirrors similar constants in the Math object, such as PI, E, LN2, LN10, LOG2E, and LOG10E, all of which are optimized for precision and performance in calculations.

