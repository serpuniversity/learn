---

title: The HTML Meter Element: Displaying Scalar Measurements

date: 2025-05-29

---


# The HTML Meter Element: Displaying Scalar Measurements

The HTML meter element provides a standardized way to display scalar measurements within a known range, offering authors a semantic tag for representing values like disk usage, search query relevance, or password strength. While its implementation requires careful attention to attribute validation and styling considerations, the meter element enhances accessibility and provides valuable context through its interactive visual representation. This article examines the technical specifications, browser support, and implementation best practices for utilizing the meter element in web development projects.


## Overview of the `<meter>` Element

The HTML meter element is a specialized tag used to represent scalar measurements within a known range or fractional values, most commonly used to display disk usage, search query relevance, or password strength [doc1, doc2]. It requires both start and end tags: `<meter>``</meter>` [doc7].

Key attributes include:

- value: A required floating point number representing the current value of the gauge that the meter element represents [doc1, doc9].

- min and max: Floating point numbers defining the minimum and maximum values of the range [doc1, doc9]. The default values are 0 and 1, respectively [doc1].

- low, high, and optimum: Semantic attributes providing additional information about the range of the measurement [doc1, doc14]. The default values for low and high are equal to min and max, respectively [doc14].

The meter element's content model uses phrasing content, allowing document text and markup but disallowing additional meter elements among descendants [doc10]. The element inherited properties from HTMLElement include methods for manipulating the element's layout and presentation [doc5].


### Browser Support and Styling

Browser support for the meter element varies:

- 6.0+ for Safari

- 11.5+ for Opera

- 8.0+ for Internet Explorer through Randy Peterman's polyfill

- Universal support since Firefox 16 and Opera 11 [doc7, doc9].

Custom styling requirements differ between browsers:

- WebKit and Blink engines (Chrome, Safari) use pseudo-elements for display

- Firefox uses -moz-appearance: meterbar, resetting default bevel and emboss to none [doc9].

The element's appearance is determined by the "value" relative to "min" and "max" [doc12]. Developers should implement custom styles as browser inconsistencies exist with pseudo-element selectors [doc11]. Modernizr testing has shown failures in certain versions of Internet Explorer [doc9].


## Meter Element Fundamentals

The meter element requires six key attributes to function properly: min, max, low, high, optimum, and value. These attributes work together to create a meaningful scalar measurement within a defined range [doc1, doc2].


### Required Attributes

- **min**: Specifies the lower bound of the range [doc1, doc9]. The default value is 0 [doc1].

- **max**: Specifies the upper bound of the range [doc1, doc9]. The default value is 1 [doc1].

- **value**: Determines the current value of the gauge [doc1, doc9]. This attribute is required and must be a floating point number [doc1, doc14].


### Optional Attributes

- **low**: Specifies the lower threshold for low values [doc1, doc14]. The default value is equal to min [doc14].

- **high**: Specifies the upper threshold for high values [doc1, doc14]. The default value is equal to max [doc14].

- **optimum**: Specifies the preferred value within the range [doc1, doc14]. The default value is 50 [doc14].


### Content Model and Restrictions

The meter element's content model allows phrasing content but prohibits additional meter elements as descendants [doc10]. The element inherits properties from HTMLElement, providing methods for layout and presentation manipulation [doc5].


### Browser Support

The element requires both the start and end tags to function correctly [doc7]. Browser compatibility varies:

- Safari: 
6.0+

- Opera: 
11.5+

- Internet Explorer: 
8.0+ through Randy Peterman's polyfill

- Firefox: 16+

- Chrome: 8+


### Styling Considerations

While the element has a default appearance determined by browser rendering, developers can use CSS to customize the visual representation. The meter's appearance is influenced by the "value" in relation to "min" and "max" [doc12]. Browser inconsistencies exist with pseudo-element selectors, particularly in WebKit and Blink engines [doc11]. Modernizr testing has shown compatibility issues in certain versions of Internet Explorer [doc9] [doc13].


## Meter Element Attributes

The meter element requires six attributes to function properly: min, max, low, high, optimum, and value. These attributes work together to create a meaningful scalar measurement within a defined range, with each attribute serving a specific purpose [doc1, doc2, doc13].


### Required Attributes

- **min**: Specifies the lower bound of the range [doc1, doc9]. The default value is 0 [doc1].

- **max**: Specifies the upper bound of the range [doc1, doc9]. The default value is 1 [doc1].

- **value**: Determines the current value of the gauge and is required [doc1, doc9]. This attribute must be a floating point number [doc1, doc14].


### Optional Attributes

- **low**: Specifies the lower threshold for low values [doc1, doc14]. The default value is equal to min [doc14].

- **high**: Specifies the upper threshold for high values [doc1, doc14]. The default value is equal to max [doc14].

- **optimum**: Specifies the preferred value within the range [doc1, doc14]. The default value is 50 [doc14].


### Content Model and Restrictions

The meter element's content model allows phrasing content but prohibits additional meter elements as descendants [doc10]. The element inherits properties from HTMLElement, providing methods for layout and presentation manipulation [doc5].


### Value Range Validation

The meter element enforces strict validation on its attribute values:

- The value attribute must fall within the range defined by min and max attributes [doc1].

- The low attribute must be greater than min and less than high or max [doc14].

- The high attribute must be less than max and greater than low [doc14].

- The optimum attribute must be within the range defined by min and max attributes [doc1].


### Default Behavior and Fallbacks

If the value attribute is less than min, the meter appears empty [doc12]. Conversely, if the value exceeds max, the meter appears fully filled [doc12]. The element automatically provides descriptive text when the browser cannot render it, combining the value with context details from the title attribute [doc4].


### Browser Support and Implementation

Browser support varies between implementations:

- WebKit and Blink engines (Chrome, Safari) use pseudo-elements for visual rendering [doc11].

- Firefox uses -moz-appearance: meterbar, with default bevel and emboss effects reset to none [doc9].

- Internet Explorer requires a polyfill for basic functionality [doc8].


## Using the Meter Element

The meter element's implementation requires careful attention to both functionality and accessibility. When deciding whether to use the meter element, developers should consider whether their data represents a scalar measurement within a defined range [doc1].

When implementing the meter element, developers must define the minimum (min) and maximum (max) values of the range [doc1, doc13]. These values establish the boundaries for the measurement being represented. The current value (value) attribute must fall within this range [doc1]. For example, if measuring disk usage, the min value would be 0 (empty disk), and the max value would be 100 (full disk) [doc13].

The low and high attributes define thresholds for low and high values, respectively [doc14]. These attributes allow developers to provide additional context about the measurement. For instance, in a password strength indicator, the low value might represent a weak password (0-24 characters), the high value might represent an excellent password (80-100 characters), and the optimum value might represent a strong password (40-60 characters) [doc14].

Developers should ensure that the meter element's content remains meaningful when styled [doc9]. While modern browsers support the element, styling can affect accessibility and semantic clarity [doc9]. To maintain accessibility, developers should test the element's display across different screen readers and themes [doc7]. For improved accessibility, consider providing additional context using semantic markup, such as the title attribute [doc4].

The meter element's behavior is consistent across modern browsers for basic functionality [doc13]. However, developers should be aware of differences in how browsers handle styling and pseudo-elements [doc11]. As with any custom styling, developers should test the element's appearance in various environments to ensure consistent visual representation [doc13].


## Browser Support and Styling

The meter element's implementation requires careful attention to both functionality and accessibility. When deciding whether to use the meter element, developers should consider whether their data represents a scalar measurement within a defined range. The meter element requires the value attribute to function, establishing the current value of the gauge [doc1].

The meter's appearance is determined by the value attribute in relation to the min and max attributes [doc12]. When implementing the element, developers must define these minimum and maximum values that establish the boundaries for the measurement being represented [doc1]. The value attribute must fall within these defined bounds, with specific behavior for values outside these limits [doc1]: values lower than min result in an empty meter, while values higher than max result in a fully filled meter [doc12].

Browser support and styling requirements vary between implementations. WebKit and Blink engines (Chrome, Safari) require custom styling, using pseudo elements for visual rendering [doc11]. Firefox supports the element through pseudo elements and custom styles, using -moz-appearance: meterbar and resetting default bevel and emboss effects to none [doc9]. Internet Explorer requires a polyfill for basic functionality, while older versions of these browsers can display the element using div and span elements within the meter tag [doc5].

For custom styling, developers face browser inconsistencies, particularly with pseudo-element selectors. The meter element requires specific CSS properties for consistent display across browsers:

- Set border to 1px solid #ccc

- Apply border-radius of 3px

- Background-color should be whiteSmoke

- Use box-shadow: 0 5px 5px -5px #333 inset

- Set width to 550px and height to 25px

- Display must be block [doc5].

The span element within the gauge needs additional properties:

- Set height to inherit

- Apply box-shadow: 0 5px 5px -5px #999 inset

- Background-color should be blue

- Use linear-gradient with specific colors and sizes

- Display should be block

- Text-indent should be -9999px [doc5].

Modern browsers support the meter element, with current browser support at 53% as of February 2013 [doc2]. While most browsers display the element correctly, developers should test across different environments to ensure consistent visual representation. The element's behavior is generally consistent for basic functionality across modern browsers [doc3].

## References

- [HTML Viewport Meta tag](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Viewport%20Meta%20tag.md)
- [HTML Spellcheck](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Spellcheck.md)
- [HTML q The Inline Quotation Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20q%20The%20Inline%20Quotation%20Element.md)
- [HTML The HTML Option Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20HTML%20Option%20Element.md)
- [HTML The External Resource Link Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20External%20Resource%20Link%20Element.md)