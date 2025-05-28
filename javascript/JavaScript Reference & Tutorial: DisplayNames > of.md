---

title: JavaScript Display Names: Functions and Internationalization

date: 2025-05-26

---


# JavaScript Display Names: Functions and Internationalization

JavaScript's Function.displayName property and Intl.DisplayNames API offer powerful tools for customizing and localizing function names and object displays. Whether you're debugging complex applications or building internationalized UIs, these features provide precise control over how your code and data are represented. This article explores best practices for setting display names, implementing localization with Intl.DisplayNames, and efficiently displaying object properties in JavaScript.


## Function displayName Property

The Function.displayName property in JavaScript allows developers to set a custom display name for functions, overriding the default which is undefined. This property affects how functions appear in consoles and profilers.

Setting the displayName property is straightforward. As shown in the first example from the documentation, developers can assign a custom name to a function:

```javascript

function func1() { }

func1.displayName = "someName"

console.log(func1.displayName) // Output: someName

```

In the second example, the displayName property is used to override the default function name:

```javascript

function func() { }

func.displayName = "function1"

console.log(func) // Output: ƒ function1()

console.log(func.name) // Output: function1

console.log(func.displayName) // Output: function1

```

Firefox implements displayName processing using several patterns. If the displayName ends with a sequence of alphanumeric characters, underscores, and dollar signs, the longest such suffix is displayed. For instance:

```javascript

function foo() {}

foo.displayName = "$foo$";

console.log(foo); // Output: function $foo$()

```

If displayName ends with square-bracket-enclosed characters, those are displayed without the brackets:

```javascript

foo.displayName = "[foo]";

console.log(foo); // Output: function foo()

```

For cases ending with alphanumeric characters and an underscore followed by certain characters (/, ., or <), the sequence is displayed without the trailing character:

```javascript

foo.displayName = "foo/";

console.log(foo); // Output: function foo()

```

If none of these patterns match, the entire displayName is displayed:

```javascript

foo.displayName = "foo^";

console.log(foo); // Output: function foo^()

```

Firefox's display process further cleans up patterns by removing trailing alphanumeric characters and underscores followed by certain characters (/ , ., <), trimming square-bracket-enclosed characters, and removing specific suffix patterns (^).

The property also supports dynamic setting through object methods. In the provided example, the displayName property can be updated after function creation:

```javascript

const object = {

  someMethod: function someMethod(value) {

    someMethod.displayName = `someMethod (${value})`;

  },

};

console.log(object.someMethod.displayName); // Output: undefined

object.someMethod("123");

console.log(object.someMethod.displayName); // Output: "someMethod (123)"

```


## Intl.DisplayNames for Language and Region Names

The Intl.DisplayNames API provides language and region display names based on locale rules, supporting multiple language variants and script types through its options parameter. Here's a detailed look at its functionality and implementation:


### Constructor and Configuration

The API is instantiated with the constructor:

```javascript

new Intl.DisplayNames(locale, options)

```

Where `locale` specifies the user's language and `options` can include:

- `type`: Determines the type of display names (language, region, script, currency)

- `localeMatcher`: Specifies the matching algorithm ("lookup" or "best fit"; default is "best fit")

- `style`: Controls display name width ("long", "short", or "narrow"; default is "long")


### Display Name Retrieval

The primary method, `.of(code)`, returns a string based on the given `code` and locale options:

```javascript

const names = new Intl.DisplayNames(['en'], { type: 'language' });

console.log(names.of('en-US')); // "American English"

console.log(names.of('fr-CA')); // "Canadian French"

```


### Supported Locales and Options

The `.supportedLocalesOf(locales, options)` static method returns supported locales without fallback to the default locale:

```javascript

console.log(Intl.DisplayNames.supportedLocalesOf(['en', 'fr', 'ja'], { type: 'region' })); // ["fr", "ja"]

```


### Polyfill and Browser Support

While widely available, browser support varies. The `Intl.DisplayNames` polyfill can be installed via CDN or npm, requiring `Intl.getCanonicalLocales` and `Intl.Locale` (or their polyfills). Current implementation status tracks daily in the Test262 standard test suite, with full support in Chrome 81, Edge 81, and Chrome Android 81.


## Displaying Object Properties and Values

In JavaScript, displaying object properties and values is a fundamental aspect of both practical application development and debugging. The language offers several mechanisms for this task, each suited to different contexts and requirements.


### Displaying Object Properties

The most basic approach to displaying object properties involves simple concatenation, as shown in the example:

```javascript

person.name + "," + person.age + "," + person.city

```

Alternative methods include directly accessing properties within loops, where it's recommended to use `person[x]` rather than `person.x` to ensure flexibility:

```javascript

for (let x in person) {

  text += person[x] + " ";

}

```

More structured approaches exist through array methods like `Object.values()` and `Object.entries()`. These methods transform objects into more accessible formats suitable for processing and display. For instance, to create an array from an object's property values:

```javascript

const myArray = Object.values(person)

```

Or to convert an object into an easily loopable structure:

```javascript

const fruits = {Bananas:300, Oranges:200, Apples:500}

for (let [fruit, value] of Object.entries(fruits)) {

  text += fruit + ": " + value + "<br>";

}

```

This flexibility allows developers to adapt object data display to their specific needs, whether for immediate consumption or integration into larger systems.


### Converting to String

When direct console output is required, the `JSON.stringify()` method provides a robust solution:

```javascript

JSON.stringify(person)

```

This approach produces JSON notation output:

```{"name":"John","age":50,"city":"New York"}```

Notably, this method ensures consistent structure and formatting for object data representation across all major browsers.


## supportedLocalesOf and Formatting Options

The `Intl.DisplayNames.supportedLocalesOf(locales, options)` static method returns an array of locale tags that are supported in display names without relying on the runtime's default locale. This allows developers to ensure that specified locales will correctly map to display names, enhancing both functionality and user experience.

The method processes its parameters as follows:

- `locales`: Accepts a single string with a BCP 47 language tag or an array of such strings. The acceptable formats mirror those supported by the underlying `Intl` object.

- `options`: An optional object containing the `localeMatcher` property, which determines the matching algorithm used. Supported values are "lookup" and "best fit"; "best fit" serves as the default.

The returned array consists of locale tags that match successfully without fallback to the default locale, providing precise control over display name availability.

The `resolvedOptions` method returns a computed object reflecting the formatting options determined during the `Intl.DisplayNames` initialization. This allows developers to inspect the specific settings applied to display name operations, facilitating advanced customization and debugging.

The `style` parameter controls display name width, offering three options:

- "long" (default): Full, detailed display names

- "short": Concise versions of display names

- "narrow": Abbreviated forms for compact displays

Each of these styles impacts the output length while maintaining semantic accuracy, enabling tailored representation based on display requirements.


## Display Names API Implementation Status

As of the latest JavaScript feature implementation status data, the `Intl.DisplayNames` object is supported across multiple platforms, including Edge, Firefox, IE, Opera, Safari, WebView Android, Chrome Android, Firefox Android, Opera Android, Safari iOS, and Samsung Internet Android. Node.js also supports the feature, with full support in Chrome 81, Edge 81, and Chrome Android 81.

The implementation status is tracked daily through the Test262 standard test suite, which generates data by running feature tests in each browser's JavaScript engine. The supported browsers include Google Chrome, Mozilla Firefox, and their respective mobile versions, with Safari and Safari iOS versions 14 and later also providing support.

The object's functionality requires the second parameter `options`, which includes properties for `localeMatcher`, `type`, and `style`. These parameters allow developers to control how display names are retrieved and formatted based on the specified locale rules.

For instance, when creating an instance of `Intl.DisplayNames`, developers can specify the type of display names (language, script, currency) and the style preference (long, short, narrow). The `supportedLocalesOf` static method returns an array of locale tags that can be successfully displayed without fallback to the default locale, ensuring precise control over localization requirements.

