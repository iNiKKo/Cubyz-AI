# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 2

**Type:** implementation
**Keywords:** cursor, selection, deletion, key handling, text manipulation
**Symbols:** down, up, gotoStart, gotoEnd, deleteLeft, deleteRight
**Concepts:** text input, cursor movement, text selection, deletion

## Summary
Handles cursor movement, text selection, and deletion in a text input component.

## Explanation
This chunk defines methods for moving the cursor up, down, to the start, and end of a text input field. It also handles text selection with shift key modifications and provides functionality to delete selected text or characters to the left or right of the cursor. The `moveCursorVertically`, `moveCursorToStart`, `moveCursorToEnd`, `deleteSelection`, `deleteLeft`, and `deleteRight` functions manage the internal state of the text input, including updating the cursor position, handling selections, and modifying the text content.

## Code Example
```zig
pub fn down(self: *TextInput, mods: main.Window.Key.Modifiers) void {
	if (self.cursor) |*cursor| {
		if (mods.shift) {
			if (self.selectionStart == null) {
				self.selectionStart = cursor.*;
			}
			_ = self.moveCursorVertically(1);
			if (self.selectionStart == self.cursor) {
				self.selectionStart = null;
			}
		} else {
			if (self.selectionStart) |selectionStart| {
				cursor.* = @max(cursor.*, selectionStart);
				self.selectionStart = null;
			} else {
				if (self.moveCursorVertically(1) == .same) {
					self.callbacks.onDown.run();
				}
			}
		}
		self.ensureCursorVisibility();
	}
}
```

## Related Questions
- How does the `down` function handle cursor movement with the shift key?
- What is the purpose of the `gotoStart` method in this chunk?
- How does the `deleteSelection` function modify the text content?
- What conditions trigger the execution of the `onDown` callback?
- How does the `moveCursorToEnd` function determine the new cursor position?
- What role does the `selectionStart` field play in text selection operations?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_2*
