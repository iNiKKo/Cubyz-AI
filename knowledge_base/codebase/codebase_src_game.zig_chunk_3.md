# [hard/codebase_src_game.zig] - Chunk 3

**Type:** gameplay
**Keywords:** key press handling, block placement, flying toggle, ghost mode, hyper speed, client-server synchronization
**Symbols:** projectionMatrix, nextBlockPlaceTime, nextBlockBreakTime, pressPlace, releasePlace, pressBreak, releaseBreak, pressAcquireSelectedBlock, flyToggle, ghostToggle, hyperSpeedToggle, getBlockWithSide
**Concepts:** player input handling, block interaction, creative mode features

## Summary
Handles player input for block placement, breaking, flying, ghost mode, and hyper speed toggles.

## Explanation
This chunk manages player interactions with the game world through various key presses. It includes functions to handle placing and breaking blocks, toggling flying and ghost modes, and enabling hyper speed. The `getBlockWithSide` function retrieves a block from either the client's render thread or the server's world based on the specified side.

## Code Example
```zig
pub fn releasePlace(_: main.Window.Key.Modifiers) void {
	nextBlockPlaceTime = null;
}
```

## Related Questions
- What is the purpose of the `pressPlace` function?
- How does the `getBlockWithSide` function determine which block to return?
- What conditions must be met for the `flyToggle` function to execute?
- What happens when the player releases the break key?
- How is the `nextBlockBreakTime` variable used in the game logic?
- What are the effects of toggling hyper speed on the player?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_3*
