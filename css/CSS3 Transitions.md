---

title: CSS3 Transitions: Implementing Smooth Property Changes

date: 2025-05-26

---


# CSS3 Transitions: Implementing Smooth Property Changes

Smooth transitions enhance web interfaces by animating changes between CSS properties. The CSS3 transition mechanism enables developers to create these visual effects with precise control over timing and behavior. Understanding how to implement transitions effectively requires knowledge of properties like transition-property, transition-duration, and transition-timing-function, as well as options for managing discrete changes and event handling. This article explores the technical details and best practices for implementing smooth property changes in modern web development.


## Basic Usage

The transition-property property determines which CSS properties will be animated. It accepts several values:

- 'none': No properties will transition

- 'all': All properties will transition

- 'property-name': Specific CSS properties for the transition

Multiple properties can be animated by separating them with commas. For example, `transition: opacity 1s, display 1s allow-discrete;` is equivalent to `transition: all 1s allow-discrete;`. The special value 'all' specifies that any CSS property should be animated.

The transition-duration property defines the time for the completion of the transition. It accepts a single value for all properties or multiple values for individual properties. For instance, `transition-duration: 3s, 5s, 2s, 1s` would be interpreted as `transition-duration: 3s, 5s` for the first two properties and 2s, 1s for the following two properties.

The transition-timing-function property controls the speed curve of the transition, with several predefined options:

- 'ease': Slow start, fast middle, slow end (default)

- 'linear': Constant speed

- 'ease-in': Slow start

- 'ease-out': Slow end

- 'ease-in-out': Symmetrical acceleration and deceleration

- 'cubic-bezier(n,n,n,n)': Custom timing function definition

The transition-delay property specifies a delay before starting the transition, accepting values in seconds or milliseconds. Negative values can create the illusion of starting before the trigger event, though the transition still begins immediately.


## Transition Properties

The transition-property property determines which CSS properties will be animated. It accepts several values:

- 'none': No properties will transition

- 'all': All properties will transition

- 'property-name': Specific CSS properties for the transition

Multiple properties can be animated by separating them with commas. For example, `transition: opacity 1s, display 1s allow-discrete;` is equivalent to `transition: all 1s allow-discrete;`. The special value 'all' specifies that any CSS property should be animated.

The transition property requires two values: the name of the property to animate and the duration of the animation. For instance, a basic transition might be defined as follows:

```css

.box {

  width: 100px;

  height: 100px;

  background-color: orange;

  transition-property: background-color;

  transition-duration: 1s;

}

.box:hover {

  background-color: red;

}

```

In this example, the background color transitions smoothly from orange to red over one second.

For multiple properties, the syntax allows specifying either similar durations for all properties or individual durations for each property. The following example demonstrates animating both width and background color:

```css

.box {

  width: 100px;

  height: 100px;

  background-color: orange;

  transition-property: width, background-color;

  transition-duration: 1s, 2s;

}

.box:hover {

  width: 200px;

  background-color: red;

}

```

In this case, the width changes over one second, while the background color transitions over two seconds.

The browser calculates intermediary frames for transitions, requiring 60 frames per second (fps) for smooth animations. This calculation is crucial for maintaining visual continuity during property changes.


## Timing and Duration

The transition-duration property determines the speed of the transition, accepting values in seconds or milliseconds. It can specify a single duration for all properties or individual durations for each property.

The transition-timing-function property controls the speed curve of the transition, offering several predefined options:

- 'ease': default behavior, slow start, fast middle, slow end

- 'linear': constant speed

- 'ease-in': slow start

- 'ease-out': slow end

- 'ease-in-out': symmetrical acceleration and deceleration

- 'cubic-bezier(n,n,n,n)': custom timing function definition

The browser implements these timing functions by calculating the animation's intermediate frames. For smooth transitions, 60 frames per second (fps) are required, though the timing function can affect this rate. For example, 'ease-in' animations may require more frames during their initial slow phase, while 'ease-out' animations may need extra frames for their concluding slowdown.

CSS provides four primary timing functions:

1. **Linear**: Moves at a constant pace, with equal movement per frame. While rarely the best choice, 3D printers represent the closest real-world analogy.

2. **Ease-out**: Moves quickly at first, then slows down towards the end. Ideal for elements entering from off-screen, creating the effect of something coming from great distance.

3. **Ease-in**: Moves slowly at first, then speeds up. Best for moving elements beyond the viewport.

4. **Ease-in-out**: Has equal acceleration and deceleration, creating a symmetrical curve. Most useful for looped animations, such as elements fading in and out repeatedly.

The transition-delay property adds a start delay to the transition, measured in seconds or milliseconds. Negative values can create the perceptual effect of starting before the trigger event, though the transition still begins immediately. This property allows precise control over when the animation sequence begins relative to the triggering event.


## Discrete Transitions

While CSS transitions typically interpolate between property values for a smooth transition effect, there are scenarios where this behavior is not desirable. To address these cases, CSS provides the 'allow-discrete' keyword, which enables developers to create stepped or discrete animations.


### Discrete Animations with 'allow-discrete'

The 'allow-discrete' keyword specifies that individual frame values should be computed rather than smoothly interpolating between them. This means that the transition will progress in distinct, stepped intervals rather than creating a continuous change. For instance, when applied to the display property, this keyword can create a "bounce effect" where the element quickly changes visibility states without intermediate values.


### Implementation Example

When implementing a discrete transition, you would typically use CSS like this:

```css

.box {

  width: 100px;

  height: 100px;

  background-color: orange;

  transition-property: width, background-color;

  transition-duration: 1s, 2s;

  transition-timing-function: ease;

  transition-delay: 0s;

  transition-fill-mode: forwards;

  transition-mode: allow-discrete;

}

.box:hover {

  width: 200px;

  background-color: red;

}

```

In this example, applying the 'allow-discrete' keyword to the transition-mode allows the width and background color changes to occur in distinct steps rather than smoothly interpolating between the values.


### Use Cases

The 'allow-discrete' keyword is particularly useful for creating UI elements that change state in a series of distinct steps rather than smoothly animating between intermediate values. Common applications include:

- **UI toggles**: Elements that switch between completely visible and completely hidden states

- **Progress indicators**: Scenarios where progress updates occur at specific, non-interpolated intervals

- **Custom animation effects**: Specific visual effects where smooth interpolation would be undesirable

While the keyword offers flexible control over animation behavior, developers should carefully consider whether a smooth transition effect better suits their interface's requirements.


## Event Handling


### Transition Events

CSS transitions generate several events that developers can use to detect animation status. These events include `transitionrun`, `transitionstart`, and `transitionend`.

The `transitionrun` event fires before any delay, while `transitionstart` occurs after any delay. Both events use the `element.addEventListener()` method for attachment:

```javascript

el.addEventListener("transitionrun", signalStart, true);

el.addEventListener("transitionstart", signalStart, true);

```

The `transitionend` event fires when the transition completes but does not trigger if the transition is aborted before completion (e.g., by making an element `display: none`). This event provides detailed information about the transition through its associated `TransitionEvent` object, which extends the `Event` object. The `TransitionEvent` object includes properties such as `propertyName` (the name of the CSS property that completed the transition) and `elapsedTime` (the number of seconds the transition was running when the event fired).

