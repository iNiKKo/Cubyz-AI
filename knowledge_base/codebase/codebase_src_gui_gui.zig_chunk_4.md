# [hard/codebase_src_gui_gui.zig] - Chunk 4

**Type:** api
**Keywords:** window selection, mouse position check, GuiCommandQueue, hover detection, render order reversal, grabbed state toggle, item deposit drop, crafting cooldown, allocator initialization, defer restore
**Symbols:** mainButtonReleased, secondaryButtonPressed, secondaryButtonReleased, updateWindowPositions, updateAndRenderGui, toggleGameMenu, inventory
**Concepts:** window management, mouse interaction, GUI rendering pipeline, inventory system, crafting cooldowns

## Summary
This chunk defines the GUI subsystem's public API, including window management (selection, ordering), mouse interaction handling for primary/secondary buttons, position updates, rendering pipeline integration, and a full inventory system with crafting cooldowns.

## Explanation
The chunk declares several pub functions: mainButtonReleased handles window selection via mouse position checks and delegates to the selected window's own release handler; secondaryButtonPressed calls inventory.update(); secondaryButtonReleased calls inventory.applyChanges(false); updateWindowPositions iterates over windowList, calling each window's updateWindowPosition() and tracks changes with a tolerance of 1e-3 squared; updateAndRenderGui orchestrates GUI state: it resets hoveredAWindow, executes GuiCommandQueue commands, processes mouse hover detection in reverse order (last-rendered first) using GuiComponent.contains and window.updateHovered returning .handled to set hoveredAWindow true, updates inventory, then renders windows only if hideGui is false and the window isn't grabbed, restoring draw color and scale with defer blocks, rendering each window via window.render(mousePos) followed by inventory.render(mousePos), and finally rendering gamepad_cursor; toggleGameMenu toggles main.Window.grabbed, hides/shows gui based on grab state, deposits or drops carried items into the player's inventory when grabbed is true (clearing hoveredItemSlot), iterates openWindows to close any with closeIfMouseIsGrabbed flag using swapRemove and calling onCloseFn, then resets reorderWindows and selectedWindow; the chunk also defines a pub const inventory struct containing fields: carried (ClientInventory), carriedItemSlot (*ItemSlot), leftClickSlots and rightClickSlots (ListManaged(*ItemSlot) initialized via main.globalAllocator), recipeItem (main.items.Item set to .null), initialized (bool false), minCraftingCooldown (std.Io.Duration fromMilliseconds 20), maxCraftingCooldown (400ms), nextCraftingAction (undefined std.Io.Timestamp), craftingCooldown (undefined std.Io.Duration), isCrafting (bool false); it declares pub fn init() which initializes carried via ClientInventory.init with allocator, hand set to main.game.Player.id, sets carriedItemSlot at position 0 with renderFrame false and marks initialized true; it declares pub fn deinit() which sets initialized false and calls carried.deinit and carriedItemSlot.deinit (body truncated in the provided snippet).

## Related Questions
- How does mainButtonReleased determine which window is selected based on mouse position?
- What happens to the inventory when secondaryButtonReleased is called versus secondaryButtonPressed?
- Why are leftClickSlots and rightClickSlots initialized with ListManaged via main.globalAllocator instead of a regular allocator?
- In updateAndRenderGui, why does hover detection iterate openWindows in reverse order?
- What condition causes toggleGameMenu to deposit or drop carried items into the player's inventory?
- How does the chunk ensure that windows are only rendered when hideGui is false and main.Window.grabbed is false?
- What role does GuiComponent.contains play in the hover detection logic within updateAndRenderGui?
- Why is there a defer block around draw.setColor and draw.setScale calls in updateAndRenderGui?
- How does the chunk handle closing windows that have closeIfMouseIsGrabbed set to true inside toggleGameMenu?
- What are the default values for minCraftingCooldown and maxCraftingCooldown expressed as std.Io.Duration?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_4*
