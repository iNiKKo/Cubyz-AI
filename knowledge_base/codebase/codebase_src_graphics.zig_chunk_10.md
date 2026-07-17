# [hard/codebase_src_graphics.zig] - Chunk 10

**Type:** implementation
**Keywords:** texture management, glyph loading, rendering pipeline, Vulkan initialization, OpenGL state setting
**Symbols:** RenderPass, RenderPass.renderPass, RenderPass.renderToWindow, init, deinit, resizeTexture, uploadData, getGlyph, drawGlyph, renderText
**Concepts:** text rendering, Vulkan render pass, FreeType, HarfBuzz, OpenGL textures

## Summary
Handles text rendering and Vulkan render pass initialization.

## Explanation
This chunk manages the lifecycle of text rendering components, including initializing and deinitializing FreeType, HarfBuzz, and OpenGL textures. It also handles the creation and destruction of Vulkan render passes based on configuration settings. The `getGlyph` function loads glyphs from a font face, uploads their bitmap data to a texture, and stores metadata about each glyph. The `drawGlyph` function sets up OpenGL uniforms and draws individual glyphs. The `renderText` function processes a string into a buffer and renders it at specified coordinates. Vulkan render passes are conditionally initialized based on the 'vulkanTestingMode' setting.

## Code Example
```zig
fn deinit() void {
	RenderPass.deinitRenderPasses();
	draw.deinitCircle();
	draw.deinitImage();
	draw.deinitLine();
	draw.deinitRect();
	draw.deinitRectBorder();
	TextRendering.deinit();
	block_texture.deinit();
	pipelines.deinit();
}
```

## Related Questions
- How does the `getGlyph` function handle glyph initialization?
- What is the purpose of the `resizeTexture` function in this code?
- How are Vulkan render passes conditionally initialized based on settings?
- What OpenGL uniforms are set by the `drawGlyph` function?
- How does the `renderText` function process and render text?
- What resources are deinitialized in the `deinit` function?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_10*
