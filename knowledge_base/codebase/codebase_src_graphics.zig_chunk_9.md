# [hard/codebase_src_graphics.zig] - Chunk 9

**Type:** implementation
**Keywords:** text rendering, line breaks, selection drawing, OpenGL commands, shadow effect
**Symbols:** calculateLineBreaks, drawSelection, render, renderTextWithoutShadow, shadowColor, renderShadow
**Concepts:** text rendering, line breaking, selection highlighting, OpenGL rendering

## Summary
This chunk handles text rendering, including calculating line breaks, drawing selections, and rendering text with or without shadows.

## Explanation
The chunk defines several functions related to text rendering in a graphics engine. The `calculateLineBreaks` function computes the dimensions of text blocks by iterating through glyphs and determining where lines should break based on maximum line width. The `drawSelection` function highlights selected text by drawing rectangles around the selected characters. The `render` function orchestrates the rendering process, calling helper functions to render text without shadows and with shadows. The `renderTextWithoutShadow` function sets up the rendering environment, binds necessary resources, and draws each glyph using OpenGL commands. The `shadowColor` function calculates a shadow color based on the perceived brightness of the original text color. The `renderShadow` function is similar to `renderTextWithoutShadow` but adjusts positions and colors to create a shadow effect.

## Code Example
```zig
pub fn calculateLineBreaks(self: *TextBuffer, fontSize: f32, maxLineWidth: f32) Vec2f {
		self.lineBreaks.clearRetainingCapacity();
		const spaceCharacterWidth = 8;
		self.lineBreaks.append(.{.index = 0, .width = 0});
		const scaledMaxWidth = maxLineWidth/fontSize*16.0;
		var lineWidth: f32 = 0;
		var lastSpaceWidth: f32 = 0;
		var lastSpaceIndex: u32 = 0;
		for (self.glyphs, 0..) |glyph, i| {
			lineWidth += glyph.x_advance;
			if (glyph.character == ' ') {
				lastSpaceWidth = lineWidth;
				lastSpaceIndex = @intCast(i + 1);
			}
			if (glyph.character == '\n') {
				self.lineBreaks.append(.{.index = @intCast(i + 1), .width = lineWidth - spaceCharacterWidth});
				lineWidth = 0;
				lastSpaceIndex = 0;
				lastSpaceWidth = 0;
			}
			if (lineWidth > scaledMaxWidth) {
				if (lastSpaceIndex != 0) {
					lineWidth -= lastSpaceWidth;
					self.lineBreaks.append(.{.index = lastSpaceIndex, .width = lastSpaceWidth - spaceCharacterWidth});
					lastSpaceIndex = 0;
					lastSpaceWidth = 0;
				} else {
					self.lineBreaks.append(.{.index = @intCast(i), .width = lineWidth - glyph.x_advance});
					lineWidth = glyph.x_advance;
					lastSpaceIndex = 0;
					lastSpaceWidth = 0;
				}
			}
		}
		self.width = maxLineWidth;
		self.lineBreaks.append(.{.index = @intCast(self.glyphs.len), .width = lineWidth});
		return Vec2f{maxLineWidth*fontSize/16.0, @as(f32, @floatFromInt(self.lineBreaks.items.len - 1))*fontSize};
	}
```

## Related Questions
- What function calculates the dimensions of a text block?
- How does the `drawSelection` function highlight selected text?
- What is the purpose of the `render` function in this chunk?
- How does the `renderTextWithoutShadow` function set up the rendering environment?
- What determines the shadow color in the `shadowColor` function?
- How is the shadow effect created in the `renderShadow` function?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_9*
