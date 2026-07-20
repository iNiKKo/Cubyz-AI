# [hard/codebase_src_sync.zig] - Chunk 0

**Type:** api
**Keywords:** mutex locking, command queue, binary serialization, network communication, gamemode change
**Symbols:** Side, client, client.mutex, client.commands, client.init, client.deinit, client.reset, client.executeCommand, client.receiveConfirmation, client.receiveFailure, client.receiveSyncOperation, client.setGamemode
**Concepts:** inventory management, network synchronization, thread safety

## Summary
Handles client-side inventory command execution and synchronization.

## Explanation
This chunk manages the client-side logic for executing inventory commands, handling confirmations, failures, and synchronization operations. It uses a mutex to ensure thread safety when accessing shared resources like the command queue. The `executeCommand` function serializes and sends commands over the network using `BinaryWriter`, while `receiveConfirmation` and `receiveFailure` handle responses from the server. The `setGamemode` function updates the player's gamemode and re-executes pending commands accordingly. The command queue is initialized with a capacity of 256 commands, and each command is serialized into binary data before being sent over the network.

The `client.mutex` variable ensures thread safety when accessing shared resources like the command queue. The `executeCommand` function serializes the payload using `BinaryWriter`, then sends it over the network using `main.network.protocols.inventory.sendCommand`. In the `receiveFailure` function, rejected commands are undone and re-executed if possible. Thread safety is ensured by locking the mutex before accessing or modifying shared resources like the command queue. The `setGamemode` function updates the player's gamemode and re-executes pending commands to reflect the new gamemode.

## Code Example
```zig
pub fn init() void {
	commands = utils.CircularBufferQueue(Command).init(main.globalAllocator, 256);
}
```

## Related Questions
- What is the purpose of the `client.mutex` variable?
- How does the `executeCommand` function handle command execution?
- What steps are taken in the `receiveFailure` function to handle rejected commands?
- How is thread safety ensured when managing the command queue?
- What role does the `setGamemode` function play in client-side logic?
- How are inventory commands serialized and sent over the network?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_0*
