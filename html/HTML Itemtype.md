---

title: HTML itemtype tag

date: 2025-05-29

---


# HTML itemtype tag

Structured data markup transforms plain web content into rich semantic information, powering personalized experiences and enhanced discoverability. At the heart of this revolution lies the HTML itemtype attribute, a powerful tool for defining the type of web elements through URL-based vocabularies. In this comprehensive exploration, we dissect the nuances of itemtype implementation, from its fundamental role in microdata to advanced applications in global identifier assignment. Through practical examples and best practices, we uncover how developers can harness this powerful attribute to enrich their content while ensuring interoperability across web platforms.


## itemtype Basics

The itemtype attribute in HTML serves to identify the type of an item, acting as a URL that defines the vocabulary for associated properties. This URL functions as a unique identifier for elements containing microdata, allowing web developers to specify the context and structure of their content in a standardized way.


### Vocabularies and URLs

The itemtype URL is crucial for establishing the vocabulary that governs an item's properties. While the attribute's value can technically be any string, the most effective implementations use valid URL strings that point to defined vocabularies. These URLs help ensure interoperability between different websites and systems that might process the microdata.


### Multiple Item Types

An item can contain multiple types by listing them as space-separated values in the attribute. However, these types must all belong to the same vocabulary to maintain consistency. This feature allows complex items to incorporate multiple classification schemes without becoming overly cumbersome.


### Example Implementation

Consider an HTML element representing a person:

```html

<div itemscope itemtype="https://schema.org/Person">

  <a href="#" itemprop="url">David Deacon</a>

</div>

```

Here, the itemtype "https://schema.org/Person" defines that this block represents a person object, while the itemprop "url" specifies a property of that object.


### Flexibility in URL Use

Developers have some flexibility in choosing their itemtype values. While URLs are common, plain words without dots or colons can also be used. For URL identifiers, it's best practice to select values that correspond to pages the developer controls, helping prevent conflicts with other vocabularies.


## Microdata Integration

The HTML itemscope attribute defines the scope of associated metadata, creating a new item that consists of a group of name-value pairs. This attribute, when specified on an element, creates an item that results in these metadata pairs. The itemtype attribute, which must contain a value with at least one unique URL string token, defines the types of these items. These types must be defined in applicable specifications and use the same vocabulary.


### Element Relationships

When used in combination with the itemscope attribute, itemtype creates a structured data context that search engines and other processors can easily navigate. The attribute's value should be a valid URL string that is an absolute URL, with URLs not automatically dereferenced by user agents unless specified otherwise in the applicable specifications.


### Multiple Item Types

An element can contain multiple types by listing them as space-separated values in the itemtype attribute, provided they all belong to the same vocabulary. For example, an event might be marked up with both "https://schema.org/Event" and "https://calendar.example/event" types. This feature allows for complex items to incorporate multiple classification schemes while maintaining structural clarity.


### Practical Applications

The itemscope and itemtype attributes enable detailed content markup across various applications. Events can be marked up with structured data using the `<div itemscope itemtype="https://schema.org/Event">` element, providing comprehensive information about the event. Similarly, products can be described with detailed attributes through markup like `<div itemscope itemtype="https://schema.org/Product">`.


### Best Practices

Developers should use valid URLs for itemtype values and ensure these URLs correspond to vocabularies they control. This practice helps prevent conflicts with other vocabularies while maintaining the semantic clarity of the marked-up content. The combination of itemscope, itemtype, and itemprop attributes creates a robust framework for structured data that enhances web page discoverability and usability for both users and search engines.


## URL Best Practices

The itemtype attribute requires that its value consist of one or more valid URL strings, each forming a unique token. These URLs serve as case-sensitive identifiers without leading or trailing whitespace, and browsers treat them as opaque identifiers rather than active resources. While the URLs themselves are not connected to specific web resources, they act as the foundation for defining microdata vocabulary.

Valid URLs for itemtype can be absolute or use the Uniform Resource Name (URN) scheme. The values must contain at least one token, with multiple types defined as space-separated values when they belong to the same vocabulary. For instance, an event might incorporate both "https://schema.org/Event" and "https://calendar.example/event" types.

The structure of URL values follows specific parsing rules, where tokens are extracted by splitting the attribute value on whitespace. Each token undergoes processing based on its characters: "#" delimits substrings from the start to the first "#", "/" extracts from the start to the last "/", and other characters prepend a "/" followed by the resulting string. This process ensures each URL token is preserved as an absolute valid URL.

Developers should ensure that itemtype URLs point to vocabularies they control, as browsers like Chrome, Edge, Firefox, Opera, and Safari all support the attribute. Vocabularies can include detailed item properties and supporting information, as demonstrated in the example where `<dl>` elements combine multiple itemtypes to describe a locomotive or turnout kit.


## Vocabulary and Properties

.itemtype attribute identifies the vocabulary for an item's properties. For example, a property named "class" for an animal item might refer to the animal's classification, while the same property for a teacher item might refer to their classroom assignment.

Multiple item types can share the same vocabulary. This allows for complex items to incorporate multiple classification schemes while maintaining structure. For instance, an item might be marked with both "https://schema.org/Event" and "https://calendar.example/event" types, demonstrating how related vocabularies can be combined.

Vocabularies can be designed to associate items with global identifiers using URLs in the itemid attribute. This is particularly useful for identifying specific items, such as books by their ISBN number or concepts by their URL. For example, the book vocabulary shown in the documentation associates items with their ISBN using the itemid attribute.

When designing new vocabularies, identifiers can use URLs or simple words (without dots or colons). While URLs offer the advantage of avoiding conflicts with other vocabularies by using identifiers controlled by the author, properties with simple word names are restricted to specific types. URL-named properties, on the other hand, can be reused across any type, providing flexibility in vocabulary design.

The itemtype URL determines which vocabulary applies to an item's properties. As shown in the documentation, a single item can contain multiple properties even when the associated image is unrelated. Properties within the same item can have the same name but different values, as demonstrated with properties "flavor" set to "Lemon sorbet" and "Apricot sorbet" for a single item.

The attribute's value must be an unordered set of unique space-separated tokens, each a valid URL string. The item types are obtained by splitting this value on ASCII whitespace. These types must be defined in applicable specifications and use the same vocabulary. While the URLs themselves are not automatically dereferenced by user agents, specifications can define circumstances where they might be used for help information.

The microdata model consists of items containing name-value pairs. Each item can have an item type, global identifier, and list of properties. Properties can have string values or nested items as values, demonstrating the flexibility of the itemtype system in representing complex data structures.


## Global Identifiers

The itemid attribute provides a unique identifier for items in microdata, functioning as a global identifier for elements containing structured data. This attribute requires a valid URL value that can be surrounded by spaces and must be parsed relative to the node document of the element on which it's specified. If the attribute is missing or parsing fails, the item has no global identifier.


### Element Relationships

The itemid attribute works in conjunction with itemscope and itemtype to define the scope and type of structured data elements. Like itemtype, this attribute must be specified on elements with both itemscope and itemtype attributes, and only on those that support global identifiers for items as defined by their specification.


### Best Practices

Similar to itemtype values, itemid URLs should reference controlled identifiers to prevent conflicts with other vocabularies. While plain words can be used without dots or colons, URL identifiers offer the advantage of clear namespace control. This practice helps maintain semantic clarity and interoperability between different microdata implementations.


### Implementation Example

A book item might use the itemid attribute to reference its ISBN:

```html

<div itemscope itemtype="https://schema.org/Book" itemid="urn:isbn:0-330-34032-8">

  <span itemprop="name">HTML Microdata</span>

</div>

```

This example demonstrates how the itemid attribute can be used to associate specific items with global identifiers, enhancing the discoverability and organization of structured content.

## References

- [HTML em The Emphasis Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20em%20The%20Emphasis%20Element.md)
- [HTML Attribute Accept](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Accept.md)
- [HTML The Data Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Data%20Element.md)
- [HTML The Generic Search Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Generic%20Search%20Element.md)
- [HTML Relpreload](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Relpreload.md)