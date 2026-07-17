# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 0

**Type:** api
**Keywords:** GUI, text input, scrollbar, callbacks, event handling, rendering, interaction
**Symbols:** TextInput, scrollBarWidth, border, fontSize, blinkDuration, texture, pos, size, pressed, obfuscated, cursor, selectionStart, currentString, textBuffer, maxWidth, maxHeight, textSize, scrollBar, callbacks, lastBlinkTime, showCusor, globalInit, globalDeinit, Callbacks, onNewline, onUp, onDown, onUpdate, init, deinit, clear, toComponent, updateHovered, mainButtonPressed, mainButtonReleased
**Concepts:** GUI component, text input handling, scrollbar integration, callback management

## Summary
The TextInput component handles text input with a graphical interface, including rendering, interaction, and managing callbacks.

## Explanation
This chunk defines the TextInput component for handling user text input within the GUI. It includes methods for initialization, deinitialization, updating, and interacting with the text input field. The component manages its own texture, position, size, and state such as cursor visibility and selection. It also interacts with a scrollbar if the text exceeds the visible area. Callbacks are provided for newline events and other user interactions.

## Code Example
```zig
pub fn globalInit() void {
	texture = Texture.initFromFile("assets/cubyz/ui/text_input.png");
}
```

## Related Questions
- What is the purpose of the TextInput component?
- How does the TextInput handle text input events?
- What methods are available for initializing and deinitializing the TextInput?
- How does the TextInput manage its scrollbar interaction?
- What callbacks are supported by the TextInput component?
- How does the TextInput update its state based on user interactions?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_0*
