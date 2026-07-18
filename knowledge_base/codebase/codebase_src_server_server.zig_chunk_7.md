# [hard/codebase_src_server_server.zig] - Chunk 7

**Type:** api
**Keywords:** mutex locking, network protocols, message broadcasting, user list management, reference counting
**Symbols:** removePlayer, connect, connectInternal, messageFrom, sendRawMessage, sendMessage, getUserByIndexAndIncreaseRefCount, chatMutex
**Concepts:** player management, network communication, thread safety, reference counting

## Summary
Handles player connection, disconnection, and messaging in the server.

## Explanation
This chunk contains functions to manage player connections and communications within a server environment. Specifically, it includes methods for removing a player (`removePlayer`), connecting a player (`connect`, `connectInternal`), handling incoming messages from players (`messageFrom`), sending raw messages (`sendRawMessage`), sending formatted messages (`sendMessage`), and retrieving users by index with reference counting (`getUserByIndexAndIncreaseRefCount`). The chunk uses mutexes for thread safety, particularly around user lists. It also interacts with network protocols to send player data and updates to other clients.

### Detailed Explanation:
- **removePlayer(user: *User) void**: This function removes a player from the server if they are disconnected. If the player is still connected, it sends a message indicating that the player has left and broadcasts this information to all other connected clients using `main.network.protocols.entity.send`. The function uses a block statement (`blk`) with mutex locking and unlocking around the user list operations.

- **connect(user: *User) void**: Increases the reference count of the user and adds them to the connection list (`userConnectList`).

- **connectInternal(user: *User) void**: Initializes the player, sends server player data via `main.network.protocols.handShake.sendServerPlayerData`, checks for duplicate players in non-testing mode by iterating through the user list, broadcasts new player information to other clients using `main.network.protocols.entity.send`, and sends an initial entity list to the newly connected client.

- **messageFrom(msg: []const u8, source: *User) void**: Sends a formatted message indicating that a user has sent a message. This function uses `sendMessage` internally.

- **sendRawMessage(msg: []const u8) void**: Locks the chat mutex and sends raw messages to all connected clients using `user.sendRawMessage`. It also logs the message in the server's log system.

- **sendMessage(comptime fmt: []const u8, args: anytype) void**: Allocates a formatted string from the provided format and arguments, frees it after use, and sends the message to all connected clients via `sendRawMessage`.

- **getUserByIndexAndIncreaseRefCount(index: usize) ?*User**: Retrieves a user by their player index and increases their reference count. It returns null if no such user is found.

## Code Example
```zig
pub fn removePlayer(user: *User) void { // MARK: removePlayer()
	if (!user.connected.load(.monotonic)) return;

	const foundUser = blk: {
		userMutex.lock();
		defer userMutex.unlock();
		for (users.items, 0..) |other, i| {
			if (other == user) {
				_ = users.swapRemove(i);
				break :blk true;
			}
		}
		break :blk false;
	};
	if (!foundUser) return;

	sendMessage("{s}§#ffff00 left", .{user.name});
	// Let the other clients know about that this new one left.
	const zonArray = main.ZonElement.initArray(main.stackAllocator);
	defer zonArray.deinit(main.stackAllocator);
	zonArray.array.append(.{.int = @intFromEnum(user.id)});
	const data = zonArray.toStringEfficient(main.stackAllocator, &.{});
	defer main.stackAllocator.free(data);
	const userList = getUserListAndIncreaseRefCount(main.stackAllocator);
	defer freeUserListAndDecreaseRefCount(main.stackAllocator, userList);
	for (userList) |other| {
		main.network.protocols.entity.send(other.conn, data);
	}
}
```

## Related Questions
- How does the server handle player disconnection?
- What is the purpose of the `connectInternal` function?
- How are messages broadcast to all connected clients?
- What role does reference counting play in user management?
- How is thread safety ensured when managing user lists?
- What steps are taken to prevent duplicate players from connecting?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_7*
