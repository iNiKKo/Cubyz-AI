# [src/gui/components/TextInput.zig] - Chunk 2470968395

**Type:** review
**Keywords:** obfuscationChar, currentString.items.len, getBufferLen, cursorPosFromObfuscated, cursorPosToObfuscated, static option, construction time, UTF-8 iterator, glyphs.len, selectionStart, pressed, deselect
**Symbols:** TextInput.select, TextInput.deselect, cursorPosFromObfuscated, cursorPosToObfuscated, getBufferLen, TextInput.obfuscate
**Concepts:** obfuscation, cursor position translation, buffer length calculation, static vs dynamic options, UTF-8 iteration, glyph rendering, selection logic, codepoint counting

## Summary
Refactors TextInput selection logic to handle obfuscation by introducing cursor position conversion functions and a dynamic buffer length getter, while addressing reviewer concern about making the obfuscation setting static at construction time.

## Explanation
The original code assumed self.currentString.items.len directly represented visible characters. With obfuscation enabled, each character is replaced by an obfuscationChar (e.g., a placeholder glyph), so the raw byte count no longer matches user-visible length. The reviewer flagged that allowing dynamic toggling of obfuscation adds unnecessary complexity; however, the diff shows new helper functions cursorPosFromObfuscated and cursorPosToObfuscated to translate between logical character positions and physical buffer indices when obfuscation is active. A getBufferLen function returns either glyphs.len*obfuscationChar.len (when obfuscated) or currentString.items.len (when not), ensuring select() uses the correct length for cursor initialization. This change preserves correctness across both modes while keeping the API surface minimal.

## Related Questions
- What is the purpose of cursorPosFromObfuscated in TextInput?
- How does getBufferLen decide between glyphs.len*obfuscationChar.len and currentString.items.len?
- Why was select modified to use getBufferLen instead of self.currentString.items.len directly?
- Does cursorPosToObfuscated handle multi-byte UTF-8 characters correctly when obfuscation is enabled?
- What happens if self.obfuscated is false in getBufferLen?
- Is there any side effect on deselect when the text is obfuscated?
- How does this change affect TextInput.obfuscate implementation?
- Can cursorPosFromObfuscated be called safely with a null cursor?
- What is the expected behavior of select when self.cursor was previously set to an obfuscated length?
- Does the diff introduce any new memory allocations for the iterator in cursorPosFromObfuscated?
- How does this refactor align with the reviewer's suggestion about static options at construction time?

*Source: unknown | chunk_id: github_pr_2029_comment_2470968395*
