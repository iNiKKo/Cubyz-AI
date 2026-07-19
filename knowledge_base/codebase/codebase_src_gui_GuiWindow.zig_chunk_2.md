# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 2

**Type:** implementation
**Keywords:** window positioning, relative positioning, mouse events, window selection, snap to center
**Symbols:** positionRelativeToFrame, positionRelativeToConnectedWindow, update, updateSelected
**Concepts:** GUI window positioning, mouse interactions, window selection

## Summary
Handles GUI window positioning and selection updates.

## Explanation
The chunk contains functions for updating the position of a GUI window relative to its frame or other windows, as well as handling mouse interactions to update selected windows. The `positionRelativeToFrame` function adjusts the window's position based on its proximity to the center of the main window. If the window is within a certain distance (`snapDistance`) from the center, it snaps to the center with specific attachment points (upper, middle, lower). Otherwise, it calculates a ratio based on the window's position relative to the frame size.

The `positionRelativeToConnectedWindow` function positions the window relative to another connected window. It checks for snapping conditions at the center and edges of the other window. If the window is within `snapDistance` from the center or edges, it snaps with specific attachment points. Otherwise, it calculates a ratio based on the window's position relative to the connected window size.

The `update` function calls a user-defined update function for the window. The `updateSelected` function updates the selected state of the window, including handling mouse-based reordering and snapping to other windows or the frame. It ensures that windows do not move outside the main window's bounds by clamping their positions.

Possible states for `relativePosition` include:
- `.attachedToFrame`: Specifies attachment points relative to the frame (upper, middle, lower).
- `.attachedToWindow`: Specifies attachment points relative to another window (lower-lower, lower-middle, upper-upper).
- `.ratio`: A floating-point ratio representing the position relative to the frame or connected window.

The code ensures that windows do not move outside the main window's bounds by clamping their positions using `@max` and `@min` functions.

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
