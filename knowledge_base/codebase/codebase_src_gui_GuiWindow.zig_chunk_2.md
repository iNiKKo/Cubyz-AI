# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 2

**Type:** implementation
**Keywords:** window positioning, mouse interaction, attachment points, snapping logic, window reordering
**Symbols:** GuiWindow, GuiWindow.relativePosition, GuiWindow.pos, GuiWindow.size, GuiWindow.updateFn, GuiWindow.updateSelectedFn, GuiWindow.snapToOtherWindow, GuiWindow.positionRelativeToFrame, GuiWindow.positionRelativeToConnectedWindow
**Concepts:** GUI window management, window snapping, user interaction handling

## Summary
Handles GUI window positioning and selection updates.

## Explanation
This chunk contains methods for updating GUI windows, including their positions relative to other windows or the frame, as well as handling user interactions like dragging. The `update` method calls a function pointer to perform general updates. The `updateSelected` method manages window reordering and snapping logic based on mouse position and attachment points.

## Code Example
```zig
fn update(self: *GuiWindow) void {
	self.updateFn();
}
```

## Related Questions
- How does the `update` method work in GuiWindow?
- What is the purpose of the `snapToOtherWindow` function?
- How does the `positionRelativeToFrame` method determine window position?
- What conditions trigger window reordering in `updateSelected`?
- How are attachment points used in positioning logic?
- What is the role of the `updateFn` and `updateSelectedFn` pointers?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_2*
