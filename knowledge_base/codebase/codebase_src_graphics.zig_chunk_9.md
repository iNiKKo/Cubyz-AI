# [hard/codebase_src_graphics.zig] - Chunk 9

**Type:** implementation
**Keywords:** text atlas, FreeType, Harfbuzz, font rendering, GPU texture upload, line wrapping, underline drawing, shadow color blending, uniform binding, texture resizing, data buffer handling, defer cleanup
**Symbols:** TextRendering, TextRendering.Glyph, TextRendering.pipeline, TextRendering.uniforms, TextRendering.freetypeLib, TextRendering.freetypeFace, TextRendering.harfbuzzFace, TextRendering.harfbuzzFont, TextRendering.glyphMapping, TextRendering.glyphData, TextRendering.glyphTexture, TextRendering.textureWidth, TextRendering.textureHeight, TextRendering.textureOffset, TextRendering.fontUnitsPerPixel, TextRendering.ftError, TextRendering.init, TextRendering.deinit, TextRendering.resizeTexture, TextRendering.uploadData
**Concepts:** text atlas management, font rendering pipeline, FreeType integration, Harfbuzz shaping, GPU texture upload, line wrapping, underline drawing, shadow color blending, uniform binding, texture resizing, data buffer handling, defer cleanup

## Summary
Text rendering pipeline: glyph atlas management with FreeType/Harfbuzz, font effect shadowing, line wrapping and underline drawing via GPU rects.

## Explanation
The chunk defines TextRendering as a struct containing static state for the text system. It holds a Pipeline (initialized from shaders), uniforms for texture bounds/rects/font effects, FreeType library/face, Harfbuzz face/font pointers, glyphMapping and glyphData lists, and two GPU textures used as an atlas. The init function creates the pipeline with SimpleVertex2D, binds null, sets font size uniform, initializes FreeType (FT_Init_FreeType), loads a font file (unscii-16-full.ttf) via FT_New_Face, configures pixel sizes (0, textureHeight), creates Harfbuzz face from FreeType face, builds Harfbuzz font, computes fontUnitsPerPixel. It then allocates glyphMapping and glyphData lists, reserves entry 0 as undefined, generates two GL_TEXTURE_2D objects, binds the first for upload (GL_RED single-channel) with nearest filtering and repeat wrapping, sets up the second texture identically. resizeTexture swaps the atlas textures, rebinds to the new primary slot, reallocates the primary texture at double width while keeping height constant, copies remaining data from the old secondary texture into the new primary via glCopyImageSubData (offsetting by textureOffset), and updates the fontSize uniform. uploadData reads a FreeType bitmap, extracts width/height, uses the buffer if present; if the offset plus width exceeds current textureWidth it calls resizeTexture to grow the atlas. The chunk also contains drawing logic: after computing line wraps (x offsets) it iterates self.lines.items, sets shadow color via draw.setColor with alpha 0xff000000, defers restoreColor, then for each wrapped segment draws a rect at start/end positions using draw.rect. All operations are synchronous and use the global allocator for lists; no concurrency is present.

## Related Questions
- How does TextRendering resize its glyph atlas when new characters exceed current texture width?
- What happens to the secondary texture slot during a resizeTexture call and why is it swapped?
- Why are both GL_TEXTURE_MIN_FILTER and GL_TEXTURE_MAG_FILTER set to GL_NEAREST in init?
- How is the shadow color applied to glyphs before drawing them with TextRendering.drawGlyph?
- Which FreeType error handling strategy does ftError use when FT_Init_FreeType fails?
- What is the purpose of reserving glyphData entry 0 as undefined during initialization?
- How does uploadData decide whether to resize or directly upload a bitmap buffer?
- Does deinit call FT_Done_FreeType and how are Harfbuzz resources cleaned up?
- Are any operations in this chunk performed asynchronously or using threads?
- What is the role of draw.setColor with alpha 0xff000000 in the line drawing loop?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_9*
