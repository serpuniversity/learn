---

title: Temporal API: PlainDateTime

date: 2025-05-27

---


# Temporal API: PlainDateTime

JavaScript's Date API has long been a source of frustration for developers due to its numerous design flaws and limitations. From ambiguous date representations to cumbersome time zone management, these issues have led many to rely on external libraries rather than trust the native implementation. The Temporal API addresses these problems with a more robust and intuitive approach to date and time management. This article explores the core features of the Temporal API, particularly focusing on the PlainDateTime object, which represents a specific point in time while maintaining immutability and supporting precise calculations. We'll examine how PlainDateTime builds upon the concepts of PlainDate and PlainTime to provide reliable date and time manipulation capabilities while addressing the deficiencies of the existing Date API.


## JavaScript's Date API Problems

The JavaScript Date API has several fundamental issues that the Temporal API aims to address. The existing implementation lacks essential methods that respect immutability, with months starting at 0 instead of 1, requiring calls like `new Date(2022, 0, 1)` to represent January 1st. This design choice leads to ambiguous date representations, particularly regarding the day of the month, which begins at 1 rather than 0.

Moreover, creating new date objects becomes cumbersome, as modifying an existing date instance directly affects its internal state. For example, attempting to set the date to February 29th in a non-leap year would fail silently, causing unintended side effects. The API's handling of time zones is equally problematic, often requiring external libraries and resulting in inconsistent parsing behavior across implementations.

The most significant drawbacks stem from immutability and time zone management. JavaScript's Date object mutates when performing operations like `setDate`, making it difficult to track changes or maintain multiple versions of the same date. Time zone handling requires additional libraries such as moment.js (now superseded by date-fns), adding complexity and potential compatibility issues for developers. These shortcomings have led to widespread adoption of alternative libraries, highlighting the need for a more robust native solution.


## Temporal API Overview

The Temporal API addresses JavaScript's fundamental date and time issues through a comprehensive set of immutable objects and methods [1]. All core components of the Temporal API (PlainDate, PlainTime, and PlainDateTime) provide precise, reliable time management capabilities [2].


### Core Components

The Temporal API introduces three primary components for managing dates and times:

- **PlainDate**: Represents a calendar date without time or time zone information [3].

- **PlainTime**: Represents a specific time of day without date or time zone information [4].

- **PlainDateTime**: Combines both date and time components into a single object [5].


### Implementation

The PlainDateTime object represents a specific point in time, allowing for precise calculations and manipulations [6]. It can be created in several ways:

- Using `Temporal.Now.plainDateTimeISO` to get the current date and time [7].

- Using a constructor with individual year, month, and day parameters [8].

- Parsing from a string in ISO 8601 format [9].


### Comparison and Conversion

Temporal provides robust methods for comparing and converting between date representations [10]. The `Temporal.PlainDate.compare()` function allows comparing two dates while ignoring calendar-specific differences [11]. Date and time can be converted between Plain and ZonedDateTime representations to handle time zone conversions [12].


### Calendar Support

The API supports multiple calendar systems through the `Temporal.Calendar` object, allowing easy switching between different cultural date formats [13]. This functionality is particularly useful for applications needing to accommodate various regional date conventions [14].


### Time Arithmetic

Temporal enables straightforward date and time calculations through methods like `add`, `subtract`, and `since` [15]. These operations return new objects instead of modifying existing ones, ensuring immutability [16]. The API also supports complex operations such as adding durations and calculating time differences between dates [17].


## PlainDateTime Basics

The PlainDateTime object combines the properties of a PlainDate and a PlainTime to represent a specific point in time without time zone information [1]. It is designed to handle date and time manipulation with precision and immutability [2].


### Construction and Initialization

A PlainDateTime can be created using several methods:

- Using the constructor with year, month, day, hour, minute, second, millisecond, microsecond, nanosecond, and calendar parameters [3]. All date parameters (year, month, day) are required.

- Parsing from a string in ISO 8601 format, which may include a calendar identifier [4].

- Retrieving the current date and time using Temporal.Now.plainDateTimeISO [5].


### Calendar Support

The PlainDateTime class supports multiple calendar systems through its calendar property [6]. The default calendar is ISO 8601, but developers can specify alternative calendars when creating or manipulating PlainDateTime objects [7].


### Time and Date Components

PlainDateTime objects contain several properties representing different aspects of the date and time:

- `year`, `month`, and `day` represent the calendar date [8].

- `hour`, `minute`, `second`, `millisecond`, `microsecond`, and `nanosecond` represent the clock time [9].

- `calendar` specifies the calendar system in use [10].

Additional properties provide information about the date structure:

- `dayOfWeek` indicates the day of the week [11].

- `daysInWeek` and `daysInMonth` provide the number of days in the current week and month, respectively [12].

- `daysInYear` indicates whether the year is a leap year [13].


### Methodology

Key methods for manipulation include:

- `with(fields)`: Creates a new PlainDateTime object with specified fields replaced by new values [14].

- `withCalendar(calendarSystem)`: Returns a new PlainDateTime object interpreted in a different calendar system [15].

- `withPlainTime(newTime)`: Returns a new PlainDateTime object with the time part entirely replaced [16].

These methods enable precise date and time calculations while maintaining the immutability that is a core feature of the Temporal API [17].


## PlainDateTime Methods

The PlainDateTime class offers several essential methods for date and time manipulation, including addition, subtraction, and conversion [1].


### Date and Time Manipulation

The `with()` method creates a new PlainDateTime object representing this date-time with specified fields replaced by new values [2]. For example:

```javascript

const original = Temporal.Now.plainDateTimeISO();

const modified = original.with({ hour: 14 });

console.log(modified); // New PlainDateTime with the hour set to 14

```

You can also replace the calendar system using the `withCalendar()` method, which returns a new PlainDateTime object representing this date-time interpreted in the new calendar system [3]. This is useful for applications needing to accommodate various regional date conventions:

```javascript

const current = Temporal.Now.plainDateTimeISO();

const hijriDate = current.withCalendar("islamic-civil");

console.log(hijriDate);

```

The `withPlainTime()` method creates a new PlainDateTime object with the time part entirely replaced by the new time [4]. This can be particularly useful when combining date and time components:

```javascript

const dateOnly = new Temporal.PlainDate(2023, 5, 15);

const specificTime = new Temporal.PlainTime(16, 30, 0);

const combinedDateTime = dateOnly.withPlainTime(specificTime);

console.log(combinedDateTime);

```


### Conversion and Comparison

The `until()` method returns a new Temporal.Duration object representing the duration between this date-time and another date-time [5]. This is particularly useful for calculating time differences between two points in time:

```javascript

const now = Temporal.Now.plainDateTimeISO();

const later = now.with({ day: 16 });

const duration = now.until(later);

console.log(duration); // Duration representing the difference between now and the next day

```

The `toString()` method formats a PlainDateTime object as a string in RFC 9557 format [6], with options to control output precision and format:

```javascript

const date = new Temporal.PlainDateTime(2023, 6, 1, 12, 30, 0, 0, "islamic-civil");

console.log(date.toString({ calendarName: "always", fractionalSecondDigits: 2 })); // Custom formatted string

```

Additional methods support conversion to other temporal representations:

- Returns a new Temporal.PlainDate object representing the date part of this date-time [7]

- Returns a new Temporal.PlainTime object representing the time part of this date-time [8]

- Returns a string representing this date-time in RFC 9557 format [9]

- Converts to a Temporal.ZonedDateTime instance representing the same date-time in a specified time zone [10]


## Calendar and Time Zone Handling

Temporal's PlainDateTime object serves as a crucial bridge between date and time representations, allowing developers to work with precise time values while maintaining strict immutability [1]. This section explores how PlainDateTime handles different calendar systems and time zones, providing a comprehensive overview of its capabilities.


### Calendar Systems

PlainDateTime operates primarily with the ISO 8601 calendar by default, but it offers extensive support for alternative systems through its `withCalendar()` method [2]. This method returns a new PlainDateTime object representing the same date in the specified calendar system [3]. For example, to convert a Gregorian date to the Islamic civil calendar, developers can use:

```javascript

const gregorianDate = Temporal.Now.plainDateTimeISO();

const hijriDate = gregorianDate.withCalendar("islamic-civil");

console.log(hijriDate);

```

This flexibility makes PlainDateTime particularly valuable for applications serving diverse cultural regions, as it allows seamless integration with local date conventions [4].


### Time Zone Handling

Unlike its ZonedDateTime counterpart, PlainDateTime explicitly excludes time zone information, focusing solely on date and time components [5]. This design choice enables developers to work with time-agnostic data, particularly useful in scenarios where time zone details are stored separately [6]. For instance, when storing local time in a non-UTC time zone, PlainDateTime provides an ideal representation:

```javascript

const localDateTime = new Temporal.PlainDateTime(2023, 10, 1, 12, 0, 0, 0, "America/New_York");

console.log(localDateTime);

```

This approach ensures that time zone-related operations are handled explicitly, preventing potential ambiguities in date-time calculations [7].


### Current Time Retrieval

The `Temporal.Now.plainDateTimeISO` function exemplifies how PlainDateTime interacts with the current time [8]. This function returns the current date and time in ISO 8601 format, providing a simple yet powerful way to obtain the current local time [9]. The returned object can then be manipulated using PlainDateTime's comprehensive set of methods [10].


### Practical Applications

Developers frequently encounter situations where time zone information is stored separately from date-time values [12]. PlainDateTime excels in these scenarios, allowing precise manipulation of date-time components while maintaining strict immutability [11]. This separation of concerns makes it particularly suitable for legacy system interactions, UI date/time pickers, and stock exchange data, where local time representation is crucial [13].

In summary, PlainDateTime's calendar and time zone handling capabilities represent a significant step forward in JavaScript's date-time management. By explicitly separating date-time components and supporting multiple calendar systems, it enables developers to work with precise time values while maintaining flexibility and immutability.

