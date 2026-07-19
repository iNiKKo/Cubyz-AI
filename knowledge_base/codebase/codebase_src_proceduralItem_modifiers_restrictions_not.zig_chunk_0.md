# [easy/codebase_src_proceduralItem_modifiers_restrictions_not.zig] - Chunk 0

**Type:** implementation
**Keywords:** not, restriction, satisfied, loadFromZon, printTooltip
**Symbols:** NeverFailingAllocator, ModifierRestriction, ProceduralItem, ZonElement, Not
**Concepts:** modifier restrictions, negation, serialization, deserialization

## Summary
Not modifier restriction implementation

## Explanation
This chunk defines a `Not` struct that represents the negation of another `ModifierRestriction`. It provides three key methods: `satisfied`, `loadFromZon`, and `printTooltip`. The `satisfied` method checks if a procedural item does not satisfy the child restriction. The `loadFromZon` function deserializes the `Not` struct from a ZonElement, creating a new instance of `Not` with its child restriction loaded from the provided ZonElement. The `printTooltip` function generates a tooltip for the `Not` modifier, indicating that it negates the tooltip of the child restriction.

The types of data structures used in this chunk include `NeverFailingAllocator`, `ModifierRestriction`, `ProceduralItem`, and `ZonElement`. Memory allocation is handled by the `allocator.create(Not)` method, which creates a new instance of `Not` on the heap. There are no explicit error handling mechanisms in this chunk, as it uses `NeverFailingAllocator` which guarantees successful allocations. Concurrency considerations are not relevant to this chunk, as it does not involve any shared mutable state or asynchronous operations.

The dependencies between different parts of this chunk include the `ModifierRestriction` struct and the `ZonElement` type, both of which are imported from other modules. The `Not` struct interacts with these components by calling their methods (`satisfied`, `loadFromZon`, and `printTooltip`) to perform its operations.

Serialization and deserialization are handled by the `loadFromZon` function, which reads data from a ZonElement and creates an instance of `Not`. Deserialization is performed when loading the child restriction from the ZonElement.

## Code Example
```zig
const Not = struct {
	child: ModifierRestriction,
}
```

## Related Questions
- What is the purpose of the Not struct?
- How does the satisfied function work?
- What is the loadFromZon function used for?
- What does the printTooltip function do?
- Can you explain how the child restriction is accessed within the Not struct?
- What are the types of data structures used in this chunk?
- How is memory allocated and deallocated in this chunk?
- What are the error handling mechanisms used in this chunk?
- What are the concurrency considerations in this chunk?
- What are the dependencies between different parts of this chunk?
- Can you describe how the Not struct interacts with other components or modules?
- What is the role of serialization and deserialization in this chunk?

*Source: unknown | chunk_id: codebase_src_proceduralItem_modifiers_restrictions_not.zig_chunk_0*
