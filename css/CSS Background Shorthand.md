---

title: CSS Background Shorthand

date: 2025-05-26

---


# CSS Background Shorthand

The CSS background shorthand property revolutionizes web development by condensing multiple background-related properties into a single, efficient declaration. This powerful tool streamlines styling while maintaining complete customization, making it essential for modern web design.


## Background Property Shorthand

The CSS background shorthand property streamlines background styling by consolidating multiple properties into a single declaration. This allows for concise and efficient management of background elements across an HTML document.

The shorthand syntax combines eight background properties into one declaration, with each value separated by at least one space character. Properties are processed in the following order: background-image, background-position, background-size, background-repeat, background-attachment, background-origin, background-clip, and background-color.

For example, a complete shorthand declaration might look like this:

body { background: url(photo.jpg) center center/cover no-repeat fixed padding-box border-box #ccc; }

This declaration sets the background image, position, size, repeat method, attachment behavior, and color for the body element, demonstrating the property's flexibility and efficiency.

The shorthand takes precedence over individual property declarations, meaning that if both a shorthand and separate property declarations are present, the shorthand will override the individual properties unless explicitly stated otherwise. For instance, background-color takes precedence over background in the shorthand, ensuring that text remains readable during image loading or in cases of web server failure.


## Background Property Order

The CSS background shorthand property processes each background-related property in a specific order, with certain properties taking precedence over others. The formal syntax defines this process as follows:

1. Background Image: Values are specified as provided, with URL values made absolute.

2. Background Position: Each item consists of an offset combining absolute length and percentage with an origin keyword. The property is specified as a list of these items.

3. Background Size: Values are specified as provided, with relative lengths converted to absolute lengths. The property is specified as a list of items.

4. Background Repeat: Values are specified as a list of two keywords per dimension. The property is specified as a list of items.

5. Background Origin: Values are specified as provided.

6. Background Clip: Values are specified as provided.

7. Background Attachment: Values are specified as provided.

8. Background Color: Values are computed colors, interpolated on red, green, blue components in alpha-premultiplied sRGBA color space. The property is specified as a value.

The CSS3 standard allows for multiple backgrounds by layering properties. Each background-related property can take a comma-separated list, with the first value being the top layer, the second value the second layer, and the background color always serving as the last layer.

The recommended property order for the shorthand is: background-image, background-position, background-repeat, background-origin, background-clip, background-size, background-color. While the order of these properties doesn't affect most cases, it's crucial to maintain the sequence for background-origin and background-clip (border-box, padding-box, content-box), as well as to declare background-size immediately following background-position.


## Background Property Defaults

The background shorthand property takes precedence over individual property declarations, meaning that if both a shorthand and separate property declarations are present, the shorthand will override the individual properties unless explicitly stated otherwise. For instance, background-color takes precedence over background in the shorthand, ensuring that text remains readable during image loading or in cases of web server failure.

The formal syntax for the background shorthand is defined as:

background = <bg-layer>[#] [?] , <final-bg-layer>

bg-layer = <bg-image> [||] <bg-position> [[] / <bg-size> []] [?] [||] <repeat-style> [||] <attachment> [||] <visual-box>

Key defaults for undeclared properties include:

- background-image: none

- background-position: 0% 0% (same as top left)

- background-size: auto

- background-repeat: repeat

- background-attachment: scroll

- background-origin: padding-box

- background-clip: border-box

- background-color: transparent

The property processing order focuses primarily on the background positioning area, with the following sequence:

1. Background Image: Values are specified as provided, with URL values made absolute.

2. Background Position: Each item consists of an offset combining absolute length and percentage with an origin keyword. The property is specified as a list of these items.

3. Background Size: Values are specified as provided, with relative lengths converted to absolute lengths. The property is specified as a list of items.

4. Background Repeat: Values are specified as a list of two keywords per dimension. The property is specified as a list of items.

5. Background Attachment: Values are specified as provided.

6. Background Origin: Values are specified as provided.

7. Background Clip: Values are specified as provided.

8. Background Color: Values are computed colors, interpolated on red, green, blue components in alpha-premultiplied sRGBA color space. The property is specified as a value.

The three primary exceptions to the general property ordering rule involve background-origin and background-clip, where the first value applies to background-origin and the second to background-clip, and background-size, which must immediately follow background-position.


## Multiple Backgrounds

The CSS background shorthand demonstrates significant improvements in code efficiency while maintaining developer flexibility. As noted in the CSS Background Shorthand Tutorial, this property enables cleaner implementation of multiple background properties through a single declaration.

To effectively utilize multiple backgrounds, developers should follow the recommended property order: background-position, background-size, background-repeat, background-attachment, background-origin, background-clip, background-color, background-image. While this sequence applies primarily to background positioning, it's crucial for maintaining correct behavior of background-origin and background-clip, which must be declared as border-box, padding-box, or content-box values.

The background shorthand applies to the background positioning area, processing properties as follows:


### Background Image

Values are specified as-is, with URL values converted to absolute paths. Each image can be combined with positioning, sizing, and repetition properties.


### Background Position

Each position consists of an offset combining absolute lengths and percentages with origin keywords. These items form a list that determines the image's placement relative to the element.


### Background Size

Values remain unchanged, with relative lengths converted to absolute sizes. This property must immediately follow background-position in the shorthand sequence.


### Background Repeat

Repeat values are specified as a list of two keywords per dimension, forming a complete declaration for both horizontal and vertical repetition.


### Background Attachment

Values remain unchanged, affecting whether the background scrolls with the content or remains fixed.


### Background Origin

Values remain unchanged, determining the background's origin point relative to the element's layout box.


### Background Clip

Values remain unchanged, specifying the painting area of the background within the element's layout box.


### Background Color

Computed colors are specified using alpha-premultiplied sRGBA color space, always serving as the final layer in layered backgrounds.

The syntax for the background shorthand, as defined in the CSS specification, allows for multiple background properties in a single declaration. Each property can take a comma-separated list, with the first value becoming the top layer, the second value the second layer, and the background color always serving as the last layer.

For example, the following declaration demonstrates proper use of multiple backgrounds and their properties:

```css

body {

  background: url(photo.jpg) center center/cover no-repeat fixed padding-box border-box #ccc,

              url(photo2.jpg) left center no-repeat;

}

```

This example correctly implements two background images with distinct positioning, sizing, and attachment behaviors. The background color ensures text readability while the multiple background layers create complex visual effects.


## Background Property Syntax

The background shorthand property allows specifying multiple CSS background properties in a single declaration, significantly reducing code size and improving maintainability. The property combines eight background properties into one declaration, with each value separated by at least one space character.

The official syntax defines the property as follows:

background = <bg-layer>[#] [?] , <final-bg-layer>

bg-layer = <bg-image> [||] <bg-position> [[] / <bg-size> []] [?] [||] <repeat-style> [||] <attachment> [||] <visual-box>


### Background Property Order and Precedence

The property processes each background-related property in a specific order, with certain properties taking precedence over others. The recommended sequence is:

1. background-color

2. background-image

3. background-repeat

4. background-attachment

5. background-position

For most cases, the order of properties doesn't affect functionality. However, proper sequence is crucial for:

- background-origin (first value) and background-clip (second value)

- background-size, which must follow background-position immediately

The shorthand syntax allows for concise declarations like:

body { background: #ffffff url("img_tree.png") no-repeat right top; }


### Multiple Background Layers

The property enables layered backgrounds through comma-separated lists. The first value becomes the top layer, the second value the second layer, with background color serving as the final layer. For example:

```css

body {

  background: url(photo.jpg) center center/cover no-repeat fixed padding-box border-box #ccc,

              url(photo2.jpg) left center no-repeat;

}

```

This implementation correctly applies two background images with distinct positioning, sizing, and attachment behaviors.


### Default Values and Property Omission

When using the shorthand, omitted property values default to their initial values:

- background-image: none

- background-position: 0% 0% (same as top left)

- background-size: auto

- background-repeat: repeat

- background-attachment: scroll

- background-origin: padding-box

- background-clip: border-box

- background-color: transparent

For example, the following declaration sets only the background color, maintaining default values for all other properties:

```css

p {

  background-color: red;

  background: url(images/bg.gif) no-repeat left top;

}

```

The text emphasizes the importance of including a fallback background color when specifying background-image, ensuring text readability during image loading or in case of web server failure.

