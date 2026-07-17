# [medium/codebase_src_gui_windows_inventory_crafting.zig] - Chunk 1

**Type:** implementation
**Keywords:** VerticalList, rootComponent, deinit, scrollBar, findAvailableRecipes, globalAllocator, toComponent, updateWindowPositions, padding, craftingResult
**Symbols:** onOpen, onClose, update, refresh
**Concepts:** inventory crafting window, UI lifecycle management, scroll state preservation, resource deallocation on close, recipe list refresh, vertical list component creation, label for empty recipes

## Summary
This chunk implements the inventory crafting window lifecycle, including initialization of available items and inventories, refreshing the recipe list with scroll state preservation, handling open/close events to allocate or deallocate resources, and updating via a refresh call.

## Explanation
The chunk defines several public functions for managing an inventory crafting UI. The onOpen function initializes three allocator-backed lists: availableItems, itemAmount, and inventories, then calls refresh to populate the window. onClose checks if window.rootComponent exists; if so it deinitializes the component and sets rootComponent to null, then deinit's the three lists and iterates over inventories.items calling inv.deinit with main.globalAllocator before finally deiniting inventories itself. The update function simply calls refresh. The refresh function first saves the current vertical scroll state from oldList.verticalList.scrollBar.currentState if window.rootComponent is non-null, otherwise uses 0. It then creates a new VerticalList with padding and a fixed height of 300 and max items 8. It calls findAvailableRecipes(list) to detect whether recipes changed; if no change occurred and the window already has a root component, it deinit's the list and returns early. If there are no children in the new list, it adds a label with the text 'No craftable\nrecipes found' centered at position (0,0). After finishing the list, it restores the saved scroll state to list.scrollBar.currentState, assigns the list as window.rootComponent via list.toComponent(), computes window.contentSize by adding the component's pos and size plus padding on both axes, then ensures width is at least the minimum window width. Finally it calls gui.updateWindowPositions(). The chunk also contains a rowList.add call that adds an Icon initialized with texture arrowTexture at position (8,0) sized 32x32, and an ItemSlot initialized with inv, recipe.sourceItems.len cast to int, .craftingResult, and .takeOnly. These additions are part of the UI construction logic inside refresh or onOpen.

## Related Questions
- What happens to the scroll position when refresh is called and no recipes changed?
- How does onClose ensure all allocated lists are freed before returning?
- Why is findAvailableRecipes invoked inside refresh instead of onOpen?
- What condition causes refresh to return early without updating window.rootComponent?
- Which function is responsible for adding the 'No craftable recipes found' label?
- How does update delegate its work to another function in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory_crafting.zig_chunk_1*
