# [medium/codebase_src_vec.zig] - Chunk 1

**Type:** implementation
**Keywords:** quaternions, axis-angle conversion, vector normalization, trigonometric functions, identity quaternion
**Symbols:** Quat, Quat.q, Quat.quatFromAxisAngle
**Concepts:** quaternion mathematics

## Summary
Defines a Quaternion struct with methods for creating quaternions from axis-angle representations.

## Explanation
The chunk defines a `Quat` struct representing a quaternion, initialized by default to the identity quaternion (0, 0, 0, 1). It includes a method `quatFromAxisAngle` that constructs a quaternion from an axis and an angle. This method normalizes the input axis, calculates half the angle, computes sine and cosine of this half-angle, and then assembles the quaternion components accordingly.

## Code Example
```zig
pub fn quatFromAxisAngle(axis: Vec3f, angle: f32) Quat {
		const normal = normalize(axis);
		const n = Vec4f{normal[0], normal[1], normal[2], 1.0};
		const a = angle*0.5;
		const sc: [2]f32 = .{@sin(a), @cos(a)};
		return .{.q = n*Vec4f{sc[0], sc[0], sc[0], sc[1]}};
	}
```

## Related Questions
- What is the default value of a Quat instance?
- How does the quatFromAxisAngle method work?
- What are the components of the Vec4f used in the Quat struct?
- Where is the normalize function defined?
- What is the purpose of the sc array in the quatFromAxisAngle method?
- How is the quaternion constructed from the axis and angle?

*Source: unknown | chunk_id: codebase_src_vec.zig_chunk_1*
