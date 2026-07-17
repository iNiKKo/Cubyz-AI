# [hard/codebase_src_models.zig] - Chunk 6

**Type:** implementation
**Keywords:** model loading, coordinate system, quad info, light weights, box faces
**Symbols:** registerModel, box, openBox, addCornerLightSamples
**Concepts:** model registration, light sampling, axis-aligned models, box generation

## Summary
Handles model registration and light sampling for axis-aligned models.

## Explanation
This chunk contains functions for registering models, calculating light samples for axis-aligned models, and generating box-shaped models. The `registerModel` function loads a model from data and registers it with a given ID. The `box` function generates six QuadInfo structures representing the faces of a box. The `openBox` function generates four QuadInfo structures for a box with one face removed. The light sampling logic in `addCornerLightSamples` calculates weights for light samples based on vertex positions and normal directions, ensuring that light contributions are correctly distributed across model corners.

## Code Example
```zig
pub fn registerModel(id: []const u8, data: []const u8, zon: ?main.ZonElement) ModelIndex {
	const coordinateSystem: vec.CoordinateSystem = if (zon) |z| z.get(vec.CoordinateSystem, "coordinateSystem") orelse .right_handed_z_up else .right_handed_z_up;
	const model = Model.loadModel(data, coordinateSystem);
	nameToIndex.put(id, model) catch unreachable;
	return model;
}
```

## Related Questions
- How do I register a new model in the system?
- What is the purpose of the `box` function in this code?
- Can you explain how light sampling works for axis-aligned models?
- How does the `openBox` function differ from the `box` function?
- What coordinate systems are supported by the model registration process?
- How are light samples deduplicated and stored for axis-aligned models?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_6*
