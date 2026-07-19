# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 3

**Type:** api
**Keywords:** text input, cursor visibility, clipboard operations, GUI rendering, obfuscation
**Symbols:** TextInput, TextInput.inputCharacter, TextInput.setString, TextInput.selectAll, TextInput.copy, TextInput.paste, TextInput.cut, TextInput.newline, TextInput.ensureCursorVisibility, TextInput.getRenderCursorPos, TextInput.render
**Concepts:** text input handling, cursor management, selection and clipboard operations, rendering with GUI components

## Summary
The TextInput component handles text input operations including character insertion, string setting, selection, copying, pasting, cutting, newline handling, and rendering with detailed cursor visibility management. It also includes methods to manage the clipboard and obfuscation of text.

## Explanation
This chunk defines the `TextInput` struct and its methods for handling text input operations such as character insertion (`inputCharacter`), setting strings (`setString`), selecting all text (`selectAll`), copying (`copy`), pasting (`paste`), cutting (`cut`), and newline handling (`newline`). The `ensureCursorVisibility` function manages the cursor's visibility by adjusting scrolling if necessary. Specifically, it ensures that the cursor remains visible within the bounds of the input field by calculating the scroll position based on the current text size and cursor position. The `getRenderCursorPos` function calculates the position for rendering the cursor, considering obfuscation. It converts the character index to a pixel offset taking into account any obfuscated characters. The `render` method handles the rendering of the text input component by drawing the background, text, and cursor with support for selection highlighting and blinking. Additionally, it manages clipboard operations such as copying selected text (`copy`) and pasting clipboard content (`paste`).

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
- How does the `inputCharacter` function handle character insertion including UTF-8 encoding?
- What is the purpose of the `ensureCursorVisibility` method in managing cursor visibility within the input field?
- How does the `copy` function interact with the clipboard to copy selected text?
- What steps are involved in rendering the text input component, including drawing the background and handling selection highlighting?
- How does the `TextInput` struct manage cursor position and visibility during various operations such as insertion and deletion?
- What is the role of the `getRenderCursorPos` function in calculating the correct cursor position for rendering?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_3*
