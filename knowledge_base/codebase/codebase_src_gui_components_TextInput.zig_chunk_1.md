# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 1

**Type:** implementation
**Keywords:** cursor, selection, keyboard modifiers, text buffer, vertical scrolling
**Symbols:** mainButtonReleased, select, deselect, reloadText, characterType, moveCursorLeft, left, moveCursorRight, right, moveCursorVertically
**Concepts:** text input, cursor movement, selection handling, scrolling

## Summary
The TextInput component handles text input interactions including cursor movement, selection, and scrolling.

## Explanation
This chunk defines the TextInput component's behavior in handling user interactions including button releases, cursor movements (left and right), and vertical scrolling. It includes methods for selecting and deselecting text, reloading text content, determining character types, and managing cursor visibility. The `mainButtonReleased` method handles releasing the main button and scrolls if necessary. The `select` method sets the TextInput as selected and resets selection start. The `deselect` method clears the cursor and selection start. The `reloadText` function updates the text buffer and recalculates line breaks based on font size and maximum width. The `characterType` function categorizes characters into literal, symbol, or whitespace types. The `moveCursorLeft` and `moveCursorRight` functions handle left and right cursor movements with support for Shift and Control modifiers to extend selection boundaries. The `left` and `right` methods adjust the cursor position based on keyboard modifiers and ensure cursor visibility after movement.

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
