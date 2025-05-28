---

title: JavaScript Map clear() Method

date: 2025-05-26

---


# JavaScript Map clear() Method

JavaScript's Map object provides a powerful way to associate keys with values, offering efficient storage and retrieval capabilities. However, managing the lifecycle of Map objects requires careful consideration of memory management and data persistence. The clear() method offers a straightforward approach to removing all elements from a Map, making it an essential tool for developers working with dynamic data structures. In this article, we'll explore the features, implementation, and implications of the clear() method, comparing it to alternative approaches and examining its behavior across modern browsers and use cases.


## Syntax and Usage

The clear() method removes all elements from a JavaScript Map object, returning nothing (undefined). Supported in all modern browsers since June 2017, including Chrome 51, Edge 15, Firefox 54, Safari 10, and Opera 38, with full compatibility across major browsers as of July 2015. The method syntax is map.clear(), requiring no parameters.

The implementation works by removing all [key, value] pairs from the internal Map Hash, though it does not clear object properties directly. To clear a Map, the method runs with O(n) algorithm execution in the garbage collector thread, where n represents the number of elements. This process is independent of the map's size and allows the garbage collector to clear all key and value objects simultaneously.

While the clear() method removes references to other objects, making them eligible for garbage collection, it's important to note that garbage collection itself is not immediate. The collector operates based on workload and memory reorganization, potentially delaying the cleanup of unreferenced objects. Modern garbage collectors can perform this process in another thread or core, reducing the visible impact on performance.


## Example Usage

```javascript

const myMap = new Map();

myMap.set("bar", "baz");

myMap.set(1, "foo");

console.log(myMap.size); // 2

console.log(myMap.has("bar")); // true

myMap.clear();

console.log(myMap.size); // 0

console.log(myMap.has("bar")); // false

```

The `map.clear()` method takes no parameters and returns undefined, effectively removing all key-value pairs from the Map object. This operation marks all keys and values eligible for garbage collection, though the actual process may occur during subsequent garbage collection cycles rather than immediately.

The `clear()` method operates with O(n) complexity, where n represents the number of elements in the map. While this process is independent of the map's size, it's important to consider that even unreferenced keys and values remain in memory until garbage collection occurs.

To further illustrate the method's functionality, consider the following example:

```html

<html>

<head>

<title>JavaScript Map Clear Example</title>

</head>

<body>

<script type="text/javascript">

let mapVar = new Map();

mapVar.set('key1', 'value1');

mapVar.set('key2', 'value2');

console.log(mapVar.size); // Output: 2

mapVar.clear();

console.log(mapVar.size); // Output: 0

</script>

</body>

</html>

```

This example demonstrates the method's behavior when applied to a map with two elements. After calling `clear()`, both the map's size and its content are reduced to zero. This operation serves as a final step in cleaning up map data, ensuring that all associated key-value pairs are removed from memory.


## Performance Considerations

When comparing Map.clear() to creating a new Map instance, several performance considerations emerge. The clear() method, while removing references to key-value pairs, still requires garbage collection overhead. Modern JavaScript engines can manage this process efficiently across multiple threads, though specific performance impacts depend on implementation details and memory configuration.

The fundamental difference lies in object lifecycle management. Using clear() maintains the same object reference while cleaning its contents, a process that requires O(n) operations for both the clear process and subsequent garbage collection. In contrast, creating a new Map instance adds additional overhead: the old map must be garbage collected, a process that includes both key-value objects and the map itself, resulting in O(n+1) operations.

For local Map usage, particularly in single-threaded environments like desktop applications, clear() generally offers better performance due to reduced memory allocation. However, in multi-threaded or garbage collection-intensive scenarios, the cost of managing multiple map objects becomes significant. The decision to use clear() or create a new instance depends heavily on application context: if the map is not referenced elsewhere and memory management efficiency is crucial, clear() provides the most direct approach.

Concurrency is another critical factor. Multi-threaded applications, especially those managing singleton class properties, must carefully handle map clearing to avoid modification exceptions. In these cases, creating a new map instance ensures consistent operation across threads, though it introduces its own overhead of managing multiple map references.


## Browser Support

The clear() method is supported across all modern browsers since July 2015, with specific support details as follows:

- Chrome: Available since Chrome 51 (June 2017)

- Edge: Available since Edge 15 (June 2017)

- Firefox: Available since Firefox 54 (July 2015)

- Safari: Available since Safari 10 (July 2015)

- Opera: Available since Opera 38 (July 2015)

The method is fully compatible with major browsers, though Internet Explorer does not support it. Common usage includes clearing a map with two elements, as shown in the example:

```javascript

let map = new Map();

map.set('bar', 'baz');

map.set(1, 'foo');

console.log(map.size); // 2

map.clear();

console.log(map.size); // 0

```

Performance considerations demonstrate that while the method removes references to key-value pairs, garbage collection overhead remains. Modern JavaScript engines manage this process across multiple threads. For applications where memory management efficiency is crucial, particularly in single-threaded environments like desktop applications, clear() generally offers better performance due to reduced memory allocation.

When comparing map operations, the delete() method removes a specific key-value pair rather than the entire structure. The clear() method's primary purpose is to remove references to other objects, allowing key-value pairs to be garbage collected if the map is not referenced elsewhere. This process requires O(n) algorithm execution in the garbage collector thread, where n represents the number of elements. The actual garbage collection may occur during subsequent cycles rather than immediately.


## Comparison with Similar Methods

The delete() method removes a specific key-value pair from a Map, returning true if successful and false if the key doesn't exist. In contrast, the clear() method removes all elements from the map, returning undefined and making the map empty.

A significant difference lies in their garbage collection behavior. The clear() method, while removing references to key-value pairs, still requires garbage collection overhead during the O(n) algorithm execution in the garbage collector thread. In contrast, the delete() method directly removes references to individual elements, making them eligible for garbage collection immediately if not otherwise referenced.

Performance considerations show that using clear() is generally more efficient for managing entire map structures, especially in single-threaded environments like desktop applications. This approach maintains the same object reference while cleaning its contents, allowing key-value pairs to be garbage collected if the map is no longer referenced elsewhere.

For multi-threaded applications, particularly those managing singleton class properties, the clear() method requires careful handling to avoid concurrency modification exceptions. In these cases, creating a new map instance ensures consistent operation across threads while avoiding the overhead of managing multiple map references.

When comparing similar methods, it's important to note that the delete() method provides more granular control over map contents, allowing developers to manage specific elements rather than entire structures. The clear() method's primary purpose is to remove references to other objects, making its contents eligible for garbage collection without altering the map's reference.


### Map vs. Null Assignment

The documentation also discusses the implications of setting a Map to null versus using clear(). When setting a map to null, the garbage collector must clear both the key-value objects and the map structure itself, resulting in O(n+1) operations. In contrast, using clear() allows the existing map structure to remain while removing all key-value pairs, which the collector can then process in O(n) operations.

This difference becomes particularly relevant when considering collection efficiency and memory management. Modern JavaScript engines are optimized to handle these operations across multiple threads, though specific performance impacts depend on implementation details and memory configuration. The choice between these approaches should consider the application's specific memory management requirements and concurrency needs.

