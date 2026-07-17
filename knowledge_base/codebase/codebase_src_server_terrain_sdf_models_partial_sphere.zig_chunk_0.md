# [easy/codebase_src_server_terrain_sdf_models_partial_sphere.zig] - Chunk 0

**Type:** implementation
**Keywords:** SDF, sphere, cut direction, randomness, bounds, allocation, seed, intersection, plane offset, normalize, floor, ceil
**Symbols:** id, minRadius, maxRadius, cutPercentage, cutDirection, cutDirectionRandomness, Instance, initAndGetExtend, instantiate, generate
**Concepts:** signed distance field, partial sphere model, terrain generation, arena allocation, seeded randomness, configuration parameters

## Summary
This chunk defines a partial sphere Signed Distance Field (SDF) model for terrain generation. It exposes configuration parameters (min/max radius, cut percentage/direction randomness) and provides an initAndGetExtend entry point that reads those from a ZonElement to produce bounds, plus an instantiate method that seeds per-instance variation.

## Explanation
The chunk declares top-level constants importing std, main.worldArena, main.heap.NeverFailingAllocator, the server terrain SDF module, and vec. It defines a public identifier id = "cubyz:partial_sphere" and exposes fields minRadius, maxRadius, cutPercentage, cutDirection, cutDirectionRandomness as part of the model's configuration surface (these are not inside any struct here; they appear to be top-level constants or fields intended for use by callers). It defines a local Instance struct with radius, cutPercentage, cutDirection. The initAndGetExtend function creates an arena-allocated self via main.worldArena.create(@This()), reads minRadius/maxRadius/cutPercentage from zon.get(f32) with defaults (16 / 0.5), normalizes cutDirection to default {-1,-1,-1} if absent, and sets cutDirectionRandomness default 0; it returns an InitResult containing the model self and a maxExtend bounds computed via @splat/@floor/@ceil around -maxRadius..+maxRadius. The instantiate method allocates Instance on the provided arena, computes radius as minRadius + (max-min)*random.nextFloat(seed), perturbs cutDirection by adding random noise scaled with cutDirectionRandomness, copies cutPercentage, builds bounds and offset using @splat/@floor/@ceil, and returns an SdfInstance with data = instance, generateFn cast via main.meta.castFunctionSelfToAnyopaque(generate), minBounds = floor(-bounds + offset), maxBounds = ceil(bounds + offset), centerPosOffset = ceil(bounds). The generate function implements the partial sphere SDF: it computes sphereSdf as length(samplePos) - radius and planeSdf as dot(cutDirection, samplePos) - radius + cutPercentage*radius*2, then returns sdf.intersection(sphereSdf, planeSdf), delegating to the server terrain SDF module. Memory ownership is explicit via NeverFailingAllocator; no error handling beyond defaults/optionals is present.

## Code Example
```zig
pub fn generate(self: *Instance, samplePos: Vec3f) f32 {
	const sphereSdf = vec.length(samplePos) - self.radius;
	const planeSdf = vec.dot(self.cutDirection, samplePos) - self.radius + self.cutPercentage*self.radius*2;
	return sdf.intersection(sphereSdf, planeSdf);
}
```

## Related Questions
- What default values are used for cutDirection and cutDirectionRandomness when the ZonElement does not provide them?
- How is the radius of an instantiated partial sphere computed from minRadius, maxRadius, and a seeded random float?
- What is the formula for planeSdf in the generate function and how does it incorporate cutPercentage?
- Which SDF module function is called to combine the sphere and plane contributions into the final distance value?
- How are the bounding extents (minBounds, maxBounds) derived from the instance radius and cutDirection offset?
- What role does main.worldArena.create play in initAndGetExtend and instantiate regarding memory ownership?
- Is there any validation performed on the input samplePos before computing sphereSdf or planeSdf?
- How is the generate function exposed to callers via SdfInstance.generateFn and what casting mechanism is used?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_partial_sphere.zig_chunk_0*
