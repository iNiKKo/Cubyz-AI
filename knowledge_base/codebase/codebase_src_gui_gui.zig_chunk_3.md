# [hard/codebase_src_gui_gui.zig] - Chunk 3

**Type:** api
**Keywords:** text input callbacks, mouse button events, window selection, inventory management, position updates
**Symbols:** textCallbacks, textCallbacks.char, textCallbacks.left, textCallbacks.right, textCallbacks.down, textCallbacks.up, textCallbacks.gotoStart, textCallbacks.gotoEnd, textCallbacks.deleteLeft, textCallbacks.deleteRight, textCallbacks.selectAll, textCallbacks.copy, textCallbacks.paste, textCallbacks.cut, textCallbacks.newline, mainButtonPressed, mainButtonReleased, secondaryButtonPressed, secondaryButtonReleased, updateWindowPositions
**Concepts:** GUI input handling, window management, inventory updates

## Summary
Handles GUI input callbacks and window interactions.

## Explanation
This chunk defines a set of callback functions for text input events and mouse button presses/releases. It manages the state of selected text inputs, windows, and inventory updates. The `mainButtonPressed` function processes main button clicks to update inventory, select windows, and toggle game menus. The `mainButtonReleased` function handles main button releases by applying inventory changes and updating window selection. The `secondaryButtonPressed` and `secondaryButtonReleased` functions manage secondary button interactions with the inventory. The `updateWindowPositions` function iteratively updates window positions until no further changes occur.

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
