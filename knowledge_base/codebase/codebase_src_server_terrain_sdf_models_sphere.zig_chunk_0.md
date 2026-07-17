# [easy/codebase_src_server_terrain_sdf_models_sphere.zig] - Chunk 0

**Type:** implementation
**Keywords:** SDF, radius, random, vector length, instance creation, initialization
**Symbols:** id, minRadius, maxRadius, Instance, initAndGetExtend, instantiate, generate
**Concepts:** SDF model, random number generation, vector operations

## Summary
This chunk defines a spherical SDF model with initialization and instantiation logic.

## Explanation
The code provides a struct `Instance` representing a sphere's radius. It includes methods for initializing the model from ZonElement data, instantiating the model with a random radius within specified bounds, and generating an SDF value at a given sample position.

## Code Example
```zig
pub fn generate(self: *Instance, samplePos: Vec3f) f32 {
	return vec.length(samplePos) - self.radius;
}
```

## Related Questions
- What is the purpose of the `id` constant?
- How does the `initAndGetExtend` function initialize the SDF model?
- What does the `instantiate` method do with the seed parameter?
- Which function calculates the SDF value for a given sample position?
- What data structure represents an instance of this sphere model?
- How is the radius of the sphere determined during instantiation?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_sphere.zig_chunk_0*
