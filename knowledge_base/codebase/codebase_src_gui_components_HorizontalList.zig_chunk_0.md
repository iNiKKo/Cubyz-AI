# [easy/codebase_src_gui_components_HorizontalList.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiComponent, ListManaged, horizontal layout, reverse iteration, position offsetting, alignment centering, mouse containment, draw translation, globalAllocator, deinit cascade
**Symbols:** HorizontalList, HorizontalList.pos, HorizontalList.size, HorizontalList.children, HorizontalList.init, HorizontalList.deinit, HorizontalList.toComponent, HorizontalList.add, HorizontalList.finish, HorizontalList.updateSelected, HorizontalList.updateHovered, HorizontalList.render, HorizontalList.mainButtonPressed, HorizontalList.mainButtonReleased
**Concepts:** GuiComponent composition, horizontal layout management, reverse-order mouse hit testing, position offsetting for scrolling, alignment-based Y positioning, memory ownership via ListManaged, global allocator usage

## Summary
Implements the HorizontalList GuiComponent for managing a horizontally scrollable list of child components, handling initialization, deinitialization, adding children with automatic size calculation, finishing layout with alignment options (left/center/right), and processing mouse interactions via reverse-order iteration.

## Explanation
The chunk defines the HorizontalList struct with fields pos, size, and children (a ListManaged of GuiComponent). It provides init() which allocates a new instance and initializes its children list. deinit() iterates over all child items calling their deinit(), then frees the children container and destroys the HorizontalList itself from main.globalAllocator. toComponent() wraps the struct into a GuiComponent variant. add() accepts anytype, casts or converts it to GuiComponent via toComponent if needed, updates its position by offsetting along X (self.size[0]) to maintain horizontal layout, expands self.size[0] and self.size[1] using @max with child dimensions, then appends the component to children. finish() sets final pos, shrinks and frees all allocated children items, then iterates over them adjusting their Y position according to alignment: left leaves unchanged, center computes mutPos.*[1]/2 + self.size[1]/2 - size[1]/2, right computes self.size[1] - size[1]. updateSelected() forwards the call to each child. updateHovered() iterates children in reverse order (using a manual index decrement loop), checks containment via GuiComponent.contains(child.pos() + self.pos, child.size(), mousePosition), and if contained delegates to child.updateHovered(mousePosition - self.pos); returns .handled on first handled result or .ignored otherwise. render() saves draw translation at self.pos, iterates children in order rendering each with mousePosition - self.pos offset, then restores translation. mainButtonPressed() uses std.mem.reverseIterator over children.items, checks containment similarly to updateHovered, delegates to child.mainButtonPressed(mousePosition - self.pos), and returns .handled on first handled or .ignored. mainButtonReleased() iterates children in order delegating to child.mainButtonReleased(mousePosition - self.pos).

## Code Example
```zig
pub fn finish(self: *HorizontalList, pos: Vec2f, alignment: graphics.TextBuffer.Alignment) void {
	self.pos = pos;
	self.children.shrinkAndFree(self.children.items.len);
	for (self.children.items) |_child| {
		const child: GuiComponent = _child;
		const mutPos = child.mutPos();
		const size = child.size();
		switch (alignment) {
			.left => {},
			.center => {
				mutPos.*[1] = mutPos.*[1]/2 + self.size[1]/2 - size[1]/2;
			},
			.right => {
				mutPos.*[1] = self.size[1] - size[1];
			},
		}
	}
}
```

## Related Questions
- How does HorizontalList handle adding a component that is not already a GuiComponent?
- What happens to the children list when finish() is called with any alignment option?
- Why does updateHovered and mainButtonPressed iterate over children in reverse order?
- How are child positions adjusted after finish() runs, specifically for center alignment?
- Does HorizontalList store its own position or rely on parent translation?
- What memory deallocation steps occur during deinit() beyond freeing the children container?
- Can a child component be added before finish() is called and still render correctly?
- How does the chunk ensure that mouse coordinates are transformed relative to self.pos when delegating to children?
- Is there any validation performed on pos or size arguments in add() or finish()?
- What type of allocator is used for HorizontalList instances and why?

*Source: unknown | chunk_id: codebase_src_gui_components_HorizontalList.zig_chunk_0*
