# [hard/codebase_src_models.zig] - Chunk 3

**Type:** implementation
**Keywords:** OBJ file parsing, collision grid, floodfill algorithm, UV normalization, model initialization
**Symbols:** collisionGridSize, CollisionGridInteger, Vec3i, Vec3f, Box, ModelIndex, QuadInfo, Triangle, Quad, allOnes, loadRawModelDataFromObj, loadModel, allTrue, disableAll, canExpand, addVert
**Concepts:** model loading, collision detection, geometry processing

## Summary
This chunk handles model loading and collision grid processing.

## Explanation
The chunk primarily processes model data from OBJ files. It includes functions for loading raw model data, initializing collision grids, and expanding collision boxes. The `loadModel` function loads model data, normalizes UV coordinates, and initializes a model index. The `loadRawModelDataFromObj` function parses OBJ file lines to extract vertices, normals, UVs, triangles, and quads. The collision grid processing involves floodfilling operations to determine collision boundaries and expanding these boundaries while ensuring all conditions are met.

## Code Example
```zig
fn addVert(vert: Vec3f, vertList: *main.List(Vec3f)) usize {
	const ind = for (vertList.*.items, 0..) |vertex, index| {
		if (vertex == vert) break index;
	} else vertList.*.items.len;

	if (ind == vertList.*.items.len) {
		vertList.*.append(vert);
	}

	return ind;
}
```

## Related Questions
- How does the `loadModel` function normalize UV coordinates?
- What is the purpose of the `allTrue` function in collision processing?
- How does the `canExpand` function determine if a collision box can be expanded?
- What role does the `floodfillQueue` play in collision grid initialization?
- How are vertices parsed from an OBJ file line in the `loadRawModelDataFromObj` function?
- What is the significance of the `allOnes` variable in collision mask operations?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_3*
