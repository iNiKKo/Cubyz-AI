# [hard/codebase_src_gui_components_TextInput.zig] - Chunk 0

**Type:** api
**Keywords:** GUI component, text input, scrollbar, callbacks, event handling, rendering
**Symbols:** TextInput, scrollBarWidth, border, fontSize, blinkDuration, texture, pos, size, pressed, obfuscated, cursor, selectionStart, currentString, textBuffer, maxWidth, maxHeight, textSize, scrollBar, callbacks, lastBlinkTime, showCusor, globalInit, globalDeinit, Callbacks, onNewline, onUp, onDown, onUpdate, init, deinit, clear, toComponent, updateHovered, mainButtonPressed
**Concepts:** GUI components, text input handling, scrollbar integration, callback system

## Summary
The TextInput component handles user input and rendering of text fields in the GUI.

## Explanation
The TextInput component handles user input and rendering of text fields in the GUI. It includes methods for initialization, deinitialization, updating, and rendering. The TextInput manages its own texture, position, size, cursor state, and text buffer. It also interacts with a scrollbar for managing overflow text. The component supports callbacks for newline events and updates the display based on user interactions.

### Constants:
- `scrollBarWidth`: 5 (width of the scrollbar)
- `border`: 3 (padding around the input field)
- `fontSize`: 16 (font size used in the text buffer)
- `blinkDuration`: .fromMilliseconds(500) (duration for cursor blinking)

### Fields:
- `texture`: Texture initialized from a file.
- `pos`: Position of the TextInput component.
- `size`: Size of the TextInput component.
- `pressed`: Boolean indicating if the input field is pressed.
- `obfuscated`: Boolean indicating if text should be obfuscated.
- `cursor`: Optional cursor position in the current string.
- `selectionStart`: Optional starting point for selection.
- `currentString`: List of characters managed by the TextInput.
- `textBuffer`: Text buffer initialized with a given text and alignment options.
- `maxWidth`: Maximum width allowed for the input field.
- `maxHeight`: Maximum height allowed for the input field.
- `textSize`: Calculated size based on font size and maximum width.
- `scrollBar`: Scrollbar component integrated into TextInput.
- `callbacks`: Callbacks for handling various events (onNewline, onUp, onDown, onUpdate).
- `lastBlinkTime`: Timestamp of the last blink event.
- `showCursor`: Boolean indicating if the cursor should be shown.

### Methods:
- **globalInit()**: Initializes the texture from a file.
- **globalDeinit()**: Deinitializes and releases resources for the texture.
- **Callbacks struct**: Contains callbacks for newline, up, down, and update events.
- **init(pos: Vec2f, maxWidth: f32, maxHeight: f32, text: []const u8, callbacks: Callbacks)**: Initializes a new TextInput instance with given parameters.
- **deinit(self: *const TextInput)**: Deinitializes the TextInput and releases resources.
- **clear(self: *TextInput)**: Clears the current string and resets cursor position.
- **toComponent(self: *TextInput)**: Converts TextInput to a GuiComponent for rendering.
- **updateHovered(self: *TextInput, mousePosition: Vec2f)**: Updates hover state based on mouse position.
- **mainButtonPressed(self: *TextInput, mousePosition: Vec2f)**: Handles main button press events and updates cursor position.

## Code Example
```zig
pub fn globalInit() void {
	texture = Texture.initFromFile("assets/cubyz/ui/text_input.png");
}
```

## Related Questions
- What are the specific numeric constants used in TextInput?
- How is the texture initialized for TextInput?
- What methods are available for initializing and deinitializing the TextInput?
- How does the TextInput manage overflow text using a scrollbar?
- What callbacks are supported by the TextInput and what do they handle?
- How is the cursor position managed within the TextInput?

*Source: unknown | chunk_id: codebase_src_gui_components_TextInput.zig_chunk_0*
