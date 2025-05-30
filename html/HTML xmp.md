---

title: HTML `<xmp>` Tag

date: 2025-05-29

---


# HTML `<xmp>` Tag

When web developers need to display code snippets or debugging output exactly as written, the `<xmp>` tag provided a unique solution in HTML. This article explores the `<xmp>` tag's functionality, comparing it to similar elements like `<pre>` and `<code>`. While no longer supported in modern browsers, understanding this deprecated tag sheds light on the evolution of HTML's text formatting capabilities.


## Introduction to `<xmp>`

The `<xmp>` tag served a specific purpose in HTML, allowing developers to display preformatted text while preserving whitespace and original formatting. This functionality made it particularly useful for displaying code snippets and debugging output, where maintaining the exact structure and whitespace of the original text was essential.

According to the W3C's HTML 3.0 reference, the `<xmp>` tag was introduced in HTML 3.2 specifically for handling preformatted text. Its most distinctive feature was the ability to display content exactly as entered, without any automatic formatting changes—unlike the `<pre>` tag, which requires manual escaping of certain characters to prevent interpretation as markup.

The tag functioned by rendering text between its opening and closing tags without interpreting any HTML content within. While it shared similarities with `<pre>` in its basic functionality, `<xmp>` offered some unique advantages. For example, the MDN Web Docs note that `<xmp>` does not require escaping ampersands and less-than characters, making it slightly more convenient for basic code snippets compared to `<pre>`.

Implementing `<xmp>` was simple and syntactically similar to `<pre>`, using the exact text between the tags without modification. However, as noted in the HTML5 specification, its use is deprecated and it has no unique attributes other than supporting standard HTML global attributes.

The tag's most distinctive feature was its ability to preserve all whitespace characters and line breaks exactly as entered, making it particularly valuable for viewing HTML source code or debugging output. However, modern HTML guidelines strongly recommend avoiding `<xmp>` in favor of `<pre>` for preformatted text, as it conflicts with SGML standards and is no longer supported in current web development practices.


## Technical Specifications

The `<xmp>` tag syntax follows a simple structure consisting of an opening `<xmp>` tag, followed by the text content, and a closing `</xmp>` tag. This syntax allows developers to define blocks of text that retain their original formatting and whitespace, distinct from regular HTML content.

The tag supports all standard HTML global attributes, enabling developers to apply common element properties and styles. However, it possesses no unique attributes, maintaining a minimal feature set focused on its core functionality. This attributeless design aligns with its role as a straightforward text-rendering element.

When implementing `<xmp>` content, developers must properly escape certain characters to prevent unintended HTML interpretation. Specifically, all < characters must be replaced with &lt;, and & characters should be rendered as &. This escaping requirement differs from `<pre>` tags, which have more stringent character encoding demands.


## Use Cases and Features

The `<xmp>` tag rendered content exactly as typed, without interpreting any HTML elements between its opening and closing tags. This behavior differed from `<pre>` tags, which require escaping special characters like < and & to prevent browser interpretation.

While the HTML2 specification recommended rendering text wide enough for 80 characters per line, this guideline was not consistently implemented across browsers. The element's deprecation in HTML3.2 marked the beginning of its decline as a supported feature, though some browsers may still recognize it due to legacy compatibility reasons.

Modern alternatives include the `<pre>` element, which shares similar functionality for displaying preformatted text. For scenarios specifically requiring code representation, the `<code>` element provides semantic meaning while maintaining proper display characteristics. Both alternatives offer broader support and maintain compliance with current web development standards.


## Browser Support and Deprecation

The `<xmp>` tag's specifications left it unsupported in modern browsers, including Chrome, Edge, Firefox, IE, Opera, and Safari. Since its initial deprecation in HTML 3.2, no major browser has maintained compatibility with the tag, rendering it effectively obsolete for web development purposes.

As noted by the MDN Web Docs, the element's use conflicts with SGML standards, which fundamentally limits its applicability in current HTML implementations. While some older browsers might still recognize `<xmp>` due to legacy compatibility, developers should avoid using it entirely in favor of more compatible alternatives.

The recommended replacement for `<xmp>` functionality is the `<pre>` tag, which shares similar characteristics for displaying preformatted text. For scenarios specifically requiring code representation, the `<code>` element provides semantically appropriate HTML structure while maintaining proper display characteristics. These modern alternatives offer broader support and maintain compliance with current web development standards, making them preferable choices for displaying uninterpreted HTML content.


## Historical Context and Alternative Solutions

The `<xmp>` tag's historical significance lies in its ability to display text exactly as entered, without interpreting any HTML elements between its tags. Introduced in HTML 3.2, it filled a specific need for displaying preformatted text, especially in debugging scenarios. However, its implementation and support were inconsistent across browsers, and it was marked as obsolete in the HTML 3.0 reference dating back to August 1995.

The tag's most distinctive feature was its handling of whitespace and HTML content. Unlike the `<pre>` tag, `<xmp>` did not require escaping characters like < and &, making it easier for simple debugging purposes. This difference in implementation led to some browsers supporting `<xmp>` for debugging `var_dump()` output in PHP, while `<pre>` required more careful content handling.

Modern alternatives to `<xmp>` include the `<pre>` element, which shares similar functionality for displaying preformatted text. For scenarios specifically requiring code representation, the `<code>` element provides semantic meaning while maintaining proper display characteristics. These alternatives offer broader support and maintain compliance with current web development standards, making them preferable choices for displaying uninterpreted HTML content.

## References

- [HTML Microformats](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Microformats.md)
- [HTML Content Categories](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Content%20Categories.md)
- [HTML Colgroup The Table Column Group Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Colgroup%20The%20Table%20Column%20Group%20Element.md)
- [HTML Responsive Images](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Responsive%20Images.md)
- [HTML Nonce](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nonce.md)