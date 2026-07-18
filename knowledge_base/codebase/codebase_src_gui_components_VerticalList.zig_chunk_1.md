# [medium/codebase_src_gui_components_VerticalList.zig] - Chunk 1

**Type:** api
**Keywords:** mouse events, GUI components, scrolling, event handling, position adjustment
**Symbols:** VerticalList, VerticalList.mainButtonPressed, VerticalList.mainButtonReleased
**Concepts:** GUI component interaction, scrollbar handling, event propagation

## Summary
Handles mouse button press and release events for a vertical list GUI component, including interaction with child components and optional scrollbar.

## Explanation
The chunk defines two methods for the `VerticalList` struct: `mainButtonPressed` and `mainButtonReleased`. The `mainButtonPressed` method checks if the mouse position is within the bounds of any child component or the scrollbar, adjusting positions based on scrolling state. It returns `.handled` if an interaction is detected, otherwise `.ignored`. The `mainButtonReleased` method similarly processes release events, ensuring that all child components receive the event regardless of whether they were interacted with.

## Code Example
```zig
pub fn mainButtonPressed(self: *VerticalList, mousePosition: Vec2f) main.callbacks.Result {
	var shiftedPos = self.pos;
	if (self.scrollBarEnabled) {
		const diff = self.childrenHeight - self.maxHeight;
		shiftedPos[1] -= diff*self.scrollBar.currentState;
		if (GuiComponent.contains(self.scrollBar.pos, self.scrollBar.size, mousePosition - self.pos)) {
			if (self.scrollBar.mainButtonPressed(mousePosition - self.pos) == .handled) return .handled;
		}
	}
	// reverse order of rendering, the last-rendered element is the first one that we should try to interact with
	var iterator = std.mem.reverseIterator(self.children.items);
	while (iterator.next()) |child| {
		if (GuiComponent.contains(child.pos() + shiftedPos, child.size(), mousePosition)) {
			if (child.mainButtonPressed(mousePosition - shiftedPos) == .handled) return .handled;
		}
	}
	return .ignored;
}
```

## Related Questions
- How does the `mainButtonPressed` method handle interactions with child components?
- What is the purpose of adjusting positions based on scrolling state in the `mainButtonPressed` method?
- How does the `mainButtonReleased` method ensure that all child components receive release events?
- What conditions determine whether an interaction is `.handled` or `.ignored` in the `mainButtonPressed` method?
- How does the chunk handle mouse button press and release events for a vertical list GUI component?
- What role does the scrollbar play in handling mouse interactions within the vertical list?

*Source: unknown | chunk_id: codebase_src_gui_components_VerticalList.zig_chunk_1*
