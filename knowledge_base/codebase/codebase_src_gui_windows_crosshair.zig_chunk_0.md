# [easy/codebase_src_gui_windows_crosshair.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI, crosshair, texture, pipeline, shaders, blending
**Symbols:** size, window, texture, pipeline, uniforms, init, deinit, render
**Concepts:** GUI window, crosshair rendering, texture loading, graphics pipeline

## Summary
This chunk initializes and manages a GUI window for displaying a crosshair in the game.

## Explanation
This chunk initializes and manages a GUI window for displaying a crosshair in the game. The code defines a `GuiWindow` with specified dimensions (`64x64`) and properties such as no title bar, background, or closeability. It includes initialization functions to set up resources like a texture from an image file (`assets/cubyz/ui/hud/crosshair.png`) and a graphics pipeline configured with specific shaders (`Image.vert`, `Image.frag`), blending settings (subtractive color blend mode), and culling mode (none). The crosshair is rendered using the defined texture and pipeline, and resources are cleaned up in the deinitialization function.

## Code Example
```zig
pub fn deinit() void {
	pipeline.deinit();
	texture.deinit();
}
```

## Related Questions
- What is the size of the crosshair window?
- How is the crosshair texture initialized?
- What shaders are used for rendering the crosshair?
- What blending settings are applied to the crosshair?
- What resources are deinitialized in the `deinit` function?

*Source: unknown | chunk_id: codebase_src_gui_windows_crosshair.zig_chunk_0*
