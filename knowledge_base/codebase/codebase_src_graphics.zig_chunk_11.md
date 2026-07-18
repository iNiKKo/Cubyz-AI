# [hard/codebase_src_graphics.zig] - Chunk 11

**Type:** implementation
**Keywords:** FreeType, HarfBuzz, shaders, textures, font effects, glyph storage, texture resizing, bitmap upload, glyph retrieval, text drawing
**Symbols:** TextRendering, TextRendering.Glyph, TextRendering.pipeline, TextRendering.uniforms, TextRendering.freetypeLib, TextRendering.freetypeFace, TextRendering.harfbuzzFace, TextRendering.harfbuzzFont, TextRendering.glyphMapping, TextRendering.glyphData, TextRendering.glyphTexture, TextRendering.textureWidth, TextRendering.textureHeight, TextRendering.textureOffset, TextRendering.fontUnitsPerPixel, TextRendering.ftError, TextRendering.init, TextRendering.deinit, TextRendering.resizeTexture, TextRendering.uploadData, TextRendering.getGlyph, TextRendering.drawGlyph, TextRendering.renderText
**Concepts:** text rendering, font management, glyph rendering

## Summary
Handles text rendering using FreeType and HarfBuzz for font management and glyph rendering.

## Explanation
The TextRendering struct manages the initialization and deinitialization of text rendering resources, including shaders, textures, and font libraries. It initializes a graphics pipeline with specific shaders and sets up texture parameters. The init function loads a font face, creates HarfBuzz objects, and initializes glyph storage. The resizeTexture function adjusts the texture size when needed, copying existing data to a new texture. The uploadData function uploads bitmap data to the texture. The getGlyph function retrieves or loads a glyph's information, rendering it if necessary. The drawGlyph function draws a single glyph at specified coordinates with optional font effects. The renderText function processes and renders a string of text using these components.

## Code Example
```zig
fn ftError(errorCode: c.FT_Error) !void {
	if (errorCode == 0) return;
	const errorString = c.FT_Error_String(errorCode);
	std.log.err("Got freetype error {s}", .{errorString});
	return error.freetype;
}
```

## Related Questions
- What is the purpose of the TextRendering struct?
- How does the init function initialize the text rendering pipeline?
- What happens if an error occurs during font loading in the init function?
- How does the resizeTexture function handle texture resizing?
- What data does the uploadData function upload to the texture?
- How is a glyph retrieved or loaded using the getGlyph function?
- What are the parameters for drawing a single glyph with drawGlyph?
- How does the renderText function process and render a string of text?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_11*
