---

title: HTML `<img>`: The Image Embed element

date: 2025-05-29

---


# HTML `<img>`: The Image Embed element

The HTML `<img>` element serves as a fundamental building block for web development, enabling developers to embed and manage images within web pages. Beyond its basic functionality of displaying visual content, the `<img>` tag incorporates a rich set of attributes that control everything from image loading behavior to styling and accessibility. This article explores the comprehensive capabilities of the `<img>` element, from its core functionality to advanced usage scenarios, highlighting best practices for developers seeking to optimize both the visual presentation and technical performance of their web pages.


## Basic Usage and Attributes

The `<img>` tag creates a holding space for referenced images, linking them to web pages rather than inserting them directly. It requires the following essential attributes:

- `src`: Specifies the image's URL. The browser retrieves the image from the web server and inserts it into the page if the URL is correct. In cases of network errors, content blocking, or link rot, the browser displays the `alt` text instead.

- `alt`: Provides alternative text for the image. This text is crucial for accessibility, as screen readers use it to inform users about the image's content. Effective alternate text descriptions should be used for all images, particularly those crucial to understanding the page's content.

Additional attributes control image appearance and behavior:

- `width` and `height`: Set the image's intrinsic size using the `width` and `height` attributes. For responsive design, these can be combined with CSS properties to control image size and layout.

- `title`: Displays a tooltip when the user hovers over the image, providing additional context without affecting accessibility.

- `crossorigin`: Controls cross-origin access for images used with canvas, allowing or denying third-party image inclusion.

- `referrerpolicy`: Specifies which referrer information to use when fetching an image, supporting options like "no-referrer," "no-referrer-when-downgrade," and "origin."

Image sources can be specified using either relative or absolute URLs. Modern best practices recommend hosting images on the same server for performance and maintenance, though absolute URLs remain valid for referencing external images.

Common image formats supported across all browsers (Chrome, Edge, Firefox, Safari, Opera) include APNG, GIF, ICO, JPEG, PNG, and SVG. While older formats like APNG and BMP remain supported for existing content, they are no longer recommended for new projects.

The `<img>` tag supports responsive image hints through attributes like `srcset`, `sizes`, and `loading`, while also enabling advanced styling options with CSS properties like border, box-shadow, and transitions. Effective implementation requires careful consideration of image optimization, accessibility, and cross-browser compatibility.


## Image Attributes Explained

According to the HTML specification, the `<img>` tag requires two fundamental attributes: `src`, which specifies the URL of the image, and `alt`, which provides alternative text for the image. These attributes work together to ensure that images are accessible and functional in all browsing situations.

The `src` attribute is mandatory and must contain the path to the image to be embedded. This URL can be either relative or absolute, depending on the image's location. For optimal performance and reliability, web developers are encouraged to host images on the same server to minimize network latency.

The `alt` attribute is equally crucial, as it provides a textual replacement for the image content. This text serves multiple purposes: it's read by screen readers to inform users about the image's content, and it's displayed when the image cannot be loaded due to network errors, content blocking, or link rot. The alternative text should accurately describe the image's content, as it may be the only information available to users who can't see the image.

Additional attributes control various aspects of image presentation and behavior. The `width` and `height` attributes set the image's intrinsic size, which helps prevent content layout shifts while the image is loading. These values can also be controlled using CSS properties like `width` and `height`.

Other relevant attributes include `loading`, which controls when the image should be loaded (immediately or deferred), and `crossorigin`, which enables cross-origin access for images used with canvas. The `referrerpolicy` attribute specifies which referrer information to use when fetching an image, supporting options like "no-referrer," "no-referrer-when-downgrade," and "origin."

The `<img>` tag supports multiple image formats, with common options including APNG (Animated Portable Network Graphics), AVIF (AV1 Image File), BMP (Bitmap file), and others. While older formats like APNG and BMP remain supported for existing content, they are no longer recommended for new projects due to improved performance alternatives.


## Accessibility Best Practices

Alt text serves multiple critical functions in web accessibility. When images fail to load due to network issues, content blocking, or link rot, the alt text ensures the content remains accessible to all users. This textual description is particularly important for visually impaired users who rely on screen readers to navigate web pages.

To write effective alt text, developers should avoid redundant information like "image of" or "picture of," as screen readers naturally identify these phrases. Instead, focus on describing the image's content clearly and concisely. For example, if an image shows a T-Rex skeleton in a museum, an appropriate alt text would be "The head and torso of a dinosaur skeleton; it has a large head with long sharp teeth." This description provides meaningful information without unnecessary repetition.

Best practices also recommend using unique alt text for each image rather than repeating identical descriptions. When multiple images are similar, consider creating a single detailed description that can be reused. This approach maintains clarity while reducing redundancy in the HTML code.

The alt text should stand alone, providing all necessary context without requiring additional explanation. This independence is crucial for screen reader users who may encounter images out of their natural reading order. When images contain actionable elements like links or buttons, the alt text should describe the link's destination or button's function rather than just stating "link" or "button."

For decorative images that don't convey essential information, use an empty alt attribute: `alt=""`. This tells screen readers to skip the image, which improves reading flow for users who don't need to hear decorative elements. However, this practice should be used sparingly, as every image should deliver some value to users.

Developers should test their alt text by temporarily disabling images in their browser and reviewing the content. This process helps ensure that the alt text provides sufficient information for understanding the page's meaning. Regular accessibility audits can further refine these descriptions, ensuring that all images fulfill their intended communication purpose effectively.


## Security and Performance

The `<img>` tag provides several attributes for controlling image loading and security, offering developers fine-grained control over how images are displayed on web pages. The crossorigin attribute enables cross-origin access for images used with canvas, allowing or denying third-party image inclusion based on the image source's CORS settings.

The referrerpolicy attribute specifies which referrer information to use when fetching an image, supporting options like "no-referrer," "no-referrer-when-downgrade," and "origin." This attribute helps balance privacy concerns with necessary referrer information for image requests, allowing developers to tailor the policy based on their specific security requirements.

The loading attribute controls when the image should be loaded, defaulting to "eager" behavior that loads images immediately regardless of their position in the viewport. This can be set to "lazy," which defers loading until the image reaches a calculated distance from the viewport, helping to improve initial page load times without tracking user scroll positions.

For image dimensions, the intrinsic height must be an integer without a unit, while the width and height attributes enable the browser to calculate the image's aspect ratio before loading. This aspect ratio helps reserve space for display and reduces layout shifts when the image is downloaded, maintaining a smooth user experience during page rendering.

The srcset attribute allows specifying a list of image files to use in different situations, while the sizes attribute provides responsive image hints to help the browser choose the most appropriate image size. Together, these attributes enable developers to optimize image performance while maintaining visual quality across various devices and screen sizes.


## Styling and Layout

The HTML `<img>` tag supports advanced styling and layout options through a combination of HTML attributes and CSS properties. These features enable developers to create responsive image galleries, implement dynamic sliders, and optimize visual presentation across devices.

The `width` and `height` attributes define the image's intrinsic size, which helps prevent content layout shifts during loading. These attributes can be combined with CSS properties like `width` and `height` to maintain consistent rendering.

For responsive design, developers can use the `object-fit` property, which controls how the image fits into its container while maintaining its aspect ratio. Possible values include:

- `contain`: Keeps the image's aspect ratio and scales it to fit within the container while maintaining its original proportions.

- `fill`: Scales the image to fill the container while preserving its aspect ratio.

- `cover`: Scales the image to cover the entire container, potentially distorting its aspect ratio.

- `none`: Resizes the image to the exact dimensions defined in the HTML, ignoring the image's aspect ratio.

- `scale-down`: Always scales down the image to fit within the container while maintaining its aspect ratio.

Image sizing should prioritize optimization through proper file compression and editing rather than relying on HTML attributes. Setting excessive dimensions can lead to poor visual quality and increased bandwidth usage.

CSS background properties offer alternative methods for image integration:

- `background-image` applies the image as a background to an HTML element.

- `background-size` controls the image's scaling behavior within its container.

- `background-repeat` determines whether the image tiles horizontally, vertically, or not at all.

Developers can also implement interactive features using JavaScript, including:

- Creating responsive image galleries

- Building carousel applications with CSS animations

- Developing dynamic image galleries

- Implementing custom sliders with navigation buttons

- Creating review carousels with smooth transitions

- Building autoplay carousels

- Implementing draggable card sliders

## References

- [HTML The Marquee Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Marquee%20Element.md)
- [HTML The Document Title Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Title%20Element.md)
- [HTML The Document Base URL Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Base%20URL%20Element.md)
- [HTML Tabindex](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Tabindex.md)
- [HTML The Picture Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Picture%20Element.md)