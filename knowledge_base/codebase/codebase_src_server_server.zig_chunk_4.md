# [hard/codebase_src_server_server.zig] - Chunk 4

**Type:** api
**Keywords:** job queue, mutex locking, binary serialization, inventory commands, network protocols, world saving, time synchronization
**Symbols:** User, User.clearJobQueue, User.isNetworkQueueFull, User.scheduleJobQueue, User.update, User.receiveCommand, User.receiveData, User.sendMessage, User.sendRawMessage, User.hasPermission, User.getSpawnPos, User.format
**Concepts:** user session management, command processing, network communication

## Summary
Handles user session management, command processing, and network communication.

## Explanation
This chunk defines the `User` struct with methods for managing user sessions. The `clearJobQueue` method clears all tasks from the job queue by extracting and cleaning them using their respective vtable functions. The `isNetworkQueueFull` function checks if the network send buffer length exceeds 900,000 bytes. The `scheduleJobQueue` method schedules jobs only when the job queue is not empty, the network queue is not full, and it has not been scheduled yet. It adds the player to the thread pool for processing. The `update` method locks the mutex, calls `scheduleJobQueue`, processes inventory commands, updates interpolation based on time differences, saves the player if necessary, and loads/unloads chunks. The `receiveCommand` method appends received command data to the inventory commands list after locking the mutex. The `receiveData` method reads position, velocity, rotation, and time from a binary reader and updates the user's state accordingly. The `sendMessage` method formats and sends messages using network protocols. The `hasPermission` function checks if a user has a specific permission path. The `getSpawnPos` function returns either the spawn position or the default world spawn position. The `format` function prints user information in the format `{name}@{playerIndex}`.

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
