# [easy/codebase_src_entityComponent_model.zig] - Chunk 0

**Type:** implementation
**Keywords:** SparseSet, BinaryReader, BinaryWriter, EntityModel, Mat4f, Vec3d, Vec3f, NeverFailingAllocator, entityComponentID, entityComponentVersion, client, server
**Symbols:** entityComponentID, entityComponentVersion, client, server, Component, components, init, deinit, clear, load, unload, get
**Concepts:** component management, client-server separation, entity models, binary serialization, memory allocation

## Summary
Manages entity components for both client and server.

## Explanation
The code defines structures and functions to manage entity components, including loading, unloading, and saving. It includes separate implementations for client and server environments.

## Code Example
```zig
pub fn load(entity: Entity, reader: *utils.BinaryReader, version: u32) main.entity.EntityComponentLoadError!void {
	if (version != 0) return error.InvalidComponentVersion;

	const entityModel = reader.readVarInt(u32) catch return error.UnreadableComponentData;

	var ptr: *Component = undefined;
	if (components.get(entity)) |p| {
		ptr = p;
		ptr.deinit();
	} else {
		ptr = components.add(main.globalAllocator, entity);
	}
	ptr.* = Component{
		.entityModel = .{.index = entityModel},
	};
	const model = ptr.entityModel.get();

	ptr.matrices = main.globalAllocator.alloc(Mat4f, model.nodeCount);
	ptr.nodes = main.globalAllocator.dupe(EntityModel.Node, model.nodes);
}
```

## Related Questions
- What structure is used to manage entity components?
- How does the client handle loading an entity component?
- What error handling is done during component loading?
- How are memory allocations managed for component data?
- What function initializes the server-side component management system?
- How does the server unload a component from an entity?

*Source: unknown | chunk_id: codebase_src_entityComponent_model.zig_chunk_0*
