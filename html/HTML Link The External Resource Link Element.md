---

title: HTML `<link>`: The External Resource Link element

date: 2025-05-29

---


# HTML `<link>`: The External Resource Link element

The `<link>` element in HTML serves as a versatile tool for establishing connections between web pages and external resources, from simple stylesheet linking to complex metadata exchange. Through its rich attribute set and support for specialized link types, the `<link>` element enables developers to fine-tune web page behavior, optimize resource loading, and enhance user experience across diverse platforms and devices. This comprehensive examination explores the element's capabilities, from its basic usage patterns to its advanced functionalities, providing developers with a detailed understanding of how to effectively utilize the `<link>` element in modern web development practice.


## Definition and Basic Usage

The `<link>` element establishes relationships between the current web page and external resources. It is used in the `<head>` section of an HTML document to link to stylesheets, scripts, or other resources that are required for the document to function properly.

The element has several key attributes:

- The "href" attribute specifies the URL of the external resource. This can be an absolute URL or a relative URL, which is relative to the root domain.

- The "type" attribute specifies the MIME type of the resource, such as "text/css" for CSS files or "text/html" for HTML documents.

- The "rel" attribute specifies the relationship between the current document and the external resource. Common values include "stylesheet" for linking to stylesheets, "icon" for favoricons, and "next" for navigation purposes.

Additional attributes provide more specific functionality:

- "media" attribute indicates the intended rendering medium, allowing resources to be loaded based on the device capabilities.

- "title" attribute defines a preferred or alternate stylesheet, which can affect how user agents handle the linked resource.

- "sizes" attribute specifies the size of the linked resource, particularly important for icon links where different size variants may be available.

The `<link>` element supports advanced features through additional attributes like "crossorigin" for handling cross-origin requests, "referrerpolicy" for controlling referrer information, and "integrity" for specifying metadata about requests. These features enable more sophisticated resource management and security controls.


## Link Types and Attributes

The href attribute specifies the URL of the external resource, which can be either an absolute URL or a relative URL that is resolved relative to the root domain. The type attribute defines the MIME type of the resource, providing a hint about the format to expect. The rel attribute establishes the relationship between the current document and the external resource, with common values including "stylesheet" for linking to CSS files and "icon" for favoricons.

Additional attributes provide more granular control over how resources are handled:

- The hreflang attribute specifies the language of the linked resource, using BCP 47 language tags. This helps user agents determine appropriate content when multiple versions of a resource exist in different languages.

- The media attribute allows the resource to be conditionally loaded based on device characteristics, using valid media queries to define the target environment.

- The title attribute provides human-readable information about the linked resource, which can affect how the user agent handles the link. For stylesheet links, this attribute can define CSS style sheet sets.

- The sizes attribute specifies the dimensions of the linked resource, particularly important for icon links where multiple size variants may be available. This attribute helps user agents select the most appropriate version of the icon based on the current display requirements.

The crossorigin attribute controls how cross-origin requests are handled, allowing values of "anonymous" or "use-credentials" to define the level of request authentication required. The referrerpolicy attribute determines which referrer information is sent when fetching the resource, with options including "no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-cross-origin", or "unsafe-url".

The link element's behavior can be further customized through event attributes like onclick, ondblclick, onmousedown, onmouseup, onmouseover, onmousemove, onmouseout, onkeypress, onkeydown, and onkeyup, which allow developers to define custom behaviors when the link is interacted with. These attributes enable sophisticated interactions while maintaining the element's primary function of establishing external resource relationships.


## Special Link Types

The `<link>` element supports specialized purposes through dedicated link types. These include:


### Stylesheet Linking

The most common use case is linking to CSS stylesheets through the "stylesheet" relationship type. This is achieved with the following attributes:

- `href` specifies the path to the stylesheet

- `rel` sets the relationship to "stylesheet"

- `type` defines the content type as "text/css"

Additional attributes enhance this functionality:

- `media` allows conditional loading based on device characteristics

- `title` provides alternatives for preferred stylesheets

- `sizes` specifies icon sizes for visual media

For example, to link to a stylesheet:

```html

<link rel="stylesheet" href="styles.css">

```


### Icon Linking

The "icon" relationship type is used for site icons, including traditional favicons and modern app icons:

- `sizes` attribute defines the icon's pixel dimensions

- `rel` attribute can include "apple-touch-icon-precomposed" for mobile platform compatibility

Example:

```html

<link rel="icon" href="favicon.ico" sizes="16x16 32x32 64x64">

<link rel="apple-touch-icon-precomposed" href="apple-touch-icon.png">

```


### Preloading

The "preload" relationship type enables preloading content before it's needed:

- `as` attribute specifies the resource type (e.g., font, script, image)

- `type` attribute defines the content type

- `media` attribute applies media queries for conditional loading

Example:

```html

<link rel="preload" href="fontawesome-webfont.woff2" as="font" type="font/woff2" crossorigin>

```


### Additional Use Cases

The element supports several other relationship types:

- `author` links to the web page's author website

- `authorship` indicates authorship metadata

- `canonical` provides the preferred version of a web page

- `next` points to the next page in a series

These specialized uses demonstrate the element's versatility in managing external resources beyond basic stylesheet linking.


## Rendering and Behavior

The `<link>` element's rendering properties and behavior are governed by several key factors, including its attributes and the presence of other elements like `<base>`.


### Render-blocking Behavior

Network handling for the `<link>` element involves queuing element tasks for success/failure events. The element's rendering can be conditionally applied based on the media attribute and potential render-blocking status. If the element's CSS rules are initialized and associated with a CSS style sheet, these rules may cause render-blocking behavior, particularly when linked resources are required for critical rendering paths.


### Resource Preloading

The `<preload>` relationship type enables preloading content before it's needed, with attributes like "as" specifying the resource type (e.g., font, script, image), and "type" defining the content type. Preloading can significantly improve load times for essential resources.


### Conditional Loading

The media attribute allows resources to be conditionally loaded based on device characteristics using valid media queries. This attribute interacts with the `<base>` element, which specifies the base URL for all relative URLs in the document, enabling precise control over resource loading based on the document's context.


### User Agent Handling

The user agent updates `<style>` blocks when certain conditions occur: the element is popped from the parser stack, becomes connected/disconnected, or children change. When the element's inline behavior is blocked, the user agent creates a CSS style sheet with type "text/css" and the specified owner node, potentially affecting the document's rendering properties and behavior.


### Shadow DOM Integration

The `<link>` element's behavior integrates with Shadow DOM through the creation of `<slot>` elements for component-based development. This integration allows developers to create separate DOM trees and combine them effectively, supporting modern web development practices while maintaining standard element behavior.


## Advanced Usage

The `<link>` element's advanced capabilities extend beyond basic resource linking through several important mechanisms:


### Navigation Links

Similar to the `<A>` element, the `<link>` can establish navigation links between documents using specific relationship types like "prev" and "next". These links enable structured document navigation without requiring visible anchor content in the document body. For example:

```html

<link rel="prev" href="chapter4.html">

<link rel="next" href="chapter6.html">

```


### Metadata Exchange

The `<link>` element facilitates metadata exchange between documents through various relationship types and attributes. This includes providing alternative stylesheet preferences using the "title" attribute or defining specific resource types like fonts with the "as" attribute. The ability to specify character encodings through the "charset" attribute (now deprecated in favor of Content-Type headers) demonstrates the element's role in metadata transmission.


### Conformance Handling

The element's structure and content requirements enforce proper document authoring practices, as specified in the HTML standard's conformance requirements. Authors must adhere to strict rules about namespace usage and element content, with user agents acting as implicit authors when processing documents. This ensures consistent rendering across different user agents while maintaining document structure integrity.


### Browser Compatibility

The `<link>` element's implementation varies across different user agent categories. Web browsers and interactive user agents process elements from the HTML namespace according to the specification, enabling robust web functionality. Non-interactive presentation user agents, including printers and overhead displays, must comply with these rules while maintaining rendering flexibility through user options.


### ARIA Integration

The `<link>` element's interaction with ARIA roles and pseudo-classes demonstrates its importance in modern web development practices. When combined with the `<a>` element, these features enable advanced accessibility and user interaction capabilities, particularly for speech browsers where traditional navigation controls may be insufficient. The element's ability to support both visible and metadata links makes it valuable for both content presentation and assistive technology integration.

## References

- [HTML li The List Item Element Demo](https://github.com/serpuniversity/learn/blob/main/html/HTML%20li%20The%20List%20Item%20Element%20Demo.md)
- [HTML Relprefetch](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relprefetch.md)
- [HTML Allowing Cross Origin use Of Images And Canvas](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Allowing%20Cross%20Origin%20use%20Of%20Images%20And%20Canvas.md)
- [HTML The Progress Indicator Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Progress%20Indicator%20Element.md)
- [HTML Attribute Autocomplete](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Autocomplete.md)