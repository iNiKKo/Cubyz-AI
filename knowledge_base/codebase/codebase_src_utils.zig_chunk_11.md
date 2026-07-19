# [hard/codebase_src_utils.zig] - Chunk 11

**Type:** algorithm
**Keywords:** interpolation, splines, time travel detection, velocity update, position update
**Symbols:** GenericInterpolation, GenericInterpolation.init, GenericInterpolation.updatePosition, GenericInterpolation.evaluateSplineAt, GenericInterpolation.interpolateCoordinate, GenericInterpolation.determineNextDataPoint, GenericInterpolation.update, GenericInterpolation.updateIndexed
**Concepts:** interpolation, cubic Hermite splines, motion updates

## Summary
The chunk defines a generic interpolation system for smooth motion updates.

## Explanation
This chunk implements a generic interpolation system that can handle motion updates for any number of elements. It uses cubic Hermite splines to interpolate positions and velocities smoothly over time. The `GenericInterpolation` function is a parameterized type that takes the number of elements as a compile-time constant. The struct returned by this function contains arrays to store past positions, velocities, and times, as well as pointers to the current output position and velocity. Specifically, it has an array `lastPos` with 8 frames for each element's position, an array `lastVel` with 8 frames for each element's velocity, and an array `lastTimes` with 8 frames for timestamps. The struct also includes a `frontIndex` to track the current frame, a `currentPoint` to indicate the last used data point, and pointers `outPos` and `outVel` to the current output position and velocity.

Methods include initialization (`init`), updating positions (`updatePosition`), evaluating splines (`evaluateSplineAt`), interpolating individual coordinates (`interpolateCoordinate`), determining the next data point (`determineNextDataPoint`), and updating the system with new time (`update`). The `updateIndexed` method allows for more complex updates based on an array of indices. Error handling includes a warning for detected time travel.

The `init` method initializes the interpolation system by setting the output position and velocity pointers, copying initial values to the past positions and velocities arrays, resetting the front index, and setting the current point to null.

The `updatePosition` method updates the position and velocity at a given time by shifting the front index, copying new values to the last positions and velocities arrays, and storing the timestamp.

The `evaluateSplineAt` function calculates spline values using cubic Hermite splines based on the provided parameters: `_t`, `tScale`, `p0`, `_m0`, `p1`, and `_m1`. It returns an array containing the interpolated value and its first derivative.

The `interpolateCoordinate` method interpolates individual coordinates using cubic interpolation if the velocity is non-zero; otherwise, it linearly interpolates.

The `determineNextDataPoint` method determines the next data point to use for interpolation based on the current time and the last times array. It selects the future time value that is at least 50 units away from the current time to prevent jumping.

The `update` method updates the system with new time by determining the next data point, calculating delta time, handling time travel detection, and updating positions and velocities either linearly or using cubic interpolation. If time travel is detected, it logs a warning and resets the last time to the current time.

The `updateIndexed` method is similar to `update` but allows for more complex updates based on an array of indices.

## Code Example
```zig
pub fn init(self: *@This(), initialPosition: *[elements]f64, initialVelocity: *[elements]f64) void {
	self.outPos = initialPosition;
	self.outVel = initialVelocity;
	@memset(&self.lastPos, self.outPos.*);
	@memset(&self.lastVel, self.outVel.*);
	self.frontIndex = 0;
	self.currentPoint = null;
}
```

## Related Questions
- What is the purpose of the `GenericInterpolation` function?
- How does the `init` method initialize the interpolation system?
- What algorithm is used for position and velocity interpolation?
- How does the `updatePosition` method work?
- What happens if time travel is detected during an update?
- How does the `evaluateSplineAt` function calculate spline values?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_11*
