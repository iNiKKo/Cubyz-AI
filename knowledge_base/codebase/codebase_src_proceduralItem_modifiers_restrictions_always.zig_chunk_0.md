# [easy/codebase_src_proceduralItem_modifiers_restrictions_always.zig] - Chunk 0

**Type:** api
**Keywords:** always, undefined, tooltip, satisfied, allocator, zon element
**Symbols:** satisfied, loadFromZon, printTooltip
**Concepts:** procedural item modifiers, tooltip generation

## Summary
This chunk provides functions for procedural item modifiers that always satisfy restrictions and load from Zon elements.

## Explanation
The `satisfied` function always returns true, indicating that the procedural item modifier is always satisfied. The `loadFromZon` function returns undefined, suggesting it does not perform any specific loading logic. The `printTooltip` function appends 'always' to the output string, providing a tooltip for the procedural item modifier.

## Code Example
```zig
pub fn satisfied(_: *const anyopaque, _: *const ProceduralItem, _: i32, _: i32) bool {
	return true;
}
```

## Related Questions
- What does the `satisfied` function return?
- How is the `loadFromZon` function implemented?
- What string is appended by the `printTooltip` function?
- Which allocator is used in this module?
- What type of element is loaded by the `loadFromZon` function?
- Where is the `ProceduralItem` type defined?
- How does the `satisfied` function interact with its parameters?
- What is the purpose of the `printTooltip` function?
- Which module imports this file?
- How does the `loadFromZon` function handle errors?
- What is the return type of the `satisfied` function?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_always.zig_chunk_0*
