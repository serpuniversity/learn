---

title: JavaScript Set clear() Method

date: 2025-05-26

---


# JavaScript Set clear() Method

In JavaScript, the Set data structure provides an efficient way to store unique values. The clear() method, introduced in ECMAScript6, offers a simple yet powerful operation to empty a set entirely. This article explores the syntax, behavior, and practical applications of the clear() method, highlighting its importance in managing dynamic sets and resetting collection states.


## Syntax and Basic Usage

The clear() method removes all elements from a set, making it empty. It is an ECMAScript6 (ES6) feature supported in all modern browsers since June 2017.

The method has no parameters and returns undefined. For example:

```javascript

let myset = new Set([23, 12, 75]);

console.log(myset); // Set(3) { 23, 12, 75 }

console.log(myset.size); // 3

myset.clear();

console.log(myset.size); // 0

```

This method is particularly useful for resetting sets before reusing them or when working with dynamic data that needs to be cleared. It provides a straightforward way to empty collections without manually removing each element.


## Method Implementation

The clear() method is specifically designed to remove all elements from a Set object, leaving it with a size of 0. Unlike the delete() method, which removes specific elements based on their value, clear() removes every element present in the set.

The method's implementation is straightforward and efficient, removing all stored values in a single operation. As with other set methods, clear() operates on the instance to which it belongs, modifying the set's contents directly and returning undefined to indicate successful completion.

This method provides a clean way to reset sets, making them suitable for reuse without manual element removal. Its implementation across major browsers ensures consistent behavior when working with JavaScript sets in modern applications.


## Browser Support

The clear() method is supported in all modern browsers since June 2017, including Google Chrome, Edge, Firefox, Opera, and Safari. As of now, no major browser has removed or deprecated this functionality.

The method's implementation is consistent across browsers, providing a reliable way to empty sets while maintaining efficient performance. For example, the method handles both primitive values and object preferences, making it versatile for various data types.

When comparing clear() to other methods, it offers distinct advantages. Unlike the delete() method, which removes specific elements based on their value, clear() removes every element from the set. This makes clear() particularly useful for resetting sets before reuse or when working with dynamic data that needs frequent clearing.


## Example Usage

The clear() method provides a simple way to reset sets before reusing them. For example:

```javascript

let myset = new Set();

myset.add(23);

console.log(myset); // Set(1) { 23 }

console.log(myset.size); // 1

myset.clear();

console.log(myset.size); // 0

```

This usage demonstrates the method's effectiveness for managing dynamic data that requires frequent clearing. The method's implementation across browsers ensures consistent behavior when working with JavaScript sets in modern applications.


## Differences from delete()

Set.clear() and Set.delete() methods serve distinct purposes in managing the contents of a JavaScript Set object. While clear() removes all elements from the set, delete() removes specific elements based on their value. This fundamental difference in functionality makes each method suitable for different use cases in application development.

The clear() method operates by removing all elements from the set in a single operation, returning undefined to indicate successful completion. This makes it particularly useful for resetting sets before reuse or when working with dynamic data that requires frequent clearing. The method is called without passing any arguments and applies to all elements in the set, making it an efficient way to empty collections.

In contrast, delete() removes specific elements from the set based on their value, returning true if the element existed and was successfully deleted, and false if the element did not exist. This method requires a value parameter and provides additional functionality for checking element existence within the set. The delete() method supports various data types and can be used to both remove elements and verify their presence in the set.

The implementation of these methods demonstrates their distinct approaches to set management. Clear() provides a straightforward way to empty sets, while delete() offers more granular control over individual elements. Together, these methods enable developers to effectively manage set contents based on specific application requirements.

