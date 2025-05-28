---

title: Set Operations in JavaScript: Union and Intersection

date: 2025-05-27

---


# Set Operations in JavaScript: Union and Intersection

JavaScript's Set data structure provides powerful tools for managing collections of unique elements. At its core, the Set enables efficient membership testing and iteration, but its true potential shines through the recently introduced operations like union, intersection, and difference. In this article, we'll explore how to perform set union in JavaScript, from basic implementation patterns to the theoretical foundations of this fundamental operation in set theory. We'll examine practical code examples, including the use of the spread operator and add() method, and discuss browser support for these features. Additionally, we'll look at how union operations fit into the larger landscape of set theory and JavaScript's implementation of set-based Boolean algebra. Get ready to deepen your understanding of JavaScript's Set API and its mathematical underpinnings.


## Introduction to Set Operations

The union operation creates a new set containing all elements that exist in any of the two sets at least once [1]. This mathematical concept is implemented in JavaScript's Set data structure through the union method, which combines elements from both sets [2].

To implement union using the spread operator, you can create a new Set from the combined elements of both sets [3]. For example:

```javascript

const setA = new Set([1, 2, 3]);

const setB = new Set([4, 2, 5]);

const unionSet = new Set([...setA, ...setB]);

console.log(unionSet); // Set { 1, 2, 3, 4, 5 }

```

Alternatively, you can use the add() method to populate a new Set with elements from both sets [3]. This approach requires iterating over one set and adding each element to a new Set:

```javascript

function showUnion(sA, sB) {

  const unionSet = new Set(sA);

  for (const num of sB) {

    unionSet.add(num);

  }

  return unionSet;

}

const set1 = new Set(['1', '6', '8']);

const set2 = new Set(['2', '3', '4']);

console.log(showUnion(set1, set2)); // Set { '1', '6', '8', '2', '3', '4' }

```

The union operation is particularly useful for combining data from multiple sets while maintaining uniqueness [4]. It forms the basis for more complex set operations and can be applied to various data structures, including arrays and other iterables [5].


## Union Method Implementation

The union operation creates a new set containing all unique elements from both input sets [6]. This fundamental set operation combines the elements of two sets into a single collection [7].

The implementation of union in JavaScript's Set data structure follows these patterns:

- Using the spread operator: Create a new Set by combining elements from both input sets [8]. This approach automatically handles uniqueness, as Sets only store distinct values [9].

- Using add() method: Initialize a new Set with elements from the first input, then iterate over the second input and add elements to the new Set [10]. This pattern ensures all elements from both sets are included [11].

The union operation forms the basis for more complex set operations and is particularly useful for combining data while maintaining uniqueness [12]. It represents the aggregation of elements from multiple sets into a single collection [13].


## Set Theory Foundations

The union operation combines elements from multiple sets into a single collection, maintaining uniqueness through the fundamental property that the union of sets is defined as \(A \cup B = \{x: x \in A \text{ or } x \in B\}\) [14]. This mathematical concept forms one of the core operations in set theory, alongside intersection and difference [15].

The union operation follows several key properties that define its behavior within set theory [16]. These include:

- Commutativity: The union of two sets remains unchanged by the order of operands, i.e., \(A \cup B = B \cup A\).

- Associativity: Multiple union operations can be performed in any order without affecting the result, represented as \((A \cup B) \cup C = A \cup (B \cup C)\).

- Identity: The union of any set with the empty set yields the original set, expressed as \(\emptyset \cup A = A\).

- Idempotence: Performing union on a set with itself results in the set itself, \(A \cup A = A\).

The union operation can be extended to an arbitrary collection of sets [17]. For a set M of sets, x belongs to the union of M if and only if there exists an A in M such that x is in A. This generalizes the union of specific sets, allowing for the definition of unions involving an arbitrary number of sets [18].

The binary union operation between two sets A and B can be defined using the axiom of pairing to create a unique set C = {A, B}, followed by the definition \(A \cup B = \bigcup\{A, B\}\) [19]. This inductive definition extends to finite unions, where \(\bigcup_{i=1}^n A_i = \bigcup_{i=1}^{n-1} A_i \cup A_n\) [20].

In the context of set theory's Boolean algebra structure, union operates in conjunction with intersection and complementation [21]. The relationship between union and intersection is governed by De Morgan's laws, expressed as \(A \cup B = (\neg A \cap \neg B)'\), where the superscript \('\' denotes complement in the universal set U [22]. This relationship demonstrates the foundational role of union in defining fundamental properties of set operations [23].


## Browser Support and Polyfills

The JavaScript `Set` data structure now includes built-in methods for union, intersection, and difference operations. These new features were added to the V8 engine and will be adopted by Node.js, making them available in Chrome and Firefox Nightly soon. Edge follows Chrome closely and Firefox Nightly supports these operations behind a flag, indicating future adoption.

The union operation combines elements from two sets into a single collection, while intersection finds common elements between them. The difference method identifies elements present in the first set but not the second. These operations are part of the ES2015 specification and are now implemented in all three major browser engines.

Browser support for these operations is robust, with reliable performance characteristics. The size property returns elements in constant time (O(1)), while array membership checks vary by length (O(n)). The set can be iterated over using foreach or for...of loops, maintaining the order of insertion.

Polyfills are available for older JavaScript engines through core-js and es-shims projects. For instance, the union functionality is provided by the set.prototype.union package. The addition of these methods completes the implementation of the JavaScript Set, making it less reliant on external dependencies or custom implementations.


## Advanced Set Operations

The Set data structure now includes methods for difference and symmetric difference operations, completing the suite of basic set operations [24]. 


### Difference Operation

The difference operation creates a new set containing elements present in the first set but not in the second [25]. This operation is particularly useful for filtering elements between sets [26]. For example:

```javascript

const set1 = new Set(['apple', 'banana', 'cherry']);

const set2 = new Set(['banana', 'kiwi']);

const diffSet = set1.difference(set2);

console.log(diffSet); // Set {"apple", "cherry"}

```

The difference operation can also be implemented manually using the filter method [27]. The following code demonstrates how to create a difference set between two arrays, which can then be converted to a Set:

```javascript

function difference(setA, setB) {

  const arrayA = Array.from(setA);

  const arrayB = Array.from(setB);

  return new Set(arrayA.filter(x => !arrayB.includes(x)));

}

const setA = new Set([1, 2, 3, 4]);

const setB = new Set([3, 4, 5, 6]);

console.log(difference(setA, setB)); // Set { 1, 2 }

```


### Symmetric Difference Operation

The symmetric difference operation creates a new set containing elements present in either set but not in both [28]. This operation is useful for identifying elements that are unique to each set [29]. For example:

```javascript

const set1 = new Set(['apple', 'banana', 'cherry']);

const set2 = new Set(['banana', 'kiwi']);

const symDiffSet = set1.symmetricDifference(set2);

console.log(symDiffSet); // Set {"apple", "cherry", "kiwi"}

```

The symmetric difference can be implemented using the difference operation and union method [30]. The following code demonstrates how to create a symmetric difference set between two arrays, which can then be converted to a Set:

```javascript

function symmetricDifference(setA, setB) {

  const unionSet = new Set([...setA, ...setB]);

  const diffA = difference(setA, setB);

  const diffB = difference(setB, setA);

  return new Set([...diffA, ...diffB]);

}

const setA = new Set([1, 2, 3, 4]);

const setB = new Set([3, 4, 5, 6]);

console.log(symmetricDifference(setA, setB)); // Set { 1, 2, 5, 6 }

```

These additional operations complement the basic union and intersection operations, providing a comprehensive toolkit for set manipulation in JavaScript [31]. Together, they enable developers to perform complex set operations efficiently and effectively [32].

