# [hard/codebase_src_graphics.zig] - Chunk 4

**Type:** api
**Keywords:** GL_TRIANGLE_STRIP, uniforms, viewport, alignment, FontEffect, underline, strikethrough, glyphs, lineBreaks, TextBuffer
**Symbols:** drawSlice, customShadedImage, customShadedRect, text, print, TextBuffer, Alignment, FontEffect, Line, LineBreak, GlyphData, addLine, initLines
**Concepts:** OpenGL rendering, uniform binding, text layout, glyph buffering, line breaking, font effects, UV mapping

## Summary
This chunk defines the graphics rendering API, providing functions to draw textured slices with UV mapping and custom-shaded rectangles/text using OpenGL uniforms. It also implements a text buffer system for layouting glyphs into lines with support for alignment, font effects (color, bold, italic), underline/strikethrough detection, and line breaking.

## Explanation
The chunk declares several public functions: drawSlice is invoked multiple times to render textured slices; customShadedImage and customShadedRect both set up OpenGL uniforms (screen viewport, start position, size, color) and bind rectVAO before drawing a GL_TRIANGLE_STRIP. The text function delegates to TextRendering.renderText with an empty struct literal. print allocates a formatted string via std.fmt.allocPrint using main.stackAllocator, then calls text; it is marked inline so the allocation happens at compile time. TextBuffer is defined as a public struct containing Alignment enum (left/center/right), FontEffect packed struct with fields color, bold, italic, underline, strikethrough and a hasLine method that returns true for underline or strikethrough depending on the argument; Line struct holds start/end positions, color, and isUnderline flag; LineBreak struct stores index and width; GlyphData struct contains x_advance, y_advance, x_offset, y_offset, character (u21), index, cluster, fontEffect, and characterIndex. The TextBuffer fields include alignment, width, buffer pointer to c.hb_buffer_t, glyphs slice, lines list managed by main.ListManaged(Line), and lineBreaks list managed similarly. addLine appends a Line only if its start != end; initLines iterates over self.glyphs, maintaining lastFontEffect state, using hasLine to decide when to finalize the current line or create a new one with updated color.

## Related Questions
- What OpenGL primitive is used by customShadedImage and customShadedRect?
- How does the print function handle memory allocation for formatted strings?
- Which TextBuffer field holds a pointer to an hb_buffer_t object?
- Under what condition does addLine append a Line to self.lines?
- What enum values are available for TextBuffer.Alignment?
- Does FontEffect store bold and italic as separate boolean fields?
- How is the hasLine method parameterized in FontEffect?
- Which struct contains x_advance, y_advance, character, and fontEffect fields?
- Is rectVAO bound before drawing in customShadedRect?
- What does initLines iterate over to process glyphs?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_4*
