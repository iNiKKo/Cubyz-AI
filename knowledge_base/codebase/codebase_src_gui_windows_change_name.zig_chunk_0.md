# [easy/codebase_src_gui_windows_change_name.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, name validation, warning display, help text, input handling
**Symbols:** settings, Vec2f, GuiComponent, GuiWindow, window, textComponent, padding
**Concepts:** GUI, player name change, validation logic

## Summary
Handles window for changing player's name in GUI. Validates input length with strict character limits, displays warnings, and updates settings accordingly.

## Explanation
Manages a window for changing the player's name, validating input length against specific character limits (50 visible characters and 500 total characters), displaying warning messages when these limits are exceeded, updating settings, and handling GUI components. The `apply` function checks if the entered name exceeds the allowed lengths and logs an error message with exact counts. If valid, it updates the player's name in settings and saves changes. The window is closed after applying new name or showing a warning for existing names. On opening, the window displays help text about formatting options including markdown-like syntax for italic (`*italic*`), bold (`**bold**`), underlined (`__underlined__`), strike-through (`~~strike-through~~`), and color codes (e.g., `#ff0000red`, `#ff7700orange`, `#00ff00green`, `#0000ffblue`). Initial text content of `TextInput` component defaults to 'quanturmdoelvloper' if no previous name exists.

## Code Example
```zig
fn apply() void {
	if (textComponent.currentString.items.len > 500 or main.graphics.TextBuffer.Parser.countVisibleCharacters(textComponent.currentString.items) > 50) {
		std.log.err("Name is too long with {}/{} characters. Limits are 50/500", .{main.graphics.TextBuffer.Parser.countVisibleCharacters(textComponent.currentString.items), textComponent.currentString.items.len});
		return;
	}
	const oldName = settings.playerName;
	main.globalAllocator.free(settings.playerName);
	settings.playerName = main.globalAllocator.dupe(u8, textComponent.currentString.items);
	settings.save();
	gui.closeWindowFromRef(&window);
	if (oldName.len == 0) {
		gui.openWindow("main");
	}
}
```

## Related Questions
- What are the specific character limits for player's name input?
- How is the warning message displayed when the name exceeds character limits?
- What initial text content does the `TextInput` component have?

*Source: unknown | chunk_id: codebase_src_gui_windows_change_name.zig_chunk_0*
