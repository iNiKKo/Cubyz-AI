# [issues/issue_1595.md] - Issue #1595 discussion

**Type:** review
**Keywords:** allocator, formatting, memory allocation, API design, abstraction levels, separation of concerns, convenience, responsibility, interface clutter, hashmap, List, Tree
**Symbols:** allocator, print, allocPrint
**Concepts:** API design, abstraction levels, separation of concerns

## Summary
The discussion revolves around whether to add a formatting function directly to the allocator for convenience versus maintaining separation of concerns.

## Explanation
The discussion revolves around whether to add a formatting function directly to the allocator for convenience versus maintaining separation of concerns. The maintainer argues against adding string formatting capabilities to the allocator, emphasizing that it is not the allocator's responsibility to handle such tasks. Specifically, the maintainer notes that an allocator should only manage memory allocation and deallocation, not perform operations like string formatting or create data structures such as hashmaps, lists, or trees. The user initially suggested integrating formatting into the allocator due to its typical position as the first argument in memory allocation operations but ultimately conceded to the maintainer's reasoning.

## Related Questions
- What are the potential drawbacks of adding string formatting to the allocator?
- How does the maintainer justify keeping formatting separate from memory allocation?
- Can you provide examples of other operations that should not be mixed with memory allocation in an allocator (e.g., creating hashmaps, lists, or trees)?
- Why is it important to maintain clear abstraction levels in software design?

*Source: unknown | chunk_id: github_issue_1595_discussion*
