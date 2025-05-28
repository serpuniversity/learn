---

title: Temporal.Instant.fromEpochMilliseconds: JavaScript's Precise Time Measurement

date: 2025-05-27

---


# Temporal.Instant.fromEpochMilliseconds: JavaScript's Precise Time Measurement

JavaScript's Date API provides several methods for working with dates and times, including converting between different representations and calculating time spans. However, these methods often lack the precision and flexibility needed for robust time manipulation. The Temporal.Instant object introduced in the Temporal API addresses these limitations by representing precise points in time with nanosecond accuracy. This article explores the Temporal.Instant.fromEpochMilliseconds method, which creates Instant objects from epoch milliseconds, showcasing its advantages and usage patterns. Through practical examples and detailed explanations, we'll demonstrate how this method enables more accurate time calculations and conversions in JavaScript applications.


## Instant Creation

The Temporal.Instant object represents a precise point in time with nanosecond precision, counting the number of nanoseconds since the Unix epoch of January 1, 1970 at 00:00 UTC. To create an Instant object, developers can use several methods, with the most straightforward being the fromEpochMilliseconds static method.


### fromEpochMilliseconds Method

The Temporal.Instant.fromEpochMilliseconds static method requires a single parameter: epochMilliseconds (number). This method converts the provided number to a BigInt and multiplies it by 1e6 to obtain the equivalent number of nanoseconds. It returns a new Temporal.Instant object representing the specified time. If the epochMilliseconds parameter cannot be converted to a BigInt (not an integer) or falls outside the representable range, a RangeError is thrown.


### Example Usage

```javascript

const instant = Temporal.Instant.fromEpochMilliseconds(0);

console.log(instant.toString()); // 1970-01-01T00:00:00Z

const vostok1Liftoff = Temporal.Instant.fromEpochMilliseconds(-275248380000);

console.log(vostok1Liftoff.toString()); // 1961-04-12T06:07:00Z

const sts1Liftoff = Temporal.Instant.fromEpochMilliseconds(355924804000);

console.log(sts1Liftoff.toString()); // 1981-04-12T12:00:04Z

```


### Alternative Creation Methods

While fromEpochMilliseconds offers precise millisecond values, developers can also create Instant objects from other sources:

- **ISO 8601 strings**: `Temporal.Instant.from("2025-02-06T11:46:06.959366942Z")` creates an instant from a UTC timestamp with exact millisecond precision.

- **Epoch seconds**: `Temporal.Instant.fromEpochSeconds(1738842325)` creates an instant from Unix seconds since 1970 UTC.

- **Epoch nanoseconds**: `Temporal.Instant.fromEpochNanoseconds(1738842325915000000)` creates an instant from Unix nanoseconds since 1970 UTC.


### Time Zone Considerations

Although Instant objects represent precise times in UTC, they can be converted to other time zones using ZonedDateTime objects. For example:

```javascript

const timestamp = Temporal.Instant.fromEpochMilliseconds(1553993100000);

console.log(timestamp.toZonedDateTimeISO('Europe/Berlin')); // 2019-03-31T01:45:00+01:00[Europe/Berlin]

console.log(timestamp.toZonedDateTimeISO('UTC')); // 2019-03-31T00:45:00+00:00[UTC]

console.log(timestamp.toZonedDateTimeISO('-08:00')); // 2019-03-30T16:45:00-08:00[-08:00]

```

These examples demonstrate the versatile time manipulation capabilities of the Temporal.Instant object and its methods for creating instances from various time sources.


## Time Manipulation

The Temporal.Instant object enables precise time measurement with nanosecond precision, counting the number of nanoseconds since the Unix epoch of January 1, 1970 at 00:00 UTC. This independence from time zones and calendars allows for accurate time span calculations through the `until` method, which returns a Temporal.Duration object representing the elapsed time between two instances.


### Time Span Calculations

The `until` method requires two parameters: `other` (another exact time) and an optional `options` object. The options object allows specifying the `largestUnit` and `smallestUnit`, with default behavior of seconds unless otherwise specified. This method computes the elapsed time before the exact time represented by the instant and since the exact time represented by `other`, optionally rounding it, and returns it as a Temporal.Duration object. The resulting duration is negative if `other` is later than the instant.


### Example Usage

```javascript

const startOfMoonMission = Temporal.Instant.from('1969-07-16T13:32:00Z');

const endOfMoonMission = Temporal.Instant.from('1969-07-24T16:50:35Z');

const missionLength = startOfMoonMission.until(endOfMoonMission, { largestUnit: 'hour' });

// => PT195H18M35S

```

Rounding options can be applied to control the granularity of the resulting duration:

```javascript

const approxMissionLength = startOfMoonMission.until(endOfMoonMission, { largestUnit: 'hour', smallestUnit: 'hour' });

// => PT195H

```


### Precision Control

The rounding process uses the specified `roundingIncrement` and `roundingMode`. The default rounding mode is `'trunc'`, which truncates any remainder towards zero. Other available modes include `'ceil'`, `'floor'`, `'expand'`, and `'halfEven'`, providing flexibility in how elapsed times are represented:

```javascript

const epoch = Temporal.Instant.fromEpochMilliseconds(0);

const billion = Temporal.Instant.fromEpochMilliseconds(1e9);

const elapsedBillion = epoch.until(billion);

// => PT1000000000S

const roundedElapsedBillion = epoch.until(billion, { largestUnit: 'hour' });

// => PT277777H46M40S

const preciseElapsedBillion = epoch.until(billion, { largestUnit: 'nanosecond' });

// => PT1000000000S

```


## Property Details

The `epochMilliseconds` property provides direct access to the number of milliseconds since the Unix epoch (January 1, 1970, at 00:00:00 UTC) for a given `Temporal.Instant` object. This property is read-only and returns an integer value that represents the time at nanosecond precision, obtained by flooring the division of `epochNanoseconds` by 1,000,000.


### Property Usage

As demonstrated in the source documents, this property enables precise time representation and comparison operations. For instance, creating an instant from a string can then retrieve its epoch milliseconds using this property:

```javascript

const instant = Temporal.Instant.from("1969-08-01T12:34:56.789Z");

console.log(instant.epochMilliseconds); // -13173903211

```


### Conversion Methods

Conversion between `Date` objects and `Temporal.Instant` can leverage the `epochMilliseconds` property:

```javascript

const legacyDate = new Date(1394104654000); // Thu Mar 06 2014 06:17:34 GMT-0500 (EST)

const instantFromLegacy = Temporal.Instant.fromEpochMilliseconds(legacyDate.getTime());

console.log(instantFromLegacy.epochMilliseconds); // 1394104654000

```

The `epochMilliseconds` property also facilitates backward compatibility through static methods:

```javascript

const instant = Temporal.Instant.fromEpochMilliseconds(1553993100000);

console.log(instant.epochMilliseconds); // 1553993100000

```


### Error Handling

The property maintains consistency in value representation by flooring division results and ensuring numerical precision:

```javascript

const exactMillis = 1553993100000;

const instant = Temporal.Instant.fromEpochMilliseconds(exactMillis);

console.log(instant.epochMilliseconds); // 1553993100000

console.log(instant.epochNanoseconds / 1000000); // 1553993100000

```

In cases where conversion or calculation errors occur (such as non-integer input values or out-of-range timestamps), the property maintains the integrity of the temporal data model by returning a value that represents the closest valid representation of the timestamp, effectively clamping to the maximum representable value when necessary.


## Browser Support

As of the latest specifications and implementation status across browsers, `Temporal.Instant.fromEpochMilliseconds()` is generally available but not part of the Baseline specification. The method is included in the Temporal proposal and is supported in all major browsers.

The implementation relies on converting the provided epoch milliseconds to a BigInt and scaling it to nanoseconds. However, the exact range for valid input values and conversion mechanisms may vary slightly between implementations. All modern browsers handle this conversion successfully within the representable range of ±108 days (approximately ±273,972.6 years).


### Browser-Specific Notes

Chrome and Node.js environments fully support the Temporal API, including this method. Firefox experimental builds partially implement the feature, while Safari and Edge lack official support for the Temporal API at this time. Developers should check for compatibility through browser detection or feature testing before relying on this method in production code.


### Alternative Conversion Methods

The preferred approach for converting legacy Date values to the Temporal API is through the `Date.prototype.toTemporalInstant()` method. This method provides better integration with existing Date objects and may offer performance optimizations. For cases where direct epoch milliseconds conversion is necessary, developers should use `Temporal.Instant.fromEpochMilliseconds()` but be aware of potential limitations in unsupported environments.


## Best Practices

When working with epoch milliseconds in JavaScript, several best practices emerge from the documentation:


### Direct Conversion and Arithmetic

JavaScript's `Date` object provides several methods for working with epoch time:

```javascript

const now = Date.now(); // Current time in milliseconds since epoch

const epochMillis = +new Date(now); // Same as `now`, demonstrating timestamp retrieval

```

When constructing times based on epoch milliseconds, developers should maintain precision by avoiding unnecessary conversions:

```javascript

const epoch = 1553993100000; // Example epoch millisecond value

const instant = Temporal.Instant.fromEpochMilliseconds(epoch);

console.log(instant.epochMilliseconds); // 1553993100000

```


### Time Conversion and Adjustment

To convert between epoch milliseconds and local time, developers can use:

```javascript

function localDateFromEpoch(epochMilli, offsetSeconds) {

  const adjustedMilli = epochMilli + offsetSeconds * 1000;

  return new Date(adjustedMilli);

}

```

This function correctly accounts for time zone offsets. For more complex calculations, the Temporal API provides robust methods:

```javascript

import { Temporal } from '@js-temporal/polyfill';

function localDateFromEpoch(epochMilli, offsetSeconds) {

  const instant = Temporal.Instant.fromEpochMilliseconds(epochMilli);

  const offsetSign = offsetSeconds < 0 ? '-' : '+';

  const offsetAsTime = new Temporal.PlainTime().add({ seconds: Math.abs(offsetSeconds) });

  const offsetString = `${offsetSign}${offsetAs

}

```


### Handling Invalid and Out-of-Range Values

JavaScript's Date object handles invalid inputs gracefully:

```javascript

const invalidDate = new Date(NaN);

console.log(invalidDate.getTime() === NaN); // true

```

Similarly, when working with epoch values:

```javascript

const outOfRangeEpoch = 1e18; // Well above maximum representable value

const instant = Temporal.Instant.fromEpochMilliseconds(outOfRangeEpoch);

console.log(instant.epochMilliseconds === Number.MAX_SAFE_INTEGER); // true

```

Developers should always validate epoch values before conversion to prevent unexpected behavior or data corruption.

