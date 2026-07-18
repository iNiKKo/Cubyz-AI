# [hard/codebase_src_server_server.zig] - Chunk 4

**Type:** api
**Keywords:** job queue, mutex locking, binary serialization, inventory commands, network protocols, world saving, time synchronization
**Symbols:** User, User.clearJobQueue, User.isNetworkQueueFull, User.scheduleJobQueue, User.update, User.receiveCommand, User.receiveData, User.sendMessage, User.sendRawMessage, User.hasPermission, User.getSpawnPos, User.format
**Concepts:** user session management, command processing, network communication

## Summary
Handles user session management, command processing, and network communication.

## Explanation
This chunk defines the `User` struct with methods for managing user sessions, including clearing job queues, scheduling tasks, updating user state, receiving commands and data, sending messages, checking permissions, getting spawn positions, and formatting user information. It interacts with various components like inventory management, network protocols, world saving, and time synchronization.

## Code Example
```zig
pub fn clearJobQueue(self: *User) void {
	while (self.jobQueue.extractAny()) |task| {
		task.vtable.clean(task.self);
	}
}
```

## Related Questions
- How does the `clearJobQueue` method work?
- What is the purpose of the `isNetworkQueueFull` function?
- How are user commands processed in the `update` method?
- What happens when a user receives data through the `receiveData` method?
- How does the `sendMessage` method format and send messages?
- What role does the `hasPermission` function play in user management?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_4*
