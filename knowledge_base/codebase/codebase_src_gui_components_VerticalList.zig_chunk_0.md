# [medium/codebase_src_gui_components_VerticalList.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, vertical list, layout management, scrollbar, hover interaction
**Symbols:** VerticalList, VerticalList.pos, VerticalList.size, VerticalList.children, VerticalList.padding, VerticalList.maxHeight, VerticalList.childrenHeight, VerticalList.scrollBar, VerticalList.scrollBarEnabled, init, deinit, toComponent, add, finish, updateSelected, updateHovered, render
**Concepts:** GUI component management, vertical layout, scrolling, interaction handling

## Summary
The VerticalList component manages a list of GUI components vertically, handling layout, scrolling, and interaction.

## Explanation
The VerticalList struct is responsible for managing a vertical arrangement of GUI components. It includes methods to initialize and deinitialize the list, add components, finalize the layout, update selection and hover states, and render the components. The component handles scrolling if the total height exceeds the maximum allowed height, using a scrollbar for navigation.

## Code Example
```zig
pub fn init(pos: Vec2f, maxHeight: f32, padding: f32) *VerticalList {
	const scrollBar = ScrollBar.init(undefined, scrollBarWidth, maxHeight - 2*border, 0);
	const self = main.globalAllocator.create(VerticalList);
	self.* = VerticalList{
		.children = .init(main.globalAllocator),
		.pos = pos,
		.size = .{0, 0},
		.padding = padding,
		.maxHeight = maxHeight,
		.scrollBar = scrollBar,
	};
	return self;
}
```

## Related Questions
- How does the VerticalList initialize its scrollbar?
- What is the purpose of the `finish` method in VerticalList?
- How does the VerticalList handle component addition?
- What conditions trigger the scrollbar to be enabled?
- How does the VerticalList update the hover state of its components?
- What role does the padding parameter play in the layout of VerticalList?

*Source: unknown | chunk_id: codebase_src_gui_components_VerticalList.zig_chunk_0*
