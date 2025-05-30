---

title: HTML External Resource Link Element

date: 2025-05-29

---


# HTML External Resource Link Element

The HTML `<a>` element, particularly through its `<link>` counterpart, establishes fundamental connections between web resources. These connections, via attributes like href and rel, enable sophisticated navigation and resource management. From defining character encodings and content types to controlling cross-origin requests and specifying link relationships, the `<link>` element's capabilities expand beyond simple page navigation. Understanding its attributes and usage scenarios is crucial for developers aiming to create accessible, optimized, and secure web applications.


## Core Attributes

The href attribute (links.html#adef-href) specifies the destination of the link, defining a link between the current element (source anchor) and the destination anchor defined by this attribute. This attribute's value can be set through scripts and supports multiple URI formats: absolute URIs (http://www.mycompany.com/one.html#anchor-one), relative URIs (./one.html#anchor-one or one.html#anchor-one), and same-document references (e.g., #anchor-one).

The href attribute enables several use cases for the `<a>` element, including standalone elements without href that create an anchor without specifying a destination, links to existing anchors requiring both href and name attributes, and links to different Web resources that require href alone.


### Document-Specific Attributes

The name attribute (links.html#adef-name-A) creates an anchor around specified text, making the anchor name part of the fragment identifier in URLs. The id attribute (global.html#adef-id) functions similarly to name but requires unique document-wide identifiers, with names differing only in case not allowed in the same document.


### Advanced Linking Features

The element supports several attributes that enhance its functionality. The charset attribute defines the character encoding of the linked resource, with a default value of ISO-8859-1 (as documented in RFC2045), and may be used for specific character sets like those required for Arabic manuals.

Additional attributes for enhancing link behavior include:

- rel and rev attributes for defining document relationships (document types, next/previous links, icon links)

- type attribute for providing advisory content type hints

- title attribute for adding context to style sheet links

- sizes attribute for specifying icon sizes, particularly useful for Apple touch icons

- media attribute for indicating the intended device rendering the linked document


## Link Relationships

The rel attribute defines the relationship between the current document and the anchor specified by the href attribute. Possible values include alternate, bookmark, chapter, contents, copyright, glossary, help, icon, and subsection. Most common usage is to specify a link to an external style sheet, setting rel to stylesheet and href to external style sheet URL.


### Link Relationship Values

For example, to establish navigation between multiple chapters in a document collection, the rel attribute can use the values "prev" and "next" to indicate relationships to previous and next resources, respectively. These values form part of a defined framework in the HTML specification for navigating document series.


### Reverse Relationship

The rev attribute shows the relationship of the current document to the linked document, as defined by the href attribute. It mirrors the values used in the rel attribute but defines a reverse relationship. For instance, using rel to link to a related document with "next" should be mirrored in the target document with rev="prev".


### Obsolete Attribute Usage

According to the WHATWG HTML Living Standard, while the rev attribute may continue to work in current user agents, it is considered obsolete and authors should use rel instead, specifying the opposite link type value. This suggests, for example, establishing a reverse link for made by specifying author in the rel attribute of the target document.


## Link Options

The link element supports several attributes that provide additional information about linked resources. These attributes enable authors to specify content type, character encoding, and other metadata that can enhance browsing experience and ensure proper resource handling.


### Content Type and Encoding

The type attribute defines the MIME type of the linked document, allowing user agents to determine how to handle the resource (e.g., text/html, application/pdf). While the attribute can be used for various content types, it is particularly useful for CSS stylesheets, where it is recommended to omit the type declaration if possible.

The charset attribute specifies the character encoding of the linked resource, with a default value of ISO-8859-1. For specialized character sets like those required for Arabic manuals, the attribute allows precise encoding definitions. However, authors should consider using the Content-Type HTTP header for character encoding declarations, as the charset attribute may be ignored by some user agents.


### Link Title and Description

The title attribute provides a textual description of the linked resource, useful for accessibility and context. In the case of `<link rel="stylesheet">` elements, the attribute can define preferred or alternate stylesheets, helping user agents select the most appropriate style sheet based on device capabilities and user preferences.


### Icon and Image Descriptions

The sizes attribute plays a crucial role in specifying different icon sizes for visual media, particularly Apple touch icons. By providing multiple icon sizes, authors can optimize image loading and ensure that browsers select the most appropriate icon based on the device's display requirements. Common values for the sizes attribute include "any" for vector formats and white-space separated pixel dimensions (e.g., 16x16, 32x32, 64x64).


### Security and Privacy

The unsafe-url attribute allows linking to resources that may contain sensitive information, though its usage is generally discouraged. The crossorigin attribute enables fine-grained control over cross-origin resource sharing, with values including anonymous and use-credentials. The referrerpolicy attribute provides privacy options, allowing authors to specify how referring information should be shared with linked resources (values include no-referrer, no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, and unsafe-url).


### Implementation Considerations

Authors should follow best practices for implementing these attributes, including placing link elements in the head section of the document. For document structure, rel attributes should specify relationships between documents using space-separated link types. The href attribute remains essential for defining the destination of the link, while the as attribute can specify the type of the linked resource (e.g., style, script, image, document, font, manifest).


## Contextual Usage

The HTML External Resource Link element, specifically the BASE element, serves to specify a document's base URI explicitly. This element must appear in the HEAD section of an HTML document before any element that refers to an external source. The BASE element's path information only affects URIs in the document where the element appears.

The BASE element's href attribute specifies an absolute URI that acts as the base URI for resolving relative URIs. The element's attributes include:

- Required attribute: href (URI)

- Attribute definition: href = [uri] (CT)

- Attribute type: [%URI;]

The element's behavior is governed by RFC1808, section 3, with user agents calculating the base URI according to specific precedences:

1. The base URI is set by the BASE element

2. The base URI is given by meta data discovered during a protocol interaction, such as an HTTP header

3. By default, the base URI is that of the current document

HTML documents containing relative URIs must have a base URI, with documents appearing in email without a URI considered erroneous. The OBJECT and APPLET elements define attributes that take precedence over the value set by the BASE element.

In the context of document positioning, the link element enables sophisticated navigation structures. According to the W3C recommendation, destination anchors can be created using either the A element with the name attribute or any other element with the id attribute. This flexibility allows authors to establish both source and destination anchors within the same document, enabling complex navigation patterns.

For example, an HTML document might contain nested headings that serve as both source and destination anchors:

```html

<h1>Chapter 1</h1>

<p>Page contents</p>

<a href="#Chapter2">Go to Chapter 2</a>

<h2 id="Chapter2">Chapter 2</h2>

<p>Chapter contents</p>

```

This structure allows users to navigate directly between section headings without scrolling through intermediate content. The link element's versatile attribute set, including rel, rev, type, and href, enables these sophisticated connections while providing options for metadata and relationship specification.


## Advanced Features


### Cross-Origin Resource Control

The crossorigin attribute enables fine-grained control over how the link handles cross-origin requests, with two primary values:

- anonymous: No special credentials handling required

- use-credentials: Requires matching credentials for secure requests


### Referrer Policy

The referrerpolicy attribute controls which referrer information is sent with requests, offering several options:

- no-referrer: No Referer header sent

- no-referrer-when-downgrade: No Referer header sent when navigating to non-TLS origin

- origin: Referrer includes scheme, host, and port

- origin-when-cross-origin: Referrer includes scheme, host, and port for cross-origin navigation, path for same-origin

- unsafe-url: Includes full referrer path and URL


### Target Frame

The target attribute defines the frame or window for rendering the linked resource, supporting both linking relationships and resource rendering. Common values include:

- _self: Renders in the current window ("Click to view")

- _blank: Opens in a new tab or window ("Open in new tab")

- _parent: Renders in the parent frame or window

- _top: Renders in the entire top-level window, replacing existing content

