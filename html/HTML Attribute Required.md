---

title: How to Use the HTML 'required' Attribute

date: 2025-05-29

---


# How to Use the HTML 'required' Attribute

The required attribute in HTML is a fundamental tool for form validation, ensuring that users complete necessary fields before submitting a form. This attribute controls which inputs must contain data, providing instant feedback through browser tooltips and visual indicators. The attribute works across multiple input types and can significantly enhance both accessibility and user experience when properly implemented. This article explores the technical aspects of using the required attribute, including its compatibility across browsers and devices, while also offering practical tips for ensuring that forms remain usable and accessible for all users.


## When to Use the 'required' Attribute

The required attribute ensures that specific form fields are completed before the form can be submitted. It applies to multiple input types, including text, search, URL, telephone, email, password, date pickers, numbers, checkboxes, radio buttons, and files. The attribute can be included with or without a value; its presence alone indicates that the field is mandatory.

When implemented on input elements, the required attribute functions as follows: if the field is left blank during form submission, most modern browsers display visual feedback such as a border around the field and a tooltip error message. The :required pseudo-class can be used in CSS to style these fields specifically.

For select elements, the required attribute works in conjunction with the `<option>` tag; at least one option must be selected before the form can be submitted. Textarea elements require both the required attribute and specific dimensions defined through the rows and cols attributes. Radio button groups need special consideration - if one radio button is marked as required, all buttons in the group must be selected. For checkbox groups, only checkboxes with the required attribute are considered mandatory.

The attribute provides improved accessibility by informing screen readers that certain fields are required. Best practice suggests accompanying the required attribute with visual feedback near the control, helping both sighted and non-sighted users understand which fields need completion.


## Supported Input Elements

The required attribute works with the following input types: text, search, url, tel, email, password, date pickers, number, checkbox, radio, and file. It functions similarly for select and textarea elements, though textarea requirements also rely on defined dimensions through the rows and cols attributes.

The attribute syntax is simple: just include "required" without a value. For example, an input field might look like this: `<input type="text" id="username" name="username" required>`. The required attribute applies to the `<input>`, `<select>`, and `<textarea>` tags, making these elements mandatory when their value is the empty string upon form submission.

All modern browsers support the required attribute, with complete compatibility in Chrome, Firefox, Safari, and Opera. Internet Explorer versions 5 and above also support this feature, though older versions may have partial compatibility. The attribute works as a boolean, meaning its presence requires the field to be filled, while its absence allows for optional fields.


## Browser Support

The required attribute has consistent full support across modern browsers, including the latest versions of Chrome, Firefox, Safari, and Opera. Internet Explorer, which began supporting this feature in version 5, continues to support it with good compatibility, though older versions may exhibit partial support.

When an input control with the required attribute receives focus, screen readers effectively identify it as required. This accessibility feature is supported in modern versions of Firefox, Chrome, and Opera, with VoiceOver in Safari also recognizing required fields. However, Internet Explorer versions 9 and below fail to identify required fields through screen readers, meaning users relying solely on these browser versions may miss this vital information.

Browser handling of form submission with empty required fields is generally consistent across supported versions. Firefox, Chrome, Safari, and Opera all display clear visual feedback on submission attempts, typically through a border around the field and a tooltip error message indicating the field requires user input. This consistency helps ensure users with various browser versions receive similar feedback mechanisms.


## Accessibility and Usability

The required attribute significantly enhances accessibility by allowing screen readers to identify mandatory fields. Modern browsers and screen reader combinations effectively recognize required fields, though compatibility varies:


### Screen Reader Compatibility

- **Firefox 8 with NVDA 2011.3 and JAWS 13:** Recognizes required fields, identifies empty fields as invalid, and draws borders around empty fields.

- **VoiceOver on Safari 5.1.2:** Effectively identifies required fields.

- **Internet Explorer 9 with NVDA 2011.3 and JAWS 13:** Fails to identify required fields, potentially causing accessibility issues.


### Visual Feedback Variations

Different browsers present required fields with varying visual feedback:

- **Firefox 8:** Displays a border around the required field.

- **Chrome 15:** Similar to Firefox, displaying a border around the field.

- **Opera 11.52:** Does not display a border.

- **Safari 5.1.2:** Provides basic visual feedback but lacks border rendering.


### User Agent Support

- **Google Chrome**: Full support across versions

- ** Microsoft Edge**: Full support across versions

- **Firefox**: Full support across versions

- **Opera**: Full support across versions

- **Internet Explorer 9**: Basic support, though with limitations


### Implementation Best Practices

To ensure usability across all users, implement multiple feedback mechanisms:

- **Text Indication:** Label required fields clearly in the form's visual layout.

- **Color Coding:** Use distinctive boundary colors around required fields.

- **Attribute Support:** Utilize `aria-required="true"` for fallback support in older browsers or screen readers that do not recognize `required`.

By combining these strategies, developers can create forms that are both accessible and user-friendly, ensuring all users understand which fields are mandatory for form submission.


## Common Error Handling

When a required field is left empty, most modern browsers display clear visual feedback to help users understand their mistake. This typically involves drawing a border around the field and displaying a tooltip error message indicating that the field requires user input. The specific behavior varies slightly between browsers, with Firefox and Chrome both drawing a border around the required field, while Internet Explorer and Opera do not display a border.

Browser developers use the :required pseudo-class to style these fields, allowing web developers to customize the appearance of mandatory fields through CSS. For example, a developer might use this selector to add a red border or background color to highlight required fields: `input:required { border-color: red; }`.

While the required attribute provides essential feedback for sighted users, developers must consider accessibility for users who rely on screen readers. Modern browsers and screen reader combinations handle required fields effectively: Firefox, Chrome, and Opera's screen readers all identify required fields, while VoiceOver in Safari 5.1.2 also recognizes these elements. However, Internet Explorer versions 9 and below fail to identify required fields through screen readers, potentially causing accessibility issues for users who depend on these browser versions.

To ensure comprehensive feedback for all users, developers should implement multiple indication mechanisms. This includes clear text labeling of required fields, distinctive color coding around required controls, and appropriate use of attributes such as aria-required="true" to provide fallback support for browsers and screen readers that do not recognize the required attribute. By following these best practices, developers can create forms that remain accessible and user-friendly across a wide range of browser versions and user groups.

