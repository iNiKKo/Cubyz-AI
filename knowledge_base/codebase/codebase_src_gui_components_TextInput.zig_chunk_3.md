# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 3

**Type:** api
**Keywords:** cursor movement, text insertion, selection handling, clipboard interaction, scrolling adjustment
**Symbols:** TextInput, TextInput.cursor, TextInput.selectionStart, TextInput.currentString, TextInput.callbacks.onNewline.inner, TextInput.textSize, TextInput.maxHeight, TextInput.border, TextInput.scrollBar.currentState, TextInput.showCusor, TextInput.lastBlinkTime, TextInput.textBuffer.indexToCursorPos
**Concepts:** text input handling, cursor management, selection and deletion, clipboard operations

## Summary
Handles text input operations including cursor movement, selection, deletion, insertion, and clipboard interactions.

## Explanation
This chunk defines the `TextInput` struct and its methods for managing text input in a GUI component. It includes functions for moving the cursor (left, right, to end), deleting characters or selections, inserting new characters, setting the entire string, selecting all text, copying, pasting, and cutting text. The `ensureCursorVisibility` method ensures the cursor remains visible by adjusting scrolling if necessary. The chunk also handles newline input and clipboard operations under specific modifier conditions.

## Code Example
```zig
pub fn deleteLeft(self: *TextInput, mods: main.Window.Key.Modifiers) void {
	if (self.cursor == null) return;
	if (self.selectionStart == null) {
		self.selectionStart = self.cursor;
		self.moveCursorLeft(mods);
	}
	self.deleteSelection();
	self.reloadText();
	self.ensureCursorVisibility();
}
```

## Related Questions
- How does the `TextInput` struct handle cursor movement to the end?
- What method is responsible for deleting a selection in the `TextInput` component?
- How does the `TextInput` manage clipboard operations like copy and paste?
- What function ensures the cursor remains visible within the text input area?
- How does the `TextInput` handle newline input under specific conditions?
- What is the role of the `ensureCursorVisibility` method in the `TextInput` component?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_3*
