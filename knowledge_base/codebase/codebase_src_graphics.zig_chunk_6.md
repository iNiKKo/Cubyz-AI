# [hard/codebase_src_graphics.zig] - Chunk 6

**Type:** implementation
**Keywords:** text parsing, glyph shaping, memory allocation, UTF-8 iteration, Harfbuzz buffer
**Symbols:** TextBuffer, TextBuffer.alignment, TextBuffer.width, TextBuffer.buffer, TextBuffer.glyphs, TextBuffer.lines, TextBuffer.lineBreaks, TextBuffer.init, TextBuffer.deinit, countVisibleCharacters
**Concepts:** text rendering, glyph management, UTF-8 handling, Harfbuzz integration

## Summary
The `TextBuffer` struct and its associated functions handle text parsing, rendering, and management in the graphics module.

## Explanation
The chunk defines a `TextBuffer` struct that manages text data for rendering. It includes methods like `init`, which initializes the buffer by parsing input text, using Harfbuzz for shaping, and allocating glyphs. The `deinit` method frees resources. The `countVisibleCharacters` function counts visible characters in a given text string, handling special formatting characters. The chunk uses UTF-8 iteration, Harfbuzz for glyph shaping, and manages memory allocation and deallocation.

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
- What is the purpose of the `TextBuffer` struct?
- How does the `init` method initialize a `TextBuffer` instance?
- What function counts visible characters in a text string?
- How does the chunk handle memory allocation and deallocation?
- What role does Harfbuzz play in the text rendering process?
- How are special formatting characters handled during text parsing?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_6*
