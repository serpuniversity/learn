---

title: HTML Ruby Text Container (RTC) Element

date: 2025-05-29

---


# HTML Ruby Text Container (RTC) Element

The HTML RTC element serves a specialized purpose in East Asian typography, providing a robust framework for annotating Chinese and Japanese logographic languages. Through its interaction with other ruby-related elements, this container enables intricate text annotations while maintaining compatibility with standard HTML attributes and global elements. Understanding the RTC element's structure, attributes, and rendering capabilities is essential for developers working with complex text presentations that require precise semantic annotation.


## Definition and Purpose

The RTC element is a specialized container in HTML typography designed for East Asian character annotations. Specifically, it is used to provide pronunciation or semantic information for Chinese and Japanese logographic languages, where small annotations above or to the right of characters offer crucial linguistic guidance.

In the context of HTML typographic annotations, the RTC element serves as a precise container for ruby text components within a ruby annotation. This structure is part of a larger framework for East Asian typography that uses small, auxiliary text to enhance character comprehension. The element's primary function is to associate specific ruby components with the base text they annotate, playing a vital role in the visual and semantic organization of complex textual presentations.

The element's content model allows for flexible annotation structures. While it primarily contains `rt` elements, it can also be immediately followed by `rb`, `rtc`, or `rt` tags, enabling complex ruby markup as defined in XHTML standards. This capability supports multiple annotation layers and types, with each `rtc` element potentially defining two distinct text associations for a given base element.

From a semantic perspective, the RTC element follows standard HTML5 design patterns while maintaining specific typographic roles. It supports core attributes and global HTML attributes, though its primary role is semantic annotation rather than interactive functionality. For advanced annotation needs, it leverages existing typographic elements like `rb` and `rt`, integrating seamlessly with existing HTML text structures while extending their capabilities for complex text rendering.


## Structure and Parent-Child Relationships

The `rtc` element functions as a specialized container for ruby text within a ruby annotation, specifically designed for East Asian typography. This structure is used to provide pronunciation or semantic annotations for Chinese and Japanese logographic languages, where small auxiliary text is placed above or to the right of characters to enhance comprehension.

Each `rtc` element must be contained within a `ruby` element and may contain `rt` elements or be immediately followed by `rb`, `rtc`, or `rt` tags. This structure enables the definition of two distinct text associations for a given base element, supporting complex ruby markup as defined in XHTML standards.


## Attributes and Support

The RTC element supports a wide range of standard HTML attributes, including accesskey, autocapitalize, class, contenteditable, and others. These attributes enable enhanced accessibility, styling, and user interaction capabilities for ruby text containers.

Common attributes include:

- class: The class attribute consists of space-separated tokens representing the element's classes. Class values should describe content nature rather than presentation.

- id: The id attribute must be unique within the element's tree, contain at least one character, and not include ASCII whitespace.

- slot: Assigns elements to shadow tree slots, matching the slot element's name attribute value.

RTC elements also support 24 event handler content attributes, with asterisked attributes having different meanings on body. These events enable interactive functionality while maintaining the element's core text container role.

The attribute support across major browsers varies, with full compatibility in Firefox 1+, Safari 3+, Chrome 1+, Edge 79+, and others. Some attributes, like autocomplete and various form-related attributes, have limited browser support but enable important user interaction capabilities.


### IDL and Attribute Behavior

The RTC element's IDL attributes mirror content attributes:

- action: Reflects content attribute, returning the node document's URL if content is missing or empty

- target: Reflects content attribute

- method & enctype: Reflect content attributes, with limited value support

- encoding: Reflects enctype content attribute

- noValidate: Reflects novalidate content attribute

- formAction: Reflects formaction content attribute, returning the node document's URL if content is missing or empty

- formEnctype: Reflects formenctype content attribute, with limited value support

- formMethod: Reflects formmethod content attribute

- formNoValidate: Reflects formnovalidate content attribute

- formTarget: Reflects formtarget content attribute

The autocomplete attribute supports values across multiple browsers, allowing developers to control form field value assistance and field type guidance. In contrast, some experimental attributes like dirName and readOnly have limited browser support but enable additional functionality.


## Rendering and Layout

The rtc element defines how annotations are rendered relative to their base text, particularly in complex ruby markup structures. Each rtc element can contain up to two text associations for a given base element, allowing for more sophisticated annotation patterns.

In simpler ruby structures, the rtc element functions similarly to rb and rt elements, containing either the base text or the corresponding ruby text. However, complex ruby markup requires the use of both rbc (ruby base container) and rtc elements. Each rbc element contains rb elements, which are paired with their respective rt elements within the corresponding rtc element.

The rtc element's content model consists of phrasing content with no ruby elements and no ruby descendants, allowing it to contain rt elements or be immediately followed by rb, rtc, or rt tags. This structure enables multiple levels of annotation and complex ruby markup patterns.

When rendering ruby text, the rtc element influences placement based on writing direction and typographic context. In horizontal layout, ruby text typically appears above the base text, while vertical layouts position ruby text to the right of the vertical line. The font size of ruby text is usually about half that of the base text.

The rtc element plays a crucial role in browser compatibility, with proper rendering behavior defined for both legacy and conforming user agents. For multiple annotations, the rtc element allows the use of rp elements to separate annotations, while also supporting data elements for machine-readable content representation.


## Usage Requirements

RTC elements must be used within `<ruby>` tags and adhere to specific syntax rules for opening and closing tags. Here are the key requirements for using RTC elements:


### Syntax and Formatting

The text content within an RTC element must not contain the less-than sign (U+003C) or an ambiguous ampersand (&). The element's structure follows the HTML syntax rules for start tags:

1. Begins with U+003C LESS-THAN SIGN character (<)

2. Followed by the element's tag name

3. One or more [ASCII whitespace] characters

4. Attributes, separated by [ASCII whitespace]

5. One or more [ASCII whitespace] characters

6. Optional U+002F SOLIDUS character for void elements or foreign elements marked as self-closing

7. Closed by U+003E GREATER-THAN SIGN character (>)


### Content Structure

The content model consists of phrasing content with no ruby elements and no ruby descendants. This allows RTC elements to contain rt elements or be immediately followed by rb, rtc, or rt tags. The element can be self-closing if it immediately precedes another ruby-related element.


### Parent and Child Relationships

RTC elements must be contained within `<ruby>` elements. They can be used to contain rt elements or be immediately followed by rb, rtc, or rt tags, enabling complex ruby markup patterns. Each RTC element can contain up to two text associations for a given base element.


### Closing Tag Requirements

The closing tag can be omitted if the element is immediately followed by an rb, rtc, or rt element opening tag or the parent closing tag. This flexibility allows for compact ruby markup while maintaining semantic clarity.


### Permitted Attributes

RTC elements support all standard HTML global attributes, including accesskey, autocapitalize, class, contenteditable, and others. These attributes enable enhanced accessibility, styling, and user interaction capabilities while maintaining the element's core text container role.

By following these usage requirements, developers can effectively use RTC elements to create complex ruby annotations while ensuring compatibility with various browser implementations and maintaining proper HTML syntax.

