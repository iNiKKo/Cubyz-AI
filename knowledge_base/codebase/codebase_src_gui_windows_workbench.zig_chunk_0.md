# [easy/codebase_src_gui_windows_workbench.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI components, item crafting, window positioning, inventory update, property display
**Symbols:** window, craftingGridInv, craftingResultInv, itemSlots, proceduralItemTypes, currentProceduralItemType, proceduralItemButton, needsUpdate, toggleProceduralItem, updateResult, openInventory, closeInventory, update, render, onOpen, onClose
**Concepts:** GUI window management, crafting system, procedural item creation, inventory interaction

## Summary
Manages the workbench GUI window for crafting procedural items. It initializes a grid-based inventory system with specific slot configurations, updates the crafting result based on item properties like durability and damage, and displays these properties in the GUI.

## Explanation
This chunk defines the logic for managing the workbench GUI window in Cubyz, which allows players to craft procedural items using a grid-based inventory system. Key functionalities include toggling between different procedural item types, updating the crafting result based on the grid contents, and displaying properties of the crafted item such as durability and damage.

The `window` variable is initialized with specific dimensions and positioning relative to other windows. The `craftingGridInv` and `craftingResultInv` variables represent client-side inventories for the workbench grid and result slots respectively. These inventories are updated based on player actions and procedural item types.

The `toggleProceduralItem` function increments the current procedural item type index, updates the button label to reflect the new item type ID, and triggers an update of the crafting grid and results.

The `updateResult` function deinitializes and reinitializes the result inventory based on the contents of the workbench grid. It calculates the crafted item using the `ProceduralItem.initFromInventory` method and updates the display accordingly.

GUI components such as buttons, lists, and item slots are used to create an interactive interface for the crafting process. The durability and damage properties of the crafted item are displayed in the GUI with specific text formatting based on their values.

When the workbench window is opened or closed, it initializes or deinitializes the inventories and updates the GUI components accordingly.

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
