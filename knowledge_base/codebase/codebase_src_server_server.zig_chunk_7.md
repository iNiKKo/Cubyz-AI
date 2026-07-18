# [hard/codebase_src_server_server.zig] - Chunk 7

**Type:** api
**Keywords:** mutex locking, network protocols, message broadcasting, user list management, reference counting
**Symbols:** removePlayer, connect, connectInternal, messageFrom, sendRawMessage, sendMessage, getUserByIndexAndIncreaseRefCount, chatMutex
**Concepts:** player management, network communication, thread safety, reference counting

## Summary
Handles player connection, disconnection, and messaging in the server.

## Explanation
This chunk contains functions to manage player connections and communications within a server environment. It includes methods for removing a player (`removePlayer`), connecting a player (`connect`, `connectInternal`), handling incoming messages from players (`messageFrom`), sending raw messages (`sendRawMessage`), sending formatted messages (`sendMessage`), and retrieving users by index with reference counting (`getUserByIndexAndIncreaseRefCount`). The chunk uses mutexes for thread safety, particularly around user lists. It also interacts with network protocols to send player data and updates to other clients.

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
