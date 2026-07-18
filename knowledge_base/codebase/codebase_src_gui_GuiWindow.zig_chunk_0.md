# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, window, pipeline, texture, shaders, rendering
**Symbols:** GuiWindow, GuiWindow.AttachmentPoint, GuiWindow.OrientationLine, GuiWindow.RelativePosition, GuiWindow.snapDistance, GuiWindow.titleBarHeight, GuiWindow.iconWidth, GuiWindow.pos, GuiWindow.size, GuiWindow.contentSize, GuiWindow.scale, GuiWindow.spacing, GuiWindow.relativePosition, GuiWindow.id, GuiWindow.rootComponent, GuiWindow.showTitleBar, GuiWindow.hasBackground, GuiWindow.hideIfMouseIsGrabbed, GuiWindow.closeIfMouseIsGrabbed, GuiWindow.closeable, GuiWindow.isHud, GuiWindow.titleBar, GuiWindow.shiftClickableInventory, GuiWindow.renderFn, GuiWindow.updateFn, GuiWindow.updateSelectedFn, GuiWindow.updateHoveredFn, GuiWindow.onOpenFn, GuiWindow.onCloseFn, GuiWindow.grabbedWindow, GuiWindow.windowMoving, GuiWindow.grabPosition, GuiWindow.selfPositionWhenGrabbed, GuiWindow.backgroundTexture, GuiWindow.titleTexture, GuiWindow.closeTexture, GuiWindow.zoomInTexture, GuiWindow.zoomOutTexture, GuiWindow.pipeline, GuiWindow.windowUniforms, GuiWindow.borderPipeline, GuiWindow.borderUniforms
**Concepts:** GUI window management, shader initialization, texture loading

## Summary
Defines the GuiWindow struct and its associated methods for managing GUI windows in the Cubyz engine.

## Explanation
The chunk defines the `GuiWindow` struct, which represents a window in the graphical user interface (GUI) of the Cubyz engine. It includes various fields such as position, size, content size, scale, and flags for visibility and interactivity. The struct also contains function pointers for rendering and updating the window's state. Additionally, it initializes and deinitializes global resources like pipelines and textures used for rendering windows.

## Code Example
```zig
pub fn globalInit() void {
	pipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/ui/button.vert",
		"assets/cubyz/shaders/ui/button.frag",
		"",
		&windowUniforms,
		graphics.draw.SimpleVertex2D,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.alphaBlending}},
	);
	borderPipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/ui/window_border.vert",
		"assets/cubyz/shaders/ui/window_border.frag",
		"",
		&borderUniforms,
		graphics.draw.SimpleVertex2D,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.alphaBlending}},
	);

	backgroundTexture = Texture.initFromFile("assets/cubyz/ui/window_background.png");
	titleTexture = Texture.initFromFile("assets/cubyz/ui/window_title.png");
	closeTexture = Texture.initFromFile("assets/cubyz/ui/window_close.png");
	zoomInTexture = Texture.initFromFile("assets/cubyz/ui/window_zoom_in.png");
	zoomOutTexture = Texture.initFromFile("assets/cubyz/ui/window_zoom_out.png");
}
```

## Related Questions
- What is the purpose of the `GuiWindow` struct?
- How are global resources like pipelines and textures initialized in this chunk?
- What fields does the `GuiWindow` struct contain?
- What function pointers are defined for the `GuiWindow` struct?
- How is the `globalInit` function used?
- What is the role of the `globalDeinit` function?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_0*
