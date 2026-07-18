# [hard/codebase_src_graphics.zig] - Chunk 6

**Type:** implementation
**Keywords:** text alignment, font styling, line management, glyph processing, text parsing
**Symbols:** TextBuffer, TextBuffer.Alignment, TextBuffer.FontEffect, TextBuffer.Line, TextBuffer.LineBreak, TextBuffer.GlyphData, TextBuffer.alignment, TextBuffer.width, TextBuffer.buffer, TextBuffer.glyphs, TextBuffer.lines, TextBuffer.lineBreaks, TextBuffer.addLine, TextBuffer.initLines, TextBuffer.Parser, TextBuffer.Parser.unicodeIterator, TextBuffer.Parser.currentFontEffect, TextBuffer.Parser.parsedText, TextBuffer.Parser.fontEffects, TextBuffer.Parser.characterIndex, TextBuffer.Parser.showControlCharacters, TextBuffer.Parser.curChar, TextBuffer.Parser.curIndex, TextBuffer.Parser.appendControlGetNext, TextBuffer.Parser.appendGetNext, TextBuffer.Parser.peekNextByte, TextBuffer.Parser.parse
**Concepts:** text rendering, font effects, line breaks, glyph data

## Summary
The TextBuffer struct manages text rendering, including alignment, font effects, and line breaks.

## Explanation
The TextBuffer struct is designed to handle the complexities of text rendering in a graphics engine. It includes an Alignment enum for text justification, a FontEffect packed struct to manage various text styles like color, bold, italic, underline, and strikethrough. The Line and LineBreak structs define the structure of lines and line breaks within the text buffer. The GlyphData struct holds detailed information about each glyph, including its advance and offset values, character data, and font effects. The TextBuffer itself contains fields for alignment, width, a HarfBuzz buffer pointer, an array of glyphs, lists for managing lines and line breaks, and methods to add lines and initialize lines based on font effects. The Parser struct within TextBuffer is responsible for parsing text input, handling control characters, and applying font effects. It includes methods to append control characters, get next characters, peek at the next byte, and parse the entire text input.

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
