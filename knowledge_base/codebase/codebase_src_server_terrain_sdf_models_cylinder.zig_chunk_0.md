# [easy/codebase_src_server_terrain_sdf_models_cylinder.zig] - Chunk 0

**Type:** serialization
**Keywords:** cylinder SDF, minRadius maxRadius, instantiate seed, generate distance, floor ceil bounds, NeverFailingAllocator, ZonElement fields, random interpolation, SdfInstance data, centerPosOffset
**Symbols:** id, Instance, initAndGetExtend, instantiate, generate
**Concepts:** SDF model definition, cylinder geometry, random instance generation, bounding volume computation, distance field evaluation

## Summary
Defines a cylinder SDF model with configurable radius/height ranges and instantiates random instances for terrain generation.

## Explanation
The chunk declares public constants id, minRadius, maxRadius, minHalfHeight, maxHalfHeight as the schema for a cylinder SDF model. It defines an Instance struct holding concrete radius and halfHeight values. The initAndGetExtend function reads optional fields from a ZonElement (minRadius, maxRadius, minHeight, maxfHeight), applies defaults (16 for minRadius, self.minRadius for maxRadius, 32/2 for minHalfHeight, twice minHalfHeight for maxHalfHeight), creates an SdfModel via main.worldArena.create(@This()), and returns the model with computed bounding extents using @floor and @ceil. The instantiate function allocates an Instance on a NeverFailingAllocator, interpolates radius and halfHeight linearly between the stored bounds using main.random.nextFloat(seed) to produce deterministic randomness per seed, constructs a Vec3f bounds array from instance.radius and instance.halfHeight, and returns an SdfInstance containing the data, a generate function cast via main.meta.castFunctionSelfToAnyopaque(generate), and floor/ceil min/max bounds plus centerPosOffset. The generate method computes the signed distance to the cylinder by evaluating the radial distance (vec.length(vec.xy(samplePos)) - self.radius) and vertical distance (@abs(samplePos[2]) - self.halfHeight), then combines them using vec.length(@max(..., Vec2f{0, 0})) + @min(0, @max(circleSdf, heightSdf)), effectively returning the maximum of zero and the larger radial/vertical deviation minus the smaller one.

## Code Example
```zig
pub fn generate(self: *Instance, samplePos: Vec3f) f32 {
	const circleSdf: f32 = vec.length(vec.xy(samplePos)) - self.radius;
	const heightSdf: f32 = @abs(samplePos[2]) - self.halfHeight;
	return vec.length(@max(Vec2f{heightSdf, circleSdf}, Vec2f{0, 0})) + @min(0, @max(circleSdf, heightSdf));
}
```

## Related Questions
- How does initAndGetExtend handle missing minHeight or maxfHeight fields in the ZonElement?
- What default values are applied when minRadius or maxRadius are not provided by the configuration?
- How is the random radius and halfHeight interpolated between min and max bounds during instantiation?
- Why is main.meta.castFunctionSelfToAnyopaque used for the generate function inside SdfInstance?
- Does the generate method treat points outside the cylinder as positive distance and inside as negative?
- What role does centerPosOffset play in the returned SdfInstance structure?
- How are the minBounds and maxBounds computed using @floor and @ceil on the instance dimensions?
- Is the Instance struct allocated with a specific memory ownership policy or is it just arena-created?
- Can multiple instances share the same seed to produce identical geometry for deterministic chunk generation?
- What happens if both circleSdf and heightSdf are negative in generate—does the formula still hold?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_cylinder.zig_chunk_0*
