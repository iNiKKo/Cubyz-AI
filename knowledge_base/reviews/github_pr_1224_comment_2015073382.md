# [src/entity_data.zig] - PR #1224 review diff

**Type:** review
**Keywords:** entity data, vtable, thread safety, block entity, mutex, lifecycle events, polymorphic behavior, R&D phase
**Symbols:** EntityDataClass, VTable, onLoadClient, onUnloadClient, onLoadServer, onUnloadServer, onPlaceClient, onBreakClient, onPlaceServer, onBreakServer, onInteract, BlockEntityData, EntryT, storage, init, deinit, reset, add, remove, get
**Concepts:** thread safety, vtable pattern, generic programming, mutex lock

## Summary
The `entity_data.zig` file introduces a new module for managing entity data, including a struct `EntityDataClass` with methods for handling various lifecycle events and interactions. It also defines a generic type `BlockEntityData` for block-specific entity data management.

## Explanation
This change adds a comprehensive system for managing entity data within the Cubyz game engine. The `EntityDataClass` struct is designed to handle different types of entities with a vtable pattern, allowing for polymorphic behavior through function pointers. Each method in the vtable is wrapped with a mutex lock to ensure thread safety during concurrent access.

The `VTable` struct contains the following methods:
- `onLoadClient`: Called when an entity is loaded on the client side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onUnloadClient`: Called when an entity is unloaded on the client side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onLoadServer`: Called when an entity is loaded on the server side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onUnloadServer`: Called when an entity is unloaded on the server side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onPlaceClient`: Called when an entity is placed on the client side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onBreakClient`: Called when an entity is broken on the client side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onPlaceServer`: Called when an entity is placed on the server side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onBreakServer`: Called when an entity is broken on the server side. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `void`.
- `onInteract`: Called when an entity is interacted with (right-click). Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `bool` indicating if the event was handled.

The `BlockEntityData` generic type provides specific functionality for managing block-related entity data. It includes:
- `EntryT`: A struct containing the absolute block position and associated data.
- `storage`: A list of `EntryT` entries.
- `init`: Initializes the storage list.
- `deinit`: Deinitializes the storage list.
- `reset`: Clears the storage list while retaining capacity.
- `add`: Adds a new entry to the storage list and updates the chunk's blockPosToEntityDataMap. Parameters: `pos: Vec3i`, `chunk: *Chunk`.
- `remove`: Removes an entry from the storage list and updates entity data across chunks if necessary. Parameters: `pos: Vec3i`, `chunk: *Chunk`.
- `get`: Retrieves data for a specific block position. Parameters: `pos: Vec3i`, `chunk: *Chunk`. Return type: `?*DataT`.

The reviewer suggests keeping the design simple until it's needed for functional use, indicating that this code is in an R&D phase.

## Related Questions
-  What is the purpose of the `EntityDataClass` struct?
-  How does the `BlockEntityData` type manage block-specific entity data?
-  Why are mutex locks used in each method of `EntityDataClass`?
-  What is the role of the vtable pattern in this design?
-  How does the `add` function handle adding new entries to the storage list?
-  What happens if an entry cannot be removed from the chunk's blockPosToEntityDataMap?
-  How does the `get` function retrieve data for a specific block position?
-  Why is the reviewer suggesting keeping the design simple until it's needed?
-  What are the potential implications of using a vtable pattern in this context?
-  How does the `remove` function handle updating entity data across chunks?

*Source: unknown | chunk_id: github_pr_1224_comment_2015073382*
