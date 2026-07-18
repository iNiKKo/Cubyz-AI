# [easy/codebase_src_proceduralItem_modifiers_restrictions_or.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, method, iteration, allocation, tooltip generation
**Symbols:** Or, Or.children, Or.satisfied, Or.loadFromZon, Or.printTooltip
**Concepts:** procedural item modifiers, restriction logic, OR operation

## Summary
Defines the Or struct for handling procedural item modifier restrictions with an OR logical operation.

## Explanation
The chunk defines a struct `Or` that represents a collection of `ModifierRestriction` objects. It includes methods to check if any child restriction is satisfied, load from ZonElement configuration, and print a tooltip string. The `satisfied` method iterates over its children and returns true if any child's `satisfied` method returns true. The `loadFromZon` method creates an instance of `Or`, allocates memory for its children, and loads each child from the ZonElement configuration. The `printTooltip` method constructs a tooltip string by appending the tooltips of its children with ' or ' in between.

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
- What is the purpose of the Or struct?
- How does the satisfied method work in the Or struct?
- What does the loadFromZon method do?
- How is the tooltip printed for an Or instance?
- What are the fields of the Or struct?
- Which methods are defined for the Or struct?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_or.zig_chunk_0*
