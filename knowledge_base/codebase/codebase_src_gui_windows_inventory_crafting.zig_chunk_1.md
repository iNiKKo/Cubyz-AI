# [medium/codebase_src_gui_windows_inventory_crafting.zig] - Chunk 1

**Type:** implementation
**Keywords:** window lifecycle, resource allocation, scroll state preservation, label rendering, dynamic content update
**Symbols:** refresh, onOpen, onClose, update
**Concepts:** inventory management, crafting recipes display

## Summary
Handles the inventory crafting window's lifecycle and refreshes its content based on available recipes.

## Explanation
The chunk manages the inventory crafting window, including initializing resources when opening, refreshing the list of craftable recipes, and cleaning up resources when closing. The `refresh` function updates the vertical list with available recipes, handling scroll state preservation and adding a label if no recipes are found. The `onOpen` initializes allocators for items and inventories, while `onClose` deinitializes them. The `update` function simply calls `refresh` to keep the window content up-to-date.

## Code Example
```zig
fn refresh() void {
	const oldScrollState = if (window.rootComponent) |oldList| oldList.verticalList.scrollBar.currentState else 0;
	const list = VerticalList.init(.{padding, padding + 16}, 300, 8);
	const recipesChanged = findAvailableRecipes(list);
	if (!recipesChanged and window.rootComponent != null) {
		list.deinit();
		return;
	}
	if (window.rootComponent) |*comp| {
		main.heap.GarbageCollection.deferredFree(.{.ptr = comp.verticalList, .freeFunction = main.meta.castFunctionSelfToAnyopaque(VerticalList.deinit)});
	}
	if (list.children.items.len == 0) {
		list.add(Label.init(.{0, 0}, 120, "No craftable\nrecipes found", .center));
	}
	list.finish(.center);
	list.scrollBar.currentState = oldScrollState;
	window.rootComponent = list.toComponent();
	window.contentSize = window.rootComponent.?.pos() + window.rootComponent.?.size() + @as(Vec2f, @splat(padding));
	window.contentSize[0] = @max(window.contentSize[0], window.getMinWindowWidth());
	gui.updateWindowPositions();
}
```

## Related Questions
- What does the `refresh` function do?
- How is scroll state preserved during a refresh?
- What happens if no recipes are found during a refresh?
- What resources are initialized when the crafting window opens?
- How are resources cleaned up when the crafting window closes?
- What triggers an update of the crafting window content?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory_crafting.zig_chunk_1*
