# [medium/codebase_src_gui_components_Button.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, textures, shaders, mouse events, state management
**Symbols:** Button, Button.border, Button.fontSize, Button.Textures, Button.Textures.texture, Button.Textures.outlineTexture, Button.Textures.outlineTextureSize, Button.Textures.init, Button.Textures.deinit, Button.normalTextures, Button.hoveredTextures, Button.pressedTextures, Button.disabledTextures, Button.pipeline, Button.buttonUniforms, Button.pos, Button.size, Button.disabled, Button.pressed, Button.hovered, Button.onAction, Button.child, Button.globalInit, Button.globalDeinit, Button.defaultOnAction, Button.Options, Button.Options.onAction, Button.Options.disabled, Button.initText, Button.initIcon, Button.deinit, Button.toComponent, Button.updateHovered, Button.mainButtonPressed, Button.mainButtonReleased, Button.render
**Concepts:** GUI components, button states, texture rendering, mouse interactions

## Summary
Defines the Button component for GUI elements in Cubyz, handling initialization, deinitialization, and rendering.

## Explanation
The Button component is part of the GUI system in Cubyz. It manages button states (normal, hovered, pressed, disabled) and renders them using textures and shaders. The component supports both text and icon buttons. Initialization involves loading textures and setting up a graphics pipeline. Deinitialization releases resources. The update methods handle mouse interactions to change button state and trigger actions.

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
- How does the Button component initialize its textures?
- What is the purpose of the globalInit function in the Button component?
- How does the Button handle mouse button release events?
- What are the different states a Button can be in?
- How is the Button's pipeline initialized?
- What is the role of the Textures struct within the Button component?

*Source: unknown | chunk_id: codebase_src_gui_components_Button.zig_chunk_0*
