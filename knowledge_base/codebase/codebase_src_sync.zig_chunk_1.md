# [hard/codebase_src_sync.zig] - Chunk 1

**Type:** api
**Keywords:** thread context, command payload, network protocols, inventory sync, gamemodes
**Symbols:** server, server.init, server.deinit, server.executeCommand, server.executeUserCommand, server.receiveCommand, server.setGamemode, addHealth
**Concepts:** command execution, user management, health system

## Summary
Handles server-side command execution and user management.

## Explanation
This chunk defines the `server` struct with methods for initializing, deinitializing, executing commands, handling user commands, receiving commands, and setting gamemodes. It also includes a function to add health to an entity, which can be executed on either the client or server side based on the provided context.

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
