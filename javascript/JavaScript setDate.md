---

title: JavaScript Date Methods: setDate

date: 2025-05-26

---


# JavaScript Date Methods: setDate

JavaScript's Date object provides powerful methods for manipulating dates, but understanding how these methods work can be crucial for accurate date calculations. One such method is setDate(), which allows developers to update the day of the month while keeping the month and year unchanged. This introduction will explore the capabilities and nuances of the setDate() method, including how it handles special cases, performs date math, and interacts with leap years. We'll examine its syntax, parameters, and return value, as well as provide practical examples of its usage in both standard and edge-case scenarios.


## setDate Method Overview

The setDate() method allows JavaScript developers to update the day part of a date object while keeping the month and year unchanged. This method takes a single integer parameter representing the day of the month, which must be between 1 and 31.

The method handles special cases for setting the date outside the normal range:

- 0 sets the date to the last day of the previous month

- -1 sets the date to the day before the last day of the previous month

- 32 sets the date to the first day of the next month (if the current month has 31 days)

- 41 sets the date to the tenth day of the next month (assuming a 31-day month)

The method automatically adjusts for leap years, ensuring that February 29th is correctly handled and adjusted to February 28th in non-leap years.

When called multiple times, the method updates the date in local time, relative to the previous setting. This can result in apparent day increments of 31, 32, or 33 days, rather than 1, 2, or 3. This behavior occurs because each subsequent setting is relative to the previous date set, rather than the original date. For example, setting the date to 32 will push the date to July 2nd, and setting it to 32 again will push it to August 1st.

The method returns the number of milliseconds between the updated date object and midnight of January 1, 1970, UTC. To obtain a Date object from this value, you must create a new Date object using the returned milliseconds.


## setDate Method Syntax and Parameters

The setDate() method syntax is dateObj.setDate(date_Value); where date_Value holds the value of the day which is used to set in the date object. This parameter must be an integer ranging from 1 to 31. The method returns the number of milliseconds between the date object and midnight of January 1, 1970.

The method requires a valid Date object created using the Date() constructor. It handles higher and lower values with date math:

- 0 sets the last day of the previous month

- -1 sets the day before the last day of the previous month

- 32 sets the first day of the next month (if 31 days)

- 41 sets the tenth day of the next month (if 31 days)

The method changes the Date object in place and returns no value. It automatically adjusts for leap years, ensuring February 29th is correctly handled and adjusted to February 28th in non-leap years. For example, setting February 29th in a non-leap year will result in February 28th.

When setting date values outside the normal range, the method handles month transitions correctly. For instance, setting 32 on a date in a 31-day month will move the date to the first day of the next month. Setting 41 will move the date to the tenth day of the next month. This behavior ensures that the date progresses logically through the month and year.

The method is widely available across modern browsers, including Google Chrome, Internet Explorer, Mozilla Firefox, Opera, and Safari. It has been supported in all modern browsers since July 2015.


## setDate Method Example Usage

Examples of using the setDate() method to update the day of a date object are as follows:

```javascript

let date = new Date('2022-02-15');

console.log(date); // February 15, 2022

date.setDate(20);

console.log(date); // February 20, 2022

```

```javascript

let date = new Date();

console.log(date); // Current date and time

date.setDate(date.getDate() + 7); // Adding 7 days to the current date

console.log(date); // Date after adding 7 days

```

Higher and lower values behave as follows:

```javascript

date = new Date('2023-02-28');

console.log(date); // February 28, 2023

date.setDate(1); // Goes to March 1, 2023

console.log(date); // March 1, 2023

date.setDate(32); // Goes to April 2, 2023

console.log(date); // April 2, 2023

date.setDate(-1); // Goes to February 27, 2023

console.log(date); // February 27, 2023

```

The method correctly handles dates outside the normal 1-31 range, automatically adjusting month transitions. For example, setting February 32 will move the date to March 1, and setting February -2 will move the date to January 31.

The method returns the number of milliseconds between the updated date object and midnight of January 1, 1970, UTC, allowing for precise date manipulation when needed.


## setDate Method Return Value

The setDate() method returns the number of milliseconds between the updated date object and midnight of January 1, 1970, UTC. To obtain a Date object from this value, you must create a new Date object using the returned milliseconds (reference: JavaScript Date Methods Documentation).

The return value represents the new time value of the Date object after the day has been updated, allowing developers to calculate the difference between the original and updated date (reference: Date.prototype.setDate() - JavaScript - MDN Web Docs - Mozilla).

For example, setting a date to February 20th, 2022 would return a value representing February 20th, 2022 at midnight, while setting it to the last day of February 2022 would return a value representing February 28th, 2022 at midnight (reference: JavaScript Date setDate() Method Documentation).


## setDate Method Considerations

When the date value falls outside the normal 1-31 range, the method handles month transitions correctly. For instance, setting February 32 will move the date to March 1, and setting February -2 will move the date to January 31. This behavior ensures that the date progresses logically through the month and year.

The method returns the number of milliseconds between the updated date object and midnight of January 1, 1970, UTC, allowing for precise date manipulation when needed. To obtain a Date object from this value, you must create a new Date object using the returned milliseconds.

The method's return value can be particularly useful when performing date calculations. For example, if you need to determine the number of days between two dates, you can use the return value of setDate() to establish a baseline date and then compare subsequent values.

The method's behavior with leap years is designed to maintain correct calendar alignment. When setting February 29th in a non-leap year, the method automatically adjusts to February 28th, ensuring accurate date calculations. This automatic adjustment helps maintain proper month transitions when working with dates spanning multiple years.

