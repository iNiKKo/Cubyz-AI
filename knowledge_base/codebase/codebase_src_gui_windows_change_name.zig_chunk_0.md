# [easy/codebase_src_gui_windows_change_name.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, text input, button click, string validation, window lifecycle
**Symbols:** window, textComponent, padding, apply, onOpen, onClose
**Concepts:** GUI window management, player settings, input validation, UI component initialization

## Summary
Handles the logic for a GUI window that allows changing the player's name, including input validation and UI component management.

## Explanation
This chunk defines a GUI window for changing the player's name. It includes functions to apply the new name with validation checks, initialize the window components on open, and deinitialize them on close. The window contains labels for instructions, a text input field for entering the name, and an apply button. It also handles UI layout and updates.

## Code Example
```zig
pub fn onOpen() void {
	const list = VerticalList.init(.{padding, 16 + padding}, 300, 16);
	const width = 420;
	if (settings.playerName.len == 0) {
		list.add(Label.init(.{0, 0}, width, "Please enter your name!", .center));
		window.closeable = false;
	} else {
		list.add(Label.init(.{0, 0}, width, "#ff0000Warning: #ffff00__For worlds from versions 0.1.0 and earlier__. #ffffffYou may lose access to your inventory data when changing the name!", .center));
		window.closeable = true;
	}
	list.add(Label.init(.{0, 0}, width, "Cubyz supports formatting your username using a markdown-like syntax:", .center));
	list.add(Label.init(.{0, 0}, width, "\\**italic*\\* \\*\\***bold**\\*\\* \\_\\___underlined__\\_\\_ \\~\\~~~strike-through~~\\~\\~", .center));
	list.add(Label.init(.{0, 0}, width, "Even colors are possible, using the hexadecimal color code:", .center));
	list.add(Label.init(.{0, 0}, width, "\\##ff0000ff#ffffff00#ffffff00#ff0000red#ffffff \\##ff0000ff#00770077#ffffff00#ff7700orange#ffffff \\##ffffff00#00ff00ff#ffffff00#00ff00green#ffffff \\##ffffff00#ffffff00#0000ffff#0000ffblue", .center));
	textComponent = TextInput.init(.{0, 0}, width, 32, if (settings.playerName.len == 0) "quanturmdoelvloper" else settings.playerName, .{.onNewline = .init(apply)});
	list.add(textComponent);
	list.add(Button.initText(.{0, 0}, 100, "Apply", .{.onAction = .init(apply)}));
	list.finish(.center);
	window.rootComponent = list.toComponent();
	window.contentSize = window.rootComponent.?.pos() + window.rootComponent.?.size() + @as(Vec2f, @splat(padding));
	gui.updateWindowPositions();
}
```

## Related Questions
- What is the purpose of the `apply` function?
- How does the window handle input validation for the player's name?
- What components are added to the GUI window when it opens?
- What happens if the player's current name is empty when opening the window?
- How is the layout of the GUI window managed?
- What steps are taken when the window is closed?

*Source: unknown | chunk_id: codebase_src_gui_windows_change_name.zig_chunk_0*
