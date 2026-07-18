# [hard/codebase_src_game.zig] - Chunk 3

**Type:** gameplay
**Keywords:** key press handling, block placement, flying toggle, ghost mode, hyper speed, client-server synchronization
**Symbols:** projectionMatrix, nextBlockPlaceTime, nextBlockBreakTime, pressPlace, releasePlace, pressBreak, releaseBreak, pressAcquireSelectedBlock, flyToggle, ghostToggle, hyperSpeedToggle, getBlockWithSide
**Concepts:** player input handling, block interaction, creative mode features

## Summary
Handles player input for block placement, breaking, flying, ghost mode, and hyper speed toggles.

## Explanation
This chunk manages player interactions with the game world through various key presses. It includes functions to handle placing and breaking blocks, toggling flying and ghost modes, and enabling hyper speed. The `getBlockWithSide` function retrieves a block from either the client's render thread or the server's world based on the specified side. Specifically:

- The `projectionMatrix` is initialized as an identity matrix.
- `nextBlockPlaceTime` and `nextBlockBreakTime` are timestamps that track when blocks can be placed or broken again after a delay defined by `main.settings.updateRepeatDelay`.
- The `pressPlace` function sets the next block placement time and calls `Player.placeBlock(mods)` to place a block.
- The `releasePlace` function resets the `nextBlockPlaceTime` to null.
- The `pressBreak` function sets the next block breaking time and calls `Player.breakBlock(0)` to break a block.
- The `releaseBreak` function resets the `nextBlockBreakTime` to null.
- The `flyToggle` function toggles flying mode for creative players, setting `isFlying` and `isGhost` accordingly.
- The `ghostToggle` function toggles ghost mode for creative players, setting both `isGhost` and `isFlying` based on the current state of `isGhost`.
- The `hyperSpeedToggle` function toggles hyper speed for creative players by flipping the value of `Player.hyperSpeed`.

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
