# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 0

**Type:** api
**Keywords:** GUI component, text input, scrollbar, callbacks, event handling, rendering
**Symbols:** TextInput, scrollBarWidth, border, fontSize, blinkDuration, texture, pos, size, pressed, obfuscated, cursor, selectionStart, currentString, textBuffer, maxWidth, maxHeight, textSize, scrollBar, callbacks, lastBlinkTime, showCusor, globalInit, globalDeinit, Callbacks, onNewline, onUp, onDown, onUpdate, init, deinit, clear, toComponent, updateHovered, mainButtonPressed
**Concepts:** GUI components, text input handling, scrollbar integration, callback system

## Summary
The TextInput component handles user input and rendering of text fields in the GUI.

## Explanation
This chunk defines the TextInput struct, which is a GUI component for handling text input. It includes methods for initialization, deinitialization, updating, and rendering. The TextInput manages its own texture, position, size, cursor state, and text buffer. It also interacts with a scrollbar for managing overflow text. The component supports callbacks for newline events and updates the display based on user interactions.

## Code Example
```zig
pub fn globalInit() void {
	texture = Texture.initFromFile("assets/cubyz/ui/text_input.png");
}
```

## Related Questions
- What is the purpose of the TextInput component?
- How does the TextInput handle text overflow?
- What callbacks are supported by the TextInput?
- How is the cursor position managed in the TextInput?
- What methods are available for initializing and deinitializing the TextInput?
- How does the TextInput update its display based on user interactions?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_0*
