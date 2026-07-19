# [hard/codebase_src_graphics.zig] - Chunk 7

**Type:** implementation
**Keywords:** text parsing, font control, character counting, Harfbuzz integration, UTF-8 handling
**Symbols:** Parser, Parser.appendControlGetNext, Parser.appendGetNext, Parser.curChar, Parser.fontEffects, Parser.parsedText, Parser.showControlCharacters, Parser.unicodeIterator, TextBuffer, TextBuffer.alignment, TextBuffer.buffer, TextBuffer.glyphs, TextBuffer.init, TextBuffer.lines, TextBuffer.lineBreaks, TextBuffer.width
**Concepts:** text rendering, font effects, control characters, glyph shaping

## Summary
The chunk implements parsing and rendering logic for formatted text, handling control characters to modify font effects like bold, italic, underline, strikethrough, color, and alignment.

## Explanation
This chunk implements parsing and rendering logic for formatted text, handling control characters to modify font effects like bold, italic, underline, strikethrough, color, and alignment. The `Parser` struct processes input text, interpreting special control characters ('*', '_', '~', '\', '#', '§') to toggle font effects such as bold, italic, underline, strikethrough, color changes, and resetting font effects. Specifically, '*' toggles bold, '__' toggles italic, '~~' toggles underline, '\\' escapes the next character, '#' followed by 7 hexadecimal digits sets the color, and '§' resets the font effect to default. The `countVisibleCharacters` function iterates over the text to count characters that are visible after processing these control characters. The `init` function initializes a `TextBuffer`, sets up a parser with the provided text and initial font effect, uses Harfbuzz for shaping the text into glyphs, and prepares the buffer for rendering.

## Code Example
```zig
pub fn countVisibleCharacters(text: []const u8) usize {
			var unicodeIterator = std.unicode.Utf8Iterator{.bytes = text, .i = 0};
			var count: usize = 0;
			var curChar = unicodeIterator.nextCodepoint() orelse return count;
			outer: while (true) {
				switch (curChar) {
					'*' => {
						curChar = unicodeIterator.nextCodepoint() orelse break;
					},
					'_' => {
						curChar = unicodeIterator.nextCodepoint() orelse break;
						if (curChar == '_') {
							curChar = unicodeIterator.nextCodepoint() orelse break;
						} else {
							count += 1;
						}
					},
					'~' => {
						curChar = unicodeIterator.nextCodepoint() orelse break;
						if (curChar == '~') {
							curChar = unicodeIterator.nextCodepoint() orelse break;
						} else {
							count += 1;
						}
					},
					'\\' => {
						curChar = unicodeIterator.nextCodepoint() orelse break;
						curChar = unicodeIterator.nextCodepoint() orelse break;
						count += 1;
					},
					'#' => {
						for (0..7) |_| curChar = unicodeIterator.nextCodepoint() orelse break :outer;
					},
					'§' => {
						curChar = unicodeIterator.nextCodepoint() orelse break;
					},
					else => {
						count += 1;
						curChar = unicodeIterator.nextCodepoint() orelse break;
					},
				}
			}
			return count;
		}
```

## Related Questions
- What are the control characters used to modify font effects in this chunk?
- How does the `Parser` struct handle different types of control characters?
- What function is responsible for counting visible characters in the text?
- How does the `init` function initialize a `TextBuffer` and use Harfbuzz?
- What are the fields of the `TextBuffer` struct and their purposes?
- How does this chunk integrate with the Harfbuzz library for glyph shaping?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_7*
