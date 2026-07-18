# [issues/issue_1866.md] - Issue #1866 discussion

**Type:** review
**Keywords:** arena, allocator, memory management, performance, consolidation, live asset reloading
**Symbols:** globalArena, worldArena
**Concepts:** memory management, allocator design, performance optimization

## Summary
Proposes merging multiple memory arenas into a single `globalArena` and `worldArena` to simplify allocator usage and reduce inefficiencies.

## Explanation
The issue discusses the current state of multiple, separate memory arenas used in different parts of the application. The proposal aims to consolidate these into two primary allocators: one for global application use (`globalArena`) and another for world-specific data (`worldArena`). This change is intended to improve clarity regarding the purpose of each allocator and potentially enhance performance by reducing overhead associated with managing multiple arenas. The maintainer also notes that live asset reloading, which currently affects only a few assets (like block textures), does not require special handling within this new arena structure.

## Related Questions
- What are the current memory arenas being used in the application?
- How does the proposed consolidation of arenas aim to improve performance?
- Why is live asset reloading not a concern for the new arena structure?
- What potential issues might arise from consolidating multiple allocators into two?
- How will the change impact the maintainability and readability of the memory management code?
- Are there any specific use cases where the current separate arenas provide advantages over a unified approach?

*Source: unknown | chunk_id: github_issue_1866_discussion*
