---

title: JavaScript DateTimeFormat resolvedOptions Method

date: 2025-05-26

---


# JavaScript DateTimeFormat resolvedOptions Method

JavaScript's Intl.DateTimeFormat provides powerful tools for date and time localization, but understanding how these tools work under the hood can make your applications more robust and reliable. This article explores the resolvedOptions method, which reveals the actual formatting options used by a DateTimeFormat instance. You'll learn how to interpret the properties returned by resolvedOptions, from the selected locale and calendar system to the time zone and specific date/time components used for display. Along the way, we'll show you how to use resolvedOptions effectively, with practical examples that help you master this essential feature of JavaScript's internationalization API.


## Method Overview

The Intl.DateTimeFormat prototype's resolvedOptions method returns an object reflecting the computed date and time formatting options during the DateTimeFormat object's initialization. This method provides insight into the effective locale and formatting options that will be used when calling the DateTimeFormat instance's format methods. The returned object contains several key properties:

The `locale` property specifies the BCP 47 language tag for the actual locale used, including Unicode extension values that were requested and are supported for this locale. Supported extensions include "ca" for calendar, "hc" for hour cycle, and "nu" for numbering system.

The properties `calendar`, `numberingSystem`, and `timeZone` retrieve their values from the options argument passed to the DateTimeFormat constructor, with default values filled in as needed. The `timeZone` property will always provide an IANA time zone name, defaulting to the runtime's default time zone if no specific time zone is provided.

Additional properties include `hour12`, `weekday`, `era`, `year`, `month`, `day`, `hour`, `minute`, `second`, and `timeZoneName`. These properties represent the specific format elements determined through format matching between the provided options and the available combinations and representations for date-time formatting in the selected locale. Their presence in the returned object indicates whether these components will be represented in formatted output.


## Browser Support

The resolvedOptions method is implemented across both desktop and mobile environments, with the following support details:

**Desktop Browsers**

Chrome supports the method since version 24, with enhanced functionality for timeZone computation in version 35. Firefox begins support in version 29, matching Chrome's initial release date. Other supported desktop browsers include Opera 15 and modern versions of Safari. Early versions of these browsers lack timeZone computation capabilities.

**Mobile Browsers**

Chrome for Android supports the method from version 26, matching its desktop counterpart's initial release. Firefox for Android begins support in version 56, while Safari iOS launched with support in version 10. However, older mobile browser versions lack support for timeZone computation.

Server environments do not have specific browser compatibility details provided, indicating that the method's implementation focuses primarily on client-side JavaScript environments.

The method's widespread availability across modern browsers and devices demonstrates its importance in date and time formatting, providing developers with detailed information about the locale and formatting options being used.


## ResolvedOptions Properties

The properties returned by the `resolvedOptions` method provide comprehensive details about the date and time formatting options in use. These properties can be categorized into several groups:


### Locale and Calendar

The `locale` property specifies the actual locale used, including any Unicode extension values that were requested and supported for this locale. This property reflects the BCP 47 language tag for the selected locale.

The `calendar` property indicates the calendar system in use, with supported calendar types for the selected locale. This property helps determine the structure and symbols used in date representations.


### Numbering System and Time Zone

The `numberingSystem` property shows the number formatting system applied, based on the locale's supported numbering systems. This property ensures consistent representation of numeric values across different cultural contexts.

The `timeZone` property returns the IANA time zone name as provided in the options argument, with a fallback to the runtime's default time zone if no specific time zone is specified. This property is crucial for accurate time display and conversion.


### Date and Time Components

The properties `hour12`, `weekday`, `era`, `year`, `month`, `day`, `hour`, `minute`, `second`, and `timeZoneName` represent specific format elements determined through the matching process between the provided options and available locale representations. Their presence in the returned object indicates whether these components will be represented in formatted output.

Each of these properties provides developers with detailed insights into the locale and formatting options being applied, allowing for precise control and customization of date and time displays.


## Example Usage

To demonstrate the use of the resolvedOptions method, consider the following examples:

```javascript

const geeks = new Intl.DateTimeFormat('zh-CN', { timeZone: 'UTC' });

const result = geeks.resolvedOptions();

console.log(result.locale); // Output: "zh-CN"

console.log(result.calendar); // Output: "gregory"

console.log(result.timeZone); // Output: "UTC"

const geeks1 = new Intl.DateTimeFormat('LT');

const result1 = geeks1.resolvedOptions();

console.log(result1.locale); // Output: "lt"

console.log(result1.calendar); // Output: "gregory"

```

In the first example, we create a DateTimeFormat object for simplified Chinese ('zh-CN') with the time zone set to UTC. The resolvedOptions method returns an object containing the locale ("zh-CN"), calendar system ("gregory"), and time zone ("UTC").

The second example demonstrates creating a DateTimeFormat object for Lithuanian ('LT'). The resolvedOptions method returns the locale ("lt") and calendar system ("gregory"). Note that the resolvedOptions method does not provide detailed information about the numbering system, time zone, or specific date and time components in this simplified example.

By examining the resolvedOptions, developers can verify the effective locale and formatting options being used by their DateTimeFormat objects. This is particularly useful for ensuring that date and time displays are consistent with the intended locale settings.

