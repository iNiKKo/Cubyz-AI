# [hard/codebase_src_gui_gui.zig] - Chunk 3

**Type:** api
**Keywords:** text input callbacks, mouse button events, window selection, inventory management, position updates
**Symbols:** textCallbacks, textCallbacks.char, textCallbacks.left, textCallbacks.right, textCallbacks.down, textCallbacks.up, textCallbacks.gotoStart, textCallbacks.gotoEnd, textCallbacks.deleteLeft, textCallbacks.deleteRight, textCallbacks.selectAll, textCallbacks.copy, textCallbacks.paste, textCallbacks.cut, textCallbacks.newline, mainButtonPressed, mainButtonReleased, secondaryButtonPressed, secondaryButtonReleased, updateWindowPositions
**Concepts:** GUI input handling, window management, inventory updates

## Summary
Handles GUI input callbacks and window interactions.

## Explanation
This chunk defines a set of callback functions for text input events and mouse button presses/releases. The `textCallbacks` struct includes methods like `char`, `left`, `right`, `down`, `up`, `gotoStart`, `gotoEnd`, `deleteLeft`, `deleteRight`, `selectAll`, `copy`, `paste`, `cut`, and `newline`. Each method checks if a text input is selected and then calls the corresponding method on that input, passing any necessary parameters such as `codepoint` or `mods` (modifiers).

The `mainButtonPressed` function processes main button clicks to update inventory, select windows, and toggle game menus. It first updates the inventory, clears the selected window and text input, calculates the mouse position, and iterates over open windows in reverse order of rendering to find the topmost window under the cursor. If a window is found and its `mainButtonPressed` method returns `.handled`, it removes the window from its current position, appends it to the end of the list (to bring it to the front), selects it, and exits. If no window is found and the game world is not null and the inventory's carried item is null, it toggles the game menu.

The `mainButtonReleased` function handles main button releases by applying inventory changes and updating window selection. It applies changes to the inventory, stores the old selected window, clears the current selection, checks each open window to see if the mouse is within its bounds, updates the selected window accordingly, and unselects it if the mouse left the previously selected window. Finally, it calls `mainButtonReleased` on the old window with the current mouse position.

The `secondaryButtonPressed` function updates the inventory when a secondary button is pressed.

The `secondaryButtonReleased` function applies changes to the inventory without updating it when a secondary button is released.

The `updateWindowPositions` function iteratively updates window positions until no further changes occur. It checks each window's position, updates it, and continues if there was any change.

## Code Example
```zig
pub fn char(codepoint: u21) void {
	if (selectedTextInput) |current| {
		current.inputCharacter(codepoint);
	}
}
```

## Related Questions
- What is the purpose of the `textCallbacks` struct?
- How does the `mainButtonPressed` function handle mouse button presses?
- What actions are performed when a secondary button is released?
- How are window positions updated in this chunk?
- What is the role of the `selectedTextInput` variable?
- How does the code determine which window to interact with on a main button press?

*Source: unknown | chunk_id: codebase_src_gui_gui.zig_chunk_3*
