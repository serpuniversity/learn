---

title: JavaScript Temporal: PlainTime and Microsecond Handling

date: 2025-05-27

---


# JavaScript Temporal: PlainTime and Microsecond Handling

JavaScript's Temporal API represents time through various specialized classes, including PlainTime, which handles time without date information. This introduction explores PlainTime's capabilities, focusing on its microsecond handling, comparison methods, and time manipulation features. The discussion highlights the API's experimental nature and its compatibility across modern browsers, providing developers with a comprehensive understanding of this precise time management tool.


## Introduction to Temporal and PlainTime

The Temporal API represents time through both wall-clock time classes and exact time classes (Instant, ZonedDateTime, nanoseconds since epoch). It introduces specialized classes for different temporal values, including PlainTime, which represents time without date information. The API creates PlainTime objects using the Temporal.PlainTime.from() method, which takes an object with an hour property.

 PlainTime objects include several methods: valueOf() (which throws an exception), compare(), and equals(). The PlainTime class does not support comparison with relational operators (<, <=, >, >=). The API also includes a polyfill available at https://github.com/tc39/proposal-temporal, which allows users to test PlainTime functionality in browser consoles.

The PlainTime class provides access to hour, second, minute, millisecond, microsecond, and nanosecond components through methods of the same name. The microsecond accessor returns an integer from 0 to 999 representing the microsecond value. The set accessor is undefined, so the microsecond value cannot be changed directly. Instead, use the .with() method to create a new PlainTime object with the desired value.

The PlainTime class supports comparison using the compare() method and formats time as "08:44:00.068123434" with the toString() method. The microsecond value can be adjusted using the .add() or .subtract() methods, as shown in the example below:

```

const time = Temporal.PlainTime.from("12:34:56");

const newTime = time.add({ microseconds: 100 });

console.log(newTime.toString()); // 12:34:56.0001

```

For date-time operations, JavaScript's current implementation works only with objects representing fixed dates and times, using a strictly specified string format for parsing. The microsecond functionality is experimental and does not work in some of the most widely-used browsers, with limited availability.


## Microsecond Property Accessors

The `microsecond` accessor property of `Temporal.PlainTime` instances returns an integer from 0 to 999 representing the microsecond (10^-6 second) component of the time. The set accessor of `microsecond` is undefined, meaning you cannot change this property directly. To modify the microsecond value, use the `.with()` method to create a new `Temporal.PlainTime` object with the desired value.

```javascript

const time2 = Temporal.PlainTime.from("12:34:56.123456789");

console.log(time2.microsecond); // 456

```

This feature allows precise time manipulation and comparison. For example, to add microseconds to a time value:

```javascript

const time = Temporal.PlainTime.from("12:34:56");

const newTime = time.add({ microseconds: 100 });

console.log(newTime.toString()); // 12:34:56.0001

```

The microsecond accessor enables accurate time calculations and conversions, though browser compatibility is limited. This functionality is part of the Experimental technology and is not Baseline because it does not work in some of the most widely-used browsers.


## Microsecond Method Interactions

The `add()` and `subtract()` methods on Temporal.PlainTime objects manipulate the microsecond value while maintaining proper time wrapping around 24 hours. For example, adding 100 microseconds to a time value yields:

```javascript

const time = Temporal.PlainTime.from("12:34:56");

const newTime = time.add({ microseconds: 100 });

console.log(newTime.toString()); // 12:34:56.0001

```

When subtracting a larger duration, the time wraps correctly:

```javascript

const laterTime = Temporal.PlainTime.from("14:00:00.123");

const earlierTime = laterTime.subtract({ hours: 1, microseconds: 123 });

console.log(earlierTime.toString()); // 13:00:00

```

The until() and since() methods also interact with microsecond values, calculating differences between times and rounding to specified units. These methods return Temporal.Duration objects representing the elapsed time, which may include nonzero fields up to the specified unit.

For example, calculating the difference between two times with the until() method:

```javascript

const time1 = Temporal.PlainTime.from("12:34:56.123");

const time2 = Temporal.PlainTime.from("12:35:00.456");

const duration = time1.until(time2, { largestUnit: 'second' });

console.log(duration.toString()); // P0DT0H0M0.333S

```

The implementation handles time zone transitions correctly, disambiguating skipped clock times during forward transitions and repeating clock times during backward transitions. Rounding modes determine how the remainder is handled when truncating to a specified unit. The available rounding modes include 'trunc' (default, truncates towards zero) and 'halfExpand'.


## Microsecond Feature Context

As of the current specification status, the microsecond functionality in Temporal.PlainTime is part of the experimental technology category. It is specifically noted as not being Baseline, meaning it does not work in some of the most widely-used browsers at present.

The Temporal library offers promising improvements over JavaScript's native Date object capabilities. While it primarily focuses on standardizing date/time handling through a strongly-typed objects approach, the microsecond resolution demonstrates its commitment to precise time manipulation.

Browser compatibility for this feature is limited, with the polyfill available at https://github.com/tc39/proposal-temporal providing a means to test PlainTime functionality in browser consoles. However, developers should exercise caution as the feature is still under development and not fully implemented across major browsers.

The microsecond accessor works consistently with the .with(), .add(), and .subtract() methods, allowing for accurate time calculations and conversions. Browser implementations handle time zone transitions correctly, with proper disambiguation for skipped and repeating clock times during transitions. Rounding modes provide the flexibility needed for precise time arithmetic operations.

