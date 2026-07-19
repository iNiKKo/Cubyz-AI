# [hard/codebase_src_gui_gui.zig] - Chunk 5

**Type:** api
**Keywords:** inventory, slots, crafting, user input, rendering, tooltip
**Symbols:** inventory, ItemStack, ClientInventory, carried, carriedItemSlot, leftClickSlots, rightClickSlots, recipeItem, initialized, minCraftingCooldown, maxCraftingCooldown, nextCraftingAction, craftingCooldown, isCrafting, init, deinit, deleteItemSlotReferences, update, applyChanges, render
**Concepts:** inventory management, GUI rendering, item interactions, crafting system

## Summary
Handles inventory management and rendering in the GUI.

## Explanation
This chunk defines a module for managing player inventories within the GUI. It includes structures for item stacks (`ItemStack`), client inventories (`ClientInventory`), and various slots for left-click (`leftClickSlots`) and right-click (`rightClickSlots`) actions. The `init` function initializes the carried inventory and related slots, setting up a default item slot with rendering disabled. The `deinit` function cleans up resources by deinitializing the carried inventory and clearing lists of item slots. The `deleteItemSlotReferences` function removes references to deleted item slots from both left-click and right-click lists.

The `update` function handles crafting logic and item interactions based on user input. It checks for specific conditions related to crafting cooldowns (`minCraftingCooldown` and `maxCraftingCooldown`) and updates the crafting state accordingly. The function also manages item transfers between inventories, including handling creative mode deposits and procedural item crafting.

The `applyChanges` function applies changes made during left-click or right-click actions. When left-click is applied, it distributes items between target inventories or swaps items within the same inventory. For right-click, it either clears the right-click slots or handles item transfers based on the type of inventory being interacted with.

The `render` function updates the position of the carried item slot and renders tooltips for hovered items, providing visual feedback to the player.

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
