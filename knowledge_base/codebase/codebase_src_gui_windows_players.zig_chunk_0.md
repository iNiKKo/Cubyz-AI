# [easy/codebase_src_gui_windows_players.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, player management, connection handling, dynamic updates, resource cleanup
**Symbols:** window, padding, userList, entityCount, kickbyConnection, kickByPlayerIndex, onOpen, onClose, update
**Concepts:** GUI window management, player list display, multiplayer interaction, dynamic content update

## Summary
Manages the GUI window for displaying and interacting with player lists in a multiplayer game.

## Explanation
This chunk defines the logic for a GUI window that displays players in a multiplayer game. It handles both client-side and server-side scenarios, updating the list of players dynamically. The `onOpen` function initializes the window content based on whether the game is running on a server or client. It uses various components like `VerticalList`, `HorizontalList`, `Label`, and `Button` to create an interactive player list. `kickByPlayerIndex` (used client-side, singleplayer/for other clients) sends the chat command `"kick @{playerIndex}"`; `kickbyConnection` (used server-side) directly calls `conn.disconnect()`. A connection still mid-handshake shows its remote IP with a "Cancel" button instead of a name with "Kick". The `onClose` function cleans up resources when the window is closed, and the `update` function ensures the player list remains current by checking for changes in the number of entities or connections.

## Code Example
```zig
pub fn onClose() void {
	if (main.server.world != null) {
		for (userList) |user| {
			user.decreaseRefCount();
		}
		main.globalAllocator.free(userList);
		userList = &.{};
	}
	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What is the purpose of the `onOpen` function?
- How does the chunk handle kicking players from the game?
- What components are used to create the player list in the GUI window?
- How does the `update` function ensure the player list remains current?
- What resources are cleaned up when the GUI window is closed?
- How does the chunk differentiate between client-side and server-side scenarios?

*Source: unknown | chunk_id: codebase_src_gui_windows_players.zig_chunk_0*
