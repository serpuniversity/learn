---

title: JavaScript DisplayNames: Language and Text Display

date: 2025-05-26

---


# JavaScript DisplayNames: Language and Text Display

JavaScript's Intl.DisplayNames object offers robust solutions for localizing language, region, script, and currency names. By providing detailed control through its constructor and methods, it enables developers to display names in the desired style and type. In a separate functionality, the Function.displayName property allows custom naming patterns for JavaScript functions, particularly useful in development tools and component debugging. Together, these features enhance both internationalization capabilities and development practice, making them essential knowledge for modern JavaScript developers.


## Display Names in JavaScript

The Intl.DisplayNames object provides a comprehensive framework for displaying localized names of languages, regions, scripts, and currencies. It requires a locale identifier (as a string or Intl.Locale instance) and an options object that can include properties like style, type, and fallback.

This constructor creates objects capable of displaying various types of names:

- New `Intl.DisplayNames` objects can be created with parameters like "en" for English, "de" for German, "fr-CA" for Canadian French, "zh-Hant" for Traditional Chinese, and "en-US" for American English.

- For script display names, constructors like `new Intl.DisplayNames('zh-Hant')` return names such as "Latin" for 'Latn', "Arabic" for 'Arab', and "Katakana" for 'Kana'.

- Currency display names take ISO-4217 3-letter codes, returning names like "US Dollar" for USD, "Euro" for EUR, "New Taiwan Dollar" for TWD, and "Chinese Yuan" for CNY.

- Region codes must follow ISO-3166 formatting, while script codes require ISO-15924 formatting.

The static `supportedLocalesOf(locales, options)` method returns supported locales without falling back to the runtime's default locale, supporting both string and array inputs. Browser compatibility spans desktop and mobile platforms, with official support from Chrome 81, Firefox 86, Safari 14, and Node.js 14.

The object's `of(code)` method processes codes based on the specified type: region codes require ISO-3166 2-letter country codes or UN M49 3-digit region codes, while language codes must conform to Unicode's language identifier grammar. The style parameter controls display width with options "long" (default), "short", and "narrow". The fallback option works for structurally valid but unsupported codes, returning either the input code or undefined based on the chosen fallback strategy.


## Intl.DisplayNames Constructor and Methods

The `Intl.DisplayNames` constructor creates objects that enable consistent translation of language, region, and script display names, with compatibility across desktop and mobile browsers since April 2021. It requires a second parameter called `options`, which includes `localeMatcher`, `type`, and `style` properties. The constructor supports four main types of display names: region names using ISO-3166 2-letter country codes, language names using Unicode language identifier grammar, currency names using ISO-4217 3-letter currency codes, and script names using ISO-15924 4-letter script codes.

The static `supportedLocalesOf(locales, options)` method returns an array of locales supported without falling back to the runtime's default locale, supporting both string and array inputs. The object's methods operate differently based on the instance's type. For region names, `code` must be either an ISO-3166 2-letter country code or UN M49 3-digit region code. For language names, `code` must conform to Unicode's language identifier grammar. For currency names, `code` must be an ISO-4217 3-letter currency code. For script names, `code` must be an ISO-15924 4-letter script code.

The `Intl.DisplayNames` constructor has several properties for customization:

- `type`: Specifies the display type (e.g., "region", "language", "currency", "script")

- `languageDisplay`: Determines how language is displayed (e.g., "dialect", "standard")

- `fallback`: Specifies what to return if the input is structurally valid but there's no matching display name (default: "code")

- `localeMatcher`: Specifies the locale matching algorithm, with possible values "lookup" and "best fit" (default: "best fit")

- `style`: Specifies the formatting style, with possible values "narrow", "short", and "long" (default: "long")

When used with "language" type, the "dialect" as the languageDisplay option is supported. fallbacks only work for structurally valid codes, returning either the input code or undefined based on the chosen fallback strategy. The constructor throws TypeError if options.type is not provided and RangeError if locales or options contain invalid values.


## Function.displayName Property

Firefox's implementation of the Function.displayName property processes display names with specific patterns:

- If the displayName ends with a sequence of alphanumeric characters, an underscore, and a dollar sign ($), the longest such suffix is displayed.

- If the displayName ends with a sequence of brackets []-enclosed characters, that sequence is displayed without the square brackets.

- If the displayName ends with a sequence of alphanumeric characters followed by an underscore and one of the characters '/', '.', or '<', the sequence is returned without the trailing character. For example, a pattern ending in _/ returns everything up to the /, while _< returns everything up to the <.

- If none of these patterns match, the entire displayName is displayed.

Firefox's devtools cleanup common patterns before displaying the name, including:

- Trimming trailing []-enclosed characters

- Removing trailing /, ., or < characters

- Removing trailing (^) characters

- Trimming trailing alphanumeric characters and underscore (_) followed by /, ., or <

- Trimming trailing alphanumeric characters and underscore (_) followed by (^)

The property can be set dynamically using code like:

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

In React, the displayName property is used by JSX to display component names when rendering. To access this property from within a component, you can use this.constructor.displayName for components that have been mounted. For components that have been minimized by Webpack, the displayName is replaced with a shorter identifier (t in this case), and can be accessed using this.constructor.name. The text explains that this.name is replaced by Webpack in production builds, while the displayName remains available in development mode.

Both the class name and the constructor's displayName can be accessed from outside the component instance using Component.name / Component.displayName, while anonymous classes/functions have undefined name and displayName properties. Code minification can change or remove displayName, so best practice for using Component names is to try displayName, fall back to name, and finally use hardcoded strings like 'Component' or 'Anonymous'. Higher-order components (HOCs) can use displayName to customize debugging information.


## Display Name Customization and Patterns

Firefox's implementation of Function.displayName handles display names with specific patterns: if the name ends with a sequence of alphanumeric characters followed by an underscore and a dollar sign ($), it displays the longest such suffix. If the name ends with a sequence of brackets []-enclosed characters, those are displayed without the square brackets. For names ending with alphanumeric characters followed by an underscore and one of '/', '.', or '<', the sequence is returned without the trailing character. If none of these patterns match, the entire name is displayed.

The devtools clean up several common patterns before displaying the name: trailing []-enclosed characters are trimmed, as are trailing /, ., or < characters. Trailing (^) characters are also removed. Alphanumeric characters followed by underscore and either /, ., or < are trimmed. Finally, alphanumeric characters followed by underscore and (^) are also trimmed.

The property can be set dynamically with code like:

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

In React development tools, the displayName property is used when displaying the component tree. Both the class name and constructor's displayName can be accessed from outside the component instance using Component.name / Component.displayName, with anonymous classes/functions having undefined name and displayName properties. Code minification can change or remove displayName, so best practice for using Component names is to try displayName, fall back to name, and finally use hardcoded strings like 'Component' or 'Anonymous'. Higher-order components (HOCs) can use displayName to customize debugging information.


## Display Name Best Practices

The `displayName` property in React serves as a key identifier for components, particularly when rendered by JSX. To access this property, developers can use `this.constructor.displayName` for mounted components, while Webpack-minimized components display a shorter identifier ("t" by default). Code minification frequently alters or removes `displayName`, making it essential to implement best practices for component identification.

In development mode, both class names and constructor's display names are accessible via `Component.name / Component.displayName`. Anonymous classes/functions lack `name` and `displayName` properties, highlighting the need for alternative identifiers. Best practice for using Component names recommends checking `displayName` first, falling back to `name`, and finally using hardcoded strings like 'Component' or 'Anonymous'. Higher-order components (HOCs) leverage `displayName` to enhance debugging information.

In practice, developers should adopt consistent naming conventions for components. Custom display names can be set on class components or stateless functional components using the syntax `function.displayName = "name"`. For example, a class component might define a custom display name as follows:

```javascript

class CustomComponent extends React.Component {

  static displayName = 'CustomComponent';

  render() { return <div>Custom Component</div>; }

}

```

This approach facilitates clearer component identification in development tools and documentation, while maintaining compatibility across minification processes.

