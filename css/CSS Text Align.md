---

title: CSS Text Align

date: 2025-05-25

---


# CSS Text Align

In web design, text alignment is a fundamental aspect of layout and typography that affects how information is presented to users. Whether you're developing a simple website or a complex web application, controlling how text appears within elements is crucial for both functionality and aesthetics. This comprehensive guide covers the basics of text alignment, including how to apply it, its behavior in responsive designs, and how it interacts with other layout techniques.


## Text Alignment Basics

The CSS text-align property controls the horizontal placement of text within HTML elements, offering several values including left, right, center, and justify. This property sets the alignment of inline-level content within block elements, with common values aligning text to the left, right, center, or justifying it across the line.

The default text alignment varies based on directionality: left for left-to-right (LTR) text and right for right-to-left (RTL) text. The property is inherited and applies to block elements, with its effect on inline elements limited to text content. Text alignment can be applied using multiple approaches: directly within HTML tags, through internal CSS in the document head, or via external stylesheets.

For left alignment, developers simply apply `text-align: left;` to their elements, which serves as the default for most text elements. Center alignment requires `text-align: center;`, positioning text in the middle of its container. Right alignment uses `text-align: right;`, placing text on the element's right side. The justify value distributes text evenly across the line, creating a flush left and right appearance suitable for certain content types like newspaper-style layouts.


## Applying Text Alignment

The text-align property affects text alignment through multiple methods, including direct element styling, class and ID selectors, and the use of flexbox for more complex layouts. For simple text alignment, inline elements can be centered using a parent container with display: flex; and align-items: center; justify-content: center;.

For block-level elements, the margin property offers an alternative to text-align: center;. By setting a fixed width and margin: auto, elements automatically center themselves within their container. This approach works for both paragraphs and header elements, though developers should note that text-align only reliably centers text within block-level elements.

Class and ID selectors offer a clean way to apply consistent styles across multiple elements. The text-left, text-center, text-right, and text-justify classes provide quick styling options for common alignment needs. These classes can be combined with responsive design techniques using prefixing, where a base class applies default styles and a media query changes the alignment at specific breakpoints.

The property's inheritance allows for parent-child styling flexibility. However, developers must be aware that text-align settings on parent elements can be overridden by child elements unless explicitly set to inherit. For responsive design, the property naturally adapts to changes in screen size, with most default values remaining valid across devices.


## Text Alignment in Responsive Design

The text-align property's behavior varies with screen size through media queries and responsive design techniques. For instance, center-aligning a header on mobile devices requires specific media query rules:

```css

@media (max-width: 600px) {

  .header {

    text-align: center;

  }

}

```

This technique allows centering headings or call-to-action buttons while maintaining left alignment on larger screens. Text justification ensures clean margins for readability, as demonstrated in educational articles:

```css

article {

  text-align: justify;

  line-height: 
1.6;

}

```

These responsive adjustments maintain consistent text alignment across devices, ensuring optimal readability and visual impact.


## Text Alignment with Flexbox

Flexbox offers developers three primary methods for centering elements. First, by setting the parent container to display: flex; and applying align-items: center; justify-content: center;, flex items are centered both vertically and horizontally. This approach requires minimal calculation and handles responsive design naturally.

For developers seeking more straightforward solutions, the documentation offers several options. The padding method applies top and bottom padding to vertically center text, while the line-height approach sets the text height equal to the container's height. Both methods require careful calculation to achieve precise alignment.

Inline elements like buttons can be centered using a wrapping div with inline style declaration: <div style="text-align: center;">button content</div>. Block-level elements achieve centering through margin auto; setting width and applying margin auto; centers the element while preventing stretching.

The documentation also highlights the importance of considering parent-child relationships. Developers must understand that text-align settings on parent elements can be overridden by child elements unless explicitly set to inherit. This property's natural adaptation to screen size makes it particularly useful for responsive web design, allowing developers to maintain consistent alignment across devices while applying specific styles through media queries.


## Additional Text Alignment Properties

The `text-align` property offers more flexibility through additional values beyond the common left, right, center, and justify:

- **Match-parent**: This non-standard value, supported in newer browsers, aligns similarly to inherit but uses the parent's direction, resulting in a computed value of either left or right. For elements where the direction is explicitly defined, this can provide more consistent alignment across parent-child relationships.

For developers working with multiple alignment styles, several related properties enhance text layout:

- **line-height**: Controls the vertical spacing between lines of text, affecting readability and visual balance. Higher values increase spacing between lines, while lower values reduce it. The property is particularly useful when combined with `text-align` for improving content presentation.

- **word-spacing**: Adjusts the space between words, allowing for precise control over character-level spacing. This property can help with spacing issues in languages where words naturally have different lengths or visual weights.

Combining text alignment with background images offers additional design possibilities:

- Using background images in combination with `text-align` can create visually striking banners or headers. For example, a centered background image with aligned text can draw attention while maintaining visual hierarchy.

Finally, the `text-align-last` property provides specific control over the alignment of the last line of a paragraph or body of text:

- **auto**: The browser's default behavior, aligning the last line similarly to non-last lines.

- **left**: Aligns the last line to the left margin.

- **right**: Aligns the last line to the right margin.

- **center**: Centers the last line.

- **justify**: Distributes space evenly between words on the last line, similar to the full paragraph.

These additional properties and techniques allow for precise control over text layout, enabling developers to create complex and responsive typography designs while maintaining semantic structure and accessibility.

