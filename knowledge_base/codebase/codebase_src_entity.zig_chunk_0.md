# [medium/codebase_src_entity.zig] - Chunk 0

**Type:** api
**Keywords:** error handling, function pointers, vtable, component lifecycle, binary serialization
**Symbols:** components, systems, EntityNetworkData, EntityComponentLoadError, Entity, EntityComponentId, EntityComponentVTable, componentList, initComponents, deinitComponents, loadComponent, unloadComponent
**Concepts:** entity ECS, networking protocol

## Summary
Manages entity components and their lifecycle, including initialization, loading, unloading, and network data handling.

## Explanation
This chunk defines the core logic for managing entity components within the Cubyz engine. It includes structures for representing entity network data, error types for component loading issues, and an enumeration for entities. The `EntityComponentVTable` struct holds function pointers for server and client load/unload operations. The `initComponents` function initializes a list of component vtables based on imported component definitions, ensuring each component has unique IDs and proper methods assigned. The `deinitComponents` function clears the component list. The `loadComponent` and `unloadComponent` functions handle loading and unloading components for both server and client sides, using the appropriate vtable methods and handling errors such as unknown component IDs.

## Code Example
```zig
pub fn deinitComponents() void {
	componentList = undefined;
}
```

## Related Questions
- How are entity components initialized in the Cubyz engine?
- What is the purpose of the `EntityComponentVTable` struct?
- How does the `loadComponent` function handle errors?
- What is the role of the `componentList` variable?
- How are duplicate component IDs detected and handled?
- What methods are available for loading and unloading components on the server side?

*Source: unknown | chunk_id: codebase_src_entity.zig_chunk_0*
