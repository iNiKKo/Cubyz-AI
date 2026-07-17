# [medium/codebase_src_items_recipes.zig] - Chunk 0

**Type:** implementation
**Keywords:** pattern parsing, string matching, key-value pairs, item recipes, memory management
**Symbols:** Segment, parsePattern, ItemStackPattern, parseItemZon, matchWithKeys, ItemWithAmount, ItemKeyPair, findRecipeItemOptions
**Concepts:** item stack patterns, recipe matching, string parsing

## Summary
Handles parsing and matching item stack patterns with recipes.

## Explanation
This chunk defines functions for parsing item stack patterns from strings, matching these patterns against target strings using a set of keys, and finding recipe item options based on parsed patterns. It uses Zig's standard library for string manipulation and memory management. The `parsePattern` function breaks down a pattern string into segments of literals and symbols. The `parseItemZon` function parses an item stack pattern from a ZonElement. The `matchWithKeys` function attempts to match a target string against a pattern using provided keys, handling both literal and symbolic segments. The `findRecipeItemOptions` function finds possible items that match a given item stack pattern, considering the amount specified.

## Code Example
```zig
const Segment = union(enum) { literal: []const u8, symbol: []const u8 }
```

## Related Questions
- How does the `parsePattern` function work?
- What is the purpose of the `ItemStackPattern` struct?
- How are item stack patterns parsed from ZonElements?
- What does the `matchWithKeys` function do with symbolic segments?
- How does the `findRecipeItemOptions` function handle literal segments?
- What error can occur if there are ambiguous symbols in a pattern?

*Source: unknown | chunk_id: codebase_src_items_recipes.zig_chunk_0*
