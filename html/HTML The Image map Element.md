---

title: HTML Image Maps: Interactive Regional Linking

date: 2025-05-29

---


# HTML Image Maps: Interactive Regional Linking

Image maps transform static graphics into interactive elements, allowing users to click on specific areas for direct navigation. Whether you're adding a complex floor plan or simply pointing to a company logo, understanding how to implement these clickable regions is crucial for modern web development. This guide walks you through the fundamentals of HTML image maps, from basic syntax to advanced implementation techniques, ensuring your interactive elements are both functional and accessible.


## Image Map Fundamentals

The HTML Image Map element enables the creation of interactive image regions through a combination of `<map>` and `<area>` tags. The `<map>` element defines an image map, while `<area>` tags create the individual clickable spots within that map.

Each `<area>` tag specifies its shape (rectangular, circular, or polygonal) and coordinates relative to the image's top-left corner using the coords attribute. The shape attribute determines the region's shape, with options including "rect" for rectangles, "circle" for circles, and "poly" for polygons. The coords values define the specific location of each clickable region.

The `<area>` tag supports several key attributes:

- Shape: Determines the region's shape (rect, circle, poly)

- Coords: Specifies the coordinates for the shape (required)

- Href: Defines the link destination for the clickable region

- Alt: Provides alternative text for accessibility (required for `<area>` elements)

For example, a rectangular clickable area would use the following syntax:

<area shape="rect" coords="34,44,270,350" href="page1.html" alt="Rectangle Link"

Circle areas would be defined similarly:

<area shape="circle" coords="140,75,50" href="page2.html" alt="Circle Link"

The `<area>` tag supports additional attributes common to hyperlinks, including alt for alternative text, href for the link destination, target for navigation, and download for file downloads. When an `<area>` has no href attribute, it functions as an exclusive clickable region, making the entire area selectable rather than just the defined coordinates.

The `<map>` element requires a name attribute that matches the usemap attribute in the `<img>` tag. This creates a relationship between the image and the associated map. The `<map>` element can contain various elements, though `<area>` tags are the primary content. The order of `<area>` elements affects tab focus order and stacking, with later areas appearing beneath previous ones, which is crucial for creating exclusive hotspot regions.


## Basic Syntax and Structure

The `<map>` element, combined with `<img>` and `<area>` tags, creates interactive image maps where specific regions function as clickable links. The `<map>` element defines an image map with a required "name" attribute that matches the "usemap" attribute in `<img>` tags, establishing the relationship between the image and its associated map.

Clickable areas are defined using `<area>` tags, which support three basic shapes: rectangular ("rect"), circular ("circle"), and polygonal ("poly"). Each shape requires different coordinate specifications:

- Rectangles need four coordinates: top-left (x1, y1) and bottom-right (x2, y2) corners

- Circles require three values: center (x, y) and radius

- Polygons use multiple coordinate pairs to define each point of the shape

The `<area>` tag supports several key attributes for each clickable region:

- Shape: Determines the region's shape (rect, circle, poly)

- Coords: Specifies the coordinates for the shape (required)

- Href: Defines the link destination for the clickable region

- Alt: Provides alternative text for accessibility (required)

To create a basic image map, developers combine an `<img>` element with a `<map>` element containing multiple `<area>` tags, each defining a different clickable region. The `<map>` element's "name" attribute must match the "usemap" attribute in the `<img>` tag, establishing the connection between the image and its associated map.


## Clickable Area Shapes

The `<area>` element defines clickable regions within images, supporting three fundamental shapes: rectangles, circles, and polygons. Each shape requires specific coordinate specifications to establish its position and size within the image.


### Rectangle Shape

For rectangular areas, the coords attribute takes four values: the top-left (x1, y1) and bottom-right (x2, y2) corners of the rectangle. For example, coordinates 34,44,270,350 define a clickable rectangle from 34 pixels from the left edge and 44 pixels from the top edge to 270 pixels from the left edge and 350 pixels from the top edge.


### Circle Shape

Circles require three values in the coords attribute: the center coordinates (x, y) followed by the radius value. For instance, coordinates 140,75,50 create a circle centered at 140 pixels from the left edge and 75 pixels from the top edge with a radius of 50 pixels.


### Polygon Shape

Polygons use multiple coordinate pairs to define their edges, with the last coordinate pair automatically closing the shape. For example, coordinates 150,100,200,200,250,100,200,0 create a triangle with vertices at (150,100), (200,200), and (250,100). The even-odd rule determines if a point is inside the polygon, ensuring accurate clickable regions.

Each area shape supports common hyperlink attributes including alt text for accessibility, href to specify the link destination, and target to control how the linked page opens. These attributes enhance both functionality and usability across various web interactions.


## Coordinate Systems and Placement

Image maps function through a combination of `<img>`, `<map>`, and `<area>` elements that work together to create interactive regions on an image. The positioning of these areas significantly impacts their functionality and the overall usability of the image map.

The `<area>` element defines clickable regions using shapes like rectangles, circles, and polygons. Each shape requires specific coordinate specifications: rectangles need top-left (x1, y1) and bottom-right (x2, y2) corners, circles need center (x, y) and radius, and polygons use multiple coordinate pairs to define vertices.

A key aspect of area positioning is stacking order, determined by the sequence of `<area>` elements within the `<map>`. The last defined area appears beneath previous ones, which is crucial for creating exclusive hotspot regions. For example, if a circular area is defined after a rectangular one, the circle will not be clickable if it overlaps the rectangle because the rectangle's coordinates fully contain the circle's area.

The Image Map element's coordinate system positions shapes relative to the top-left corner of the associated image. This absolute placement requires careful consideration when implementing responsive designs, as image resizing changes pixel dimensions. While basic image maps scale with their containing elements, creating responsive maps often requires JavaScript solutions to dynamically adjust coordinates based on image dimensions.

The `<usemap>` attribute in the `<img>` tag establishes the relationship between the image and its associated map. When implementing responsive designs, developers must account for how image resizing affects area coordinates. For instance, if an image changes size, the coordinates of clickable regions must be recalculated to maintain proper placement and functionality.


### Best Practices

To ensure effective image map implementation:

- Use descriptive alt text for both the image and each clickable area

- Order `<area>` elements based on their visual placement to control stacking

- Use JavaScript for responsive design when basic HTML scaling is insufficient

- Test area coordinates thoroughly to maintain proper click functionality across different screen sizes


## Accessibility and Best Practices

The `<area>` element's alt attribute plays a crucial role in providing alternative text for both visual and non-visual users. This attribute combines with other map elements to offer user choice, similar to how `<a>` elements provide alternative text through their own alt attributes. While the requirement for alt text is explicitly stated for `<area>` elements with href attributes, best practice recommends including it for all `<area>` elements to ensure comprehensive accessibility coverage.

The alt attribute serves dual purposes in image maps - acting as both a screen reader description for visually impaired users and a link descriptor for web crawlers. This dual functionality aligns with its counterpart in `<a>` elements, where the attribute specifies the link destination while also providing context for users who cannot see the image. For developers creating interactive image maps, including descriptive alt text becomes essential for maintaining accessibility standards across different user groups.

The HTML standard clearly mandates that the `<area>` element must contain an alt attribute when representing a hyperlink, with this text providing the same choice as the hyperlink would in a text-only environment. The attribute's importance is further underscored by its requirement when defining clickable areas, ensuring that web content remains accessible even when images fail to load. This attribute-driven approach mirrors the broader web accessibility principles established for standard hyperlink implementation, maintaining consistency in how web developers address content accessibility through structured markup.

## References

- [HTML The HTML Select Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20HTML%20Select%20Element.md)
- [HTML The Document Title Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Document%20Title%20Element.md)
- [HTML Small The Side Comment Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Small%20The%20Side%20Comment%20Element.md)
- [HTML dt The Description Term Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20dt%20The%20Description%20Term%20Element.md)
- [HTML Date And Time Formats Used In HTML](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Date%20And%20Time%20Formats%20Used%20In%20HTML.md)