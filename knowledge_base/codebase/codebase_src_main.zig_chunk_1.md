# [hard/codebase_src_main.zig] - Chunk 1

**Type:** api
**Keywords:** callback functions, GUI toggling, inventory management, hotbar slots, debug overlays
**Symbols:** escape, inventory, ungrabMouse, openCreativeInventory, openChat, openCommand, takeBackgroundImageFn, toggleHideGui, toggleHideDisplayItem, toggleDebugOverlay, togglePerformanceOverlay, toggleGPUPerformanceOverlay, toggleNetworkDebugOverlay, toggleAdvancedNetworkDebugOverlay, toggleVulkanDebugOverlay, cycleHotbarSlot, setHotbarSlot
**Concepts:** GUI management, user input handling, inventory system, debug overlays

## Summary
Defines various callback functions for handling user input and GUI interactions in the game.

## Explanation
This chunk contains a series of callback functions that handle different types of user inputs and GUI actions within the game. Each function is responsible for specific tasks such as toggling GUI windows, managing inventory states, adjusting game settings, and handling hotbar slots.

- **escape**: Manages the state of various GUI elements based on user input by setting `gui.selectedTextInput` to null and calling `inventory(mods)`.

- **inventory**: Checks if a world exists before opening the 'inventory' and 'hotbar' windows and toggling the game menu.

- **ungrabMouse**: Releases mouse control when the window is grabbed.

- **openCreativeInventory**: Opens the creative inventory window only in creative mode after ungrabbing the mouse.

- **openChat**: Checks if the chat window is open before opening it and selecting input.

- **openCommand**: Clears the chat input and adds a '/' character for command execution.

- **takeBackgroundImageFn**: Temporarily hides GUI elements and disables item display to take a background image.

- **toggleHideGui**: Toggles the visibility of the GUI (`gui.hideGui = !gui.hideGui`).

- **toggleHideDisplayItem**: Toggles the visibility of item display (`itemdrop.ItemDisplayManager.showItem = !itemdrop.ItemDisplayManager.showItem`).

- **toggleDebugOverlay**: Toggles the debug window (`gui.toggleWindow("debug")`).

- **togglePerformanceOverlay**: Toggles the performance graph window (`gui.toggleWindow("performance_graph")`).

- **toggleGPUPerformanceOverlay**: Toggles the GPU performance measuring window (`gui.toggleWindow("gpu_performance_measuring")`).

- **toggleNetworkDebugOverlay**: Toggles the network debug window (`gui.toggleWindow("debug_network")`).

- **toggleAdvancedNetworkDebugOverlay**: Toggles the advanced network debug window (`gui.toggleWindow("debug_network_advanced")`).

- **toggleVulkanDebugOverlay**: Toggles the Vulkan info debug window (`gui.toggleWindow("debug_vulkan_info")`).

- **cycleHotbarSlot(i: comptime_int)**: Cycles through 12 hotbar slots using modulo arithmetic to wrap around. The function returns a pointer to an anonymous struct with a `set` method that updates `game.Player.selectedSlot`.

- **setHotbarSlot(i: comptime_int)**: Sets a specific hotbar slot based on the input parameter `i`. The function returns a pointer to an anonymous struct with a `set` method that updates `game.Player.selectedSlot` to `i - 1`.

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
