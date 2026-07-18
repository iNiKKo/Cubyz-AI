# [hard/codebase_src_models.zig] - Chunk 6

**Type:** implementation
**Keywords:** string hashmap, deduplication, degeneracy check, light samples, normal direction
**Symbols:** nameToIndex, getModelIndex, quads, extraQuadInfos, models, quadDeduplication, addQuad, addCornerLightSamples
**Concepts:** model management, quad handling, light sampling

## Summary
Handles model indexing and quad management in the Cubyz voxel engine.

## Explanation
This chunk manages models and their associated quads within the Cubyz voxel engine. It includes functions for retrieving model indices by name, adding quads with deduplication checks, and handling light sampling for aligned normal directions. The `getModelIndex` function looks up a model index using a string name, logging an error if the model is not found. The `addQuad` function adds a quad to the list after checking for degeneracy and performing various calculations related to face neighbors and light samples. The `addCornerLightSamples` function calculates light samples for each corner of a quad.

## Code Example
```zig
pub fn getModelIndex(string: []const u8) ModelIndex {
	return nameToIndex.get(string) orelse {
		std.log.err("Couldn't find voxelModel with name: {s}.", .{string});
		return @enumFromInt(0);
	};
}
```

## Related Questions
- How does the `getModelIndex` function retrieve a model index?
- What is the purpose of the `quadDeduplication` hashmap?
- How are degenerate quads handled in the `addQuad` function?
- What calculations are performed for light samples in the `addCornerLightSamples` function?
- How does the chunk manage model indices and quads?
- What is the role of the `extraQuadInfos` list in this chunk?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_6*
