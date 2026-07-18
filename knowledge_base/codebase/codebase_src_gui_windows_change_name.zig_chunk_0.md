# [easy/codebase_src_gui_windows_change_name.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, name validation, warning display, help text, input handling
**Symbols:** settings, Vec2f, GuiComponent, GuiWindow, window, textComponent, padding
**Concepts:** GUI, player name change, validation logic

## Summary
Handles window for changing player name in GUI

## Explanation
Manages a window for changing the player's name, validating input length and updating settings. Includes logic for displaying warnings and help text.

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
- What is the purpose of the `apply` function in this chunk?
- How does the `apply` function validate the player's name input?
- What happens if the player's name exceeds the character limit?
- Where is the warning message displayed when the name is too long?
- What is the initial text content of the `TextInput` component?
- How is the `GuiWindow` initialized in this chunk?
- What is the purpose of the `onOpen` function?
- What components are added to the `VerticalList` in the `onOpen` function?
- What is the purpose of the `onClose` function?
- How does the `onClose` function handle the `GuiWindow`'s root component?
- What is the purpose of the `apply` function's error logging statement?
- Where is the player's name stored in the settings?

*Source: unknown | chunk_id: codebase_src_gui_windows_change_name.zig_chunk_0*
