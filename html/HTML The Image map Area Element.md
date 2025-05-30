---

title: The Image Map Area Element: Creating Clickable Image Regions in HTML

date: 2025-05-29

---


# The Image Map Area Element: Creating Clickable Image Regions in HTML

Image maps transform static images into interactive elements, allowing users to navigate to different web pages or perform specific actions based on their clicks. By defining regions on an image, developers can create intuitive and engaging user interfaces for web applications. This comprehensive guide explores the technical implementation of image maps, from basic concepts to advanced features, helping web developers create accessible and responsive interactive content.


## Image Map Basics

The `<map>` element creates an image map, which is an image containing multiple clickable areas. An `<img>` tag references the image map using the usemap attribute, linking it to the map's unique name. The `<map>` element acts as a container for one or more `<area>` elements, each defining a clickable region on the image.

The `<area>` element supports three basic shapes: rect (rectangle), circle, and poly (polygon). For rectangular areas, the coords attribute requires two pairs of coordinates: the top-left and bottom-right corners. Circular areas need center coordinates and radius, while polygonal areas require a series of x,y coordinate pairs defining the shape's vertices.

Each `<area>` element can contain attributes for additional functionality, including:

- href: Specifies the URL to navigate to when the area is clicked

- alt: Provides alternative text for the clickable area

- shape: Defines the shape of the clickable region

- coords: Specifies the coordinates of the clickable region

- onclick: Triggers JavaScript functions when the area is clicked

For example, a clickable circle with center (123, 123) and radius 50 would be defined as:

```html

<area shape="circle" coords="123,123,50" href="circle-link.html" alt="Circle Link">

```

The `<area>` element is a self-closing tag and must be nested within a `<map>` element, which requires a name attribute to establish the image map's unique identifier. The `<map>` element is referenced in the `<img>` tag's usemap attribute.

For advanced implementations, the text provides an example of a polygonal area using the code:

```html

<area shape="poly" coords="x1,y1,x2,y2,x3,y3,..." href="link.html" alt="Polygon Link">

```

This allows developers to create complex shapes for interactive image regions.


## Defining Image Maps

The `<map>` element establishes a container for clickable areas, requiring a unique name attribute that matches the usemap attribute in the `<img>` tag referencing the image. The name attribute must:

- Have a non-empty value

- Contain no ASCII whitespace characters

- Not equal the name attribute of another `<map>` element in the same document

- Match any specified ID attribute

Each `<map>` element must contain one or more `<area>` tags, which define the shape, coordinates, and attributes of clickable regions. The `<area>` element supports three shape types:

- "rect" for rectangular areas: defined by two pairs of coordinates representing top-left and bottom-right corners

- "circle" for circular areas: defined by center coordinates and radius

- "poly" for polygonal areas: defined by a series of x,y coordinate pairs

A comprehensive example of an `<area>` element implementation demonstrates multiple shapes:

```html

<map name="planets_map">

  <area shape="rect" coords="0,0,82,126" href="sun.htm" alt="Sun">

  <area shape="circle" coords="90,58,3" href="mercury.htm" alt="Mercury">

  <area shape="circle" coords="124,58,8" href="venus.htm" alt="Venus">

</map>

```

This example creates a map with three regions: a rectangular area representing the sun, and circular areas for mercury and venus.

The `<map>` element accepts several global attributes, including class, dir, id, lang, style, and title, though most implementations utilize just the name attribute for defining image maps. The element also supports event attributes such as onclick, ondblclick, and onmouseover to trigger JavaScript actions based on user interactions.


## Area Element Properties

The `<area>` tag supports a wide range of attributes to create interactive image regions. The most fundamental attributes are shape, coords, href, and alt, each serving a specific purpose in defining clickable regions.

The `shape` attribute determines the type of clickable area, accepting three values: "rect" for rectangular areas, "circle" for circular areas, and "poly" for polygonal areas. For rectangular areas, the syntax requires four integer values representing the top-left and bottom-right corners: `x1,y1,x2,y2`. For circular areas, the attribute necessitates three numbers: the center coordinates followed by the radius (`x,y,radius`). Polygonal areas require a series of x,y coordinate pairs, with at least six integers total to define the vertices of the polygon.

The `coords` attribute works in conjunction with the shape attribute to specify the exact coordinates of the clickable area. It must contain a valid list of integers, with the format varying based on the shape attribute's value. Rectangular areas use two pairs of coordinates, while circular areas need three integers (center coordinates and radius). Polygonal areas require pairs of x and y values representing the vertices of the desired shape.

The `href` attribute specifies the URL to navigate to when the area is clicked, while the `alt` attribute provides alternative text for the clickable region. This attribute is particularly important for accessibility, as screen readers and other assistive technologies rely on it to convey information about the clickable area to users who cannot interact with the image directly.

Additional attributes support more advanced functionality. The `hreflang` attribute specifies the language of the destination URL using a valid language tag from BCP 47. The `type` attribute indicates the MIME type of the destination URL, as defined in RFC 2046. Both of these attributes can help improve the usability and accessibility of image maps for users with specific needs or preferences.

For developers working with image maps, understanding these attributes is crucial for creating effective and accessible interactive content. The proper use of these attributes ensures that image maps function correctly across different devices and browsers, while also providing essential information for users who rely on assistive technologies.


## Responsive and Accessible Image Maps

The creation of accessible, mobile-friendly image maps requires careful consideration of two key factors: fallback content and responsive design. To ensure compatibility across devices, developers should implement a simple fallback mechanism using alternative content structures like tables or lists of links.

For interactive image regions, modern approaches favor JavaScript libraries over traditional methods. Matt Stow's jQuery plugin offers an effective solution for creating responsive image maps, while WordPress users can leverage his plugin's free equivalent. Current best practices recommend against using server-side image map methods like the ismap attribute, which were common in earlier web development standards.

The HTML elements used for image maps remain consistent across browser versions: the `<map>` element requires a unique name attribute that matches the usemap attribute of the associated `<img>` tag. Each `<map>` element must contain at least one `<area>` element to define clickable regions, with supported shapes including rect, circle, and poly.

When implementing image maps, developers should pay attention to browser compatibility requirements. For instance, the relList IDL attribute must correctly reflect the [rel] content attribute in Edge Legacy, Internet Explorer, and IE, with current support available in newer versions of Firefox, Safari, Chrome, and Opera. Similarly, the referrerPolicy attribute should properly mirror the [referrerpolicy] attribute with known values in modern browsers.

In summary, effective image map implementation combines semantic HTML structure with responsive design principles and accessible fallback content, ensuring consistent behavior across devices and browsers.


## Processing Image Maps

The browser processes image maps through a multi-step parsing and user interaction model. When an image with a usemap attribute is encountered, the browser first parses the attribute value as a hash-name reference to a map element. If the reference is null, the image is not associated with an image map.

The browser then collects all area elements within the referenced map element as the image map's regions. For interactive processing, the browser follows these steps:

1. If displaying image text content, the browser removes area elements without href attributes and those with empty alt attributes, unless another area element shares the same href and has non-empty alt text.

2. Each remaining area element represents a hyperlink, which the browser makes available to the user.

The processing model requires browser support for specific IDL attributes:

- relList must reflect the [rel] content attribute in older versions of Edge, Internet Explorer, and IE (supported in Firefox 41+, Safari 14.1+, Chrome 52+, Opera 79+)

- referrerPolicy must reflect the [referrerpolicy] content attribute, limited to known values (supported in Firefox 50+, Safari 14.1+, Chrome 52+, Opera 79+)

This processing model ensures that image map regions behave correctly across browsers while supporting modern accessibility and security features.

