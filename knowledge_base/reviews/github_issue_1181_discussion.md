# [issues/issue_1181.md] - Issue #1181 discussion

**Type:** review
**Keywords:** Zig, managed, unmanaged, HashMaps, List, allocators, errors, reviews, default, renaming
**Symbols:** HashMap, utils.List, ListManaged
**Concepts:** data structures, memory management, code quality

## Summary
The discussion revolves around transitioning from managed to unmanaged data structures in Zig, specifically focusing on HashMaps and internal `utils.List`. The maintainer suggests renaming the current `List` to `ListManaged` while keeping managed lists for convenience.

## Explanation
The issue highlights the deprecation of managed variants of data structures in Zig 0.14.0, with plans to remove them in 0.15.0. The team is considering converting all usages of HashMaps and internal `utils.List` to their unmanaged counterparts. The maintainer argues that while unmanaged lists reduce reliance on explicit allocators, they can lead to more errors, especially across function interfaces, making mistakes harder to spot in reviews. Despite this, the maintainer supports making Unmanaged the default `List`, proposing to rename the current `List` to `ListManaged` to maintain both options.

## Related Questions
- What are the potential benefits of using unmanaged data structures in Zig?
- How might renaming `List` to `ListManaged` impact existing codebases?
- What specific mistakes are more likely with unmanaged lists across function interfaces?
- How does the deprecation of managed variants affect Cubyz's migration to Zig master?
- What is the timeline for transitioning to unmanaged data structures in Cubyz?
- How can we ensure that the transition to unmanaged data structures does not introduce new bugs?

*Source: unknown | chunk_id: github_issue_1181_discussion*
