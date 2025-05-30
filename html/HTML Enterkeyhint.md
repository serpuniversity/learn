---

title: HTML enterkeyhint Attribute Best Practices

date: 2025-05-29

---


# HTML enterkeyhint Attribute Best Practices

As web development continues to evolve, developers seek ways to enhance user experience beyond traditional functionality. One such enhancement is the enterkeyhint attribute, which personalizes virtual keyboard behavior based on form input type. This attribute offers six distinct label presentations, from "Done" to "Search," allowing developers to guide users more effectively through their interactions. Understanding how to implement and optimize this feature requires knowledge of its technical specifications and browser compatibility. In this article, we explore the enterkeyhint attribute's capabilities, usage, and impact on both developer implementation and user experience.


## enterkeyhint Overview

The enterkeyhint attribute operates as an enhanced means of keyboard customization, specifically influencing how virtual keyboards display the Enter key based on contextual input type. According to Mozilla's documentation, this attribute allows for six distinct label presentations: "Done," commonly indicating form completion; "Enter," for standard new-line insertion; "Go," for URL navigation or action initiation; "Next," for progressive form traversal; "Previous," for backward field navigation; and "Search," directing query submission.

Implementing this attribute requires developers to assign one of these values to form input elements. In practice, this customization can significantly enhance user experience, especially on mobile devices where physical keyboards are unavailable. For instance, applying enterkeyhint="search" to a text input triggers a blue "search" button appearance, while enterkeyhint="go" displays a corresponding "go" action label.

Browser compatibility demonstrates widespread support across modern versions, with 94% coverage in Safari, 79% in Firefox, and 77% in Chrome. This attribute has been consistently implemented since November 2021 across both desktop and mobile platforms. While Windows 11 no longer supports dedicated touch modes, the attribute remains relevant for virtual keyboard configurations accessed through accessibility settings.


## enterkeyhint Values

The attribute takes six specific values: "enter," "done," "go," "next," "previous," and "search."

- "enter" typically inserts a new line

- "done" indicates there is nothing more to input and the input method editor (IME) will be closed

- "go" typically means to take the user to the target of the text they typed

- "next" typically takes the user to the next field that will accept text

- "previous" typically takes the user to the previous field that will accept text

- "search" typically takes the user to the results of searching for the text they have typed

The attribute is used to customize the enter key behavior, with user agents potentially using contextual information from the inputmode, type, or pattern attributes to display a suitable enter key label (or icon) if no enterkeyhint attribute is provided. For example, an "enter" value displays "Enter," "done" displays "Done," "go" displays "Go," "next" displays "Next," "previous" displays "Previous," and "search" displays "Search."


## Implementing enterkeyhint

The enterkeyhint attribute applies to all HTML elements that are editable, including form controls and elements using contenteditable. The available values and their effects are as follows:

- "enter" displays the standard "Enter" text

- "done" indicates completion and closes the input method editor

- "go" navigates to the target of the text input

- "next" moves to the next field that will accept text

- "previous" moves to the previous field that will accept text

- "search" displays a search icon or text

- "send" shows an email icon or "Send" text

To demonstrate its implementation, consider this HTML example:

```html

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>HTML enterkeyhint attributes</title>

</head>

<body>

    <form>

        <input placeholder="Enter button will change to Next" enterkeyhint="next">

        <input placeholder="Enter button will change to previous" enterkeyhint="previous">

        <input placeholder="Enter button will change to enter" enterkeyhint="enter">

        <input placeholder="Enter button will change to done" enterkeyhint="done">

        <input placeholder="Enter button will change to search" enterkeyhint="search">

        <input placeholder="Enter button will change to go" enterkeyhint="go">

        <input placeholder="Enter button will change to send" enterkeyhint="send">

    </form>

</body>

</html>

```

This example illustrates how each input element's enter key icon changes based on its specified attribute value. The attribute has consistent support across modern browsers, with 94% coverage in Safari, 79% in Firefox, and 77% in Chrome. Edge supports 13.1% and Internet Explorer 64% of its versions. While the attribute remains relevant for virtual keyboard configurations through accessibility settings, dedicated touch modes in Windows 11 no longer support it.


## Accessibility Benefits

The enterkeyhint attribute significantly enhances accessibility by providing clear instructions to users about what action pressing Enter will perform. For instance, when set to "done," it indicates the end of input, while "next" and "previous" help users navigate between form fields without relying on mouse clicks.

This attribute aligns with Web Content Accessibility Guidelines (WCAG) by improving keyboard navigation, particularly beneficial for users with motor disabilities who may find traditional mouse navigation challenging. Its compatibility across multiple browsers ensures consistent accessibility features for developers implementing these guidelines.

The attribute's impact extends to all form inputs, including textareas and contenteditable elements, making it a versatile tool for enhancing user experience. While its primary value lies in guiding virtual keyboard behavior, developers report improved form completion rates and reduced user errors through clearer input expectations.


## Browser Support

Browser support for the enterkeyhint attribute is comprehensive, with consistent implementation across major web browsers since at least November 2021. The attribute is supported by all modern browsers.

The attribute's implementation varies slightly across platforms. On iOS devices, virtual keyboards display navigation arrows above the standard key layout when the enterkeyhint attribute is applied. In contrast, Android users with Firefox Mobile experience automatic next-input functionality for the first form field and submit behavior for the final field.

This cross-platform compatibility ensures that developers can implement consistent keyboard navigation hints across both desktop and mobile environments. While specific behavior may differ between operating systems, the attribute provides a standardized way to customize enter key functionality for virtual keyboards.

