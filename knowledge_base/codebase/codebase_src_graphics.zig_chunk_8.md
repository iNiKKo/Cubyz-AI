# [hard/codebase_src_graphics.zig] - Chunk 8

**Type:** implementation
**Keywords:** Harfbuzz, text shaping, mouse position, character index, cursor position, line breaks
**Symbols:** TextBuffer, TextBuffer.showControlCharacters, TextBuffer.parse, TextBuffer.deinit, TextBuffer.getLineOffset, TextBuffer.mousePosToIndex, TextBuffer.indexToCursorPos, TextBuffer.calculateLineBreaks
**Concepts:** text rendering, text interaction, line breaking, glyph handling

## Summary
Handles text parsing, rendering, and interaction logic.

## Explanation
This chunk implements the TextBuffer struct, which manages text rendering and interaction. It includes methods for initializing text buffers from parsed text, deinitializing resources, converting mouse positions to character indices, and calculating cursor positions. The code uses Harfbuzz for shaping text and handles line breaks based on font size and maximum line width.

The `parse` method initializes the parser, sets up Harfbuzz buffer, adds UTF-32 characters, sets direction, script, language, shapes the text, retrieves glyph information and positions, guesses text indices from cluster indices, merges it all together into glyphs, finds lines, and appends line breaks.

The `deinit` method frees allocated resources for glyphs, lines, and line breaks.

The `getLineOffset` method calculates the offset based on alignment and width differences.

The `mousePosToIndex` method converts mouse positions to character indices by iterating through glyphs and checking mouse position relative to glyph advance.

The `indexToCursorPos` method calculates cursor positions by iterating through glyphs and finding the position of a specific character index.

The `calculateLineBreaks` method calculates line breaks based on font size, maximum line width, and handling spaces and newlines.

## Code Example
```zig
pub fn deinit(self: TextBuffer) void {
	self.lines.allocator.free(self.glyphs);
	self.lines.deinit();
	self.lineBreaks.deinit();
}
```

## Related Questions
- How does the TextBuffer handle text parsing?
- What method is used for deinitializing resources in TextBuffer?
- How does TextBuffer convert mouse positions to character indices?
- What role does Harfbuzz play in this chunk's functionality?
- How are line breaks calculated in the TextBuffer?
- What methods are available for interacting with a TextBuffer instance?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_8*
