# [hard/codebase_src_gui_gui.zig] - Chunk 6

**Type:** implementation
**Keywords:** leftClickSlots, rightClickSlots, hoveredItemSlot, main.stackAllocator, ClientInventory, creative, shift key, dropStack, takeHalf, fillAnyFromCreative
**Symbols:** applyChanges, render
**Concepts:** inventory distribution, creative mode fill, tooltip rendering, stack allocation, GUI interaction

## Summary
Implements the GUI interaction logic for inventory slots: left-click distributes items to target inventories (with shift+click creative fill), right-click deposits or takes half, and handles drop actions when no slot is hovered.

## Explanation
The chunk defines three functions. applyChanges(leftClick) first checks initialization and world presence; on left click it deinitializes the crafting recipe item, then if there are items in leftClickSlots it allocates arrays of ClientInventory and u32 via main.stackAllocator, copies each slot's inventory pointer and itemSlot index into them, calls carried.distribute with those arrays, and clears leftClickSlots. If no slots exist but a hoveredItemSlot is present, it skips crafting/workbenchResult inventories; if shift is held (main.KeyBoard.key("mainGuiButton").modsOnPress.shift) and the hovered inventory is creative, it retrieves the item via getItem(hovered.itemSlot) and calls ClientInventory.fillAnyFromCreative with main.game.Player.inventory. Otherwise it checks pressed state or drops the carried stack. On right click it clears rightClickSlots if any exist; otherwise for a hovered slot it skips crafting/workbenchResult, fills creative inventories by depositing one unit, or takes half from other inventories via takeHalf; if no window is hovered and selectedWindow is null it calls carried.dropOne(0). render(mousePos) checks initialization, sets carriedItemSlot.pos to mousePos minus an offset, renders the carried item slot at (0,0), then retrieves the hovered slot; if the carried amount is zero it fetches the tooltip content from the hovered inventory's getItem and calls tooltip.renderFromText with the mouse position.

## Related Questions
- What happens when leftClickSlots is empty but a hovered item slot exists in applyChanges?
- How does the chunk handle shift+click on a creative inventory?
- Which inventories are skipped during right-click deposit or half-take operations?
- What condition causes render to skip tooltip display even if an item is hovered?
- Where is main.stackAllocator used for allocation in this chunk?
- How does the chunk ensure carriedItemSlot renders at a consistent offset from mousePos?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_6*
