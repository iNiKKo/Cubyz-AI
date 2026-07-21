# [medium/codebase_src_gui_components_Button.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, button, texture, shader, interaction, state management
**Symbols:** Button, Button.border, Button.fontSize, Button.Textures, Button.Textures.texture, Button.Textures.outlineTexture, Button.Textures.outlineTextureSize, Button.Textures.init, Button.Textures.deinit, Button.normalTextures, Button.hoveredTextures, Button.pressedTextures, Button.disabledTextures, Button.pipeline, Button.buttonUniforms, Button.pos, Button.size, Button.disabled, Button.pressed, Button.hovered, Button.onAction, Button.child, Button.globalInit, Button.globalDeinit, Button.defaultOnAction, Button.Options, Button.Options.onAction, Button.Options.disabled, Button.initText, Button.initIcon, Button.deinit, Button.toComponent, Button.updateHovered, Button.mainButtonPressed, Button.mainButtonReleased
**Concepts:** GUI components, button interaction, texture management, shader initialization

## Summary
Defines the Button component for GUI elements in Cubyz, handling initialization, rendering, and interaction logic.

## Explanation
The Button component is part of the GUI system in Cubyz, handling initialization, rendering, and interaction logic. The button has a border size of 3 units and uses textures for different states (normal, hovered, pressed, disabled). The `globalInit` function initializes shared resources like shaders and textures for these states. The `initText` and `initIcon` functions create buttons with text or icon labels. The component handles mouse events to update its state and trigger actions when clicked.

The `buttonUniforms` struct contains uniform locations for rendering, including screen, start, size, color, and scale. Memory management for Button instances is handled by the global allocator, which creates and destroys button objects as needed.

Textures are initialized using the `init` method of the `Textures` struct, which loads textures from specified file paths and stores their sizes. The `deinit` method releases these resources when they are no longer needed.

## Code Example
```zig
pub fn globalInit() void {
	pipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/ui/button.vert",
		"assets/cubyz/shaders/ui/button.frag",
		"",
		&buttonUniforms,
		graphics.draw.SimpleVertex2D,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.alphaBlending}},
	);
	normalTextures = Textures.init("assets/cubyz/ui/button");
	hoveredTextures = Textures.init("assets/cubyz/ui/button_hovered");
	pressedTextures = Textures.init("assets/cubyz/ui/button_pressed");
	disabledTextures = Textures.init("assets/cubyz/ui/button_disabled");
}
```

## Related Questions
- What is the purpose of the `globalInit` function in the Button component?
- How are textures initialized for different button states?
- What does the `initText` function do and what parameters does it take?
- How does the Button handle mouse events like pressing and releasing?
- What is the role of the `buttonUniforms` struct in rendering?
- How is memory managed for Button instances in Cubyz?
- What are the different states a Button can be in, and how are they represented?
- How does the Button component interact with other GUI components?
- What is the significance of the `pipeline` variable in the Button component?
- How is the `onAction` callback triggered in the Button component?

*Source: unknown | chunk_id: codebase_src_gui_components_Button.zig_chunk_0*
