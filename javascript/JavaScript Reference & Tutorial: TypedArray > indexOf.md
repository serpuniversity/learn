---

title: TypedArray.prototype.indexOf()

date: 2025-05-27

---


# TypedArray.prototype.indexOf()

The `indexOf()` method of TypedArray instances searches for the first occurrence of a specified element and returns its index. Implemented with the same algorithm as Array.prototype.indexOf, it provides a powerful way to locate elements within typed arrays. This article explores the method's functionality, including its parameters, return values, and performance characteristics, offering developers valuable insights into modern JavaScript array manipulation.


## Method Overview

The `indexOf()` method of TypedArray instances returns the first index at which a given element can be found in the typed array, or -1 if it is not present. This method has the same algorithm as Array.prototype.indexOf.

The method takes two parameters: `searchElement` and `fromIndex` (optional). The `searchElement` parameter specifies the element to locate in the typed array, while the `fromIndex` parameter specifies the zero-based index at which to start searching, converted to an integer. If `fromIndex` is negative, it is treated as `len + n`, with `k` clamped to 0 if it is less than 0. The method iterates from `k` to `len`, checking for a strict equality match between the element at `k` and `searchElement`.

If the `fromIndex` is omitted, it is treated as 0. If it is greater than or equal to the ArrayLength of the typed array, the method returns -1 without searching. The method throws a TypeError exception if the this value is not an Object or does not have a [[TypedArrayName]] internal slot.

The method has full support across browsers since March 2016. It follows the same algorithm as Array.prototype.indexOf, with the exception that it accesses the this object's [[ArrayLength]] internal slot instead of performing a [[Get]] of "length". If the buffer is detached after ValidateTypedArray is performed, the method returns -1.


## Parameters

The `searchElement` parameter specifies the element to locate in the typed array. This can be any valid JavaScript value, including numbers, strings, objects, and other primitives. The method performs a strict equality comparison (===) between each element in the array and the `searchElement`.

The `fromIndex` parameter, which is optional, specifies the zero-based index at which to start searching. This value is converted to an integer: if it is negative, it is treated as `len + n`, with `k` clamped to 0 if it is less than 0. If `fromIndex` is omitted, the search begins at index 0.

The method returns the first index of `searchElement` in the typed array; -1 if not found. If the element is found multiple times within the specified range, it returns the index of the first occurrence. If the element is not found between the `fromIndex` and the last index of the typed array, it returns -1, even if the element is present later in the array.


## Return Value

The method returns -1 if the length is 0, implementing the same algorithm as Array.prototype.indexOf(). It supports both one- and two-argument calls, with the two-argument form allowing searches to start at a specific index.

When called with one argument, the method returns -1 if fromIndex is greater than or equal to the ArrayLength of the typed array. The implementation throws a TypeError exception if the this value is not an Object or does not have a [[TypedArrayName]] internal slot.

The method checks for matches using strict equality (===) and returns the index of the first found element. If the element is not found between the fromIndex and the last index of the typed array, it returns -1, even if the element is present later in the array. This behavior ensures that searches respect the specified range, making the method particularly useful for targeted array operations.


## Algorithm

The method begins by validating the TypedArray object with ValidateTypedArray. It checks the length of the array - if the length is 0, it immediately returns -1. The method then sets n to ToIntegerOrInfinity(fromIndex), with a default of 0 if fromIndex is undefined. It handles negative indices by setting k to len + n and clamping values below 0 to 0.

Following these initial steps, the implementation enters a loop iterating from k to len. Within this loop, it checks if HasProperty(O, ! ToString(F(k))) to determine if the current position is within the array's bounds. If the position is valid, it retrieves elementK using ! Get(O, ! ToString(F(k))) and performs a strict equality comparison (===) between elementK and searchElement.

Upon finding a match, the method returns the current index F(k). If the loop completes without finding a match, it returns -1. This behavior returns the index of the first occurrence of the searchElement, or -1 if not found, matching the algorithm of Array.prototype.indexOf with the specific array length check replaced by the internal slot access.


## Browser Compatibility

The method has full support across browsers since March 2016, though the specific compatibility across different devices and versions is not detailed in the documentation.

As with Array.prototype.indexOf, TypedArray.prototype.indexOf throws a TypeError exception when invoked as a function, and requires the this value to have a [[TypedArrayName]] internal slot. The method is not generic and can only be called on typed array instances.

The implementation follows the same algorithm as Array.prototype.indexOf, with the exception that it accesses the this object's [[ArrayLength]] internal slot instead of performing a [[Get]] of "length". This means that the method checks for matches using strict equality (===) and returns the index of the first found element or -1 if not found.

The method's performance and compatibility are closely tied to that of Array.prototype.indexOf, which implemented the feature in ES5 (JavaScript 2009) with full support across modern browsers since July 2013. However, specific browser compatibility data is not detailed in the typed array documentation, focusing instead on the feature's availability and implementation across different JavaScript environments.

