# [src/entity_data.zig] - PR #1224 review diff

**Type:** review
**Keywords:** EntityDataClass, VTable, mutex, BlockEntityData, List, Vec3i, Chunk, onLoadClient, onUnloadClient, onPlaceServer, thread safety
**Symbols:** EntityDataClass, VTable, onLoadClient, onUnloadClient, onLoadServer, onUnloadServer, onPlaceClient, onBreakClient, onPlaceServer, onBreakServer, onInteract, BlockEntityData, EntryT, storage, init, deinit, reset, add, remove, get
**Concepts:** thread safety, vtable pattern, generic programming, block management, entity lifecycle

## Summary
The `entity_data.zig` file introduces a new module for managing entity data, including a struct `EntityDataClass` with methods for handling various lifecycle events of entities. It also defines a generic type `BlockEntityData` for storing block-specific entity data.

## Explanation
This change adds a comprehensive system for managing entity data within the Cubyz game engine. The `EntityDataClass` struct is designed to handle different lifecycle events such as loading, unloading, placing, breaking, and interacting with entities. It uses a vtable pattern to allow dynamic dispatch of these methods. Each method in `EntityDataClass` acquires a mutex lock before executing the corresponding vtable function, ensuring thread safety during concurrent access.

The `BlockEntityData` generic type is introduced to manage block-specific entity data. It includes functions for initializing, deinitializing, resetting, adding, removing, and retrieving entity data associated with blocks. The storage for these entities is managed using a list (`List(EntryT)`), and each entry contains the absolute block position and the actual data.

The reviewer suggests keeping the architecture simple until it is needed for functional use, particularly after the Chest feature is completed. This approach aims to simplify changes and limit diffs to one file in case of interface changes.

## Related Questions
- What is the purpose of the `EntityDataClass` struct in the Cubyz game engine?
- How does the `BlockEntityData` generic type manage block-specific entity data?
- Why are mutex locks used in each method of `EntityDataClass`?
- What is the role of the vtable pattern in the `EntityDataClass` struct?
- How does the `add` function handle adding new entity data to a chunk?
- What happens if an entry cannot be found during the removal process in `BlockEntityData`?
- How does the `get` function retrieve entity data associated with a block position?
- Why is the reviewer suggesting keeping the architecture simple until further notice?
- What are the potential benefits of separating the entity data management into multiple files?
- How does the `deinit` function ensure proper cleanup of resources in `BlockEntityData`?

*Source: unknown | chunk_id: github_pr_1224_comment_2015073382*
