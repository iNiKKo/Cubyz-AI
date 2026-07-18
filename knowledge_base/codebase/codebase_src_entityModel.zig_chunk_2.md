# [medium/codebase_src_entityModel.zig] - Chunk 2

**Type:** implementation
**Keywords:** memory allocation, GLTF file handling, node processing, coordinate transformation, vertex extraction
**Symbols:** cloneMetaData, loadModelAndTexture
**Concepts:** entity ECS, model loading, GLTF parsing

## Summary
Handles cloning and loading of entity models, including texture and GLTF file parsing.

## Explanation
This chunk contains two main functions: `cloneMetaData` and `loadModelAndTexture`. The `cloneMetaData` function duplicates the metadata of an `EntityModel`, allocating new memory for arrays like nodes, parents, pivots, and strings using `main.worldArena.dupe`. It also clones a map (`nodeIndexMap`) that tracks node names to indices. Specifically, it initializes all fields as follows:

- `height`: copied from the original entity model.
- `texturePath`: duplicated string using `main.worldArena.dupe(u8, self.texturePath)`.
- `modelId`: duplicated string if present, otherwise set to null.
- `entityModelId`: duplicated string using `main.worldArena.dupe(u8, self.entityModelId)`.
- `vao`, `indexCount`, and `defaultTexture` are initialized to null or zero.
- `coordinateSystem`: copied from the original entity model.
- `nodeIndexMap`: cloned map using `self.nodeIndexMap.clone()`.
- `nodes`, `nodeParents`, and `nodePivots`: duplicated arrays using `main.worldArena.dupe(Node, self.nodes)`, `main.worldArena.dupe(?u16, self.nodeParents)`, and `main.worldArena.dupe(Mat4f, self.nodePivots)` respectively.
- `nodeCount`: copied from the original entity model.

The `loadModelAndTexture` function loads a model from a GLTF file, including its textures and geometry. It uses the CGLTF library to parse the file (`c.cgltf_parse`), load buffers (`c.cgltf_load_buffers`), and validate the data (`c.cgltf_validate`). For each node in the parsed GLTF data, it calculates transformation matrices by converting translation, rotation, and scale from the GLTF coordinate system to the engine's coordinate system. It also processes each primitive within a mesh, extracting vertex and index data for rendering.

Specifically, the function performs the following steps:
- Initializes `vertices` and `indices` lists using `main.List(Vertex)` and `main.List(u32)`, respectively.
- Sorts nodes by depth to ensure correct hierarchy processing.
- Allocates memory for `nodes`, `nodeParents`, and `nodePivots` arrays in the world arena.
- For each node, it calculates a transformation matrix (`pivotMat`) using translation, rotation, and scale transformations converted from GLTF coordinates to engine coordinates.
- Maps nodes into the engine's coordinate system by setting up parent-child relationships based on the parsed hierarchy.
- Extracts vertex data for rendering by iterating through primitives in the mesh, converting positions, normals, and UVs as necessary. It also handles error cases such as unsupported primitive types or missing parent nodes.

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

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_2*
