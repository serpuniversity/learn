---

title: HTML translate Attribute: Managing Content Translation

date: 2025-05-29

---


# HTML translate Attribute: Managing Content Translation

Content localization has become increasingly important in today's global digital landscape, and HTML provides several mechanisms to manage multilingual content. From translating page titles to managing form labels, developers need precise control over which text is translated and which remains in its original language. In this article, we'll explore the HTML translate attribute, a powerful tool for managing content translation. We'll examine how it works with parent-child elements, interacts with other HTML features, and remains supported by translation tools despite browser limitations. Through practical examples and implementation guidance, we'll help you use this attribute effectively in your multilingual web projects.


## Attribute Overview

The HTML translate attribute controls whether an element's content should be translated, supporting 'yes' for translation and 'no' to prevent translation. It applies universally across all HTML elements, enabling precise content management for localization and multilingual websites. The attribute works by defaulting to 'yes', allowing all text to be translated, while 'no' specifies content that must remain in its original language.

This attribute interacts with HTML's inheritance model, where parent elements can set translation defaults that child elements may override. For example, a `<div translate="no">` will apply the non-translating setting to all child elements unless explicitly overridden with `<p translate="yes">`. The attribute's impact extends to attribute values, though best practices recommend treating them as untranslatable, as they are part of page syntax rather than natural language content.

Developers should implement the translate attribute thoughtfully, particularly in complex documents. A single misapplied 'translate="no"' can block translation across numerous elements, while 'translate="yes"' in a parent element can make child elements translatable. The attribute works harmoniously with other HTML features, including the lang attribute, which sets language information for search engines and screen readers. To ensure browser compatibility and proper parsing, all HTML documents should begin with the doctype declaration, maintaining standards mode and enabling features like attribute inheritance and JavaScript functionality.


## Element Support

The translate attribute applies to all HTML elements, from headings and paragraphs to images and form controls. This universality makes it a powerful tool for content management in multilingual websites and applications.

In practice, developers apply this attribute to control which elements participate in automatic translation processes. For example, to prevent a specific paragraph from being translated while allowing surrounding text to be translated, they might write:

```html

<p translate="no">Don't translate this!</p>

<p>This can be translated to any language.</p>

```

The attribute's compatibility with existing HTML features enables sophisticated content management strategies. When combined with the lang attribute, developers can create documents that vary language content while maintaining consistent structural elements. For instance, an article might use:

```html

<p lang="en" translate="yes">This text will be translated to the page's language.</p>

<p lang="fr" translate="no">Cet article est exclusivement en français.</p>

```

This structure allows automatic translation systems to handle the English content while maintaining the French text in its original language, preventing potential translation errors or loss of cultural context.


## Implementation Examples

Parent elements set attributes that inherit to child elements unless explicitly overridden. For example, a `<div translate="no">` will apply the non-translating setting to all child elements unless explicitly overridden with `<p translate="yes">`. The attribute's behavior extends to attribute values, though best practices recommend treating them as untranslatable, as they are part of page syntax rather than natural language content.

The process of managing translation inheritance requires careful attention to attribute values. For instance, if a `<div>` contains multiple paragraphs, setting translate="no" on the `<div>` will prevent translation of all `<p>` elements within it. However, if a `<p>` element needs to be translated despite the parent setting, it should include translate="yes" explicitly. This inheritance model allows for flexible content management while maintaining consistent translation controls across document structures.


## Browser Support

The translate attribute is not supported by modern browsers, as documented in the HTML specification and detailed implementation guides. While the attribute remains useful for content management systems and localization tools, its lack of browser support affects practical implementation.

Browser compatibility testing reveals that the attribute is not recognized in any major browser version, including the latest releases from Chrome, Firefox, Safari, and Edge. This limitation impacts developers seeking to leverage the attribute for automated translation processes or multilingual content management.

However, the attribute continues to hold value for localization workflows through its integration with translation tools. According to official documentation, the attribute is respected by systems like Google Translate, Microsoft Translator, and Yandex Translate. This compatibility enables developers to create content that is selectively translated while maintaining precise control over which elements remain in their original language.

The attribute's usefulness extends to content management systems that process HTML documents. Despite browser limitations, tools that parse and manipulate HTML retain support for the translate attribute, allowing developers to mark content for translation while preserving specific elements as untranslated.

In practice, developers working with browsers that do not support the translate attribute can use alternative methods to achieve similar results. As documented in official resources, Google and Microsoft previously supported non-standard methods such as `class="notranslate"` and `style="notranslate"`. While these methods are not directly supported by the translate attribute, they demonstrate the ongoing importance of content control mechanisms in multilingual web development.

For developers working in environments where browser support is guaranteed, the translate attribute provides a robust framework for managing content translation. The attribute's detailed inheritance model and support for both attribute-level and child-element control enables sophisticated content management strategies that align with best practices for multilingual web development.


## Translation Workflows

Lokalise offers comprehensive tools for managing HTML translations, from project setup to file management and collaboration. After creating a project in Lokalise, users upload HTML files containing content to be translated. The platform automatically detects language but allows manual selection if necessary, with the `%LANG_ISO%` placeholder system for managing translations across multiple languages.

The translation process requires careful management of both content and structure. While the basic translation workflow is straightforward, longer HTML documents need thorough checking of all nodes to ensure accurate translation. Users can leverage the platform's AI-powered translation and quality assurance tools to enhance the process, though professional translator assistance may be needed due to HTML expertise requirements.

Project management features allow for efficient workflow, with translations separated into language-specific folders. Content appears in the browser interface, and untranslated values can be managed through various options, including export settings and string filtering. This structured approach ensures that all content elements, from page titles to image alt text, are properly translated and integrated back into the original HTML structure.

## References

- [HTML Attribute Reference](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Reference.md)
- [HTML Figcaption The Figure Caption Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Figcaption%20The%20Figure%20Caption%20Element.md)
- [HTML tr The Table row Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20tr%20The%20Table%20row%20Element.md)
- [HTML add Javascript To Your web Page](https://github.com/serpuniversity/learn/blob/main/html/HTML%20add%20Javascript%20To%20Your%20web%20Page.md)
- [HTML The Mark Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Mark%20Text%20Element.md)