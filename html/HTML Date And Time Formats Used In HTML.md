---

title: HTML Date and Time Formats

date: 2025-05-29

---


# HTML Date and Time Formats

HTML's `<time>` element and related date/time input types offer powerful tools for semantic markup and precise temporal data representation. This article explores these features in depth, from the technical specifications to real-world implementation challenges. We'll examine how the `<time>` element and `datetime` attribute transform date/time information into machine-readable formats, while the input types "date", "datetime-local", and "time" provide intuitive user interfaces for selecting specific times. Along the way, we'll uncover the complexities of browser implementation, locale-specific formatting, and the limitations developers face when customizing date/time display. Whether you're building a calendar application, implementing search functionality, or simply improving accessibility on your website, this guide will help you master HTML's date/time capabilities.


## The `<time>` Element

The `<time>` element in HTML provides a way to mark up specific times or date information, with the `datetime` attribute allowing the element's contents to be translated into a machine-readable format. This element forms part of the broader effort in HTML5 to provide enhanced semantic markup capabilities for date and time information.

According to the specification, the `datetime` attribute supports multiple formats, including:

- Date-only format (YYYY-MM-DD)

- Date and time with timezone (YYYY-MM-DDThh:mm:ssZ)

- Date and time without timezone (YYYY-MM-DDThh:mm:ss)

This allows for precise representation of temporal information while maintaining compatibility with both human readers and machine processors. The element supports a wide range of usage scenarios, from representing simple time values to complex date durations and time zones.

As of 2023, browser support stands at 62.0% for full support across all major browser versions, with partial support ranging from 18.0% to 49.0%. This demonstrates growing adoption of the feature, particularly for direct time representation and basic date values.

The `<time>` element enables better integration of temporal information into web content, particularly when combined with other semantic HTML features. Its support for machine-readable formats enhances functionality across various applications, from calendar integration to improved search engine optimization through smarter date parsing.


## datetime Attribute Formats

Based on the HTML5 specification, the datetime attribute supports multiple formats for date and time representation, including:

Date Components:

- Year (YYYY)

- Month (MM)

- Day (DD)

Time Components:

- Hour (hh)

- Minute (mm)

- Second (ss)

- Time Zone Designator (TZD) - "Z" denotes Zulu (Greenwich Mean Time)

The attribute follows these format syntaxes:

- Basic format: YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00)

- Extended format: YYYY-MM-DDThh:mm:ss.sTZD (e.g., 1997-07-16T19:20:30.45+01:00)

The datetime attribute can represent:

- Valid yearless date string: MM-DD (e.g., 11-12)

- Valid date string: YYYY-MM-DD (e.g., 1887-12-01)

- Valid time string: HH:MM, HH:MM:SS (e.g., 23:59, 12:15:47)

- Valid local date and time string: YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS (e.g., 2022-01-01 12:00, 2022-01-01 12:30:45)

- Valid time duration: PnD (P2D for two days), PTnHnM (PT15H10M for 15 hours and 10 minutes)

The attribute's browser support stands at 62.0% for full support across major browser versions, with 18.0% to 49.0% partial support across different implementation levels.


## Browser Support and Display

The implementation of date and time input in web browsers closely follows the user's system settings. On desktop devices, Chrome, Firefox, and Opera format inputs based on the browser language setting, while Edge mirrors the Windows language setting. Notably, Dutch users with their system language set to en-us receive the date format 01/30/2019 instead of the expected 30-01-2019.

Mobile devices exhibit similar behavior: Chrome on Android adheres to the device's display language, while other browsers may follow analogous logic. These implementations demonstrate that all web browsers currently ignore any date formatting configuration within the operating system.

System-wide date format changes typically require altering the browser language rather than modifying the operating system settings. For instance, switching the `LANG` environment variable to `en_US.UTF-8` displays dates as mm/dd/yyyy, whereas `pt_BR` results in dd/mm/yyyy format. However, the `LC_TIME` variable appears to have inconsistent results across different systems.

Google Chrome's latest beta version displays dates in the DD-MM-YYYY format, though this behavior may vary between locales and browser versions. For developers seeking to change display formats, environment variable modifications offer a viable solution for Unix-based systems, particularly through changes to the `LANG` and `LC_TIME` variables.

The HTML5 specifications indicate that browsers derive date input formats from the user's system settings, with available options including dd/mm/yyyy, mm/dd/yyyy, and yyyy-mm-dd. While the HTML5 input type "date" control follows the RFC 3339 specification, using the full-date format YYYY-MM-DD, browsers maintain complete control over the visual presentation of date inputs.


## Input Types: date, datetime-local, time

The HTML input system provides specialized types for date and time selection: "date", "datetime-local", and "time". These elements simplify user interaction while ensuring proper validation and formatting.


### Date Input

The `<input type="date">` element provides a straightforward method for selecting dates, using a text field that automatically converts to a date picker when focused. This input type follows the HTML5 specification, which refers to the RFC 3339 standard for full-date format (`yyyy-mm-dd`). The element supports additional attributes for setting minimum and maximum dates, ensuring users select dates within a specific range.


### Time and Date-Time Inputs

The `<input type="time">` element allows users to select specific times, while `<input type="datetime-local">` combines date and time selection into a single control. Both inputs display pickers that conform to the browser's language settings, though developers can influence the format through HTML attributes.


### Implementation Variations

While browsers maintain control over visual presentation, developers can use several methods to influence display formats:

- Setting default values: Using the `value` attribute allows specifying a date format that displays in the input field, though this doesn't affect user input capabilities.

- Changing input type: Modifying an input field from "text" to "date" enables users to enter dates in a specified format, though this requires careful consideration of user preferences and system configurations.

The `<time>` element serves as a companion tag for date and time information, allowing semantic markup of specific times while supporting machine-readable formats through its `datetime` attribute. This attribute follows the same date-time syntax as the `<datetime-local>` input type, providing consistency across HTML5 date and time features.


## Customizing Display Formats

Web developers seeking to influence the display format of date and time inputs face several limitations. While browsers determine the input format based on system settings and user preferences, web authors have limited control over the visual presentation of these elements.


### Using Environment Variables

developers can modify environment variables to influence date formatting across different systems:

- For Linux, changing the `LANG` and `LC_TIME` environment variables affects date display. For example, setting `LANG` to `en_US.UTF-8` displays dates as `mm/dd/yyyy`, while setting it to `pt_BR` displays dates as `dd/mm/yyyy`.

- While `LC_TIME` doesn't work for the author, it may function differently on other systems.


### Custom Locale Creation

users can create custom locales using resources like `<http://lh.2xlibre.net/locale/pt_BR/>`, allowing precise control over date formatting. Advanced documentation references include:

- `<https://ccollins.wordpress.com/2009/01/06/how-to-change-date-formats-on-ubuntu/>`

- `<https://askubuntu.com/questions/21316/how-can-i-customize-a-system-locale>`


### Current Workarounds

developers can implement basic formatting guidance through existing attributes:

- The "pattern" attribute allows specifying a regular expression that the date input value must match, though it doesn't affect the display format.

- The "placeholder" attribute provides a hint for the expected input format.

However, the fundamental display format remains under browser control, with the HTML5 specification referencing the RFC 3339 format (`yyyy-mm-dd`) used in standard form submissions.

