---

title: JavaScript Set.prototype.isDisjointFrom: A Comprehensive Guide

date: 2025-05-26

---


# JavaScript Set.prototype.isDisjointFrom: A Comprehensive Guide

The JavaScript Set interface offers powerful built-in methods for managing collections of unique values. One particularly useful method, introduced in ES6, is `isDisjointFrom`. This function checks whether two sets have any elements in common, returning true if the sets are disjoint and false otherwise. While its functionality can be extended to work with other set-like objects, it requires careful implementation to ensure compatibility across different data structures and environments. This guide explores the method's definition, usage, and implementation details, demonstrating how to efficiently compare sets while maintaining robust compatibility with modern JavaScript environments.


## Definition and Usage

The **isDisjointFrom** method checks if two sets have no elements in common, returning true if they are disjoint sets and false otherwise. This functionality mirrors similar methods in other programming languages like Python's `isdisjoint()` method, which also determines if two sets or iterables contain no mutual elements.

For execution, the method requires that the secondary argument be a set-like object. This includes actual Set instances, Map objects, and any object implementing the required properties (size, has(), keys()) as specified by the JavaScript `Set` interface. Arrays, however, do not qualify as set-like due to their lack of has() method and size property.

The implementation efficiently determines disjoint status by comparing the smaller set first. If this set has more elements than the other's size, it iterates over the smaller set's keys, checking for element presence in the larger set. Any match results in a false return. If no matches are found after examination of the smaller set's elements, the method returns true.

A related set of operations includes union, intersection, difference, symmetric difference, subset, and superset checking methods. These collectively enable comprehensive set comparison functionality as demonstrated in various implementation examples across different programming languages and libraries.


## Implementation and Compatibility

The es-shim package provides cross-browser compatibility for Set.prototype.isDisjointFrom in environments supporting ES3. The package implements the es-shim API interface and works in ES3-supported environments, using es-set to provide the Set implementation where needed.

The package supports common usage patterns and includes test cases for both Set and Map-based operations. For example:

```javascript

var assert = require('assert');

var isDisjointFrom = require('set.prototype.isdisjointfrom');

var set1 = new Set([1, 2]);

var set2 = new Set([2, 3]);

var set3 = new Set([1]);

assert.equal(isDisjointFrom(set1, set2), false);

assert.equal(isDisjointFrom(set2, set1), false);

assert.equal(isDisjointFrom(set1, set3), false);

assert.equal(isDisjointFrom(set2, set3), true);

assert.equal(isDisjointFrom(set3, set2), true);

```

In addition to the primary method, the package provides implementations for several related set methods including union, intersection, difference, symmetricDifference, isSubsetOf, and isSupersetOf. These collectively enable comprehensive set comparison functionality.


## Related Set Operations

The `Set` class in JavaScript provides several methods for set operations, including `union`, `difference`, `symmetricDifference`, `isSubsetOf`, and `isSupersetOf`, in addition to the `isDisjointFrom` method.

The `intersection` method returns a new set containing elements in both the original set and a given set, making it useful for finding common elements between datasets. The `union` method returns a new set containing all unique elements from both the original set and a given set, perfect for merging lists while automatically handling duplicates.

The `difference` method returns a new set with elements that are in the original set but not in the given set, particularly useful for filtering out unwanted elements. The `symmetricDifference` method returns a new set containing elements that are in either the original set or the given set, but not in both, helping in identifying unique elements between two datasets.

The `isSubsetOf` method checks if all elements of the original set are contained within a given set, returning a boolean. This is useful for validating data subsets, such as permissions or feature sets. The `isSupersetOf` method checks if the original set contains all elements of a given set, also returning a boolean. This is used to verify comprehensive data sets, ensuring no critical elements are missing.

The `isDisjointFrom` method specifically takes a set and returns a new set containing elements in both the original set and the given set. The implementation works efficiently by checking the smaller set first, iterating over its keys and comparing against the larger set. If any match is found, it returns false, while continuing to the next key. If no matches are found after examining the smaller set's elements, it returns true.

The implementation requires that the secondary argument be a set-like object, which must provide three properties: a `size` property containing a number, a `has()` method that takes an element and returns a boolean, and a `keys()` method that returns an iterator of the set's elements. This includes actual Set instances, Map objects, and any object implementing these methods. Arrays are not considered set-like due to their lack of has() method and size property.


## Shim Implementation Details

The es-shim package provides this functionality in ES3 environments through the es-shim API interface. When a compliant environment is detected, the method is implemented directly. However, in non-compliant environments or older browsers, the package falls back to the es-set shim to provide the required functionality.

The package supports common usage patterns and includes test cases for both Set and Map-based operations. It works across node v22 and equivalent Chrome versions, which have Set's isDisjointFrom method but exhibit a bug with set-like arguments containing non-SMI integer sizes.

The implementation requires the secondary argument to implement three properties: a size property containing a number, a has() method that takes an element and returns a boolean, and a keys() method that returns an iterator of the set's elements. This includes actual Set instances, Map objects, and any object implementing these methods. Arrays are not considered set-like due to their lack of has() method and size property.

The shimmed functionality includes related set methods such as union, intersection, difference, symmetricDifference, isSubsetOf, and isSupersetOf, providing comprehensive set comparison functionality. The package is available through npm and includes tests that can be run using `npm test`. It is part of the es-shims project and is licensed under MIT.


## Testing and Usage Examples

The package includes comprehensive test cases for common usage patterns, demonstrating functionality in both Set and Map-based operations. For example:

```javascript

const xx = new Set([4, 5, 6])

const yy = new Set([7, 8])

console.log(xx.isDisjointFrom(yy)) // true

const mapA = new Map([[4, 0], [5, 0], [6, 0]])

const mapB = new Map([[7, 0], [8, 0]])

console.log((new Set(mapA.keys())).isDisjointFrom(mapB)) // true

```

The implementation is thoroughly tested in environments that fully support ES6 Set functionality, including node v22 and equivalent Chrome versions. While these modern browsers implement the `Set.prototype.isDisjointFrom` method, they have a specific bug when dealing with set-like arguments that contain non-SMI integer sizes.

This rigorous testing across multiple versions ensures reliable performance in both set and map-based operations, validating the method's functionality for real-world applications.

