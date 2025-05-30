---

title: HTML The generic search element

date: 2025-05-29

---


# HTML The generic search element

The HTML `<search>` element represents a container for form controls or content related to search operations, with support across major browsers including Firefox, Safari, Chrome, Opera, and Samsung Internet. This introduction will explore the element's characteristics, accessibility benefits, and implementation considerations for developers working with search functionality in web applications.


## Introduction to the HTML Search Element

The `<search>` element represents a container for form controls or content related to search or filtering operations. It can be used for various scopes, including global site search, page-specific searches, or Internet-wide searches. The element must be used where flow content is expected and requires both opening and closing tags. Support for this feature is currently limited, with major browser engines including Firefox, Safari, Chrome, Opera, and Samsung Internet not implementing it.

The `<search>` element defines an implicit ARIA role of "search," which provides accessibility benefits by automatically adding the appropriate landmark role to the element. It supports multiple ARIA roles including "form," "group," and "region." The element's content falls under the categories of "flow content" and "palpable content." The HTML specification treats the `<search>` element as a generic search container that can wrap form controls or perform JavaScript-based filtering without a traditional form structure.

Examples of its usage include website header search forms and web application search functionality. The element can contain input fields for searching and filtering, checkboxes for match options, and sections for displaying search results and no results content. While not specifically designed for presenting search results, it can include "quick search" functionality with suggestions and links that should be nested within the search container.


## Element Characteristics and Support

The `<search>` element requires both opening and closing tags and defines an implicit ARIA role of "search," which removes the need for adding `role="search"` to a `<form>` element. This landmark role provides accessibility benefits by automatically adding the appropriate landmark role to the element.

The element supports multiple permitted ARIA roles, including "form," "group," "none," "presentation," "region," and "search." Its content falls under the categories of "flow content" and "palpable content." The element's DOM interface uses the `HTMLElement` interface, which supports metadata attributes such as `title`, `lang`, `translate`, and `dir`, as well as user interaction attributes.

Browser compatibility is currently limited, with major engines including Firefox, Safari, Chrome, Opera, Samsung Internet, and Opera Android not implementing the feature. The `<search>` element is only appropriate for containing form controls or performing search/filtering operations within a website or application, not for presenting search results. Suggestions and links for quick search functionality should be nested within the `<search>` element rather than presented as standalone content.


## Content and Accessibility

The `<search>` element's content model consists of flow content and palpable content, meaning it can contain any flow content elements and text that could be read aloud to assist visually impaired users. To ensure accessibility, content within the element should be descriptive and provide clear instructions for users.


### Tag Requirements

Both the `<search>` element's opening and closing tags are mandatory, ensuring proper structure and facilitating parsing by assistive technologies. The element must contain at least one form control, such as an `<input>` element with the type attribute set to "search".


### ARIA Roles

The element defines an implicit ARIA role of "search", which provides basic accessibility information. For more complex implementations, it supports additional ARIA roles including "form", "group", "none", "presentation", "region", and "search". The appropriate role should be chosen based on the element's specific functionality and content.


### Content Nesting

While the `<search>` element itself is not intended for displaying search results, it can contain elements related to filtering and quick search functionality. This includes input fields, checkboxes for match options, and sections for displaying filtered content. These nested elements should be clearly marked and structured to maintain accessibility and usability.


### Implementation Best Practices

To ensure optimal accessibility, developers should:

- Use descriptive labels for form controls

- Provide error messages for invalid input

- Implement proper keyboard navigation

- Use semantic HTML elements where appropriate (e.g., `<header>`, `<footer>`, `<aside>`)


## Implementation Examples

The `<search>` element can wrap a standard submittable search form, with the form having the role="search" attribute. In this scenario, the form acts as a generic search container that posts to a backend to display a filtered list. When implementing such functionality, the form can be wrapped in the `<search>` element to remove the need for the role="search" attribute on the form element.

For more modern filterable search implementations, the element can be used without a traditional form structure. In one example, an Angular application demonstrates JavaScript-based filtering functionality. The search element allows filtering results within the client without requiring a form submission, as demonstrated in the following code snippet:

`<search>`

  `<label for="search">`Search Players`</label>`

  `<input type="search" id="search" autocomplete="off" [(ngModel)]="searchText" placeholder="Search by entering a player name" />`

  `<button type="submit">`Go`</button>`

`</search>`

When implementing search functionality, developers are encouraged to follow the ARIA specification, which recommends using the element that provides appropriate semantics when one exists. In these cases, the search element should replace the ARIA role attribute. The element supports multiple permitted ARIA roles, including "form," "group," "none," "presentation," "region," and "search," allowing for flexibility in accessibility and user interface design.


### Implementation Considerations

To effectively implement search functionality using the `<search>` element, developers should consider the following best practices:

- Wrap search functionality and results within the element

- Use appropriate form control elements (e.g., `<input type="search">`)

- Implement proper error handling for invalid input

- Provide clear instructions for users

- Ensure proper keyboard navigation and accessibility


## Technical Specifications

The `<search>` element processes input values through specific steps, maintaining the original order and combining values with U+002C COMMA (comma) separators. Constraint validation checks for valid email address lists, where each address must match the ABNF production from RFC 1123 and follow Unicode character set rules. Email addresses can contain atext (RFC 5322 section 3.2.3) or "." (RFC 1034 section 3.5) syntax, with a maximum length of 63 characters and a structure defined by label (let-dig [ldh-str let-dig]). Valid examples include "user@example.com".

The element's value is defined through a set of comma-separated tokens, each representing a valid email address. Email addresses are extracted by splitting the string on commas. The `<search>` element supports multiple attributes including autocomplete, dirname, list, maxlength, minlength, multiple, pattern, placeholder, readonly, required, and size. For the multiple attribute, users can select multiple email addresses, supported across all current engines including Firefox 3.6+, Safari 4+, Chrome 2+, Opera 12.1+, Edge 79+, Internet Explorer 10+, Firefox Android, Safari iOS, Chrome Android (version 37+), WebView Android, Samsung Internet, and Opera Android (version 12.1+).

The element's value is managed through IDL attributes and methods, including list, value, and select(). Supported events include input and change. The element does not support attributes such as accept, alpha, alt, checked, colorspace, formaction, formenctype, formmethod, formnovalidate, formtarget, height, max, min, popovertarget, popovertargetaction, src, step, or width. Similarly, IDL attributes and methods like checked, files, selectionStart, selectionEnd, selectionDirection, valueAsDate, and valueAsNumber are not supported. Instead, the `<search>` element represents a one-line plain text edit control with user agent value obscuration, supported across all current engines.

## References

- [HTML rtc The Ruby Text Container Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20rtc%20The%20Ruby%20Text%20Container%20Element.md)
- [HTML A The Anchor Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20A%20The%20Anchor%20Element.md)
- [HTML Author Fast Loading HTML Pages](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Author%20Fast%20Loading%20HTML%20Pages.md)
- [HTML Using HTML Comments](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20HTML%20Comments.md)
- [HTML Accesskey](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Accesskey.md)