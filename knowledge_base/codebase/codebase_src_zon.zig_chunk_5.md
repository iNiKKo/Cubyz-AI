# [hard/codebase_src_zon.zig] - Chunk 5

**Type:** serialization
**Keywords:** ZonElement union, std.StringHashMap, ListManaged, UTF-8 continuation bytes, line number calculation, character buffer indexing, whitespace skipping, literal parsing, object key handling, array element appending, error message formatting, allocator ownership, public API functions
**Symbols:** parseElement, parseNumber, parseString, parseObject, parseArray, printError, skipWhitespaceAndComments, parseIdentifierOrStringOrEnumLiteral
**Concepts:** JSON parsing, AST construction, error reporting with line numbers

## Summary
This chunk implements the core ZON file parser in Zig, providing functions to tokenize and parse JSON-like structures (objects, arrays, strings, numbers, booleans) into a typed AST represented by the ZonElement union.

## Explanation
The chunk defines several public parsing functions that operate on a character buffer 'chars' with an index pointer. The entry point is parseElement, which dispatches based on the first character: digits or +/- invoke parseNumber; 't', 'f', 'n' invoke literal parsers for true/false/null; quotes invoke parseString; braces invoke parseObject/parseArray. Each parser advances the index and returns a ZonElement tagged union (object, array, string, number, bool, null). parseObject builds a std.StringHashMap(ZonElement), skipping whitespace/comments via skipWhitespaceAndComments, handling optional leading dots on keys, parsing key identifiers or quoted strings via parseIdentifierOrStringOrEnumLiteral, then expecting '=' before the value. It tracks duplicate keys and frees old entries with allocator.free(old.key) and old.value.deinit(allocator). parseArray builds a ListManaged(ZonElement), appending each parsed element and skipping commas. All parsers call printError on failure; printError computes line number by counting '\n' up to the index, extracts the error message substring, and logs a formatted stack trace with '^' marker at the exact character position (handling UTF-8 continuation bytes). The chunk does not define any struct or enum types here—those are imported from elsewhere—but it declares all parsing functions as pub fn NAME(...), making them part of this module's API surface.

## Related Questions
- How does parseElement dispatch between number, string, boolean, null, object, and array tokens?
- What is the exact behavior of skipWhitespaceAndComments in each parser function?
- How are duplicate keys detected and cleaned up inside parseObject?
- Why does printError compute line numbers by scanning for '\n' rather than using a precomputed offset table?
- Does this chunk handle escaped characters inside quoted strings, or only raw ASCII?
- What happens if the input buffer ends prematurely while parsing an object key identifier?
- How are commas handled in parseArray versus parseObject (are they optional)?
- Is there any validation that numeric values fit within u32 range before returning a number element?
- Does the parser support comments other than whitespace, and how are they skipped?
- What is the purpose of the NeverFailingAllocator type parameter in these functions?

*Source: unknown | chunk_id: codebase_src_zon.zig_chunk_5*
