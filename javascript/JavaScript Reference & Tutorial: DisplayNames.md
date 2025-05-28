---

title: JavaScript DisplayNames: Function and Internationalization

date: 2025-05-26

---


# JavaScript DisplayNames: Function and Internationalization

JavaScript developers have access to powerful features for function customization and internationalization through the Function.displayName property and the Intl.DisplayNames API. These tools enable developers to control how functions and locale information are presented in the console, profilers, and applications. The Function.displayName property allows setting custom display names with specific processing rules, while the Intl.DisplayNames API provides localized language, region, script, and currency names. Understanding and utilizing these features ensures better developer experience and more informative console output across different platforms and locales.


## Function.displayName Property

The Function.displayName property allows developers to specify a display name for JavaScript functions. The property is set using the syntax `function.displayName = name`. If the property is not explicitly set, the default display name is undefined.

According to the documentation, the property follows specific patterns when displaying names:

- For names ending in alphanumeric characters followed by `_` and `$`, the longest such suffix is displayed.

- For names ending in `[]`-enclosed characters, those sequences are displayed without the brackets.

- For names ending in alphanumeric characters followed by `_` and then `/`, `.`, or `<`, the sequence is returned without the trailing `/`, `.`, or `<`.

- If none of these patterns match, the entire name is displayed.

Browser support for this property is strong, with native implementation in Mozilla Firefox. The property is utilized by the browser's console and profilers to display function names. A practical example of dynamic displayName setting and usage is shown below:

```javascript

const object = {

  someMethod: function someMethod(value) {

    someMethod.displayName = `someMethod (${value})`;

  },

};

console.log(object.someMethod.displayName); // undefined

object.someMethod("123");

console.log(object.someMethod.displayName); // "someMethod (123)"

```

The property can also be manipulated within arrays and methods, as demonstrated in the following code segment:

```javascript

function foo() {}

function testName(name) {

  foo.displayName = name;

  console.log(foo);

}

testName("$foo$"); // function $foo$()

testName("foo bar"); // function bar()

testName("Foo.prototype.add"); // function add()

testName("foo ."); // function foo .

testName("foo<"); // function foo<

testName("foo?"); // function foo?

testName("foo()"); // function foo()

testName("[...]"); // function ...

testName("foo<"); // function foo<

testName("foo..."); // function foo<

testName("foo(^)"); // function foo()

```


## Intl.DisplayNames for Language and Region Display Names

The Intl.DisplayNames API enables JavaScript developers to access the Unicode CLDR package's translations of language, region, script, and currency names. It provides four main types of display names: region names using ISO-3166 2-letter country codes, language names using Unicode language identifier grammar, currency names using ISO-4217 3-letter currency codes, and script names using ISO-15924 4-letter script codes. The API supports customization through its options parameter, which includes localeMatcher, type, and style properties.

The type property specifies the type of display name and can be "region", "language", "currency", or "script". The style property controls the display width of the name and has three options: "long", "short", or "narrow". The API provides methods for creating instances of Intl.DisplayNames and retrieving specific display names. For region code display names in English, the API supports both ISO-3166 2-letter country codes and UN M49 3-digit region codes. For language display names in English, it follows Unicode's language identifier grammar.

Browser support for the Intl.DisplayNames API is strong, with full support across Edge, Firefox, IE, Opera, Safari, WebView Android, Chrome Android, and other relevant platforms. The feature has been widely available since April 2021, with support in Chrome since version 81, Firefox since version 86, and Safari since version 14. The API continues to evolve, with plans for broader adoption as libraries and applications transition from shipping their own translation data to using native functionality.


## Usage Examples: Function displayName and Intl.DisplayNames

The Function.displayName property allows setting custom display names for functions, with specific patterns for how names are processed and displayed. The property follows these rules when displaying names:

- For names ending in alphanumeric characters followed by `_` and `$`, the longest such suffix is displayed.

- For names ending in `[]`-enclosed characters, those sequences are displayed without the brackets.

- For names ending in alphanumeric characters followed by `_` and then `/`, `.`, or `<`, the sequence is returned without the trailing `/`, `.`, or `<`.

- If none of these patterns match, the entire name is displayed.

Here's how you can use the Function.displayName property:

```javascript

function customFunction() {}

customFunction.displayName = "Custom Function Name";

console.log(customFunction); // ƒ Custom Function Name()

console.log(customFunction.name); // Custom Function Name

console.log(customFunction.displayName); // Custom Function Name

const object = {

  someMethod: function someMethod(value) {

    someMethod.displayName = `someMethod (${value})`;

  },

};

console.log(object.someMethod.displayName); // undefined

object.someMethod("123");

console.log(object.someMethod.displayName); // "someMethod (123)"

```

Mozilla Firefox utilizes the Function.displayName property for its console and profilers to display function names. To ensure compatibility across browsers, developers should rely on features that have native implementation in Firefox, as supported properties and behavior may change in the future.

The Intl.DisplayNames API provides localized display names for languages, regions, scripts, and currencies, with full support across major browsers and platforms. To use the API, create an instance with the desired locale and options, and call the of() method with the appropriate code. The available options include:

- `localeMatcher`: matches the input to the closest available locale

- `type`: specifies the type of display name (region, language, currency, script)

- `style`: controls the display width (long, short, narrow)

Here's an example usage of the API:

```javascript

const regionNames = new Intl.DisplayNames(['en'], { type: 'region' });

const languageNames = new Intl.DisplayNames(['en'], { type: 'language' });

console.log(regionNames.of('US')); // United States

console.log(regionNames.of('BZ')); // Belize

console.log(languageNames.of('en')); // English

```

The API supports both ISO-3166 2-letter country codes and UN M49 3-digit region codes for regions, Unicode language identifier grammar for languages, ISO-4217 3-letter currency codes for currencies, and ISO-15924 4-letter script codes for scripts. For complete translation data, developers should use the native functionality rather than shipping their own translation packages.

