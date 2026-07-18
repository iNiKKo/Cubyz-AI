# [easy/codebase_src_gui_windows_workbench.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, item crafting, window positioning, inventory update, property display
**Symbols:** window, craftingGridInv, craftingResultInv, itemSlots, proceduralItemTypes, currentProceduralItemType, proceduralItemButton, needsUpdate, toggleProceduralItem, updateResult, openInventory, closeInventory, update, render, onOpen, onClose
**Concepts:** GUI window management, crafting system, procedural item creation, inventory interaction

## Summary
Manages the workbench GUI window for crafting items.

## Explanation
This chunk defines the logic for a workbench GUI window in the Cubyz engine. It handles the initialization, updating, rendering, and closing of the workbench window. The workbench allows players to craft procedural items using a grid-based inventory system. Key functionalities include toggling between different procedural item types, updating the crafting result based on the grid contents, and displaying properties of the crafted item. The chunk uses various GUI components like buttons, lists, and item slots to create an interactive interface.

## Code Example
```zig
fn toggleProceduralItem() void {
	currentProceduralItemType += 1;
	currentProceduralItemType %= proceduralItemTypes.items.len;
	proceduralItemButton.child.label.updateText(proceduralItemTypes.items[currentProceduralItemType].id());
	needsUpdate = true;
}
```

## Related Questions
- What is the purpose of the `toggleProceduralItem` function?
- How does the workbench window update its content when a procedural item type changes?
- What components are used to create the crafting grid in the workbench window?
- How is the durability and damage of the crafted item displayed in the GUI?
- What happens when the workbench window is opened or closed?
- How does the `updateResult` function handle the crafting process?

*Source: unknown | chunk_id: codebase_src_gui_windows_workbench.zig_chunk_0*
