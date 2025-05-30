---

title: HTML `<rt>`: The Ruby Text Element

date: 2025-05-29

---


# HTML `<rt>`: The Ruby Text Element

The `<rt>` element represents one of the essential components of HTML's ruby annotation system, specifically tailored for enhancing the presentation and accessibility of East Asian typography. While its technical implementation builds upon foundational browser support dating back to Internet Explorer 5, the element's proper usage requires an understanding of its relationship with the surrounding `<ruby>` structure and supporting `<rp>` fallback mechanisms. Through carefully managing its content model and leveraging global attributes, developers can create accessible pronunciation guides and translation aids that maintain consistent presentation across modern and legacy browser implementations.


## Definition and Usage

The `<rt>` element is specifically designed to provide pronunciation, translation, or transliteration information for East Asian typography. It must always be contained within a `<ruby>` element and represents phrasing content, though it can optionally omit its end tag under certain conditions.

According to the HTML specification, `<rt>` supports global attributes only and falls under flow content, phrasing content, and palpable content categories. The technical interface for the element is defined as HTMLElement.

When used within a `<ruby>` element structure, `<rt>` doesn't represent anything on its own. Instead, it's used by the `<ruby>` element to determine its representation. For browsers that don't support ruby annotations, the `<rt>` element provides fallback pronunciation information through the `<rp>` element, which typically displays the pronunciation text in parentheses after the base text.

The element has been widely implemented across browsers since July 2015, with complete support in major engine versions. Current browser support includes Chrome 5.0, Edge 5.5, Firefox 38.0, Safari 5.0, and Opera 15.0. The implementation is based on Internet Explorer's support, which has been present since version 5, approximately three years before the 2001 W3C Ruby Annotation specification.

The `<rt>` element's role in East Asian typography is to provide small annotations rendered above, below, or next to base text. This functionality has been available for 11 years across various implementations, including use cases in textbook adaptations for different Chinese languages, Hokkien, and Mandarin. It's also utilized in Ministry of Education textbooks from Taiwan and as a learning tool for Hindi language acquisition.


## Basic Syntax and Structure

The `<rt>` element functions as a container for ruby text, which is additional information about the base text that appears in a `<ruby>` element. This text can provide pronunciation, translation, or transliteration information, particularly for characters in Chinese, Japanese, and Korean languages.

The element's content consists purely of phrasing content and support global attributes only. It falls under flow content, phrasing content, and palpable content categories in the HTML structure. The `<rt>` element requires a start tag but can omit its end tag under specific conditions - when immediately followed by another `<rt>` or `<rp>` element, or when no more content follows in the parent element.

Browser compatibility extends back to Internet Explorer 5, which introduced the element three years before the 2001 W3C Ruby Annotation specification. Current implementation covers major browsers, including Chrome 5.0, Edge 5.5, Firefox 38.0, Safari 5.0, and Opera 15.0, with the technology based on reverse-engineering Internet Explorer's implementation. The element's rendering typically displays ruby text above base text in horizontal text and to the right in vertical text, though browsers without `<ruby>` support display ruby text inline after the base text. Modern implementations style ruby text with default settings of line-height: normal, though developers can override these through CSS.


## Rendering and Browser Support

The default rendering of ruby text displays it above base text in horizontal text and to the right in vertical text. However, browsers that don't support ruby annotations display the ruby text inline after the base text, using {display: none;} to hide this content in supported browsers. Internet Explorer has been supporting `<ruby>` since version 5, which introduced the technology three years before the 2001 W3C Ruby Annotation specification.

Browser compatibility extends across multiple platforms, with verified support in Webkit since the start of 2010, Chrome, Firefox 38+, Safari 5+, Chrome, Opera 79+, and Edge 12+ (Internet Explorer 5+). The element uses the `HTMLElement` interface and supports all global attributes, falling under flow content, phrasing content, and palpable content categories.


### Display Variations

When not supported, browsers render ruby text in parentheses immediately following base text. This fallback mechanism is controlled through the `<rp>` element, which provides alternative content for browsers that don't understand `<ruby>`. Current implementation allows all major browsers to display ruby text according to these standards, with specific styling controlled through CSS properties like line-height: normal.


## Example Usage

While the base text of a `<ruby>` element typically appears as normal inline text, several mechanisms ensure proper rendering across different browser implementations and languages. The `<rp>` element provides essential fallback support, displaying alternative content for browsers that don't understand `<ruby>` annotations. For example, `<rp>` might be used to enclose `<rt>` elements that contain annotation text, ensuring compatibility across various browser versions and platforms.

The `<ruby>` element structure consists of two main components: the base text and the ruby text. These can be used to display both single characters and entire words, providing comprehensive support for multiple languages and character sets. For instance, a `<ruby>` tag can accommodate multiple `<rt>` elements to break down compound characters or phrases, allowing for detailed pronunciation guides that span multiple syllables or words.

In practice, developers can implement `<ruby>` elements with minimal complexity, requiring only basic HTML syntax and some simple CSS styling. By including `<rp>` elements that provide alternative content for unsupported browsers, developers ensure broad compatibility while leveraging modern typographic features for East Asian text. The flexibility of the `<ruby>` structure allows for both single-character annotations and multi-syllable guides, making it a versatile tool for enhancing text accessibility and clarity.


## Technical Specifications

The `<rt>` element is defined within the HTMLElement interface and supports all global attributes, making it a flexible component of HTML's text-level semantics. It consistently falls under the categories of flow content, phrasing content, and palpable content, providing clear guidance on its appropriate usage within structured documents.

Implementation across various environments ensures broad compatibility, with the element's support extending to all current engines including Firefox 1+, Safari 1+, Chrome 1+, Opera 8+, and Edge 79+. This widespread implementation reflects the element's fundamental role in enhancing text functionality for East Asian typography.

The element's content model strictly requires a start tag and allows for omitted end tags under specific conditions, either when immediately followed by another `<rt>` or `<rp>` element, or when no additional content follows in the parent element. This design mirrors broader HTML principles for managing structural and phrasing content effectively.

