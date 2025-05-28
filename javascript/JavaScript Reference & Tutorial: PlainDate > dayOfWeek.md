---

title: JavaScript Date Handling: dayOfWeek and Related Methods

date: 2025-05-27

---


# JavaScript Date Handling: dayOfWeek and Related Methods

JavaScript's built-in Date object has long been a source of frustration for developers due to its numerous quirks and inconsistencies. From zero-based months to ambiguous weekday calculations, traditional date handling in JavaScript has fallen short of modern development needs. The Temporal API represents a significant step forward in date manipulation, offering immutable date objects and comprehensive calendar support. This article delves into the nuances of JavaScript's date handling, focusing on the dayOfWeek property and related methods within the Temporal API. We'll explore how to work with weekdays, calculate bridge public holidays, and generate week dates while maintaining calendar-aware calculations.


## dayOfWeek Property

The `dayOfWeek` property returns a 1-based day index in the week of a date, with 1 representing Monday and 7 representing Sunday in the ISO 8601 calendar system. This property is calendar-dependent and cannot be modified directly. All commonly supported calendars use 7-day weeks, with the first day of the week typically being Monday, even when locales may consider a different day as the first day of the week.

Developers can access the `dayOfWeek` property through `Temporal.PlainDate` or `Temporal.PlainDateTime` instances. For example, the date "2021-07-01" would return 4 for Thursday, while the same date in the Chinese calendar (`[u-ca=chinese]`) would also return 4.

To use this property effectively, developers need to be aware of its calendar-dependency and the fixed nature of the week structure. The `daysInWeek` property, which is always 7 for commonly supported calendars, provides the context needed to understand the week structure. For instance, while `dayOfWeek` returns values from 1 to 7, the ISO 8601 calendar system's week starts on Monday, aligning with the property's implementation.


### Date Manipulation and Calculation

The property cannot be directly modified, but developers can create new date objects with specific dayOfWeek values using the `add()` or `subtract()` methods. For example, to change a date's dayOfWeek, you need to calculate the difference between the current dayOfWeek and the desired value, then adjust the date accordingly. This is demonstrated in the `getDayInSameWeek`, `getNextDayInWeek`, and `getPreviousDayInWeek` functions provided in the documentation.


### Practical Applications

Developers can leverage `dayOfWeek` for advanced date calculations. For instance, the Temporal API includes functionality for calculating bridge public holidays in countries where holidays fall on specific weekdays. The API evaluates dayOfWeek to determine whether a holiday requires a bridge day, returning either the holiday date itself or an array of dates to be taken off work.

The API also demonstrates its capabilities through demonstrations like the `thisWeek` function, which generates an array of 7 dates representing the current week starting from Monday. This functionality showcases the API's comprehensive date component customization while maintaining calendar-aware calculations.


## Temporal API Overview

The Temporal API resolves fundamental issues with the JavaScript Date object through improved design principles and enhanced functionality. Key improvements include immutable date objects, correct month indexing, and comprehensive time zone handling. The API's design addresses common pitfalls of the current Date object while offering a more intuitive and predictable API.


### Immutable Dates and Correct Indexing

Temporal API objects are immutable, preventing accidental modifications that can lead to bugs. The API corrects the Date object's zero-based month indexing by using one-based numbering, matching natural language and calendar systems. This change eliminates ambiguity when working with date values and simplifies date arithmetic.


### Time Zone and Calendar Support

The API handles time zones explicitly through `ZonedDateTime` objects, which store time zone information along with date and time data. This approach prevents common issues with time zone transitions and daylight saving time changes. Temporal supports multiple calendar systems including Gregorian, Hebrew, and Islamic calendars, offering more flexibility than the current Date object.


### Enhanced Date Manipulation

The API introduces several improvements for date manipulation, including:

- `add()` and `until()` methods that make calculations more intuitive

- `round()` function for precise time field rounding

- `with()` method for creating new date objects with updated properties

These features demonstrate the API's commitment to providing clear, predictable, and powerful date handling capabilities. The API's comprehensive functionality is designed to replace the limitations of the current Date object while maintaining familiar JavaScript syntax and semantics.


## Week Calculation Methods

JavaScript provides several methods for working with weeks, including the built-in `getDay()` method, `toLocaleDateString()`, and the more flexible `toLocaleString()` with custom options. When creating a Date object with a date string, such as `new Date('2022-01-29')`, the browser calculates the weekday based on the local timezone. To get the correct weekday for the UTC timezone, developers should use `new Date('2022-01-29').toLocaleString('en', { weekday: 'long', timeZone: 'UTC' })`, which returns the appropriate string representation of the day.


### Date Formatting and Customization

The API offers extensive customization options through the `toLocaleString()` method, supporting both 12-hour (AM/PM) and 24-hour time formats. For example, developers can generate formatted week dates using individual component access, creating strings like "04/01/2021 at 14:30" with `${date.day}/${date.month}/${date.year} at ${date.hour}:${String(date.minute).padStart(2, '0')}`.


### Week Calculation Functions

The Temporal API includes several useful functions for calculating a week's dates:

- The `days()` function creates an array of 7 dates starting from Monday, using the formula `var first = current.getDate() - current.getDay() + 1` to correctly align the week start.

- The `thisWeek()` function calculates the current week's dates by finding the Monday of the current week and generating an array of 7 dates from that point.


### Calendar-Aware Calculations

The API handles timezone differences correctly, ensuring that date calculations account for local time zones. For instance, developers can use `Temporal.PlainDate` to get the day of the week accurately, with the property returning values from 1 (Monday) to 7 (Sunday) in the ISO 8601 calendar system. This property is calendar-dependent, maintaining consistent week structures across different calendar implementations.


## Date Manipulation Functions

Temporal API demonstrates its capabilities through several useful functions for manipulating dates, including changing the day of the week, calculating bridge public holidays, and generating arrays of week dates. For instance, a developer can create a new `Temporal.PlainDateTime` object with a desired `dayOfWeek` value using the `add()` or `subtract()` method.


### Date Manipulation Methods

Developers can leverage `add()`, `subtract()`, `round()`, and `with()` methods to manipulate dates effectively. These methods, available through the PlainDate and PlainDateTime classes, provide intuitive and predictable date arithmetic. For example, to set a date to the first day of the week, developers can use `with({ day: 1 })` and repeatedly apply `add({ days: 7 })` to generate the subsequent weeks.


### Function Examples

The API includes several useful functions that demonstrate its capabilities:


#### Bridge Public Holidays

The `bridgePublicHolidays` function calculates bridge public holidays in countries where holidays fall on specific weekdays. For example:

- Labour Day (5-01) in 2020 results in ['2020-05-01']

- Labour Day in 2018 requires ['2018-04-30', '2018-05-01']

- Labour Day in 2021 produces an empty array

The function handles different day-of-week cases:

- No bridge day needed for Monday (day 1)

- Monday bridge day needed for Wednesday (day 3)

- Friday bridge day needed for Friday (day 5)

- Both Monday and Tuesday are bridge days for Tuesday (day 2)

- Both Thursday and Friday are bridge days for Thursday (day 4)

- No bridge days needed for Saturday (day 6) or Sunday (day 7)


#### Week Calculation

Temporal's week calculation functions illustrate its strengths. The days() function creates an array of 7 dates starting from Monday using the formula `var first = current.getDate() - current.getDay() + 1`. The thisWeek() function calculates the current week's dates by finding the Monday of the current week and generating an array of 7 dates from that point.


### Calendar-Awareness

The API handles timezone differences correctly, ensuring that date calculations account for local time zones. For instance, developers can use `Temporal.PlainDate` to get the day of the week accurately, with the property returning values from 1 (Monday) to 7 (Sunday) in the ISO 8601 calendar system. This property maintains consistent week structures across different calendar implementations while providing calendar-aware calculations.


## Best Practices

When working with JavaScript dates, developers should create date objects using UTC strings to avoid timezone-related issues. The getUTCDay() method provides the correct weekday value for the UTC timezone, while toLocaleDateString() offers more flexible date formatting options.

Creating Date objects from date strings requires careful consideration of timezone implications. The browser's default behavior is to calculate the weekday based on the local timezone when creating a Date object with a date string. For example, `new Date('2022-01-29')` instantiates the date in the local timezone. However, date-only ISO 8601 strings like "2022-01-29" are parsed as UTC, and appending a timestamp ("2022-01-29T00:00:00") results in a local date object where getDay() returns the expected value. To get the weekday for the UTC timezone, developers should use `new Date().getUTCDay()`.

The built-in parser interprets ISO 8601 strings as UTC, but getting the weekday name in a specific timezone requires setting the time zone using `toLocaleString` with suitable options. For example, to get the weekday name in the UTC timezone, you can use `new Date().toLocaleString('en', { weekday: 'long', timeZone: 'UTC' })`. Alternatively, the toLocaleDateString method provides more direct and useful output for determining the day of the week.

Developers should avoid relying on the Date object's mutability, as modifications can lead to unexpected behavior when passing date objects between functions. For precise date arithmetic and calendar-aware calculations, the Temporal API's PlainDate methods provide reliable alternatives. The API's comprehensive properties include dayOfWeek (1-7), where Monday is represented as 1 and Sunday as 7, following the ISO 8601 standard.

