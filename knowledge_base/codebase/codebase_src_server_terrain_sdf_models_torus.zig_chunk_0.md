# [easy/codebase_src_server_terrain_sdf_models_torus.zig] - Chunk 0

**Type:** implementation
**Keywords:** SDF, Torus, Initialization, Instantiation, Random Seed
**Symbols:** id, minRadius, maxRadius, minThickness, maxThickness, Instance, initAndGetExtend, instantiate, generate
**Concepts:** SDF Model, Torus Shape, Randomization

## Summary
Torus SDF Model Initialization and Instantiation

## Explanation
This chunk defines a torus-shaped SDF model with customizable minimum and maximum radius and thickness. It initializes the model based on ZonElement data, calculates its extend, and provides an instantiation function to generate the model's instance using a random seed.

## Code Example
```zig
pub fn initAndGetExtend(zon: ZonElement) sdf.SdfModel.InitResult {
	const self = main.worldArena.create(@This());
	self.minRadius = zon.get(f32, "minRadius") orelse 16;
	self.maxRadius = zon.get(f32, "maxRadius") orelse self.minRadius;
	self.minThickness = zon.get(f32, "minThickness") orelse self.minRadius/2;
	self.maxThickness = zon.get(f32, "maxThickness") orelse self.minThickness;

	return .{.model = self, .maxExtend = .{
		.min = .{@floor(-self.maxRadius - self.maxThickness), @floor(-self.maxRadius - self.maxThickness), @floor(-self.maxThickness)},
		.max = .{@ceil(-self.maxRadius - self.maxThickness), @ceil(-self.maxRadius - self.maxThickness), @ceil(-self.maxThickness)},
	}};
}
```

## Related Questions
- What is the purpose of the `id` field in this chunk?
- How does the `initAndGetExtend` function initialize the torus model based on ZonElement data?
- What are the default values for `minRadius`, `maxRadius`, `minThickness`, and `maxThickness`?
- What is the purpose of the `Instance` struct in this chunk?
- How does the `instantiate` function generate an instance of the torus model using a random seed?
- What is the purpose of the `generate` function in this chunk?
- How does the `generate` function calculate the distance for a given sample position to determine if it falls within the torus shape?
- What are the minimum and maximum bounds calculated by the `initAndGetExtend` function?
- What is the center position offset used in the `instantiate` function?
- What is the purpose of the `generate` function's return value?
- How does the `Instance` struct store the radius and thickness values for the torus model?
- What are the default values for the radius and thickness when they are not provided in the ZonElement data?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_torus.zig_chunk_0*
