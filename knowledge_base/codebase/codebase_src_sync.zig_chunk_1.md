# [hard/codebase_src_sync.zig] - Chunk 1

**Type:** api
**Keywords:** thread context, command payload, network protocols, inventory sync, gamemodes
**Symbols:** server, server.init, server.deinit, server.executeCommand, server.executeUserCommand, server.receiveCommand, server.setGamemode, addHealth
**Concepts:** command execution, user management, health system

## Summary
Handles server-side command execution and user management.

## Explanation
This chunk defines the `server` struct with methods for initializing (`init`), deinitializing (`deinit`), executing commands (`executeCommand`), handling user commands (`executeUserCommand`), receiving commands (`receiveCommand`), and setting gamemodes (`setGamemode`). The `addHealth` function is also included to add health to an entity, which can be executed on either the client or server side based on the provided context.

The `init` method sets the thread context to `.server`. The `deinit` method asserts that the current thread context is `.server` and then resets it to `.other`. The `executeCommand` function initializes a command with the given payload, executes it, and handles any errors by sending a failure message over the network. It also sends confirmation data and synchronization operations to relevant users. If the command payload is of type `.open`, it sends initial items to the user's inventory.

The `executeUserCommand` function reads the command type from the binary reader, deserializes the payload based on the type, and then calls `executeCommand`. The `receiveCommand` method passes the remaining data from the reader to the user's command handling method. The `setGamemode` function updates the user's gamemode and sends a gamemode update over the network.

The `addHealth` function asserts the correct thread context, checks if the side is `.client`, and then executes the command on either the client or server side.

## Code Example
```zig
pub fn init() void {
	threadContext = .server;
}
```

## Related Questions
- What is the purpose of the `init` method in the server struct?
- How does the `executeCommand` function handle errors?
- What does the `setGamemode` function do?
- How are commands received and processed by the server?
- What is the role of the `addHealth` function?
- How is thread context managed within the server module?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_1*
