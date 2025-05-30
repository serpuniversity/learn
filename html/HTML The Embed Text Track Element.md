---

title: The HTML `<track>` Element: Adding Text Tracks to Media

date: 2025-05-29

---


# The HTML `<track>` Element: Adding Text Tracks to Media

The HTML `<track>` element represents a significant advancement in web multimedia capabilities by enabling developers to associate text-based content with `<video>` and `<audio>` elements. Through this versatile element, web developers can implement subtitles, captions, descriptions, chapters, and metadata that enhance accessibility and viewing experience. Operating with attributes that support multiple languages and track types, the `<track>` element serves as a foundation for modern web applications that require synchronized text content with multimedia presentations. This article explores the technical intricacies of the `<track>` element, including its attributes, browser support, and API integration, providing developers with a comprehensive understanding of how to implement this functionality in their projects.


## Element Overview

`<p>`The HTML `<track>` element enables authors to associate text-based content with `<video>` and `<audio>` elements, providing functionalities for subtitles, captions, descriptions, chapters, and metadata. This versatile element supports multiple languages through the `<code>`srclang`</code>` attribute and can display content in various forms, from translations and transcriptions to navigational aids for visually impaired users.`</p>`

`<p>`Essentially, the `<track>` element acts as a container for timed text tracks, which are typically formatted in WebVTT (Web Video Text Tracks) format with a `<code>`.vtt`</code>` file extension. Each track requires several key attributes to function properly:`</p>`

`<ul>`

    `<li>``<code>`src`</code>`: Required attribute specifying the URL of the text track file`</li>`

    `<li>``<code>`kind`</code>`: Specifies the type of text track, with options including subtitles, captions, descriptions, and metadata`</li>`

    `<li>``<code>`srclang`</code>`: Required attribute for subtitles, specifying the language code of the text track data`</li>`

    `<li>``<code>`label`</code>`: Optional attribute providing a user-readable title for the text track`</li>`

`</ul>`

`<p>`The element itself is a void element, meaning it should not contain any content between the opening and closing tags. It can be configured to display text tracks in one of three modes: showing by default, hidden, or disabled. These modes control how cues are handled by the user agent, determining whether they are displayed immediately, managed in the active cue list, or completely inactive.`</p>`


## Key Attributes

The `<track>` element supports several important attributes that enable fine-grained control over text track functionality:


### Kind Attribute

The kind attribute is an enumerated attribute that specifies the type of text track, with valid values including subtitles, captions, descriptions, and metadata. When omitted, the kind attribute defaults to subtitles.

The attribute can be used in the following ways:

- Subtitles: Used when the sound is available but not understood (e.g., language barrier)

- Captions: Used when the sound is unavailable or not clearly audible, including transcription of dialogue, sound effects, and relevant musical cues (e.g., deaf users)

- Descriptions: Provides textual descriptions of video components for audio synthesis when the visual component is obscured, unavailable, or not usable


### Src Attribute

The src attribute is a required attribute that specifies the URL of the text track file. The file should be formatted in WebVTT format with a .vtt extension, which allows for cues, timings, and styling options through CSS.


### Srclang Attribute

The srclang attribute is a required attribute for subtitles, specifying the language code of the text track data. This attribute must be present when the kind attribute is set to subtitles to ensure proper language identification.


### Label Attribute

The label attribute is an optional attribute that provides a human-readable title for the text track. This can be used to display a user-friendly name for the track, making it easier for users to identify different language versions or types of content.


### Default Attribute

The default attribute is used to indicate that the track should be enabled if the user's preferences do not indicate that another track would be more appropriate. This attribute may only be used on one track element per media element.


## Browser Support

The `<track>` element has achieved near-universal support across all major browsers, including Chrome, Edge, Safari, Firefox, and Opera, from their respective minimum version requirements. It operates consistently across these platforms, allowing developers to add subtitles, captions, descriptions, chapters, and metadata to `<video>` and `<audio>` elements without requiring user activation.

The element's implementation closely follows W3C specifications, with attributes like src, kind, srclang, label, and default functioning as described in the HTML5 standard. For developers working with older versions of Internet Explorer, the element has supported since version 10, though specific browser compatibility details may vary between implementations.

The `<track>` element's core functionality—associating text-based content with multimedia elements—remains robust across implementations, with consistent support for .vtt files and WebVTT formatting. While minor implementation nuances exist between browsers, the element's fundamental capabilities remain consistent across platforms, enabling reliable text track integration in modern web applications.


## Track Management

The `<track>` element implements a sophisticated track management system that allows for dynamic addition, removal, and lifecycle tracking of text tracks. When a media element is created, the user agent sets the element's blocked-on-parser flag to true, and when the element is popped off the stack of open elements, it honors user preferences for automatic text track selection and populates the list of pending text tracks, setting the blocked-on-parser flag to false.

Each text track maintains a list of text track cues, represented by TextTrackCue objects. These cues contain structured data including identifiers, start and end times (down to fractions of a second), pause-on-exit flags, and format-specific metadata such as writing direction for WebVTT cues. The element's core state is tracked through a readiness state attribute with four possible values: Not Loaded, Loading, Loaded, or Failed to Load. This state determines how the track is handled by the user agent and whether cues are displayed to the user.

The track's mode attribute controls its active state, with three possible values: Disabled, Hidden, or Showing by default. In Disabled mode, the track is inactive with no cues displayed and no events fired. Hidden mode enables the track while keeping cues off-screen for momentary display by the user agent. Showing by default activates the track, displaying cues over video (for subtitles/captions), providing non-visual access (for descriptions), or enabling navigation functionality (for chapters). The system dynamically manages track lists, adding new tracks if they're not disabled and their readiness state is Loading, while removing inactive tracks when their state changes or their containing node's properties alter.


## API Integration

The `<track>` element's API integration allows developers to programmatically manage text tracks through the TextTrack and HTMLTrackElement interfaces. This enables dynamic track addition, removal, and modification using the HTMLMediaElement.addTextTrack() method, which mirrors the behavior of declarative `<track>` elements.

The TextTrack interface provides several key properties for managing individual tracks:

- language: Returns the text track language string

- id: Returns the track's unique identifier, useful for fragment syntax in in-band tracks

- mode: Returns the track's current mode (disabled, hidden, showing) with setter capability for mode changes

- cues: Returns the track's list of cues as a TextTrackCueList object

- activeCues: Returns currently active cues as a TextTrackCueList object

The TextTrackCueList interface offers methods for managing individual cues:

- length: Returns the number of cues in the list

- [index]: Returns the cue at the specified index in text track cue order

- getCueById(id): Returns the cue with the matching identifier, or null if none exists

The system maintains three categories of text tracks:

1. Tracks added using addTextTrack(), in order of addition, oldest first

2. Media-resource-specific tracks, defined by the media resource's format specification

3. Subtitles, captions, descriptions, chapters, and metadata tracks

Developers can manipulate tracks through the HTMLTrackElement interface, which provides access to TextTrack properties and methods. The track management system dynamically handles track lists, adding new tracks if not disabled and their readiness state is Loading, while removing inactive tracks when their state changes or their containing node's properties alter.

The API supports multiple engine implementations across major browsers, including Firefox 31+, Safari 6+, Chrome 23+, Opera 12.1+, Edge 79+, and Internet Explorer 10+. All current engines support the TextTrack interface and its properties, ensuring consistent track management functionality across platforms.

