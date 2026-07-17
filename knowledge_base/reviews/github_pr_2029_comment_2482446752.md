# [src/gui/components/TextInput.zig] - PR #2029 review diff

**Type:** review
**Keywords:** TextInput, obfuscation, cursor, buffer, length, position, conversion, init function, un-obfuscate button, passwords, IP addresses
**Symbols:** TextInput, select, deselect, cursorPosFromObfuscated, cursorPosToObfuscated, getBufferLen, obfuscate
**Concepts:** Text obfuscation, Cursor position handling, Buffer length calculation

## Summary
Added obfuscation functionality to the TextInput component, including methods for converting cursor positions and getting buffer length.

## Explanation
The changes introduce obfuscation support to the TextInput component by adding several new functions: `cursorPosFromObfuscated`, `cursorPosToObfuscated`, and `getBufferLen`. These functions handle the conversion of cursor positions and determine the buffer length based on whether the text is obfuscated. The reviewer notes that there will be no un-obfuscate button, as they believe it's unnecessary for typical use cases involving passwords or IP addresses.

## Related Questions
- What is the purpose of the `cursorPosFromObfuscated` function?
- How does the `getBufferLen` function determine the buffer length?
- Why was the decision made to not include an un-obfuscate button?
- What changes were made to handle obfuscated text in the TextInput component?
- Can you explain the role of the `obfuscationChar.len` constant in the code?
- How does the `cursorPosToObfuscated` function work with UTF-8 encoded strings?

*Source: unknown | chunk_id: github_pr_2029_comment_2482446752*
