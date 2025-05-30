---

title: Add a Hitmap on Top of an Image

date: 2025-05-29

---


# Add a Hitmap on Top of an Image

Interactive images, where specific regions serve as clickable hotspots, combine functional usability with visual storytelling. From simple image maps to sophisticated heatmaps, this article explores the technical implementation and practical applications of these interactive elements. We'll start with the basics of image mapping, including rectangular, circular, and polygonal areas, and then build up to advanced techniques like responsive design and data visualization. By the end, you'll understand how to create interactive images that enhance user experience while providing valuable information through visual overlays and data representations.


## Basic Image Map

The HTML image map system creates interactive regions within an image using the `<img>` tag with the `usemap` attribute, which links to a map defined with the `<map>` tag containing `<area>` elements. This structure allows precise definition of clickable areas through the use of different shapes - rectangular (`rect`), circular (`circle`), and polygonal (`poly`) regions.

Each clickable area is defined within the `<map>` tag using the `<area>` element, which requires several key attributes:

- `shape`: Defines the shape of the clickable area, using values like "rect", "circle", or "poly".

- `coords`: Specifies the coordinates of the area, formatted differently based on the shape:

  - For rectangles, this is a pair of coordinates representing the upper-left and bottom-right corners (e.g., "34,44,270,350").

  - For circles, this is the center's x and y coordinates followed by the radius (e.g., "337,300,44").

  - For polygons, this is a series of x and y coordinates for each vertex (e.g., "140,121,181,116,...").

The `href` attribute provides the destination URL or JavaScript action for each clickable area, with an optional `alt` attribute for accessibility purposes. The process also requires matching the `usemap` attribute in the `<img>` tag with the `name` attribute in the `<map>` element for proper association.

Implementing these elements results in an interactive image where specific regions can link to different resources, with coordinates defined relative to the image's own dimensions in CSS pixels. This system forms the basis for more advanced heatmap functionality, combining these basic image map elements with additional layers of information to create dynamic, data-driven visualizations.


## Detailed Shape Coordinates

The HTML `<area>` element defines clickable regions within an image, supporting rectangular, circular, and polygonal shapes. Coordinates for these regions are defined using pixel values relative to the image's dimensions, allowing precise placement of interactive elements.

For rectangular areas, coordinates represent pairs of x-y positions for the upper-left and bottom-right corners. For example, coordinates "34,44,270,350" define a rectangle 236 pixels wide and 306 pixels tall, starting 34 pixels from the left and 44 pixels from the top of the image.

Circular areas require specifying the center's x and y coordinates followed by the radius. The example "337,300,44" creates a circle with its center at 337 pixels from the left and 300 pixels from the top, having a radius of 44 pixels.

Polygonal areas can create any shape using a series of x-y coordinates for each vertex. The provided example demonstrates a complex polygon with multiple vertices, allowing for intricate hotspot definitions.

Each clickable area includes additional attributes beyond coordinates:

- `shape`: Defines the shape type (rect, circle, poly)

- `href`: Specifies the URL or JavaScript action for the hotspot

- `alt`: Provides alternative text for accessibility (optional)

Implementers should ensure coordinates match the image's dimensions exactly, with pixel values representing precise positions on the image. This system forms the basis for more sophisticated image interactions, including those requiring multiple overlapping hotspots or dynamic positioning.


## Background Image Overlay

To overlay an image on top of a generated heatmap, developers use the CSS `::after` pseudo-element on elements with the id "heatmap". This approach allows precise control over the overlay's positioning and appearance while maintaining separation between content and presentation.

The pseudo-element requires several key CSS properties for proper display:

- `position: absolute` establishes the overlay's positioning context

- `top` and `left` properties align the overlay with the parent element

- `width` and `height` set the overlay to 100% of the parent's dimensions

- A higher `z-index` ensures the overlay appears above the heatmap

- `background-image` sets the image URL, with `background-size: cover` or `contain` for scaling

- `background-repeat: no-repeat` prevents image tiling

- `background-position: center center` centers the image within the overlay

For optimal display, the heatmap element must be correctly positioned as the pseudo-element uses its dimensions for alignment. This technique enables developers to create complex overlays without modifying the underlying HTML structure, maintaining clean separation of concerns between content and presentation.


## Responsive Image Mapping

Responsive design challenges require careful consideration of image map performance and accessibility implications. Multiple image instances referencing the same map can lead to unpredictable behavior across browsers. Safari and Chromium-based browsers skip later image instances entirely during keyboard navigation, while Firefox activates all image maps simultaneously, making it difficult for users to reach the intended targets.

Best practices emphasize text links over image maps due to their lighter weight, better maintainability, and enhanced accessibility. For interactive image maps, the recommended minimum size is 72 x 72 CSS pixels, with generous gaps between touch targets to prevent accidental clicks. The example from 50languages.com demonstrates this limitation, where users find it much easier to tap large regions like Russia or North America compared to smaller areas like Albania or Estonia.


## Advanced Heatmap Integration

The Heatmap Layer from the Google Maps JavaScript API provides client-side rendering of heatmaps, creating colored overlays on top of maps with red representing higher intensity and green representing lower intensity. To enable this functionality, developers must include the `visualization` library in their Maps JavaScript API bootstrap URL.

Data is added to the heatmap using `LatLng` or `WeightedLocation` objects within an array or `MVCArray[]` object. For example, 14 data points can be added to a San Francisco map using an array of `LatLng` objects, with the map centered on San Francisco and set to a zoom level of 13 with satellite view.

The implementation process involves creating a new `HeatmapLayer` object and adding it to the map using the `setMap()` method. The provided documentation includes a complete example demonstrating how to center the map on San Francisco, create a HeatmapLayer with specified data, and display it on the map.

The heatmap functionality has expanded beyond traditional map layers to integrate with image overlays. The Cloudinary blog features a React application that allows users to create heatmaps on images, using a 1024-pixel gradient map to represent alpha values from data points. The application supports positioning heatmaps in four locations: top-left, top-right, bottom-left, and bottom-right.

For developers looking to create custom heatmap visualizations, resources are available through multiple JavaScript libraries. The AnyChart library provides a comprehensive solution, as demonstrated in the documentation for creating interactive heatmaps. Basic implementation requires including AnyChart core and heatmap modules, organizing data with an `x` value for each point, and rendering the chart within an HTML container.

When integrating heatmaps with image overlays, considerations must be given to the underlying image dimensions and the transparency effect. The example from the Cloudinary blog uses random data points to create a visualization, while other implementations focus on applying alpha values to a gradient map for color representation. This approach requires careful handling of alpha blending to produce accurate visualizations.

