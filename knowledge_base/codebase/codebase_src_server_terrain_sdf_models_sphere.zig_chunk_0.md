# [easy/codebase_src_server_terrain_sdf_models_sphere.zig] - Chunk 0

**Type:** implementation
**Keywords:** terrain generation, SDF, randomization, vector operations, distance calculation
**Symbols:** id, minRadius, maxRadius, Instance, initAndGetExtend, instantiate, generate
**Concepts:** world generation, Signed Distance Function (SDF)

## Summary
Defines a spherical Signed Distance Function (SDF) model for terrain generation.

## Explanation
This chunk implements a spherical SDF model used in terrain generation. It includes the initialization of the sphere model with minimum and maximum radii, instantiation of individual spheres with random sizes within the specified range, and the generation function that calculates the distance from any point to the surface of the sphere.

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
