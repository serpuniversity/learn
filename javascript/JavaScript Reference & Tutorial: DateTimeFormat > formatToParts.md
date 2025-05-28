---

title: JavaScript Reference & Tutorial: DateTimeFormat > formatToParts

date: 2025-05-26

---


# JavaScript Reference & Tutorial: DateTimeFormat > formatToParts

The `DateTimeFormat.prototype.formatToParts` method provides detailed control over date and time formatting by returning an array of objects representing each component of the formatted string. This method allows developers to access and manipulate individual date-time parts, offering greater customization compared to the standard format() method. The returned array enables flexible handling of various calendar systems, time zones, and localization requirements, making it a powerful tool for date-time formatting in modern web applications.


## DateTimeFormat.prototype.formatToParts

The `DateTimeFormat.prototype.formatToParts` method returns an array of objects representing each part of the formatted date and time string. Each object contains two properties: `type`, which indicates the type of date-time component (such as date, time, or year), and `value`, which contains the formatted string representation of that component.

The method processes the input date using the configured date and time components. If the configuration includes the year component, it may output a `relatedYear` token instead of a standard year value, particularly when working with calendar systems that do not have universal year numbering systems (such as the Hebrew calendar).

The formatToParts array provides flexibility in customizing date-time displays. For example, it allows separating traditional calendar date components (era, year, month, day) from time components (hour, minute, second) and handling time zone-related information (time zone name, time zone offset).

The method works across modern browsers, supporting both Date and Temporal objects for input while ensuring compatibility with various calendar systems and localization requirements.


## Syntax and Parameters

The `DateTimeFormat.prototype.formatToParts` method processes the input date using the configured date and time components. It returns an array of objects representing each part of the formatted string, with each object containing a `type` property and a `value` property.

The method accepts an optional `date` parameter, which can be a `Date` or `Temporal.PlainDateTime` object. If omitted, it defaults to formatting the current date (as returned by `Date.now()`), which could be slightly confusing in practice. For cases where a specific date is required, it's advisable to always explicitly pass a date object.

The method's implementation details vary between browsers and locales, with some implementing features specific to certain calendar systems. For example, when working with calendars that do not have universal year numbering systems (such as the Hebrew calendar), the method may output a `relatedYear` token instead of a standard year value.

The return value is an array of objects, each containing two properties: `type` and `value`. The `type` property indicates the type of date-time component, while the `value` property contains the formatted string representation of that component. The string concatenation of all `value` properties in the array will result in the same string as would be returned by the `format()` method.


## Date-Time Component Types

The `formatToParts()` method outputs an array of objects, each containing two properties: `type` and `value`. The `type` property indicates the type of date-time component, while the `value` property contains the formatted string representation of that component.

The types of date-time components returned can vary based on the configuration of the `DateTimeFormat` object and the available date-time components. Common component types include:

- Era: The era of the date, such as BC or AD

- Year: The year component, which may be represented as a string or a related year token for certain calendar systems

- Month: The full month name, abbreviated month name, or month number

- Day: The day of the month

- Day of Week: The day of the week, which may be represented by a numeric value or localized name

- Hour: The hour component, which can be represented in 12-hour or 24-hour format

- Minute: The minute component

- Second: The second component

- Time Zone: The time zone information, including time zone name or offset

- Other: Additional components specific to certain configurations or locales

For example, if a `DateTimeFormat` object is configured to output both the Gregorian year and a year name token, both will appear in the output when combined in a format that requires both components. The string concatenation of all `value` properties in the array will result in the same string as would be returned by the `format()` method.

The method handles various calendar systems and time zones, allowing for flexible date-time formatting across different locales. Common calendar systems include the Gregorian calendar, Hebrew calendar, and Chinese calendar, with appropriate component types returned based on the selected calendar system.


## Custom Formatting Examples

The formatToParts method provides detailed control over date and time formatting through its customizable output structure. Here's how you can use it for custom date formatting:


### Basic Usage

```javascript

const formatter = new Intl.DateTimeFormat('en-US', {

  dateStyle: 'full',

  timeStyle: 'full',

});

const [datePart, timePart] = formatter.formatToParts(new Date());

console.log(datePart.value); // Full date string

console.log(timePart.value); // Full time string

```


### Custom Day Formatting

```javascript

function formatDay(date) {

  const formatter = new Intl.DateTimeFormat('en-US', {

    weekday: 'long',

    day: '2-digit',

  });

  return formatter.formatToParts(date).map(part => part.value).join(' ');

}

console.log(formatDay(new Date())); // Monday 2nd March 2023

```


### Handling Special Day Cases

```javascript

function formatSpecialDay(date) {

  const formatter = new Intl.DateTimeFormat('en-US', {

    weekday: 'long',

    day: '2-digit',

  });

  return formatter.formatToParts(date).map(part => {

    if (part.type === 'day' && part.value.endsWith('1')) {

      return `${part.value}st`;

    } else if (part.value.endsWith('2')) {

      return `${part.value}nd`;

    } else {

      return part.value;

    }

  }).join(' ');

}

console.log(formatSpecialDay(new Date('2023-03-02'))); // Monday 2nd March 2023

```


### Time Zone Formatting

```javascript

function formatTimeZone(date) {

  const formatter = new Intl.DateTimeFormat('en-US', {

    hourCycle: 'h23',

    timeZoneName: 'shortOffset',

  });

  return formatter.formatToParts(date).map(part => part.value).join(' ');

}

console.log(formatTimeZone(new Date('2023-03-15T15:30:00Z'))); // 15:30 +00:00

```


### Number System Customization

```javascript

function formatNumberSystem(date) {

  const formatter = new Intl.DateTimeFormat('bs-Latn-BA', {

    numberingSystem: 'latn',

  });

  return formatter.formatToParts(date).map(part => part.value).join(' ');

}

console.log(formatNumberSystem(new Date())); // 15:30 +00:00

```

These examples demonstrate how to use formatToParts for creating flexible and customized date-time formats while maintaining browser compatibility and locale-specific behavior.


## Browser Compatibility

The Intl.DateTimeFormat() constructor creates DateTimeFormat objects with support widely available across many devices and browser versions, with implementations present since September 2017. It can be called with or without 'new', creating a new instance in both cases. When called without 'new' and 'this' is another DateTimeFormat instance, it returns the existing instance.

The constructor accepts two parameters: locales and options. The locales parameter should be a string with a BCP 47 language tag or an Intl.Locale instance, or an array of such identifiers. The runtime's default locale is used if undefined or none supported. Unicode extension keys nu (numberingSystem) and ca (calendar) can be set with options to override locales property. The options parameter is an object with three sections: locale options, date-time component options, and style shortcuts. Locale options include localeMatcher, which defaults to "best fit" but can also be "lookup". Date-time component options include dateStyle and timeStyle, which can be "full", "long", "medium", or "short". Style shortcuts include numeric, useGrouping, calendar, and timeZone.

When creating DateTimeFormat objects in Node.js, formatting differs from Chrome browsers. Node.js returns "2019-03-04" while Chrome returns "04.03.2019". To achieve consistent formatting across implementations, developers should use the formatToParts method with more general language codes.

The resolvedOptions method returns an object with properties reflecting the options computed during DateTimeFormat initialization. These properties include locale (BCP 47 language tag), calendar (supported calendar type), numberingSystem (supported numbering system), and timeZone (IANA time zone name). Optional properties include hourCycle.

The formatToParts method returns an array of objects representing the formatted date and time components. Each object contains a type property indicating the component type (such as month, day, or year) and a value property containing the formatted string representation of that component. The string concatenation of all value properties in the array will result in the same string as would be returned by the format method.

