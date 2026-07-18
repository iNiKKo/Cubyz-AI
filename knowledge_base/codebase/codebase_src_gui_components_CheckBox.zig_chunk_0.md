# [easy/codebase_src_gui_components_CheckBox.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, checkbox, texture, label, interaction, rendering
**Symbols:** CheckBox, CheckBox.border, CheckBox.fontSize, CheckBox.boxSize, CheckBox.textureCheckedNormal, CheckBox.textureCheckedHovered, CheckBox.textureCheckedPressed, CheckBox.textureEmptyNormal, CheckBox.textureEmptyHovered, CheckBox.textureEmptyPressed, CheckBox.pos, CheckBox.size, CheckBox.state, CheckBox.pressed, CheckBox.hovered, CheckBox.onAction, CheckBox.label, globalInit, globalDeinit, init, deinit, toComponent, updateHovered, mainButtonPressed, mainButtonReleased, render
**Concepts:** GUI component, checkbox interaction, texture rendering, label management

## Summary
The CheckBox component handles rendering and interaction for a checkbox GUI element.

## Explanation
This chunk defines the CheckBox struct, which represents a checkbox in the GUI. It includes methods for initialization, deinitialization, updating hover state, handling button presses and releases, and rendering. The CheckBox uses textures to display different states (normal, hovered, pressed) of both checked and unchecked boxes. It also manages a label component that displays text alongside the checkbox. The globalInit and globalDeinit functions handle loading and unloading of textures used by all CheckBox instances.

## Code Example
```zig
pub fn globalInit() void {
	textureCheckedNormal = Texture.initFromFile("assets/cubyz/ui/checked_box.png");
	textureCheckedHovered = Texture.initFromFile("assets/cubyz/ui/checked_box_hovered.png");
	textureCheckedPressed = Texture.initFromFile("assets/cubyz/ui/checked_box_pressed.png");
	textureEmptyNormal = Texture.initFromFile("assets/cubyz/ui/box.png");
	textureEmptyHovered = Texture.initFromFile("assets/cubyz/ui/box_hovered.png");
	textureEmptyPressed = Texture.initFromFile("assets/cubyz/ui/box_pressed.png");
}
```

## Related Questions
- What is the purpose of the globalInit function in the CheckBox component?
- How does the CheckBox handle different states (checked, unchecked) during rendering?
- What method is used to initialize a new CheckBox instance?
- How does the CheckBox manage its label component?
- What textures are loaded by the globalInit function and what do they represent?
- How does the CheckBox respond to mouse button presses and releases?

*Source: unknown | chunk_id: codebase_src_gui_components_CheckBox.zig_chunk_0*
