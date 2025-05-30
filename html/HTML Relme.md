---

title: HTML rel=me: Linking Web Identities with Microformats

date: 2025-05-29

---


# HTML rel=me: Linking Web Identities with Microformats

The HTML `rel="me"` attribute has evolved significantly since its introduction as part of the XHTML Friends Network (XFN) specification. Originally designed to link web identities, it has become essential for verified site linking, social authentication, and digital identity verification across platforms. This article explores the technical foundations of `rel="me"`, its implementation across various HTML elements, and its crucial role in modern web development. From enabling simple personal connections to facilitating robust authentication processes, understanding the attribute's capabilities is vital for web developers, content creators, and platform implementers working to establish trusted online identities.


## What is HTML rel=me?

The `rel="me"` attribute originates from the XHTML Friends Network (XFN) microformat specification, where it indicates that the current resource is represented by the linked party. This semantic relationship enables individuals to identify themselves to web services via their domain name or specific URL. The attribute's use has evolved through various implementation stages, including support for domain verification, social link authentication (RelMeAuth), and web-sign-in functionality.

Developed as part of the XFN 1.1 specification, the `rel="me"` value establishes profile equivalence and identity consolidation between pages. For instance, Tantek's home page might contain a simplified hyperlink `<a href="https://github.com/tantek" rel="me">@t</a>`, while his GitHub profile would include `<a href="https://tantek.com/" rel="me">https://tantek.com/</a>`. This bi-directional connection confirms that both URL representations refer to the same individual, facilitating verified site linking and authentication processes.

The attribute's functionality operates through reciprocal connections, where a user's website contains a rel="me" link to their third-party site profile. When this reciprocal connection is detected, domain verification succeeds, indicating that the user controls the personal website sufficient to establish a link back to their third-party profile. This process combines domain verification with OAuth authorization mechanisms supported by third-party services, creating a robust framework for digital identity verification and social authentication.


## Evolution of the rel Attribute

The `rel` attribute in HTML evolved through several stages, expanding from basic document navigation to support complex relationship definitions between resources. In its early incarnation with HTML 2.0, the attribute facilitated linking stylesheets and document navigation elements like `rel="next"` and `rel="prev"`.

The 1999 release of HTML 4.01 introduced significant enhancements, including `rel="alternate"` for alternate document versions and `rel="author"` and `rel="help"` for defining relationships with author information and support materials. This period also marked the foundation of modern `rel` functionality through XML-based syntax in XHTML.

The 2000s saw continued evolution with the introduction of `rel="canonical"` for managing duplicate content and `rel="nofollow"` to combat spam through link manipulation. Microformats further developed the attribute's capabilities in 2005-2010 with `rel="me"` for web identity verification and `rel="tag"` for content categorization.

HTML5 expanded the `rel` attribute's scope through new tags like `<a>`, `<link>`, `<form>`, and `<area>`, while adding critical security features such as `rel="noopener"` and `rel="noreferrer"`. The latest developments include resource optimization tools like `rel="preload"`, `rel="prefetch"`, and `rel="dns-prefetch"`, along with modern icon management through `rel="icon"` and specialized mobile optimization through `rel="apple-touch-icon"`.

Throughout its history, the `rel` attribute has maintained a robust framework for defining document relationships, continuously adapting to meet the evolving needs of web development and digital communication.


## Technical Implementation

In the anchor and link elements, the `rel` attribute defines the relationship between the current document and the linked resource, allowing for semantic connections that provide context for how the linked content interacts with the current document.


### `<a>` Element Usage

For the `<a>` element, the `rel` attribute most commonly indicates alternative document representations when paired with the `alternate` keyword, provides a link to the document's author using the `author` keyword, or indicates a help document using the `help` keyword. The attribute can also be used to flag external links (not part of the same site) or specify that the link should not be followed (using `nofollow`).


### `<link>` Element Usage

The `<link>` element employs the `rel` attribute in several ways:

- `alternate` provides an alternate representation of the current document, supporting translations and different document formats.

- `canonical` defines the preferred URL for the current document, helping search engines manage duplicate content.

- `stylesheet` indicates an external stylesheet to be applied to the document.

- `icon` specifies the icon resource for the page, typically used for bookmarking and website identification.


### Implementation in Web Development

Web developers implement rel=me through reciprocal connections between a user's website and their third-party profiles. For example, Tantek's home page might contain a simplified hyperlink `<a href="https://github.com/tantek" rel="me">@t</a>`, while his GitHub profile would include `<a href="https://tantek.com/" rel="me">https://tantek.com/</a>`. This bi-directional connection confirms that both URL representations refer to the same individual, facilitating verified site linking and authentication processes.


### Technical Considerations

When implementing `rel` attributes, developers must ensure that:

- The attribute follows the IANA registry for valid values.

- All values are space-separated and unique.

- The attribute provides meaningful relationships that enhance document discoverability and accessibility.


## Social Media Integration

The `rel="me"` attribute's social media integration spans multiple platforms, with notable implementations by Mastodon, GitHub, and WordPress. As reported in the Microformats Wiki, Mastodon supports the `<link rel="me" href="...">` tag, recommending integration through custom `main.html` overrides in MkDocs Material (commit `3fc8b6b`), which automatically adds the attribute to social links using Mastodon icons.

The attribute plays a crucial role in verified site connections, where platforms like GitHub and WordPress enable users to link their personal websites with third-party profiles. For WordPress, the implementation involves adding a new social link through the links page, where users can customize the `rel` attribute to include `me`, as demonstrated in the provided configuration examples.

The attribute's evolution has seen increasing adoption across social media platforms. According to documentation from 2019, IndieLogin has implemented a comprehensive rel-me solution that supports both RelMeAuth and web-sign-in, focusing particularly on independent website verification. This implementation combines traditional domain verification with OAuth authorization mechanisms, providing a robust framework for digital identity verification across social networks.

Current standards continue to expand the attribute's functionality. Recent developments include enhanced verification processes and improved integration with existing social features. The latest implementation from GitHub demonstrates how the attribute can be used to verify user authenticity, while the Mastodon example shows how platform-specific standards can be adapted for broader web identity verification. These advancements underscore the attribute's growing importance in social media integration and digital identity verification processes.


## Best Practices

Web developers should implement rel=me for profile linking, establishing clear connections between a user's website and their third-party profiles. Content creators must ensure reciprocal rel=me connections to enable proper identity verification across platforms.

To implement rel=me effectively, web developers should follow these best practices:

1. Use reciprocal connections: The attribute's functionality operates through bidirectional links, where a user's website contains a rel="me" link to their third-party site profile. This confirms that both URL representations refer to the same individual.

2. Ensure valid content: The rel attribute value must be an unordered set of unique, space-separated keywords. All values must adhere to the IANA registry for valid link relations.

3. Implement across elements: The attribute can be used in anchor (`<a>`) and link (`<link>`) tags to establish relationships between documents. For example, Tantek's home page might contain a simplified hyperlink `<a href="https://github.com/tantek" rel="me">@t</a>`, while his GitHub profile would include `<a href="https://tantek.com/" rel="me">https://tantek.com/</a>`.

4. Verify reciprocal relationships: Platforms like Mastodon, GitHub, and WordPress require reciprocal rel=me connections for successful domain verification. This process combines traditional domain verification with OAuth authorization mechanisms supported by third-party services.

5. Follow implementation guidelines: Developers should refer to official documentation and platform-specific guidelines for implementing rel=me. For WordPress, this involves adding a new social link through the links page and configuring the rel attribute to include "me".

6. Monitor implementation effectiveness: Regularly review rel=me connections to ensure their continued effectiveness. This includes verifying reciprocal relationships and checking for any platform-specific implementation requirements.

## References

- [HTML br The Line Break Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20br%20The%20Line%20Break%20Element.md)
- [HTML Alternate Stylesheet](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Alternate%20Stylesheet.md)
- [HTML sub The Subscript Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20sub%20The%20Subscript%20Element.md)
- [HTML Using Microformats In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Using%20Microformats%20In%20HTML.md)
- [HTML The Content Span Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Content%20Span%20Element.md)