# [easy/codebase_src_server_terrain_sdf_models_sphere.zig] - Chunk 0

**Type:** implementation
**Keywords:** terrain generation, SDF, randomization, vector operations, distance calculation
**Symbols:** id, minRadius, maxRadius, Instance, initAndGetExtend, instantiate, generate
**Concepts:** world generation, Signed Distance Function (SDF)

## Summary
Defines a spherical Signed Distance Function (SDF) model for terrain generation.

## Explanation
This chunk implements a spherical Signed Distance Function (SDF) model used in terrain generation: `id = "cubyz:sphere"`. The `minRadius` is set to a default value of `16`, and the `maxRadius` defaults to the same value as `minRadius` if not specified. The `initAndGetExtend` function reads these values from Zon and returns a `maxExtend` bounding box with minimum bounds at `floor(-maxRadius)` and maximum bounds at `ceil(maxRadius)`. During instantiation, a random radius is chosen uniformly between `minRadius` and `maxRadius`, and the function returns bounds and center offset based on this instance radius. The `generate(samplePos)` function calculates the signed distance from `samplePos` to the sphere's surface using the formula `length(samplePos) - radius`, where negative values indicate points inside the sphere and positive values indicate points outside. The `Instance` struct holds the specific radius for each instance of the spherical SDF model.

## Code Example
```zig
pub fn generate(self: *Instance, samplePos: Vec3f) f32 {
	return vec.length(samplePos) - self.radius;
}
```

## Related Questions
- What is the ID of the spherical SDF model?
- How are the minimum and maximum radii initialized for the sphere model?
- What does the `initAndGetExtend` function return?
- How is a random radius determined during instantiation?
- What does the `generate` function calculate?
- What is the purpose of the `Instance` struct in this chunk?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_sphere.zig_chunk_0*
