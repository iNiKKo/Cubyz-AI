# [medium/codebase_src_gui_windows_inventory_crafting.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture initialization, item availability, recipe finding, UI refresh, vertical list, horizontal list
**Symbols:** window, padding, availableItems, itemAmount, inventories, arrowTexture, init, deinit, addItemStackToAvailable, findAvailableRecipes, refresh
**Concepts:** inventory management, crafting recipes, GUI window handling

## Summary
The chunk manages the crafting inventory GUI window, handling item availability, recipe finding, and UI refresh.

## Explanation
This chunk defines the logic for the crafting inventory GUI window in Cubyz. It initializes and deinitializes textures, manages available items and their amounts, finds recipes based on player inventory contents, and refreshes the GUI to display these recipes. The `init` function loads the arrow texture, while `deinit` frees it. The `addItemStackToAvailable` function updates the list of available items and their quantities. The `findAvailableRecipes` function determines which recipes can be crafted with the current inventory items, creating a list of possible crafting combinations. The `refresh` function updates the GUI window to reflect any changes in available recipes, ensuring that the player sees the correct options.

## Code Example
```zig
pub fn deinit() void {
	arrowTexture.deinit();
}
```

## Related Questions
- How does the chunk initialize the arrow texture?
- What function updates the list of available items and their quantities?
- How does the chunk determine which recipes can be crafted?
- What steps are involved in refreshing the GUI window?
- How is the vertical list used to display crafting options?
- What happens if no craftable recipes are found?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory_crafting.zig_chunk_0*
