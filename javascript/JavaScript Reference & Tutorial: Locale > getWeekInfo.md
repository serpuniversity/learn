---

title: JavaScript: Locale and Week Information

date: 2025-05-26

---


# JavaScript: Locale and Week Information

The way we structure and interpret time varies significantly between cultures - what we consider the start of the week, which days are weekends, and even how we count the days in the first week of a year all differ based on where you're from. These differences can make a big impact on everything from scheduling meetings to calculating important dates. In this article, we'll dive into how JavaScript handles these locale-specific time rules, with a particular focus on the `getWeekInfo` method that helps us understand the week structure for any given language and region. Whether you're building a calendar app or just want to know why your weekend seems to start on a different day than what your computer thinks, this guide will give you the technical details you need.


## getWeekInfo Method

The `getWeekInfo()` method returns a `weekInfo` object containing three properties: `firstDay`, `weekend`, and `minimalDays`. This locale-specific information is used to determine the week structure for the given locale (MDN Web Docs).

The `firstDay` property is an integer between 1 (Monday) and 7 (Sunday), indicating the first day of the week for the locale. The `weekend` property is an array of integers between 1 and 7, where 1 represents Monday and 7 represents Sunday, indicating the weekend days for the locale. These weekend days are usually continuous because UTS 35 stores `weekendStart` and `weekendEnd` (IMGP).

The `minimalDays` property is an integer between 1 and 7 indicating the minimal days required in the first week of a month or year for calendar calculations (MDN Web Docs).

The method's specific implementations vary across locales. For example, Hebrew (he) has a `firstDay` of 7 (Sunday), a weekend consisting of [5, 6] (Thursday and Friday), and requires only 1 minimal day (IMGP). In contrast, English (en-GB) has a `firstDay` of 1 (Monday), a weekend of [6, 7] (Saturday and Sunday), and requires 4 minimal days (IMGP).

Browser compatibility varies but generally includes modern browsers like Chrome, Edge, Firefox, Safari, and mobile versions of these browsers, as well as Deno and Node.js environments (IMGP). Implementation details reveal that while every browser implements this functionality, it's marked as non-standard in browser compatibility data, with specific implementation quirks noted in the TC39 repository (IMGP).


## Locale Information and Browser Support

The Intl.Locale object provides week information through the getWeekInfo method, with different implementations across browsers. While every browser implements this functionality, it's marked as non-standard in browser compatibility data, with specific implementation quirks noted in the TC39 repository.

The getWeekInfo method returns a weekInfo object containing three properties: firstDay, weekend, and minimalDays. The firstDay property is an integer between 1 (Monday) and 7 (Sunday), indicating the first day of the week for the locale. The weekend property is an array of integers between 1 and 7, where 1 represents Monday and 7 represents Sunday, indicating the weekend days for the locale. These weekend days are usually continuous because UTS 35 stores weekendStart and weekendEnd.

The minimalDays property is an integer between 1 and 7 indicating the minimal days required in the first week of a month or year for calendar calculations. This information varies significantly by locale. For example, Hebrew (he) has a firstDay of 7 (Sunday), a weekend consisting of [5, 6] (Thursday and Friday), and requires only 1 minimal day. In contrast, English (en-GB) has a firstDay of 1 (Monday), a weekend of [6, 7] (Saturday and Sunday), and requires 4 minimal days.

While the method is supported across major browsers including Chrome, Edge, Firefox, Safari, and mobile versions of these browsers as well as Deno and Node.js, implementation details reveal that this behavior is marked as non-standard in browser compatibility data. The API returns an object with three properties: firstDay, weekend, and minimalDays, matching the specification found in [Intl Locale Info Proposal # sec-Intl.Locale.prototype.getWeekInfo](https://tc39.es/proposal-intl-locale-info/#sec-Intl.Locale.prototype.getWeekInfo).

The implementation works as follows: extracting the locale from the provided Intl.Locale object, creating a record with specific fields based on the locale, determining the first day of the week using StringToWeekdayValue (which maps weekday names to their corresponding integral values), and setting the first day field if a valid first day is found before returning the constructed record. This process ensures that the week information returned matches the specific rules for each locale as defined in the UTS 35 specification.


## Week Information Properties

The weekInfo object returned by getWeekInfo includes three key properties: firstDay, weekend, and minimalDays. For purposes of calendar calculations, the week structure differs between locales, with some exceptions:

- firstDay: This integer property indicates the first day of the week, where 1 represents Monday and 7 represents Sunday. The value depends on the locale, with some examples including:

  - Hebrew (Israel): 7 (Sunday)

  - Afrikaans (South Africa): 7 (Sunday)

  - English (United Kingdom): 1 (Monday)

  - Arabic (Afghanistan): 6 (Saturday)

- weekend: The weekend property is an array of integers between 1 and 7, representing the weekend days where 1 is Monday and 7 is Sunday. Similar to firstDay, the values vary by locale, including:

  - Hebrew: [5, 6] (Thursday and Friday)

  - Afrikaans: [6, 7] (Saturday and Sunday)

  - English (UK): [6, 7] (Saturday and Sunday)

- minimalDays: An integer between 1 and 7 indicating the minimal number of days required in the first week of a month or year for week calculations. While the default is 4 for ISO 8601-compliant locales, other variations exist:

  - Hebrew: 1

  - Afrikaans: 1

  - English (UK): 4

  - Divehi (Maldives): 1

These week-related properties are essential for accurate date and time calculations across different locales and provide the foundation for more complex calendar operations.


## Locale-Specific Week Data

The getWeekInfo method returns distinct week data for various locales, including Hebrew, Afrikaans, English (UK), and many others. For Hebrew (Hebrew Israel), the value is { firstDay: 7, weekend: [5, 6], minimalDays: 1 }, indicating a Sunday start and Shabbat (Sabbath) spanning Thursday evening to Saturday night. 

The Afrikaans locale follows similar rules to Hebrew with { firstDay: 7, weekend: [6, 7], minimalDays: 1 }, also starting on Sunday and observing Saturday and Sunday as weekend days. The English (UK) locale, however, aligns with ISO standards: { firstDay: 1, weekend: [6, 7], minimalDays: 4 }, indicating Monday as the start of the week and Saturday and Sunday as weekend days, requiring four minimal days in the first week of any year or month.

Additional examples include Malay (Malaysian Borneo), with a week structure of { firstDay: 7, weekend: [5, 7], minimalDays: 1 }, where Friday and Sunday mark the weekend days. This illustrates the diverse week configurations across different locales, providing accurate data for calendar calculations in each specific region.


## API and Proposal Status

The proposal for `getWeekInfo` is marked as non-standard across all browsers, with implementation details noted in the TC39 repository. The behavior appears consistent across engines, though all browsers throw an error when directly calling `msBN.getWeekInfo()`; instead, developers should use `msBN.weekInfo;` to access the week information object.

The method's implementation is based on the ECMAScript specification, specifically the Intl Locale Info Proposal under section `sec-Intl.Locale.prototype.getWeekInfo`. Each browser processes the request by extracting the locale from the Intl.Locale object, creating a record based on the locale's specific rules, determining the first day of the week through StringToWeekdayValue mapping, and returning the constructed record.

While the week information API follows the specified pattern across browsers, the implementation details vary. For instance, Deno returns { firstDay: 1, weekend: [6, 7], minimalDays: 1 } for Malay (Malaysian Borneo), whereas other browsers might return a similar structure with variations in weekend array and minimalDays property values. This divergence highlights the need for developers to account for potential implementation differences when using these APIs across environments.

