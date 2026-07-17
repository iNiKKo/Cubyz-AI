# [hard/codebase_src_graphics.zig] - Chunk 5

**Type:** implementation
**Keywords:** TextBuffer, Parser, bold italic underline strikethrough, hex color parsing, unicode iterator, control characters, line management, font effects
**Symbols:** TextBuffer, Line, Parser, appendControlGetNext, appendGetNext, peekNextByte, parse, countVisibleCharacters
**Concepts:** text rendering pipeline, font effect parsing, markdown-style formatting, unicode iterator handling, color parsing from hex

## Summary
Implements text rendering pipeline: TextBuffer stores glyph lines, Parser handles markdown-style font effects (bold/italic/underline/strikethrough/color) and control character handling.

## Explanation
TextBuffer holds alignment, width, buffer pointer, glyphs list, managed lines of Line structs, and lineBreaks. addLine appends a non-empty line to self.lines; initLines iterates glyphs, tracks lastFontEffect, creates or extends underline/overline segments based on hasLine checks, resets color when needed, and adds final segment if present. Parser contains unicodeIterator (std.unicode.Utf8Iterator), currentFontEffect, parsedText list of u32 codepoints, fontEffects list of FontEffect, characterIndex list of u32 offsets, showControlCharacters flag, curChar (u21) and curIndex (u32). appendControlGetNext appends a gray control effect when showControlCharacters is true, then advances iterator; appendGetNext always appends currentFontEffect. peekNextByte returns first byte of next UTF-8 sequence or 0 if exhausted. parse runs the main loop: initializes state, enters infinite while(true) and switches on curChar. '*' toggles bold/italic (double '*' triggers bold). '_' checks double underscore via peekNextByte; single '_' is a regular character, double '_' toggles underline. '~' similarly handles strikethrough with double tilde. '\' consumes escape sequence without effect. '#' parses hex color: shifts by 4 bits per nibble, uses switch on digit/letter to compute value, masks existing color, appends control char after each nibble, loops until shift==0. '§' resets fontEffect to a zeroed struct with the current color (effectively clearing effects). else branch is regular character: appendGetNext advances iterator and records codepoint. countVisibleCharacters iterates text, skips '*' and double '_' sequences, increments count for single '_' characters.

## Code Example
```zig
		fn peekNextByte(self: *Parser) u8 {
			const next = self.unicodeIterator.peek(1);
			if (next.len == 0) return 0;
			return next[0];
		}
```

## Related Questions
- How does TextBuffer handle line breaks between glyphs?
- What is the purpose of showControlCharacters in Parser?
- How are double underscores treated differently from single underscores?
- What happens when a '#' character is encountered during parsing?
- How does parse reset font effects using '§'?
- Why does appendControlGetNext only run when showControlCharacters is true?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_5*
