# [medium/codebase_src_entityModel.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, extern struct, pub const, std.StringHashMap, Vec3f, Quat, Mat4f, ZonElement, texturePath, coordinateSystem, vertex attributes, arena allocator
**Symbols:** EntityModel, Node, Vertex, recalc, attributeDescriptions
**Concepts:** entity hierarchy, mesh vertex layout, Zon element parsing, texture path resolution, coordinate system selection, tag-based player model detection, arena allocation, Vulkan vertex input descriptors

## Summary
This chunk defines the EntityModel struct and its Node/Vertex types with initialization logic that reads height, texture paths, coordinate systems, and tags from Zon elements, plus deinit and cloneMetaData methods.

## Explanation
The chunk declares pub const EntityModel = struct { ... } containing fields: height (f32), texturePath ([]const u8), modelId (?[]const u8), entityModelId ([]const u8), nodeIndexMap (std.StringHashMap(u16)), nodes ([]Node), nodeParents ([]?u16), nodePivots ([]Mat4f), nodeCount (u16), vao (?graphics.VertexArray), indexCount (c_int), defaultTexture (?main.graphics.Texture), coordinateSystem (CoordinateSystem). Inside EntityModel, pub const Node = struct { pos: Vec3f, rot: vec.Quat, scale: Vec3f } with a method recalc(self: Node, pivotMat: Mat4f) Mat4f that multiplies translation, rotationQuat, and scale into the given pivot matrix. pub const Vertex = extern struct { pos: [3]f32, normal: [3]f32, uv: [2]f32, nodeId: c_uint } with a static attributeDescriptions array of four VkVertexInputAttributeDescription entries mapping locations 0–3 to the vertex fields using @offsetOf. The init function takes assetFolder ([]const u8), entityModelId ([]const u8), index (EntityModelIndex), and zon (ZonElement) and returns an EntityModel. It reads modelId from zon.get(

## Related Questions
- What fields does the EntityModel struct contain and what are their types?
- How is the Node type defined within EntityModel and what transformation does its recalc method perform?
- Describe the Vertex extern struct layout and how attributeDescriptions maps each vertex field to a Vulkan input location.
- In init, how is modelId obtained from zon and under what condition is it set to null?
- How does init determine whether an entity model represents the player based on tags loaded from zon?
- What steps are taken in init to construct texturePath when a defaultTexture entry exists in zon?
- If file access for texturePath fails, how does init fall back to an assets directory path and what cleanup occurs?
- How is coordinateSystem chosen if not explicitly provided by zon?
- What allocations are performed for nodeIndexMap, nodes, nodeParents, nodePivots in init?
- When cloneMetaData is called, which fields are duplicated using main.worldArena.dupe and how is modelId handled when it is null?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_0*
