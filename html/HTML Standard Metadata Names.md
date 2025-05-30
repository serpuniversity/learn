---

title: HTML Standard Metadata Names

date: 2025-05-29

---


# HTML Standard Metadata Names

Web developers regularly enhance their sites with metadata through HTML's `<meta>` element, yet many may not realize how standardized these metadata names have become. The HTML5 specification has established a curated list of standard metadata names serving crucial functions like application identification, content description, and author attribution. Whether you're optimizing for search engines or enhancing user experience, understanding these officially recognized metadata fields is essential for effective web development.


## Standard Metadata Names Defined

The HTML5 specification defines several standard metadata names for the `<meta>` element that web developers may use to provide additional semantic information about their pages. These standard names serve as a predefined set of metadata elements, including application-name, author, description, generator, and keywords.


### Application-Name Metadata

The application-name metadata provides a short string representing the name of the web application being represented by the page. When the site's standard `name` attribute doesn't meet user expectations, user agents may prefer displaying this name in their user interface instead.


### Author Metadata

This metadata contains a free-form string representing one of the page's authors. When multiple authors contribute to a document, this metadata allows specifying who is credited as the primary creator.


### Description Metadata

The description metadata supplies a short, human-readable summary of the page's content, particularly useful for search engine optimization purposes. As noted by MDN Web Docs, this information might be displayed directly in search engine results:

```html

<meta name="description" content="The MDN Web Docs site provides information about Open Web technologies including HTML, CSS, and APIs for both websites and progressive web apps." />

```


### Generator Metadata

This metadata records the software used to generate the document, which can help identify the source of the content. For example, a static site generator might include its name and version in this metadata field.


### Keywords Metadata

The keywords metadata lists relevant keywords associated with the document, traditionally used for search engine optimization. While its importance has diminished with modern search algorithms, it remains a valid metadata field for specifying important concepts related to the page's content.

The HTML Standard also outlines a registration process for new metadata names, ensuring that these extensions adhere to specific guidelines and do not conflict with existing naming conventions. This registration system maintains a curated set of metadata names that web developers can use to enhance their documents while ensuring compatibility across different web applications and user agents.


## Metadata Name Registration Process

Anyone can create new metadata names, but they should carefully consider whether the name conflicts with existing URLs or represents functionality that user agents may need to process specially. Before implementing a new name, Web developers should consult the WHATWG Wiki MetaExtensions page to ensure compatibility with existing metadata names.

When specifying a new metadata name, developers must provide several pieces of information:

- The keyword representing the name being defined

- A brief non-normative description of the metadata's meaning and required format

- A link to more detailed specification information, which could be another wiki page or external documentation

- A list of synonyms with identical processing requirements (though authors should not directly use these names, they are registered for legacy content compatibility)

The registration system defines three statuses for metadata names:

- Proposed: Names awaiting wide peer review and approval

- Ratified: Names that have received thorough review and approval, with defined handling for pages using them

- Discontinued: Names found unsuitable after review, with existing pages permitted to continue using them while new pages should avoid adoption

Notably, the system maintains pragmas defined with the `http-equiv` attribute on `meta` elements, including content-language, content-type, and default-style options that do not require state tracking. This flexible registration process balances innovation in web metadata with the need for compatibility and standardization across user agents.


## Metadata Tag Implementation

The `<meta>` tag provides document metadata through name-value pairs, with the `name` attribute specifying the metadata name and the `content` attribute providing the associated value. This tag is crucial for defining character encoding, page description, keywords, author identification, and viewport settings, all of which help browsers and search engines understand and properly display web content.


### Character Encoding

The `charset="UTF-8"` attribute within the `<meta>` tag specifies the character encoding used to display the page, with UTF-8 being particularly recommended due to its broad character coverage. For example:

```html

<meta charset="UTF-8">

```


### Page Description

The `name="description"` attribute allows webmasters to provide a concise summary of the webpage, which search engines may display in their results. This tag should include a brief, relevant description of the page's content.


### Keywords

While the `name="keywords"` attribute once played a significant role in SEO, modern search algorithms have reduced its importance. This attribute should include a comma-separated list of keywords relevant to the page's content.


### Author Information

The `name="author"` attribute specifies the page's author, providing credit without direct SEO impact. For multiple authors, this metadata allows specifying the primary creator.


### Viewport Configuration

The `name="viewport"` attribute is essential for creating mobile-friendly webpages, controlling the layout by defining the width and scale for different screen sizes.


### Metadata Registration Requirements

When creating new metadata names, developers must ensure they do not conflict with existing URLs or represent functionality that user agents process specially. The registration process requires specifying:

- Keyword: The actual metadata name

- Brief description: The metadata's meaning and required format

- Specification: A link to detailed information about the metadata's requirements

- Synonyms: Other names with identical processing requirements (for legacy content compatibility)


### Name Comparison Rules

The `name` attribute is compared in ASCII case-insensitive manner, allowing for flexibility in name declaration while ensuring consistent processing across implementations.


## Metadata Name Status and Usage

Before creating a new metadata name, developers must check whether the name conflicts with existing URLs or represents functionality that user agents process specially. This includes avoiding names that could cause unintended behavior when combined with URL values in the `content` attribute or those that require special handling by user agents.

According to the WHATWG Wiki MetaExtensions page, developers should provide detailed information about any new metadata names, including:

- Keyword: The actual name being defined

- Brief description: A short non-normative description of what the metadata name's meaning is, including the format the value is required to be in

- Specification: A link to a more detailed description of the metadata name's semantics and requirements (could be another wiki page or an external page)

- Synonyms: A list of other names that have exactly the same processing requirements (authors should not use these names, only intended for legacy content support)

- Status: One of the following options:

  - Proposed: Name has not received wide peer review and approval

  - Ratified: Name has received wide peer review and approval, with specification defining handling of pages using the name, including incorrect usage

  - Discontinued: Metadata name has received wide peer review and found wanting, existing pages using it, new pages should avoid, with details of replacement values

The system maintains several standard metadata names that define the processing requirements for metadata elements. These names include:

- application-name: A short free-form string giving the name of the web application represented by the page. This value may be translated using the `[lang]` attribute to specify language. The application name selection process begins with the document's language, adds any non-matching default language to the list, selects the first matching `meta` element, and returns the value of the `content` attribute.

- author: A free-form string giving the name of one of the page's authors. This metadata appears useful for Contact purposes, especially when content management systems automatically populate it.

- description: A free-form string describing the page, intended for use in page directories such as search engine results. This metadata provides a concise summary of the page's content.

- generator: A string identifying the software used to generate the document. This metadata allows distinguishing between content created by different tools.

- keywords: A set of comma-separated strings, each representing a keyword relevant to the document. While its importance has diminished with modern search algorithms, this metadata remains useful for specifying important concepts related to the page's content.


## Known Issues and Compatibility

The HTML Standard's metadata framework includes several mechanisms that impact how authors define and implement metadata. These features range from fundamental parsing requirements to high-level architectural constraints that affect document compatibility and performance.


### Parsing and Syntax Constructs

The specification defines several syntax rules that impact metadata implementation. Notably, unclosed `i` elements require special handling, with all unclosed elements reconstructed in each paragraph. This can lead to unexpected DOM structures when parsing HTML documents.

The text also highlights issues with named character references, noting that they require a semicolon to prevent interpretation as characters. This requirement ensures predictable parsing behavior but can introduce subtle errors in metadata implementation.


### Interoperability Challenges

A significant challenge arises from the restricted use of the GRAVE ACCENT character (`) in unquoted attributes. The specification requires a valid DOCTYPE to trigger no-quirks mode, while UTF-7 encoding is restricted to prevent cross-site scripting attacks. These requirements help maintain a robust web platform but can complicate implementation for metadata providers.


### Implementation Quirks

The standard includes several implementation quirks that affect metadata implementation. For instance, the `template` element's template contents have a null browsing context, which exempts them from content model requirements and attribute value microsyntax requirements. This exemption can lead to unexpected behavior when implementing custom metadata models.


### Error Handling and Conformance

The HTML Standard prioritizes robust error handling, particularly in cases where incorrect metadata can cause significant issues. For example, the specification prevents the value "false" for elements that appear to be enabled but indicate disabled status. This design simplifies implementation requirements but can cause confusion in tutorials and documentation.

In cases where metadata might interact with URL values, the specification requires careful attention to attribute syntax. For example, the `area` element's `shape` attribute accepts both "circ" and "circle", but the specification disallows "circ" to simplify learning materials. This restriction helps prevent common authoring errors while maintaining consistency across implementations.


### Document Structure and Conformance

The specification defines specific document structure requirements that impact metadata implementation. DOM nodes with a null browsing context, such as those inside shadow trees, are exempt from most document conformance requirements except for HTML syntax rules. This exemption applies particularly to the `template` element's template contents, which can affect how metadata is applied to dynamic content.

The text also notes that non-conforming attribute values and attributes, such as the `carpet` input type or an attribute `texture` that is not permitted, will be treated as missing attributes by user agents. This behavior ensures consistent parsing but can cause metadata to be ignored in certain contexts.


### Advanced Features and Quirks

The HTML Standard includes advanced features that can affect metadata implementation. For instance, the `form` element's content model restricts it from appearing inside phrasing content, which can impact how metadata is associated with form-related information. Similarly, the text explains that authors should not use elements, attributes, or attribute values for purposes other than their intended semantic purpose, particularly in cases where `hgroup` elements are used to represent multiple levels of heading hierarchy.

These implementation details demonstrate the complexity of metadata handling in the HTML Standard, requiring authors to consider not only semantic correctness but also parsing implications and implementation quirks.

## References

- [HTML div The Content Division Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20div%20The%20Content%20Division%20Element.md)
- [HTML Font](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Font.md)
- [HTML Nonce](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nonce.md)
- [HTML Attribute max](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20max.md)
- [HTML The Textarea Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Textarea%20Element.md)