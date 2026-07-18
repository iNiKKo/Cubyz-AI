# [hard/codebase_src_block_entity.zig] - Chunk 2

**Type:** implementation
**Keywords:** block entities, inventory management, rendering, shaders, textures
**Symbols:** BlockEntityTypes, BlockEntityTypes.@"cubyz:chest", BlockEntityTypes.@"cubyz:chest".inventorySize, BlockEntityTypes.@"cubyz:chest".StorageServer, BlockEntityTypes.@"cubyz:chest".init, BlockEntityTypes.@"cubyz:chest".deinit, BlockEntityTypes.@"cubyz:chest".reset, BlockEntityTypes.@"cubyz:chest".onInventoryUpdateCallback, BlockEntityTypes.@"cubyz:chest".inventoryCallbacks, BlockEntityTypes.@"cubyz:chest".onLoadClient, BlockEntityTypes.@"cubyz:chest".onUnloadClient, BlockEntityTypes.@"cubyz:chest".onLoadServer, BlockEntityTypes.@"cubyz:chest".onUnloadServer, BlockEntityTypes.@"cubyz:chest".onStoreServerToDisk, BlockEntityTypes.@"cubyz:chest".onStoreServerToClient, BlockEntityTypes.@"cubyz:chest".updateClientData, BlockEntityTypes.@"cubyz:chest".updateServerData, BlockEntityTypes.@"cubyz:chest".getServerToClientData, BlockEntityTypes.@"cubyz:chest".getClientToServerData, BlockEntityTypes.@"cubyz:chest".renderAll, BlockEntityTypes.@"cubyz:sign", BlockEntityTypes.@"cubyz:sign".StorageServer, BlockEntityTypes.@"cubyz:sign".StorageClient, BlockEntityTypes.@"cubyz:sign".textureDeinitList, BlockEntityTypes.@"cubyz:sign".textureDeinitLock, BlockEntityTypes.@"cubyz:sign".pipeline, BlockEntityTypes.@"cubyz:sign".uniforms, BlockEntityTypes.@"cubyz:sign".textureWidth, BlockEntityTypes.@"cubyz:sign".textureHeight, BlockEntityTypes.@"cubyz:sign".textureMargin, BlockEntityTypes.@"cubyz:sign".init, BlockEntityTypes.@"cubyz:sign".deinit
**Concepts:** block entity management, inventory handling, text rendering, shader pipeline initialization, texture management

## Summary
Defines block entity types for chests and signs, including initialization, deinitialization, inventory management, and rendering logic.

## Explanation
The chunk defines two block entity types: 'cubyz:chest' and 'cubyz:sign'. Each type has its own storage structures, lifecycle methods (init, deinit, reset), and specific callbacks for handling inventory updates. The chest entity manages an inventory with a fixed size of 20 slots and handles server-side loading, unloading, storing to disk, and updating data. The sign entity manages text rendering, including texture management and shader pipeline initialization. Both entities handle synchronization between client and server states and provide methods for rendering.

### 'cubyz:chest'
- **Storage:** Uses `BlockEntityDataStorage` with an inventory ID (`invId`) to manage the chest's inventory data.
- **Inventory Size:** The chest has a fixed inventory size of 20 slots.
- **Lifecycle Methods:**
  - `init`: Initializes the storage server for the chest.
  - `deinit`: Deinitializes the storage server for the chest.
  - `reset`: Resets the storage server for the chest.
- **Callbacks:** Handles inventory updates with `onInventoryUpdateCallback` which sets a flag to indicate that the chunk has changed when an update occurs.
- **Server-Side Methods:*
  - `onLoadServer`: Loads data from the reader and creates an externally managed inventory on the server side.
  - `onUnloadServer`: Destroys the externally managed inventory and removes it from storage.
  - `onStoreServerToDisk`: Stores the chest's inventory to disk if it is not empty.
- **Client-Side Methods:*
  - `updateClientData`: Updates client-side data for the chest.
  - `updateServerData`: Handles server-side updates, including removing and updating the chest's inventory.

### 'cubyz:sign'
- **Storage:** Uses two storage structures (`StorageServer` and `StorageClient`) to manage text rendering and texture management.
- **Lifecycle Methods:**
  - `init`: Initializes the shader pipeline for text rendering, sets up texture deinitialization list, and initializes server-side storage.
  - `deinit`: Deinitializes the shader pipeline and cleans up textures from the deinitialization list.
- **Texture Management:*
  - `textureWidth`, `textureHeight`, `textureMargin`: Defines dimensions for text rendering textures.
  - `pipeline`: Initializes a shader pipeline with specific vertex and fragment shaders, uniforms, and attachments.

Both entities ensure proper synchronization between client and server states through their respective methods.

## Code Example
```zig
pub fn init() void {
	StorageServer.init();
}
```

## Related Questions
- What is the inventory size for the 'cubyz:chest' block entity?
- How does the 'cubyz:chest' handle server-side loading of data?
- What methods are available for managing textures in the 'cubyz:sign' block entity?
- How does the 'cubyz:sign' initialize its shader pipeline?
- What is the role of the 'textureDeinitList' in the 'cubyz:sign' block entity?
- How does the 'cubyz:chest' handle inventory updates on the server side?

*Source: unknown | chunk_id: codebase_src_block_entity.zig_chunk_2*
