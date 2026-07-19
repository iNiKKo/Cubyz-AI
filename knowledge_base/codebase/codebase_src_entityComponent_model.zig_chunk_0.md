# [easy/codebase_src_entityComponent_model.zig] - Chunk 0

**Type:** api
**Keywords:** SparseSet, BinaryReader, Mat4f, EntityModel, error handling
**Symbols:** entityComponentID, entityComponentVersion, client.Component, client.components, client.init, client.deinit, client.clear, client.load, client.unload, client.get, server.Component, server.components, server.init, server.deinit, server.loadFromData, server.unload, server.put, server.get
**Concepts:** entity ECS, model component, client-server architecture, data serialization

## Summary
Defines the model component for entities, handling both client and server logic including initialization, deinitialization, loading, unloading, and data serialization.

## Explanation
This chunk defines the model component for entities in the Cubyz engine, with `entityComponentVersion = 0` -- `load`/`loadFromData` both return `error.InvalidComponentVersion` if the given version doesn't match 0. It includes separate structures and functions for client-side and server-side operations.

The client structure (`client.Component`) manages rendering-related data such as matrices and nodes. The struct contains:
- `entityModel`: an index to the entity model.
- `bufferAllocation`: a sub-allocation for node buffer.
- `matrices`: an array of transformation matrices.
- `nodes`: an array of entity model nodes.

The client structure provides functions like:
- `deinit`: frees matrices, nodes, and releases the buffer allocation from `modelRenderer.client.nodeBuffer`.
- `init`: initializes the client-side model component system.
- `deinit`: deinitializes the client-side model component system.
- `clear`: clears all components.
- `load`: loads a component from binary data, initializing or updating the component as needed.
- `unload`: unloads a component by freeing its resources and removing it from the sparse set.
- `get`: retrieves a component for an entity.

The server structure (`server.Component`) holds just an `entityModel` index. The server provides functions like:
- `init`: initializes the server-side model component system.
- `deinit`: deinitializes the server-side model component system.
- `loadFromData`: loads a component from binary data, initializing or updating the component as needed.
- `unload`: unloads a component by removing it from the sparse set.
- `put`: stores/overwrites a component and calls `main.entity.server.transmitChange(Self, entity)` to notify clients of the change.
- `get`: retrieves a component for an entity.

Both sides use a `SparseSet` to map entities to their respective components. Functions like `init`, `deinit`, `load`, `unload`, and `get` are provided for managing component lifecycle and access.

## Code Example
```zig
pub fn deinit(self: Component) void {
	main.globalAllocator.free(self.matrices);
	main.globalAllocator.free(self.nodes);

	main.entity.systems.modelRenderer.client.nodeBuffer.free(self.bufferAllocation);
}
```

## Related Questions
- What is the purpose of the `client.Component` struct?
- How does the server handle saving entity model components?
- What function initializes the client-side model component system?
- How are matrices and nodes managed in the client's model component?
- What error can occur when loading a model component with an invalid version?
- How is the `SparseSet` used to manage entity components on both the client and server?
- What does the `put` function do in the server-side component management?
- How is memory freed for a model component during deinitialization?
- What is the role of the `entityModel` field in both client and server components?
- How are changes to entity models transmitted from the server to clients?

*Source: unknown | chunk_id: codebase_src_entityComponent_model.zig_chunk_0*
