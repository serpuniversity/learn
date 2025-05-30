---

title: Prefetching Resources with HTML Link rel=prefetch

date: 2025-05-29

---


# Prefetching Resources with HTML Link rel=prefetch

Web developers constantly seek ways to improve user experience by reducing load times and ensuring smooth navigation between pages. One powerful tool in their arsenal is the HTML link rel=prefetch attribute, which instructs browsers to load resources in advance of when they're actually needed. This preloading mechanism can significantly reduce perceived latency, especially for applications with predictable navigation patterns or single-page applications where content often depends on previously loaded resources. In this article, we'll explore the fundamentals of using rel=prefetch, including how to implement it, when to use it most effectively, and how modern browsers handle these requests to ensure optimal performance for both developers and users.


## Prefetch Basics

The HTML link rel=prefetch attribute enables web developers to instruct browsers to load files that may be required later, such as after page interactions or when visitors navigate to another page. These "preloaded" resources improve user experience by ensuring new page content loads more quickly.

The basic structure of the link element requires an href attribute specifying the resource URL and an as attribute defining the resource type (script, style, font). For example:

`<link rel="prefetch" href="/css/styles.css" as="style">`

When the browser encounters a link element with rel=prefetch, it queues the request and sends it when the network is idle and the main page content has loaded. The browser prioritizes these requests at the lowest level, ensuring they do not compete with main content resources for bandwidth.

The tag structure also supports additional attributes to enhance functionality:

- `<link rel="prefetch" href="https://example.com/page2.html">`

- `<link rel="dns-prefetch" href="//example.com">`

- `<link rel="preconnect" href="https://example.com">`

These elements work together to optimize resource loading:

- dns-prefetch performs DNS lookups before they are needed

- preconnect establishes early connections to important third-party origins

- prefetch loads resources in advance based on predicted user navigation


## Tag Structure and Attributes

The `href` attribute is essential for specifying the exact URL of the resource to be prefetched. This attribute requires a valid URL that points to the desired file, such as a stylesheet, script, or image. The `as` attribute, which follows the `href`, indicates the type of resource being fetched and influences how the browser handles the request. Supported values for `as` include:

- `style` for CSS files

- `script` for JavaScript files

- `font` for font resources

- `image` for image files

- `document` for entire pages or documents

- `fetch` for XHR/fetch requests

The attribute values determine the browser's behavior, including which headers to send and how to handle caching. For example, when fetching a font, including the `crossorigin` attribute is essential to allow cross-origin access:

`<link rel="prefetch" href="/fonts/custom.woff2" as="font" crossorigin="anonymous" type="font/woff2">`


### Usage Considerations

The `href` and `as` attributes work together to control when and how resources are fetched. Using the correct combination ensures that the browser prioritizes requests appropriately and handles the resources according to their intended use. For example, prefetching a JavaScript file with high priority ensures it is available when needed:

`<link rel="preload" href="used-later.js" as="script" fetchpriority="high">`

This combination allows the browser to preload essential resources while prioritizing main content loading. Developers should carefully consider which resources to prefetch based on their site architecture and user navigation patterns.


## Performance Considerations

Browser implementations of prefetching prioritize these requests lower than main content resources, ensuring they do not compete for bandwidth during page loading. This strategy is designed to prevent performance degradation of existing content while still providing benefits for future user interactions.

Prefetch operation details show that browsers queue up all hints and request each resource when the network is idle, prioritizing these requests at the lowest level through headers like `Sec-Purpose: prefetch`. The request process includes standard HTTP headers such as `Accept`, which helps the browser match cached resources following navigation, though it also includes specific headers like `Sec-Fetch-Dest: empty` tailored for prefetch operations.

The browser's handling of prefetch requests includes detailed management of cache storage. Prefetched files are stored in the HTTP Cache if the resource is cacheable, with a standard caching duration of five minutes as demonstrated in implementation examples. This caching behavior is controlled by the server's Cache-Control headers, though certain directives like `no-cache` or `no-store` may block prefetching.


### Implementation Best Practices

For optimal performance, browsers should be informed of network and device conditions before implementing prefetching. Modern implementations recommend checking connection status and data usage settings before initiating prefetch requests. Accessibility and user consent are crucial, particularly for sites that prefetch large resources. Implementation guidelines suggest using JavaScript APIs to dynamically adjust prefetching behavior based on real-time network conditions and user intent.

The feature's effectiveness varies across different use cases. For websites with predictable navigation paths, implementing prefetch hints via `<link>` tags in the document head can significantly reduce load times for subsequent page visits. In single-page applications or complex navigation structures, combining prefetching with dynamic request generation based on user interaction patterns can further improve performance metrics like Time to Interactive and First Contentful Paint.

The browser's implementation of prefetching as a "low" priority fetch operation aligns with its design goals of optimizing future page loads without compromising current performance. Developers should therefore consider prefetching as a complementary strategy to preloading, focusing on assets critical for next user interactions while maintaining awareness of potential resource usage impacts.


## Supported Resources

Prefetched resources can be of several types, including scripts, stylesheets, fonts, and images. Each type requires specific handling to ensure efficient resource loading and caching. For instance, font resources require the `as="font"` attribute with appropriate cross-origin handling, as demonstrated in the example:

`<link rel="prefetch" href="/fonts/custom.woff2" as="font" crossorigin="anonymous" type="font/woff2">`

This configuration ensures that browsers treat font resources differently from other asset types, optimizing both download and rendering processes. The browser prioritizes these requests lower than main content resources, as indicated by the network request headers, which include `Sec-Purpose: prefetch`.

The caching behavior follows standard HTTP Cache rules, with prefetched files stored for up to five minutes as shown in implementation examples. However, server Cache-Control directives can influence this duration, and certain restrictive directives like `no-cache` or `no-store` may prevent successful prefetching.


### Specific Resource Handling

For scripts and stylesheets, the primary consideration is ensuring they are available when needed. Modern browsers automatically prioritize these resources, as demonstrated by improved Time to Interactive metrics when prefetching React for future navigations. This optimization reduces the initial load time for subsequent pages, making the overall browsing experience more responsive.

Images, particularly those referenced through CSS background properties, benefit significantly from prefetching. By treating images as dependent resources of prefetched stylesheets, browsers can eliminate network latency, reducing Largest Contentful Paint (LCP) times. This optimization technique is crucial for page performance, especially when LCP elements are complex image backgrounds.

The effectiveness of these optimizations varies based on implementation. For example, Netflix reported a 30% improvement in Time to Interactive by prefetching React for future navigations. However, developers must carefully consider resource volume to avoid overloading devices, particularly on networks with limited bandwidth.


## Browser Support and Limitations

Modern browsers support cache partitioning, which makes the rel="prefetch" attribute ineffective for resources intended for different top-level sites. For example, a prefetch link to "https://news.example/article" would not be accessible from "https://aggregator.example/". This limitation extends to cross-site navigation, where the main document's prefetching capabilities may be restricted.

The browser prioritizes prefetch resources at the lowest level, making them dependent on network availability and device conditions. While prefetching improves future page loads, modern implementations require developers to check connection status and data usage settings before initiating these requests. This ensures that additional resource requests do not impact current page performance.


### Technical Implementation

Prefetched resources are stored in the HTTP Cache when cacheable, with a standard caching duration of five minutes. Server Cache-Control directives significantly influence this duration, and restrictive directives like `no-cache` or `no-store` can prevent successful prefetching. The browser's implementation of prefetching as a "low" priority fetch operation aligns with its design goals of optimizing future page loads while maintaining current performance standards.

