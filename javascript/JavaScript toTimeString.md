---

title: JavaScript Date toTimeString Method

date: 2025-05-26

---


# JavaScript Date toTimeString Method

JavaScript's Date object includes several methods for working with dates and times, but sometimes you just need the time portion of a date. That's where the toTimeString() method comes in. It returns the time as a string, in your local time zone, perfect for displaying or processing just the time information. In this article, we'll explore how to use toTimeString(), what it returns, and how it handles different input scenarios.


## Introduction to toTimeString

The toTimeString() method returns the time portion of a Date object as a string, in the local time zone. It does not accept any parameters and is part of the ECMAScript1 specification, widely supported in modern browsers including Chrome, Firefox, Opera, and Safari since at least 2015.

The returned string follows the format "HH:mm:ss GMT±xxxx (TZ)", where:

- HH represents the hour (24-hour clock)

- mm represents the minute

- ss represents the second

- ±xxxx is the local time zone offset from GMT

- TZ is the timezone's name (e.g., PST, CET)

For example, creating a Date object representing June 28, 1993 at 2:39:07 PM India Standard Time, then calling toTimeString() produces "14:39:07 GMT+0530 (India Standard Time)".

The method correctly handles invalid dates, returning "Invalid Date" when provided with an invalid input. For instance, attempting to format "December 26, 2023 34:90:00" results in "Invalid Date".


## Syntax and Parameters

The toTimeString() method is an ECMAScript1 (JavaScript 1997) feature supported in all modern browsers including Chrome, Firefox, Opera, and Safari since at least 2015. It operates by taking a Date object created using the Date() constructor and returning the time portion of that date as a string in the local time zone.

The method returns a string in the format "HH:mm:ss GMT±xxxx (TZ)", where:

- HH represents the hour in a 24-hour clock format

- mm represents the minute

- ss represents the second

- ±xxxx indicates the local time zone offset from GMT

- (TZ) displays the timezone's name

The returned string always represents the time portion of the date in human-readable form, with no date information included. For example, creating a Date object for June 28, 1993 at 2:39:07 PM India Standard Time and calling toTimeString() produces "14:39:07 GMT+0530 (India Standard Time)".

When working with the Date object, developers can call toTimeString() to extract just the time information while keeping the full date object intact. This method is particularly useful for displaying or processing time values independently of their associated dates.


## Return Value

The method returns a string representing the time portion of the given date object in the local time zone. The returned string follows the format HH:mm:ss GMT±xxxx (TZ), where HH represents the hour, mm represents the minute, ss represents the second, and ±xxxx represents the local time zone offset from GMT. The (TZ) component displays the timezone's name, such as "PDT" or "CET".

The method correctly handles invalid dates, returning "Invalid Date" when provided with an invalid input. For example, attempting to format "December 26, 2023 34:90:00" results in "Invalid Date". The hour is limited to 24, the minute to 59, and the second to 59. Milliseconds are not included in the returned string.

The implementation of the method is consistent across major browsers, though minor variations exist in formatting and timezone name representation. Some browsers may display the timezone name in the local language (e.g., "(CET)" in German instead of "(Central European Time)"). The offset is always represented in the format ±HHMM, where HH represents hours and MM represents minutes from UTC. For example, Indian Standard Time is displayed as +0530.


## Return Value Format

The returned string appears consistent across major browsers, following the format "HH:mm:ss GMT±xxxx (TZ)". Each component of this format serves a specific purpose:

- HH represents the hour in a 24-hour clock format and always includes leading zeros (e.g., 01, 02, 13). The maximum value is 23.

- mm represents the minute and follows the same leading zero rule (e.g., 01, 02, 59). The maximum value is 59.

- ss represents the second and also uses leading zeros (e.g., 01, 02, 59). The maximum value is 59.

- ±xxxx indicates the local time zone offset from GMT, where "±" represents whether the offset is ahead (+) or behind (-) GMT. "xxxx" consists of two digits for hours and two digits for minutes. For example, New York's Eastern Standard Time is represented as -0500, while India Standard Time is +0530.

- (TZ) displays the time zone's name, such as PDT, PST, CET, or IST.

Major variations in output typically arise from differences in time zone display preferences. Some browsers, particularly those with localized environments, may render (TZ) in the local language. For instance, "(Central European Time)" might appear as "(Mitteleuropäische Zeit)" in German-language browsers.

While the specification doesn't formally define the output format, all major implementations agree on this standard, ensuring compatible cross-browser functionality. However, developers should be aware that minor discrepancies in time zone display might affect internationalized applications.


## Examples

The method consistently returns the time portion of a Date object in the local time zone. For example, creating a Date object representing October 15, 1996 at 5:35:32 AM and calling toTimeString() produces "05:35:32 GMT+0530 (India Standard Time)".

When called on a Date object with only a date but no time (e.g., October 15, 1996), the method returns "00:00:00 GMT+0530 (India Standard Time)". If no date object is provided, it defaults to the current time in the local timezone: `let dateobj = new Date(); let B = dateobj.toTimeString(); console.log(B); // Output: 14:58:08 GMT+0530 (India Standard Time)`.

The output format always includes the hour (HH), minute (mm), and second (ss) in a 24-hour clock format, with leading zeros where necessary. The time zone offset (±xxxx) indicates the local time zone's difference from GMT, and the (TZ) component displays the timezone's name. For instance, "05:35:32 GMT+0530 (India Standard Time)" shows the time in India Standard Time, while "22:45:10 GMT-0800 (Pacific Standard Time)" demonstrates the format for Pacific Standard Time in the United States.

