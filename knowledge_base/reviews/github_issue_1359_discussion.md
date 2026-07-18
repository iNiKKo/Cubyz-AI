# [issues/issue_1359.md] - Issue #1359 discussion

**Type:** review
**Keywords:** garbage collection, ArenaAllocator, memory overhead, complexity, allocation, callback
**Symbols:** ArenaAllocator
**Concepts:** garbage collection, memory management, arena allocation

## Summary
Discussion about implementing a garbage collection system using an ArenaAllocator, with concerns about memory overhead and complexity.

## Explanation
The issue discusses the potential implementation of a garbage collection system in Cubyz, specifically using an ArenaAllocator. The proposal involves triggering garbage collection after a certain number of allocations and copying live pointers to a new arena. However, the maintainer decided against this approach, suggesting that it may not be as useful due to its complexity and memory overhead.

## Related Questions
- What is the primary concern with using ArenaAllocator for garbage collection?
- How does the proposed garbage collection system handle memory overhead?
- Why did the maintainer choose a different form of garbage collection in #1413?
- Can you explain how the ArenaAllocator works in this context?
- What are the potential benefits and drawbacks of using an ArenaAllocator for garbage collection?
- How does the proposed system ensure that all live pointers are correctly identified and copied?

*Source: unknown | chunk_id: github_issue_1359_discussion*
