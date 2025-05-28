---

title: JavaScript RelativeTimeFormat: format Method Breakdown

date: 2025-05-27

---


# JavaScript RelativeTimeFormat: format Method Breakdown

JavaScript's Intl.RelativeTimeFormat API provides developers with a powerful tool for handling relative time formatting in a locale-aware manner. Using this built-in solution, developers can format time differences across multiple units including year, quarter, month, week, day, hour, minute, and second. This article explores the API's capabilities, including its core format method and customizable options for numeric representation and style preferences.


## RelativeTimeFormat Overview

The Intl.RelativeTimeFormat API provides JavaScript developers with a powerful tool for handling relative time formatting in a locale-aware manner. This built-in solution supports multiple time units including year, quarter, month, week, day, hour, minute, and second. The format function works across different locales, automatically selecting the appropriate unit based on the time delta.

The API works by taking the locale as its first parameter, followed by a difference (positive or negative) and a unit of time (year, quarter, month, week, day, hour, minute, or second). For example, the following code creates a relative time formatter in English and formats 2 days as "in 2 days" and -1 day as "1 day ago":

```javascript

const rtf1 = new Intl.RelativeTimeFormat('en');

let diffInDays = rtf1.format(2, 'days');

```

The format function requires two arguments: the amount of time (as a number or Date object) and the unit of time. It returns a string representing the relative time, such as "tomorrow", "2 years ago", or "in 10 minutes". The implementation automatically selects the most appropriate unit based on the time delta, returning "yesterday" for 1 day ago and "next year" for 1 year from now rather than "in 370 days" or "in 52 weeks".

The API supports customization through several options:

- Style: Can be 'long', 'short', or 'narrow'; 'long' is the default

- Numeric: Can be 'always' or 'auto'; 'auto' produces phrases like "next month" or "yesterday"

- LocaleMatcher: Allows for more control over locale selection

- NumberingSystem: Provides options for different number representation methods


## format Method Basics

This method serves as the core functionality of the Intl.RelativeTimeFormat API, providing developers with a standardized way to format time values based on relative units and locale preferences. The API requires two primary inputs: a numeric value representing the time delta and a string indicating the time unit (year, quarter, month, week, day, hour, minute, or second).

The format function operates with both positive and negative values, returning localized strings that reflect the specified time difference. With default settings (localeMatcher: "best fit", numeric: "always", style: "long"), the API produces output such as "1 day ago" for -1 day and "in 1 day" for 1 day. When the numeric option is set to "auto", the API employs more concise phrases like "yesterday" for -1 day and "tomorrow" for 1 day.

For unit support, the API includes "year", "quarter", "month", "week", "day", "hour", "minute", and "second", allowing developers to create contextually appropriate time differences. The implementation requires the input to be a numeric value representing the date distance, as this approach simplifies implementation while addressing the core objective of providing internationalized date distance calculation tools.


## numeric and Style Options

The numeric option offers developers two choices: 'always' and 'auto'. When set to 'always', the API produces phrases like "1 day ago" or "in 1 day" (default behavior with no options specified). Setting numeric to 'auto' allows the API to employ more concise phrases such as "yesterday" for -1 day and "tomorrow" for 1 day, resulting in more idiomatic output.

The style option provides three customization levels: 'long', 'short', and 'narrow'. The default 'long' style produces full phrases like "in one month" or "1 day ago", while 'short' reduces this to "in 1 mo." or "1 day ago". The narrow style further condenses these to "in 1 mo." or "1 day ago", often matching short style representations.

The API's implementation demonstrates this functionality through various language examples. For instance, with the English locale, the value 2 days produces "in 2 days", while -1 day generates "1 day ago". When using the Spanish locale, the same values produce "dentro de 2 días" and "hace 1 día", respectively. Customization options further refine these outputs, as demonstrated by the 'auto' setting which produces "1 day ago" for -1 day and "in 0 days" for 0 days.

The API also includes support for the numberingSystem option, though this is particularly relevant when discussing number formatting rather than relative time. These options together provide developers with fine-grained control over how time differences are represented in user interfaces, allowing for both precise technical descriptions and more casual, conversational language depending on the application's requirements.


## Supported Units and Locale Data

The supported units include year, quarter, month, week, day, hour, minute, and second, aligning with the core functionality described in the documentation. These units enable precise time distance calculations while supporting both small and large time intervals.

Localized formatting operates through the BCP 47 language tags, allowing developers to create culturally appropriate time formats. The provided examples demonstrate this through both English and Spanish locales, with consistent unit support across languages. For instance, the text shows "1 day ago" for -1 day and "in 1 day" for 1 day in both languages.

The API's implementation demonstrates robust support for multiple language options, as evidenced by the examples provided for English and Spanish. The functionality remains consistent across different time units, allowing developers to choose the most appropriate granularity for their applications.

