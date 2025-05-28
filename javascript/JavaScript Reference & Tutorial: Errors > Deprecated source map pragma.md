---

title: JavaScript Source Map Pragmas: Using `//@` vs `//#`

date: 2025-05-26

---


# JavaScript Source Map Pragmas: Using `//@` vs `//#`

JavaScript source maps enable developers to map compiled code back to its original source, facilitating better debugging of obfuscated code. However, the recent change from `//@` to `//#` pragmas addresses compatibility issues with Internet Explorer's conditional compilation system. Understanding this change is crucial for maintaining efficient debugging workflows across modern development environments.


## Deprecated Pragmas

The use of `//@` to indicate sourceURL pragmas and sourceMappingURL pragmas in JavaScript is deprecated, with the recommended alternative being `//#`. This change was implemented due to conflicts with Internet Explorer's conditional compilation comment (`//@cc_on`), which caused issues particularly with libraries like jQuery.

The deprecated syntax appears as either `//@ sourceMappingURL=http://example.com/path/to/your/sourcemap.map` or `//@ sourceURL=http://abcd.com/path/name.map`, while the updated standard syntax requires developers to use `//# sourceMappingURL=http://example.com/path/to/your/sourcemap.map` or to set a SourceMap header in the JavaScript file: `SourceMap: /path/to/file.js.map`.

According to the Mozilla Developer Network, the source map pragma change was necessary to maintain compatibility with modern development tools while ensuring correct functionality across various browsers and development environments.


## Reason for Deprecation

The introduction of the source map pragma conflict occurred during the development of Internet Explorer's conditional compilation system, which utilized the `//@cc_on` syntax to enable conditional compilation features. This legacy system interfered specifically with the source map functionality when processing libraries like jQuery, leading to compatibility issues across different development environments.

The interaction between these two systems created unpredictable behavior when attempting to establish source mappings, particularly during the compilation and minification process. This fundamental conflict necessitated the change in pragma syntax in order to maintain consistent and reliable source map functionality across various JavaScript development workflows.


## Standard Syntax

Developers should use `//# sourceMappingURL` instead of the deprecated `//@ sourceMappingURL` to indicate source mappings. This change was implemented due to a conflict with Internet Explorer's conditional compilation comment (`//@cc_on`), which interfered with source maps, particularly affecting libraries like jQuery.

The updated standard syntax requires developers to use `//# sourceMappingURL=http://example.com/path/to/your/sourcemap.map` or to set a SourceMap header in the JavaScript file: `SourceMap: /path/to/file.js.map`. The SourceMap header provides the location of the source map for the resource, with precedence over the source annotation and using the header URL to resolve the source map file.

The HTTP `SourceMap` response header has been available since January 2020 and works across many devices and browser versions, with wide browser support. Alternative methods include using the `X-SourceMap` header, which uses the same syntax.

These changes maintain compatibility with modern development tools while ensuring correct functionality across various browsers and development environments. Source maps enable developers to map compiled code back to original source files, allowing for better debugging of obfuscated code and maintaining developer productivity.


## Alternative Solutions


### Alternative Solutions

Developers have two main options for specifying source map locations in their JavaScript files: using the `SourceMap` header or the `X-SourceMap` header. These alternatives provide flexibility for developers who prefer not to use comments in their code.

The `SourceMap` header follows a similar syntax to the deprecated `//@` notation:

- Absolute path: `http SourceMap: /path/to/file.js.map`

- Relative path: `http SourceMap: ./path/to/file.js.map`

This header approach works alongside or as an alternative to the comment-based solution, offering developers a choice based on their specific development workflow and toolchain requirements.


## Impact on Debugging

Source maps enable developers to maintain readable and debuggable client-side code even after it has been minified and combined, according to Mozilla Developer Network. This technology works by generating a mapping between the compiled JavaScript code and the original source code, allowing developers to step through the original code while debugging the compiled version.

Current supporting browsers include WebKit nightly builds, Safari, Google Chrome, and Firefox 23+, with Firefox 24+ enabling source maps by default. The source map query process involves right-clicking on generated code, selecting "Get original location," and passing generated line and column numbers to retrieve original code positions. This functionality is particularly useful for languages like CoffeeScript, ECMAScript 6, SASS/LESS, and others that compile to JavaScript, providing native browser support through source maps.

The Closure Compiler is the only JavaScript compiler/minifier currently supporting source map generation. The compiler generates both JavaScript code and a source map file during the minification process. The source map file contains information about the original source files and mappings between generated code and source code, structured as follows:

- version: 3

- file: "out.js" (name of the generated code file)

- sourceRoot: "" (optional, allows prepending source files with folder structure)

- sources: ["foo.js", "bar.js"] (list of source file names)

- names: ["src", "maps", "are", "fun"] (list of variable/method names)

- mappings: "AAgBC,SAAQ,CAAEA" (contains mapping information)

The source map file is only downloaded when source maps are enabled in developer tools and dev tools are open, with the file referenced using the X-SourceMap header: /path/to/file.js.map. Support exists for both single-line comments (`//# sourceMappingURL=code-min.js.map`) and header-based references (`X-SourceMap: /path/to/file.js.map`).

To address potential cross-site scripting (XSSI) issues, the source map specification recommends prepending the first line of the source map with ")]}" to create a syntax error that will be thrown. WebKit developer tools automatically handle this, checking the first three characters of the source map to determine if the syntax error should be applied and removing all characters leading to the first newline if necessary.

