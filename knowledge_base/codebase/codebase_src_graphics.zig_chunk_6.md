# [hard/codebase_src_graphics.zig] - Chunk 6

**Type:** implementation
**Keywords:** text alignment, font styling, line management, glyph processing, text parsing
**Symbols:** TextBuffer, TextBuffer.Alignment, TextBuffer.FontEffect, TextBuffer.Line, TextBuffer.LineBreak, TextBuffer.GlyphData, TextBuffer.alignment, TextBuffer.width, TextBuffer.buffer, TextBuffer.glyphs, TextBuffer.lines, TextBuffer.lineBreaks, TextBuffer.addLine, TextBuffer.initLines, TextBuffer.Parser, TextBuffer.Parser.unicodeIterator, TextBuffer.Parser.currentFontEffect, TextBuffer.Parser.parsedText, TextBuffer.Parser.fontEffects, TextBuffer.Parser.characterIndex, TextBuffer.Parser.showControlCharacters, TextBuffer.Parser.curChar, TextBuffer.Parser.curIndex, TextBuffer.Parser.appendControlGetNext, TextBuffer.Parser.appendGetNext, TextBuffer.Parser.peekNextByte, TextBuffer.Parser.parse
**Concepts:** text rendering, font effects, line breaks, glyph data

## Summary
The TextBuffer struct manages text rendering, including alignment, font effects, and line breaks.

## Explanation
The TextBuffer struct is designed to handle the complexities of text rendering in a graphics engine. It includes an Alignment enum for text justification, which can be set to left, center, or right. The FontEffect packed struct manages various text styles like color, bold, italic, underline, and strikethrough. Each field in FontEffect is explicitly defined: `color` as a 24-bit unsigned integer with a default value of 0xffffff (white), `bold`, `italic`, `underline`, and `strikethrough` as booleans with default values of false. The Line struct defines the structure of lines within the text buffer, containing fields for start and end positions (`start` and `end` as f32), color (`color` as a 24-bit unsigned integer), and whether it is underlined (`isUnderline` as a boolean). The LineBreak struct defines the structure of line breaks within the text buffer, containing fields for the index (`index` as u32) and width (`width` as f32). The GlyphData struct holds detailed information about each glyph, including its advance values (`x_advance` and `y_advance` as f32), offset values (`x_offset` and `y_offset` as f32), character data (`character` as a 21-bit unsigned integer), index (`index` as u32), cluster (`cluster` as u32), font effects (`fontEffect` as FontEffect), and character index (`characterIndex` as u32). The TextBuffer itself contains fields for alignment, width, a HarfBuzz buffer pointer (`buffer`), an array of glyphs (`glyphs`), lists for managing lines (`lines`) and line breaks (`lineBreaks`), and methods to add lines (`addLine`) and initialize lines based on font effects (`initLines`). The Parser struct within TextBuffer is responsible for parsing text input, handling control characters, and applying font effects. It includes methods to append control characters (`appendControlGetNext`), get next characters (`appendGetNext`), peek at the next byte (`peekNextByte`), and parse the entire text input (`parse`). The `parse` method processes each character in the input, updating the current font effect based on special control characters like '*', '_', and '~'.

## Code Example
```zig
fn addLine(self: *TextBuffer, line: Line) void {
	if (line.start != line.end) {
		self.lines.append(line);
	}
}
```

## Related Questions
- What are the possible alignments for text in TextBuffer?
- How does TextBuffer handle different font effects like bold and italic?
- What is the structure of a LineBreak in TextBuffer?
- How does the Parser struct within TextBuffer manage control characters?
- What method initializes lines based on font effects in TextBuffer?
- How does TextBuffer determine when to add a new line during rendering?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_6*
