---

title: Using the HTML lang Attribute

date: 2025-05-29

---


# Using the HTML lang Attribute

The HTML lang attribute plays a crucial role in marking up web content with proper language identification, impacting everything from screen reader functionality to search engine optimization. This technical specification outlines the proper usage, implementation, and browser support for the lang attribute, while highlighting its importance in creating accessible and semantically structured web pages.


## Identifying Document Language

The HTML `lang` attribute serves as a crucial mechanism for identifying the language of text content on the web, affecting both screen reader functionality and search engine optimization. According to the documentation, the attribute must be applied to the `<html>` element to establish the primary language for the document, with common language codes including "en" for English, "es" for Spanish, and "fr" for French.

Within the document, language-specific content can be marked using the `lang` attribute on specific elements. For example, `<p lang="fr">`Sauf pour ce qui est écrit en mauvais français.`</p>` demonstrates how to designate French text within an otherwise English document. The attribute requires ISO language codes, with extended codes like "en-gb" for British English also being valid.

The attribute's importance extends to accessibility and text processing. Screen readers like VoiceOver on iOS automatically switch voices based on the language declaration, while tools like JAWS and NVDA load specific phonetic engines and dictionaries. This functionality impacts how browsers handle hyphenation, date formats, number input, spellcheck, and quote character formatting.

While the attribute is widely supported in modern browsers such as Chrome and Opera, it remains unsupported in Internet Explorer, Firefox, and Safari. Incorrect language declarations can lead to improper rendering of text elements, particularly regarding hyphenation and date formats. The attribute's effectiveness varies across different browser implementations and platforms, emphasizing the need for precise and consistent usage.


## Setting Primary Language

The `lang` attribute should be applied to the `<html>` element to establish the primary language for the document. The attribute value represents the language of the document, requiring ISO language codes such as "en" for English or "en-gb" for British English. For example, to set the primary language to British English, the attribute would be specified as follows: `<html lang="en-gb">`.

This attribute serves as the foundation for language identification in HTML, with extensions allowing for more specific language range declarations within the document. For instance, if a document contains multiple languages, the primary language should be set on the `<html>` element, while secondary languages can be declared using the lang attribute within specific elements. This structure allows for precise language identification while maintaining the document's primary language declaration.

The attribute's importance extends to both accessibility and technical functionality. Screen readers use the declaration to switch language profiles, ensuring correct accent and pronunciation. Modern browsers support the attribute across various platforms, with consistent implementation across Chrome, Edge, Firefox, Opera, and Safari. While the attribute's technical impact is broader than immediate visual changes, its correct implementation significantly enhances the document's accessibility and semantic structure.


## Language Range Declaration

The `lang` attribute can be used within specific elements to mark up content in different languages, providing precise control over language identification throughout a document. The attribute value, specified in the format [language]-[script]-[region] according to RFC 5646 (BCP 47), allows for detailed language tagging beyond basic language codes.

Elements may carry their own language specification using this global attribute. For instance, `<p lang="fr">`Ce texte est en français.`</p>` correctly marks French content within an English document. The attribute supports language range declarations, enabling precise control over text processing and styling.

In HTML 5, the `lang` attribute applies to any HTML element, extending its functionality beyond specific elements defined in HTML 4.1. Common language codes follow a two-letter format (e.g., "en" for English, "fr" for French), though extended codes like "en-gb" for British English also adhere to the valid language tag structure.

The attribute's impact extends to practical applications, allowing browsers and assistive technologies to process text correctly based on language specifications. While the exact processing differs across browsers and implementations, proper language declaration significantly enhances content accessibility and semantic structure.


## ISO Language Codes

The `lang` attribute requires ISO language codes to accurately identify the language of text content on a web page. According to the HTML specification, common codes include "en" for English, "es" for Spanish, and "fr" for French. The attribute must follow ISO 639-1 language codes, which provide standardized abbreviations for languages.

For HTML documents, the language should be declared as follows:

```html

<html lang="en">

```

In XHTML documents, the language is declared within the `<html>` tag with an additional namespace declaration:

```html

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">

```

The attribute is supported by all modern browsers, including Chrome, Edge, Firefox, Opera, and Safari. Its correct implementation significantly enhances content accessibility and semantic structure, though it primarily affects screen readers and search engines when used for text in different languages.

Valid ISO language codes include a wide range of languages, from Abkhazian (ab) to Zhuang (za), providing comprehensive coverage of global linguistic needs. The attribute's precision enables proper browser handling of text elements, ensuring correct hyphenation, date format processing, and quote character usage across different languages.


## Browser and Screen Reader Support

The `lang` attribute significantly influences how screen readers process content, with different readers implementing language switching in various ways. VoiceOver on iOS automatically switches voices based on language declarations, while JAWS and NVDA both load specific phonetic engines and dictionaries. This functionality impacts hyphenation, date format processing, number input, spellcheck, and quote character usage.

Browser support varies widely: Chrome and Opera fully support the attribute, while older browsers like Firefox, Internet Explorer, and Safari lack implementation. Hyphenation algorithms differ between languages, and correct declaration is crucial for proper text processing. Incorrect language declarations can lead to misaligned hyphenation patterns, incorrect date format rendering, and misinterpreted number input. The attribute's impact extends to modern web development practices, particularly in multilingual website construction and accessibility compliance.

## References

- [HTML The Button Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Button%20Element.md)
- [HTML Understanding Quirks And Standards Modes](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Understanding%20Quirks%20And%20Standards%20Modes.md)
- [HTML dir](https://github.com/serpuniversity/learn/blob/main/html/HTML%20dir.md)
- [HTML Microformats](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Microformats.md)
- [HTML Attribute Dirname](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Dirname.md)