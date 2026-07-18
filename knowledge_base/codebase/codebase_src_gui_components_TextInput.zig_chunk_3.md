# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 3

**Type:** api
**Keywords:** text input, cursor visibility, clipboard operations, GUI rendering, obfuscation
**Symbols:** TextInput, TextInput.inputCharacter, TextInput.setString, TextInput.selectAll, TextInput.copy, TextInput.paste, TextInput.cut, TextInput.newline, TextInput.ensureCursorVisibility, TextInput.getRenderCursorPos, TextInput.render
**Concepts:** text input handling, cursor management, selection and clipboard operations, rendering with GUI components

## Summary
The TextInput component handles text input operations such as character insertion, string setting, selection, copying, pasting, cutting, and rendering with cursor visibility management.

## Explanation
This chunk defines the `TextInput` struct and its methods for handling text input. It includes functions for inserting characters (`inputCharacter`), setting strings (`setString`), selecting all text (`selectAll`), copying (`copy`), pasting (`paste`), cutting (`cut`), and handling newlines (`newline`). The `ensureCursorVisibility` function manages the cursor's visibility by adjusting scrolling if necessary. The `getRenderCursorPos` function calculates the position for rendering the cursor, considering obfuscation. The `render` method handles the rendering of the text input component, including drawing the background, text, and cursor, with support for selection highlighting and blinking.

## Code Example
```zig
pub fn inputCharacter(self: *TextInput, character: u21) void {
	if (self.cursor) |*cursor| {
		self.deleteSelection();
		var buf: [4]u8 = undefined;
		const utf8 = buf[0 .. std.unicode.utf8Encode(character, &buf) catch return];
		self.currentString.insertSlice(cursor.*, utf8);
		self.reloadText();
		cursor.* += @intCast(utf8.len);
		self.ensureCursorVisibility();
	}
}
```

## Related Questions
- How does the `inputCharacter` function handle character insertion?
- What is the purpose of the `ensureCursorVisibility` method?
- How does the `copy` function interact with the clipboard?
- What steps are involved in rendering the text input component?
- How does the `TextInput` struct manage cursor position and visibility?
- What is the role of the `getRenderCursorPos` function in the rendering process?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_3*
