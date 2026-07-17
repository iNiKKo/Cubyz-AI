# [hard/codebase_src_graphics.zig] - Chunk 7

**Type:** implementation
**Keywords:** allocator, fontUnitsPerPixel, characterIndex, lineBreaks, alignment, scaledMaxWidth, Vec2f, draw.rect, sentinel entries, word wrap logic, mouse position conversion, text buffer lifecycle, selection bounds assertion
**Symbols:** deinit, getLineOffset, mousePosToIndex, indexToCursorPos, calculateLineBreaks, drawSelection
**Concepts:** text layout, line breaking, word wrapping, mouse interaction, selection rendering

## Summary
Implements TextBuffer lifecycle and text layout: glyph data allocation, line-break calculation with word wrapping, mouse-to-index and index-to-position conversions, selection drawing, and deinitialization.

## Explanation
The chunk defines the TextBuffer struct (not shown here) and provides methods for its entire runtime lifecycle. In initLines it allocates self.glyphs from an allocator into a GlyphData array, then populates each glyph with x/y_advance/offset values derived from integer positions scaled by TextRendering.fontUnitsPerPixel, character codepoint/index/cluster from parser arrays via textIndexGuess mapping, and fontEffect. It calls self.initLines(true) followed by self.initLines(false), appends two sentinel lineBreaks entries at indices 0 and glyphs.len with width 0, then returns self. deinit frees the glyph array and calls self.lines.deinit() and self.lineBreaks.deinit(). getLineOffset computes a horizontal offset based on alignment (left=0, center=0.5, right=1) by multiplying (self.width - next line break width) with the factor; it is used internally by mousePosToIndex and drawSelection. mousePosToIndex translates a Vec2f mouse position into a u32 character index: it truncates y/16 to pick a line, clamps between 0 and self.lineBreaks.len-2, calls getLineOffset for that line to get x, then iterates glyphs in the line range [start,end) returning the first glyph whose characterIndex lies left of (x + glyph.x_advance/2), or if none, returns the last glyph’s index or bufferLen. indexToCursorPos walks lines (outer loop) and glyphs within each line, accumulating x from getLineOffset and subtracting glyph.y_advance per glyph to track y; when a glyph matches the requested characterIndex it returns {x,y}; after exhausting all lines it falls through returning the last computed position. calculateLineBreaks clears self.lineBreaks and appends an initial sentinel at index 0, then iterates glyphs: lineWidth accumulates x_advance; spaces set lastSpaceWidth/lastSpaceIndex; newlines append a line break with width reduced by spaceCharacterWidth (8) before resetting; if lineWidth exceeds scaledMaxWidth it attempts to wrap at the most recent space (removing that space from the current line and inserting a new break), otherwise wraps at the current glyph. After the loop self.width is set, a final sentinel is appended, and it returns a Vec2f of total width*fontSize/16 and height computed as fontSize times number of lines minus one. drawSelection asserts selectionStart <= selectionEnd, then walks to the start row (outer label) by scanning glyphs until characterIndex >= selectionStart; once found it enters an inner loop that draws 16px high rects for each glyph whose index is between selectionStart and selectionEnd, stopping when reaching selectionEnd or end of line. The chunk does not declare any new types here beyond using existing ones (GlyphData, Vec2f), but defines several public functions: deinit, getLineOffset, mousePosToIndex, indexToCursorPos, calculateLineBreaks, drawSelection, and implicitly initLines via self.initLines calls.

## Code Example
```zig
pub fn deinit(self: TextBuffer) void {
	self.lines.allocator.free(self.glyphs);
	self.lines.deinit();
	self.lineBreaks.deinit();
}
```

## Related Questions
- How does calculateLineBreaks handle wrapping at a space versus the current glyph when lineWidth exceeds scaledMaxWidth?
- What is the purpose of the sentinel lineBreak entries appended in initLines and why are their widths set to zero?
- Explain how mousePosToIndex uses getLineOffset to compute the starting x position for a given line before scanning glyphs.
- In indexToCursorPos, why does y decrease by glyph.y_advance inside each glyph loop and then increase by 16 after finishing a line?
- How does drawSelection determine the start row when selectionStart is not at the beginning of a line?
- Where are the glyphAdvance values (x_advance/y_advance) obtained from in initLines, and how are they scaled to f32?
- What happens internally if calculateLineBreaks encounters no spaces before exceeding scaledMaxWidth on a line?
- Describe the role of textIndexGuess in mapping parser arrays to glyphs during initialization.
- How does deinit ensure proper cleanup of both glyph data and the auxiliary line structures?
- Why is there an assertion selectionStart <= selectionEnd in drawSelection, and what would occur if it were violated?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_7*
