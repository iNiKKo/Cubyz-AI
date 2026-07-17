# [medium/codebase_src_entityModel.zig] - Chunk 1

**Type:** api
**Keywords:** texture path, GLTF parse, cgltf_load_buffers, NodeRemap, depth sort, nodeIndexMap, vertex extraction, chunk_type
**Symbols:** deinit, cloneMetaData, loadModelAndTexture
**Concepts:** texture path resolution, GLTF parsing, hierarchy depth sorting, node index mapping, coordinate system conversion

## Summary
This chunk implements the EntityModel public API for texture path resolution and GLTF model loading. It defines deinit(), cloneMetaData(), loadModelAndTexture() with full parsing of cgltf data, hierarchy depth sorting, node index mapping, parent linking, coordinate system conversion, vertex/attribute extraction, and error handling.

## Explanation
The chunk begins by resolving the texture path: it splits the input string on ':' to obtain a module identifier and texture name, then attempts to load from main.worldArena.allocator using an assetFolder prefix; if that fails (caught), it falls back to a static assets/... path. The deinit() method cleans up self.defaultTexture and self.vao by calling their respective deinit methods. cloneMetaData() performs deep duplication of all owned fields: Node array, ?u16 nodeParents, Mat4f nodePivots, texturePath bytes, modelId bytes, entityModelId bytes; it leaves vao null, resets indexCount to 0, and copies coordinateSystem and clones nodeIndexMap. loadModelAndTexture() is the core implementation: after initializing self.defaultTexture from the resolved path, it checks that a modelId exists (otherwise returning error.NoModelSpecified). It reads the .glb asset via main.assets.readAsset into a stack-allocated buffer, then parses with c.cgltf_parse; on failure it logs and returns getGltfError(result). Buffers are loaded with c.cgltf_load_buffers(

## Related Questions
- What happens when the texture path resolution fails in loadModelAndTexture?
- How does cloneMetaData handle duplication of owned fields versus borrowed references?
- Which error is returned if a GLTF parse step fails and how is it reported to the caller?
- In what order are nodes processed after cgltf_parse and why is depth sorting required?
- What is the purpose of NodeRemap.compareDepth and how does it affect nodeIndexMap population?
- How are vertex attributes extracted from a GLTF primitive in loadModelAndTexture?
- What error is returned if a primitive type other than triangles is encountered?
- Does cloneMetaData reset indexCount to zero, and why might that be necessary?
- Where does the chunk allocate memory for nodes, nodeParents, and nodePivots?
- How are parent relationships between GLTF nodes resolved after hierarchy sorting?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_1*
