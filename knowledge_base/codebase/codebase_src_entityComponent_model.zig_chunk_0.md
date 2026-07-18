# [easy/codebase_src_entityComponent_model.zig] - Chunk 0

**Type:** api
**Keywords:** SparseSet, BinaryReader, Mat4f, EntityModel, error handling
**Symbols:** entityComponentID, entityComponentVersion, client.Component, client.components, client.init, client.deinit, client.clear, client.load, client.unload, client.get, server.Component, server.components, server.init, server.deinit, server.loadFromData, server.unload, server.put, server.get
**Concepts:** entity ECS, model component, client-server architecture, data serialization

## Summary
Defines the model component for entities, handling both client and server logic including initialization, deinitialization, loading, unloading, and data serialization.

## Explanation
This chunk defines the model component for entities in the Cubyz engine. It includes separate structures and functions for client-side and server-side operations. The client structure manages rendering-related data such as matrices and nodes, while the server handles saving and transmitting changes. Both sides use a `SparseSet` to map entities to their respective components. Functions like `init`, `deinit`, `load`, `unload`, and `get` are provided for managing component lifecycle and access. The chunk also includes error handling for version mismatches and data reading issues.

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
