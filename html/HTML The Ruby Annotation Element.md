---

title: The `<ruby>` HTML Element

date: 2025-05-29

---


# The `<ruby>` HTML Element

The `<ruby>` HTML element provides a versatile solution for adding annotations to text, particularly where pronunciation guidance or semantic clarification is needed. This introduction highlights the element's basic functionality, its support across modern browsers, and its applications in multiple languages and contexts.


## Overview of Ruby Annotations

The `<ruby>` element facilitates the addition of ruby annotations, which display additional information alongside base text. These annotations enhance understanding and pronunciation guidance, particularly for East Asian languages. However, their application extends beyond these linguistic contexts to provide semantic clarification or phonetic guidance in various languages and academic settings.

The basic structure of a ruby annotation consists of a `<ruby>` element containing the base text, with the annotation provided inside an `<rt>` element. This configuration produces the annotation above the base text when rendered. The `<ruby>` element also supports optional `<rp>` elements, which display parentheses around the annotation in browsers that do not fully support ruby annotations, ensuring consistent representation across different viewing environments.

The element's design allows for flexible annotation placement, with text rendering above, below, or to the right of the base text as appropriate. For vertical text, annotations typically appear to the right of the base text. This layout flexibility enables effective use cases across multiple languages, including Japanese (where annotations often appear on the opposite side of the base text), Chinese (for Pīnyīn annotations), Korean (for name transliteration), and Vietnamese (for tone indication).

The `<ruby>` element serves both phonetic guidance and semantic clarification, making it valuable for educational content, language learning resources, and academic literature. Its implementation works across modern browsers, with support dating back to 2015, though full compatibility varies between different browser versions and platforms.


## Basic Usage and Structure

The `<ruby>` element functions by surrounding base text that requires explanation or pronunciation guidance with an `<rt>` element containing the annotation. For example:

```html

<!DOCTYPE html>

<html>

<body>

<p>Google<ruby>Google<rt>Gō-google</rt></ruby> is a popular search engine.</p>

</body>

</html>

```

In this instance, "Google" appears with the annotation "Gō-google" displayed above it. When browser support is lacking, the optional `<rp>` element can be employed to present fallback content, typically in the form of parentheses:

```html

<p>GeeksforGeeks<ruby>GeeksforGeeks<rt>GeeksforGeeks</rt> <rp>(GeeksforGeeks)</rp></ruby></p>

```

The `<ruby>` element's basic structure requires both start and end tags, with phrasing content permitted between them. This structure allows for flexible annotation placement, with text rendering above, below, or to the right of the base text based on the text orientation:

```html

<p>Google<ruby>Google<rt>Google</rt> (Google)</ruby></p> <!-- Browsers with support -->

<p>Google<ruby>Google<rt>Google</rt> (Google)</ruby></p> <!-- Fallback rendering for unsupported browsers -->

```

The `<ruby>` element's implementation works across modern browsers, with support dating back to 2015. Its usage can be extended to various languages beyond East Asian contexts for pronunciation guidance or semantic clarification, demonstrating its versatility in multilingual web content.


## Rendering and Browser Support

The `<ruby>` element facilitates detailed text annotations through its combination with `<rt>` and `<rp>` elements. This enables comprehensive support across modern browsers, with compatibility dating back to 2015 when Chrome 5.0, Firefox 38.0, Edge 15.0, Safari 5.0, and Opera 5.5 introduced initial support.

The base structure consists of `<ruby>` tags containing both the text requiring explanation and the `<rt>` elements that provide the annotation. For browsers that do not support ruby annotations, the `<rp>` element displays fallback content, typically in parentheses. This ensures consistent representation across different viewing environments while maintaining accessibility.

The element's display capabilities vary based on text orientation, with annotations typically appearing above horizontal text and to the right of vertical text. This flexibility supports multiple language needs, including Japanese (where annotations often appear on the opposite side of the base text), Chinese (for Pīnyīn annotations), Korean (for name transliteration), and Vietnamese (for tone indication).

Browser compatibility extends across various devices and versions, though some older versions may not fully support CSS properties for text transformation. The element's global attributes enable semantic enrichment while maintaining compatibility with assistive technologies, as it does not correspond to a specific ARIA role.


## Advanced Usage and Applications

The `<ruby>` element's functionality extends beyond simple word-level annotations to support complex linguistic requirements. It allows dividing base text into smaller units, each with its own annotation, through a combination of `<ruby>`, `<rt>`, and `<rp>` elements.

For instance, the element supports phonetic guidance in multi-syllable Japanese kanji characters, where each syllable can be annotated separately. The structure for complex annotations includes multiple `<ruby>` elements within a parent container, each targeting specific parts of the base text. This capability enables detailed textual enrichment while maintaining semantic clarity.


### Multilingual Applications

Ruby annotations find application beyond East Asian languages, particularly in languages that require pronunciation guidance. For example, in Hebrew, while Unicode fonts provide built-in pronunciation marks, the `<ruby>` element can still be used for additional annotation. The element also supports English and European languages through semantic annotations, though its use in these contexts is less common due to the availability of alternative text-based solutions.


### Implementation Details

The basic structure of the `<ruby>` element remains consistent across complex annotations, with the start and end tags required for proper rendering. Each annotation unit follows the format `<ruby>base text<rt>annotation</rt></ruby>`, with multiple units combined as needed for complex text. For browsers without full `<ruby>` support, the `<rp>` element provides essential fallback functionality, indicating the presence of annotations through parentheses around the base text.


## Accessibility and Text Transformation

The `<ruby>` element enhances accessibility through its ability to provide clear pronunciation guidance for non-phonetic scripts. In languages like Chinese, Japanese, and Korean, where characters can have multiple pronunciations or meanings, the element allows authors to provide essential contextual information.

Developers achieve this by combining the `<ruby>` element with the `<rt>` element, which contains the annotation text. For browsers that do not support ruby annotations, the optional `<rp>` element provides fallback content - typically, parentheses around the base text - ensuring that the pronunciation or meaning information is still conveyed.

The element's global attributes ensure compatibility with assistive technologies while maintaining semantic meaning. Unlike some HTML elements that map to specific ARIA roles, `<ruby>` does not correspond to any particular role. This design choice prevents authors from misusing the element to represent other types of content, maintaining its specialized functionality for text annotation.

Accessibility improvements come through proper implementation of related CSS properties. While the `<ruby>` element itself doesn't have specific attributes, authors can use the `text-transform` property to adjust the visual presentation of annotated text. For example, `text-transform: full-size-kana` specifically targets Japanese text, improving presentation but requiring careful consideration of browser compatibility.

