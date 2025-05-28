---

title: CSS Float Clear

date: 2025-05-26

---


# CSS Float Clear

Managing float and clear properties in CSS is crucial for creating flexible, responsive layouts where content needs to interweave in specific ways. Whether you're trying to get text to flow around an image or ensure multiple floated elements stack properly, mastering these properties can transform basic webpage elements into a sophisticated, multi-column design system. This article breaks down the fundamentals of float and clear, showing you exactly how these properties work together to control the layout of your web pages – from simple two-column designs to complex multi-level float structures.


## CSS Float and Clear Properties

The CSS float property controls how an element positions itself within its container, allowing content to wrap around it. By default, elements are non-floating, meaning they occupy their natural position in the document flow. To position an element, you can set its float property to left or right. For example, an image with float: left will move to the left side of its container while text wraps around it.

The clear property determines how subsequent elements interact with floated elements. It controls whether an element floats next to a floated item or remains below it. The property accepts values of left, right, or both, each affecting how elements interact with float properties.

For instance, consider two div elements: one floated left and another following it. If the second div has a clear: left value, it will position below the first div, creating a new baseline. The clear property works by creating an invisible bar at the top of the cleared element that extends to the side defined by the clear value, forcing the element to wrap below anything the bar hits.

When applied to floating elements, the clear property influences the position of later floats, ensuring they do not overlap. For example, applying clear: both to an element ensures it clears any preceding left and right floats, positioning it below all floated elements.

In practical applications, these properties are essential for building responsive layouts where content needs to wrap around other elements. Understanding how float and clear interact allows developers to create complex, multi-column layouts with precise control over element placement.


## How Float and Clear Work Together

The float property controls an element's positioning, while the clear property manages how elements interact with floating content. When an element is floated, subsequent content will wrap around it on the opposite side, unless cleared.

The clear property applies to both floating and non-floating elements. For non-floated blocks, the property shifts the element's border edge down past any preceding floats, collapsing vertical margins if applicable. When applied to floating elements, it controls their stacking order—later floats cannot position higher than earlier ones.

The property accepts several values: none (default), left, right, both, inline-start, and inline-end. Matching these values ensures proper element positioning. For example, applying clear: left to an element ensures it appears below preceding left-floated elements.

Common clearing techniques include traditional methods like adding empty divs with `clear: both;` or using br tags with the same property. Modern approaches recommend creating clearfix elements with `overflow: auto;` or using pseudo-elements like `.clearfix::after { content: ""; clear: both; display: table; }`. These techniques address common float clearing issues while maintaining semantic structure.


## Clear Values and Their Effects

The clear property allows precise control over how elements interact with floating content. It accepts several keyword values: none (default), left, right, both, inline-start, and inline-end. The property works by creating an invisible bar at the top of the element that extends to the side defined by the clear value, forcing subsequent elements to wrap below this bar.

The property's default value (none) allows elements to wrap around floating content, while specifying left or right prevents wrapping only for the respective float direction. Using both ensures clearing from both sides, matching the float direction. For example, applying clear: both to an element positioned after left-floated divs will force it to appear below all preceding left floats.

The MDN Web Docs provide an example demonstrating these effects: without clear: both, a paragraph wraps around adjacent floating divs, while the next division wraps after the paragraph. Applying clear: both ensures the paragraph no longer wraps around the floating divs. This property applies to block-level elements, with inline and inline-block elements not supporting clear: both.

The clearfix technique effectively resolves containing issues by setting the parent element's overflow property to auto. Traditional methods include adding empty divs with clear: both or using br tags with the same property. Modern approaches, recommended by most web development standards, use the ::after pseudo-element with content: "", clear: both, and display: table properties. This method remains effective in modern web development while maintaining semantic structure.


## Modern Clearfix Techniques

The evolution of CSS float clearing has seen a shift from traditional methods like adding empty divs or using br tags to more efficient solutions. Modern approaches recommend using the clearfix technique, which employs pseudo-elements for cleaner code. This technique, as recommended by the Web Docs, utilizes the ::after pseudo-element with content: "", clear: both, and display: table properties. While this method has proven effective, it requires updating thousands of lines of code in Internet Explorer 10 to ensure proper functionality.

For developers looking for a reliable alternative, the voodoo method offers a simpler solution. This approach uses a combination of display: block, clear: both, and minimal styling to achieve float clearing. The method requires careful application to avoid creating unwanted gaps, particularly when used with float properties. However, when combined with appropriate margin and padding adjustments, it provides an efficient clear solution.

Both the clearfix and voodoo methods have evolved from earlier techniques that utilized overflow: auto. While these older methods remain functional, modern best practices recommend maintaining semantic structure and avoiding unnecessary markup. This includes using empty divs or clearfix classes solely for float clearing, opting instead for more targeted solutions where possible.


## Implementing Clear in CSS Layout

The most reliable modern method for clearing floats is the clearfix technique, which evolved from earlier solutions like adding empty divs or using br tags. The recommended approach uses a pseudo-element with the following CSS:

```css

.clearfix::after {

  content: "";

  display: table;

  clear: both;

}

```

This method effectively resolves containing issues while maintaining semantic structure. For developers transitioning from older techniques, updating code to use this method requires minimal changes across thousands of lines in Internet Explorer 10.

While traditional methods like adding empty divs with clear: both or using br tags with the same property remain functional, modern best practices recommend maintaining semantic structure and avoiding unnecessary markup. Instead of using unrelated elements like br tags or divs with clearfix classes for float clearing, developers are advised to maintain semantic structure and avoid creating unwanted gaps.

 floated elements. Common clearfix implementations include:

1. jQuery UI's `ui-help-clearfix` class, which performs a similar function.

2. A wrapper element with a hidden overflow:

```css

.floatWrapper {

  overflow: hidden;

  width: 100%;

  height: 100%;

}

```

3. The modern micro clearfix:

```css

.clearfix {

  *zoom: 1;

}

.clearfix::after {

  content: "";

  display: table;

  clear: both;

}

```

When implementing clear in CSS layouts, it's important to consider the containing element's height. If all child elements are floated, the parent element may collapse in height. To prevent this, the parent element should have its display property set to flow-root, or an empty div with clear: both can be added after the floated elements to force the parent to contain its children properly.

For developers using multiple float directions, the clearfix technique remains the most maintainable solution. While the voodoo method using display: block and clear: both may work in simpler cases, it requires careful application to avoid unintended margin gaps, particularly when combined with float properties.

