# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 2

**Type:** api
**Keywords:** cursor navigation, keyboard modifiers, text selection, line-based movement, start/end positioning
**Symbols:** TextInput, TextInput.right, TextInput.down, TextInput.up, TextInput.gotoStart, TextInput.gotoEnd, TextInput.moveCursorToStart, TextInput.moveCursorToEnd, TextInput.deleteSelection
**Concepts:** text input handling, cursor movement, text selection

## Summary
Handles cursor movement and text selection in a TextInput component.

## Explanation
This chunk implements functions for moving the cursor within a text input field, including handling keyboard modifiers like Shift and Control. It manages cursor navigation (left, right, up, down) and text selection. The `moveCursorVertically` function adjusts the cursor position based on vertical movement relative to lines. The `gotoStart` and `gotoEnd` functions move the cursor to the beginning or end of the text, respectively, with options for selecting text. The `deleteSelection` function removes selected text from the input field.

## Code Example
```zig
pub fn right(self: *TextInput, mods: main.Window.Key.Modifiers) void {
	if (self.cursor) |*cursor| {
		if (mods.shift) {
			if (self.selectionStart == null) {
				self.selectionStart = cursor.*;
			}
			self.moveCursorRight(mods);
			if (self.selectionStart == self.cursor) {
				self.selectionStart = null;
			}
		} else {
			if (self.selectionStart) |selectionStart| {
				cursor.* = @max(cursor.*, selectionStart);
				self.selectionStart = null;
			} else {
				self.moveCursorRight(mods);
			}
		}
		self.ensureCursorVisibility();
	}
}
```

## Related Questions
- How does the TextInput handle cursor movement when Shift is pressed?
- What function moves the cursor to the start of the text?
- How does the TextInput manage vertical cursor movement?
- What happens if there is no selection when moving the cursor left or right?
- How does the deleteSelection function work?
- What role do keyboard modifiers play in TextInput navigation?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_2*
