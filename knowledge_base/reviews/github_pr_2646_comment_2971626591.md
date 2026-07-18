# [src/tool/modifiers/restrictions/conductedWith.zig] - PR #2646 review diff

**Type:** review
**Keywords:** Encased, Vec2i, NeverFailingAllocator, ModifierRestriction, Tool, ZonElement, getIndexInCheckArray, satisfied, BFS, Queue, Initialization, Deinitialization, Memory management
**Symbols:** Encased, Vec2i, NeverFailingAllocator, ModifierRestriction, Tool, ZonElement, getIndexInCheckArray, satisfied
**Concepts:** Breadth-first search (BFS), Queue data structure, Initialization and deinitialization, Memory management

## Summary
The code introduces a new file `conductedWith.zig` that defines a struct `Encased` and functions for checking tool restrictions based on block positions.

## Explanation
The review focuses on the initialization of the queue in the `satisfied` function. The reviewer suggests replacing hardcoded initial directions with relative positions to improve flexibility and correctness. This change ensures that the search starts from the correct position, enhancing the functionality of the tool restriction check.

## Related Questions
- What is the purpose of the `Encased` struct in this code?
- How does the `getIndexInCheckArray` function calculate the array index?
- Why is a queue used in the `satisfied` function?
- What changes were suggested to improve the initialization of the queue?
- How does the code handle memory allocation and deallocation?
- What is the role of the `NeverFailingAllocator` in this context?

*Source: unknown | chunk_id: github_pr_2646_comment_2971626591*
