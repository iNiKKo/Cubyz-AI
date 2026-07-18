# [easy/codebase_src_server_terrain_sdf_models_rectangular_cuboid.zig] - Chunk 0

**Type:** implementation
**Keywords:** SDF, cuboid, distance field, randomization, vector operations
**Symbols:** Array3D, NeverFailingAllocator, sdf, SdfInstance, vec, Vec3f, Vec3i, ZonElement, id, minRadii, maxRadii, Instance, initAndGetExtend, instantiate, generate
**Concepts:** SDF model, rectangular cuboid, Signed Distance Field

## Summary
Rectangular cuboid SDF model initialization and instantiation

## Explanation
This chunk defines a rectangular cuboid SDF (Signed Distance Field) model. It initializes the model with minimum and maximum radii based on ZonElement data, calculates the extend, and instantiates the model with random radii. The generate function computes the distance from the sample position to the surface of the cuboid.

The `initAndGetExtend` function initializes the SDF model by setting `minRadii` and `maxRadii`. If ZonElement data is available for `minSideLengths`, it sets `self.minRadii` as `(zon.get(Vec3f, "minSideLengths") orelse @as(Vec3f, @splat(32)))/@as(Vec3f, @splat(2));`. If ZonElement data is available for `maxSideLengths`, it sets `self.maxRadii` as `(zon.get(Vec3f, "maxSideLengths") orelse self.minRadii*@as(Vec3f, @splat(2)))/@as(Vec3f, @splat(2));`. If no data is available for `maxSideLengths`, it defaults to twice the value of `minRadii`.

The extend of the model is calculated as `.min = @floor(-self.maxRadii)` and `.max = @ceil(self.maxRadii)`. The `instantiate` function initializes an instance with random radii by adding a vector generated from `main.random.nextFloatVector(3, seed)` to `self.minRadii`, scaled by the difference between `self.maxRadii` and `self.minRadii`. The generate function computes the distance using dimensionalSdf: Vec3f = @abs(samplePos) - self.radii; followed by vec.length(@max(dimensionalSdf, @as(Vec3f, @splat(0)))) + @min(0, @max(dimensionalSdf[0], dimensionalSdf[1], dimensionalSdf[2])) to determine the distance from the sample position to the surface of the cuboid.

## Code Example
```zig
pub fn initAndGetExtend(zon: ZonElement) sdf.SdfModel.InitResult {
	const self = main.worldArena.create(@This());
	self.minRadii = (zon.get(Vec3f, "minSideLengths") orelse @as(Vec3f, @splat(32)))/@as(Vec3f, @splat(2));
	self.maxRadii = (zon.get(Vec3f, "maxSideLengths") orelse self.minRadii*@as(Vec3f, @splat(2)))/@as(Vec3f, @splat(2));

	return .{.model = self, .maxExtend = .{
		.min = @floor(-self.maxRadii),
		.max = @ceil(self.maxRadii),
	}};
}
```

## Related Questions
- What is the purpose of the `id` constant in this chunk?
- How are the minimum and maximum radii calculated from the ZonElement data?
- What is the extend of the model based on the calculated min and max radii?
- What is the generate function used for in this SDF model implementation?
- How does the `instantiate` function initialize an instance of the rectangular cuboid SDF model?
- What are the parameters passed to the `generate` function?
- What operations are performed on the dimensionalSdf vector within the `generate` function?
- What is the purpose of the `@max(dimensionalSdf, @as(Vec3f, @splat(0)))` operation in the `generate` function?
- How does the `@min(0, @max(dimensionalSdf[0], dimensionalSdf[1], dimensionalSdf[2]))` operation affect the result of the `generate` function?
- What is the purpose of the `@floor(-self.maxRadii)` and `@ceil(self.maxRadii)` operations in the `initAndGetExtend` function?
- How does the `main.random.nextFloatVector(3, seed)` function contribute to the randomization of the radii in the `instantiate` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_rectangular_cuboid.zig_chunk_0*
