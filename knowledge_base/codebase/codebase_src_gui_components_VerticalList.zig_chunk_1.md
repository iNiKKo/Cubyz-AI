# [medium/codebase_src_gui_components_VerticalList.zig] - Chunk 1

**Type:** implementation
**Keywords:** rendering, scrollbar, visibility, hit testing, translation, viewport, children iteration, mouse position, deferred restore, reverse iterator
**Symbols:** render, mainButtonPressed, mainButtonReleased
**Concepts:** UI rendering, scrollbar handling, viewport culling, reverse-order hit testing, mouse interaction, translation management, clip region restoration

## Summary
Implements rendering and mouse interaction for a scrollable vertical list UI component, including translation/clip management, scrollbar handling, child visibility culling, and reverse-order hit testing.

## Explanation
The render method saves the current draw translation and clip region, computes an adjusted position by subtracting the visible offset from the scrollbar state, then iterates over children in forward order, skipping any whose bounding box lies outside the viewport. The mainButtonPressed method first processes the scrollbar if enabled (returning handled immediately on hit), then reverses the iteration order of children to prioritize topmost elements and calls each child's mainButtonPressed, returning handled on the first match; otherwise returns ignored. The mainButtonReleased method similarly applies the same offset computation, forwards the release event to the scrollbar, then iterates all children in forward order to propagate releases.

## Code Example
```zig
pub fn render(self: *VerticalList, mousePosition: Vec2f) void {
	const oldTranslation = draw.setTranslation(self.pos);
	defer draw.restoreTranslation(oldTranslation);
	const oldClip = draw.setClip(self.size);
	defer draw.restoreClip(oldClip);
	var shiftedPos = self.pos;
	if (self.scrollBarEnabled) {
		const diff = self.childrenHeight - self.maxHeight;
		shiftedPos[1] -= diff*self.scrollBar.currentState;
		self.scrollBar.render(mousePosition - self.pos);
	}
	_ = draw.setTranslation(shiftedPos - self.pos);

	for (self.children.items) |*child| {
		const itemYPos = child.pos()[1];
		const adjustedYPos = itemYPos + shiftedPos[1] - self.pos[1];

		if (adjustedYPos + 2*child.size()[1] < 0 or adjustedYPos - child.size()[1] > self.maxHeight) {
			continue;
		}
		child.render(mousePosition - shiftedPos);
	}
}
```

## Related Questions
- How does the render method handle translation and clip restoration?
- What condition determines whether a child is culled during rendering?
- Why are children iterated in reverse order for mainButtonPressed?
- Does the scrollbar receive mouse events before or after children in mainButtonPressed?
- How is the shifted position computed when the scrollbar is enabled?
- What does returning .handled signify in mainButtonPressed?
- Is mainButtonReleased forwarded to all children regardless of visibility?
- Are any draw API calls exposed outside this file for translation/clip management?
- Does the render method use mousePosition directly or relative coordinates?
- How is the scrollbar's currentState used to offset child positions?

*Source: unknown | chunk_id: codebase_src_gui_components_VerticalList.zig_chunk_1*
