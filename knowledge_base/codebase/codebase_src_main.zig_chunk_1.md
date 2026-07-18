# [hard/codebase_src_main.zig] - Chunk 1

**Type:** api
**Keywords:** callback functions, GUI toggling, inventory management, hotbar slots, debug overlays
**Symbols:** escape, inventory, ungrabMouse, openCreativeInventory, openChat, openCommand, takeBackgroundImageFn, toggleHideGui, toggleHideDisplayItem, toggleDebugOverlay, togglePerformanceOverlay, toggleGPUPerformanceOverlay, toggleNetworkDebugOverlay, toggleAdvancedNetworkDebugOverlay, toggleVulkanDebugOverlay, cycleHotbarSlot, setHotbarSlot
**Concepts:** GUI management, user input handling, inventory system, debug overlays

## Summary
Defines various callback functions for handling user input and GUI interactions in the game.

## Explanation
This chunk contains a series of callback functions that handle different types of user inputs and GUI actions within the game. Each function is responsible for specific tasks such as toggling GUI windows, managing inventory states, and adjusting game settings. Functions like `escape`, `inventory`, and `ungrabMouse` manage the state of various GUI elements based on user input. Others, such as `openCreativeInventory` and `toggleDebugOverlay`, provide additional functionality by opening specific windows or toggling debug overlays. The chunk also includes functions for cycling through hotbar slots (`cycleHotbarSlot`) and setting a specific hotbar slot (`setHotbarSlot`). These callbacks are likely connected to user input events, such as key presses, to trigger the appropriate actions within the game.

## Code Example
```zig
fn toggleHideGui(_: Window.Key.Modifiers) void {
	gui.hideGui = !gui.hideGui;
}
```

## Related Questions
- What is the purpose of the `escape` function?
- How does the `openCreativeInventory` function check if the player is in creative mode?
- What action does the `toggleHideGui` function perform?
- How are hotbar slots cycled through using the functions defined in this chunk?
- What specific debug overlays can be toggled using the functions in this chunk?
- How does the `takeBackgroundImageFn` function temporarily modify GUI and item display settings?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_1*
