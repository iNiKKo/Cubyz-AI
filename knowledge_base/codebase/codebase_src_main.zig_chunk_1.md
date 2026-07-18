# [hard/codebase_src_main.zig] - Chunk 1

**Type:** api
**Keywords:** callback functions, GUI toggling, inventory management, hotbar slots, debug overlays
**Symbols:** escape, inventory, ungrabMouse, openCreativeInventory, openChat, openCommand, takeBackgroundImageFn, toggleHideGui, toggleHideDisplayItem, toggleDebugOverlay, togglePerformanceOverlay, toggleGPUPerformanceOverlay, toggleNetworkDebugOverlay, toggleAdvancedNetworkDebugOverlay, toggleVulkanDebugOverlay, cycleHotbarSlot, setHotbarSlot
**Concepts:** GUI management, user input handling, inventory system, debug overlays

## Summary
Defines various callback functions for handling user input and GUI interactions in the game.

## Explanation
This chunk contains a series of callback functions that handle different types of user inputs and GUI actions within the game. Each function is responsible for specific tasks such as toggling GUI windows, managing inventory states, adjusting game settings, and handling hotbar slots. Functions like `escape` manage the state of various GUI elements based on user input by setting `gui.selectedTextInput` to null and calling `inventory(mods)`. The `inventory` function checks if a world exists before opening the 'inventory' and 'hotbar' windows and toggling the game menu. The `ungrabMouse` function releases mouse control when the window is grabbed, while `openCreativeInventory` opens the creative inventory window only in creative mode after ungrabbing the mouse. The `openChat` function checks if the chat window is open before opening it and selecting input, and `openCommand` clears the chat input and adds a '/' character for command execution. The `takeBackgroundImageFn` temporarily hides GUI elements and disables item display to take a background image. Functions like `toggleHideGui`, `toggleHideDisplayItem`, and various debug overlay toggles (`toggleDebugOverlay`, `togglePerformanceOverlay`, etc.) manage the visibility of specific windows or settings. Hotbar slots are managed by `cycleHotbarSlot` which cycles through 12 hotbar slots, and `setHotbarSlot` sets a specific slot based on an input parameter.

## Code Example
```zig
fn toggleHideGui(_: Window.Key.Modifiers) void {
	gui.hideGui = !gui.hideGui;
}
```

## Related Questions
- What is the purpose of the escape function?
- How does the inventory function check if a world exists before opening windows?
- What action does the ungrabMouse function perform when the window is grabbed?
- How does the openCreativeInventory function ensure it only opens in creative mode?
- What specific debug overlays can be toggled using the functions in this chunk?
- How are hotbar slots cycled through and set to a specific slot?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_1*
