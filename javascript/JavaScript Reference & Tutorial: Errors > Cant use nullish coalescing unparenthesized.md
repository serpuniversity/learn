---

title: JavaScript Nullish Coalescing Operator Best Practices

date: 2025-05-26

---


# JavaScript Nullish Coalescing Operator Best Practices

The JavaScript nullish coalescing operator (??) introduced in 2020's ECMAScript specification offers developers a precise tool for handling null and undefined values. While similar to the logical OR operator in its short-circuiting behavior, ?? specifically addresses common pitfalls with falsy values, making it essential for modern JavaScript development. From defensive coding practices to advanced object pattern matching, this article explores the operator's nuanced behavior across different scenarios and environments, helping developers master this powerful new tool while maintaining compatibility with older JavaScript ecosystems.


## Nullish Coalescing Operator Overview

The nullish coalescing operator (??) was introduced in JavaScript's 2020 specification as a new logical operator. It works between two operands, returning the first operand if it is not null or undefined. If the first operand is null or undefined, it returns the second operand from the expression. This operator behaves similarly to the logical OR operator (||) in short-circuiting behavior but specifically checks for nullish values (null and undefined).

Let's break down its behavior with different types of values. The operator returns the first operand if it is not null or undefined, effectively providing a default value when the primary value is nullish. For example, if `expression1()` returns null, and `expression2()` returns "Dillion", the nullish operator returns "Dillion" because `expression1()` is nullish.

The operator distinguishes between nullish and falsey values, making it particularly useful for handling values that may be empty or falsy. Consider the function `Component(props)`: previously, `props.enabled || true` evaluated to true for various falsy values including `undefined`, `false`, `0`, `NaN`, and the empty string ''. The introduction of the nullish coalescing operator allows for more precise default handling:

```javascript

function Component(props) {

  const enable = props.enabled ?? true;

}

```

This change ensures that `enable` correctly evaluates based on whether `props.enabled` is null or undefined, rather than simply any falsy value.

When combined with other operators or expressions, understanding correct syntax and evaluation order becomes crucial. The nullish operator has the same precedence as the OR operator (level 3 in MDN's operator precedence table), making it crucial to use parentheses correctly to control evaluation:

```javascript

let area = (height ?? 100) * (width ?? 50);

```

This ensures both height and width are properly evaluated before multiplication. The operator's ability to short-circuit evaluation—only computing the right operand when the left is nullish—makes it particularly powerful for defensive coding practices.

The operator's recent introduction means compatibility across different JavaScript environments requires careful consideration. For developers targeting older browsers or environments, using tools like Babel for transpilation becomes essential to maintain this feature while ensuring broad compatibility.


## Operator Precedence and Syntax

The nullish coalescing operator (??) and OR operator (||) share similarities in their short-circuiting behavior but differ in how they handle falsy values. The nullish operator specifically checks for null and undefined values, returning the second operand only when the first is nullish. In contrast, the OR operator treats any falsy value (including 0, '', false) as a valid condition for returning the second operand.

The primary syntactic restriction is that the nullish coalescing operator cannot be directly combined with AND (&&) or OR (||) operators in the same expression without causing a SyntaxError. For example, attempting to evaluate `null || undefined ?? "foo"` or `true || undefined ?? "foo"` will result in an error. To correctly implement these expressions, developers must use parentheses to explicitly define evaluation order, such as `(null || undefined) ?? "foo"`.

This behavior stems from the intentional undefined precedence between &&/|| and ?? operators, designed to prevent counterintuitive expression evaluation. As a result, developers should avoid attempting to chain nullish coalescing directly with && or || operators. Instead, they can use optional chaining (?.) as an alternative for null/undefined handling where appropriate. This approach allows maintaining clear code while adhering to the language's operator precedence rules.


## Using Nullish Coalescing with Objects

Destructuring with default values is a common pattern in JavaScript, and the nullish coalescing operator provides a safer alternative to traditional null checks. Consider the following example where a function receives an object with potential missing properties:

```javascript

function Component({ content = "", title = "Missing Title", date = "" }) {

  const props = {

    content,

    title,

    date

  };

  console.log(props);

  // Output will vary based on input, but will never include undefined for missing properties

}

```

This approach allows maintaining clean, readable code while ensuring default values are used when properties are missing. However, developers working with TypeScript strict mode must be particularly careful, especially when dealing with GraphQL-generated `Maybe<T>` types. A robust pattern might look like this:

```typescript

function safeProps<T extends object>(source: T): T {

  return Object.fromEntries(

    Object.entries(source).map(([key, value]) => [key, value ?? undefined])

  ) as T;

}

```

This utility function safely converts all null and undefined values to undefined, making it easier to work with strict type checking. When combined with optional chaining and nullish coalescing, developers can write defensively while maintaining type safety:

```javascript

const element = document.querySelector(".some-element");

const link = element?.querySelector("a[href]") ?? document.createElement("link");

```

In this example, if the element is not found, the code safely creates a new link element without throwing an error. The nullish coalescing operator's short-circuiting behavior makes these patterns particularly powerful for ensuring safe property access while maintaining performance.


## Comparison with Logical OR Operator

The nullish coalescing operator (??) and logical OR (||) operators share similarities in their short-circuiting behavior but fundamentally differ in how they handle falsy values. While both operators return the second operand when the first is falsy, their definitions of "falsy" values diverge significantly.

The OR operator treats any falsy value (0, '', false) as a valid condition for returning the second operand, while the nullish coalescing operator specifically checks for null and undefined values, returning the second operand only when the first is nullish. This difference becomes particularly important in scenarios where developers need to distinguish between null/undefined and other falsy values.

The operators' distinct behaviors lead to different outcomes in certain situations. Consider a simple example where a variable may contain an empty string, which is valid in many contexts:

Using OR:

```javascript

let age1 = ''; // empty string

age1 || 21; // returns 21

```

Here, the empty string is considered falsy, and the OR operator returns the second operand.

In contrast, using nullish coalescing:

```javascript

let age2 = ''; // same empty string

age2 ?? 21; // returns 21

```

In this case, the nullish coalescing operator returns the second operand, treating the empty string as a valid value.

These distinctions become crucial in real-world scenarios. For instance, in Angular applications, developers frequently use property access with nullish coalescing:

```javascript

const keyword = this.route.snapshot.queryParamMap.get('keyword') ?? 'default keyword';

const page = this.route.snapshot.queryParamMap.get('page') ?? '0';

```

Similarly, safe property access patterns become more precise:

```javascript

const content = postData?.content ?? '';

const title = postData?.title ?? 'Default Title';

```

While both operators are designed to handle null and undefined values, the nullish coalescing operator's more specific behavior makes it particularly useful for modern JavaScript development. This precision helps developers avoid unintended behavior when working with falsy values that should remain defined, such as 0 or empty strings.

The operators' different scopes—nullish coalescing operating specifically within JavaScript while logical OR working across languages—reflect their distinct design philosophies. Modern JavaScript development can leverage these operators effectively, though developers must understand their behaviors to avoid potential pitfalls. The nullish coalescing operator's precision in handling null and undefined values makes it a valuable addition to JavaScript's operator suite, particularly when working with modern frameworks and typesafe environments.


## Browser Support and Migration Considerations

The nullish coalescing operator (??) was added to TypeScript 3.7 in November 2019 and included in ES2020, with Node 14 supporting it starting in April 2020. While the operator is powerful for modern JavaScript development, developers targeting older environments must consider compatibility.


### Browser Support

As of 2023, the nullish coalescing operator is widely supported in modern browsers. Chrome, Safari, Edge, and Firefox all support the operator natively. However, compatibility issues arise in V8-based environments for expressions combining nullish coalescing with logical OR (||) or AND (&&), where the operator precedence can cause SyntaxErrors. Developers should be particularly cautious when upgrading codebases between these browsers.


### Migration Best Practices

When migrating from traditional null/undefined checking with ||, developers should thoroughly test their applications for any unintended behavior. The nullish coalescing operator generally introduces less cognitive load for determining potential bugs, though developers should understand its specific behavior with null and undefined values.

For TypeScript developers working with strict mode and GraphQL-generated Maybe<T> types, using a utility function approach can help maintain type safety. This pattern allows converting all null and undefined values to undefined, making the codebase more robust:

```typescript

function nullToUndefinedSource<T extends object, ResultType = NullToUndefined<T>>(object: T): ResultType {

  return Object.fromEntries(

    Object.entries(object).map(([key, value]) => [key, value ?? undefined])

  ) as ResultType;

}

function nullToUndefinedTarget<T extends object, ResultType = NullToUndefined<T>>(object: T): ResultType {

  const source = object as { [key: string]: any };

  const result: { [key: string]: any } = {};

  for (const key in object) {

    if (Object.hasOwn(object, key)) {

      result[key] = source[key] ?? undefined;

    }

  }

  return result as ResultType;

}

```

These functions convert null values to undefined across object properties, maintaining type safety while ensuring compatibility with older TypeScript versions that lack direct support for nullish coalescing.

