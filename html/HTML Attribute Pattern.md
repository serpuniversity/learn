---

title: HTML pattern Attribute: Input Validation with Regular Expressions

date: 2025-05-29

---


# HTML pattern Attribute: Input Validation with Regular Expressions

The pattern attribute in HTML5 provides a powerful mechanism for client-side input validation through regular expressions. This technical specification details how developers can enforce specific input formats while enhancing form usability and accessibility. Through detailed examples and best practices, the article demonstrates how to implement effective pattern validation across various input types while ensuring compatibility with different browsers and user needs.


## Syntax and Basic Usage

The pattern attribute enforces input validation using regular expressions, specifically with `<input>` elements. This attribute requires browser support and works with text, date, search, url, tel, email, and password input types.

To use the pattern attribute effectively, developers must:

- Set the document type to HTML5 using <!DOCTYPE html>

- Specify the character set as UTF-8 with `<meta charset="UTF-8">`

- Provide context through the title attribute

- Display sample values using the placeholder attribute

- Mark mandatory fields with the required attribute

The pattern attribute follows JavaScript RegExp rules and requires the 'v' flag for unicode awareness. It must match the entire input value, not just a substring, by implicitly including `^(?:` at the start and `)$` at the end of the pattern text.

When applied correctly, the pattern attribute improves usability through visual feedback. Developers can style invalid inputs with `input:invalid{ color:red; }` and valid inputs with `input:valid{ color:green; }`. For mandatory fields, developers can style them with `input[required]{ background-color:#F08080; }`.

The attribute provides several usability and accessibility considerations, including:

- Describing patterns in visible text near the control

- Including a title attribute to describe the pattern

- Using title contents during constraint validation to inform users

By implementing these best practices, developers can enhance both the functionality and accessibility of their forms while ensuring proper input validation.


## Supported Browsers and Element Compatibility

The pattern attribute enables HTML forms to enforce specific input formats using regular expressions. It works with the following input types: text, date, search, url, tel, email, and password.


### Browser Support

The pattern attribute requires browser support and works with specific input types. Supported browsers include:

- Google Chrome

- Edge (Internet Explorer Mode in Microsoft Edge)

- Firefox

- Opera

- Safari

The attribute is supported starting from the following versions:

- text: 
5.0

- date: 
10.0

- search: 
4.0

- url: 
10.1

- tel: 
9.6

- email: 
9.6

- password: 
9.6

For optimal form validation, developers should ensure their documents use HTML5 doctype (`<!DOCTYPE html>`) and specify UTF-8 character encoding (`<meta charset="UTF-8">`). The title attribute should provide context, while the placeholder attribute can display sample values. Mandatory fields can be marked with the required attribute.


### Pattern Attribute Structure

The pattern attribute enforces validation by comparing the input value against a specified regular expression. The regular expression must match the entire input value, not just a substring. This is achieved by implicitly including `^(?:` at the start and `)$` at the end of the pattern text, with no forward slashes around the pattern.

When used correctly, the pattern attribute enhances form usability through visual feedback. The browser applies a red border to invalid inputs (`input:invalid{ color:red; }`) and applies a green color to valid inputs (`input:valid{ color:green; }`). For mandatory fields, developers can style them with `input[required]{ background-color:#F08080; }`.

The attribute provides several usability and accessibility considerations. When included, developers should describe the pattern in visible text near the control and include a title attribute to describe the pattern. User agents may use the title contents during constraint validation to inform users.


## Regular Expression Basics

The pattern attribute enforces validation using JavaScript RegExp rules. The pattern must match the entire input value, not just a substring, by implicitly including `^(?:` at the start and `)$` at the end of the pattern text. No forward slashes should be specified around the pattern text.

The pattern attribute applies to various input types: text, date, search, url, tel, email, and password. For email and url types, the value must match specific expected syntaxes. If the pattern attribute is not present and the value doesn't match the expected syntax, the ValidityState object's typeMismatch property will be true.

The attribute can be specified with no value, which is treated as the empty string. Any non-empty input value results in a constraint violation. User agents may use the title attribute during constraint validation to inform users that the pattern is not matched. While some browsers display tooltips with title contents, improving usability for sighted users, assistive technology may read the title aloud when the control gains focus. However, it's important to note that the title attribute should only be used for visual display of text content, as many user agents do not expose it in an accessible manner.


### Regular Expression Components

HTML patterns can include various components:

- Characters: Directly included characters match themselves

- Metacharacters: Special characters like ( ) [ ] { } . * ? | \ that perform specific functions

- Character classes: Groups describing multiple possible characters

- Quantifiers: Specifying how many times a pattern should repeat

- Group characters: Nested brackets allowing for complex pattern structures


### Character Selection and Exclusion

HTML patterns can select characters using:

- Alternatives: Kaffee|Tee|Saft for coffee, tea, or juice

- Special characters: ( ) [ ] { } . * ? | \ for controlling pattern structure and meaning

- Predefined metacharacters: \d (one digit), \D (one non-digit), \w (letter, digit, underscore), \s (whitespace), \S (non-whitespace)

- Group characters: Round brackets ( ), square brackets [ ], curly brackets { } for organizing pattern elements

- Quantifiers: Applying to the last expression within round brackets, allowing for complex matching patterns


### Implementation Best Practices

To implement pattern validation effectively:

- Include the document type as HTML5 (`<!DOCTYPE html>`) and specify UTF-8 character encoding (`<meta charset="UTF-8">`)

- Provide context through the title attribute

- Display sample values using the placeholder attribute

- Mark mandatory fields with the required attribute

- Describe patterns in visible text near the control

- Include a title attribute to describe the pattern

- Use title contents during constraint validation to inform users

By understanding and correctly implementing these fundamentals, developers can create both functional and accessible form validation systems using the HTML pattern attribute.


## Input Type-Specific Patterns

The input pattern attribute enforces specific formatting rules for various `<input>` types, ensuring that user inputs match predefined criteria before form submission. For text fields, the attribute works with six input types: text, search, url, tel, email, and password. The pattern must be a valid regular expression that matches the entire input value, with no forward slashes required around the pattern text.


### Text Input

For standard text inputs, developers can enforce specific character requirements. For example:

```html

<input type="text" pattern="[A-Z]{3}" title="Must be three capital letters">

```

This pattern ensures that only three uppercase letters are accepted. The browser displays a tooltip indicating "Must be three capital letters" when the input is invalid.


### Search Input

Search inputs can enforce additional restrictions on characters. For instance:

```html

<input type="search" pattern="[^'\x22]+" title="Invalid input">

```

This pattern prevents the input from containing single quotes (') or double quotes (") characters.


### URL Input

URL fields must start with either "http://" or "https://", followed by at least one character. The pattern enforces this structure:

```html

<input type="url" pattern="https?://.+" title="Include http:// or https://">

```

The browser displays "Include http://" when the input format is incorrect.


### Email Input

Email validation requires a specific format, ensuring the correct structure of user inputs. For example:

```html

<input type="email" pattern="[^@]+@[^@]+\.[^@]+" title="Invalid email address">

```

This pattern checks for a valid email format, preventing common mistakes in email entry.


### Password Input

Password fields can enforce minimum length requirements while preventing easily guessable patterns. For example:

```html

<input type="password" pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters">

```

This pattern requires a minimum of 8 characters, including at least one digit, one lowercase letter, and one uppercase letter.


### Date Input

While date inputs (introduced in HTML5) can use the pattern attribute, the pattern must match the specific date format expected by the browser. For example:

```html

<input type="date" pattern="\d{4}-\d{2}-\d{2}">

```

This pattern enforces a four-digit year followed by two-digit month and day, separated by hyphens.


### Tel Input

The telephone input type requires a specific pattern to ensure correct formatting. For example:

```html

<input type="tel" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" title="Enter numbers in the format 123-456-7890">

```

This pattern enforces a three-digit area code followed by a three-digit exchange code and a four-digit line number, separated by hyphens.


## Accessibility and Usability Considerations

The pattern attribute provides several usability and accessibility considerations that developers should understand when implementing form validation. When included, patterns should be described in visible text near the control, and a title attribute should provide a description of the pattern. This information is crucial for users who rely on assistive technology to interact with web forms.

User agents may use the title attribute during constraint validation to inform users that the pattern is not matched. While some browsers display tooltips with title contents, this can exclude keyboard-only and touch-only users. The title attribute should only be used for visual display of text content, as many user agents do not expose it in an accessible manner. When using this attribute, developers should ensure that they also provide alternative text descriptions for better accessibility.

The pattern attribute works with specific input types: text, date, search, url, tel, email, and password. For email and url types, the value must match specific expected syntaxes. If the pattern attribute is not present and the value doesn't match the expected syntax, the ValidityState object's typeMismatch property will be true.

When implementing pattern validation, developers should keep several limitations in mind. The attribute works with specific input types and requires the value to match the entire input, not just a substring. It implicitly includes `^(?:` at the start and `)$` at the end of the pattern text, with no forward slashes around the pattern. The regular expression must match the entire value, not just a section. For email input types, both pattern and multiple attributes must be used, with the pattern matching the entire value.

The pattern attribute is particularly limited for certain types of data validation. For credit card types like American Express, the attribute fails to provide accurate validation. Similarly, phone numbers, prices, and VIN numbers vary significantly by country and vehicle class, making the attribute unreliable for these inputs. Email validation works better when using the email input type, which performs validation against email address patterns rather than relying on regular expressions.

For date validation, the attribute's limitations become apparent when considering different date formats and century ranges. While it can provide basic validation for specific formats, the attribute is not sufficient for comprehensive date validation, which requires server-side checking to prevent security issues. In all cases, developers should prioritize clear and concise pattern descriptions, proper attribute usage, and alternative text explanations to ensure both usability and accessibility.

## References

- [HTML Script Type Attribute](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Script%20Type%20Attribute.md)
- [HTML Tabindex](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Tabindex.md)
- [HTML nav The Navigation Section Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20nav%20The%20Navigation%20Section%20Element.md)
- [HTML Attribute Dirname](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Attribute%20Dirname.md)
- [HTML The Content Template Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Content%20Template%20Element.md)