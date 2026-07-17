# [hard/codebase_src_gui_gui.zig] - Chunk 0

**Type:** api
**Keywords:** ConcurrentQueue, ListManaged, orderedRemove, appendAssumeCapacity, globalInit, onOpenFn, onCloseFn, updateWindowPositions, BagSlot
**Symbols:** GuiCommandQueue, GuiCommandQueue.Action, GuiCommandQueue.Command, initWindowList, deinitWindowList, init, GuiWindow, tooltip, windowlist
**Concepts:** window list management, command queue, GUI component initialization, callback registration, deferred position updates

## Summary
This chunk defines the GUI subsystem's window list management, command queue for opening/closing windows, and initialization of all GUI components.

## Explanation
The chunk declares a ListManaged(windowList) to hold GuiWindow pointers, plus separate hudWindows and openWindows lists. It exposes selectedWindow, selectedTextInput, hoveredAWindow, reorderWindows, hideGui, scale, and hoveredItemSlot as public or internal state. A GuiCommandQueue struct holds an enum Action {open, close} and a Command struct with window pointer and action; it uses main.utils.ConcurrentQueue for thread-safe command storage. The queue provides init(), deinit(), scheduleCommand() which pushes to the concurrent queue, and executeCommands() which drains the queue and dispatches open/close actions via executeOpenWindowCommand/executeCloseWindowCommand. Those functions update openWindows by orderedRemove or appendAssumeCapacity, call onOpenFn/onCloseFn callbacks, and defer updateWindowPositions(). initWindowList() initializes the command queue, creates the three window lists with main.globalAllocator, iterates over windowlist's struct declarations to set each windowStruct.window.id from the declaration name, calls addWindow(), and then maps function names (render, update, updateSelected, updateHovered, onOpen, onClose) onto their Fn fields if declared. deinitWindowList() clears and frees all lists and deinitializes the command queue. The init() function iterates over windowlist declarations again to call any init method present, then calls globalInit() for GuiWindow, GuiComponent.BagSlot, Button, CheckBox, ItemSlot, ScrollBar, ContinuousSlider, DiscreteSlider, and TextInput.

## Related Questions
- How does the GUI subsystem handle opening a window that already exists in openWindows?
- What is the purpose of the GuiCommandQueue and why use a ConcurrentQueue for commands?
- Which functions are automatically wired to their Fn fields during initWindowList?
- Does deinitWindowList free memory or just reset pointers, and what does clearAndFree do?
- How are window IDs assigned in initWindowList and where is addWindow called?
- What state variables control whether the GUI is hidden (hideGui) or reordered (reorderWindows)?
- Where is updateWindowPositions deferred and why is it placed there?
- Are any of the component globalInit calls optional or guarded by a flag?
- How does selectedTextInput relate to openWindows and what happens when a text input is focused?
- What is the relationship between hudWindows and openWindows in terms of lifecycle?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_0*
