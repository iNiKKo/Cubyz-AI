# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 1

**Type:** implementation
**Keywords:** mouse interaction, keyboard handling, word-based navigation, text buffer, cursor visibility
**Symbols:** textPos, TextInput, mainButtonReleased, select, deselect, reloadText, characterType, moveCursorLeft, left, moveCursorRight, right
**Concepts:** GUI component, text input, cursor movement, text selection, scrolling

## Summary
This chunk implements the logic for a text input component in a GUI system, handling mouse and keyboard interactions to manage text selection, cursor movement, and scrolling.

## Explanation
The TextInput struct manages text input functionality within a graphical user interface. It includes methods for handling button presses and releases, selecting and deselecting text, moving the cursor left or right with modifiers (like shift or control), reloading text, and ensuring the cursor remains visible. The `characterType` function categorizes characters into literals, symbols, or whitespace to assist in word-based cursor movement. The chunk also contains methods for scrolling text within a constrained area if the content exceeds the available height.

## Code Example
```zig
fn characterType(char: u8) enum { literal, symbol, whitespace } {
	if (std.ascii.isAlphanumeric(char)) return .literal;
	if (!std.ascii.isAscii(char)) return .literal;
	if (char == '_') return .literal;
	if (std.ascii.isWhitespace(char)) return .whitespace;
	return .symbol;
}
```

## Related Questions
- How does the TextInput handle mouse button releases?
- What is the purpose of the `reloadText` function in TextInput?
- How does the cursor move when control modifier is pressed?
- What does the `characterType` function determine?
- How is text selection managed in TextInput?
- What ensures the cursor remains visible during operations?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_1*
