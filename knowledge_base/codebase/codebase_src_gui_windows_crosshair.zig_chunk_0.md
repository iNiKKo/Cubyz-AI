# [easy/codebase_src_gui_windows_crosshair.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, Texture, Pipeline, uniforms, init, deinit, render, graphics.draw, assets, HUD, c_int, SimpleVertex2D, blend factors, scissor, custom shaded image
**Symbols:** c_int, GuiWindow, GuiComponent, Texture, Vec2f, Pipeline, SimpleVertex2D, screen, start, size, color, uvOffset, uvDim, window, textures, pipeline, uniforms, init, deinit, render
**Concepts:** HUD window setup, graphics pipeline initialization, texture loading from assets, custom shaded image rendering, blend factor configuration, scissor region handling

## Summary
This chunk defines the crosshair GUI window: it sets up a fixed‑size HUD window with no title bar or background, initializes a graphics pipeline and texture from asset files, and provides render logic that binds the texture and draws a custom shaded image using uniform offsets.

## Explanation
The chunk declares several top-level constants and variables. It imports std, main.graphics (aliased as graphics), main.vec.Vec2f, c, and ../gui.zig (aliased as gui). From these it pulls GuiWindow, GuiComponent, Texture, Vec2f, Pipeline, draw.SimpleVertex2D, and the C type c_int. A constant size is set to 64 f32. A pub var window of type GuiWindow is initialized with contentSize = Vec2f{size, size}, showTitleBar = false, hasBackground = false, isHud = true, hideIfMouseIsGrabbed = false, and closeable = false. An unexported texture variable of type Texture is left undefined. An unexported pipeline variable of type graphics.Pipeline is left undefined. A pub var uniforms struct is defined with fields screen: c_int, start: c_int, size: c_int, color: c_int, uvOffset: c_int, uvDim: c_int, all initially undefined. The init function creates a Pipeline by calling graphics.Pipeline.init with shader paths for Image.vert and Image.frag, an empty vertex fragment string, the uniforms pointer, SimpleVertex2D as the draw mode, an empty array of vertex attributes, and attachment flags that set color blend factors to one with subtract blending on both channels and alpha blend op subtract. It then initializes texture from assets/cubyz/ui/hud/crosshair.png. The deinit function calls pipeline.deinit() and texture.deinit(). The render function binds the texture at slot 0, sets the scissor via graphics.draw.getScissor(), and draws a custom shaded image using graphics.draw.customShadedImage with uniforms and origin (0,0) and size (size,size).

## Related Questions
- What is the size of the crosshair window and how is it configured?
- How are the uniforms for the custom shaded image defined in this chunk?
- What shader files does the pipeline load from assets/cubyz/shaders/graphics/
- Which blend factors are set when initializing the graphics pipeline here?
- Does this chunk provide any deinitialization logic, and what resources does it clean up?
- How is the texture bound for rendering in the render function of this window?
- What draw mode is used by SimpleVertex2D in the pipeline initialization call?
- Are there any GUI component references exposed publicly from this file?
- Is the crosshair window marked as a HUD and what does that imply about its visibility?
- How are the uvOffset and uvDim fields of uniforms intended to be used?
- What is the origin point passed to customShadedImage in render?
- Does this chunk import any other GUI-related types besides GuiWindow and GuiComponent?

*Source: unknown | chunk_id: codebase_src_gui_windows_crosshair.zig_chunk_0*
