---

title: Pure-CSS Tooltips with HTML and CSS

date: 2025-05-26

---


# Pure-CSS Tooltips with HTML and CSS

In today's digital age, providing immediate feedback and enhancing user experience through interactive elements is crucial for any website or application. While traditional methods like JavaScript tooltips offer extensive functionality, they add complexity and potentially degrade performance. This article explores a pure-CSS approach to creating interactive tooltips, demonstrating how basic HTML and CSS can transform simple text into informative, interactive elements that enhance user interactions without requiring additional scripting. From basic placement to advanced animations, we'll uncover how these seemingly simple techniques can significantly improve how users interact with web content.


## Basic Tooltip Structure

The tooltip is created using a single <div> element with a class of "tooltip". This container holds the tooltip text within a nested <span> element:

```html

<div class="tooltip">Hover over me <span class="tooltiptext">Tooltip text</span></div>

```

The CSS styling for this basic tooltip requires the parent element to have `position: relative` and a dotted black border-bottom. The tooltip text itself requires additional properties:

```css

.tooltip {

  position: relative;

  border-bottom: 1px dotted #000;

}

.tooltip .tooltiptext {

  visibility: hidden;

  width: 120px;

  background-color: #555;

  color: #fff;

  text-align: center;

  padding: 5px 0;

  border-radius: 6px;

  position: absolute;

  z-index: 1;

  bottom: 100%;

  left: 50%;

  margin-left: -60px; /* centers the tooltip */

}

/* Additional styles for arrow */

.tooltip::after {

  content: "";

  position: absolute;

  top: 100%;

  left: 50%;

  margin-left: -5px;

  border-width: 5px;

  border-style: solid;

  border-color: #555 transparent transparent transparent;

}

```

The tooltip text is initially hidden with `visibility: hidden`, but becomes visible on hover. The positioning uses a combination of absolute positioning and margin adjustments to center the tooltip vertically while keeping it anchored below the hoverable text.

For right or left alignment, the positioning changes slightly. Right-aligned tooltips use `top: 105%` and `left: 105%`, while left-aligned versions use `right: 105%` instead of `left`. Top-aligned tooltips use `bottom: 100%`, while bottom-aligned versions maintain `top: 105%`.

These basic styles provide a foundation for customizable tooltips, though more complex designs may require additional CSS adjustments.


## Tooltip Text Positioning

Tooltips can be positioned in multiple directions depending on the desired layout. For top placement, both horizontal and vertical distances from the target element are controlled using percentages. The vertical positioning uses `top: 105%` while keeping `left: 10%` to place the tooltip to the left of the hoverable text. 

For bottom placement, similar percentages are used but with the `top: 105%` and `left: 10%` swapped to position the tooltip above and to the left of the text. The text notes that the value of "x" determines the horizontal distance from the container's top, while "y" controls the vertical distance from the container's left end.

The arrow functionality demonstrates how CSS pseudo-elements can create distinct visual effects. The arrow's position is calculated using percentages relative to the tooltip's dimensions, allowing it to touch the tooltip when "x" is zero and remain centered when "y" is 50.

Left positioning uses absolute positioning with `top: 100%` and `left: 50%`, applying `transform: translateX(-50%)` to center the tooltip horizontally while placing it to the left of the target element. Right positioning mirrors these properties but applies them to the right side instead, making it particularly useful when horizontal space is limited and tooltip overlap should be avoided.

These positioning methods can be applied through various HTML and CSS implementations. For example, one approach uses empty content pseudo-elements with specific border properties to create triangle shapes. The tooltip container's positioning requires careful management of margins and transforms to achieve precise placement.


## Tooltip Arrow Implementation

The tooltip arrow is created using border properties and pseudo-elements, with each arrow direction requiring specific positioning and styling:

For bottom arrows, the pseudo-element `::after` is styled with:

- `content: " "; position: absolute`

- `top: 100%`, `left: 50%`

- `margin-left: -5px`

- `border-width: 5px`

- `border-style: solid`

The black arrow is created with `border-color: black transparent transparent transparent`.

For top arrows, the pseudo-element `::after` is styled similarly but with:

- `bottom: 100%`, `left: 50%`

The black arrow is created with `border-color: transparent transparent black transparent`.

The left arrow pseudo-element `::after` is styled with:

- `top: 50%`, `right: 100%`

- `margin-top: -5px`

The black arrow is created with `border-color: transparent black transparent transparent`.

The right arrow pseudo-element `::after` is styled with:

- `top: 50%`, `left: 100%`

- `margin-top: -5px`

The black arrow is created with `border-color: transparent transparent transparent black`.

The tooltip container uses absolute positioning with `z-index: 1`, positioned based on target element's position:

- Bottom arrows: `bottom: 120%`, `left: 50%`, `margin-left: -75px`

- Top arrows: `top: 100%`, `left: 50%`, `margin-left: -75px`

The tooltip text displays with:

- `position: absolute`

- `left: 50%`, `transform: translateX(-50%)`

- `margin: 10px` (top/bottom), `10px` (left/right)

- `width: 120px`

- `padding: 5px`

- `border-radius: 6px`

- `background-color: #333`

- `color: #fff`

- `text-align: center`

- `display: none` (hidden by default)


## Tooltip Display and Animation

The tooltip's visibility is controlled through a combination of CSS properties and pseudo-elements. The tooltip text is initially hidden with `visibility: hidden`, while the entire tooltip container has an initial opacity of 0. On hover, both the text and its wrapper display using `display: block`.

The text becomes visible through transitions defined with `transition: opacity 0.3s`, where the opacity changes from 0 to 1 over 0.3 seconds. This creates a smooth fade-in effect for the tooltip content. For bottom-aligned tooltips, the display properties adjust the positioning to `bottom: 120%` of the parent height and `left: 50%`, with a horizontal margin of `-75px` to center the tooltip.

The tooltip arrow, created using a border trick, also transitions its visibility on hover. The pseudo-element uses a `border-width` of 5px and `border-style: solid`, with the border color set to the tooltip's background color and transparent for all sides except the bottom. This creates a clean, black arrow tip when the tooltip is visible.

For left-aligned tooltips, the positioning changes to `right: 100%` with a similar margin adjustment. Right-aligned versions use `left: 100%` instead. The arrow positioning remains consistent, using top: 50% and margin-top: -5px to center it vertically. The transition behavior ensures a smooth appearance even when the tooltip overlaps with other elements, using a `transition-delay` of 100ms to prevent abrupt changes when skimming over the display area.

This implementation approach allows tooltips to function correctly with interactive elements like buttons and links, providing clear, on-demand information to users while maintaining a clean interface design.


## Optimizing Tooltip Performance

The CSS tooltip approach often conflicts with browser title attribute behavior, particularly in older versions like Opera 9.5b. Most modern browsers display both the custom tooltip and the default browser tooltip simultaneously when hovering over an element, rendering the custom tooltip invisible. This occurs because both the custom tooltip and the browser's title attribute seek to display information, leading to overlapping content.

A common workaround involves moving the tooltip text from the title attribute to a custom HTML element, which requires CSS2 compatibility. However, this method creates another issue: browsers currently support the title attribute semantically, making alternative solutions necessary. Future working drafts of XHTML 2.0 may introduce new attributes suitable for this method, potentially allowing better separation of content and style while maintaining browser compatibility.

James Hopkins' alternative solution addresses these challenges by using CSS3 pseudo-elements and styling with z-index and position properties. This approach works in modern browsers above IE7 while maintaining compatibility with default browser rendering of title attributes. Implementation involves setting up the HTML structure with div elements using the title attribute for CSS styling:

```html

<div title="Tooltip text for first div"></div>

<div title="Tooltip text for second div"></div>

```

The CSS styling includes setting `pointer-events` to `none` for the tooltip to remain visible while allowing underlying elements to be clickable. Transition behaviors require adjustments to prevent abrupt changes when hovering over the display area, with `transition-delay` of 100ms recommended to ensure smooth appearance while skimming over the display area.

Additional considerations for implementation include handling z-index layering issues with `position: absolute`, ensuring proper visibility control through `visibility: hidden` and `visibility: visible` instead of opacity transitions, and managing content display for elements like lists that require text input. These optimizations enable effective tooltip implementation while addressing critical display and accessibility concerns.

