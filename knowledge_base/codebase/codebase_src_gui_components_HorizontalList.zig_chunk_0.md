# [easy/codebase_src_gui_components_HorizontalList.zig] - Chunk 0

**Type:** implementation
**Keywords:** memory allocation, list management, positioning, hover detection, button interaction, render loop
**Symbols:** HorizontalList, HorizontalList.pos, HorizontalList.size, HorizontalList.children, HorizontalList.init, HorizontalList.deinit, HorizontalList.toComponent, HorizontalList.add, HorizontalList.finish, HorizontalList.updateSelected, HorizontalList.updateHovered, HorizontalList.render, HorizontalList.mainButtonPressed, HorizontalList.mainButtonReleased
**Concepts:** GUI component management, horizontal layout, event handling, rendering pipeline

## Summary
The HorizontalList component manages a horizontal layout of GUI components, handling initialization, deinitialization, adding children, finishing layout, updating selection and hover states, rendering, and button interactions.

## Explanation
This chunk defines the HorizontalList struct, which is responsible for managing a collection of GUI components arranged horizontally. It includes methods for initializing and deinitializing the list, adding child components, finalizing the layout with position and alignment, updating selection and hover states, rendering the list, and handling button press events. The component uses global memory allocation and maintains a list of child GuiComponent instances. It ensures that child components are properly positioned and interacted with based on their order in the list.

## Code Example
```zig
pub fn init() *HorizontalList {
	const self = main.globalAllocator.create(HorizontalList);
	self.* = HorizontalList{
		.children = .init(main.globalAllocator),
		.pos = .{0, 0},
		.size = .{0, 0},
	};
	return self;
}
```

## Related Questions
- How does the HorizontalList initialize its children?
- What is the purpose of the `finish` method in HorizontalList?
- How does HorizontalList handle mouse hover events?
- What memory allocation strategy does HorizontalList use?
- How are child components positioned within a HorizontalList?
- What happens when a button is pressed on a HorizontalList?

*Source: unknown | chunk_id: codebase_src_gui_components_HorizontalList.zig_chunk_0*
