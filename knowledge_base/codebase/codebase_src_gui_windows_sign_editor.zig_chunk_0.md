# [easy/codebase_src_gui_windows_sign_editor.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, text input, button click, window open/close, data update
**Symbols:** window, textComponent, padding, pos, oldText, deinit, openFromSignData, apply, onOpen, onClose
**Concepts:** GUI window management, sign text editing, user input handling, window lifecycle

## Summary
Handles the logic for a GUI window used to edit sign text in the Cubyz voxel engine.

## Explanation
This chunk defines the behavior and structure of a GUI window specifically designed for editing sign text. It includes functions for opening and closing the window, applying changes to the sign's text, and handling user input through components like TextInput and Button. The window has a content size of (128, 256) pixels and padding of 8 pixels. The `openFromSignData` function initializes the window with specific position and oldText data. The `apply` function checks if the text length is within limits (visibleCharacterCount <= 100 and total characters <= 500), updates sign text, and closes the game menu. The `onOpen` function sets up GUI components including a TextInput for editing text and a Button to apply changes. Memory management includes freeing oldText in the `deinit` function.

## Code Example
```zig
pub fn deinit() void {
	main.globalAllocator.free(oldText);
	oldText = &.{};
}
```

## Related Questions
- How does the `openFromSignData` function initialize the sign editor window with specific position and oldText data?
- What is the purpose of the `apply` function, including its text length constraints (visibleCharacterCount <= 100 and total characters <= 500)?
- How does the `onOpen` function set up the GUI components for the sign editor, including TextInput and Button?
- What happens when the user clicks the 'Apply' button in the sign editor, updating the sign text and closing the game menu?
- How is memory managed in this chunk, particularly with the `deinit` function freeing oldText?

*Source: unknown | chunk_id: codebase_src_gui_windows_sign_editor.zig_chunk_0*
