---

title: The Marquee Element

date: 2025-05-29

---


# The Marquee Element

The Marquee element represents one of the more distinctive vestiges of early web development history—a visual gimmick that once animated scrolling text across web pages. Developed during the competitive browser war between Microsoft's Internet Explorer and Netscape Navigator, the element's functionality remains surprisingly straightforward: it creates scrolling text or images within a defined area. However, its technical limitations and poor accessibility have relegated it to the annals of web development history. While modern browsers still support the element for backward compatibility, developers are strongly advised to seek alternative solutions that provide better control and accessibility.


## Marquee Element Overview

The Marquee element emerged during the early days of web browser competition, specifically within Microsoft's Internet Explorer environment around Netscape 4 and Internet Explorer 4. While its origins date back to these early browser wars, the element's inclusion in HTML specifications is noteworthy for being both unusual and ultimately unsuccessful.

The element's technical implementation followed a simple structure, allowing developers to insert scrolling text or images through straightforward HTML tags. Essential attributes included direction, width, height, and behavior, which provided basic control over the scrolling mechanism. The behavior attribute offered simple options for alternate scrolling or continuous looping, with support for additional parameters like scrollamount and scrolldelay to fine-tune the display.

Despite its widespread implementation across major browsers including Chrome, Edge, Firefox, Safari, and Opera, the Marquee element faced significant usability challenges. Common issues included text movement affecting clickable links, constant motion making complete content read inaccessible, and general eye fatigue for users who relied on static page layouts.

The element's departure from official HTML specifications occurred through incremental deprecation rather than sudden removal, with browsers continuing to support it for compatibility reasons. However, this legacy support is increasingly unreliable, particularly for features like alternate behavior and specific attribute values. Modern web development guidelines consistently recommend against use of the Marquee element, favoring CSS and JavaScript alternatives that offer greater control and compatibility across evolving web standards.


## Technical Specifications

The Marquee element creates scrolling text that can move from right to left, bottom to top, or bounce within specified dimensions. It supports various attributes including direction, width, height, behavior, and style properties.

Basic attributes control the flow and appearance of the scrolling content:

- direction sets the scroll movement (left, right, up, down)

- width and height define the scrolling area's dimensions

- bgcolor sets the background color of the scrolling area

- behavior determines the scrolling pattern (scroll, alternate)

Additional properties fine-tune the scrolling behavior:

- scrollamount controls the number of lines scrolled per second

- scrolldelay sets the delay between scroll actions in milliseconds

The element's internal CSS implementation uses transform and translate properties for movement effects. While the element has a documented DOM interface (HTMLMarqueeElement), its specification in HTML5 and Living Standard documents indicates it is considered obsolete.

Browser compatibility varies, with current support maintained primarily for legacy page compatibility rather than official standard implementation. Modern web development guidelines consistently recommend against using the Marquee element in favor of CSS and JavaScript alternatives that offer greater flexibility and compatibility across evolving web standards.


## Implementation Examples

The Marquee element supports three primary scrolling directions: left to right (default), right to left, and vertical (up or down). While the original implementation restricted direction to horizontal movement, modern browsers allow vertical scrolling through the direction attribute.

Basic usage requires only the opening and closing `<marquee>` tags, with content placed between them. Additional attributes control the scrolling behavior:

- direction: Specifies scrolling direction (left, right, up, down)

- height: Sets marquee height in pixels or percentage of window

- width: Sets marquee width in pixels or percentage of enclosing window

- bgcolor: Sets background color

- behavior: Controls scrolling type (scroll, slide, alternate)

- scrollamount: Sets display movement in pixels

- scrolldelay: Sets delay between displays in milliseconds

For vertical scrolling, developers can use direction="up" or direction="down". The element also supports spacing attributes:

- hspace: Sets horizontal space between marquee and surrounding content

- vspace: Sets vertical space between marquee and surrounding content


### Usage Examples

A simple horizontal marquee with basic attributes:

```html

<marquee direction="left" scrolldelay="100" scrollamount="3" behavior="alternate">

  The quick brown fox jumps over the lazy dog.

</marquee>

```

A vertical marquee with additional styling:

```html

<marquee direction="up" scrollamount="2" scrolldelay="50"

  style="height: 100px; width: 200px; background-color: #f0f0f0; color: #333;">

  Vertical scrolling text example.

</marquee>

```


### JavaScript Integration

While the Marquee element provides basic functionality, integrating JavaScript can offer more control and compatibility. The following example demonstrates how to achieve similar effects through JavaScript:

```html

<div id="marqueeContainer" style="width: 300px; overflow: hidden; border: 1px solid #000;">

  <div id="marqueeContent" style="white-space: nowrap;">

    The quick brown fox jumps over the lazy dog.

  </div>

</div>

<script>

const container = document.getElementById('marqueeContainer');

const content = document.getElementById('marqueeContent');

const width = container.offsetWidth;

const interval = 120;

function animateMarquee() {

  const scrollAmount = -width;

  content.style.transform = `translateX(${scrollAmount}px)`;

  container.style.animation = `marquee ${2 * interval}ms linear infinite`;

}

animateMarquee();

setInterval(() => content.style.transform = `translateX(0px)`, interval);

</script>

```

This JavaScript implementation offers greater control over scrolling behavior while maintaining compatibility across modern browsers.


## Alternatives and Best Practices


### CSS Implementation

Modern web development recommends using CSS for creating scrolling effects, and the Marquee element can be replicated with keyframe animations. The following example demonstrates a horizontal marquee using CSS3:

```css

@keyframes marquee {

  0% { transform: translateX(100%); }

  100% { transform: translateX(-100%); }

}

.marquee-container {

  white-space: nowrap;

  overflow: hidden;

  position: relative;

  animation: marquee 10s linear infinite;

}

.marquee-content {

  display: inline-block;

  background-color: #f0f0f0; /* Similar to bgcolor attribute */

  color: #333; /* Similar to text color control */

}

```


### Event-Based Control

The Marquee element supports event handlers for more dynamic control. The following example shows how to start and stop marquee movement using JavaScript:

```html

<div id="marqueeContent">The quick brown fox jumps over the lazy dog.</div>

<script>

const marquee = document.getElementById('marqueeContent');

// Start marquee

marquee.classList.add('marquee-active');

// Stop marquee on mouseover and resume on mouseout

marquee.addEventListener('mouseover', () => marquee.classList.remove('marquee-active'));

marquee.addEventListener('mouseout', () => marquee.classList.add('marquee-active'));

</script>

<style>

.marquee-active {

  animation-play-state: running;

}

@keyframes marquee {

  0% { transform: translateX(100%); }

  100% { transform: translateX(-100%); }

}

</style>

```


### JavaScript-based Alternatives

JavaScript libraries and plugins offer more advanced features while maintaining compatibility. The liMarquee plugin extends basic marquee functionality with enhanced controls:

```html

<li-marquee>

  <li-marquee-content>

    <p>The quick brown fox jumps over the lazy dog.</p>

  </li-marquee-content>

  <li-marquee-options>

    <li-marquee-parameter name="direction" value="right" />

    <li-marquee-parameter name="loop" value="infinite" />

    <li-marquee-parameter name="scrollamount" value="20" />

    <li-marquee-parameter name="scrolldelay" value="50" />

  </li-marquee-options>

</li-marquee>

```

This implementation demonstrates how JavaScript libraries can replicate Marquee's functionality more efficiently while adhering to web standards.


## Browser Compatibility and Future Outlook

As the marquee element has been officially deprecated in both HTML Living Standard and HTML5 specifications, its future in web standards is uncertain. The element's official documentation considers it experimental and subject to change, while browser support has become increasingly inconsistent.

While all major browsers including Chrome, Edge, Firefox, Safari, and Opera maintain basic support for backwards compatibility, implementation details vary significantly. Some browsers disregard height and width attributes, while others stop animation regardless of loop settings. Direction handling also produces inconsistent results across different platforms.

The element's legacy status has led to the abandonment of proposed CSS properties for Marquee Module Level 3, which were intended to standardize animation effects. Modern development practices consistently recommend alternative methods, with CSS keyframe animations and JavaScript libraries offering superior control and compatibility.

Developers should avoid using the marquee element in new projects, opting instead for contemporary approaches that align with evolving web standards and maintain user-friendly functionality across diverse devices and browsers.

