# [easy/codebase_src_server_terrain_sdf_models_partial_sphere.zig] - Chunk 0

**Type:** world_generation
**Keywords:** Signed Distance Function, terrain generation, randomization, configuration parsing, instance creation
**Symbols:** id, minRadius, maxRadius, cutPercentage, cutDirection, cutDirectionRandomness, Instance, initAndGetExtend, instantiate, generate
**Concepts:** terrain generation, SDF models, partial sphere

## Summary
Defines a partial sphere SDF model for terrain generation.

## Explanation
This chunk defines a partial sphere Signed Distance Function (SDF) model used in terrain generation. It includes initialization from configuration data, instantiation with randomized parameters, and the actual SDF calculation function. The `initAndGetExtend` function initializes the model by setting default values if not provided in the ZonElement configuration. The `instantiate` function creates an instance of the partial sphere with a radius that is a random value between the minimum and maximum set in the configuration, and it randomizes the cut direction based on the specified randomness factor. After randomization, the cut direction is normalized using `vec.normalize`. The `generate` function calculates the SDF value for a given sample position, representing the distance to the surface of the partial sphere.

## Code Example
```zig
pub fn generate(self: *Instance, samplePos: Vec3f) f32 {
    const sphereSdf = vec.length(samplePos) - self.radius;
    const planeSdf = vec.dot(self.cutDirection, samplePos) - self.radius + self.cutPercentage*self.radius*2;
    return sdf.intersection(sphereSdf, planeSdf);
}
```

## Related Questions
- What is the purpose of the `initAndGetExtend` function?
- How does the `instantiate` function randomize and normalize the instance parameters?
- What does the `generate` function calculate for a given sample position?
- What are the default values set in the `initAndGetExtend` function if not provided in the configuration?
- How is the cut direction randomized during instantiation?
- What is the role of the `Instance` struct in this module?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_partial_sphere.zig_chunk_0*
