---

title: JavaScript Date: getDate() Method

date: 2025-05-26

---


# JavaScript Date: getDate() Method

The JavaScript Date object provides comprehensive functionality for date and time manipulation, with methods designed for various operations including date extraction, formatting, and modification. This article focuses on the getDate() method, which returns the day of the month for a specified date according to local time. We'll explore the method's syntax, supported browsers, and compatibility, then examine its behavior with valid and invalid date inputs. The article also demonstrates basic usage, interacts with other Date methods, and showcases common usage scenarios for generating formatted date strings and manipulating date values. Understanding this method's functionality and limitations is crucial for developers working with JavaScript dates.


## Introduction to Date Object and getDate() Method

The JavaScript Date object serves as a standard for computing date and time, offering extensive capabilities for date manipulation and formatting. As documented in the language specification, the `getDate()` method returns the day of the month (1 to 31) for a specified date according to local time. This method is implemented in JavaScript 1.0 and is supported by all major browsers, including Internet Explorer 7 and the latest versions of Chrome, Firefox, Safari, and Opera.

A detailed examination of the supported browser compatibility reveals universal support across all modern browsers, with ECMAScript1 compatibility established since July 2015. The method syntax is straightforward: `DateObj.getDate()`, requiring no parameters. It returns the day of the month as an integer between 1 and 31, behaving predictably for valid dates while returning `NaN` for invalid inputs, as demonstrated in the official documentation examples.

The method's behavior aligns with JavaScript's handling of months, which are zero-based (January = 0, December = 11), and its interpretation of date strings. For instance, a date string representing the last day of April ("new Date(2019, 04, 00)") correctly returns the first day of May, showcasing the method's reliance on local timezone settings and its treatment of month numbers.


## Syntax and Usage


### Syntax Overview

The `getDate()` method is invoked using the following syntax:

```javascript

DateObj.getDate()

```

Where `DateObj` represents a valid JavaScript Date object. This method requires no parameters. When called on a Date object, it returns the day component of the date as an integer between 1 and 31, corresponding to the day of the month. For example, calling `getDate()` on a Date object representing March 15th would return the value 15.


### Basic Usage Examples

To demonstrate its usage, consider the following examples:

```javascript

// Create a Date object for a specific date

let specificDate = new Date('2023-03-15');

console.log(specificDate.getDate()); // Output: 15

// Create a Date object for the current date and time

let currentDate = new Date();

console.log(currentDate.getDate()); // Output: Current day of the month

```

These examples illustrate how `getDate()` can extract the day component from both specific and current Date objects.


### Method Interactions with Other Date Methods

The `getDate()` method interacts with other Date methods to facilitate various date manipulations. For instance, when used with `setDate()`, it can adjust the day component of a Date object. Here's how you might add 10 days to the current date:

```javascript

let currentDate = new Date();

currentDate.setDate(currentDate.getDate() + 10);

console.log(currentDate.getDate()); // Output: Current day of the month + 10

```

This sequence demonstrates how `getDate()` can be used in conjunction with other methods to modify and retrieve date values.


## Method Behavior and Return Values

The `getDate()` method returns an integer between 1 and 31, representing the day of the month according to the local time zone. For valid dates, it behaves as expected, returning the day component of the date (e.g., `new Date('2023-12-25').getDate()` returns 25). If the date string is invalid or out of bounds, it returns NaN. For instance, attempting to extract the date from an invalid string like `new Date('2019-04-33')` results in NaN (Not-a-Number), as demonstrated in the official documentation examples.

The method's behavior with date strings illustrates its reliance on the local time zone. As noted in the MDN Web Docs, strings parsed as UTC (like "2019-12-25T23:59:59") return the last day of the month, while strings parsed as local time can return different results depending on the host time zone offset. This is exemplified by the behavior difference between UTC and local time zones, where a host at UTC +0530 would see "2019-04-01" as April 1, while a host at UTC -0400 would interpret it as March 31.

Furthermore, the method interacts with other Date methods in predictable ways. For example, setting a Date object to the last day of the month with "00" as the day component results in the last day of the previous month, as shown in the official documentation examples using "new Date(2019, 04, 00)". This behavior is consistent across all major browser implementations, as confirmed by compatibility data from the JavaScript specification.


## Common Usage Scenarios

The `getDate()` method provides essential functionality for extracting date components in JavaScript development. Common usage scenarios include creating formatted date strings and manipulating date values directly within the date object.


### Formatted Date Strings

One practical application involves generating specific date formats using the `getDate()` method in conjunction with other date methods and string manipulation techniques. For example, to create a date string in "yy-MM-dd" format:

```javascript

const today = new Date();

const year = today.getFullYear().toString().substring(2); // Extract last two digits of year

const month = (today.getMonth() + 1).toString().padStart(2, '0'); // Month 0-based, padded to 2 digits

const day = today.getDate().toString().padStart(2, '0'); // Day padded to 2 digits

console.log(`${year}-${month}-${day}`); // Output: Current date in yy-MM-dd format

```

This sequence demonstrates how to extract and format various date components using a combination of `getDate()`, `getFullYear()`, and basic string manipulation.


### Date Value Manipulation

The method's capability for direct date value manipulation makes it valuable in scenarios requiring precise date adjustments. For example, to create a date string representing a holiday that occurs 30 days before the current date:

```javascript

const currentDate = new Date();

currentDate.setDate(currentDate.getDate() - 30);

const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');

const day = currentDate.getDate().toString().padStart(2, '0');

console.log(`Holiday: ${currentDate.getFullYear()}-${month}-${day}`); // Output: Holiday date in yyyy-MM-dd format

```

This example illustrates how `getDate()` can be used as part of a larger sequence to manipulate and format date values effectively.

The versatility of `getDate()` in these scenarios highlights its importance for both precise date manipulation and flexible date formatting in JavaScript development.

