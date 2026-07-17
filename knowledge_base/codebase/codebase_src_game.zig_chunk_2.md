# [hard/codebase_src_game.zig] - Chunk 2

**Type:** implementation
**Keywords:** connection management, asset loading, game pause, handshake processing, inventory setup
**Symbols:** World, World.conn, World.manager, World.name, World.milliTime, World.gameTime, World.dayTime, World.connected, World.paused, World.blockPalette, World.itemPalette, World.proceduralItemPalette, World.biomePalette, World.entityModelPalette, World.entityComponentPalette, World.itemDrops, World.playerBiome, World.shouldRestart, World.shouldReload, World.init, World.@continue, World.deinit, World.pause, World.finishHandshake
**Concepts:** networking, asset management, game state initialization, player inventory, gamemode handling

## Summary
The `World` struct manages game state, including initialization, deinitialization, and handling network handshakes.

## Explanation
The `World` struct in the Cubyz engine is responsible for managing various aspects of the game world. It initializes network connections, handles assets, and sets up game states such as player inventory and gamemode. The `init` method establishes a connection to the server, while the `deinit` method cleans up resources. The `pause` method pauses the game, deinitializes GUIs, and resets various components. The `finishHandshake` method processes data received during the handshake with the server, initializing palettes and loading assets.

## Code Example
```zig
pub fn deinit(self: *World) void {
	main.server.stop(.stop);

	if (main.server.thread) |serverThread| {
		serverThread.join();
		main.server.thread = null;
	}

	self.conn.deinit();

	self.connected = false;
	self.pause();
	self.manager.deinit();
}
```

## Related Questions
- What is the purpose of the `World` struct in the Cubyz engine?
- How does the `World` struct initialize network connections?
- What methods are available for deinitializing the game world?
- How does the `World` struct handle pausing the game?
- What assets are loaded during the handshake process?
- How is the player's inventory initialized in the `World` struct?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_2*
