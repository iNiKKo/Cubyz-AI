# [easy/codebase_src_gui_windows_connecting.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, ConnectionManager, atomic.Value, VerticalList, future.cancel, finishHandshake, restoreConnection, globalAllocator.dupe, openModalWindowFromRef, closeWindowFromRef
**Symbols:** State, window, connectionManager, ip, connectFuture, handshakeZon, state, errorMessage, start, cancel, onOpen, onClose, update
**Concepts:** modal window management, async connection task spawning, thread fallback on error, state machine with atomic transitions, handshake completion and world finish, error notification raising, settings persistence

## Summary
This chunk implements the GUI window for multiplayer connection management, handling state transitions between connecting, connected, failed, and cancelled states while coordinating with the ConnectionManager and test world handshake.

## Explanation
The chunk declares a GuiWindow instance named window with fixed content size (128x64), background enabled, and closeable disabled. It defines an enum State with four values: connecting, connected, failed, cancelled. Global variables include connectionManager (?*ConnectionManager), ip ([]const u8), connectFuture (?std.Io.Future(void)), handshakeZon (main.ZonElement), state (atomic.Value(State) initialized to .connecting), and errorMessage ([]const u8). The function start(_ip: []const u8, manager: *ConnectionManager) copies the IP address using main.globalAllocator.dupe, sets connectionManager, resets state to .connecting, opens a modal window via gui.openModalWindowFromRef(&window), and spawns connectFromNewThread asynchronously with main.io.concurrent. If spawning fails (e.g., thread creation error), it logs an error message and falls back to executing connectFromNewThread synchronously in the current thread. The function cancel() checks if connectFuture exists, cancels it via future.cancel(main.io), and nullifies connectFuture. onOpen() initializes a VerticalList with padding-based sizing, adds a Label showing 'Connecting...' centered at (0,0) spanning width, adds a Button labeled 'Cancel' whose onAction is initialized to the cancel function, finishes the list centered, assigns it as window.rootComponent, adjusts window content size based on component position and size plus padding, and calls gui.updateWindowPositions(). onClose() asserts connectFuture is null, frees ip if non-empty via main.globalAllocator.free, sets ip to empty string, and deinitializes window.rootComponent if present. update() performs a stateSwitch over state.load(.acquire). In .connecting it does nothing. In .connected it awaits connectFuture if present (nullifying it), calls main.game.testWorld.finishHandshake(handshakeZon) catching errors: on error it sets errorMessage to @errorName(err) and transitions state to .failed; on success it closes the window via gui.closeWindowFromRef(&window), frees settings.lastUsedIPAddress, duplicates ip into settings.lastUsedIPAddress, saves settings, closes all other open windows, and opens the HUD. In .failed it awaits connectFuture if present (nullifying it), closes the window, restores the connection manager via gui.windowlist.multiplayer_join.restoreConnection(connectionManager.?), raises a notification with errorMessage, then clears errorMessage. In .cancelled it closes the window and restores the connection manager without raising a notification.

## Code Example
```zig
fn cancel() void {
	if (connectFuture) |*future| {
		_ = future.cancel(main.io);
		connectFuture = null;
	}
}
```

## Related Questions
- What happens if main.io.concurrent fails to spawn the connection thread?
- How is the IP address stored and freed when the window closes?
- Which state transitions are possible from .connecting in this chunk?
- Does update() await connectFuture before calling finishHandshake?
- Where is settings.lastUsedIPAddress updated after a successful handshake?
- What does restoreConnection do with connectionManager.??

*Source: unknown | chunk_id: codebase_src_gui_windows_connecting.zig_chunk_0*
