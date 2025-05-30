---

title: rel=prerender in HTML: Understanding the Specifications and Implementation

date: 2025-05-29

---


# rel=prerender in HTML: Understanding the Specifications and Implementation

Web performance optimization continues to evolve rapidly, with modern browsers introducing increasingly sophisticated techniques for resource preloading and page preparation. Among the most significant developments is the `rel="prerender"` attribute, designed to hint at potential navigation targets and initiate background preparation for faster subsequent page loads. This attribute has played a crucial role in early approaches to speculative resource loading, particularly in environments where complete page prerendering was feasible. However, its implementation has faced numerous challenges, leading to recent deprecation in favor of more flexible alternatives. This detailed exploration examines the technical specifications of `rel="prerender"`, its successful implementation in supporting browsers, and its relationship to modern preloading techniques like the Speculation Rules API. Through analysis of browser support, best practices, and real-world applications, we uncover the lessons behind this transition and its implications for future web performance optimization strategies.


## rel=prerender Overview

The `rel="prerender"` attribute was designed to allow web pages to hint to user agents that certain resources might be needed for the next navigation, enabling preemptive fetching and processing of these resources. Originally, this involved fetching subresources and performing background rendering to prepare for faster delivery of the targeted content when requested.

According to theWHATWG HTML Living Specification, when a page includes a `rel="prerender"` link, the user agent must implement the processing model described in Resource Hints. The browser attempts to establish a connection with the specified origin URL, using either preconnect (for HTTP) or preconnect+TCP+TLS (for HTTPS). The connection attempt is subject to resource constraints, allowing the user agent to perform a partial handshake (DNS only for HTTP, DNS or DNS+TCP for HTTPS) or skip the connection entirely.

The browser determines the optimal number of connections per origin based on negotiated protocol, current connectivity profile, available device resources, global connection limits, and other context-specific variables. User agents have discretion in implementing various prerendering strategies, including allocating fewer CPU, GPU, or memory resources, delaying some requests until the requested HTML resource is visible, and preventing prerendering when resources are limited.

Prerendering may be abandoned due to high cost or resource requirements, or due to the type or properties of the fetched content. The user agent may implement other strategies as well. When prerendering a document, the user agent must set the document property.

The attribute particularly excelled when handling complete page prerendering, as demonstrated by its successful implementation in Chrome and Internet Explorer. However, recent developments have led to its deprecation and replacement by more efficient techniques, such as the Speculation Rules API. This shift reflects ongoing efforts to optimize web performance while maintaining user-centric resource management.


## Browser Support and Current Status

Chrome and Internet Explorer were the only browsers to support `rel="prerender"` before its deprecation. In IE11, both prefetch and prerender functionalities were implemented, expanding compatibility in Microsoft's web browser.

The attribute's implementation has faced challenges, as evidenced by its inconsistent behavior across versions. For instance, when using JavaScript to replace an existing `link rel="prerender"` element's URL, Chrome's Task Manager consistently prerenders only the original URL rather than the updated one. This limitation affects dynamic navigation and content management systems that rely on frequent URL changes.

Modern browser development has shifted focus from the simple implementation of `rel="prerender"` to more sophisticated speculative loading techniques like the Speculation Rules API. While originally allowing manual configuration through the browser's dashboard settings, Netlify's Prerendering feature now operates in a BETA capacity, automating the process through dashboard settings and offering more refined control over the pre-rendering process.

The attribute's core functionality, fetching and processing target resources, remains relevant through newer techniques. Speculation Rules API, for example, allows controlled preloading based on specific URL patterns or CSS selectors, combining the direct action of `rel="prerender"` with more flexible JavaScript execution. This API approach enables developers to optimize resource loading without relying on the now-deprecated attribute.

Browser support for alternative preloading methods has expanded significantly past Chrome and IE's original implementation. The `rel="preload"` attribute, particularly, demonstrates broad compatibility, with modern browsers supporting early fetch requests for critical assets. While specific implementation details vary across versions and devices, the baseline functionality of `rel="preload"` has maintained consistent support since January 2021, offering developers a more widely compatible alternative to the now-deprecated `rel="prerender"`.


## Rel=prerender vs. Rel=prefetch

The `rel="prerender"` attribute and its companion `rel="prefetch"` attribute serve distinct purposes in web optimization, each designed to preemptively load resources to enhance subsequent user navigation.

`rel="prerender"` is specifically intended for full page prerendering - that is, fetching and processing a complete page that the user is likely to navigate to next. According to theWHATWG HTML Living Specification, browsers implement this functionality as a resource hint that triggers background fetching and rendering of the target document. However, it's important to note that the attribute has been deprecated and is now superseded by more advanced techniques like the Speculation Rules API.

In contrast, the `rel="prefetch"` attribute is used for fetching and caching resources that might be needed later. This includes scripts, stylesheets, and other assets that improve the user experience by reducing wait times for near-future resources. Modern browsers support `rel="prefetch"` more widely than `rel="prerender"`, including Chrome, Firefox, and Internet Explorer.

Both attributes offer specific advantages based on their intended use. `rel="prerender"` enables complete page optimization, making it particularly effective for complex applications where entire page contents need to be preloaded and rendered. `rel="prefetch"`, on the other hand, excels at optimizing individual resource loading, allowing developers to target specific assets for early fetching and caching.

Modern implementation best practices recommend using JavaScript to dynamically generate `link rel="prefetch"` and `link rel="prerender"` elements. This approach enables developers to trigger these hints based on user behavior, such as hovering over links or preparing content for intended clicks. By carefully managing the creation of these hints - including applying appropriate delays and managing duplicate requests - developers can optimize resource loading while avoiding unnecessary network usage.


## Prerendering in Action

The `<link rel="prerender" href="/path/to/next/page/">` approach allows developers to tell a web page to load and render a second page in the background, where the second page is highly likely to be visited next. This technique works best in multi-page registration processes where users typically visit pages in sequence. For example, in a registration flow, the current page might include the line `<link rel="prerender" href="/path/to/page-b/">`, instructing the browser to begin rendering the next page while the user fills out the current form.

Implementation follows these key steps:

1. Add the `<link>` tag with `rel="prerender"` to the `<head>` section of the current page, specifying the next page's URL.

2. Ensure the target page is "safe" - containing no dependencies on POST data from previous requests and not requiring interactive elements like Flash or specific JavaScript conditions.

3. Monitor browser behavior:

   - Chrome automatically handles prerendering based on speculative hints and user settings

   - For more control, implement speculation rules using JSON with `href_matches` and `selector_matches` conditions

   - Use the `Sec-Purpose` HTTP header to indicate page purpose: `prefetch;prerender`

The process provides several benefits:

- Nearly instant display of the second page when users click through

- Control over which page is loaded even if the user doesn't visit it

- Improved performance metrics like LCP (First Input Delay)

However, developers must also address potential challenges:

- Bandwidth usage: Prerendering downloads entire pages, which can cause resource waste, especially on mobile devices

- User experience: Pages load and render even if users don't request them

- Data consumption: Both server and user-side data usage may increase unnecessarily


## Best Practices for Dynamic Prerendering

Best practices for dynamic prerendering with JavaScript prioritize intelligent implementation to balance performance improvements with user experience and resource management.

JavaScript enables the dynamic creation of `<link rel="prefetch">` and `<link rel="prerender">` elements, allowing developers to trigger these hints based on user behavior. This approach, recommended in best practices, offers more flexibility than hard-coding in HTML, particularly for applications where precise timing and context are crucial.

For effective implementation, developers should:

1. Use JavaScript for prefetching and prerendering on probable clicks rather than applying these hints broadly across multiple pages.

2. Implement hover events to trigger actions, as demonstrated in the "Best-ish Practices for Dynamically Prefetching & Prerendering" guide that suggests considering implementation for pages with significant links.

3. Monitor browser behavior through available APIs, such as `document.prerendering` and `PerformanceNavigationTiming's activationStart` property, to confirm when prerendering begins and completes.

The JavaScript implementation may face limitations, particularly when handling multiple prerender hints. Official documentation indicates that browsers can only run a single prerender process per browser instance. To address this, developers must prevent subsequent prerendering attempts after the first has begun, as demonstrated in best practices implementations that limit the number of prerender processes based on hover counts.

While prerendering services like Prerender.io require Node.js and Express configuration, frameworks with native static site generation capabilities provide the most effective control over pre-rendering decisions. For optimal results, developers should combine these implementation options with careful monitoring of network and memory usage to ensure the technology enhances rather than degrades user experience.

## References

- [HTML id](https://github.com/serpuniversity/learn/blob/main/html/HTML%20id.md)
- [HTML Elements Reference](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Elements%20Reference.md)
- [HTML The Menu Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Menu%20Element.md)
- [HTML dir](https://github.com/serpuniversity/learn/blob/main/html/HTML%20dir.md)
- [HTML Guides](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Guides.md)