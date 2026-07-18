# [easy/codebase_src_gui_components_HorizontalList.zig] - Chunk 0

**Type:** implementation
**Keywords:** memory allocation, list management, positioning, hover detection, button interaction, render loop
**Symbols:** HorizontalList, HorizontalList.pos, HorizontalList.size, HorizontalList.children, HorizontalList.init, HorizontalList.deinit, HorizontalList.toComponent, HorizontalList.add, HorizontalList.finish, HorizontalList.updateSelected, HorizontalList.updateHovered, HorizontalList.render, HorizontalList.mainButtonPressed, HorizontalList.mainButtonReleased
**Concepts:** GUI component management, horizontal layout, event handling, rendering pipeline

## Summary
The HorizontalList component manages a horizontal layout of GUI components, handling initialization, deinitialization, adding children, finishing layout, updating selection and hover states, rendering, and button interactions.

## Explanation
This chunk defines the HorizontalList struct, which is responsible for managing a collection of GUI components arranged horizontally. It includes methods for initializing and deinitializing the list, adding child components, finalizing the layout with position and alignment, updating selection and hover states, rendering the list, and handling button press events. The component uses global memory allocation via `main.globalAllocator` and maintains a list of child GuiComponent instances using `ListManaged`. It ensures that child components are properly positioned based on their order in the list and handles mouse interactions accordingly.

- **Initialization (`init`)**: Allocates memory for a new HorizontalList instance, initializes its children with an empty ListManaged initialized via global allocator, sets initial position to (0, 0) and size to (0, 0).
- **Deinitialization (`deinit`)**: Frees all child components and the list itself.
- **Adding Children (`add`)**: Adds a new GuiComponent to the children list. Adjusts the HorizontalList's width based on the added component's position and size. Updates the overall size of the HorizontalList accordingly.
- **Finalizing Layout (`finish`)**: Sets the final position for the HorizontalList, aligns child components vertically according to specified alignment (left, center, right), and shrinks the children list to fit only necessary elements.
- **Updating Selection (`updateSelected`)**: Iterates through all child components and updates their selection state.
- **Handling Hover Events (`updateHovered`)**: Checks if a mouse position intersects with any child component's bounding box. If so, it calls `updateHovered` on the intersecting component to handle hover events.
- **Rendering (`render`)**: Sets translation for rendering based on HorizontalList's position, iterates through all children and renders them in order, then restores original translation state.
- **Button Press Handling (`mainButtonPressed`)**: Iterates through child components in reverse order (last rendered first) to handle button press events. Returns `.handled` if any component handles the event.
- **Button Release Handling (`mainButtonReleased`)**: Calls `mainButtonReleased` on all child components.

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
