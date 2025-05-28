---

title: Temporal.PlainYearMonth: A Deep Dive into JavaScript's New Year-Month API

date: 2025-05-27

---


# Temporal.PlainYearMonth: A Deep Dive into JavaScript's New Year-Month API

JavaScript's Temporal library revolutionizes how developers work with dates and times through its high-precision Temporal objects. While the Temporal.PlainYearMonth class might seem abstract at first glance, it's a crucial building block for applications requiring calendar-specific date calculations and comparisons. From financial software that needs accurate year-month tracking to historical research tools that span multiple calendar systems, understanding PlainYearMonth opens up new possibilities for robust date manipulation in JavaScript.


## Overview of Temporal.PlainYearMonth

The PlainYearMonth object represents a calendar-specific year-month, enabling precise manipulation and comparison across different calendar systems. While the year and month fields are straightforward - year as an integer and month as a positive integer - the object's capabilities extend through its calendar-specific properties and methods.

Month representation uses the monthCode, a calendar-specific string that typically starts with "M" followed by a two-digit month number (or "M00L" for leap months). The number of months in a year varies by calendar system, from the standard 12 months in ISO 8601 to different values in lunar calendars. The first month of the year is represented as "M00L" rather than "M01", distinguishing it from subsequent months.

The class includes comprehensive comparison methods. The compare() method returns -1, 0, or 1 based on month comparison, while equals() specifically checks for both identical underlying ISO date values and calendar systems. Since the year-month is calendar-dependent, two month representations from different calendar systems might be equal according to compare() but not equals().

Working with plain year-months requires careful handling of calendar parameters. The constructor accepts year, month, and optional calendar and referenceDay parameters. Improper usage of calendar and referenceDay should be avoided unless using the canonical day selected by Temporal.PlainYearMonth.from() for the same year-month. For example, creating a PlainYearMonth for Chinese calendar dates requires specifying the correct referenceDay, as demonstrated in the constructor documentation.


## Creating Temporal.PlainYearMonth Objects

The `Temporal.PlainYearMonth` constructor requires the year and month as parameters, with additional options for calendar and reference day. Here are several valid examples demonstrating its usage:

```javascript

const ym = new Temporal.PlainYearMonth(2021, 7);

console.log(ym.toString()); // 2021-07

const ym2 = new Temporal.PlainYearMonth(2021, 7, "chinese");

console.log(ym2.toString()); // 2021-07-01[u-ca=chinese]

const ym3 = new Temporal.PlainYearMonth(2021, 7, "chinese", 31);

console.log(ym3.toString()); // 2021-07-31[u-ca=chinese]

const ym4 = new Temporal.PlainYearMonth(2021, 7, "chinese", 1);

console.log(ym4.toString()); // 2021-07-01[u-ca=chinese]

```

Note that the calendar parameter specifies the calendar system, with "iso8601" being the default. The referenceDay parameter is required when using non-ISO calendars and must be the ISO-calendar day corresponding to the first day of the desired calendar year and month. The constructor throws RangeError if the year, month, or referenceDay values do not represent a valid date in the specified calendar.

The Temporal.PlainYearMonth.from() method accepts three parameters: year, month, and calendar. Here's an additional example using this method:

```javascript

const ym = Temporal.PlainYearMonth.from(2021, 7, "chinese");

console.log(ym.toString()); // 2021-06-10[u-ca=chinese]

```

Improper usage of calendar and referenceDay parameters should be avoided unless the referenceDay is the canonical day selected by Temporal.PlainYearMonth.from() for the same year-month. For instance, the following code demonstrates the constructor's behavior when given invalid parameters:

```javascript

// This will throw a TypeError

new Temporal.PlainYearMonth('2021', 7, 'chinese');

// This will throw a RangeError

new Temporal.PlainYearMonth(2021, 13);

```


## Working with Year-Month Data

The PlainYearMonth object provides essential functionality for manipulating calendar-specific year-month values through its comprehensive set of properties and methods. These include monthCode, monthsInYear, and year for basic access to month-specific information, as well as the ability to convert between different representations through methods like from() and with().


### Adding and Subtracting Durations

The add() and subtract() methods enable precise adjustment of year-month values by calendar-aware durations. These operations follow a defined algorithm that first processes years, then months, and finally any remaining smaller units converted to days. For example:

```javascript

const ym = new Temporal.PlainYearMonth(2021, 7);

const result = ym.add({ months: 6 }); // Adds six months to the original year-month

console.log(result.toString()); // 2022-01

```

The methods handle out-of-range values based on the specified overflow option, either clamping the result or throwing an error as appropriate. This ensures that operations remain within the representable range of ±273,972.6 years centered on the Unix epoch.


### Comparison and Sorting

The class includes robust comparison methods for ordering and equivalence testing. The compare() method returns -1, 0, or 1 based on month comparison, while the equals() method checks for both identical underlying ISO date values and calendar systems. These methods enable reliable sorting and equality testing across different calendar systems.

For instance, comparing two Chinese calendar dates requires proper calendar handling:

```javascript

const ym1 = new Temporal.PlainYearMonth(2021, 7, "chinese", 1);

const ym2 = new Temporal.PlainYearMonth(2021, 6, "chinese", 30);

console.log(ym1.compare(ym2)); // 1

console.log(ym1.equals(ym2)); // false

```

These features together provide a powerful toolkit for working with calendar-specific year-month data in JavaScript, enabling both basic access and complex manipulations while maintaining strict accuracy and calendar awareness.


## Calendar-Specific Properties

The PlainYearMonth object includes several key properties for working with calendar-specific year-month data:


### Calendar-Specific Properties

The calendarId property returns the calendar used to interpret the date (experimental), while the constructor property indicates the constructor function that created the instance.


#### Month and Year Information

The month property returns the 1-based month index, which differs from the 0-based indexing used in JavaScript's Date object (monthCode: "M01" corresponds to January, not "M00"). The monthCode property returns a calendar-specific string representing the month, typically "M" followed by a two-digit month number. For leap months, this code follows the previous month's code and ends in "L" (e.g., "M11L" for February in a leap year).

The calendar system determines the number of days in the month (daysInMonth: 28, 29, 30, or 31) and year (daysInYear: 365 or 366 in leap year). The monthsInYear property returns the positive integer representing the number of months in the year, which is 12 for ISO 8601 but may differ in other calendar systems.


### Era and Year Context

The era property returns the calendar-specific era string, with undefined in ISO 8601 calendar systems. The eraYear property provides the year index within the era, which decreases as time proceeds (e.g., BCE era in Gregorian calendar). The year property returns the integer representing the number of years relative to the start of a calendar-specific epoch year, with the first year usually being the latest era's first year (year 1) or ISO 8601 year 0001.


### Leap Year Determination

The inLeapYear property returns a boolean indicating whether the year-month is in a leap year, while the month property can return a month index greater than 12 for certain calendar systems that support leap months (e.g., "M00L" for the first month of the year in some calendars).

These properties together provide a deep understanding of calendar-specific year-month data, enabling precise manipulation and comparison across different calendar systems while maintaining strict accuracy.


## Advanced Features and Considerations

The `Temporal.PlainYearMonth` class's `with()` method enables creation of new instances with specified fields replaced, functioning as a setter for year-month fields while preserving immutability. To change the `calendarId` property, conversion to a `Temporal.PlainDate` object via `toPlainDate()`, modification, and re-conversion back to `Temporal.PlainYearMonth` is required.

The `with()` method accepts an `info` object specifying at least one of the properties recognized by `Temporal.PlainYearMonth.from()`: `era`, `eraYear`, `month`, `monthCode`, or `year`. Uniquely, only one of `month` or `monthCode` needs to be provided, with the system automatically adjusting the other based on the specified calendar. Similarly, one of `era` and either `eraYear` or `year` must be given. The method returns a new `Temporal.PlainYearMonth` object with updated fields and retains other properties from the original date.

The method processes two parameters:

1. `info`: An object containing at least one of the recognized properties.

2. `options`: An optional object specifying behavior when a date component is out of range, containing a single `overflow` property.

The `overflow` property defines how to handle out-of-range components:

- "constrain" (default): Clamps the out-of-range component to a valid value

- "reject": Throws a `RangeError` for out-of-range values

The method's operation follows these key behaviors:

- Throws a `TypeError` if `info` is not an object or `options` is not an object or `undefined`

- Throws a `RangeError` for inconsistent property values, non-numeric properties, or numerical values out of range with `overflow` set to "reject"

- Ensures the result remains within the representable range of ±273,972.6 years from the Unix epoch

For edge cases, the method requires careful handling of calendar parameters and reference days. The `Temporal.PlainYearMonth.from()` static method provides safer construction, automatically managing reference days to ensure valid month representations across different calendar systems.

