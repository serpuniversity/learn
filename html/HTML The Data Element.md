---

title: HTML Data Element: Linking Content with Machine-Readable Data

date: 2025-05-29

---


# HTML Data Element: Linking Content with Machine-Readable Data

Linking web content with machine-readable data has become increasingly crucial as the web evolves from static information publishing to interactive, data-driven applications. The HTML Data element, introduced to provide a standardized way of associating content with structured data outputs, represents a significant step towards more intelligent web interactions. This specification defines how the Data element functions within HTML's structure, how developers and developers implement its features, and the practical applications that enable both enhanced functionality and improved user experiences. As modern browsers continue to adopt and refine these standards, understanding the Data element's capabilities and limitations becomes essential for creating web applications that truly harness the power of the modern web.


## Defining the Data Element

The HTML Data element enables content to be associated with machine-readable output through a structured value attribute. As described in the HTML Standard, this element represents its children and captures machine-readable data in the context of web-based applications and documents.

The content category for the Data element encompasses both flow content and phrasing content, as documented in the HTML Standard. This dual classification allows for versatile integration within various HTML structures while maintaining consistent interpretation across modern browsers.

A practical example of Data element usage is demonstrated in product listings, where each data instance contains a specific value identifier. For instance, different product variants may be distinguished through unique numeric identifiers: "499" for Mini PC, "899" for Small laptop, "1399" for Large laptop, and "2099" for Desktop PC. This integration facilitates enhanced functionality for both developers and machine processors, particularly when combined with microformats or microdata attributes.


## Data Attribute Implementation

The data-* attribute allows developers to store custom data directly within HTML elements, offering a flexible way to enhance both content and functionality. According to the HTML standard, this attribute follows specific naming conventions:

- Attribute names must begin with "data-" and contain only lowercase letters

- The attribute may be used without a value: data-foo

- It supports values of any string, including those containing HTML

Developers leveraging data-* attributes can implement various use cases:

- Database functionality: Track specific database record identifiers

- Custom styling: Use CSS's attr() function based on attribute values

   Example: [data-size="large"] { padding: 2rem; font-size: 125%; }

The attribute enjoys widespread browser support across multiple engines:

Firefox 6+

Safari 10+

Chrome 62+

Opera 79+

Edge 79+

Firefox Android

Safari iOS

Chrome Android

WebView Android

Samsung Internet

Opera Android

When implementing data-* attributes, developers should adhere to the following guidelines:

- Store encoded data to prevent security vulnerabilities

- Use PHP's htmlspecialchars() function to safely encode data

- Consider the attribute's accessibility implications, particularly when embedding time or date-related information


## Data Usage and Examples

The `<data>` element combines machine-readable value representation with human-readable content display, while also supporting integration with microformats or microdata attributes. This dual functionality allows for both structured data processing and direct content presentation, as demonstrated in product listing examples where each data instance contains specific value identifiers for different product variants.

Implementation of data attributes extends beyond standalone usage, demonstrating versatile application across various elements. For instance, the `<input>` element can incorporate data attributes to capture dynamic user input, with proper handling through server-side processing to maintain consistent format translation between client and server environments. The `<button>` element can similarly utilize data attributes to store specific action identifiers, facilitating both client-side interaction and server-side processing.

The data-* attribute's browser compatibility spans all major engines, supporting both desktop and mobile environments across modern browsers. Implementation best practices emphasize encoding requirements, particularly when storing JSON data, where direct value assignment requires client-side decoding using JSON.parse(). For security and accessibility considerations, developers should employ proper sanitization techniques, such as PHP's htmlspecialchars() function, to prevent vulnerabilities while ensuring compliant data representation.


## Browser Support and Compatibility

The HTML Data element and its functionality are supported across all major browsers, with consistent implementation across current engines. The element, introduced as "Defines content linked to machine-readable output" in the HTML Standard, represents its children and captures machine-readable data through the value attribute.

The Data element's value attribute specifies the machine-readable translation of the content, as demonstrated in examples where product names link to specific numeric identifiers: "499" for Mini PC, "899" for Small laptop, "1399" for Large laptop, and "2099" for Desktop PC. This functionality combines human-readable content display with structured data processing capabilities.

The Data element's browser compatibility spans all current engines, including:

- Firefox 22+

- Safari 10+

- Chrome 62+

- Opera 79+

- Edge 79+

- Firefox Android

- Safari iOS

- Chrome Android

- WebView Android

- Samsung Internet

- Opera Android

For specific attribute functionality, the element supports:

- action attribute (Firefox 1+, Safari 4+, Chrome 1+, Opera 8+, Edge 79+, Edge (Legacy) 12+, Internet Explorer 5.5+)

- form-related attributes (Firefox 1+, Safari 3+, Chrome 1+, Opera 12.1+, Edge 79+, Edge (Legacy) 12+, Internet Explorer 6+)

- target attribute (Firefox 1+, Safari 3+, Chrome 1+, Opera 12.1+, Edge 79+, Edge (Legacy) 12+, Internet Explorer 6+)

- type attribute for object representation (Firefox 1+, Safari 3+, Chrome 1+, Opera 12.1+, Edge 79+, Opera Android 12.1+, Internet Explorer 5.5+)

The element follows a consistent content category classification of flow content and phrasing content, making it adaptable for various HTML structures while maintaining uniform interpretation across browser implementations.


## Accessibility and Best Practices


### Accessibility and Best Practices

Data elements and attributes must adhere to accessibility guidelines, particularly when embedding time or date-related information. The HTML standard specifies that dateTime attributes must conform to specific syntaxes: valid month strings, valid date strings, valid yearless date strings, valid time strings, and valid local date and time strings.

The Data element requires proper sanitization techniques to prevent security vulnerabilities. User agents should treat persistently stored data as potentially sensitive, ensuring prompt deletion from underlying storage when deleted. For data mining tools, specific requirements include maintaining paragraph nesting levels and preventing heading nesting level increases when generating document outlines.


### Security Considerations

The Data element presents two primary security risks: information leakage and information spoofing. Third-party sites can access data not intended for their domain, such as users' shopping wishlists being used for targeted advertising or work-in-progress documents accessed by competitors. Hostile sites can manipulate data by adding items to wishlists or setting session identifiers to track user actions.

To prevent cross-site scripting attacks, user input must use safelist-based filters, allowing known-safe constructs while disallowing all other input. This approach is more secure than blocklist-based filters, which can fail to protect against emerging threats. When allowing img elements, attributes must be explicitly safelisted, and URL schemes must be explicitly safelisted, including javascript: and other user agent-implemented schemes.


### Implementation Requirements

HTML implementations must support both scripting and non-scripting modes. Implementations without scripting support (or with scripting disabled) are exempt from supporting specific events and DOM interfaces mentioned in the specification. These user agents must act as if events and DOM were supported. Conformance checkers must verify document conformance to specified criteria, checking both with and without scripts and ensuring scripts do not cause non-conforming states.


### Usage Guidelines

Data elements can be used as orphan nodes, such as creating a td element in a script. However, authors must use HTML elements only where explicitly allowed or required by other specifications, including XML compound documents where elements from other namespaces can provide relevant contexts. When embedding time or date-related information, authors should employ proper sanitization techniques, particularly when storing JSON data, where direct value assignment requires client-side decoding using JSON.parse().

