# [easy/codebase_src_gui_windows_players.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, player management, connection handling, dynamic updates, resource cleanup
**Symbols:** window, padding, userList, entityCount, kickbyConnection, kickByPlayerIndex, onOpen, onClose, update
**Concepts:** GUI window management, player list display, multiplayer interaction, dynamic content update

## Summary
Manages the GUI window for displaying and interacting with player lists in a multiplayer game.

## Explanation
This chunk defines the logic for a GUI window that displays players in a multiplayer game. It handles both client-side and server-side scenarios, updating the list of players dynamically. The `onOpen` function initializes the window content based on whether the game is running on a server or client. If the game is running on the client side, it lists all entities with player components, displaying their names and providing a 'Kick' button to remove them from the game using the chat command `"kick @{playerIndex}"`. On the server side, it lists connected users, showing their usernames if the handshake is complete or their IP addresses if not, along with appropriate buttons ('Kick' for completed handshakes and 'Cancel' for ongoing ones). The `kickByPlayerIndex` function sends a chat command to kick a player by index, while `kickbyConnection` directly disconnects a server-side connection. The `onClose` function cleans up resources when the window is closed, including decreasing reference counts for users and freeing the user list. The `update` function ensures the player list remains current by checking for changes in the number of entities or connections.

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
