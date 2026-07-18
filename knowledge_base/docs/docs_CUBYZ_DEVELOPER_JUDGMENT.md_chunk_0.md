# [medium/docs_CUBYZ_DEVELOPER_JUDGMENT.md] - Chunk 0

**Type:** documentation
**Keywords:** allocator-conscious, explicit code, predictable, memory discipline, concurrency safety, type system design, optional types, avoiding over-engineering, clear naming conventions, stack allocator, world arena, global allocator, arena allocator, atomic values, union(enum)
**Symbols:** main.stackAllocator, main.worldArena, NeverFailingAllocator, union(enum), ?T, SparseSet
**Concepts:** Memory Management, Concurrency, Type System, Code Clarity, Avoiding Over-Engineering

## Summary
This document outlines the judgment patterns and coding practices preferred by Cubyz maintainers based on analyzing GitHub PR reviews, emphasizing explicit, predictable code over clever solutions, memory discipline, concurrency safety, type system usage, avoiding over-engineering, and clear naming.

## Explanation
The document synthesizes insights from 649 GitHub PR review threads to capture the core judgment patterns of Cubyz maintainers. It highlights a strong preference for explicit code that is allocator-conscious, rejecting clever or generic solutions in favor of predictability. Key areas covered include memory management, concurrency, type system design, avoiding unnecessary complexity, and clear naming conventions. Specific practices detailed include matching allocators to data lifetimes, proper synchronization of shared fields, using tagged unions for distinct cases, preferring optional types over sentinel values, and avoiding arbitrary hardcoded limits without justification.

## Related Questions
- What is the primary preference for memory management in Cubyz?
- How should allocators be matched to data lifetimes according to Cubyz guidelines?
- Why are atomic values important in Cubyz's concurrency model?
- When should optional types (`?T`) be used instead of sentinel values?
- What is the stance on adding abstraction layers without a concrete need?
- How does Cubyz handle premature optimization and no measurable benefit objections?
- What is the recommended approach to naming and clarity in Cubyz code?
- Why are hardcoded limits with no documented reasoning flagged in Cubyz?
- How should resource acquisition be paired with cleanup in Cubyz functions?
- What is the correct idiom for handling allocators that structurally guarantee not to fail?

*Source: unknown | chunk_id: docs_CUBYZ_DEVELOPER_JUDGMENT.md_chunk_0*
