# [hard/codebase_src_sync.zig] - Chunk 0

**Type:** implementation
**Keywords:** circular buffer queue, mutex locking, binary reader writer, command undo redo, thread context assertion, inventory sync operation, gamemode switching, serialize payload, network send command
**Symbols:** Side, client, server, mutex, commands, init, deinit, reset, executeCommand, receiveConfirmation, receiveFailure, receiveSyncOperation, setGamemode
**Concepts:** inventory command handling, client-server synchronization, undo/redo state management, mutex-protected queues, binary serialization, gamemode switching, thread context assertions, network protocol messaging

## Summary
This chunk defines the client-side and server-side state structures for inventory command handling, including initialization, deinitialization, mutex-protected execution of commands, serialization/deserialization via BinaryReader/BinaryWriter, undo/redo logic on failure or sync operations, gamemode switching with command replay, and thread-context assertions.

## Explanation
The chunk declares a Side enum (client/server) and two top-level structs: client and server. The client struct contains a pub var mutex initialized to an empty Mutex, a CircularBufferQueue of Command (initialized in init() using main.globalAllocator with capacity 256), and several public functions. init() sets commands to the allocated queue; deinit() calls reset() then commands.deinit(); reset() locks the mutex, iterates popping front from commands, finalizes each command into a BinaryReader (catching errors and logging via std.log.err), unlocks after loop. executeCommand(payload) constructs a Command with the payload, locks mutex, defers unlock, calls cmd.do(...) passing .client and main.game.Player.gamemode.raw (catch unreachable), serializes the payload using cmd.serializePayload(main.stackAllocator), frees that data, then sends via main.network.protocols.inventory.sendCommand to main.game.world.?.conn, and pushes the command back onto the queue. receiveConfirmation(reader) locks mutex, pops front from commands, finalizes into reader; if pop returns null it panics (no explicit error handling shown). receiveFailure() locks mutex, defers unlock, creates an empty List(Command) tempData, defers its deinit, then while popping back from commands undoes each command and appends to tempData. If tempData.popOrNull() yields a command, it finalizes that command into a fresh BinaryReader (logging error on failure). Then it replays all items in tempData by calling cmd.do(...) with .client and the current gamemode.raw, pushing back onto commands. receiveSyncOperation(reader) mirrors the undo/replay pattern but executes Command.SyncOperation.executeFromData(reader) to apply server-side sync data before replaying undone commands. setGamemode(gamemode) locks mutex, defers unlock, calls main.game.Player.setGamemode(gamemode), then undoes all pending commands (popBack loop into tempData), and replays them with the new gamemode. The server struct contains init() which sets threadContext to .server, deinit() which asserts threadContext is still .server before resetting it to .other, and executeCommand(payload, source) which constructs a Command, calls cmd.do(...) passing .server and either source.gamemode.raw or .creative if source is null (catching errors), sending failures via main.network.protocols.inventory.sendFailure on error. The chunk also re-exports several types from other modules: Block, Neighbor, Gamemode, NeverFailingAllocator, Inventory, InventoryId, InventoryAndSlot, Item, ItemStack, utils (BinaryReader/BinaryWriter), vec (Vec3d/Vec3f/Vec3i), ZonElement, and the entity component @

## Related Questions
- What is the capacity of the client-side command queue and how is it allocated?
- How does reset() handle remaining commands after deinit? What error logging occurs?
- In executeCommand, what happens if cmd.do fails with an error versus unreachable?
- Describe the exact sequence of operations in receiveFailure when a server sends failure.
- What data is passed to main.network.protocols.inventory.sendCommand and why is world.?.conn used?
- How does setGamemode replay commands after changing the gamemode? Does it preserve payload?
- In receiveSyncOperation, what role does Command.SyncOperation.executeFromData play before replaying undone commands?
- What threadContext values are valid for client versus server and how is assertion enforced in deinit?
- Are any of the public functions in this chunk async or blocking? How do they interact with the main event loop?
- How does the chunk ensure memory safety when finalizing commands into BinaryReader (catch vs panic)?
- What happens to a command that is popped from the front during reset but never finalized successfully?
- Does executeCommand push the command back onto the queue after sending it, and why?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_0*
