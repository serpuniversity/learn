---

title: HTML `<script>` type attribute

date: 2025-05-29

---


# HTML `<script>` type attribute

The `<script>` element is fundamental to web development, enabling dynamic content and functionality through client-side scripting. However, many developers overlook or misunderstand the type attribute, which plays a crucial role in how browsers interpret and process script elements. This article explores the type attribute's functionality, examining how it prevents direct script execution and serves as an identifier for the Babel compiler. We'll review common MIME type values, discuss browser compatibility, and explain the HTML5 requirements for modern web development best practices.


## Type Attribute Functionality

The type attribute of the `<script>` element serves two primary functions: it prevents the browser from directly running the script and identifies the script for the Babel compiler. When present, its value must be a valid MIME type, with the default value being "text/javascript" if the attribute is omitted.


### Common MIME Type Values

The attribute supports multiple MIME types, including text/javascript (the default), text/ecmascript, application/ecmascript, and application/javascript. The choice of MIME type affects how modern browsers interpret the script content.


### Script Processing Behavior

Browsers only understand supported MIME types in the type attribute of `<script>` elements, with most mainstream browsers defaulting to ECMAScript (JavaScript). When the user agent does not support the scripting language specified in the script block's type attribute, the browser aborts processing of the script element. This ensures compatibility while preventing unauthorized execution of unsupported code.


### Browsers and MIME Types

Browser support for different MIME types varies. Modern browsers generally only recognize "text/javascript", while older implementations might support additional types like "text/ecmascript" or "application/ecmascript". The attribute syntax requires proper formatting, with the value containing a single media type, typically following the format "media_type/subtype".


### HTML5 Requirements

In HTML5, the type attribute is no longer required for JavaScript, with a default value of "text/javascript". The attribute should be omitted instead of using "JavaScript" as a value, and the charset parameter must not be specified. This change reflects evolving standards and best practices in web development, although developers may continue to include it for explicit type declarations.


## Common MIME Type Values

The type attribute of the `<script>` element serves two primary functions: it prevents the browser from directly running the script and identifies the script for the Babel compiler. When present, its value must be a valid MIME type, with the default value being "text/javascript" if the attribute is omitted.


### Common MIME Type Values

The attribute supports multiple MIME types, including text/javascript (the default), text/ecmascript, application/ecmascript, and application/javascript. The choice of MIME type affects how modern browsers interpret the script content. For example, text/ecmascript and application/ecmascript are historical alternatives to text/javascript that some older implementations may still recognize.


### Script Processing Behavior

Browsers only understand supported MIME types in the type attribute of `<script>` elements, with most mainstream browsers defaulting to ECMAScript (JavaScript). When the user agent does not support the scripting language specified in the script block's type attribute, the browser aborts processing of the script element. This ensures compatibility while preventing unauthorized execution of unsupported code.


### Browsers and MIME Types

Browser support for different MIME types varies. Modern browsers generally only recognize "text/javascript", while older implementations might support additional types like "text/ecmascript" or "application/ecmascript". The attribute syntax requires proper formatting, with the value containing a single media type, typically following the format "media_type/subtype".


### HTML5 Requirements

In HTML5, the type attribute is no longer required for JavaScript, with a default value of "text/javascript". The attribute should be omitted instead of using "JavaScript" as a value, and the charset parameter must not be specified. This change reflects evolving standards and best practices in web development, although developers may continue to include it for explicit type declarations.


## Script Processing Behavior

When the user agent does not support the scripting language specified in the script block's type attribute, the browser aborts processing of the script element. This mechanism ensures compatibility while preventing unauthorized execution of unsupported code.

According to the HTML standard, the script processing steps include checking if the currentScript attribute needs to be updated and determining the script's execution context. If the script's type is not supported, the user agent must halt processing at this point.

For example, Babel, a popular compiler targeting ES6 compatibility, specific targets script elements with explicit types like `type/babel`, `type/jsx`, or `type/babel`. When Babel processes the code, browsers simply ignore the Babel scripts, which are transformed on-the-fly into ES5 JavaScript.

The browser's response to an unsupported MIME type varies depending on the specific script type. Classic scripts require that the script's root not be a shadow root, while module scripts must have a null currentScript attribute. The script's result is then evaluated based on its type: non-null results execute the script, while import maps register the script's relevant global object and result.


## Browsers and MIME Types

Most modern browsers default to ECMAScript (JavaScript) for script processing and do not fully support ES6 compatibility. This behavior stems from the attribute handling in HTML specifications: while browsers recognize multiple MIME types including text/javascript, text/ecmascript, application/ecmascript, and application/javascript, their native support varies.

Browsers process scripts using their registered MIME types, running classic scripts through their appropriate parser/compiler while handling VBScript or PerlScript through their specific interpreters. Custom MIME types like "type/f*ckjs" are ignored by browsers due to their unrecognized format.

When using Babel for ES6 compatibility, modern browsers simply ignore the Babel scripts, processing them as ES5 JavaScript through the browser's standard JavaScript engine. This approach ensures both compatibility with older browsers and the ability to transpile modern JavaScript syntax safely.


## HTML5 Requirements

In HTML5, the type attribute for script elements is no longer required when working with JavaScript, with a default value of "text/javascript". Developers should omit the attribute rather than using "JavaScript" as a value, and the charset parameter must not be specified.


### Browser Support and Handling

Most modern browsers default to ECMAScript (JavaScript) for script processing and do not fully support ES6 compatibility. When using Babel for ES6 compatibility, modern browsers simply ignore the Babel scripts, processing them as ES5 JavaScript through the browser's standard JavaScript engine.


### Specific Requirements

The HTML specification warns against using certain attributes in the script element:

- The charset attribute must not be present, with a value of ASCII case-insensitive "utf-8" if present

- The language attribute must not be present, with a value of ASCII case-insensitive "JavaScript" if present

- The type attribute must either be omitted or have a value of "text/javascript"

- The attribute should be omitted instead of using "JavaScript" as a value

## References

- [HTML Fencedframe The Fenced Frame Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Fencedframe%20The%20Fenced%20Frame%20Element.md)
- [HTML The Strong Importance Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Strong%20Importance%20Element.md)
- [HTML Constraint Validation](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Constraint%20Validation.md)
- [HTML Global Attributes](https://github.com/serpuniversity/learn/blob/main/html/HTML%20Global%20Attributes.md)
- [HTML The Style Information Element](https://github.com/serpuniversity/learn/blob/main/html/HTML%20The%20Style%20Information%20Element.md)