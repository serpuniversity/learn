---

title: HTML `<li>`: The List Item element

date: 2025-05-29

---


# HTML `<li>`: The List Item element

The li element is a fundamental building block of HTML lists, defining discrete items within unordered (ul) or ordered (ol) collections. This versatile element supports nested structures, custom styling, and responsive design principles, making it essential for creating structured content. Whether you're building navigation menus, product lists, or step-by-step instructions, understanding the capabilities and limitations of the li element is crucial for effective web development.


## li Element Basics

The li element defines a list item and must be contained within an unordered (ul) or ordered (ol) list, as well as in menu lists (menu). In ul and menu tags, list items are typically displayed with bullet points, while in ol tags, they are displayed with numbers or letters. Each li element can contain other li elements or any normal content, creating nested lists with adjusted marker styles (as stated in the HTML Standard documents).

The li element supports various attributes, including Global Attributes and Event Attributes as recognized by browser engines such as Firefox, Safari, Chrome, Opera, and Edge. It also supports the value attribute for ol lists, which specifies the start value of a list item (10), causing subsequent items to increment from that number (as documented in the li tag official HTML documentation). For ul and menu tags, the browser automatically announces how many items are in the list and keeps listeners informed of the current list item's position (Axe Rules documentation).

The `<li>` tag structure has several technical specifications defined in the HTML specifications:

- It requires at least one li element to be present when used in ul tags, providing block-level display styling with default properties including list-style-type: disc, margin-top: 1em, margin-bottom: 1em, margin-left: 0, margin-right: 0, and padding-left: 40px (from HTML UL tag documentation).

- The value attribute must be a valid integer and is used to determine the ordinal value of the list item, particularly when the li's list owner is an ol element (from the MDN Web Docs).

- The element supports semantic roles such as listitem when a child of ul, ol, or menu elements (MDN Web Docs specification).

The li element's compatibility across major browsers is robust, with full support in Firefox, Safari, Chrome, Opera, and Edge. It's important to note that while the type attribute was previously used to control numbering styles, it has been deprecated in favor of the CSS list-style-type property for consistent styling across different browsers and devices.


## Default Display and Styling

By default, li elements establish themselves as list items with browser-defined margins and list-style properties that adhere to the parent ul or ol structure. The default CSS styling for li elements, as specified in the HTML Standard documents, displays them with a block-level layout and applies properties including list-style-type: disc, margin-top: 1em, margin-bottom: 1em, margin-left: 0, margin-right: 0, and padding-left: 40px.

When nested within an ordered list (ol), li elements maintain the default list-style-type of disc for the outer unordered list while adopting square markers for the nested structure, demonstrating the automatic adjustment of marker styles according to their hierarchical position (as shown in the Creating Lists guide by Shay Howe).

The element's inherent display properties make it particularly useful for creating structured content, such as navigation menus, where flow content can be styled horizontally through CSS, either by setting display properties to inline or inline-block for list items (li), or employing floating techniques to position items side-by-side while maintaining their marker visibility (as demonstrated in the Creating Lists guide by Shay Howe).

The combination of inherent styling and structural capabilities makes the li element a versatile foundation for organized web content presentation, adaptable through CSS for both basic and complex list structures.


## List Item Markers

The marker style can be customized using the list-style-type property, which supports several options including disc, circle, square, and custom images. The property can be applied to `<ul>`, `<ol>`, or `<li>` elements.

For custom list item markers, the list-style-type value is set to none, and the `<li>` element's background property specifies the image, position, and repeat. Padding-left creates space for the background image. The default list style positioning is outside, placing markers to the left of content. The list-style-position property allows customization to inside or inherit. Inside places markers in line with the first line of content, while outside keeps content to the right of markers.

The list-style shorthand property combines list-style-type and list-style-position into a single value, offering flexible styling options. As of 2020, most modern browsers support the ::marker pseudo-element for custom list markers, with the exception of Opera. For browsers that don't support ::marker, developers can use alternative methods such as li:before with content: "" and inline-block display, or apply color styles directly to the `<li>` items.

The color styles affect all `<li>` content, including the bullets. A common approach is to use the list-style-image property with an image of a colored bullet, though this requires using images. Another option is to use `<span>` elements, which work cross-browser including Internet Explorer and provide control over text and bullet size, though this is considered less elegant.


## Nested Lists

HTML allows for the creation of nested lists through the use of `<ul>` and `<ol>` elements within `<li>` elements, maintaining proper hierarchical marker styles. Each `<li>` can contain any normal element, including other `<ul>` or `<ol>` elements, enabling complex list structures. When a nested list begins within an `<li>`, it must properly close before continuing the original list (Shay Howe's Creating Lists guide).

The marker styles adjust automatically based on nesting depth. For example, an unordered list nested within an ordered list uses hollow circles instead of solid discs, as the unordered list is one level deep (Shay Howe's Creating Lists guide). This automatic styling is consistently applied across modern browsers, with `<li>` elements maintaining their list-item display properties regardless of nesting level.


## Styling Considerations

To address the specific challenge of setting bullet colors, developers have multiple effective approaches. The first method employs CSS's `:before` pseudo-element combined with `border-radius` for a clean, cross-browser compatible solution. This technique uses the `em` unit for responsiveness, making it adaptable to font size changes while remaining fully supported in IE 8 and later browsers.

An alternative approach utilizes the basic color property directly on the `<li>` element, although this method affects both the bullet and text color. For developers requiring precise control without additional element usage, setting `list-style-image` to a colored bullet image is an option, though it requires incorporating images into the design.

Modern CSS solutions should avoid wrapping list items in span elements, as this practice is considered less elegant while achieving similar results. By directly styling list items with colors while maintaining proper list styling through global attributes, developers can create visually styled navigation menus that remain adaptable to future changes in browser standards and design requirements.

