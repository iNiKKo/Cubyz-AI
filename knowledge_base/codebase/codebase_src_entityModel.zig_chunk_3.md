# [medium/codebase_src_entityModel.zig] - Chunk 3

**Type:** implementation
**Keywords:** GLTF parsing, vertex buffer, index buffer, error handling, scene graph traversal
**Symbols:** EntityModel, EntityModel.vao, EntityModel.indexCount, EntityModel.nodeCount, EntityModel.loadFromGltf, EntityModel.getHierarchyDepth, EntityModel.getGltfError, EntityModel.bind
**Concepts:** entity ECS, 3D model loading, GLTF format, vertex array object binding

## Summary
The chunk implements entity model loading and binding using GLTF format.

## Explanation
This chunk defines the `EntityModel` struct, which handles the loading of 3D models in the GLTF format. It includes methods for processing primitives, reading attributes like position, normal, and UV coordinates, converting them to engine-specific formats, and binding the model for rendering. The `getHierarchyDepth` function calculates the depth of a node in the scene graph, while `getGltfError` maps CGltf error codes to Zig errors. The `bind` method prepares the model for rendering by binding the vertex array object and texture.

## Code Example
```zig
pub fn bind(self: *EntityModel) void {
		self.vao.?.bind();
		self.defaultTexture.?.bindTo(0);
	}
```

## Related Questions
- How does the `EntityModel` struct handle GLTF model data?
- What is the purpose of the `getHierarchyDepth` function in this chunk?
- How are errors from CGltf mapped to Zig errors in this code?
- What steps are involved in binding an entity model for rendering?
- How does the chunk process vertex and index data from GLTF primitives?
- What is the role of the `coordinateSystem.convertVec` method in this implementation?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_3*
