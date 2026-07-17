# [hard/codebase_src_game.zig] - Chunk 4

**Type:** implementation
**Keywords:** input handling, physics calculations, player movement, block placement, mode toggling
**Symbols:** update, pressPlace, releasePlace, pressBreak, releaseBreak, pressAcquireSelectedBlock, flyToggle, ghostToggle, hyperSpeedToggle, getBlockWithSide
**Concepts:** player input handling, game state updates, movement physics, block interactions, player modes

## Summary
Handles player input and updates game state, including movement, block placement, and toggling various player modes.

## Explanation
This chunk contains functions for handling player input such as placing and breaking blocks, flying, ghost mode, hyper speed, and acquiring selected blocks. It also includes an update function that manages player physics, movement calculations, and interactions with the game world. The code updates player position based on input, applies friction, and adjusts movement speed according to player state (flying, crouching, sprinting). It uses various global variables like `world`, `camera`, and `Player` for these operations.

## Code Example
```zig
pub fn pressPlace(mods: main.Window.Key.Modifiers) void {
	const time = main.timestamp();
	nextBlockPlaceTime = time.addDuration(main.settings.updateRepeatDelay);
	Player.placeBlock(mods);
}
```

## Related Questions
- What function handles player block placement?
- How is the player's movement speed adjusted based on input?
- What does the `flyToggle` function do?
- Where is the global `world` variable used in this chunk?
- How are player modes like flying and ghost toggled?
- What is the purpose of the `getBlockWithSide` function?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_4*
