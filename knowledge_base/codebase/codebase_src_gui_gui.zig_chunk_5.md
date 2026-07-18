# [hard/codebase_src_gui_gui.zig] - Chunk 5

**Type:** api
**Keywords:** inventory, slots, crafting, user input, rendering, tooltip
**Symbols:** inventory, ItemStack, ClientInventory, carried, carriedItemSlot, leftClickSlots, rightClickSlots, recipeItem, initialized, minCraftingCooldown, maxCraftingCooldown, nextCraftingAction, craftingCooldown, isCrafting, init, deinit, deleteItemSlotReferences, update, applyChanges, render
**Concepts:** inventory management, GUI rendering, item interactions, crafting system

## Summary
Handles inventory management and rendering in the GUI.

## Explanation
This chunk defines a module for managing player inventories within the GUI. It includes structures for item stacks, client inventories, and various slots for left-click and right-click actions. The `init` function initializes the carried inventory and related slots. The `deinit` function cleans up resources. The `deleteItemSlotReferences` function removes references to deleted item slots. The `update` function handles crafting logic and item interactions based on user input. The `applyChanges` function applies changes made during left-click or right-click actions, distributing items between inventories or handling creative mode deposits. The `render` function updates the position of the carried item slot and renders tooltips for hovered items.

## Code Example
```zig
pub fn init() void {
	carried = ClientInventory.init(main.globalAllocator, 1, .serverShared, .{.hand = main.game.Player.id}, .{});
	carriedItemSlot = ItemSlot.init(.{0, 0}, carried, 0, .default, .normal);
	carriedItemSlot.renderFrame = false;
	initialized = true;
	isCrafting = false;
}
```

## Related Questions
- What is the purpose of the `init` function in the inventory module?
- How does the `update` function handle crafting actions?
- What does the `applyChanges` function do when left-click is applied?
- How are item slots managed in this chunk?
- What role does the `render` function play in the GUI?
- How is the carried inventory initialized and deinitialized?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_5*
