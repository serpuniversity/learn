---

title: Master CSS3 Object-Fit for Image and Content Resizing

date: 2025-05-26

---


# Master CSS3 Object-Fit for Image and Content Resizing

CSS3's object-fit property revolutionizes how we handle responsive images and content, offering precise control over element sizing within containers. This article explores the fundamentals of object-fit, examining how different values resize images while preserving aspect ratios and allowing for versatile content placement. From stretching images to cover containers to maintaining their original proportions with empty space, we'll uncover the best practices for mastering this crucial CSS3 feature.


## Understanding object-fit

The object-fit property in CSS3 allows developers to control how images and videos resize within their containers. The property offers five primary options: fill, contain, cover, none, and scale-down.

The fill value stretches images to completely cover the container dimensions, as demonstrated when an image is set to 1000px width and 400px height. This stretching occurs regardless of the image's original aspect ratio. However, if the image's width and height match its aspect ratio, the image will not be distorted.

The contain value maintains the image's aspect ratio while ensuring it fits within the container. This results in empty space if the container's aspect ratio differs from the image's. The example shows an image with the same 1000px width and 400px height attributes maintaining its aspect ratio within the container.

The cover value scales the image to cover the container while maintaining its aspect ratio, which may crop parts of the image that don't fit. This creates an effect where the image appears zoomed in within the container, as illustrated by the example with the specified dimensions.

These properties work with both images and videos. The object-fit property requires careful consideration of image characteristics, as the browser behavior varies based on whether the available space matches or exceeds the image's aspect ratio. Understanding these interactions allows developers to choose the most appropriate fitting method for their content.


## The fill value

The object-fit: fill value stretches the image to completely cover the container dimensions, disregarding the original aspect ratio. This results in the image being stretched to fit the container's 1000px width and 400px height. If the image's width and height match its aspect ratio, the image will not be distorted, but in most cases, some degree of stretching occurs.

The stretching behavior is consistent regardless of the image's original dimensions. For example, if an image with dimensions 800px by 600px is applied to a container with 1000px width and 400px height, the image will be stretched to fill the container, potentially distorting the aspect ratio.

Developers should note that while the fill value provides complete coverage, it may not be suitable for images where preserving the original aspect ratio is important. The behavior of the fill value is consistent across modern browsers, making it a reliable choice for cases where full container coverage is desired, regardless of the original image dimensions.


## The contain value

object-fit: contain scales the image to fit within its container while maintaining its aspect ratio, potentially leaving empty space if the container's aspect ratio differs from the image's. This value ensures that the image retains its original proportions, though it may not fill the entire container.

When applied to an image with the same 1000px width and 400px height attributes, the container maintains the image's aspect ratio while adjusting its size to fit within the container dimensions. If the container's aspect ratio matches the image's, the image will fill the entire container without distortion. However, if the container's aspect ratio differs, the image will be centered and scaled proportionally, with empty space appearing around the image.

The contain value works in conjunction with the object-position property to control the alignment of the image within its container. By default, the object-position value is 50% 50%, which centers the image in its content box. This centering behavior can be modified using keyword values (top, bottom, left, right) or length/percentage values to adjust the image's positioning.

Despite its usefulness, the contain value isn't always the most suitable choice. When maintaining aspect ratio is crucial and some empty space is acceptable, contain provides a reliable method for ensuring images fit their containers without distortion. However, developers should consider alternative fit methods when complete container coverage is preferred or when maintaining specific image proportions is essential.


## The cover value

The object-fit: cover value scales the image to cover the container while maintaining its aspect ratio, which may result in cropping parts of the image that don't fit. This behavior is particularly useful when you need to ensure the image fills the container without distorting its proportions, but you're willing to sacrifice some image content to achieve this.

When applied to an image with dimensions 1000px width by 400px height, the cover value will scale the image to cover the container while maintaining its aspect ratio. If the container's dimensions differ from the image's aspect ratio, parts of the image will be cropped to fill the container completely. For example, if the container is 1000px by 600px, the image will be scaled to cover the width while maintaining its 4:1 aspect ratio, resulting in 100px of the image being cropped from the top and bottom.

The cover value works in conjunction with the object-position property to control image display. By default, this property centers the image within the container using an object-position value of 50% 50%. However, developers can adjust this positioning using keyword values (top, bottom, left, right) or length/percentage values. For instance, setting object-position to 100% 0 would center the image, while 100% -20% would crop the image to display part of the turtle and alligator heads, with 20% of the image offset to the left.

This property works both with and without surrounding containers. When used with grid areas, setting object-fit to cover on an image with width and height properties of 100% ensures the image fits nicely within a grid area that expands and contracts with the viewport. Developers can achieve similar results for responsive layouts by combining object-fit with grid positioning and media queries, creating images that maintain their aspect ratio while filling various container sizes on different devices.


## Browser support and compatibility

The object-fit property's implementation began in 2014, with significant browser support across modern versions. As of the latest standards, the property operates as follows:

- Firefox (31.0)

- Chrome (16.0)

- Safari (36.0)

- Opera (7.1)

- Microsoft Edge (19.0)

The property requires specific handling for Internet Explorer versions 9 through 10, as well as Edge. For these browsers, developers can use polyfills from GitHub repositories such as object-fit-images for images and fitie for videos. Additionally, custom styling workarounds can be implemented using browser-specific selectors:

For IE9:

.root figure { height:200px; overflow:hidden; }

.root img { height:auto; width:auto; }

For IE10+:

_:-ms-lang(x), figure { height:200px; overflow:hidden; }

figure { img { width:33%; height:200px; object-fit:contain; object-position:0 0; } }

_:-ms-lang(x), img { height:auto; width:auto; }

These implementations demonstrate the property's effectiveness in creating responsive designs while maintaining image integrity across different browsers and devices.

