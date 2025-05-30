---

title: Understanding HTML rel=noreferrer

date: 2025-05-29

---


# Understanding HTML rel=noreferrer

When you click a link on a website, that website typically receives information about where you came from - this is known as a "referral." Modern browsers provide several ways to control this behavior through link attributes. This article focuses on the `rel=noreferrer` attribute, which specifically prevents the browser from sending your originating page's URL to the linked page. We'll explore what this attribute does, how it works with other link attributes like `noopener`, and why you might want to use it. Along the way, we'll discuss its implications for website security, privacy, and analytics tracking.


## What is rel=noreferrer?

The rel='noreferrer' attribute instructs the browser not to send the URL of the current page to the linked page. This value is supported by major modern browsers including Chrome, Firefox, IE/Edge, Opera, and Safari (Chrome 6.0, Firefox 4.0, IE/Edge 12.0, Opera 11.1, Safari 5.0).

The attribute works to prevent a specific JavaScript exploit involving window.opener, which allowed the opened page to call back into the original page, potentially leading to security vulnerabilities. Modern browsers effectively prevent this exploit when the attribute is used.

When combined with the noopener attribute, the noreferrer attribute provides both security and privacy benefits. It prevents the target page from accessing the referring page's context and blocks referral information leakage. This ensures that when a user clicks a link with this attribute, the server of the target resource will not know where the visitor came from, making it difficult to track referral traffic in analytics tools.

WordPress automatically applies the rel=noopener noreferrer attribute to external links that open in new tabs, providing built-in protection. Website owners should check their platform's implementation and ensure the attribute is properly applied where needed. While the attribute has no direct impact on SEO, it can make it harder to track referral traffic in analytics tools, particularly for sensitive websites where detailed traffic analysis is not essential.


## How does it work with other rel attributes?

When combined with the `noopener` attribute, `noreferrer` provides both security and privacy benefits. The `noopener` attribute prevents newly opened tabs or windows from controlling the original page, safeguarding users from potential exploits. This is achieved by setting `null` on the `Window.opener` property of the external site's window, while still allowing some cross-domain restrictions.

The `noreferrer` attribute instructs the browser to remove the Referer HTTP header and any information related to the referring website or origin when navigating to an external site link. Together, these attributes prevent the target page from accessing the referring page's context and block referral information leakage. This results in traffic appearing as direct traffic rather than referral traffic in Google Analytics, making it harder to track referral sources while maintaining privacy.

WordPress automatically applies the `noopener noreferrer` attribute to external links that open in new tabs, providing built-in protection. Website owners should verify this implementation and ensure proper security by checking their platform's settings and adding the attribute where needed. While generally recommended for external links, exceptions exist: trusted websites require no tag, and internal links do not need these attributes. The combination of `noopener` and `noreferrer` is particularly important for server-side work and Node.js applications, according to best practices from GitHub's nodebestpractices repository and Helmet.js documentation.


## Best practices for implementation

WordPress implements these attributes automatically for external links opening in new tabs, providing built-in protection. Website owners should verify this implementation and ensure proper security by checking their platform settings and adding the attribute where needed.


### Link Security and Website Protection

The "noopener" attribute prevents the linked page from accessing your site's window.opener property, effectively protecting against potential manipulation by untrusted affiliate partners or unknown websites. To verify that these attributes are applied, website owners can use browser developer tools to inspect page elements or search for "noopener noreferrer" in the WordPress code editor.


### Special Considerations

While the "noopener noreferrer" tag generally provides adequate protection for external links, additional precautions may be necessary for specific use cases. When using affiliate links, it's crucial to maintain both security and tracking functionality, as these links often provide valuable revenue. To achieve this, website owners can use UTM parameters alongside the "noreferrer" attribute to preserve campaign tracking details while prioritizing security.


### Implementation Best Practices

For websites allowing user-generated content, automatically applying these security attributes to external links can help prevent malicious actors from inserting harmful links. Many website platforms, including popular platforms like WordPress, automatically enforce these security layers to protect both the website and its visitors. Website owners should check their platform settings and use appropriate tools or plugins to ensure consistent application of these security measures.


## SEO and analytics considerations

The "noreferrer" attribute does not directly affect SEO, according to the What is Noreferrer? documentation, which states that links with "noreferrer" remain crawlable and pass link juice. This attribute primarily impacts how traffic is recorded in analytics tools, with modern browsers sending only domain-level referrer information by default.

The attribute's most significant SEO implication is the potential impact on referral tracking. As noted in the rel="noreferrer" documentation, the target website will see direct traffic rather than referral traffic data in Google Analytics. This masked referral data can affect analytics accuracy, particularly for websites that rely on detailed traffic segmentation.

Website owners should weigh this potential impact when implementing "noreferrer". For comparison, trusted websites or affiliate partnerships may require careful handling of referral data, while internal linking typically doesn't need these attributes. As the MDN documentation notes, the attribute is particularly useful for user-generated content, where malicious actors might insert harmful links - in these cases, the added security of "noreferrer" outweighs the tracking benefits.

The attribute's impact on SEO ranking is minimal, with rel="noreferrer" being considered a neutral factor. The W3Things documentation further clarifies that these attributes primarily affect how links are treated by search engines, with no direct penalty or benefit. Website owners should focus on maintaining proper link structure and content quality for SEO optimization.


## Security implications

When combined with the "noopener" attribute, the "noreferrer" attribute helps protect against security vulnerabilities such as reverse tabnapping. This exploit involves external sites modifying the original site with malicious code or redirecting to another site, which can occur when visitors navigate to new pages. The attribute blocks external sites from accessing the window.opener property, protecting against phishing attacks where visitors might unknowingly hand over login or credit card information.

The "noreferrer" attribute particularly addresses a specific JavaScript exploit that allows the opened page to call back into the original page via window.opener. For example, the JavaScript code "window.opener.location = 'http://gotcha.badstuff';" can be used to exploit this vulnerability. Modern browsers effectively prevent this exploit when the "noreferrer" attribute is used.

The attribute's security benefits extend beyond just protecting against reverse tabnapping. When combined with "noopener", it provides better protection for server-side work and Node.js applications. According to GitHub's nodebestpractices repository and Helmet.js documentation, these attributes together prevent newly opened tabs or windows from controlling the original page, safeguarding users from potential exploits and ensuring proper security practices.

WordPress, starting with version 5.1, automatically includes "noopener noreferrer" on all links set to open in new tabs, while Elementor's visual editor applies it automatically when users enable "Open in new tab" for links. This automated implementation ensures security for website owners without requiring technical expertise. However, it's important to understand the trade-offs: while these security measures protect against attacks, they can also affect how referral traffic is tracked in analytics tools.

