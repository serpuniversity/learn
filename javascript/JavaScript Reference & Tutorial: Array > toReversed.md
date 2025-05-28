---

title: JavaScript Array toReversed() Method

date: 2025-05-26

---


# JavaScript Array toReversed() Method

In JavaScript, array manipulation is a fundamental operation that developers perform regularly. While there are several methods for working with arrays, the introduction of the toReversed() method in ES2023 adds a more elegant solution for creating a reversed copy of an array. This article explores the functionality of toReversed(), comparing it to existing methods like reverse() and slice().reverse(). We'll examine its implementation, browser support, performance considerations, and provide practical examples of its usage. Additionally, we'll cover how to implement compatibility for older browsers through polyfills and shims, ensuring modern array manipulation techniques are accessible across all development environments.


## What is Array.toReversed()?

The toReversed() method of Array instances returns a new array with elements in reversed order, serving as the copying counterpart to the built-in reverse() method. Unlike reverse(), which modifies the original array, toReversed() returns a distinct array with reversed elements while preserving the original array's state.

This method creates a new array through a process that reads the length property of the target array and visits each property with an integer key between length - 1 and 0 in descending order, adding the value of the current property to the end of the new array. This approach preserves empty slots as undefined in the returned array, making it suitable for sparse arrays where properties may be irregularly spaced.


### Implementation and Browser Support

The method syntax requires no parameters and returns a new array with reversed elements, maintaining the original array's structure. It was introduced as an ES2023 feature and has achieved widespread support across modern browsers, becoming available since July 2023 in Chrome 110, Edge 110, Firefox 115, Safari 16.4, and Opera 96. For developers working with older browsers, polyfills are available to implement this functionality, as detailed in the core-js package.

Developers familiar with array reversal techniques may recognize this method as a more elegant alternative to previous approaches using slice().reverse(). While both methods effectively achieve the same result, toReversed() offers enhanced readability and simplicity by providing a built-in solution for array reversal without modifying the original data.


## Implementation and Usage

The toReversed() method provides a more straightforward approach to array duplication and reversal compared to the older slice().reverse() technique. Here's how you can use it:

```javascript

let actual_array = [60, 78, 90, 34, 67];

console.log("Existing Array: ", actual_array);

let result_array = actual_array.toReversed();

console.log("Final Array: ", result_array);

```

This code will output:

```

Existing Array: [60, 78, 90, 34, 67]

Final Array: [67, 34, 90, 78, 60]

```

As shown in the example, toReversed() creates a new array with the elements in reverse order while leaving the original array unchanged. The original array remains intact, preserving its structure and any empty slots.

For developers working with modern browsers, this built-in functionality simplifies array manipulation. However, for those using older browsers like Internet Explorer 11, alternative implementations are available. Here's a basic polyfill that mirrors the toReversed() behavior using reduceRight():

```javascript

if (!Array.prototype.toReversed) {

  Array.prototype.toReversed = function() {

    return this.slice().reverse();

  };

}

```

This polyfill checks if the toReversed() method is available, and if not, adds it to the Array prototype using the established slice().reverse() technique. This ensures compatibility across all browsers while maintaining the intended functionality.


## Browser Support

The method was introduced as an ES2023 feature and became supported in all major browsers since July 2023. As of the latest updates, Chrome 110, Edge 110, Firefox 115, Safari 16.4, and Opera 96 fully support the Array.prototype.toReversed() method.

This polyfill implementation demonstrates the method's availability in different browser versions: "For developers working with older browsers like Internet Explorer 11, polyfills are available to implement this functionality."

The feature's inclusion in modern browsers' updates follows a typical pattern where browser support becomes available after the operating system receives an update, particularly noticeable on mobile devices where OS updates are tied to firmware installations.

The core-js package implements the es-shim API interface, providing compatibility down to ES3 environments while maintaining specification compliance. This shim implementation exemplifies how the method works: "When Array.prototype.toReversed is present, it returns the same array after reversing. When it's not present, the package provides a shim that can be accessed via toReversed.shim()."

This ESnext spec-compliant shim operates with the following behavior: "The main export takes the array to operate on as the first argument. The package provides three usage examples, including installation via npm: npm install --save array.prototype.toreversed."

For developers requiring broader compatibility, additional polyfill options are available, with one demonstrating the shim's functionality: "When Array.prototype.toReversed is present, use toReversed.shim() to get the shimmed version; verify that Array.prototype.toReversed remains available."

While the method has achieved widespread support, developers should be aware that some older browser versions may still lack implementation: "This feature might not work in older devices or browsers."


## Polyfills and Shims

A native polyfill implementation uses the existing reverse() method to achieve the desired functionality. This approach demonstrates browser compatibility considerations: "This feature might not work in older devices or browsers."

For developers requiring broader compatibility, additional polyfill options are available, including a comprehensive solution from the core-js package. This package implements the es-shim API interface, providing compatibility down to ES3 environments while maintaining specification compliance: "The package implements the es-shim API interface and works in an ES3-supported environment while complying with the proposed spec."

The core-js package offers three primary usage examples:

1. Installation via npm: `npm install --save array.prototype.toreversed`

2. Implementation for non-existent methods: "When Array.prototype.toReversed is not present, delete Array.prototype.toReversed and use toReversed.shim() to get the polyfill. Verify arr.toReversed() works as expected."

3. Shim usage for existing methods: "When Array.prototype.toReversed is present, use toReversed.shim() to get the shimmed version. Verify Array.prototype.toReversed is still available."

The package includes comprehensive testing functionality: "The package includes tests that can be run with npm install and npm test."

A simple, widely supported alternative to the official polyfill uses the reduceRight() method: "When Array.prototype.toReversed is present, use toReversed.shim() to get the shimmed version; verify that Array.prototype.toReversed remains available."

This shim implementation demonstrates the method's compatibility across different browser versions: "The package is described as an ESnext spec-compliant shim/polyfill/replacement for Array.prototype.toReversed that works as far down as ES3."

For developers working with older browsers, the following basic polyfill implementation provides the desired functionality: "When Array.prototype.toReversed is present, it returns the same array after reversing. When it's not present, the package provides a shim that can be accessed via toReversed.shim()."

Developers can implement the polyfill in their projects to support ES2023 features on older browsers: "When used on sparse arrays, toReversed() takes empty slots as if they have the value undefined."


## Performance Considerations

Performance testing reveals significant differences in execution time between Array.prototype.toReversed() and alternative implementation methods. In various browser environments, using toReversed() can result in approximately 20% slower performance compared to equivalent array reversal techniques.

The most efficient approach remains the original slice().reverse() combination, which demonstrates consistent speed advantages in both Chrome and Firefox environments. This variant creates a new array through the slice operation before applying reverse, maintaining optimal performance while ensuring compatibility.

For developers prioritizing performance, the following alternatives offer improved execution times while maintaining array immutability:

1. items.slice().reverse(): A direct combination of slice and reverse operations, known to outperform the toReversed() method.

2. [...items].reverse(): Translates the rest syntax into an array followed by reverse, providing a modern alternative to the slice version.

3. Array.from(items).reverse(): Utilizes Array.from to create a new array before applying reverse, demonstrating similar performance characteristics to the slice variant.

These optimized approaches provide developers with efficient options for array reversal while maintaining the immutability of the original array data. For projects requiring minimal performance impact, the native slice().reverse() combination remains the recommended implementation strategy.

