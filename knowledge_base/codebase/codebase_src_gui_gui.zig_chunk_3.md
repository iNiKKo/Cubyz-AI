# [hard/codebase_src_gui_gui.zig] - Chunk 3

**Type:** api
**Keywords:** SimpleCallback, GuiCommandQueue, windowList, openWindows, selectedTextInput, TextInput, orderedRemove, Vec2f, scale, inventory
**Symbols:** openWindowCallback, closeWindowFromRef, closeWindow, isWindowOpen, setSelectedTextInput, textCallbacks.char, textCallbacks.left, textCallbacks.right, textCallbacks.down, textCallbacks.up, textCallbacks.gotoStart, textCallbacks.gotoEnd, textCallbacks.deleteLeft, textCallbacks.deleteRight, textCallbacks.selectAll, textCallbacks.copy, textCallbacks.paste, textCallbacks.cut, textCallbacks.newline, mainButtonPressed, mainButtonReleased
**Concepts:** window management, mouse hit testing, callback factory pattern, command queue scheduling, optional chaining, text input selection, GUI event handling

## Summary
This chunk defines the core window management callbacks for the GUI system: opening windows via a callback factory, closing windows by ID or reference, querying open state, handling text input selection, and implementing mouse-driven window activation/deactivation with hit-testing.

## Explanation
The chunk declares several public functions that serve as entry points for GUI interactions. The openWindowCallback function takes a compile-time string id and returns a SimpleCallback constructed via initWithPtr pointing to openWindowFromRef; it accesses the windowlist array field using @field(windowlist, id).window. The closeWindowFromRef function accepts a pointer to GuiWindow and schedules a .close command on the GuiCommandQueue with the window as payload. The closeWindow function iterates over windowList.items, compares each window.id against the provided id using std.mem.eql(u8), calls closeWindowFromRef when matched, logs an error if no match is found, and returns early. The isWindowOpen function similarly scans openWindows.items for a matching id and returns true or false. setSelectedTextInput conditionally deselects the current selected text input (if any) before assigning a new pointer; it uses optional chaining to safely access the current value. The textCallbacks struct contains multiple pub fn methods: char, left, right, down, up, gotoStart, gotoEnd, deleteLeft, deleteRight, selectAll, copy, paste, cut, newline. Each method checks if selectedTextInput is non-null and forwards the call to the corresponding TextInput method (e.g., current.inputCharacter(codepoint)). The mainButtonPressed function updates inventory, clears selectedWindow, deselects text input, computes mouse position scaled by scale, then iterates backwards over openWindows.items using a while loop with index i; it uses @reduce(.And) to test if mousePosition lies within each window's bounds (pos <= mouse < pos + size). If the window reports .handled via mainButtonPressed(mousePosition), it removes that window from its original position using orderedRemove(i), appends it back at the end, sets selectedWindow to that window, and returns. The mainButtonReleased function applies inventory changes with a boolean flag, saves oldWindow, clears selectedWindow, then loops over openWindows.items again computing mouse position relative to each window; if the relative position is within bounds (>= Vec2f{0,0} and < size), it sets selectedWindow to that window. After the loop, if selectedWindow differs from oldWindow, it resets selectedWindow to null. Finally, if oldWindow exists, it retrieves its mainButtonReleased(mousePosition) call; the chunk ends mid-statement for that last line.

## Related Questions
- How does openWindowCallback construct a callback for a given window id?
- What happens when closeWindow is called with an id that does not exist in windowList?
- Which function schedules the .close action on GuiCommandQueue and why is it used instead of direct closure?
- How does setSelectedTextInput handle the case where selectedTextInput is already non-null?
- In mainButtonPressed, what is the purpose of iterating over openWindows.items in reverse order?
- What condition must be met for a window to be considered handled during mouse button press?
- How does mainButtonReleased determine which window should become selected after release?
- Why is inventory.applyChanges called with true in mainButtonReleased but not in mainButtonPressed?
- What role does the scale factor play when computing mouse position for hit testing?
- Does any function in this chunk perform binary serialization or networking operations?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_3*
