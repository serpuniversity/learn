---

title: Set.prototype.delete()

date: 2025-05-26

---


# Set.prototype.delete()

The delete() method in JavaScript's Set object provides a straightforward way to remove elements from a collection, but its implementation and behavior can vary depending on the type of elements stored. While removing primitive values works as expected, deleting objects requires a deeper understanding of reference equality. This article explores the nuances of Set.prototype.delete(), explaining its behavior for different data types and providing practical examples to help developers use this method effectively.


## delete() Method Overview

The delete() method removes a specified value from the Set instance. It returns true if the deletion is successful and false otherwise. This method works by checking for the existence of the value in the set and removing it if found.

When using objects as values in the Set, deletion requires matching by reference rather than value equality. To remove a specific object, you must have a reference to that object rather than creating a new object with the same properties. The method iterates through the set using the forEach method to find and delete the object reference.

Additional details on implementation and usage:

- The method has been supported across browsers since July 2015 and is defined in the ECMAScript 2026 Language Specification (section 14.7.2.1).

- When working with objects, ensure you use the exact reference to the object rather than creating a new object with the same properties.

- While deleting elements during iteration is generally safe, it's important to note that this operation can affect the iteration process. Alternatively, you can use the filter method to create a new set with the desired elements.


## Syntax and Basic Usage

The delete() method removes a specified value from a Set instance. It accepts a single parameter (value) representing the value to remove and returns a boolean indicating whether the deletion was successful (true) or not (false).


### Basic Usage

The method follows this syntax:

```javascript

setInstance.delete(value)

```

For example:

```javascript

let mySet = new Set([1, 2, 3]);

console.log(mySet.delete(2)); // true

console.log(mySet); // Set(2) { 1, 3 }

```

If the value is not present in the set, the method returns false:

```javascript

console.log(mySet.delete(4)); // false

console.log(mySet); // Set(2) { 1, 3 }

```


### Handling Objects as Values

When using objects as values in the Set, deletion requires matching by reference rather than value equality. Attempting to delete an object using a new object with the same properties will fail:

```javascript

var s = new Set([1,2,3]);

var newItem = [4, 5];

s.add(newItem); // Set(5) {1, 2, 3, 4, [4, 5]}

s.delete(newItem); // true

```

To successfully delete an object, you must use the exact reference to the original object:

```javascript

var s = new Set([1,2,3]);

var obj = { id: 2 };

s.add(obj); // Set(4) {1, 2, 3, [object Object]}

s.delete(obj); // true

```

If you need to delete an object based on a specific property, you can use the forEach method to find and delete the correct reference:

```javascript

let mySet = new Set([ { id: 1 }, { id: 2 }, { id: 3 } ]);

for (const item of mySet) {

    if (item.id == 2) {

        mySet.delete(item); // Optional

        break;

    }

}

console.log([...mySet]);

```

Alternatively, you can use the filter method to create a new set with the desired elements:

```javascript

const result = mySet.filter(x => x.id !== 2);

```

This approach creates an immutable copy of the set without the specified element.


## Dealing with Objects as Values

When using objects as values in the Set, deletion requires matching by reference rather than value equality. This means that when you add an object to a Set, you're adding a reference to that object, not a copy of its properties.

Attempting to delete an object from the Set using a new object with the same properties will fail because the Set performs reference equality checks:

```javascript

var s = new Set([1,2,3]);

var newItem = [4, 5];

s.add(newItem); //Set(5) {1, 2, 3, 4, [4, 5]}

s.delete(newItem); //This works

```

For primitive types like numbers and strings, the equality checks work as expected:

```javascript

var s = new Set([1,2,3]);

s.add(4); //Set(4) {1, 2, 3, 4}

s.delete(4); //This works

```

To successfully delete an object from the Set, you must use the exact reference to the original object. This is important to keep in mind when working with complex objects that may be modified or removed elsewhere in your code.

If you need to remove an object based on a specific property, you can use the Set's forEach method to find and delete the correct reference:

```javascript

mySet.forEach(x => x.Name === 'Ann' ? mySet.delete(x) : x)

```

Alternatively, you can use the filter method to create a new set with the desired elements:

```javascript

function removeObjectFromSet(set, obj) {

  return new Set([...set].filter((el) => JSON.stringify(el) != JSON.stringify(obj)))

}

```

This approach creates an immutable copy of the set without the specified element, which can be useful when you're working with complex objects and want to maintain the original set structure.


### Notes on Implementation

The delete() method works by checking if the value exists in the set and then removing it if found. It's part of the ECMAScript 2026 Language Specification and has been supported across browsers since July 2015. The method returns true if the value was already in the set, otherwise false.


## Common Usage Examples

The delete() method works as follows:

```javascript

let fruits = new Set(['Apple', 'Banana', 'Orange']);

console.log(fruits.delete('Orange')); // true

console.log([...fruits]); // ["Apple", "Banana"]

```

If the element is not found, it returns false:

```javascript

console.log(fruits.delete('Grapes')); // false

console.log([...fruits]); // ["Apple", "Banana"]

```

The method works with primitive types like numbers and strings:

```javascript

var s = new Set([1,2,3]);

s.add(4);

console.log(s.delete(4)); // true

console.log([...s]); // [1, 2, 3]

```

However, for objects, deletion requires matching by reference rather than value equality. This means you need to use the exact reference to the object:

```javascript

var s = new Set([1,2,3]);

var obj = { id: 2 };

s.add(obj);

console.log(s.delete(obj)); // true

```

Attempting to delete an object using a new object with the same properties will fail:

```javascript

var s = new Set([1,2,3]);

var newItem = [4, 5];

s.add(newItem);

console.log(s.delete(newItem)); // false

```

To remove an object based on a specific property, you can use the Set's forEach method to find and delete the correct reference:

```javascript

let mySet = new Set([ { id: 1 }, { id: 2 }, { id: 3 } ]);

mySet.forEach(x => x.id === 2 ? mySet.delete(x) : x);

console.log([...mySet]); // [ { id: 1 }, { id: 3 } ]

```

Alternatively, you can use the filter method to create a new set with the desired elements:

```javascript

function removeObjectFromSet(set, obj) {

  return new Set([...set].filter((el) => JSON.stringify(el) != JSON.stringify(obj)))

}

let mySet = new Set([ { id: 1 }, { id: 2 }, { id: 3 } ]);

let updatedSet = removeObjectFromSet(mySet, { id: 2 });

console.log([...updatedSet]); // [ { id: 1 }, { id: 3 } ]

```

The delete() method returns true for all successful deletions, regardless of the element's original type. It has been supported across browsers since July 2015 and is part of the ECMAScript 2026 Language Specification, specifically defined in section 14.7.2.1.


## Method Implementation and Browser Support

Set.prototype.delete() is an instance method of the Set object, specifically defined in the ECMAScript 2026 Language Specification (section 14.7.2.1). The method removes a specified value from the set and returns true if successful, false otherwise. It works by checking if the value exists in the set and then removing it if found.

The method has been supported across browsers since July 2015, with wide compatibility across Chrome, Edge, Firefox, Opera, and Safari. Implementation follows similar principles to the delete operator for object properties, with key differences in usage and return values between Set.clear() and Set.delete() methods.

