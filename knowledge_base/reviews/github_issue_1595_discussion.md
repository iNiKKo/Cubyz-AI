# [issues/issue_1595.md] - Issue #1595 discussion

**Type:** review
**Keywords:** allocator, formatting, memory allocation, API design, abstraction levels, separation of concerns, convenience, responsibility, interface clutter, hashmap, List, Tree
**Symbols:** allocator, print, allocPrint
**Concepts:** API design, abstraction levels, separation of concerns

## Summary
The discussion revolves around whether to add a formatting function directly to the allocator for convenience versus maintaining separation of concerns.

## Explanation
The maintainer argues against adding string formatting capabilities to the allocator, emphasizing that it is not the allocator's responsibility to handle such tasks. The maintainer believes this would blur the lines between different abstraction levels and clutter the allocator's interface. The user initially suggested integrating formatting into the allocator due to its typical position as the first argument in memory allocation operations but ultimately conceded to the maintainer's reasoning.

## Related Questions
- What are the potential drawbacks of adding string formatting to the allocator?
- How does the maintainer justify keeping formatting separate from memory allocation?
- Can you provide examples of other operations that should not be mixed with memory allocation in an allocator?
- Why is it important to maintain clear abstraction levels in software design?
- What are the benefits and drawbacks of convenience functions versus clean API design?
- How might integrating formatting into the allocator affect its performance or usability?

*Source: unknown | chunk_id: github_issue_1595_discussion*
