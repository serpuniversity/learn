---

title: JavaScript: eval in Strict Mode

date: 2025-05-26

---


# JavaScript: eval in Strict Mode

The `eval()` function stands as a powerful and controversial feature of JavaScript, capable of evaluating strings as executable code while the `Function()` constructor creates function objects with their own lexical scope. While widely supported across modern browsers, `eval()` presents significant performance and security challenges, particularly in strict mode. This article explores the fundamentals of `eval()`, its behavior and limitations in strict mode, and provides best practices for safe and efficient JavaScript development.


## Overview of eval

The `eval()` method in JavaScript evaluates code represented as a string, while the `Function()` constructor creates function objects with their own lexical scope. When evaluating expressions, `eval()` returns the corresponding value, and when evaluating statements, it executes them and returns the completion value. The function takes a single string parameter and runs JavaScript code in the current lexical scope, making it a powerful but risky tool.

A major limitation of `eval()` is its performance impact due to dynamic string evaluation. This slowness is exacerbated in strict mode, where the function creates local variables for the evaluated code rather than modifying the outer scope. However, the function remains widely supported across modern browsers, including Chrome, Edge, Firefox, Safari, and Opera.

The security risks of `eval()` are well-documented, as it allows execution of arbitrary code and can be exploited through code injection attacks. Even seemingly innocuous uses, like checking for malware through `eval("String.fromCharCode(72, 101, 108, 108, 111)")`, demonstrate its potential to facilitate malicious activities. The function's ability to modify the surrounding scope and perform expensive variable lookups further compounds these risks.

Developers often turn to alternatives like `window.Function()` or specific JSON parsing methods to achieve similar functionality more safely. For complex evaluations, creating functions with parameter bindings using `Function()` can offer better performance and security. Overall, while `eval()` remains a powerful tool in JavaScript, its use should be approached with extreme caution, particularly in environments where user input is involved.


## Strict Mode Restrictions

In strict mode, JavaScript reserves the identifiers 'eval' and 'arguments' as keywords, preventing them from being used as variable names or formal parameters. This restriction applies uniformly across strict mode functions, whether declared with simple parameters or more complex structures like default parameters, rest parameters, or destructuring.

These restrictions serve several purposes:

1. Prevention of accidental code injection: By disallowing 'eval' as a variable name, strict mode prevents developers from inadvertently shadowing the built-in function, which could lead to security vulnerabilities.

2. Improved error handling: The ban on using 'eval' and 'arguments' as identifiers converts certain JavaScript silent errors into explicit exceptions, making debugging easier and security issues more apparent.

3. Enhanced language consistency: Disallowing duplicate parameter names, including those involving 'eval' and 'arguments', simplifies the compiler's task of mapping variable references to specific definitions, enabling better optimization opportunities.

This strict treatment of 'eval' and 'arguments' aligns with strict mode's overall goal of converting common coding errors into explicit exceptions, while maintaining compatibility with older JavaScript syntax through careful design. The restrictions apply to both script-level and function-level strict mode, ensuring consistent behavior across global and local scopes.


## Behavior in Strict Mode

In strict mode, the `eval()` function demonstrates several key differences from its behavior in sloppy mode:


### Local Variable Scope

When evaluating code in strict mode, `eval()` creates local variables for the evaluated code, similar to how function declarations work. This means that any variables declared or modified within `eval()` are restricted to that local scope and do not affect outer variable references. This behavior is distinct from sloppy mode, where `eval()` could introduce new variables into the surrounding function or global scope, requiring runtime mapping to determine specific variable definitions.


### Variable Resolution

Strict mode enforces a clear separation between evaluated code and the surrounding scope. Variables declared inside `eval()` are only visible within that evaluation context, preventing accidental global variable creation. This differs from sloppy mode, where `eval()` could create variables in the surrounding scope, leading to potential conflicts and hard-to-debug issues when the evaluated string is acquired from external input.


### Performance and Optimization

The local scoping behavior of `eval()` in strict mode allows JavaScript engines to perform better optimizations. When evaluated strings are confined to local scope, engines can disable optimizations related to inlining and scope inspections that are necessary when variables can be dynamically created or modified in the surrounding scope. This distinction is particularly important in functions with complex scopes, where `eval()` calls might introduce performance overhead due to the need for additional scope inspection.


### Security Considerations

The restricted scoping behavior of `eval()` in strict mode also enhances security by preventing third-party code from accessing or modifying the surrounding scope. This limitation aligns with the broader security model of strict mode, which prevents code from reading or changing local variables that might contain sensitive information. Developers are encouraged to thoroughly test `eval()` usage in strict mode to ensure that no functionality breaks due to the stricter scoping rules.


## Evaluation Differences


### Block-Scoped Function Declarations

The behavior of block-scoped function declarations varies between sloppy and strict modes. In sloppy mode, function declarations inside blocks remain visible outside the block, making them callable from any point within the containing scope. This creates potential for scope pollution and hard-to-debug issues when functions are acquired from external input.

In strict mode, function declarations inside blocks are only visible within the block, matching their behavior in function declarations. This change prevents accidental global function creation and helps maintain cleaner scope management.


### Variable Resolution

Strict mode enforces stricter variable resolution rules compared to sloppy mode. When a variable is accessed within the scope of an evaluated string, strict mode requires that the variable actually exists in that scope. If the variable does not exist, a ReferenceError is thrown rather than creating a global variable, which helps prevent silent errors and makes debugging easier.

For example, consider the following code:

```javascript

{

  "use strict";

  eval("x = 10");

  console.log(x); // ReferenceError: x is not defined

}

```

In contrast, sloppy mode would allow this code to create a global variable `x` without throwing an error:

```javascript

eval("x = 10");

console.log(x); // 10

```


### Performance and Scope Inspections

The differences in variable resolution between modes affect JavaScript engine optimizations. In sloppy mode, engines must perform additional scope inspections to determine variable definitions, especially when dealing with complex scopes or dynamically created variables. Strict mode removes the need for these expensive inspections by ensuring all variables are defined in the evaluation scope.

These optimizations can significantly impact performance, particularly in functions with complex scopes or frequent dynamic variable creation. Developers using `eval()` in strict mode should expect different performance characteristics compared to sloppy mode, especially when working with large or complex code structures.


## Best Practices

The `eval()` function's primary security risk is its vulnerability to code injection attacks. Malicious code can run inside the application without permission, and third-party code can access the scope of the application, leading to potential attacks (MDN Web Docs, Mozilla). Therefore, `eval()` should be used minimally and only when absolutely necessary (Eval is evil).

For processing user input, handling JSON data, or accessing object properties dynamically, developers should consider safer alternatives. JSON data is best managed using JSON.parse(), which allows a subset of JavaScript syntax while enforcing stricter structure rules (MDN Web Docs, Mozilla). For safe expression evaluation, developers should use the Function() constructor whenever possible. This approach enables property access and descendant property handling while providing better performance and security (Mozilla Developer Network).

When working with frequently executed code, alternatives to `eval()` offer significant performance advantages due to reduced runtime compilation requirements. For example, the Function() constructor allows engines to perform more optimizations by parsing the source string as a function body rather than a script (Mozilla Developer Network). Modern JavaScript engines convert JavaScript to machine code, obliterating variable naming concepts and requiring expensive variable name lookups for `eval()` operations.

Developers should thoroughly test `eval()` usage in strict mode to ensure compatibility with stricter scoped variable handling. Avoid `eval()` for property access and descendant property handling, as these use cases can still lead to object injection attacks when using unconstrained input (Mozilla Developer Network). Always prefer safer alternatives when possible to maintain robust security practices and improve code maintainability.

