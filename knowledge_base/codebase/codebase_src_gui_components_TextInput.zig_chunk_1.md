# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 1

**Type:** implementation
**Keywords:** cursor, selection, keyboard modifiers, text buffer, vertical scrolling
**Symbols:** mainButtonReleased, select, deselect, reloadText, characterType, moveCursorLeft, left, moveCursorRight, right, moveCursorVertically
**Concepts:** text input, cursor movement, selection handling, scrolling

## Summary
The TextInput component handles text input interactions including cursor movement, selection, and scrolling.

## Explanation
This chunk defines the TextInput component's behavior in handling user interactions including button releases, cursor movements (left and right), and vertical scrolling. It includes methods for selecting and deselecting text, reloading text content, determining character types, and managing cursor visibility.

The `mainButtonReleased` method handles releasing the main button and scrolls if necessary. If the text size exceeds the maximum height, it calculates the difference (`diff = self.textSize[1] - (self.maxHeight - 2*border)`) and adjusts the text position based on the scrollbar's current state (`textPos[1] -= diff*self.scrollBar.currentState`). It then updates the cursor position based on the mouse position relative to the text buffer (`self.cursor = self.textBuffer.mousePosToIndex(mousePosition - textPos - self.pos, self.currentString.items.len)`) and sets the TextInput as selected (`gui.setSelectedTextInput(self)`). If the cursor is at the selection start, it clears the selection start (`self.selectionStart = null`). Finally, it resets the pressed state (`self.pressed = false`).

The `select` method sets the TextInput as selected (`gui.setSelectedTextInput(self)`) and resets selection start (`self.selectionStart = null`). The `deselect` method clears the cursor (`self.cursor = null`) and selection start (`self.selectionStart = null`). The `reloadText` function updates the text buffer (`self.textBuffer.deinit(); self.textBuffer = TextBuffer.init(main.globalAllocator, self.currentString.items, .{}, true, .left)`) and recalculates line breaks based on font size and maximum width (`self.textSize = self.textBuffer.calculateLineBreaks(fontSize, self.maxWidth - 2*border - scrollBarWidth)`).

The `characterType` function categorizes characters into literal, symbol, or whitespace types. The `moveCursorLeft` function handles left cursor movement with support for Shift and Control modifiers to extend selection boundaries. When the Control modifier is used (`mods.control`), it moves the cursor to the start of the previous word by decrementing the cursor position until a non-whitespace character is found, then continues decrementing until a different type of character is encountered. The `moveCursorRight` function handles right cursor movement with similar support for Shift and Control modifiers. When the Control modifier is used (`mods.control`), it moves the cursor to the end of the next word by incrementing the cursor position until a non-whitespace character is found, then continues incrementing until a different type of character is encountered.

The `left` and `right` methods adjust the cursor position based on keyboard modifiers and ensure cursor visibility after movement (`self.ensureCursorVisibility()`).

The `moveCursorVertically` function adjusts the cursor position vertically by calculating the new index based on the relative lines parameter and ensuring the cursor remains within bounds.

## Code Example
```zig
pub fn deselect(self: *TextInput) void {
	self.cursor = null;
	self.selectionStart = null;
}
```

## Related Questions
- How does the TextInput component handle button releases?
- What is the logic behind moving the cursor left with control modifier?
- How does the TextInput component manage text selection with Shift and Control modifiers?
- What steps are involved in reloading text content in the TextInput component?
- How does the TextInput component ensure cursor visibility after movements?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_1*
