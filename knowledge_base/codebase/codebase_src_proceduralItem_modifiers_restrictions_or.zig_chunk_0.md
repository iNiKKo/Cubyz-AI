# [easy/codebase_src_proceduralItem_modifiers_restrictions_or.zig] - Chunk 0

**Type:** implementation
**Keywords:** modifier restrictions, satisfaction check, children array, tooltip formatting, ZON parsing
**Symbols:** Or, Or.children, Or.satisfied, Or.loadFromZon, Or.printTooltip
**Concepts:** procedural item modifiers, OR combination logic, tooltip generation, ZON data loading

## Summary
This chunk defines the Or struct and its methods for representing an OR combination of modifier restrictions, including satisfaction checking, loading from ZON data, and tooltip printing.

## Explanation
The Or struct contains a children field holding a slice of ModifierRestriction. The satisfied method iterates over all children and returns true if any child is satisfied by the given procedural item at coordinates (x, y). The loadFromZon function allocates an Or instance, reads the 'children' array from the provided ZonElement using toSlice(), allocates the appropriate number of ModifierRestriction instances, and delegates loading each child via ModifierRestriction.loadFromZon. The printTooltip method appends parentheses around a space-separated list of children's tooltips, inserting ' or ' between them.

## Code Example
```zig
pub fn satisfied(self: *const Or, proceduralItem: *const ProceduralItem, x: i32, y: i32) bool {
	for (self.children) |child| {
		if (child.satisfied(proceduralItem, x, y)) return true;
	}
	return false;
}
```

## Related Questions
- How does the Or struct evaluate satisfaction across multiple modifier restrictions?
- What is the exact sequence of operations in loadFromZon when parsing children from a ZON element?
- Why does printTooltip insert ' or ' between child tooltips instead of commas?
- Which function is responsible for allocating memory for the Or instance and its children array?
- How are coordinates x and y used during satisfaction checks in the Or struct?
- What happens if the children slice is empty when calling satisfied on an Or instance?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_or.zig_chunk_0*
