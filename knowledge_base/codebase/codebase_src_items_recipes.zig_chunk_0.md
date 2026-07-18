# [medium/codebase_src_items_recipes.zig] - Chunk 0

**Type:** implementation
**Keywords:** pattern parsing, symbol handling, string matching, key-value pairs, error handling
**Symbols:** Segment, parsePattern, ItemStackPattern, parseItemZon, matchWithKeys, ItemWithAmount, ItemKeyPair
**Concepts:** item pattern parsing, pattern matching, string manipulation

## Summary
Parses item patterns and matches them against target strings.

## Explanation
This chunk defines functions for parsing item patterns from strings and matching those patterns against target strings. It includes a `parsePattern` function that converts a pattern string into segments of literals and symbols, a `parseItemZon` function that parses an item pattern from a ZonElement, and a `matchWithKeys` function that attempts to match a pattern against a target string using a set of keys. The chunk also defines several structs for representing item patterns, amounts, and key pairs.

## Code Example
```zig
const Segment = union(enum) { literal: []const u8, symbol: []const u8 }
```

## Related Questions
- How does the `parsePattern` function work?
- What is the purpose of the `ItemStackPattern` struct?
- How are symbols and literals handled in pattern parsing?
- What error can occur if there are ambiguous symbols in a pattern?
- How does the `matchWithKeys` function handle multiple possible matches?
- What is the role of the `ItemWithAmount` struct?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_0*
