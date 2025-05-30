---

title: The `<fencedframe>` Element: Privacy-Powered Document Embedding

date: 2025-05-29

---


# The `<fencedframe>` Element: Privacy-Powered Document Embedding

In recent years, web developers and privacy advocates have increasingly demanded more robust tools for embedding and displaying content from other sites while preserving user privacy. The `<fencedframe>` element represents an experimental improvement over traditional `<iframe>` tags, offering enhanced privacy controls through strict isolation of communication and data access. This article examines the technical specifications, browser requirements, and privacy features of the `<fencedframe>` element, highlighting its role in modern web development and privacy protection.


## Privacy-Powered Document Embedding

The `<fencedframe>` element represents a nested browsing context, embedding another HTML page into the current one. It closely resembles `<iframe>` elements in functionality but features enhanced privacy controls through isolation of communication and data access. Key distinguishing characteristics include restricted communication between the `<fencedframe>` content and its embedding site, controlled cross-site data access, and scripting limitations that prevent manipulation or direct data access via standard scripting methods.


### Technical Specifications

The element supports flow content, phrasing content, embedded content, interactive content, and palpable content categories. Both the starting and ending tags are required, and it accepts no permitted content. The `<fencedframe>` element has global attributes and experimental attributes including `allow`, which specifies a Permissions Policy for the element's content based on the request origin, and `height` and `width`, which control the element's visual size.


### Browser Integration and Requirements

Browser implementation requires handling of specific events including fencedtree click, defined through asynchronous document notification processes. Content Security Policy (CSP) restrictions apply, limiting navigation influences to protocol scheme values "https:", "https://*:*", and "*". Each `<fencedframe>` operates within an isolated JavaScript environment, unable to access the embedding context's DOM or have its own DOM accessed by the embedding context.

The element enables communication through controlled mechanisms, including attributes that define available features based on request origin. Experimental attributes and configurations allow for future control over feature availability through the allow attribute, currently managing camera and geolocation permissions. The element's visual properties are configured using the object-position property for positioning and contentWidth/contentHeight properties of the config object to define embedded document size constraints.


### Privacy-Sandbox Integration

The Fenced Frame element plays a crucial role in Privacy Sandbox initiatives, particularly with its integration with Protected Audience and Shared Storage APIs. It operates independently as a tree structure with either a root fenced frame or child iframes, allowing internal communication similar to typical iframes while maintaining strict isolation from external contexts. The element prevents third-party cookie reliance and other privacy risks associated with traditional iframes, though it still allows limited functionality through specific APIs and permissions policies.


## Technical Specifications

The fenced frame enforces a strict boundary between the embedding page and the cross-site embedded document, preventing any communication between the two unless explicitly allowed through specific APIs. This isolation prevents the joining of user data from both contexts, a common vulnerability in traditional iframes.

The element operates based on a configuration object model, with attributes managed through a custom mechanism rather than traditional URL and src attributes. Content categories include flow content, phrasing content, embedded content, interactive content, and palpable content, supporting a wide range of document types while maintaining strict isolation protocols.

The element requires both starting and ending tags, supporting global attributes and experimental attributes including allow, height, and width. The allow attribute specifies a Permissions Policy for the element's content based on request origin, currently managing camera and geolocation permissions. The height and width attributes control the element's visual size through experimental parameters, with default values of 150 and 300 pixels respectively.

Browser implementation requires handling specific events including fencedtree click, with asynchronous document notification processes for communication. Content Security Policy restrictions limit navigation influence to protocol schemes "https:", "https://*:*", and "*", ensuring secure content integration while maintaining isolation between embedding and embedded contexts.


## Browser Compatibility and Integration

The `<fencedframe>` element requires specific browser implementations to handle events such as fencedtree click through asynchronous document notification processes. Browser compatibility remains limited, with detailed specifications documented in the HTML specification and browser compatibility sections of relevant resources.

The element functions based on the HTMLFencedFrameElement interface, providing configuration properties including allow, config, height, and width. Content model categories support flow content, phrasing content, embedded content, interactive content, and palpable content, enabling a wide range of document types while maintaining strict isolation protocols.

The element operates through both the Window and Document interfaces, requiring modifications to browsing context creation and policy container inheritance. Nesting mechanisms include traversable and navigable contexts, with special handling for page visibility and event dispatching, particularly through the fencedtreeclick event handler.

Browser compatibility constraints require specific HTTP response headers including the Supports-Loading-Mode header for navigation control. Future developments aim to expand feature control through the allow attribute while maintaining strict privacy boundaries defined by the Privacy Sandbox initiative.


## Privacy-Sandbox Integration

The Fenced Frame element operates as a core component of the Privacy Sandbox, particularly in its integration with the Protected Audience and Shared Storage APIs. These elements represent a significant evolution in web privacy, addressing fundamental challenges in cross-site tracking and data isolation.


### Storage Partitioning

The element introduces robust storage partitioning, ensuring that cross-site iframes no longer share storage. For example, a domain `shoes.example` will no longer be able to access information stored by an iframe from a different origin. The system applies these partitioning rules to LocalStorage, IndexedDB, and cookies, significantly reducing information leakage across first-party storage contexts.


### Cross-Site Data Handling

The Fenced Frame element enables secure access to unpartitioned cross-site data through the Shared Storage API while maintaining strict isolation between the embedded content and its hosting environment. This architecture allows publishers to display targeted advertisements based on user interests registered through interest groups, without exposing sensitive information about the user's interests to either the publisher or the ad-serving environment.


### Privacy-Sandbox Features

The element supports multiple privacy sandbox features through its configuration mechanism. These include Protected Audience API capabilities for interest-based ad serving, attribution-reporting functionality, private-aggregation capabilities, and shared-storage operations. The system ensures that these features operate within the strict confines of the isolation boundary, preventing any unauthorized data access or communication across partitioned contexts.


### Implementation Roadmap

Google's roadmap for the Fenced Frame element envisions full adoption closer to 2026, following the complete phase-out of third-party cookies in Chrome, anticipated for 2024. This phased approach allows the industry to transition to new realities while maintaining existing levels of privacy and security. The implementation details include strict enforcement of isolation boundaries through cryptographic mechanisms and controlled permission policies, ensuring that the transition to fenced frames maintains the highest standards of web privacy.


## Accessibility and Usability

The `<fencedframe>` element implements specific restrictions on focus movement across the boundary between embedded content and its host page. Standard web features controlled via Permissions Policy, including camera and geolocation, are entirely blocked within fenced frames. The element supports only a subset of features specifically enabled for fenced frames: Protected Audience API, attribution-reporting, private-aggregation, shared-storage, shared-storage-select-url, and Shared Storage API functionalities.

User navigation through the element operates under strict limitations, allowing only user-initiated actions like clicks or tabbing to traverse the content boundary. This design prevents potential information leakage through API calls while maintaining the accessibility of embedded content. Screen readers can leverage the title attribute to provide context about the embedded content, improving usability compared to elements lacking descriptive attributes.

To set content for a fencedframe, an API generates a FencedFrameConfig object, which is then applied to the element's config property. The element utilizes the object-position property for positioning adjustments and contentWidth/contentHeight properties from the config object to control visual size. These properties enable precise layout while maintaining the isolation boundary between the embedded content and host page.

## References

- [HTML Alternate Stylesheet](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Alternate%20Stylesheet.md)
- [HTML Define Terms With HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Define%20Terms%20With%20HTML.md)
- [HTML Attribute Reference](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Reference.md)
- [HTML The Date Time Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Date%20Time%20Element.md)
- [HTML s The Strikethrough Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20s%20The%20Strikethrough%20Element.md)