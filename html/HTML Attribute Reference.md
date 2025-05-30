---

title: HTML Attribute Reference

date: 2025-05-29

---


# HTML Attribute Reference

HTML attributes transform simple web page elements into dynamic, feature-rich components. From basic styling to advanced functionality, these attribute-value pairs control nearly every aspect of web content. In this guide, we'll explore the most essential HTML attributes, from core functionality to advanced techniques like responsive images and metadata.


## Core HTML Attributes

Core HTML attributes provide additional information about elements, with most coming in name-value pairs. This functionality is crucial for enhancing both the functionality and accessibility of web content.

For image elements, the src attribute specifies the path to the image, while width and height attributes provide essential size information. The alt attribute offers crucial alternative text for images, improving accessibility and SEO. The style attribute enables direct styling of elements, allowing developers to control visual aspects like color, font, and size.

The lang attribute of the `<html>` tag declares the document's language, supporting localization through country codes (e.g., en-US). The title attribute provides additional information about elements, often displaying as tooltips when users hover over them. While the HTML standard doesn't require lowercase attribute names, W3C recommends using lowercase for compatibility with stricter document types like XHTML.

Basic attribute usage follows a simple syntax: attribute_name="value". For example, setting the color of an `<h1>` element to green would use the style attribute as follows:

```html

<h1 style="color:green;">This text is green.</h1>

```

Developers should use relative URLs in the src attribute of `<img>` tags for robustness, especially when changing domains. The attribute value should be enclosed in quotes, with each property-value pair separated by a semicolon. For instance:

```html

<img src="img_girl.jpg" style="width:100px;height:200px;" alt="A girl">

```

Understanding these core attributes is fundamental for effective HTML development, as they enable precise control over element behavior, appearance, and functionality.


## Element-Specific Attributes

The `<img>` element's src attribute is the essential gateway for displaying images on web pages. It accepts both absolute URLs, which link to external images hosted on other websites, and relative URLs for images stored within the same website. When using relative URLs, paths without a leading slash are considered relative to the current page, while paths beginning with a slash are relative to the domain root (e.g., src="img_girl.jpg" and src="/images/img_girl.jpg"). This flexibility in URL specification helps maintain robust image display even when domain changes occur.

For images to display correctly, the `<img>` tag requires both width and height attributes, specifying the dimensions in pixels. The alt attribute is crucial for providing alternative text descriptions that enhance accessibility and improve search engine optimization. When an image fails to display due to connection issues or incorrect src attributes, the alt text serves as a fallback, ensuring content remains accessible to all users. This attribute also benefits users of screen readers, making web content more inclusive for individuals with visual impairments.


## Form-related Attributes

The `<input>` element's type attribute defines the type of input field, with options including text, number, date, and email. This attribute determines the visual appearance and behavior of the input field, as seen in the following examples:

```html

<input type="text"> <!-- Standard text input -->

<input type="number"> <!-- Numeric input field -->

<input type="date"> <!-- Date picker input -->

<input type="email"> <!-- Email input field with validation -->

```

The required attribute is a boolean attribute that makes an input field mandatory. When present, browsers display an error message if the field is submitted without user input. This ensures that all required fields are completed before form submission.

```html

<input type="text" required> <!-- Mandatory text input -->

```

The placeholder attribute provides a hint for input values, displayed as grey text within the input field. This helps guide users on what information to enter. For instance:

```html

<input type="text" placeholder="Enter your name">

```

The value attribute specifies the default text for input elements. This can be particularly useful for prefilling form data after a failed submission. Example usage:

```html

<input type="text" value="Default Value">

```

Additional form-related attributes include action, which specifies where form data should be sent upon submission, and method, which defines the HTTP method used (GET or POST). These attributes work together to control form behavior and data handling.


## Accessibility and Localization

The alt attribute of the `<img>` tag provides an essential alternative text description for images, which improves accessibility and supports search engine optimization. When an image fails to display due to connection issues or incorrect src attributes, the alt text serves as a crucial fallback, ensuring content remains accessible to all users, including those who rely on screen readers.


### Language and Document Structure

The lang attribute of the `<html>` tag declares the language of the Web page, supporting localization through country codes in the format language-country. This attribute helps screen readers and translation tools understand the document's language context. While the HTML standard doesn't explicitly require lowercase attribute names, W3C recommends using lowercase for compatibility with stricter document types like XHTML.


### Additional Accessibility Features

The title attribute defines extra information about an element and displays as a tooltip when the user hovers over the element, providing immediate context without cluttering the page content. This attribute helps enhance user experience by offering quick information about interactive elements like buttons or links.


### Form Element Localization

The form element's lang attribute allows specifying the language of the form elements, supporting multilingual forms and improved accessibility for users who need to understand form instructions in their preferred language. This attribute works in conjunction with the lang attribute of the `<html>` tag to establish consistent language contexts across the page.


## Advanced Attributes

The srcset attribute of the `<img>` element offers a powerful solution for managing image resolutions, allowing developers to specify multiple image sources with different sizes. This attribute determines which image to display based on the current device's capabilities, ensuring that users receive the most appropriate image quality while maintaining optimal loading performance.

The srcset attribute accepts multiple URL values, each associated with a specific image resolution. These URLs can reference either the image's original source or separate optimized versions stored on the server. The browser evaluates the device's capabilities and available network bandwidth to select the most suitable image from the available options, improving both performance and visual quality.

For instance, a common implementation might include both a low-resolution version for quick initial display and a high-resolution version for larger screens:

```html

<img src="img_lowres.jpg" srcset="img_lowres.jpg 640w, img_highres.jpg 1280w">

```

This configuration tells the browser to use the lower-resolution image for smaller screens or devices, while reserving the higher-quality version for larger displays. The 640w and 1280w values represent the image widths at which each source should be used, helping the browser make informed decisions about image selection and rendering.

The `<meta>` element's content attribute provides additional metadata definitions, offering a flexible way to include structured information within HTML documents. This attribute can accept various values, allowing developers to define custom data points or follow established metadata standards (such as Open Graph for social media integration).

For example, setting a meta description helps search engines understand the content of a page:

```html

<meta name="description" content="A brief summary of the page's main content">

```

This attribute enables developers to control how their content is presented in search results and social media previews, enhancing both usability and discoverability. The meta content attribute can also be used to specify character set definitions, viewport settings, and other HTML-related metadata, providing a versatile tool for controlling document behavior and appearance.

## References

- [HTML Nobr The non Breaking Text Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Nobr%20The%20non%20Breaking%20Text%20Element.md)
- [HTML The Ruby Annotation Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Ruby%20Annotation%20Element.md)
- [HTML The Document Body Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Body%20Element.md)
- [HTML Relnoopener](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relnoopener.md)
- [HTML The Generic Search Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Generic%20Search%20Element.md)