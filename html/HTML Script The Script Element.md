---

title: `<script>`: The Script element

date: 2025-05-29

---


# `<script>`: The Script element

The script element is a fundamental building block of modern web development, enabling dynamic content manipulation and interactive user experiences. This technical exploration delves into the intricacies of script elements, examining how their attributes shape script behavior and influence document parsing. From basic type attribute functionality to advanced features like async and defer, this article provides comprehensive guidance on mastering the script element for efficient, cross-browser compatible web development.


## Type Attribute

The type attribute in the script tag determines how the content between the script tags is interpreted. While the default MIME type is text/javascript, the attribute supports various other MIME types as well.

For classic scripts, the type attribute can be omitted, empty, or match a JavaScript MIME type essence. In these cases, the browser interprets the content using the JavaScript Script top-level production. However, for JavaScript module scripts, the script element requires a type attribute specifically set to "module," with JSON content requiring a MIME type of text/json. This distinction affects how the script element processes its content, ensuring compatibility with different script types and formats.

The attribute's value also influences the script's execution behavior. When an external script is referenced using the src attribute, the type attribute determines whether the script is treated as a classic script or a module script. A type attribute of "module" allows script and all dependencies to be fetched in parallel, while the classic script's behavior remains unchanged regardless of the attribute's presence.

Developers must ensure that content within script elements meets specific production requirements based on the type attribute's value. For inline scripts, content must adhere to JavaScript specification's Script or Module productions, while external scripts must conform to the documentation production in ABNF. This ensures proper parsing and execution of script content across different environments and uses.


## Script Tag Attributes

The `<script>` element supports multiple attributes to control its behavior and interaction with the document, including async, defer, crossorigin, integrity, nomodule, nonce, and referrerpolicy.

The async attribute, present for classic scripts only, indicates that the script should be fetched in parallel to parsing and evaluated as soon as available. This attribute provides similar functionality to the defer attribute when both are present. For module scripts, the async attribute causes the script and all dependencies to be fetched in parallel to parsing, evaluated when parsing completes.

The defer attribute, also available for classic scripts, specifies that the script should be fetched in parallel and evaluated when parsing completes. This attribute has no effect on module scripts, which defer by default. Scripts with the defer attribute will execute in the order in which they appear in the document, allowing the elimination of parser-blocking JavaScript where the browser would otherwise have to load and evaluate scripts before continuing to parse.

The crossorigin attribute controls error information exposure and credentials mode for cross-origin requests. For classic scripts, it determines the error information exposure from other origins, while for module scripts it controls credentials mode for cross-origin requests. Module scripts require CORS protocol for cross-origin fetching.

The integrity attribute provides inline metadata for the user agent to verify that a fetched resource has been delivered without unexpected manipulation. This attribute must not be specified when the src attribute is absent and is used for Subresource Integrity checks.

The nomodule attribute serves as a boolean flag to prevent script execution in user agents that support ES module features. This attribute enables selective execution of module scripts in modern user agents and classic scripts in older user agents. When specified on a module script, the browser will ignore the attribute due to the inherent module support.

Additional attributes include:

- fetchpriority, which provides a hint for the relative priority to use when fetching an external script (high, low, or auto)

- nonce, a cryptographic nonce value for Content-Security-Policy script-src attribute

- referrerpolicy, indicating which referrer to send when fetching the script or resources it loads:

  - no-referrer, no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, and unsafe-url options are available

These attributes offer comprehensive control over script execution, loading, and security, ensuring optimal performance and compatibility across different environments and user agents.


## JavaScript Fundamentals

The script element enables dynamic content manipulation, style changes, and attribute modifications through JavaScript. Common operations include modifying HTML content, applying styles, and altering attributes. For example, to display "Hello JavaScript!" in an element with id "demo", the script would use document.getElementById("demo").innerHTML = "Hello JavaScript!". Similarly, styles can be changed with document.getElementById("demo").style.fontSize = "25px"; document.getElementById("demo").style.color = "red"; document.getElementById("demo").style.backgroundColor = "yellow"; and attributes can be modified using document.getElementById("image").src = "picture.gif".

Content changes, style modifications, and attribute adjustments demonstrate the fundamental capabilities of JavaScript when embedded via the script element. This enables developers to create interactive and dynamic web experiences that respond to user actions or fetch data from external sources.


## Script Reference Methods

Several methods exist for referencing script elements in JavaScript. For inline scripts, developers can use an ID attribute: `<script id="uniqueScriptId">...</script> var thisScript = document.getElementById('uniqueScriptId'); </script> This approach works for both synchronous and asynchronous scripts and provides consistent knowledge of the script tag's identity.

For dynamic script loading, a simple loop through all script elements yields the most recent script: var scripts = document.getElementsByTagName('script'); var thisScriptTag = scripts[scripts.length - 1]; However, this method can fail in certain edge cases, such as when scripts are loaded asynchronously or dynamically.

Alternative methods include using a data attribute, selecting by source URL, or creating custom elements within the script. These approaches offer flexibility for different development scenarios while maintaining compatibility across major browsers.


## Script Execution Context

The script element's execution context is significantly influenced by the async and defer attributes, which control how scripts are fetched and evaluated in relation to document parsing.

For classic scripts, the async attribute causes the script and its dependencies to be fetched in parallel to parsing. When async is present, the script is evaluated as soon as it's available, potentially before parsing completes. This allows elimination of parser-blocking JavaScript where the browser would otherwise need to load and evaluate scripts before continuing to parse. When both async and defer attributes are present, the element acts as if only the async attribute is specified.

The defer attribute affects script execution sequence more than parallelism. For classic scripts, defer causes the script to be fetched in parallel to parsing and evaluated when parsing completes. This attribute has no effect on module scripts, which defer loading by default. Scripts with the defer attribute execute in the order they appear in the document, enabling elimination of parser-blocking JavaScript where browsers would otherwise need to load and evaluate scripts before continuing to parse.

The behavior of scripts with neither async nor defer attributes is different between classic and module scripts. For classic scripts, the script is fetched and evaluated immediately, blocking parsing until both the script and its dependencies complete. For module scripts, including dependencies, the script fetch and evaluation occur immediately as well, though evaluation timing differs from classic scripts due to ES module semantics.


### Script Reference Methods

Several methods enable referencing script elements in JavaScript. For inline scripts, developers can use an ID attribute: `<script id="uniqueScriptId">...</script> var thisScript = document.getElementById('uniqueScriptId');`

For dynamic script loading, developers can use a loop through all script elements to access the most recent script: var scripts = document.getElementsByTagName('script'); var thisScriptTag = scripts[scripts.length - 1];

The document.write() method allows including another script while the DOM is not yet rendered, enabling linear script execution (except for deferred scripts that will be rendered later). This method works only for inline scripts; innerText, text, and textContent properties for external scripts are empty.

Additional approaches include using a data attribute, selecting by source URL, or creating custom elements within the script. These methods offer flexibility across development scenarios while maintaining compatibility with major browsers.

