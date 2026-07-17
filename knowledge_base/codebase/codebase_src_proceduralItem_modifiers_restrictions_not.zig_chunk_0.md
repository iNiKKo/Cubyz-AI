# [easy/codebase_src_proceduralItem_modifiers_restrictions_not.zig] - Chunk 0

**Type:** implementation
**Keywords:** not, negation, modifier, restriction, tooltip
**Symbols:** Not, Not.child, satisfied, loadFromZon, printTooltip
**Concepts:** ModifierRestriction, ProceduralItem, ZonElement

## Summary
Not modifier restriction implementation

## Explanation
This chunk defines a `Not` struct that represents the negation of another `ModifierRestriction`. It provides a method `satisfied` to check if a procedural item does not satisfy the child restriction. The `loadFromZon` function loads the `Not` modifier from a ZonElement, and `printTooltip` generates a tooltip for the `Not` modifier.

## Code Example
```zig
const Not = struct {
	child: ModifierRestriction,
}
```

## Related Questions
- What is the purpose of the Not struct?
- How does the satisfied function work?
- Where is the loadFromZon function defined?
- What does the printTooltip function do?
- Which functions are exported by this chunk?
- What are the symbols declared in this chunk?
- How many lines of code does the shortest function body have?
- What is the purpose of the NeverFailingAllocator type?
- Where is the ModifierRestriction struct defined?
- What is the loadFromZon function used for?
- Which functions are called by the satisfied function?
- What is the purpose of the ZonElement type?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_not.zig_chunk_0*
