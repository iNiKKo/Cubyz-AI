# [easy/codebase_src_proceduralItem_modifiers_restrictions_always.zig] - Chunk 0

**Type:** api
**Keywords:** always restriction, ZonElement loading, tooltip printing, function implementation, public API
**Symbols:** satisfied, loadFromZon, printTooltip
**Concepts:** procedural item modifiers, restriction handling, tooltip generation

## Summary
This chunk defines functions for handling procedural item modifiers with an 'always' restriction.

## Explanation
The chunk provides three public functions: `satisfied`, `loadFromZon`, and `printTooltip`. The `satisfied` function always returns true, indicating that the modifier is always applicable. The `loadFromZon` function is intended to load data from a ZonElement but currently returns undefined. The `printTooltip` function appends the string 'always' to an output string, presumably for displaying information about the modifier.

## Code Example
```zig
pub fn satisfied(_: *const anyopaque, _: *const ProceduralItem, _: i32, _: i32) bool {
	return true;
}
```

## Related Questions
- What does the `satisfied` function always return?
- How is data loaded from a ZonElement in this chunk?
- What string does the `printTooltip` function append to the output?
- What is the purpose of the `NeverFailingAllocator` parameter in `loadFromZon`?
- Why does the `loadFromZon` function return undefined currently?
- How many public functions are defined in this chunk?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_always.zig_chunk_0*
