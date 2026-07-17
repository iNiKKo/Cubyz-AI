# [hard/codebase_src_graphics.zig] - Chunk 8

**Type:** implementation
**Keywords:** TextBuffer, renderShadow, renderTextWithoutShadow, glyph texture binding, line wrapping, underline drawing, shadowColor, draw.setColor, main.stackAllocator
**Symbols:** render, renderTextWithoutShadow, renderShadow, shadowColor
**Concepts:** text rendering pipeline, glyph texture binding, line wrapping, underline drawing, shadow effect, OpenGL viewport uniforms, stack allocator usage

## Summary
This chunk implements the rendering pipeline for a TextBuffer struct, providing methods to draw text with optional shadow effects and underlines using OpenGL calls.

## Explanation
The chunk defines public functions render, renderTextWithoutShadow, and renderShadow on the TextBuffer type. render delegates to renderShadow (for a drop shadow) then renderTextWithoutShadow. renderTextWithoutShadow sets up translation/scale via draw.setTranslation/setScale with defer restores, binds the text rendering pipeline scissor, queries GL viewport uniforms, binds glyph texture 0, and uses draw.rectVao.bind(). It allocates lineWraps on main.stackAllocator (defer free). It iterates over self.lineBreaks.items to compute per-line offsets via getLineOffset, then loops glyphs in each line range; for non-newline glyphs it calls TextRendering.getGlyph with catch continue, then TextRendering.drawGlyph using glyph.x_offset/y_offset and fontEffect. After the glyph loop it records lineWraps[i] as x - getLineOffset(i), resets x to 0, increments y by 16. Then it iterates self.lines.items; for each Line it computes underline offset (15 if isUnderline else 8), saves/restores color via draw.setColor with alpha blending, and loops over lineWraps/j to compute visible segments using @max/@min on start/end indices, drawing rects where start < end. renderShadow mirrors this flow but applies shadowColor to glyph fontEffect.color and to the Line color before alpha blending; it also offsets translation by fontSize/16.0.

## Related Questions
- How does renderShadow compute the offset for its translation and scale?
- What is the purpose of lineWraps in renderTextWithoutShadow and how is it allocated?
- Which OpenGL call binds the glyph texture used by TextRendering.drawGlyph?
- Under what condition does renderTextWithoutShadow skip drawing a glyph?
- How are underline offsets calculated for Line structs with isUnderline set?
- What happens when TextRendering.getGlyph fails in renderTextWithoutShadow?
- How does shadowColor decide whether to return white or black?
- Where are draw.setColor and draw.restoreColor used within the text rendering flow?
- What role does getLineOffset play in positioning glyphs across multiple lines?
- Is there any clipping applied via TextRendering.pipeline.bind(draw.getScissor())?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_8*
