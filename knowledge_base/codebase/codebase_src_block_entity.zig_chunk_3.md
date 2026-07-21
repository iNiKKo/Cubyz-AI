# [hard/codebase_src_block_entity.zig] - Chunk 3

**Type:** implementation
**Keywords:** mutex locking, binary serialization, memory allocation, error handling, data synchronization
**Symbols:** textureWidth, textureHeight, textureMargin, init, deinit, reset, onUnloadClient, onUnloadServer, onLoadClient, updateClientData, onLoadServer, updateServerData, onStoreServerToClient, onStoreServerToDisk, getServerToClientData, getClientToServerData, updateTextFromClient
**Concepts:** entity ECS, client-server synchronization, text updates, resource management

## Summary
Handles initialization, deinitialization, and data management for block entities, including client-server synchronization and text updates.

## Explanation
This chunk manages the lifecycle of block entities within the Cubyz engine. It initializes and deinitializes storage servers and clients, sets up graphics pipelines for rendering, and handles loading, updating, and storing entity data. The code includes functions for handling client and server-specific operations, such as removing entities, updating text, and synchronizing data between the client and server. It also manages memory allocation and deallocation for entity text and textures, ensuring proper resource management.

Specifically, it defines constants for texture dimensions:
- `textureWidth` is set to 128 pixels.
- `textureHeight` is set to 72 pixels.
- `textureMargin` is set to 4 pixels.

The initialization function (`init`) sets up the graphics pipeline with specific shader files and configuration options. The deinitialization function (`deinit`) cleans up resources such as textures, pipelines, and storage servers/clients. Memory allocation for entity text involves duplicating strings using `main.globalAllocator.dupe(u8, event.update.remaining)` and freeing memory when entities are removed or updated.

The initialization function (`init`) is defined as follows:
```zig
pub fn init() void {
    StorageServer.init();
    StorageClient.init();
    if (!main.settings.launchConfig.headlessServer) {
        pipeline = graphics.Pipeline.init(
            "assets/cubyz/shaders/block_entity/sign.vert",
            "assets/cubyz/shaders/block_entity/sign.frag",
            "",
            &uniforms,
            graphics.VertexArray.EmptyVertex,
            &.{},
            .{},
            .{.depthTest = true, .depthCompare = .equal, .depthWrite = false},
            .{.attachments = &.{.alphaBlending}},
        );
    }
}
```

The deinitialization function (`deinit`) is defined as follows:
```zig
pub fn deinit() void {
    while (textureDeinitList.popOrNull()) |texture| {
        texture.deinit();
    }
    textureDeinitList.deinit(main.globalAllocator);
    if (!main.settings.launchConfig.headlessServer) {
        pipeline.deinit();
    }
    StorageServer.deinit();
    StorageClient.deinit();
}
```

## Code Example
```zig
pub fn deinit() void {
	while (textureDeinitList.popOrNull()) |texture| {
		texture.deinit();
	}
	textureDeinitList.deinit(main.globalAllocator);
	if (!main.settings.launchConfig.headlessServer) {
		pipeline.deinit();
	}
	StorageServer.deinit();
	StorageClient.deinit();
}
```

## Related Questions
- What specific values are assigned to textureWidth, textureHeight, and textureMargin?
- How does the initialization function (`init`) set up the graphics pipeline with shader files and configuration options?

*Source: unknown | chunk_id: codebase_src_block_entity.zig_chunk_3*
