# [medium/codebase_src_gui_windows_inventory_crafting.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, item management, recipe matching, texture handling, list operations
**Symbols:** window, padding, availableItems, itemAmount, inventories, arrowTexture, init, deinit, addItemStackToAvailable, findAvailableRecipes
**Concepts:** GUI window management, inventory system, crafting recipes

## Summary
Handles the crafting inventory GUI window, managing available items and recipes.

## Explanation
This chunk defines the logic for the crafting inventory GUI window in Cubyz. It initializes and deinitializes textures, manages lists of available items and their amounts, and finds recipes that can be crafted based on the player's inventory. The `init` function initializes the arrow texture from a file. The `deinit` function deinitializes the arrow texture. The `addItemStackToAvailable` function updates the list of available items and their quantities by iterating through the player's inventory and adding or updating item amounts in the `availableItems` and `itemAmount` lists.

The `findAvailableRecipes` function performs several key tasks:
1. It duplicates the current item amounts to track changes.
2. It resets the item amounts to zero.
3. It iterates through the player's inventory to update the available items list with the current stack amounts.
4. If no changes are detected in the available items, it returns false.
5. It removes any items that are no longer present in the inventory from the `availableItems` and `itemAmount` lists.
6. It deinitializes and clears old inventories.
7. It iterates through all possible recipes to determine if they can be crafted with the current available items.
8. For each craftable recipe, it creates a new `ClientInventory` instance with the source items and the crafting result.
9. It adds the source items and the crafting result to a GUI layout by creating horizontal lists for each recipe, which are displayed as columns.
10. It adds an icon for the crafting arrow between the source items and the crafting result.

The function also handles texture initialization and deinitialization, and uses data structures such as `availableItems`, `itemAmount`, and `inventories`.

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
