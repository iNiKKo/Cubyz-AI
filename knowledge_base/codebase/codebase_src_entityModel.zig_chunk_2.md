# [medium/codebase_src_entityModel.zig] - Chunk 2

**Type:** implementation
**Keywords:** GLTF, hierarchy depth, primitive type filtering, coordinate system conversion, vertex attributes, VAO binding, entity model registration, default fallback, StringHashMapUnmanaged, List
**Symbols:** EntityModel, EntityModelIndex, playerEntityModels, reverseIndices, entityModels, getHierarchyDepth, bind
**Concepts:** GLTF asset loading, hierarchy depth calculation, primitive type filtering, coordinate system conversion, vertex attribute extraction, VAO binding, entity model registration, default fallback handling

## Summary
This chunk defines the EntityModel struct and its associated entity management API, including initialization from GLTF assets, hierarchy depth calculation, primitive processing with coordinate system conversion, vertex attribute extraction (position/normal/texcoord), VAO binding, model registration via an index map, default fallback handling, and bulk reset logic.

## Explanation
The chunk declares EntityModel as a struct containing fields for node pivots, parents, VAO, index count, node count, coordinate system, vertices, indices, default texture, and metadata. It implements init() which processes GLTF nodes: it maps parent relationships via nodeIndexMap (returning error.EntityModelPrimitiveHasNoParent if missing), computes final transformation matrices by applying translation, rotationQuat, and scale conversions through self.coordinateSystem.convertVec/convertQuat/convertScale, filters primitives to only c.cgltf_primitive_type_triangles (warning on others), reads indicesAccessor and attributes (position, normal, texcoord) via cgltf_accessor.read_float into local buffers, then constructs Vertex entries with converted positions, normals, UVs (flipped Y), and nodeId set to the parent index. After processing all nodes it initializes self.vao from vertices/indices arrays and sets counts. getHierarchyDepth recursively walks node.parent until null, incrementing depth each step. bind() calls vao.bind() and defaultTexture.bindTo(0). EntityModelIndex is a struct holding an index with a getter that asserts bounds before returning &entityModels.items[self.index]. Global vars playerEntityModels (List of EntityModelIndex), reverseIndices (StringHashMapUnmanaged mapping entityModelId to EntityModelIndex), and entityModels (List of EntityModel) are declared. register() creates an EntityModelIndex, appends a new EntityModel.init(...) to entityModels using main.worldArena, then inserts the index into reverseIndices (panic on OOM). reset() iterates all models calling model.deinit(), clears lists, and resets playerEntityModels. getById() looks up id in reverseIndices returning ?EntityModelIndex or null. default() checks for 

## Related Questions
- What error is returned when a primitive lacks a parent node in EntityModel.init?
- How does getHierarchyDepth compute the depth of a GLTF node hierarchy?
- Which primitive type is accepted by default and what happens to others during init?
- Describe how coordinate system conversion is applied to position, rotation, and scale attributes.
- What fields are populated in each Vertex entry after processing a triangle primitive?
- How does the bind method prepare EntityModel for rendering?
- Explain the purpose of reverseIndices and how it relates to entityModels.
- What happens inside reset() when clearing all registered models?
- How does getById handle missing identifiers versus the special default fallback?
- Is there any concurrency protection around entityModels or reverseIndices in this chunk?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_2*
