---

title: HTML `<bdi>`: The Bidirectional Isolate element

date: 2025-05-29

---


# HTML `<bdi>`: The Bidirectional Isolate element

HTML's `<bdi>` element provides a powerful tool for managing text directionality in web development, particularly for languages that require bidirectional text flow. This introduction will explore the functionality, implementation, and best practices of `<bdi>`, helping developers understand how to effectively use this often-overlooked HTML feature.


## Definition and Usage

The `<bdi>` element creates a bidirectional isolate, allowing text to maintain its intended directionality within a document. It is particularly useful for languages that require text to flow in multiple directions, such as Arabic and Hebrew.

The element functions by wrapping a span of text and instructing the bidirectional algorithm to treat the text in isolation from its surroundings. Text within `<bdi>` tags maintains its specified directionality without affecting or being affected by the directionality of surrounding text.


### Technical Implementation

To use the `<bdi>` element, the directionality must be explicitly set using the dir attribute, which accepts values of either 'ltr' (left-to-right) or 'rtl' (right-to-left). If directionality is unknown, such as when inserting user-generated content, `<bdi>` should be used instead of CSS's `unicode-bidi: isolate` property on a `<span>` or other text-formatting element.


### Browser Support

The element is widely supported across modern browsers, including Chrome, Firefox, Safari, and Microsoft Edge, with good support dating back to version 16 for Chrome and 10 for Firefox. As of the latest data, Safari does not support the element.


## Functionality

When the browser encounters `<bdi>` content, it applies the Unicode Bidirectional Algorithm (UBA), treating the text within it as an isolated unit. Latin characters are treated as left-to-right (LTR), while Arabic characters are treated as right-to-left (RTL). Other characters like spaces and punctuation are neutral and assume the directionality of their surrounding characters.

The element's directionality is determined by the first non-space, non-punctuation character encountered: LTR characters set it to LTR, while AL (Arabic-like) or R characters set it to RTL. In cases of ambiguity, the browser falls back to the element's existing directionality: if dir="auto", the user agent determines the correct direction based on the content. Known directionality-capable attributes include abbr, alt, content, label, placeholder, and title, with document.dir providing the overall document directionality.

The text renders correctly across modern browsers without additional styling, though developers should use it in conjunction with CSS for consistent display. To demonstrate, consider a simple paragraph structure: the first paragraph uses auto directionality, the second uses RTL, and the third uses LTR. The rendered result displays these paragraphs with appropriate alignment, while any usernames (like "Student" or "Teacher") are correctly flushed right with a preceding colon.


## Implementation

The directionality of text within a `<bdi>` element is determined by the value of its dir attribute, which can be set to either "ltr" (left-to-right) or "rtl" (right-to-left). When this attribute is not explicitly set, the element defaults to an "auto" directionality state, allowing the user agent to determine the correct direction based on the content of the `<bdi>`.

The determination of directionality follows specific rules based on Unicode bidirectional character types:

- Latin characters (L) are treated as left-to-right

- Arabic-like (AL) and right (R) characters are treated as right-to-left

- Neutral characters (such as spaces and punctuation) inherit directionality based on their surrounding characters

The element's behavior is distinct from other HTML elements in its handling of the dir attribute. While most elements inherit directionality from their parent elements, `<bdi>` employs a special "auto" state that prevents directionality inheritance. This ensures that text direction is determined solely by the content within the `<bdi>` element.

If directionality cannot be determined from the content (for example, when the text consists entirely of neutral characters), the element's direction defaults to "ltr". This behavior differs from other elements, which typically use null as their fallback directionality. The `<bdi>` element's directionality status is represented by the Document/dir property, which returns the element's dir attribute value and supports the ltr, rtl, and auto states.


## Accessibility and Best Practices

The `<bdi>` element requires careful consideration when implementing to ensure proper accessibility and semantic meaning. While the element enhances text directionality, its use should be complemented by appropriate CSS styling and combined with other relevant HTML attributes for optimal accessibility.


### Styling and Presentation

The element behaves as if ASCII whitespace is present, meaning it treats Latin characters as left-to-right (LTR) and Arabic characters as right-to-left (RTL). Text directionality is determined automatically based on the first non-space, non-punctuation character encountered. This behavior differs from `<span>` elements, which inherit directionality from their parent elements.


### Semantic Considerations

When using `<bdi>`, it's essential to combine it with other HTML attributes for full accessibility support. The dir attribute should be set to either "ltr" or "rtl" to explicitly determine text direction. For unknown directionality, such as when inserting user-generated content, `<bdi>` provides a more reliable solution than CSS's `unicode-bidi: isolate` property applied to a `<span>` or similar element.


### Browser Compatibility and Support

While widely supported across modern browsers, older versions may not fully implement the `<bdi>` element's functionality. Developers should ensure that their implementation accounts for potential differences in browser support. To improve accessibility, consider combining `<bdi>` with ARIA (Accessible Rich Internet Applications) attributes. While the `<bdi>` element itself doesn't provide additional semantics, ARIA attributes can enhance web page functionality for users with disabilities.


## Technical Specifications

The `<bdi>` element behaves as if ASCII whitespace is present when encountered by the parser, making Latin characters appear left-to-right (LTR) and Arabic characters right-to-left (RTL) by default. This behavior distinguishes it from `<span>` elements, which inherit directionality from parent elements.


### Content Classification

The element is classified as flow and phrasing content, meaning it can appear anywhere flow content is allowed and is used for presenting text information. Palpable content, a related category, indicates that the text creates visible changes in the document layout.


### HTML Interface

The `<bdi>` element follows the HTMLElement DOM interface, with support for all global attributes except the dir attribute, which always defaults to auto. This means the user agent determines directionality based on the content unless explicitly set to rtl or ltr.


### Directionality Handling

The element's directionality is controlled through the directionality (dir) attribute, which can be set to either rtl or ltr. When directionality is unknown or needs to be determined automatically, `<bdi>` is the recommended approach over CSS's unicode-bidi: isolate property applied to `<span>` or similar elements.


### Browser Support

The element requires both start and end tags and behaves distinctly from other HTML elements by never inheriting its dir attribute value from parent elements. While widely supported across modern browsers, older versions may exhibit different implementation details. The element's technical specifications indicate compatibility with various browser versions and operating systems, though specific browser support documentation is not provided.

