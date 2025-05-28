---

title: JavaScript toString() Method

date: 2025-05-26

---


# JavaScript toString() Method

JavaScript's toString() method provides a versatile way to convert objects to strings, with distinct implementations for Function objects and all other objects. While developers rarely call toString() directly, understanding its behavior is crucial for effective JavaScript development. This comprehensive look at toString() covers its inner workings, parameter handling, and practical applications in everything from cross-window communication to custom object representations.


## Introduction to toString()

The toString() method is a fundamental feature of JavaScript, built into every object to provide a string representation of its value. This built-in capability enables JavaScript to convert objects to text or use them in string contexts, though developers rarely call it directly in their code.

Two distinct forms of toString() exist: one for Function objects and another for all other objects, including arrays and numbers. The Function.prototype.toString() method returns the source code of a function as a string, a feature available since the language's earliest specification in 1997. This method always returns the exact source code, including any comments, making it a powerful tool for inspecting function definitions.

For other objects, Object.prototype.toString() provides a default implementation that returns "[object Object]" when called. This method can be overridden by developers to customize object string representations. When converting numeric values to strings, the number.toString() method handles this internally, allowing specification of the number's base between 2 and 36 for base conversion.

The method's behavior varies across object types: arrays use the Array.prototype.toString() implementation to produce comma-separated values, while functions return their source code. When called on objects that implement Symbol.toPrimitive, JavaScript first attempts to convert the object using that method before falling back to toString(). This flexible approach allows developers to control how their objects behave in string contexts while providing sensible defaults for built-in types.


## Function.prototype.toString

Function.prototype.toString returns the source code of the function as a string, a feature dating back to ECMAScript1 (1997). This method always returns the exact source code, including any interspersed comments, providing developers with direct access to the function's definition.

When called on built-in function objects, Function.prototype.toString adheres strictly to the source code used to create the function. Even bound functions and other non-JavaScript functions produce native function strings in the format "function someName() { [native code] }". For intrinsic object methods and functions, the method returns the initial name of the function, though the content may be implementation-defined.

The standard behavior of toString is demonstrated through various examples:

```javascript

function f() {}

console.log(f.toString()); // Output: function f() {}

```

```javascript

const g = () => "Hello World!";

console.log(g.toString()); // Output: () => "Hello World!"

```

The method handles different types of functions effectively:

```javascript

// Function

console.log(f.toString()); // Output: function f() {}

// Class method

class A {}

A.prototype.g = function() {};

console.log(A.prototype.g.toString()); // Output: function g() {}

// Generator function

function* h() {}

console.log(h.toString()); // Output: function* h() {}

// Arrow function

const k = a => a;

console.log(k.toString()); // Output: function k(a) { return a; }

// Method property

const obj = { m: function() {} };

console.log(obj.m.toString()); // Output: function m() {}

```

For getter and setter descriptors, toString returns their respective source code:

```javascript

const l = {

  get prop() {} // Returns getter function source code

  set prop(value) {} // Returns setter function source code

};

console.log(l.prop.toString());

```

Developers can leverage toString for both reading and modifying functions dynamically:

```javascript

function original() { console.log('Original'); }

console.log(`${original}`); // Output: function original() { console.log('Original'); }

const modified = new Function('console.log("Modified")');

console.log(modified.toString()); // Output: function anonymous() { console.log("Modified"); }

```

When applied to non-function objects, Function.prototype.toString throws a TypeError, maintaining strict type validation and preventing accidental conversions.


## Object.prototype.toString

Every JavaScript object inherits a toString method that, by default, returns "[object Object]". This default implementation provides a standardized way for JavaScript to represent objects as text, though developers can override this behavior to customize object string representations.

The method's primary purpose is to convert objects to string representations that JavaScript can use in various contexts, such as displaying objects in HTML or using them within string operations. While developers rarely call toString() directly in their code, the method plays a crucial role in JavaScript's internal operations for handling object conversions.

The default "[object Object]" representation follows a consistent pattern across JavaScript objects, providing a fallback for objects that don't implement a custom toString method. This fallback ensures that all objects can be converted to strings without modification, while allowing developers to provide more meaningful string representations through custom implementations.


## toString() with Parameters

The toString() method of Number values returns a string representing the number value according to ECMAScript specifications. This method provides two forms of conversion: the default decimal representation and conversions to other bases between 2 and 36.

The method accepts an optional radix parameter to specify the base for the conversion:

```javascript

num.toString() // Default decimal conversion

num.toString(radix) // Custom base conversion

```

The radix must be an integer within the range of 2 to 36. Values outside this range will result in a RangeError, while non-number inputs will throw a TypeError.

For negative numbers, toString() preserves the sign, returning the positive binary representation for radix 2 while representing other bases correctly. Zero values, both 0 and -0, convert to the string "0".

The method handles various numeric representations effectively:

```javascript

console.log(-123.toString(2)) // Output: "-1111011"

console.log(255.toString(16)) // Output: "ff"

console.log(Math.PI.toString(8)) // Output: "3.1130216497040266"

```

Special cases are handled as follows:

```javascript

console.log(NaN.toString()) // Output: "NaN"

console.log(Infinity.toString()) // Output: "Infinity"

```

When converting large numbers (beyond Number.MAX_SAFE_INTEGER), the method may produce multiple valid representations, selecting the one with the most trailing zeroes.


### Base Conversion Mechanics

The implementation processes the conversion through several key steps:

1. Validation of the radix parameter

2. Conversion of the number value using ThisNumberValue

3. Handling negative numbers by prepending a hyphen

4. Calculation of exponent and mantissa based on the specified radix precision

5. Formatting the result as a string, handling special cases and precision limits


## Common Use Cases

The toString() method's most practical applications emerge through its foundational use in modern JavaScript development. It enables developers to convert objects to strings in a consistent, reliable manner, leveraging the language's core functionality for common tasks.


### Visual Studio Intellisense Support

Visual Studio leverages toString() to process XML code comments, providing enhanced autocomplete and documentation features. For example, when documenting a function with XML comments like this:

```javascript

function areaFunction(radiusParam) {

  /// <summary>Determines the area of a circle based on a radius parameter.</summary>

  /// <param name="radius" type="Number">The radius of the circle.</param>

  /// <returns type="Number">Returns a number that represents the area.</returns>

  var areaVal;

  areaVal = Math.PI * radiusParam * radiusParam;

  return areaVal;

}

```

The editor uses the function.toString() method to parse these XML comments, extracting detailed information about the function's parameters and return type for improved code assistance and documentation.


### Function Serialization for Cross-Window Communication

In multi-window applications, this method plays a crucial role in function sharing between windows. When a function needs to be executed asynchronously or in a different window context, developers can serialize the function using its source code representation. This approach ensures compatibility even if the original window is no longer available.

For example, a function might be saved to local storage or sent between windows for later execution:

```javascript

// Save function to local storage

localStorage.setItem('areaFunction', areaFunction.toString());

// Later, in another window context

const serializedFunction = localStorage.getItem('areaFunction');

const dynamicFunction = new Function(serializedFunction);

```

This capability enables complex asynchronous operations and cross-window communication patterns while ensuring compatibility across different execution contexts.


### Custom Object String Representation

Developers commonly override the default toString() method to provide more meaningful string representations for custom objects. This customization enhances debugging and logging by displaying relevant information about object state. For instance:

```javascript

class Circle {

  constructor(radius) {

    this.radius = radius;

  }

  toString() {

    return `Circle with radius ${this.radius}`;

  }

}

const circle = new Circle(5);

console.log(circle.toString()); // Output: Circle with radius 5

```

This approach provides a flexible way to control how objects are displayed in text contexts, improving code readability and maintainability.


### TrustedScript for Secure String Conversion

The toString() method's implementation in the TrustedScript interface enables safe string conversion for sanitized scripts. This feature, while not Baseline and with limited browser support, provides developers with a powerful tool for maintaining security in script execution.

When used through Trusted Types policies, this method returns a sanitized string that can be safely executed as a script, preventing common security vulnerabilities associated with improper string handling. This application highlights the method's versatility in modern web development frameworks and security-conscious environments.

