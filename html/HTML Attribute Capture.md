---

title: HTML capture attribute: Accessing device cameras and microphones

date: 2025-05-29

---


# HTML capture attribute: Accessing device cameras and microphones

This article explores the capture attribute in HTML file input elements, specifically its functionality in accessing device cameras and microphones. It examines how the attribute works with different values (user and environment), its implementation details across various browsers, and how it integrates with other attributes like accept to provide more sophisticated file input controls. The article demonstrates practical implications through code examples and testing results on both mobile and desktop browsers.


## Attribute overview

When applied to file input elements with the type attribute set to "file", the capture attribute can take two values: "user" for front-facing camera/microphone and "environment" for back-facing camera/microphone. Its presence prompts the browser to use media capture mechanisms instead of file selection dialogs.

This functionality allows users to select media files directly from their device's camera or microphone rather than browsing their storage. For example, the code snippet provided by the author demonstrates this capability:

```html

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8" />

    <meta name="viewport" content="width=device-width,initial-scale=1" />

    <style>

        * { font-size: 
1.5rem; }

    </style>

</head>

<body>

    <label for="environment">Capture environment:</label>

    <br>

    <input type="file" id="environment" capture="environment" accept="video/*" >

    <br><br>

    <label for="user">Capture user:</label>

    <br>

    <input type="file" id="user" capture="user" accept="image/*" >

</body>

</html>

```

When tested on a mobile device, clicking the "environment" input opens the camera in video recording mode, while clicking the "user" input opens the camera in image capture mode. The phone's camera does not differentiate between front and back-facing cameras, but the "user" value still functions as intended.

The attribute works in conjunction with the accept attribute to specify MIME types for captured media. For instance, adding `accept="image/*"` allows users to select photos, while changing it to `accept="video/*"` enables video capture. Together, these attributes provide a comprehensive solution for in-browser media capture, though implementation details vary between desktop and mobile browsers.


## Attribute values and behavior

The `capture` attribute in HTML is used with the `<input type="file">` element to control how users interact with the file selection dialog. It allows you to prompt the user to capture a new media file using their device's camera or microphone, rather than simply selecting a file from their storage.

When applied to a file input, the `capture` attribute can take two values: `"user"` for front-facing camera/microphone and `"environment"` for back-facing camera/microphone. Its presence prompts the browser to use media capture mechanisms instead of file selection dialogs.

The attribute functions by requesting that the browser prioritize capturing new media over selecting existing files. For instance, setting `capture="user"` will prompt the user to use the front-facing camera, suitable for capturing selfies or videos of themselves. Conversely, `capture="environment"` will direct the user to use the back-facing camera for capturing pictures or videos of their surroundings.

The behavior of the `capture` attribute varies slightly between device and browser versions. For example, Android implementations since version 3.0 support the attribute, while iOS Safari requires the `accept` attribute for image and video selection. On iOS 10.3.1, the behavior began conforming to specifications, providing two options: "Take Photo or Video" and "Choose Existing."

Browser support for the attribute has evolved over time. Initially introduced as a Boolean attribute, it has been updated to an enumerated attribute with states "user" and "environment." Desktop browser implementations vary, with Edge, Chrome, Firefox, Opera, and Safari all supporting the attribute, though mobile support appears more consistent across versions.


## Implementation details

When the capture attribute is present in an HTML file input, supported browsers display a specialized media capture dialog rather than the standard file selection interface. For instance, on iOS Safari, this results in a dialog box offering two options: "Take Photo or Video" and "Choose Existing."

The behavior differs between supported and unsupported devices. According to testing across multiple Android versions (4.1.2, 4.3, 4.2.2) and iOS 7.0.4, modern mobile browsers consistently display both camera capture and file selection options when the attribute is correctly implemented. In contrast, older Android versions show only the file selection dialog unless both the accept attribute and capture attribute are properly configured.

Browser compatibility varies significantly. While desktop browser implementations support the attribute, mobile support has a broader range. The attribute works as expected on Android 3.0 and later, with consistent behavior across Chrome, Firefox, Opera, and Safari on mobile devices. The attribute has been fully supported on these platforms since their respective introduction, though some older versions may exhibit limited functionality.

Implementation details vary based on the specific browser and device combination. For example, testing on a Samsung Galaxy S3 running Android 4.1.2 shows the attribute working correctly, while the same combination with Android 4.3 exhibits partial functionality, showing the camera option within the standard file selection dialog. These variations highlight the importance of thorough testing across target devices when implementing capture functionality.


## Integration with other attributes

The accept attribute complements the capture attribute by specifying the MIME types of media that can be captured. When the accept attribute is set to "image/*", for example, the file picker displays in the Image Capture state, optimized for direct media capture using the preferred camera-facing mode. Meanwhile, an accept attribute of "video/*" triggers the Video Capture state, providing a user interface tailored for video recording.

The combination of these attributes allows developers to create more sophisticated file input controls that balance user experience with functionality. For instance, an HTML form might include both image and video capture capabilities, with specific controls for each type of media. This setup provides users with clear options for their capture preferences while maintaining compatibility with a wide range of device and browser configurations.

It's worth noting that while the capture attribute significantly enhances file input controls, it requires careful implementation to ensure consistent behavior across devices and browsers. Specifically, developers must account for variations in browser support and device capabilities. As seen in the provided examples, certain combinations of attributes—particularly when dealing with images and videos—can affect how the file picker behaves, requiring thorough testing across multiple platforms.


## Browser support

Current browser implementations of the capture attribute primarily affect mobile devices, with varying degrees of support available on desktop systems. The attribute operates as a boolean value or takes specific string values of "user" or "environment" to determine camera usage.

Mobile browsers across major platforms have implemented significant support since version 3.0 for Android devices and iOS 10.3.1, which began conforming more closely to specification requirements. Specifically, versions 25 and above of Chrome for tablets and mobile devices fully support the attribute, with similar support from Firefox (version 79) and Opera (version 14). Safari for iOS introduced support in version 10, while Samsung's WebView implementation has demonstrated functional support since version 4.4.

Despite these advancements, desktop browser support remains inconsistent. Edge, Chrome, Firefox, Opera, and Safari all implement the attribute, though specific versions may vary in compatibility. For instance, while modern versions of these browsers handle the attribute correctly, earlier versions may exhibit limited functionality or fallback to standard file selection dialogs.

The attribute's impact is most clearly demonstrated when used in conjunction with the accept attribute, particularly for image and video capture. When the accept attribute is set to "image/*", the browser presents users with a media capture dialog that prioritizes camera access over file selection. This behavior is consistent across supported devices and versions, offering a standardized approach to in-browser media capture that balances user experience with functional requirements.

