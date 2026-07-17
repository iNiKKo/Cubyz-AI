# [easy/codebase_src_gui_components_CheckBox.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiComponent, Texture.initFromFile, globalAllocator, onAction callback, mouse hover detection, scissor clipping, custom shaded rectangle, label positioning, state machine
**Symbols:** CheckBox, border, fontSize, boxSize, textureCheckedNormal, textureCheckedHovered, textureCheckedPressed, textureEmptyNormal, textureEmptyHovered, textureEmptyPressed, pos, size, state, pressed, hovered, onAction, label, globalInit, globalDeinit, init, deinit, toComponent, updateHovered, mainButtonPressed, mainButtonReleased, render
**Concepts:** GUI component, checkbox state machine, texture atlas binding, mouse hover detection, callback invocation, scissor clipping, custom shaded rectangle rendering, label positioning, memory allocation

## Summary
Implements the CheckBox GUI component with state management (pressed/hovered), texture binding for checked/unchecked states, and rendering via a custom shaded rectangle.

## Explanation
The CheckBox struct is defined as a public type extending GuiComponent. It holds position and size fields, a boolean state indicating whether it is checked, pressed and hovered flags, an onAction callback pointer, and a label pointer. Initialization loads textures for both checked and unchecked states (normal, hovered, pressed) via globalInit() which reads from assets/cubyz/ui/. Deinitialization frees all loaded textures and destroys the CheckBox instance using main.globalAllocator. The init function creates a Label with left alignment, allocates memory for the CheckBox, sets its size to accommodate the label plus borders, and stores the provided onAction callback. Hover detection is handled by updateHovered which sets hovered=true and returns .handled. Press handling uses mainButtonPressed to set pressed=true. Release logic in mainButtonReleased checks if pressed was true; if so it resets pressed, then toggles state only when the mouse position is within the CheckBox bounds (using GuiComponent.contains) and hovered is true, invoking onAction with the new state. Rendering branches based on state: for checked boxes it binds textureCheckedNormal/Pressed/Hovered, for unchecked boxes it binds textureEmptyNormal/Pressed/Hovered; after binding textures it calls Button.pipeline.bind(draw.getScissor()) to set scissor clipping, then draws a custom shaded rectangle at self.pos with height offset by boxSize/2 and width boxSize. The label position is computed relative to the checkbox bounds and rendered via self.label.render(mousePosition - textPos). All fields are mutable except onAction which is const; no additional public methods beyond the ones listed.

## Related Questions
- What textures are loaded for the checked state of a CheckBox?
- How does the CheckBox determine whether to toggle its state on release?
- Which function is responsible for freeing resources allocated by CheckBox.init?
- What happens when updateHovered is called with an out-of-bounds mouse position?
- Does mainButtonReleased invoke onAction if the checkbox is unchecked?
- How does render handle the case where state is false and pressed is true?
- What value does toComponent return for a CheckBox instance?
- Is the label always rendered inside the custom shaded rectangle bounds?
- Where are the texture files located relative to the project root?
- Can onAction be null when creating a CheckBox via init?

*Source: unknown | chunk_id: codebase_src_gui_components_CheckBox.zig_chunk_0*
