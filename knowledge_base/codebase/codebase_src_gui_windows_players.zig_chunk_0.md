# [easy/codebase_src_gui_windows_players.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, HorizontalList, playerComponent, entity_manager, connectionManager, chatCommand, increaseRefCount, decreaseRefCount, mutex locking
**Symbols:** window, padding, userList, entityCount, kickbyConnection, kickByPlayerIndex, onOpen, onClose, update
**Concepts:** GUI window management, player list rendering, connection enumeration, entity manager integration, chat command execution, reference counting for users, vertical/horizontal lists, kick controls

## Summary
This chunk defines the player list GUI window, handling both local entity enumeration and remote connection listing with kick controls.

## Explanation
The chunk declares a global GuiWindow instance named window with a fixed content size of Vec2f{128, 256} and closeIfMouseIsGrabbed set to true. It maintains a userList array of main.server.User pointers (initialized empty) and an entityCount usize tracking the number of entities when no world exists. The chunk defines two functions: kickbyConnection(conn: *main.network.Connection) void which calls conn.disconnect(), and kickByPlayerIndex(playerIndex: usize) void which allocates a chat command string via std.fmt.allocPrint(main.globalAllocator.allocator, "kick @{d}", .{playerIndex}) catch unreachable and executes it through main.sync.client.executeCommand(.{.chatCommand = .{.message = command}}). The onOpen() function initializes a VerticalList with padding 8 and height 300, width 16; if main.server.world is null it enumerates main.client.entity_manager.entities.items(), retrieves the playerComponent via main.entity.components.@

## Code Example
```zig
fn kickbyConnection(conn: *main.network.Connection) void {
	conn.disconnect();
}
```

## Related Questions
- What is the default content size of the player list window?
- How does the chunk handle the case when main.server.world is null during onOpen?
- Which function is called to execute a kick chat command?
- What padding value is used for the VerticalList in onOpen?
- How are remote connections enumerated and displayed in onOpen?
- What happens to userList memory when the world exists versus when it does not?
- Does the chunk use any mutex locking, and where?
- Which component retrieves player data from entities?
- What label text is shown when no other players exist locally?
- How are kick buttons wired for local entities versus remote connections?

*Source: unknown | chunk_id: codebase_src_gui_windows_players.zig_chunk_0*
