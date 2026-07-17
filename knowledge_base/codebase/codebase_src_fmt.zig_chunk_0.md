# [medium/codebase_src_fmt.zig] - Chunk 0

**Type:** serialization
**Keywords:** union, fromAnytype, Placeholder, parse, alignment, width, precision, formatFunction, anyFormatFunction, specifierArg
**Symbols:** FormatArg, Placeholder, FormatErrorTrace
**Concepts:** formatting, type dispatch, placeholder parsing, alignment, width precision, custom format functions, error handling, pointer size analysis, null terminated strings

## Summary
Defines a runtime format argument union and placeholder parser for formatting values with alignment, width, precision, and custom functions.

## Explanation
The chunk declares FormatArg as a union of int, uint, f16/f32/f64/f80/f128, string, nullTerminatedString, formatFunction, anyFormatFunction, and err. It provides fromAnytype to dispatch based on type info: comptime_int/float go directly; signedness is checked for unsigned ints; pointers are handled by size (one/slice/c) and child type (u8 arrays become strings, sentinel or c-arrays become nullTerminatedString), with a recursive fallback to fromAnytype for one-sized pointers. Structs/enums/unions/opaque types that have a format method are wrapped into a typeErasedFormat struct containing the original function casted via anyopaque; otherwise a genericFormat is used which prints "{any}". Errors are returned as .err. The Placeholder struct mirrors std.fmt.Placeholder with fields specifierArg, fill, alignment, argPos, width, precision and implements parse using std.fmt.Parser: it extracts argPos, consumes the specifier argument up to ':', validates that any following char is ':' or '}', logs an error for unexpected chars, then parses optional fill byte (only '<','^','>' are accepted), alignment ('<','^','>'), checks for leading zero in width when neither fill nor alignment present, reads width number, skips '.' if present and errors otherwise, reads precision number, and ensures no trailing characters. It returns a Placeholder with defaults: fill ' ' or '0', alignment .right, argPos null, width/precision as parsed values.

## Related Questions
- How does fromAnytype handle a pointer to an array of u8?
- What happens when a struct has a format method versus no format method?
- Which alignment characters are accepted by Placeholder.parse and what do they map to?
- How is the fill byte determined when width starts with zero?
- What error is returned if an unexpected character appears after the specifier argument?
- Does FormatArg include a variant for arbitrary user-defined format functions?
- Is there support for null-terminated strings in FormatArg and how are they distinguished from regular slices?
- How does the parser decide whether to treat width as having a leading zero or not?
- What default values are assigned to fill and alignment when none are provided?
- Can argPos be set by the caller or is it always derived from parsing?

*Source: unknown | chunk_id: codebase_src_fmt.zig_chunk_0*
