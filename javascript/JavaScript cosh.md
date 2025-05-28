---

title: JavaScript Math cosh() Method

date: 2025-05-26

---


# JavaScript Math cosh() Method

The Math.cosh() function in JavaScript calculates the hyperbolic cosine of a number using the formula (e^x + e^-x) / 2. This mathematical operation, which operates as a static method of the Math object, finds applications in engineering, physics, and financial modeling. The function's implementation across major browsers aligns with ECMAScript 6 standards, offering full support since June 2017. While its functionality extends beyond traditional mathematical contexts, developers should note its absence in Internet Explorer versions. The method's reliable cross-platform compatibility makes it a valuable addition to JavaScript projects requiring precise mathematical computations.


## Math.cosh() Overview

The `Math.cosh()` function in JavaScript calculates the hyperbolic cosine of a number, returning a precise value that is essential in engineering, physics, and financial modeling. This mathematical operation is based on the formula (e^x + e^-x) / 2, where e represents Euler's number (approximately 2.71828). The function operates as a static method of the Math object, meaning it must be invoked through the Math placeholder without creating a Math object instance.

The hyperbolic cosine function is defined for all real numbers, including negative values. For example, Math.cosh(0) returns 1, while Math.cosh(1) and Math.cosh(-1) both yield approximately 1.543080634815244, demonstrating the function's symmetry. As expected, Math.cosh(Infinity) and Math.cosh(-Infinity) both evaluate to Infinity, while operations with non-numeric values result in NaN (Not a Number).

The method's implementation across major browsers follows ECMAScript 6 standards, achieving full support since June 2017. Current support includes Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, with consistent implementation across desktop and mobile platforms. While the method provides robust functionality, developers should note its absence in Internet Explorer versions.

In practical applications, developers can employ Math.cosh() for various scientific and engineering calculations. For instance, the function proves valuable in physics simulations, particularly for modeling phenomena like damping or wave behavior. In financial modeling, Math.cosh() can be used to predict growth and decay in hyperbolically modeled investment scenarios, demonstrating its versatility beyond traditional mathematical contexts.


## Function Syntax and Usage

The `Math.cosh()` method requires a single parameter: `number`, which represents the value for which the hyperbolic cosine is to be calculated. The method returns the hyperbolic cosine of the given argument, following the mathematical formula (e^x + e^-x) / 2. For a non-numeric argument, it returns `NaN` (Not a Number).

The method works with both positive and negative inputs, demonstrating its symmetry across the number line. For instance, Math.cosh(0) returns 1, while Math.cosh(1) and Math.cosh(-1) both yield approximately 1.543080634815244, showcasing the function's consistent behavior for both positive and negative inputs.

Special cases include Math.cosh(-Infinity) and Math.cosh(Infinity), both of which evaluate to Infinity, while operations with non-numeric values result in NaN. The method's implementation follows ECMAScript 6 standards, achieving full browser support since June 2017 across modern browsers including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38. Internet Explorer does not support the Math.cosh() method.


## Hyperbolic Cosine Calculation

The hyperbolic cosine function is defined mathematically as (e^x + e^-x) / 2, where e represents Euler's number (approximately 2.71828). This formula serves as the foundation for the implementation of the Math.cosh() method across JavaScript platforms, including browser environments and mathematical libraries like Math.js.

The implementation across platforms consistently applies this formula to calculate hyperbolic cosine values. For example, Math.cosh(0) yields 1, while Math.cosh(1) and Math.cosh(-1) both approximate 1.543080634815244, demonstrating the function's symmetry around the origin. The method produces Infinity for both positive and negative infinity inputs, and returns NaN for non-numeric arguments.

The Math.js library provides an equivalent implementation using its `cosh(x)` function, which computes (1/2) * (exp(x) + exp(-x)). This implementation adheres to the same mathematical principles while offering additional functionality through its support for various number types including BigNumber and Complex values, though these features are not utilized in the standard Math.cosh() implementation across browsers.


## Supported Browsers and Versions

The Math.cosh() method returns precise hyperbolic cosine values across multiple platforms, with full support since June 2017 when ECMAScript 6 standards were implemented. The function is available in all modern browsers, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, as detailed in the official documentation. The implementation consistently follows the formula (e^x + e^-x) / 2, where e represents Euler's number.

Browser compatibility extends to mobile platforms, with support in Chrome Android 38, Firefox Android 25, Opera Android 25, Safari iOS 8, and Samsung Internet 3.0. The method also functions across server environments, supporting versions 0.12 of Node.js and other server-side JavaScript implementations. While widely supported in modern browsers, Internet Explorer does not provide implementation for this feature, as noted in multiple documentation sources.


## Practical Applications

JavaScript's `Math.cosh()` function offers precise calculations for a variety of scientific and engineering applications. In physics simulations, developers can model phenomena like damping or wave behavior through direct function calls, as demonstrated in the example where `Math.cosh(dampingCoefficient * time)` calculates the amplitude for a damped system.

For financial modeling, developers can apply the function to predict growth and decay in hyperbolically modeled investment scenarios. The core example provided shows how to calculate investment outcomes using the formula `initialInvestment * Math.cosh(growthRate * years)`, effectively demonstrating the practical implementation of hyperbolic cosine in financial analysis.

The function's reliable cross-platform compatibility, supported since June 2017 across modern browsers, makes it a valuable addition to any JavaScript project requiring precise mathematical computations. Its foundation in standardized mathematical principles, implemented through the formula (e^x + e^-x) / 2, ensures accurate results that align with both theoretical expectations and practical applications across scientific and engineering domains.

