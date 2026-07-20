# [hard/codebase_src_gui_gui.zig] - Chunk 4

**Type:** implementation
**Keywords:** mouse position, GUI commands, window updates, inventory handling, rendering pipeline, gamepad cursor
**Symbols:** updateAndRenderGui, toggleGameMenu
**Concepts:** GUI management, game menu toggling

## Summary
Handles GUI updates, rendering, and game menu toggling.

## Explanation
**Explanation**
The chunk contains two main functions: `updateAndRenderGui` and `toggleGameMenu`. The `updateAndRenderGui` function manages the updating and rendering of the graphical user interface (GUI). It retrieves the mouse position, executes GUI commands, updates selected windows, checks for hovered items, updates inventory, and renders open windows and the gamepad cursor. Specifically, it calculates the mouse position relative to the window scale (`mousePos = main.Window.getMousePosition()/@as(Vec2f, @splat(scale))`), updates the selected window if applicable (`selected.updateSelected(mousePos)`), checks if any window is hovered over by iterating through open windows in reverse order (`var i: usize = openWindows.items.len; while (i != 0) { ... }`), and handles rendering in reverse order of opening. The `toggleGameMenu` function toggles the game menu by grabbing or releasing the mouse, handling inventory interactions, closing windows if the mouse is grabbed, and resetting various states (`main.Window.setMouseGrabbed(!main.Window.grabbed); if (!main.Window.grabbed) { hideGui = false; } else { ... }`).

## Code Example
```zig
pub fn toggleGameMenu() void {
	main.Window.setMouseGrabbed(!main.Window.grabbed);
	if (!main.Window.grabbed) {
		hideGui = false;
	} else { // Take of the currently held item stack and close some windows
		inventory.carried.depositOrDrop(&.{main.game.Player.inventory});
		hoveredItemSlot = null;
		var i: usize = 0;
		while (i < openWindows.items.len) {
			const window = openWindows.items[i];
			if (window.closeIfMouseIsGrabbed) {
				_ = openWindows.swapRemove(i);
				window.onCloseFn();
			} else {
				i += 1;
			}
		}
		reorderWindows = false;
		selectedWindow = null;
	}
}
```

## Related Questions
- What does the `updateAndRenderGui` function do?
- How is the mouse position used in this chunk?
- What happens when a window is hovered over?
- How is the game menu toggled?
- What role does the inventory play in this chunk?
- How are windows rendered in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_4*
