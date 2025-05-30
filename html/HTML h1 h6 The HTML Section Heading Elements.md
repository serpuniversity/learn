---

title: HTML Section Heading Elements: `<h1>` to `<h6>`

date: 2025-05-29

---


# HTML Section Heading Elements: `<h1>` to `<h6>`

HTML heading elements are fundamental building blocks for creating well-structured and accessible web content. The six available heading levels, from h1 to h6, enable developers to establish a clear hierarchy that enhances readability while providing essential semantic information to assistive technologies. Through browser-specific styling defaults and proper implementation techniques, these elements create visually distinct sections while maintaining compatibility across modern browsers. This article explores the best practices for using HTML headings, from fundamental structure and semantics to advanced features that enable complex document layouts while ensuring accessibility for all users.


## Overview of HTML Section Heading Elements

The six HTML heading elements (h1 to h6) create a structured hierarchy, with h1 representing the most important heading and h6 the least. This allows web developers to clearly indicate the importance and relationship between different sections of content.

Each heading level is automatically styled with browser-specific margin properties, ensuring that headings consistently stand out from regular text. For example, an h1 is displayed with a 1.33em margin (21.28px), while an h6 uses a 0.83em margin (13.28px). These margins help create proper spacing between headings and improve readability.


### Usage Guidelines

The recommended approach is to use only one h1 per page, typically reserved for the main title or primary heading. Subsequent content should use h2 for main sections, h3 for subsections, and so on, following this hierarchy: h1, h2, h3, h4, h5, h6. Skipping heading levels is discouraged, as it can confuse both users and assistive technologies.


### Semantic Considerations

While these elements generate substantial margin properties in browsers, developers should resist the temptation to use headings for styling purposes. For example, increasing font size through heading elements rather than CSS style attributes can lead to inconsistent results across different devices and browsers.


### Browser Support

All modern browsers including Google Chrome, Edge, Firefox, Opera, and Safari fully support these elements, maintaining consistent behavior across platforms. This widespread support makes the proper implementation of heading elements essential for cross-browser compatibility and accessibility.


## HTML Heading Structure and Usage Guidelines

The HTML heading structure should always follow a logical hierarchy, with each heading level representing a specific section of content. This ensures that both users and assistive technologies can easily navigate the document. For example, a newspaper article might use h1 for the main title, h2 for chapter titles, and h3 for subsections within those chapters.


### Nested Heading Structure

Headings can be nested to reflect the hierarchical organization of page content. However, skipping heading levels can create confusion for screen reader users, who rely on the proper sequence to understand the document structure. For instance, after an h2 heading, the next logical structure would be an h3, rather than directly returning to an h2 or h1.


### Best Practices for Use

The h1 tag should be used only once per page, typically for the main content title. Subsequent content should use h2 for main sections, h3 for subsections, and so on. This hierarchical structure helps both users and search engines understand the content's organization. Screen readers and other assistive technologies use headings to generate an ordered list of all headings on a page, allowing users to quickly navigate to specific sections.


### Technical Considerations

HTML heading tags are flow content, meaning they must contain phrasing content and cannot accept other block-level elements directly. While the align attribute is deprecated and should not be used, these elements automatically generate some white space (margin) before and after them when displayed. The size of each heading level is defined using em units, providing consistent rendering across different browsers and devices. For example, an h1 has a font size of 2em (32px), while an h6 has a font size of 1em (16px).


## HTML Heading Styling and Browser Support

Each heading element automatically generates browser-specific margin properties, ensuring consistent spacing between headings and regular text. Specifically, the `<h1>` element displays with a 1.33em margin (21.28px) above and below, while the `<h6>` element uses a 2.33em margin (37.28px) on both sides.

Default font sizes for each heading level adhere to a consistent pattern, with `<h1>` set at 2em (32px) and `<h6>` at 0.67em (10.72px). This progressive decrease in font size maintains visual hierarchy across the page while ensuring that headings remain easily readable.

While these elements generate default styling properties, developers can selectively override specific styles using the `margin` property. For instance, the `margin-block` property controls vertical spacing above and below each heading, allowing developers to maintain the semantic structure while adjusting layout as needed. The `font-size` property directly controls the heading's text size, providing flexibility for responsive design adaptations.


## Accessibility Considerations for HTML Headings

The role of HTML headings extends beyond visual design, playing a crucial part in how both users and assistive technologies navigate web content. Screen readers, in particular, rely on these elements to generate an ordered list of all headings on a page, allowing users to quickly locate specific sections.

Visually impaired users face significant challenges when headings are missing or improperly structured. Without proper heading elements, they must listen to the entire document, which can be time-consuming and frustrating. This underscores the importance of using headings to break up content into logical sections that assistive technology can effectively navigate.


### Content Structure and Navigation

Screen readers use heading structure to determine content hierarchy, announcing each heading as users navigate through the document. This enables users to understand the document's structure and quickly locate specific sections. For example, when reading a newspaper story, a screen reader user should be able to hear "Story Title" followed by "Chapter 1," "Chapter 2," and so on, rather than a continuous stream of text.


### Technical Implementation

To ensure effective accessibility, HTML heading tags should be implemented correctly without relying on visual cues alone. While it's possible to create visually impressive headings using CSS, this approach removes the semantic value that makes heading elements valuable for accessibility. The proper way to create headings is through the appropriate HTML tags, as demonstrated in the live example from the MDN documentation.

Each heading should represent a specific section of content, with the hierarchy structured logically. The example provided shows how multiple sectioning elements can be labeled using ARIA attributes, helping users understand the page structure even when headings are missing. However, it's important to note that these techniques should be used sparingly and only when necessary, as proper heading structure serves the same purpose more effectively.


## Advanced HTML Heading Features

The HTML heading system supports custom element declarations beyond the standard six levels, although browser compatibility and implementation vary. For documents requiring headings beyond h6, developers have several options:


### Custom Heading Levels

While HTML5 allows declaration of custom heading elements like h7, this approach may cause issues in older browsers, particularly Internet Explorer versions prior to 11. These custom elements function technically, but may not render correctly or be properly interpreted by assistive technologies.

HTML5's recommendation for deeper heading hierarchies is to use `div` elements with class attributes rather than custom heading tags. This approach maintains semantic integrity while providing the necessary structure for complex documents. For example, to style content as h7 while maintaining semantic clarity, developers can use:

```html

<style>

  .h7 { font-weight: bold; margin-top: 1em; }

</style>

<div class="h7">Some text</div>

```


### Semantic Structure with Hierarchy

For documents where the standard six levels are insufficient, HTML5 introduces `section` elements to define deeper nesting structures. When using this approach, each additional level of `section` nesting increments the heading level: at the 7th level of nesting, an h1 would effectively become a 7th level heading.

However, implementing deeper nesting requires additional considerations. To enable these features in older versions of Internet Explorer, developers must include the following script:

```html

<script>

  document.createElement('section')

</script>

```

along with appropriate CSS rules:

```css

section { display: block; }

```


### Implementation Best Practices

Developers are advised to use custom heading levels with caution, particularly for content requiring deeper hierarchy. For most documents, the standard six levels (h1 to h6) provide sufficient structure while maintaining compatibility across modern browsers and assistive technologies.

The recommended approach for styling content at or beyond h6 level is to use `div` elements with class attributes, combining semantic clarity with flexible styling options. This method ensures that content remains fully accessible and maintainable, while providing the necessary structure for complex document layouts.

