# [hard/codebase_src_graphics.zig] - Chunk 8

**Type:** implementation
**Keywords:** Harfbuzz, text shaping, mouse position, character index, cursor position, line breaks
**Symbols:** TextBuffer, TextBuffer.showControlCharacters, TextBuffer.parse, TextBuffer.deinit, TextBuffer.getLineOffset, TextBuffer.mousePosToIndex, TextBuffer.indexToCursorPos, TextBuffer.calculateLineBreaks
**Concepts:** text rendering, text interaction, line breaking, glyph handling

## Summary
Handles text parsing, rendering, and interaction logic.

## Explanation
This chunk implements the TextBuffer struct, which manages text rendering and interaction. It includes methods for initializing text buffers from parsed text, deinitializing resources, converting mouse positions to character indices, and calculating cursor positions. The code uses Harfbuzz for shaping text and handles line breaks based on font size and maximum line width.

The `parse` method initializes the parser, sets up Harfbuzz buffer, adds UTF-32 characters, sets direction, script, language, shapes the text, retrieves glyph information and positions, guesses text indices from cluster indices, merges it all together into glyphs, finds lines, and appends line breaks. Specifically, it creates a Harfbuzz buffer (`c.hb_buffer_create()`), adds parsed text as UTF-32 characters (`c.hb_buffer_add_utf32(buffer, parser.parsedText.items.ptr, @intCast(parser.parsedText.items.len), 0, @intCast(parser.parsedText.items.len))`), sets the buffer's direction to left-to-right (`c.hb_buffer_set_direction(buffer, c.HB_DIRECTION_LTR)`), script to common (`c.hb_buffer_set_script(buffer, c.HB_SCRIPT_COMMON)`), and language to default (`c.hb_buffer_set_language(buffer, c.hb_language_get_default())`). It then shapes the text using the Harfbuzz font (`c.hb_shape(TextRendering.harfbuzzFont, buffer, null, 0)`), retrieves glyph information and positions (`c.hb_buffer_get_glyph_infos(buffer, &len).?` and `c.hb_buffer_get_glyph_positions(buffer, &len).?`), guesses text indices from cluster indices, and merges this information into glyphs. The method also finds lines by iterating through the glyphs and appending line breaks based on the calculated width.

The `deinit` method frees allocated resources for glyphs, lines, and line breaks (`self.lines.allocator.free(self.glyphs); self.lines.deinit(); self.lineBreaks.deinit();`).

The `getLineOffset` method calculates the offset based on alignment and width differences (`const factor: f32 = switch (self.alignment) { .left => 0, .center => 0.5, .right => 1 }; const diff = self.width - self.lineBreaks.items[line + 1].width; return diff*factor;`).

The `mousePosToIndex` method converts mouse positions to character indices by iterating through glyphs and checking mouse position relative to glyph advance (`if (mousePos[0] < x + glyph.x_advance/2) { return @intCast(glyph.characterIndex); }`).

The `indexToCursorPos` method calculates cursor positions by iterating through glyphs and finding the position of a specific character index (`while (true) { for (self.glyphs[self.lineBreaks.items[i].index..self.lineBreaks.items[i + 1].index]) |glyph| { if (glyph.characterIndex == index) { return .{x, y}; } x += glyph.x_advance; y -= glyph.y_advance; } i += 1; if (i >= self.lineBreaks.items.len - 1) { return .{x, y}; } y += 16; }`).

The `calculateLineBreaks` method calculates line breaks based on font size, maximum line width, and handling spaces and newlines. It clears existing line breaks (`self.lineBreaks.clearRetainingCapacity()`), sets up space character width (`const spaceCharacterWidth = 8;`), appends initial line break (`self.lineBreaks.append(.{.index = 0, .width = 0});`), iterates through glyphs to calculate line width (`lineWidth += glyph.x_advance;`), handles spaces by storing last space width and index (`if (glyph.character == ' ') { lastSpaceWidth = lineWidth; lastSpaceIndex = @intCast(i + 1); }`), handles newlines by appending line breaks (`if (glyph.character == '
') { self.lineBreaks.append(.{.index = @intCast(i + 1), .width = lineWidth - spaceCharacterWidth}); lineWidth = 0; lastSpaceIndex = 0; lastSpaceWidth = 0; }`), and if the line width exceeds the scaled maximum width, it either breaks at the last space or continues without breaking (`if (lineWidth > scaledMaxWidth) { if (lastSpaceIndex != 0) { lineWidth -= lastSpaceWidth; self.lineBreaks.append(.{.index = lastSpaceIndex, .width = lastSpaceWidth - spaceCharacterWidth}); lastSpaceIndex = 0; lastSpaceWidth = 0; } else { ...`).

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
