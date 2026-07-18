# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 2

**Type:** implementation
**Keywords:** window positioning, relative positioning, mouse events, window selection, snap to center
**Symbols:** positionRelativeToFrame, positionRelativeToConnectedWindow, update, updateSelected
**Concepts:** GUI window positioning, mouse interactions, window selection

## Summary
Handles GUI window positioning and selection updates.

## Explanation
The chunk contains functions for updating the position of a GUI window relative to its frame or other windows, as well as handling mouse interactions to update selected windows. The `positionRelativeToFrame` function adjusts the window's position based on its proximity to the center of the main window. The `positionRelativeToConnectedWindow` function positions the window relative to another connected window. The `update` function calls a user-defined update function for the window. The `updateSelected` function updates the selected state of the window, including handling mouse-based reordering and snapping to other windows or the frame.

## Code Example
```zig
fn update(self: *GuiWindow) void {
	self.updateFn();
}
```

## Related Questions
- How does the `positionRelativeToFrame` function determine the window's position?
- What conditions trigger the snapping behavior in `positionRelativeToConnectedWindow`?
- What is the purpose of the `update` function in this chunk?
- How does the `updateSelected` function handle mouse-based reordering?
- What are the possible states for `relativePosition` in these functions?
- How does the code ensure that windows do not move outside the main window's bounds?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_2*
