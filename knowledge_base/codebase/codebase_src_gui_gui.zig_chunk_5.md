# [hard/codebase_src_gui_gui.zig] - Chunk 5

**Type:** implementation
**Keywords:** ClientInventory, ItemSlot, swapRemove, mainGuiButton, craftFrom, craftProceduralItem, depositToAny, openWindows, shiftClickableInventory, stackAllocator
**Symbols:** inventory, inventory.carried, inventory.carriedItemSlot, inventory.leftClickSlots, inventory.rightClickSlots, inventory.recipeItem, inventory.initialized, inventory.minCraftingCooldown, inventory.maxCraftingCooldown, inventory.nextCraftingAction, inventory.craftingCooldown, inventory.isCrafting, inventory.init, inventory.deinit, inventory.deleteItemSlotReferences, inventory.update, inventory.applyChanges
**Concepts:** inventory management, crafting cooldowns, item slot queues, shift click deposit, window iteration, stack allocator usage

## Summary
Implements the client-side inventory system, including item slot management, crafting cooldown logic, and deposit operations.

## Explanation
The chunk defines a pub const inventory struct that holds state for carried items, left/right click slots, crafting timers, and recipe tracking. It exposes init() to construct a ClientInventory with the player ID as owner, deinit() to free allocated resources, deleteItemSlotReferences(slot) to remove hovered or queued slots from both leftClickSlots and rightClickSlots lists via swapRemove loops, update() which runs every frame when initialized: it checks if the hovered slot is immutable (skip), then evaluates crafting conditions—if the slot type is .crafting or .workbenchResult and mode is .takeOnly and mainGuiButton.pressed—entering a cooldown loop that advances nextCraftingAction by minCraftingCooldown (20ms) to maxCraftingCooldown (400ms); inside, for .crafting it clones the item into recipeItem if null, compares equality, and on shift press calls main.game.Player.inventory.craftFrom with carried or player inventory; for .workbenchResult it calls craftProceduralItem. After crafting returns, reset isCrafting to false. If no crafting, it checks shift+mainGuiButton.pressed: when the slot's super.id matches the player inventory's super.id, it iterates openWindows.shiftClickableInventory windows and deposits into any matching window before depositing into the bag; otherwise deposits directly into player inventory. For normal mode with carried item count > 0, left click appends to leftClickSlots if not already present or stack size differs from carried item at index 0; right click deposits one unit into carried and appends to rightClickSlots. applyChanges(leftClick) begins by deiniting recipeItem and resetting isCrafting, then allocates targetInventories and targetSlots arrays sized to leftClickSlots.items.len using main.stackAllocator with defer frees.

## Related Questions
- What are the minimum and maximum crafting cooldown durations defined in this inventory struct?
- How does update() handle a hovered item slot that is marked as immutable?
- Under what conditions does the chunk call main.game.Player.inventory.craftFrom versus craftProceduralItem?
- Which list structures store slots pending left-click and right-click actions, and how are they cleared in deinit?
- What happens to recipeItem when applyChanges is invoked with leftClick set to true?
- How does the chunk decide whether to deposit into openWindows or directly into the player inventory on shift press?
- In update(), what guard prevents appending a slot to leftClickSlots if it already exists in that list?
- What role does main.timestamp() play inside the crafting cooldown loop?
- Does deleteItemSlotReferences modify the hoveredItemSlot pointer when removing a slot from leftClickSlots?
- How are targetInventories and targetSlots allocated in applyChanges, and what ensures their memory is freed?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_5*
