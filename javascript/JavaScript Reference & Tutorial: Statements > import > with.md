---

title: JavaScript Import and Statement Usage

date: 2025-05-27

---


# JavaScript Import and Statement Usage

JavaScript's import statement represents a fundamental shift in how developers structure and organize their code, enabling more modular and maintainable applications. This article explores the various aspects of JavaScript's import system, from basic syntax to advanced usage patterns and best practices. We'll examine how import statements work with different module types, how they interact with the developer's environment, and how modern JavaScript tools support and extend this functionality. Along the way, we'll uncover hidden gotchas, performance considerations, and security implications that every developer should understand when working with ES modules.


## JavaScript's import Statement

The import statement enables JavaScript modules to import functionality from one another. These imports can take several forms, including curly braces for named imports, asterisks for namespace imports, and default import syntax.

Named imports allow developers to import multiple exports from a single module while optionally renaming them:

```javascript

import { myExport } from "/modules/my-module.js";

import { foo, bar } from "/modules/my-module.js";

import { reallyReallyLongModuleExportName as shortName } from "/modules/my-module.js";

```

Namespace imports create a sealed object containing all module exports as properties:

```javascript

import * as myModule from "/modules/my-module.js";

myModule.doAllTheAmazingThings();

```

The default export can be accessed through a dedicated key:

```javascript

import { default as myDefault } from "/modules/my-module.js";

```

ES modules follow specific resolution rules for import specifiers. Relative specifiers beginning with `/`, `./`, or `../` are resolved relative to the current module URL, while absolute specifiers can be any parsable URL. The most common specifier types are:

- `/relative/path.js`: Resolves relative to the current module URL

- `http://example.com/module.js`: Absolute URL, resolved as-is

- `bareSpecifier.js`: Resolves through the host environment's module resolution rules

Supported MIME types include `text/javascript` for JavaScript, `application/json` for JSON modules, and `application/wasm` for WebAssembly modules. Data URLs for modules require specific import attributes, with `text/javascript` URLs interpreted as modules but unable to use relative imports due to the `data:` scheme's lack of hierarchy.

When implementing ES modules in development environments, developers must address several considerations:

- Configuration: Update `tsconfig.json` with appropriate compiler options for TypeScript projects:

```json

{

  "compilerOptions": {

    "module": "es20215",

    "target": "es20215",

    "sourceMap": true

  }

}

```

Node.js projects require enabling ES module support with the `--experimental-modules` flag or using a compatible version. For older Node.js versions, projects can enable ES module support with:

```javascript

module.exports = {

  entry: './src/index.ts',

  output: {

    filename: 'bundle.js',

    path: path.resolve(__dirname, 'dist')

  },

  resolve: {

    extensions: ['.ts', '.js', '.mjs']

  },

  module: {

    rules: [

      { test: /.ts$/, use: 'ts-loader', exclude: /node_modules/ }

    ]

  },

  experiments: { outputModule: true }

};

```

Browser compatibility requires careful configuration. Modern browsers support ES modules directly, but older versions need polyfills or transpilers. The root HTML file should include the script tag with the `type="module"` attribute:

```html

<script type="module" src="app.js"></script>

```

Developers must also address cross-origin resource-sharing errors when loading modules from different domains. Webpack can transpile code for older browsers, and developers should check browser compatibility using resources like Can I Use (https://caniuse.com/).


## import Statement Syntax and Usage

The import statement's syntax appears simple but can be misleading, particularly when dealing with curly braces for destructuring syntax. Identifier names in import statements do not necessarily correspond to the contents of the imported file; instead, they represent how imported items will be accessed in the current scope.

For example, the following code demonstrates a common pattern of exporting a function and later renaming it:

```javascript

// utilities.js

export function dogs() { /* ... */ }

export function monkeys() { /* ... */ }

```

In the importing module:

```javascript

import utility from "./utilities"; // utility.dogs() and utility.monkeys() are available

```

While it's technically possible to rename functions like this for import purposes, this practice is generally discouraged for clarity.

When importing multiple items, the object destructuring syntax requires matching names between the export and import statements:

```javascript

// utilities.js

export function cows() { /* ... */ }

export function cats() { /* ... */ }

```

```javascript

import { cows, cats } from "./utilities"; // This works

import { dogs, cats } from "./utilities"; // This causes a SyntaxError

```

The import statement can use the as keyword to assign custom names to imported identifiers, though this practice is rarely needed due to the matching requirements between export and import names:

```javascript

import { dogs as myDogs } from "./utilities"; // This is valid but uncommon

```

The most common usage pattern groups all exported items into a single object, which must be accessed using the specified names:

```javascript

import * as utilities from "./utilities"; // utilities.dogs() and utilities.monkeys() are available

```

This approach does not allow renaming individual exports, but developers must maintain awareness of the original export names to access them.


## JavaScript Statements Overview

JavaScript statements form the core building blocks of programs, executed sequentially by web browsers. Each statement consists of values, operators, expressions, keywords, and comments, following a basic structure that developers can build upon.

Statements begin with keywords such as `var`, `let`, and `const` for declaring variables and constants, `if` and `switch` for conditional logic, and `for` for iterative processes. These foundational elements enable script authors to control program flow and perform operations efficiently.

A key aspect of JavaScript syntax is its use of semicolons to separate statements, though the language allows for implicit statement termination in many cases. For optimal readability and compatibility, developers are encouraged to maintain explicit semicolon usage, particularly in more complex expressions and multi-line statements.

The language's architecture supports several distinct types of statements, including conditional logic, loop structures, and object manipulation operations. While detailed object manipulation statements fall outside the scope of this overview, developers should be aware of the fundamental mechanisms supporting these operations through expressions, properties, and functions.

Understanding JavaScript statements forms the basis for effective programming practice, allowing developers to construct dynamic, responsive applications that execute efficiently across modern web environments.


## with Statement and Contextual Usage

The `with` statement extends the scope chain for a statement by adding the given object to the head of the scope chain during evaluation. It works by searching the object for the specified identifier through an `in` check before searching the upper scope chain. The statement can contain multiple statements enclosed in a block statement (`{ ... }`). It has two types of identifiers: unqualified and qualified. Unqualified identifiers are resolved by searching the scope chain, while qualified identifiers are resolved by searching the prototype chain of an object. The global object sits on top of the scope chain and its properties automatically become global variables without qualifiers.


### Historical Usage and Modern Alternatives

Despite its established presence in JavaScript, the `with` statement has faced criticism for its performance impact and readability issues. The primary concern with `with` is the performance overhead it introduces by forcing the specified object to be searched first for all name lookups. This makes all identifiers slower to find within the `with` block, and the optimizer cannot make assumptions about identifier references, requiring repeated property lookups.

Developers often use `with` to save a temporary variable or to reduce file size by avoiding repeated object references. However, modern JavaScript provides alternative approaches for these use cases. For example, when manipulating deeply nested object structures, developers can use destructuring assignment to create local bindings:

```javascript

const { info } = data[i];

nodes[i].onclick = function() { showStuff(info) };

```

Additionally, JavaScript offers advanced features like Proxy objects to achieve similar functionality with more control. In scenarios where `with` has proven beneficial, alternatives include carefully managing scope with let and const declarations, or using namespace objects to encapsulate related functionality.


### Performance Considerations

Performance benchmarking has shown that the "flat" version of an object is 36% faster to search when using `with()`. By limiting the scope to top-level keys, developers can achieve similar performance to the native `with()` function. The decision to use `with` should be based on coding simplicity and ease of refactoring rather than performance concerns. In most typical usage scenarios, the performance difference is minor, especially in comparison to other optimization opportunities available in JavaScript development.


### Security and Best Practices

The `with` statement's primary security risk is accidental variable leakage. A single missing key in an object can expose unexpected values, as demonstrated in database call scenarios where missing expected keys can lead to security vulnerabilities. Additionally, the statement makes code harder to minify and debug, as it indicates multiple scopes (function, closure, global) and increases the likelihood of name collisions. In environments with strict variable management requirements, the `with` statement's global scope implications make it particularly problematic.

Modern JavaScript development practices recommend avoiding `with` statements due to their known drawbacks. However, certain libraries and frameworks continue to implement their own versions of scoped variables using similar mechanisms. Before adopting any scoped variable solution, developers should carefully evaluate the trade-offs between performance benefits and maintainability concerns.


## Module Implementation and Best Practices

The decision to place import statements at the bottom of a JavaScript file appears to be a matter of personal preference rather than an enforced language requirement. While function hoisting in JavaScript allows functions to be called before their definition, the practice of placing all import statements at the top of the file remains a common convention for maintaining clear code organization.

However, this conventional approach can cause issues when using module bundlers, which require all import statements to be reordered to the top of the file before processing. Placing imports at the bottom may simplify file management for IDEs that support code folding, but it can make dependencies less apparent and potentially cause confusion for developers who expect to find import statements at the top of a file.

Modern JavaScript development best practices generally recommend following the conventional approach of placing import statements at the top of the file. This approach improves code readability and maintains consistency across development environments, while the modern module bundlers handle the internal reordering of imports as needed. Proper configuration of development tools and understanding of module bundler requirements are essential for effective JavaScript development using ES6 import statements.

