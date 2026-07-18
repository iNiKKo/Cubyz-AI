# [easy/codebase_src_server_terrain_sdf_models_sphere.zig] - Chunk 0

**Type:** implementation
**Keywords:** terrain generation, SDF, randomization, vector operations, distance calculation
**Symbols:** id, minRadius, maxRadius, Instance, initAndGetExtend, instantiate, generate
**Concepts:** world generation, Signed Distance Function (SDF)

## Summary
Defines a spherical Signed Distance Function (SDF) model for terrain generation.

## Explanation
This chunk implements a spherical SDF model used in terrain generation: `id = "cubyz:sphere"`. `initAndGetExtend` reads `minRadius` (default `16`) and `maxRadius` (defaults to `minRadius` if not given) from Zon, and returns a `maxExtend` bounding box from `floor(-maxRadius)` to `ceil(maxRadius)`. `instantiate` picks a random radius uniformly between `minRadius` and `maxRadius` for that specific instance, and returns bounds/center offset derived from that instance radius. `generate(samplePos)` returns the signed distance from `samplePos` to the sphere's surface: `length(samplePos) - radius` (negative inside, positive outside).

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
