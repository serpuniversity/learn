---

title: The HTML Figure with Optional Caption Element

date: 2025-05-29

---


# The HTML Figure with Optional Caption Element

In web development, properly structuring content is crucial for both functionality and accessibility. The HTML `<figure>` element addresses this need by allowing developers to group related content, such as images, diagrams, and code snippets, while maintaining semantic independence from the main document flow. This article explores the `<figure>` element's core functionality, its proper implementation, and best practices for ensuring accessibility. Through detailed examples and technical specifications, we'll demonstrate how to effectively use this element to enhance web content structure and improve user experience.


## Definition and Core Functionality

The `<figure>` element represents a self-contained unit of content that can be referenced and separated from the main flow of the document without affecting its meaning. This unit is often accompanied by an `<figcaption>` element that provides a caption or legend. The `<figure>` element's content should be related to the main document but positioned independently, allowing it to be moved away from the main text when needed.

The element requires both start and end tags and must contain flow content. It can house various types of content including images, diagrams, tables, and code snippets, as demonstrated in the W3C HTML5 specification. The `<figcaption>` element serves to describe the content of its parent `<figure>` element, either appearing before or after the figure's contents. While the `<figure>` element can exist without an `<figcaption>`, this use is considered a misapplication since there would be no caption to describe.

The `<figure>` element's structure must adhere to specific technical requirements. It can contain any element that accepts flow content and must have both a start and end tag, with content placed between them. When using figcaption, it must be the first or last child of the figure to maintain proper functionality for assistive technologies. This positioning ensures that screen readers announce the caption immediately upon reaching the figure, providing context before the reader encounters the main content.

For example, the `<figure>` element can group multiple image elements within a single unit, as shown in this structured example:

```html

<figure>

  <img src="https://www.tutorialspoint.com/images/cbse_syllabus_icon.svg" alt="Rose" width="150" height="150">

  <figcaption>Fig.1 - Rose, Hyderabad, India.</figcaption>

</figure>

```

Alternatively, it can nest multiple figures together with a shared caption:

```html

<figure>

  <img src="/orang-utan.jpg" alt="Baby Orang Utan hanging from a rope">

  <img src="/macaque.jpg" alt="Macaque in the trees">

  <figcaption>A cheeky macaque, Lower Kintaganban River, Borneo. Original by Richard Clark</figcaption>

</figure>

```

The `<figure>` element's semantic purpose addresses the need for associated captions in web content, particularly for images, diagrams, and code examples. By grouping related elements together and providing descriptive captions, it enhances both the document's structure and accessibility.


## Element Structure and Syntax

The `<figure>` element requires both start and end tags and must contain flow content. It must contain at least one child element, which can be any element that accepts flow content. The element can contain multiple child elements, including images, diagrams, tables, and code snippets, as demonstrated in various W3C specifications and implementation examples.

While the primary purpose of `<figure>` is to contain images, the element's flexibility allows for alternative content such as tables or code snippets, as noted in the MDN Web Docs summary. The `<figcaption>` element provides a caption for the figure content and can be placed before or after the figure's contents, though it must directly follow the content in the DOM for proper functionality, as specified by the HTML5 figure element documentation.

The element's design allows it to contain complex content structures, including multiple images with shared captions, as shown in the figure and figcaption documentation example:

```html

<figure>

  <img src="/macaque.jpg" alt="Macaque in the trees">

  <img src="/orang-utan.jpg" alt="Baby Orang Utan hanging from a rope">

  <figcaption>A cheeky macaque, Lower Kintaganban River, Borneo. Original by Richard Clark</figcaption>

</figure>

```

This structure enables developers to group related content while maintaining semantic clarity for both sighted and screen reader users. The element's independence from the main document flow, combined with clear relationship markers through the `<figcaption>` element, enhances both accessibility and semantic accuracy in web development.


## Best Practices and Accessibility

The `<figure>` element requires a meaningful relationship between its content and caption, with the `<figcaption>` element directly following the content it describes. This structure provides proper functionality for assistive technologies and enhances accessibility for screen reader users.

To maintain semantic accuracy, the `<figcaption>` element should directly precede or follow its associated content within the `<figure>` element. This positions the caption logically, allowing screen readers to announce the caption immediately upon reaching the figure. While the element allows captions to appear before content, this positioning may cause accessibility issues unless the content structure requires it.

Developers should ensure that the `<figure>` element contains both a start and end tag, with the content placed between them. The `<figcaption>` element, when present, should be the first or last child of the figure to maintain proper functionality for assistive technologies. This structure enables screen readers to announce the caption immediately upon reaching the figure, providing context before the reader encounters the main content.

When using multiple images within a `<figure>` element, the `<figcaption>` should describe all images collectively, rather than describing each image individually. This approach maintains semantic clarity and provides a more useful caption for screen reader users. For example, a caption describing multiple images might state "A cheeky macaque, Lower Kintaganban River, Borneo. Original by Richard Clark" rather than providing separate captions for each image.

Accessibility considerations also apply when using images with no alt text. In such cases, the `<figcaption>` should still provide a meaningful description of the image, as demonstrated in the HTML5 specification example: `<figure role="region" aria-labelledby="caption-text"> <img src="/images/logo.png" alt="" /> </figure> <figcaption id="caption-text">The site logo, featuring a simplified representation of the company's name and slogan</figcaption>` Note that this approach requires non-empty alt attributes on images and may need further testing across different browsers and screen readers.


## Browser Support and Implementation

The `<figure>` element has achieved widespread browser support since its introduction in July 2015. Modern browsers including Internet Explorer, Firefox, and Chrome fully implement the specification, as documented by the MDN Web Docs. The element's semantic functionality has proven robust across different versions and manufacturers, though developers are advised to test implementation across multiple browsers and screen readers for optimal compatibility.

When implementing optional captions, developers should leverage the `<figcaption>` element's accessibility features. The `<figcaption>` must be the first or last child of the `<figure>` element to maintain proper functionality for assistive technologies, as specified by the HTML5 figure element documentation. To physically separate the caption from its associated content while maintaining accessibility, developers can employ the `aria-labelledby` attribute, requiring a non-empty `alt` attribute on the associated image element. Alternatively, JavaScript and CSS techniques enable hidden caption elements while maintaining semantic accuracy, though both approaches require thorough cross-browser testing.

Common implementation patterns include nesting images within a `<figure>` with a shared caption, as demonstrated in the W3C HTML5 specification examples: `<figure><img src="/macaque.jpg" alt="Macaque in the trees"><img src="/orang-utan.jpg" alt="Baby Orang Utan hanging from a rope"><figcaption>A cheeky macaque, Lower Kintaganban River, Borneo. Original by Richard Clark</figcaption></figure>` As noted in the MDN documentation, the `<figure>` element effectively groups related content while maintaining semantic independence, supporting its role in web content annotation.


## Example Usage

The `<figure>` element demonstrates versatility in content types, supporting images, diagrams, tables, and code snippets alongside its primary image functionality. As noted in the W3C HTML5 specification, the `<figure>` element enables content that can be moved away from the main document flow, including elements like illustrations and diagrams. This structure maintains semantic clarity while allowing for flexible layout options.

Content placement within the `<figure>` element follows specific structural guidelines to maintain accessibility and semantic accuracy. The `<figcaption>` element must directly precede or follow the content it describes, with the most common placement being immediately after the content. However, developers should avoid placing `<figcaption>` between content items, as this structure may cause accessibility issues for screen reader users (Fig. 1).

The element's implementation can accommodate various content types through appropriate structure and semantic markup. For instance, it supports image groups with shared captions, as demonstrated in the following structure:

```html

<figure>

  <img src="/macaque.jpg" alt="Macaque in the trees">

  <img src="/orang-utan.jpg" alt="Baby Orang Utan hanging from a rope">

  <figcaption>A cheeky macaque, Lower Kintaganban River, Borneo. Original by Richard Clark</figcaption>

</figure>

```

This structure enables developers to group related content while maintaining semantic independence, as recommended by the W3C specification and MDN Web Docs.

The `<figure>` element's capabilities extend to non-image content, including text snippets and diagrams, as shown in the following example:

```html

<figure>

  <pre>

    <code>

      function add(a, b) {

        return a + b;

      }

    </code>

  </pre>

  <figcaption>A JavaScript function that adds two numbers</figcaption>

</figure>

```

In this example, the `<figure>` element groups a code snippet with its descriptive caption, demonstrating the element's flexibility in managing various content types while maintaining semantic accuracy and accessibility.

