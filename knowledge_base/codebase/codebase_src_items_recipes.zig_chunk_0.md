# [medium/codebase_src_items_recipes.zig] - Chunk 0

**Type:** implementation
**Keywords:** pattern parsing, symbol handling, string matching, key-value pairs, error handling
**Symbols:** Segment, parsePattern, ItemStackPattern, parseItemZon, matchWithKeys, ItemWithAmount, ItemKeyPair
**Concepts:** item pattern parsing, pattern matching, string manipulation

## Summary
Parses item patterns and matches them against target strings.

## Explanation
This chunk defines functions for parsing item patterns from strings and matching those patterns against target strings. It includes a `parsePattern` function that converts a pattern string into segments of literals and symbols, handling cases where symbols are enclosed in braces `{}`. The function returns an array of `Segment`, which can be either a literal string or a symbol. If there is ambiguity with symbols (i.e., multiple consecutive symbols without any literals between them), the function returns an error `AmbiguousSymbols`. Additionally, if there are unclosed braces or empty braces in the pattern, it returns errors `UnclosedBraces` and `EmptyBraces`, respectively.

The `parseItemZon` function parses an item pattern from a ZonElement. It extracts the amount of items (defaulting to 1) and then calls `parsePattern` to parse the remaining part of the string into segments. The resulting pattern is stored in an `ItemStackPattern`, which includes both the parsed pattern and the amount.

The `matchWithKeys` function attempts to match a pattern against a target string using a set of keys (represented as a `std.StringHashMap`). It iterates through each segment, handling literals by checking if they start with the corresponding substring in the target. For symbols, it checks if there is an entry in the key map that matches the symbol and starts with the corresponding substring in the target. If no match is found for a symbol, it tries to find multiple possible matches and returns all valid key pairs.

The chunk also defines several structs: `ItemStackPattern` represents parsed item patterns along with their amounts; `ItemWithAmount` stores an item index and its amount; and `ItemKeyPair` combines an `ItemWithAmount` struct with a set of keys.

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
