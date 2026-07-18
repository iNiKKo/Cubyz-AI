# [medium/codebase_src_gui_components_VerticalList.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, vertical list, layout management, scrollbar, hover interaction
**Symbols:** VerticalList, VerticalList.pos, VerticalList.size, VerticalList.children, VerticalList.padding, VerticalList.maxHeight, VerticalList.childrenHeight, VerticalList.scrollBar, VerticalList.scrollBarEnabled, init, deinit, toComponent, add, finish, updateSelected, updateHovered, render
**Concepts:** GUI component management, vertical layout, scrolling, interaction handling

## Summary
The VerticalList component manages a list of GUI components vertically, handling layout, scrolling, and interaction.

## Explanation
The VerticalList struct is responsible for managing a vertical arrangement of GUI components. It includes methods to initialize and deinitialize the list, add components, finalize the layout, update selection and hover states, and render the components. The component handles scrolling if the total height exceeds the maximum allowed height, using a scrollbar for navigation. Specific details include:

- **Initialization**: Initializes with `pos`, `maxHeight`, and `padding` parameters. It sets up a scrollbar with width of 10 units and calculates its size based on `maxHeight - 2*border`. The initial position is set to `pos`, the size is initialized as `{0, 0}`, padding is set to the provided value, and maxHeight is set accordingly.

- **Deinitialization**: Frees all child components and deinitializes the scrollbar before destroying itself.

- **Adding Components**: Adds a component by adjusting its position based on existing children's positions and sizes. It updates the total size of the list to accommodate new additions.

- **Finalizing Layout**: Adjusts the layout according to alignment (left, center, right). If the total height exceeds `maxHeight`, it enables scrolling with a scrollbar positioned at `{self.size[0] + border, border}` and adjusts the width accordingly.

- **Updating Hover State**: Iterates through child components in reverse order to handle hover interactions. It also updates the scrollbar's state if enabled.

- **Rendering Components**: Renders each component within its bounds, adjusting for scrolling if necessary.

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
- What are the dimensions and parameters used during initialization of VerticalList?
- How does deinitialization free resources associated with VerticalList?
- Describe the process of adding a new component to VerticalList.
- Under what conditions is the scrollbar enabled, and how is its position calculated?
- Explain the logic for updating hover states in VerticalList.

*Source: unknown | chunk_id: codebase_src_gui_components_VerticalList.zig_chunk_0*
