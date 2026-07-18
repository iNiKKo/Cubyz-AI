# [medium/codebase_src_gui_windows_inventory_crafting.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, item management, recipe matching, texture handling, list operations
**Symbols:** window, padding, availableItems, itemAmount, inventories, arrowTexture, init, deinit, addItemStackToAvailable, findAvailableRecipes
**Concepts:** GUI window management, inventory system, crafting recipes

## Summary
Handles the crafting inventory GUI window, managing available items and recipes.

## Explanation
This chunk defines the logic for the crafting inventory GUI window in Cubyz. It initializes and deinitializes textures, manages lists of available items and their amounts, and finds recipes that can be crafted based on the player's inventory. The `init` function initializes the arrow texture from a file. The `deinit` function deinitializes the arrow texture. The `addItemStackToAvailable` function updates the list of available items and their quantities by iterating through the player's inventory and adding or updating item amounts in the `availableItems` and `itemAmount` lists. The `findAvailableRecipes` function checks for new or removed items in the inventory, clears old inventories, and iterates through all possible recipes to determine if they can be crafted with the current available items. It then creates a GUI layout for each recipe by adding source items and the crafting result to a list of horizontal lists, which are displayed as columns. The function also handles texture initialization and deinitialization, and uses data structures such as `availableItems`, `itemAmount`, and `inventories`.

## Code Example
```zig
pub fn init() void {
	arrowTexture = Texture.initFromFile("assets/cubyz/ui/inventory/crafting_arrow.png");
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `addItemStackToAvailable` function update the available items list?
- What steps are involved in finding and displaying available recipes in the crafting inventory?
- How is the texture for the crafting arrow initialized and deinitialized?
- What data structures are used to manage available items and their amounts?
- How does the chunk handle changes in the player's inventory to update available recipes?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory_crafting.zig_chunk_0*
