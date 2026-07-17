# [easy/codebase_src_gui_windows_workbench.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, ClientInventory, ItemSlot, ProceduralItemTypeIndex, HorizontalList, VerticalList, deinit, rootComponent, needsUpdate
**Symbols:** window, craftingGridInv, craftingResultInv, itemSlots, proceduralItemTypes, currentProceduralItemType, proceduralItemButton, needsUpdate, toggleProceduralItem, updateResult, openInventory, closeInventory, update, render, onOpen, onClose
**Concepts:** GUI window positioning, procedural item type selection, crafting grid layout, ItemSlot component initialization, inventory lifecycle management, result inventory handling, needsUpdate flag pattern

## Summary
This chunk defines the workbench GUI window, including procedural item type selection, crafting grid layout with ItemSlot components, result inventory handling, and lifecycle callbacks for opening/closing.

## Explanation
The chunk declares a top-level GuiWindow named 'window' positioned relative to the inventory window, with content size computed from its root component. It defines two ClientInventory instances: 'craftingGridInv' (25 slots) and 'craftingResultInv' (1 slot). A global array 'itemSlots' holds pointers to ItemSlot components for each grid position. Procedural item types are stored in a List<ProceduralItemTypeIndex> named 'proceduralItemTypes', with a current index tracked by 'currentProceduralItemType'. The Button component 'proceduralItemButton' is used to cycle procedural items; its label text is updated via toggleProceduralItem(). The openInventory() function initializes both inventories, builds the crafting grid using nested HorizontalList/VerticalList loops, populates each slot with ItemSlot.init() using slotInfo from the current procedural item type (handling disabled/optional states), adds a VerticalList containing the procedural item button and a result list (Icon + ItemSlot for the crafted item), then attaches the resulting GuiComponent to window.rootComponent and recomputes contentSize. closeInventory() deinitializes both inventories and cleans up the root component if present. update() checks needsUpdate flag, resets it, closes then reopens the inventory. render() reads craftingResultInv.getItem(0) and prints durability (color-coded), swing speed, and damage using main.graphics.draw.print(). onOpen() initializes proceduralItemTypes by iterating ProceduralItemTypeIndex.iterator(), appending each type to the list, then calls openInventory(). onClose() deinitializes proceduralItemTypes and closes inventory.

## Related Questions
- What is the purpose of the needsUpdate flag in this chunk?
- How does openInventory initialize the crafting grid slots using procedural item type information?
- Which function deinitializes both inventories and cleans up window.rootComponent on close?
- What happens to currentProceduralItemType when onOpen is called?
- How are disabled or optional slotInfo states reflected in ItemSlot initialization?
- Where does the result inventory's item come from after crafting completes?
- What data is printed by render and how is durability color determined?
- Does this chunk declare any pub const re-exports of external modules?

*Source: unknown | chunk_id: codebase_src_gui_windows_workbench.zig_chunk_0*
