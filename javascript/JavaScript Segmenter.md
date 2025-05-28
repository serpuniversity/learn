---

title: JavaScript Segmenter

date: 2025-05-27

---


# JavaScript Segmenter

JavaScript's core functionality encompasses a rich set of built-in objects that serve as fundamental building blocks for web development. From basic value properties to sophisticated text processing capabilities, these objects enable developers to implement complex applications with ease. This article focuses on two key aspects of JavaScript's standard library: the standard built-in objects and the recent addition of the Segmenter API for Japanese text processing. The segmenter demonstrates how modern JavaScript continues to evolve, providing developers with powerful tools for handling international text while maintaining compatibility across major browsers.


## JavaScript Standard Built-in Objects

The JavaScript standard built-in objects represent core functionality and fundamental building blocks of the language. These objects include:

Value properties:

- globalThis

- Infinity

- NaN

- undefined

Function properties:

- eval()

- isFinite()

- isNaN()

- parseFloat()

- parseInt()

- decodeURI()

- decodeURIComponent()

- encodeURI()

- encodeURIComponent()

- escape()

- unescape() (Deprecated)

Fundamental objects:

- Object

- Function

- Boolean

- Symbol

Error objects:

- Error

- AggregateError

- EvalError

- RangeError

- ReferenceError

- SyntaxError

- TypeError

- URIError

- InternalError

Numbers and dates:

- Number

- BigInt

- Math

- Date

- Temporal

Text processing:

- String

- RegExp

Indexed collections:

- Array

- Int8Array

- Uint8Array

- Uint8ClampedArray

- Int16Array

- Uint16Array


## Intl.Segmenter Implementation

The text provides comprehensive details on the JavaScript implementation of the Segmenter API specifically for Japanese language processing. The implementation achieves Baseline status across all three major browser engines, with Mozilla's FormatJS providing a polyfill for `Intl.Segmenter`.

The Segmenter functionality goes beyond basic string splitting by working with Unicode code points and returning segments between boundaries. For Japanese text processing, where characters do not appear as spaces on the screen, this granularity is essential. The API supports three segmentation levels: grapheme (default), word, and sentence.

The constructor creates an Intl.Segmenter object with a specified locale and options, including granularity. The example demonstrates creating a Japanese-specific segmenter with word granularity:

```javascript

const segmenterJa = new Intl.Segmenter("ja-JP", { granularity: "word" });

```

The segment method takes a string and returns an iterable object, which can be converted to an array for processing. Each segment object contains the actual text, its index, the full input string, and an isWordLike flag for word granularity.

For developers working with Japanese text, the Segmenter provides accurate segmentation capabilities. The API handles non-space-separated languages well, counting characters correctly even in the absence of spaces. The implementation demonstrates Mozilla's commitment to modern JavaScript standards and cross-browser compatibility.


## Segmenter Constructor

The Segmenter constructor requires a locale identifier and optional options object. The constructor accepts general language tags or array of such identifiers, with support available across Chrome, Edge, Firefox, Opera, and Safari. When called without the 'new' keyword, it results in a TypeError.

The available options include 'localeMatcher' (with values "lookup" and "best fit", default "best fit") and 'granularity' (default "grapheme", also supporting "word" and "sentence").

The example below demonstrates creating a French word segmenter:

```javascript

const segmenterFr = new Intl.Segmenter("fr", { granularity: "word" });

```

This segmenter correctly segments French words, as shown in this example:

```javascript

const input = "Moi ? N'est-ce pas ?";

const segments = segmenterFr.segment(input);

for (const { segment, index, isWordLike } of segments) {

  console.log(

    "segment at code units [%d, %d]: Â«%sÂ»%s",

    index,

    index + segment.length,

    segment,

    isWordLike ? " (word-like)" : ""

  );

}

```

The basic use case includes:

1. Creating a locale-specific segmenter

2. Using the segmenter to get an iterator over a string's segments

3. Iterating through segments to process or display them

Additional functionality allows checking supported locales:

```javascript

console.log(Intl.Segmenter.supportedLocalesOf(["fr"])); // Displays supported French locales

```

This method returns an array of strings representing supported locale tags, enabling developers to verify compatibility before creating a segmenter. The supported locales can include Indonesian, German, and even Balinese, demonstrating the robustness of the implementation across multiple language families.


## Segmenter Methods and Properties

The Intl.Segmenter object provides three granularity levels: grapheme (default), word, and sentence. The constructor takes a locale identifier and optional options object, with the granularity defaulting to "grapheme".

The segment method returns an iterable object, which can be converted to an array for processing. Each segment object contains the text, index, input string, and isWordLike for word granularity.

For example, a word segmenter for French can be created as follows:

```javascript

const segmenterFr = new Intl.Segmenter("fr", { granularity: "word" });

```

The segmenter correctly processes French text, as demonstrated in this example:

```javascript

const input = "Moi ? N'est-ce pas ?";

const segments = segmenterFr.segment(input);

for (const { segment, index, isWordLike } of segments) {

  console.log(

    "segment at code units [%d, %d]: Â«%sÂ»%s",

    index,

    index + segment.length,

    segment,

    isWordLike ? " (word-like)" : ""

  );

}

```

The feature supports multiple languages through the `supportedLocalesOf` method, which returns an array of supported locale tags. This enables developers to verify compatibility before creating a segmenter.

Additional functionality includes:

- Segmentation of text with emoji

- Support for languages with complex grapheme boundaries, including Indic scripts

- Unicode-compliant segmentation algorithms for sentence and word boundaries


## Browser Support and Implementation

The Segmenter feature has achieved Baseline status across all three major browser engines: Chrome, Edge, Firefox, Opera, and Safari. This integration brings robust Unicode text segmentation capabilities to modern JavaScript development.

The API supports three granularity levels: grapheme (default), word, and sentence, allowing developers to choose the appropriate segmentation level for their use case. For example, grapheme segmentation is ideal for languages like Japanese, where spaces do not always indicate word boundaries.

A notable implementation detail is the handling of empty strings, where no segments are found and iterators complete immediately upon first next() access. The API also demonstrates flexibility through locale support, with built-in recognition of multiple language families including Indonesian, German, and Balinese.

Performance optimization is achieved through shared work across instantiations, as described in the repository documentation. The implementation notes that while the V8 engine (used in Chrome) ships with its own nonstandard segmentation API (Intl.v8BreakIterator), this new standard API aims to align more closely with modern JavaScript API design principles.

The feature's success highlights the growing importance of locale-sensitive text processing in web development. As demonstrated in practical applications, developers can now perform accurate word or character counting, sentence splitting, and advanced text manipulation tasks that were previously challenging with standard string manipulation methods.

