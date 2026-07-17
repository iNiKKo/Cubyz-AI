# [easy/codebase_src_gui_windows_sign_editor.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, TextInput, VerticalList, deinit, openFromSignData, apply, onOpen, onClose, mouse grab, text buffer parser
**Symbols:** window, textComponent, padding, pos, oldText, deinit, openFromSignData, apply, onOpen, onClose
**Concepts:** GUI window management, sign editing interface, vertical list layout, input validation, block entity text update

## Summary
This chunk defines the GUI window for editing signs, including its initialization, deinitialization, and event handlers for opening from sign data and applying changes.

## Explanation
The chunk declares a public GuiWindow instance named 'window' with specific content size and mouse grab settings. It imports several components: Button, Label, TextInput, VerticalList, and the main module's Vec2f type. The window is initialized in the 'onOpen' function where it creates a VerticalList containing a TextInput (initialized with oldText) and an Apply button; both TextInput and the button share the same apply closure that validates text length limits before updating the block entity via main.block_entity.BlockEntityTypes.@

## Code Example
```zig
pub fn deinit() void {
	main.globalAllocator.free(oldText);
	oldText = &.{};
}
```

## Related Questions
- What is the content size of the sign editor window?
- How does the apply function validate text length limits?
- Which components are added to the VerticalList in onOpen?
- What happens when a sign is opened from existing data via openFromSignData?
- Where is oldText allocated and freed during the window lifecycle?
- Does the Apply button share its action with the TextInput's newline handler?
- How does deinit ensure no memory leaks occur after closing the window?

*Source: unknown | chunk_id: codebase_src_gui_windows_sign_editor.zig_chunk_0*
