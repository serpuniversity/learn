---

title: HTML `<figcaption>` Element: The Figure Caption

date: 2025-05-29

---


# HTML `<figcaption>` Element: The Figure Caption

The `<figcaption>` element plays a crucial role in HTML by providing captions for media elements such as images, videos, and audio files. This semantic markup enhances both accessibility and SEO through descriptive content, making it an essential component for web developers and content creators. Proper implementation of `<figcaption>` improves user experience for all visitors, particularlythose relying on assistive technologies.


## Definition and Purpose

The `<figcaption>` element serves a specific purpose in HTML, acting as a caption for media elements such as images, videos, and audio files. It must be placed immediately after the corresponding media element within a `<figure>` element.

The `<figcaption>` element supports only global attributes and contains flow content, with both starting and ending tags being mandatory. It must be either the first or last child of the `<figure>` element, though it's common practice to place it after the media content for visual consistency.

This semantic markup improves both accessibility and SEO by providing descriptive context for the content. Screen readers can read out the text within the `<figcaption>` element, helping users who rely on assistive technologies to understand the content. Search engines also benefit from this additional textual information about the image or media element.


## Technical Specifications

The `<figcaption>` element operates within strict technical specifications that ensure proper semantic structure. It exists as a container for flow content and requires both a start and end tag, making it a mandatory element within the `<figure>` parent. Content placed between these tags becomes the figure caption, providing descriptive context for various media types including images, videos, and audio files.

The `<figcaption>` element's position within the `<figure>` structure is crucial for maintaining semantic clarity. It must appear as either the first or last child of the figure element, though placement immediately following the media content is common practice for visual consistency. This positioning helps screen readers and other assistive technologies correctly interpret the relationship between the caption and its associated media element.


## Usage and Best Practices

The `<figcaption>` element should be used only once per `<figure>` element, as per the HTML5 specification. While it's not obligatory to use a `<figcaption>` with every `<figure>` element, its inclusion significantly enhances accessibility and content understanding. The element's primary purpose is to describe or explain the content within the `<figure>` element, helping both non-impaired and visually impaired users.

The `<figcaption>` element's positioning within the `<figure>` structure is crucial for semantic clarity and accessibility. It always requires both starting and ending tags, which are mandatory for this element. To enhance visual distinction, web developers are encouraged to use CSS styles to differentiate the `<figcaption>` element from other page content.

For complex data representations like tables, it's generally more appropriate to use the `<table>` element with its dedicated `<caption>` element to provide context rather than the `<figure>` and `<figcaption>` combination. This approach aligns with best practices for maintaining semantic HTML structure and improving accessibility for all users.


## Browser Compatibility

The `<figcaption>` element's browser compatibility has been thoroughly tested across modern web browsers, and it is officially supported by every major browser including Chrome, Firefox, Safari, Edge, and Opera. This universal support ensures consistent rendering and functionality across different platforms.

The element's structure remains consistent across implementations, requiring both start and end tags as part of its mandatory syntax. The `<figcaption>` is designed to be flexible within the `<figure>` container, allowing it to be placed as either the first or last child. However, it's most commonly seen immediately following the main media content for visual clarity, particularly important when used with responsive media elements like those managed by the `<picture>` element.

This widespread browser support extends to the underlying technical specifications of the `<figcaption>`, which are consistent with the HTML5 standard. Web developers can confidently use this element across their projects, knowing it will work reliably in all target browsers without the need for additional cross-browser compatibility code.


## Example Implementation

To illustrate proper implementation, consider the following examples:

Basic usage pairs the `<img>` tag with a `<figcaption>` for image captions:

```html

<figure>

  <img src="https://www.tutorialspoint.com/cg/images/logo.png" alt="logo" style="width:50%">

  <figcaption> Tutorialspoint Logo </figcaption>

</figure>

```

For more complex presentations, the `<figure>` can contain multiple image elements:

```html

<figure>

  <img src="dog1.jpg" alt="Maltese Terrier">

  <img src="dog2.jpg" alt="Black Labrador">

  <img src="dog3.jpg" alt="Golden Retriever">

  <figcaption> Multiple dogs in different breeds </figcaption>

</figure>

```

When using the `<figure>` for code snippets, the `<figcaption>` provides a descriptive caption:

```html

<figure>

  <pre>

    <code>

p { color: #333; font-family: Helvetica, sans-serif; font-size: 1rem; }

    </code>

  </pre>

  <figcaption> Basic CSS paragraph styling </figcaption>

</figure>

```

The `<figure>` element supports multiple nested `<figure>` structures where appropriate:

```html

<figure role="group">

  <figure>

    <img src="dog1.jpg" alt="Maltese Terrier">

    <img src="dog2.jpg" alt="Black Labrador">

    <img src="dog3.jpg" alt="Golden Retriever">

  </figure>

  <figcaption> Multiple images in figure </figcaption>

</figure>

```

To enhance accessibility, consider the following styling approach:

```css

figure { text-align: center; margin: 20px; }

figcaption { font-style: italic; color: #555; margin-top: 5px; }

```

These examples demonstrate the `<figcaption>` element's versatility in providing clear, descriptive captions for various content types while maintaining semantic web practices.

