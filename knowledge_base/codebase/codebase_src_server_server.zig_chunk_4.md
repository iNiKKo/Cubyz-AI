# [hard/codebase_src_server_server.zig] - Chunk 4

**Type:** implementation
**Keywords:** mutex locking, binary serialization, error handling, networking, player state update
**Symbols:** User, User.update, User.receiveCommand, User.receiveData, User.sendMessage, User.sendRawMessage, User.hasPermission, User.getSpawnPos, User.format, updatesPerSec, updateTime, world, userMutex, users, userDeinitList, userConnectList, connectionManager, running, restart, lastTime, thread
**Concepts:** user management, command processing, world interaction, server operations

## Summary
Handles user updates, command processing, and world interactions in the server.

## Explanation
This chunk defines the `User` struct with methods for updating user state, receiving commands and data, sending messages, checking permissions, getting spawn positions, and formatting user information. It also includes static variables for managing users, a connection manager, and a thread for server operations. The `init` function sets up the world, initializes various components, and starts the connection manager. The `deinit` function pauses operations, clears user lists, and unschedules players.

## Code Example
```zig
pub fn sendMessage(self: *User, comptime fmt: []const u8, args: anytype) void {
	const msg = std.fmt.allocPrint(main.stackAllocator.allocator, fmt, args) catch unreachable;
	defer main.stackAllocator.free(msg);
	self.sendRawMessage(msg);
}
```

## Related Questions
- How does the `User` struct handle command data?
- What is the purpose of the `receiveData` method in the `User` struct?
- How does the server manage user permissions?
- What happens if a world generation fails during server initialization?
- How are users managed and tracked by the server?
- What role does the `connectionManager` play in the server operations?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_4*
