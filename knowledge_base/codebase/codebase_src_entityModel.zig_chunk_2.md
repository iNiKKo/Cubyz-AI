# [medium/codebase_src_entityModel.zig] - Chunk 2

**Type:** implementation
**Keywords:** memory allocation, GLTF file handling, node processing, coordinate transformation, vertex extraction
**Symbols:** cloneMetaData, loadModelAndTexture
**Concepts:** entity ECS, model loading, GLTF parsing

## Summary
Handles cloning and loading of entity models, including texture and GLTF file parsing.

## Explanation
This chunk contains two main functions: `cloneMetaData` and `loadModelAndTexture`. The `cloneMetaData` function duplicates the metadata of an `EntityModel`, allocating new memory for arrays like nodes, parents, pivots, and strings using `main.worldArena.dupe`. It also clones a map (`nodeIndexMap`) that tracks node names to indices. The `loadModelAndTexture` function loads a model from a GLTF file, including its textures and geometry. It uses the CGLTF library to parse the file, load buffers, and validate the data. It then processes each node, calculating transformation matrices and mapping them into the engine's coordinate system. Finally, it extracts vertex and index data for rendering.

## Code Example
```zig
fn cloneMetaData(self: *EntityModel) EntityModel {
	const newNodes = main.worldArena.dupe(Node, self.nodes);
	const newNodeParents = main.worldArena.dupe(?u16, self.nodeParents);
	const newNodePivots = main.worldArena.dupe(Mat4f, self.nodePivots);
	return .{
		.height = self.height,
		.texturePath = main.worldArena.dupe(u8, self.texturePath),
		.modelId = if (self.modelId) |modelId| main.worldArena.dupe(u8, modelId) else null,
		.entityModelId = main.worldArena.dupe(u8, self.entityModelId),
		.vao = null,
		.indexCount = 0,
		.defaultTexture = null,
		.coordinateSystem = self.coordinateSystem,
		.nodeIndexMap = self.nodeIndexMap.clone() catch unreachable,
		.nodes = newNodes,
		.nodeParents = newNodeParents,
		.nodePivots = newNodePivots,
		.nodeCount = self.nodeCount,
	};
}
```

## Related Questions
- How does the `cloneMetaData` function handle memory allocation for duplicated arrays?
- What steps are involved in loading a model and texture using the `loadModelAndTexture` function?
- How is the GLTF file parsed and validated within this chunk?
- What transformation is applied to each node's position, rotation, and scale?
- How are vertices and indices extracted from the GLTF data for rendering?
- What error handling is implemented when loading a GLTF model?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_2*
