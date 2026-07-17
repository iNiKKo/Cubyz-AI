# [hard/codebase_src_game.zig] - Chunk 1

**Type:** api
**Keywords:** mutex locking, thread safety, gamemode, inventory, block placement, network connection
**Symbols:** setPosBlocking, getPosBlocking, getVelBlocking, getEyePosBlocking, getEyeVelBlocking, getEyeCoyoteBlocking, getJumpCoyoteBlocking, setGamemode, isCreative, isActuallyFlying, steppingHeight, placeBlock, kill, dropFromHand, breakBlock, acquireSelectedBlock, World, World.conn, World.manager, World.name
**Concepts:** player state management, inventory interactions, gamemode handling, block placement, world interaction

## Summary
This chunk defines player-related functions and properties, including position, velocity, gamemode management, block placement, and inventory interactions.

## Explanation
The chunk contains several public functions that manage the player's state in a game. Functions like `setPosBlocking` and `getPosBlocking` handle thread-safe updates and retrievals of the player's position using a mutex for synchronization. Other functions such as `setGamemode`, `isCreative`, and `isActuallyFlying` manage the player's gamemode and flying status, respectively. The chunk also includes methods for placing blocks (`placeBlock`), killing the player (`kill`), dropping items from the inventory (`dropFromHand`), breaking blocks (`breakBlock`), and acquiring selected blocks (`acquireSelectedBlock`). These functions interact with various components like the renderer, inventory system, and network connection manager. The `World` struct at the end of the chunk defines a world entity with a connection, manager, and name.

## Code Example
```zig
pub fn isCreative() bool {
	return gamemode.load(.monotonic) == .creative;
}
```

## Related Questions
- How does the `setPosBlocking` function ensure thread safety?
- What is the purpose of the `steppingHeight` function in the player logic?
- How does the `placeBlock` function interact with the inventory system?
- What conditions trigger the `kill` function to reset the player's state?
- How does the `acquireSelectedBlock` function handle item acquisition in creative mode?
- What is the role of the `World` struct in this chunk?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_1*
